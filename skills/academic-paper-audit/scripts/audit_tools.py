"""Local evidence inventory, conservative arithmetic and audit report validation.

No command performs network requests, executes submitted research code or edits
evidence. JSON results go to stdout; callers choose where to save them.
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import urlsplit

VERSION = "0.0.1"
DOMAINS = (
    "text_methods", "statistics_data", "figures_images", "metadata_provenance",
    "references_notices", "ethics_registration", "cross_paper",
)
SCHEMA = Path(__file__).resolve().parents[1] / "assets" / "report.schema.json"


def _nonnegative_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def percentage_check(count, total, reported, places):
    """Check an unweighted percentage using exact rational bounds, including ties."""
    _nonnegative_integer(count, "count")
    _nonnegative_integer(total, "total")
    _nonnegative_integer(places, "places")
    if total == 0 or count > total:
        raise ValueError("Require 0 <= count <= total and total > 0")
    if places > 12:
        raise ValueError("places must be between 0 and 12")
    try:
        raw = str(reported)
        if len(raw) > 100:
            raise ValueError("reported must be a decimal of at most 100 characters")
        number = Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError("reported must be a finite decimal") from exc
    if not number.is_finite() or not 0 <= number <= 100:
        raise ValueError("reported must be finite and between 0 and 100")
    if abs(number.as_tuple().exponent) > 100:
        raise ValueError("reported decimal exponent is outside supported bounds")
    value = Fraction(number)
    if (value * 10 ** places).denominator != 1:
        raise ValueError("reported has more precision than places permits")
    exact = Fraction(count * 100, total)
    tolerance = Fraction(1, 2 * 10 ** places)
    difference = abs(exact - value)
    return {
        "count": count, "total": total, "reported": str(number), "places": places,
        "exact_percentage_fraction": str(exact),
        "tolerance_percentage_points": str(tolerance),
        "absolute_difference_fraction": str(difference),
        "compatible": difference <= tolerance,
        "boundary_tie": difference == tolerance,
        "assumption": "Unweighted counts; nearest rounding; boundary ties accepted conservatively.",
        "limitation": "Does not establish the intended denominator, design, truncation rule or misconduct.",
    }


def flow_check(initial, excluded, dropouts, analyzed, *, disjoint=False):
    values = {"initial": initial, "excluded": excluded, "dropouts": dropouts, "analyzed": analyzed}
    for name, value in values.items():
        _nonnegative_integer(value, name)
    if not disjoint:
        raise ValueError("Confirm disjoint losses in the same population with --disjoint")
    if excluded + dropouts > initial or analyzed > initial:
        raise ValueError("Counts exceed the initial population under the disjoint assumption")
    expected = initial - excluded - dropouts
    return {
        **values, "expected_analyzed": expected, "difference": analyzed - expected,
        "reconciles": analyzed == expected,
        "assumption": "Exclusions and dropouts are disjoint and use the same population/timepoint.",
        "limitation": "Population definitions and overlapping losses must be checked in the source.",
    }


def _file_signature(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def inventory(root, files):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("root must be a directory")
    if not files:
        raise ValueError("Supply at least one explicit file")
    selected = {}
    for name in files:
        supplied = Path(name)
        candidate = supplied if supplied.is_absolute() else root / supplied
        # Reject symlinks/junctions in all components below the chosen root.
        lexical = Path(os.path.abspath(candidate))
        try:
            relative = lexical.relative_to(root)
        except ValueError as exc:
            raise ValueError("Evidence file is outside root") from exc
        current = root
        for part in relative.parts:
            current = current / part
            info = current.lstat()
            if current.is_symlink() or getattr(info, "st_file_attributes", 0) & 0x400:
                raise ValueError("Symlinks and reparse points are not accepted as evidence paths")
        path = lexical.resolve(strict=True)
        if not path.is_relative_to(root):
            raise ValueError("Evidence file resolves outside root")
        if not stat.S_ISREG(path.stat().st_mode):
            raise ValueError("Evidence inputs must be regular files")
        if path in selected:
            raise ValueError("The same evidence path was supplied more than once")
        selected[path] = relative.as_posix()
    artifacts = []
    for index, (path, label) in enumerate(sorted(selected.items(), key=lambda pair: pair[1]), 1):
        before = path.stat()
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            opened = os.fstat(handle.fileno())
            if _file_signature(before) != _file_signature(opened):
                raise ValueError("Evidence changed before hashing; retry on a stable copy")
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
            after = os.fstat(handle.fileno())
        if _file_signature(opened) != _file_signature(after) or _file_signature(after) != _file_signature(path.stat()):
            raise ValueError("Evidence changed while hashing; retry on a stable copy")
        artifacts.append({
            "id": f"A{index:03d}", "label": label, "kind": "original",
            "size_bytes": after.st_size, "sha256": digest.hexdigest(),
            "derived_from": [], "transformations": [], "limitation": "",
        })
    return {
        "package_version": VERSION,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": artifacts,
        "limitation": "Hashes identify observed bytes, not authenticity or legal chain of custody. IDs belong to this inventory; preserve existing audit IDs when merging.",
    }


def _unique_ids(items, name, errors):
    ids = [item["id"] for item in items]
    duplicates = sorted(value for value, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"Duplicate {name} IDs: {', '.join(duplicates)}")
    return set(ids)


def schema_errors(instance, schema_path):
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise ValueError("Validation requires jsonschema 4.26.0; install the skill's requirements.txt") from exc
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    checker = FormatChecker()

    @checker.checks("date-time", raises=(ValueError, TypeError))
    def timezone_timestamp(value):
        if not isinstance(value, str):
            return True
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})", value):
            return False
        if value[-1].upper() != "Z" and (int(value[-5:-3]) > 23 or int(value[-2:]) > 59):
            return False
        normalized = value.upper().replace("Z", "+00:00")
        parsed = datetime.fromisoformat(normalized)
        return parsed.utcoffset() is not None

    validator = Draft202012Validator(schema, format_checker=checker)
    errors = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: str(list(item.absolute_path))):
        location = "/".join(map(str, error.absolute_path)) or "$"
        errors.append(f"{location}: {error.message}")
    return errors


def validate_report(report):
    errors = schema_errors(report, SCHEMA)
    if errors:
        return errors
    artifacts = _unique_ids(report["artifacts"], "artifact", errors)
    sources = _unique_ids(report["sources"], "source", errors)
    findings = _unique_ids(report["findings"], "finding", errors)
    all_ids = [item["id"] for group in ("artifacts", "sources", "findings") for item in report[group]]
    if len(all_ids) != len(set(all_ids)):
        errors.append("IDs must also be unique across artifacts, sources and findings")
    coverage = {item["domain"]: item for item in report["coverage"]}
    if len(coverage) != len(DOMAINS) or set(coverage) != set(DOMAINS):
        errors.append("Coverage must contain each of the seven domains exactly once")
    source_by_id = {item["id"]: item for item in report["sources"]}
    artifact_by_id = {item["id"]: item for item in report["artifacts"]}
    for item in report["sources"]:
        if item["url"] is not None:
            try:
                parsed = urlsplit(item["url"])
                valid_url = parsed.scheme in ("http", "https") and parsed.hostname and not parsed.username and not parsed.password
                valid_url = valid_url and not any(char.isspace() for char in item["url"])
                # Accessing port also rejects non-numeric/out-of-range ports.
                parsed.port
            except ValueError:
                valid_url = False
            if not valid_url:
                errors.append(f"{item['id']}: source URL must be HTTP(S) with a host and no embedded credentials")
        if item["access_status"] != "read" and not item["limitations"].strip():
            errors.append(f"{item['id']}: incomplete source access requires limitations")

    def check_links(item, key, targets):
        unknown = set(item[key]) - targets
        if unknown:
            errors.append(f"{item.get('id', item.get('domain'))}: unknown {key}: {', '.join(sorted(unknown))}")

    def has_available_evidence(item):
        return bool(set(item["artifact_ids"]) & artifacts) or any(
            source_by_id[key]["access_status"] != "unavailable"
            for key in item["source_ids"] if key in source_by_id
        )

    for item in report["artifacts"]:
        check_links(item, "derived_from", artifacts)
        if item["kind"] == "original" and (item["derived_from"] or item["transformations"]):
            errors.append(f"{item['id']}: original artifact cannot have derivation history")
        if item["kind"] == "derived" and (not item["derived_from"] or not item["transformations"]):
            errors.append(f"{item['id']}: derived artifact requires parent IDs and transformations")
        if (item["sha256"] is None or item["size_bytes"] is None) and not item["limitation"].strip():
            errors.append(f"{item['id']}: unavailable size/hash requires a limitation")

    # Iterative topological traversal detects cycles without recursion limits.
    pending = {key: set(value["derived_from"]) & artifacts for key, value in artifact_by_id.items()}
    while pending:
        ready = {key for key, parents in pending.items() if not parents}
        if not ready:
            errors.append("Artifact derivation contains a cycle")
            break
        pending = {key: parents - ready for key, parents in pending.items() if key not in ready}

    assessed = set()
    for item in report["coverage"]:
        check_links(item, "artifact_ids", artifacts)
        check_links(item, "source_ids", sources)
        if item["status"] in ("completed", "partial"):
            assessed.add(item["domain"])
            if not item["artifact_ids"] and not item["source_ids"]:
                errors.append(f"{item['domain']}: assessed scope requires evidence references")
            elif not has_available_evidence(item):
                errors.append(f"{item['domain']}: unavailable sources alone cannot establish assessed evidence")
    active = [item for item in report["findings"] if item["status"] == "active"]
    for item in report["findings"]:
        check_links(item, "artifact_ids", artifacts)
        check_links(item, "source_ids", sources)
        check_links(item, "related_findings", findings)
        if item["id"] in item["related_findings"]:
            errors.append(f"{item['id']}: finding cannot relate to itself")
        if not item["artifact_ids"] and not item["source_ids"]:
            errors.append(f"{item['id']}: finding requires evidence references")
        if item["status"] == "active":
            if not has_available_evidence(item):
                errors.append(f"{item['id']}: active finding requires available evidence")
            if item["category"] not in assessed:
                errors.append(f"{item['id']}: active finding requires assessed domain coverage")
            if item["self_challenge"]["outcome"] == "resolved":
                errors.append(f"{item['id']}: resolved challenge cannot remain active")
            if item["level"] in (2, 3):
                if item["self_challenge"]["outcome"] == "not_performed":
                    errors.append(f"{item['id']}: Level 2/3 requires a completed self-challenge")
                if not item["human_review_required"]:
                    errors.append(f"{item['id']}: Level 2/3 requires independent human review")
        if item["level"] == 4:
            corroboration = [source_by_id[key] for key in item["source_ids"] if key in source_by_id]
            if not any(s["authoritative"] and s["article_match"] and s["access_status"] == "read" for s in corroboration):
                errors.append(f"{item['id']}: Level 4 requires a read authoritative article-matched source")
    status = report["assessment"]["status"]
    if not assessed and status != "insufficient_evidence":
        errors.append("No assessed evidence: assessment must be insufficient_evidence")
    if status == "no_significant_anomaly" and any(item["level"] >= 2 for item in active):
        errors.append("Assessment contradicts active Level 2+ findings")
    if status == "minor_anomalies" and any(item["level"] >= 2 for item in active):
        errors.append("Minor assessment contradicts active Level 2+ findings")
    if status == "externally_documented_issue" and not any(item["level"] == 4 for item in active):
        errors.append("Externally documented assessment requires an active Level 4 finding")
    if status in ("minor_anomalies", "clarification_required", "expert_review_required") and not active:
        errors.append("Anomaly assessment requires at least one active finding")
    if status != "insufficient_evidence" and any(item["level"] == 4 for item in active) and status != "externally_documented_issue":
        errors.append("Active Level 4 finding requires externally_documented_issue assessment")
    return errors


def validate_checkpoint(checkpoint):
    errors = schema_errors(checkpoint, SCHEMA.with_name("checkpoint.schema.json"))
    if errors:
        return errors
    artifacts = _unique_ids(checkpoint["artifacts"], "artifact", errors)
    sources = _unique_ids(checkpoint["sources"], "source", errors)
    _unique_ids(checkpoint["findings"], "finding", errors)
    _unique_ids(checkpoint["completed_checks"], "completed check", errors)
    all_ids = [item["id"] for group in ("artifacts", "sources", "findings", "completed_checks") for item in checkpoint[group]]
    if len(all_ids) != len(set(all_ids)):
        errors.append("Checkpoint IDs must be unique across registries")
    coverage = {item["domain"]: item for item in checkpoint["coverage"]}
    if len(coverage) != len(DOMAINS) or set(coverage) != set(DOMAINS):
        errors.append("Checkpoint coverage must contain each of the seven domains exactly once")
    for group in ("completed_checks", "findings"):
        for item in checkpoint[group]:
            for key, targets in (("artifact_ids", artifacts), ("source_ids", sources)):
                if set(item[key]) - targets:
                    errors.append(f"{item['id']}: unknown {key}")
            if not item["artifact_ids"] and not item["source_ids"]:
                errors.append(f"{item['id']}: checkpoint entry requires evidence references")
    for item in checkpoint["findings"]:
        if item["status"] == "active" and coverage.get(item["category"], {}).get("status") not in ("completed", "partial"):
            errors.append(f"{item['id']}: active finding requires assessed coverage")
    if checkpoint["last_observed_at"] is None or any(item["sha256"] is None for item in checkpoint["artifacts"]):
        if not checkpoint["limitations"]:
            errors.append("Unknown checkpoint time/hash requires explicit limitations")
    return errors


def checkpoint_from_report(report):
    errors = validate_report(report)
    if errors:
        raise ValueError("Cannot checkpoint invalid report: " + "; ".join(errors))
    checks = []
    for domain in report["coverage"]:
        for description in domain["checks"]:
            checks.append({
                "id": f"CHECK_{len(checks) + 1:03d}", "description": description,
                "artifact_ids": list(domain["artifact_ids"]), "source_ids": list(domain["source_ids"]),
            })
    # Generated check IDs must not collide with user-assigned evidence/finding IDs.
    used_ids = {item["id"] for group in ("artifacts", "sources", "findings") for item in report[group]}
    for item in checks:
        base = item["id"]
        suffix = 1
        while item["id"] in used_ids:
            item["id"] = f"{base}_{suffix}"
            suffix += 1
        used_ids.add(item["id"])
    checkpoint = {
        "schema_version": VERSION, "audit_id": report["audit"]["id"], "protocol_version": VERSION,
        "article": dict(report["audit"]["article"]), "scope": report["audit"]["scope"],
        "last_observed_at": report["audit"]["created_at"],
        "artifacts": [{key: item[key] for key in ("id", "label", "sha256")} for item in report["artifacts"]],
        "sources": [{"id": item["id"], "identifier": item["url"] or item["identifier"],
                     "verification_notes": f"Prior source record: {item['access_status']}; {item['statement']} Limitations: {item['limitations']}"} for item in report["sources"]],
        "coverage": [{key: item[key] for key in ("domain", "status", "scope")} for item in report["coverage"]],
        "completed_checks": checks,
        "findings": [{**{key: item[key] for key in ("id", "category", "status", "level", "observation", "locator")},
                      "artifact_ids": list(item["artifact_ids"]), "source_ids": list(item["source_ids"]),
                      "verification_notes": f"{item['self_challenge']['outcome']}: {item['self_challenge']['details']} Next: {item['verification_needed']}"} for item in report["findings"]],
        "pending_steps": list(report["next_steps"]),
        "limitations": list(report["limitations"]) + ["Summary of a prior report; no new source inspection, clock observation or authentication was performed. Recheck identity and changed evidence before resuming."],
    }
    errors = validate_checkpoint(checkpoint)
    if errors:
        raise ValueError("Checkpoint conversion failed: " + "; ".join(errors))
    return checkpoint


def load_json(path):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"Non-finite JSON value: {value}")

    def finite_float(value):
        result = float(value)
        if not math.isfinite(result):
            raise ValueError("JSON numeric value exceeds finite floating-point range")
        return result

    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object, parse_constant=reject_constant, parse_float=finite_float)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    files = subparsers.add_parser("inventory", help="Hash explicit regular files inside an evidence root")
    files.add_argument("--root", type=Path, required=True)
    files.add_argument("files", nargs="+", type=Path)
    percent = subparsers.add_parser("percentage", help="Check rounding compatibility for unweighted counts")
    percent.add_argument("--count", type=int, required=True)
    percent.add_argument("--total", type=int, required=True)
    percent.add_argument("--reported", required=True)
    percent.add_argument("--places", type=int, required=True)
    flow = subparsers.add_parser("flow", help="Reconcile disjoint participant losses")
    for name in ("initial", "excluded", "dropouts", "analyzed"):
        flow.add_argument(f"--{name}", type=int, required=True)
    flow.add_argument("--disjoint", action="store_true")
    validate = subparsers.add_parser("validate-report", help="Validate schema and evidence cross-references")
    validate.add_argument("report", type=Path)
    checkpoint = subparsers.add_parser("checkpoint", help="Convert a valid report into a continuation record")
    checkpoint.add_argument("report", type=Path)
    resume = subparsers.add_parser("validate-checkpoint", help="Validate a continuation record without executing it")
    resume.add_argument("checkpoint", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "inventory":
            result = inventory(args.root, args.files)
        elif args.command == "percentage":
            result = percentage_check(args.count, args.total, args.reported, args.places)
        elif args.command == "flow":
            result = flow_check(args.initial, args.excluded, args.dropouts, args.analyzed, disjoint=args.disjoint)
        elif args.command == "checkpoint":
            result = checkpoint_from_report(load_json(args.report))
        elif args.command == "validate-checkpoint":
            checkpoint = load_json(args.checkpoint)
            errors = validate_checkpoint(checkpoint)
            result = {"valid": not errors, "errors": errors,
                      "pending_steps": checkpoint["pending_steps"] if not errors else None}
            print(json.dumps(result, indent=2, ensure_ascii=True, allow_nan=False))
            return 1 if errors else 0
        else:
            report = load_json(args.report)
            errors = validate_report(report)
            counts = Counter(item["level"] for item in report["findings"] if item["status"] == "active") if not errors else {}
            result = {"valid": not errors, "errors": errors, "active_finding_counts": {str(level): counts.get(level, 0) for level in range(1, 5)} if not errors else None}
            print(json.dumps(result, indent=2, ensure_ascii=True, allow_nan=False))
            return 1 if errors else 0
    except (OSError, ValueError, RecursionError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
