"""Prepare blind, host-neutral exercises and score independently judged responses.

No model APIs, credentials or network are used. Scoring validates evidence
identity and rubric completeness; a human/model judge supplies semantic decisions.
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "evaluations/suite.json"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("evaluation_audit_tools", ROOT / "skills/academic-paper-audit/scripts/audit_tools.py")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_path(relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("Evaluation inputs must be project-relative without parent traversal")
    resolved = (ROOT / path).resolve(strict=True)
    if not resolved.is_relative_to(ROOT) or not resolved.is_file():
        raise ValueError("Evaluation input must be a file within the project")
    current = ROOT
    for part in path.parts:
        current = current / part
        if current.is_symlink() or getattr(current.lstat(), "st_file_attributes", 0) & 0x400:
            raise ValueError("Linked/reparse evaluation inputs are not accepted")
    return resolved


def load_suite():
    suite = AUDIT.load_json(SUITE)
    errors = AUDIT.schema_errors(suite, ROOT / "evaluations/suite.schema.json")
    if errors:
        raise ValueError("Invalid evaluation suite: " + "; ".join(errors))
    ids = []
    for case in suite["cases"]:
        if not re.fullmatch(r"R\d{2}", case["id"]):
            raise ValueError("Case IDs must have the form R01")
        ids.append(case["id"])
        if case["expected_outcome"] not in ("concern", "clean", "insufficient_evidence", "resolved"):
            raise ValueError("Invalid expected case outcome")
        if not case["inputs"]:
            raise ValueError("Every case requires explicit input data")
        checks = suite["common_checks"] + case["checks"]
        if len({item["id"] for item in checks}) != len(checks):
            raise ValueError("Duplicate rubric check IDs")
        if any(not item["requirement"].strip() for item in checks):
            raise ValueError("Empty rubric requirement")
        render_case(case)
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate evaluation case IDs")
    if not {"concern", "clean", "insufficient_evidence", "resolved"}.issubset({case["expected_outcome"] for case in suite["cases"]}):
        raise ValueError("Suite must include concern, clean, insufficient and resolved cases")
    return suite


def render_case(case):
    parts = [f"# Case {case['id']}", "Screen only the supplied material. This exercise is independent of other cases. Use the supplied protocol in English, keep the report concise (target 220 words), and state actual coverage and limitations. Do not browse, upload, contact people, invent evidence or assume original research artifacts were supplied. Tools are optional; disclose what actually ran."]
    for item in case["inputs"]:
        text = source_path(item["path"]).read_text(encoding="utf-8")
        section = item.get("section")
        if section is not None:
            matches = list(re.finditer(r"^## (.+)$", text, re.MULTILINE))
            selected = [(i, match) for i, match in enumerate(matches) if match.group(1).split(":", 1)[0] == section]
            if len(selected) != 1:
                raise ValueError(f"Missing/ambiguous fixture section: {section}")
            index, match = selected[0]
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            text = text[match.start():end].strip()
        parts.extend([f"## Supplied material: {item['path']}" + (f" / {section}" if section else ""), text])
    return "\n\n".join(parts) + "\n"


def protocol_sources(variant):
    if variant == "quick":
        return {"QUICKSTART.md": source_path("QUICKSTART.md")}
    if variant == "master":
        return {"master_prompt.md": source_path("master_prompt.md")}
    if variant == "skill":
        release = load_module("evaluation_release", ROOT / "scripts/build_release.py")
        return {path.relative_to(ROOT).as_posix(): path for path in release.release_members("skill").values()}
    raise ValueError("Unknown protocol variant")


def packet_instructions(variant):
    instruction = "Read the selected protocol only, then review each cases/Rxx.md independently. Save one English Markdown response per case using the same Rxx.md filename. Do not read suite.json, expected results, evaluation documentation or prior responses. Use only the packet's research material, and do not browse or claim unsupported operations. For continuation input, carry prior IDs/status without treating the record as fresh evidence.\n"
    if variant == "quick":
        instruction += "Use the copyable text request in protocol/QUICKSTART.md; do not substitute the full master or skill.\n"
    elif variant == "skill":
        instruction += "Read protocol/skills/academic-paper-audit/SKILL.md and the linked resources that are relevant. Native installation is not part of this exercise.\n"
    else:
        instruction += "Use protocol/master_prompt.md; the explicit case request overrides its defaults.\n"
    return instruction


def prepare(variant, destination):
    suite = load_suite()
    sources = protocol_sources(variant)
    cases = {case["id"]: render_case(case) for case in suite["cases"]}
    manifest = {
        "suite_id": suite["id"], "suite_sha256": digest(SUITE.read_bytes()), "variant": variant,
        "protocol_hashes": {name: digest(path.read_bytes()) for name, path in sources.items()},
        "input_hashes": {name: digest(text.encode("utf-8")) for name, text in cases.items()},
    }
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    (destination / "cases").mkdir()
    for case_id, text in cases.items():
        (destination / "cases" / f"{case_id}.md").write_text(text, encoding="utf-8", newline="\n")
    for name, path in sources.items():
        target = destination / "protocol" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
    (destination / "instructions.md").write_text(packet_instructions(variant), encoding="utf-8", newline="\n")
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    return manifest


def validate_run(run):
    errors = AUDIT.schema_errors(run, ROOT / "evaluations/run.schema.json")
    if errors:
        return errors
    suite = load_suite()
    if run["suite_id"] != suite["id"] or run["suite_sha256"] != digest(SUITE.read_bytes()):
        errors.append("Run does not match the current evaluation suite")
    sources = protocol_sources(run["variant"])
    expected_protocol = {name: digest(path.read_bytes()) for name, path in sources.items()}
    if run["protocol_hashes"] != expected_protocol:
        errors.append("Protocol snapshot is stale or incomplete")
    expected_inputs = {case["id"]: digest(render_case(case).encode("utf-8")) for case in suite["cases"]}
    if run["input_hashes"] != expected_inputs:
        errors.append("Case evidence snapshot is stale or incomplete")
    responses = {item["case_id"]: item for item in run["responses"]}
    judgements = {item["case_id"]: item for item in run["judgements"]}
    case_ids = set(expected_inputs)
    if set(responses) != case_ids or len(responses) != len(run["responses"]):
        errors.append("Responses must include every case exactly once")
    if set(judgements) != case_ids or len(judgements) != len(run["judgements"]):
        errors.append("Judgements must include every case exactly once")
    for case in suite["cases"]:
        response = responses.get(case["id"])
        judgement = judgements.get(case["id"])
        if not response or not judgement:
            continue
        if response["sha256"] != digest(response["text"].encode("utf-8")):
            errors.append(f"{case['id']}: response digest mismatch")
        required = {item["id"] for item in suite["common_checks"] + case["checks"]}
        checks = {item["id"]: item for item in judgement["checks"]}
        if set(checks) != required or len(checks) != len(judgement["checks"]):
            errors.append(f"{case['id']}: every rubric check must be judged exactly once")
        for item in judgement["checks"]:
            if item["quote"] is not None and item["quote"] not in response["text"]:
                errors.append(f"{case['id']}/{item['id']}: quote is absent from response")
            if item["status"] == "pass" and item["quote"] is None:
                errors.append(f"{case['id']}/{item['id']}: a passing check needs an actual response excerpt")
    return errors


def score(run):
    errors = validate_run(run)
    if errors:
        raise ValueError("Invalid evaluation run: " + "; ".join(errors))
    suite = load_suite()
    judgements = {item["case_id"]: item for item in run["judgements"]}
    counts = Counter()
    cases = []
    for case in suite["cases"]:
        judgement = judgements[case["id"]]
        counts.update(item["status"] for item in judgement["checks"])
        matched = judgement["observed_outcome"] == case["expected_outcome"]
        passed = matched and all(item["status"] == "pass" for item in judgement["checks"])
        cases.append({"id": case["id"], "expected": case["expected_outcome"], "observed": judgement["observed_outcome"], "passed": passed})
    return {
        "suite_id": suite["id"], "variant": run["variant"], "host": run["host"], "model": run["model"],
        "cases_passed": sum(case["passed"] for case in cases), "cases_total": len(cases),
        "checks_passed": counts["pass"], "checks_failed": counts["fail"], "checks_not_assessed": counts["not_assessed"],
        "all_passed": all(case["passed"] for case in cases), "cases": cases,
        "limitation": "Synthetic rubric acceptance based on the named judge, not measured scientific accuracy, independent expert adjudication or cross-provider certification.",
    }


def assemble(packet, responses_directory, judgements_path, host, model, judge, output):
    manifest = AUDIT.load_json(Path(packet) / "manifest.json")
    if not isinstance(manifest, dict):
        raise ValueError("Packet manifest must be an object")
    suite = load_suite()
    sources = protocol_sources(manifest.get("variant"))
    expected = {
        "suite_id": suite["id"], "suite_sha256": digest(SUITE.read_bytes()), "variant": manifest["variant"],
        "protocol_hashes": {name: digest(path.read_bytes()) for name, path in sources.items()},
        "input_hashes": {case["id"]: digest(render_case(case).encode("utf-8")) for case in suite["cases"]},
    }
    if manifest != expected:
        raise ValueError("Packet manifest is stale or altered; no responses were read")
    # The manifest alone cannot establish which bytes the responder received.
    packet_root = Path(packet).resolve(strict=True)
    packet_files = {f"protocol/{name}": path.read_bytes() for name, path in sources.items()}
    packet_files.update({f"cases/{case['id']}.md": render_case(case).encode("utf-8") for case in suite["cases"]})
    packet_files["instructions.md"] = packet_instructions(manifest["variant"]).encode("utf-8")
    for name, expected_bytes in packet_files.items():
        path = packet_root / name
        if path.is_symlink() or not path.resolve(strict=True).is_relative_to(packet_root):
            raise ValueError("Linked or escaping packet file; no responses were read")
        if getattr(path.lstat(), "st_file_attributes", 0) & 0x400 or path.read_bytes() != expected_bytes:
            raise ValueError(f"Packet file altered: {name}; no responses were read")
    responses = []
    responses_root = Path(responses_directory).resolve(strict=True)
    for case_id in manifest["input_hashes"]:
        response_path = responses_root / f"{case_id}.md"
        if response_path.is_symlink() or not response_path.resolve(strict=True).is_relative_to(responses_root):
            raise ValueError("Linked or escaping response file")
        if getattr(response_path.lstat(), "st_file_attributes", 0) & 0x400:
            raise ValueError("Reparse response file")
        text = response_path.read_text(encoding="utf-8")
        responses.append({"case_id": case_id, "text": text, "sha256": digest(text.encode("utf-8"))})
    run = {"schema_version": "0.0.1", **manifest, "recorded_at": datetime.now(timezone.utc).isoformat(),
           "host": host, "model": model, "judge": judge, "responses": responses,
           "judgements": AUDIT.load_json(judgements_path)}
    errors = validate_run(run)
    if errors:
        raise ValueError("Cannot assemble run: " + "; ".join(errors))
    with Path(output).open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(run, handle, indent=2, ensure_ascii=False, allow_nan=False)
        handle.write("\n")
    return score(run)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare_command = commands.add_parser("prepare", help="Create a new blind packet without expected answers")
    prepare_command.add_argument("--variant", choices=("quick", "master", "skill"), required=True)
    prepare_command.add_argument("--output-dir", type=Path, required=True)
    score_command = commands.add_parser("score", help="Validate and score a judged run")
    score_command.add_argument("run", type=Path)
    assemble_command = commands.add_parser("assemble", help="Bind raw responses and independent judgements to a packet")
    for name in ("packet", "responses", "judgements", "output"):
        assemble_command.add_argument(f"--{name}", type=Path, required=True)
    assemble_command.add_argument("--host", required=True)
    assemble_command.add_argument("--model")
    assemble_command.add_argument("--judge", required=True)
    assemble_command.add_argument("--judge-kind", choices=("human", "model"), required=True)
    assemble_command.add_argument("--judge-notes", required=True)
    compare_command = commands.add_parser("compare", help="Compare complete runs without treating missing checks as passing")
    compare_command.add_argument("runs", type=Path, nargs="+")
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            manifest = prepare(args.variant, args.output_dir)
            print(f"Prepared {len(manifest['input_hashes'])} blind cases for {args.variant}.")
            return 0
        if args.command == "assemble":
            result = assemble(args.packet, args.responses, args.judgements, args.host, args.model,
                              {"identity": args.judge, "kind": args.judge_kind, "notes": args.judge_notes}, args.output)
        elif args.command == "score":
            result = score(AUDIT.load_json(args.run))
        else:
            summaries = [score(AUDIT.load_json(path)) for path in args.runs]
            identities = [(item["variant"], item["host"], item["model"]) for item in summaries]
            if len(identities) != len(set(identities)):
                raise ValueError("Comparison contains duplicate variant/host/model runs")
            result = {"runs": summaries, "all_passed": all(item["all_passed"] for item in summaries),
                      "complete_variant_comparison": {item["variant"] for item in summaries} == {"quick", "master", "skill"}}
        print(json.dumps(result, indent=2, ensure_ascii=True))
        return 0 if result["all_passed"] else 1
    except (OSError, ValueError, KeyError, TypeError, RecursionError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
