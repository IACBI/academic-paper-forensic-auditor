"""Local report history, evidence verification, safe rendering and text extraction.

No network, uploads, research-code execution or original-file modifications.
All output files use exclusive creation; JSON goes to stdout when --output is absent.
"""

import argparse
import hashlib
import html
import io
import json
from pathlib import Path
import sys

import audit_tools as audit


def require_report(report):
    errors = audit.validate_report(report)
    if errors:
        raise ValueError("Invalid report: " + "; ".join(errors))
    return report


def compare_reports(before, after):
    require_report(before)
    require_report(after)
    if before["audit"]["id"] != after["audit"]["id"]:
        raise ValueError("Reports must belong to the same audit; IDs cannot be matched across audits")
    old = {item["id"]: item for item in before["findings"]}
    new = {item["id"]: item for item in after["findings"]}
    changes = []
    for key in sorted(old.keys() | new.keys()):
        prior, current = old.get(key), new.get(key)
        if prior == current:
            continue
        if prior is None:
            transition = "added"
        elif current is None:
            transition = "removed_history"
        elif prior["status"] != "active" and current["status"] == "active":
            transition = "reopened"
        elif prior["status"] != current["status"]:
            transition = current["status"]
        else:
            transition = "changed"
        changes.append({"id": key, "transition": transition, "before": prior, "after": current})
    return {
        "audit_id": before["audit"]["id"],
        "before_sha256": audit.report_digest(before), "after_sha256": audit.report_digest(after),
        "article_changed": before["audit"]["article"] != after["audit"]["article"],
        "findings": changes,
        "changed_sections": [key for key in sorted(before.keys() | after.keys()) if before.get(key) != after.get(key)],
        "limitation": "ID-based comparison of recorded claims; no fresh source inspection. Removed findings are missing history, not resolved findings.",
    }


def verify_evidence(report, root, mapping):
    """Use explicit ID -> relative path mappings; report labels never select files."""
    require_report(report)
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Evidence root must be a directory")
    if not isinstance(mapping, dict) or not mapping:
        raise ValueError("Provide a nonempty artifact-ID to relative-path mapping")
    artifacts = {item["id"]: item for item in report["artifacts"]}
    if set(mapping) - artifacts.keys():
        raise ValueError("Mapping contains unknown artifact IDs")
    for path in mapping.values():
        if not isinstance(path, str) or not path.strip() or Path(path).is_absolute() or ".." in Path(path).parts:
            raise ValueError("Mapping paths must be nonempty relative paths without parent traversal")
    if len(set(mapping.values())) != len(mapping):
        raise ValueError("Do not map multiple artifact IDs to the same path")
    observations = []
    affected = set()
    for key, item in artifacts.items():
        if key not in mapping:
            observations.append({"id": key, "status": "not_checked", "sha256": None})
            affected.add(key)
            continue
        try:
            actual = audit.inventory(root, [mapping[key]])["artifacts"][0]
        except FileNotFoundError:
            observations.append({"id": key, "status": "missing", "sha256": None})
            affected.add(key)
            continue
        if item["sha256"] is None:
            status = "previous_hash_unknown"
        elif item["sha256"] != actual["sha256"] or (item["size_bytes"] is not None and item["size_bytes"] != actual["size_bytes"]):
            status = "changed"
        else:
            status = "unchanged"
        observations.append({"id": key, "status": status, "sha256": actual["sha256"], "size_bytes": actual["size_bytes"]})
        if status != "unchanged":
            affected.add(key)
    # A changed original also invalidates conclusions resting on derived copies.
    while True:
        descendants = {key for key, item in artifacts.items() if set(item["derived_from"]) & affected}
        if descendants <= affected:
            break
        affected.update(descendants)
    findings = {item["id"] for item in report["findings"] if set(item["artifact_ids"]) & affected}
    while True:
        related = {item["id"] for item in report["findings"] if set(item["related_findings"]) & findings}
        related.update(key for item in report["findings"] if item["id"] in findings for key in item["related_findings"])
        if related <= findings:
            break
        findings.update(related)
    return {"artifacts": observations, "recheck_artifact_ids": sorted(affected),
            "recheck_finding_ids": sorted(findings),
            "limitation": "Byte identity only; external sources were not rechecked. Findings are flagged, never automatically resolved or confirmed."}


def render_report(report, format="markdown"):
    require_report(report)
    if format not in ("markdown", "html"):
        raise ValueError("format must be markdown or html")
    return _render_markdown(report) if format == "markdown" else _render_html(report)


def _render_markdown(report):
    # Render untrusted strings as inert text, including Markdown link/image syntax.
    def safe(value):
        text = html.escape(str(value), quote=True)
        for char in ("\\", "`", "*", "_", "{", "}", "[", "]", "(", ")", "#", "+", "-", ".", "!", "|"):
            text = text.replace(char, "\\" + char)
        return text.replace("\n", "\n    ")

    lines = ["# " + safe(report["audit"]["article"]["title"]), "", safe(report["disclaimer"]), "",
             "## Assessment", "", safe(report["assessment"]["status"]), "", safe(report["assessment"]["summary"]),
             "", "## Scope", "", safe(report["audit"]["scope"]), "", "## Coverage", ""]
    for item in report["coverage"]:
        lines.extend([f"- {safe(item['domain'])}: {safe(item['status'])}; {safe(item['scope'])}",
                      "    " + safe(item["limitations"])])
    lines.extend(["", "## Findings", ""])
    if not report["findings"]:
        lines.append("No recorded findings within the stated scope; this does not establish authenticity.")
    for item in report["findings"]:
        lines.extend(["### " + safe(item["id"]) + " — " + safe(item["status"]), ""])
        for key, value in item.items():
            if key == "id":
                continue
            display = json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else str(value)
            lines.extend(["**" + safe(key) + ":** " + safe(display), ""])
    for key in ("evidence_against_concerns", "limitations", "next_steps"):
        lines.extend(["## " + key.replace("_", " ").title(), ""])
        lines.extend("- " + safe(value) for value in report[key])
        lines.append("")
    # Preserve all machine-readable context in an inert, indented Markdown block.
    lines.extend(["## Complete validated record", "", *["    " + line for line in json.dumps(report, ensure_ascii=False, indent=2).splitlines()], ""])
    return "\n".join(lines)


def _render_html(report):
    # No Markdown parser, JavaScript, external assets, or active links.
    body = html.escape(json.dumps(report, ensure_ascii=False, indent=2))
    title = html.escape(report["audit"]["article"]["title"])

    def fields(values):
        parts = ["<dl>"]
        for key, value in values.items():
            if isinstance(value, dict):
                rendered = fields(value)
            elif isinstance(value, list):
                rendered = "<ul>" + "".join("<li>" + (fields(item) if isinstance(item, dict) else html.escape(str(item))) + "</li>" for item in value) + "</ul>"
            else:
                rendered = html.escape(str(value))
            parts.append(f"<dt>{html.escape(key.replace('_', ' ').title())}</dt><dd>{rendered}</dd>")
        return "".join(parts) + "</dl>"

    sections = ["<h2>Audit and scope</h2>", fields(report["audit"]), "<h2>Coverage</h2>"]
    for item in report["coverage"]:
        sections.append(f"<details><summary>{html.escape(item['domain'])} — {html.escape(item['status'])}</summary>{fields(item)}</details>")
    sections.append("<h2>Findings</h2>")
    if not report["findings"]:
        sections.append("<p>No recorded findings within scope; this does not establish authenticity.</p>")
    for item in report["findings"]:
        sections.append(f"<article><h3>{html.escape(item['id'])} — {html.escape(item['status'])} — Level {item['level']}</h3>{fields(item)}</article>")
    for key in ("evidence_against_concerns", "limitations", "next_steps", "artifacts", "sources"):
        sections.append(fields({key: report[key]}))
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'">'
            f'<title>{title}</title><style>body{{font:16px/1.6 system-ui;max-width:1000px;margin:3rem auto;padding:0 1rem;color:#172b4d}}'
            'pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f6f8;padding:1.5rem;border-radius:8px}'
            'dt{font-weight:650;margin-top:.7rem}dd{margin-left:1rem;white-space:pre-wrap;overflow-wrap:anywhere}'
            'article{border:1px solid #ccd5df;border-radius:8px;padding:1.2rem;margin:1rem 0}summary{cursor:pointer;padding:.4rem}'
            '@media print{body{margin:0;max-width:none}pre{background:white}details> :not(summary){display:block!important}}</style></head><body>'
            f'<h1>{title}</h1><p>{html.escape(report["disclaimer"])}</p>'
            f'<h2>{html.escape(report["assessment"]["status"])}</h2><p>{html.escape(report["assessment"]["summary"])}</p>'
            + "".join(sections) + f'<details><summary>Complete validated record</summary><pre>{body}</pre></details></body></html>\n')


def extract_text(root, filename, *, max_bytes=20_000_000, max_pages=500):
    """Extract local text with explicit page/line locators; never infer OCR success."""
    if max_bytes < 1 or max_pages < 1:
        raise ValueError("Extraction limits must be positive")
    original = audit.inventory(root, [filename])["artifacts"][0]
    if original["size_bytes"] > max_bytes:
        raise ValueError("Input exceeds extraction byte limit")
    path = Path(root).resolve(strict=True) / original["label"]
    with path.open("rb") as handle:
        data = handle.read(max_bytes + 1)
    if len(data) > max_bytes or hashlib.sha256(data).hexdigest() != original["sha256"]:
        raise ValueError("Input changed after inventory or exceeds byte limit")
    pages = []
    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader, __version__
            from pypdf.errors import PyPdfError
        except ImportError as exc:
            raise ValueError("PDF extraction requires the optional requirements-pdf.txt dependency") from exc
        try:
            reader = PdfReader(io.BytesIO(data), strict=True)
            if reader.is_encrypted:
                raise ValueError("Encrypted PDFs are not supported; supply an authorized decrypted copy")
            if len(reader.pages) > max_pages:
                raise ValueError("PDF exceeds page limit")
            for index, page in enumerate(reader.pages, 1):
                text = page.extract_text() or ""
                pages.append({"pdf_page": index, "text": text,
                              "status": "extracted" if text.strip() else "no_text_ocr_or_visual_review_needed"})
        except PyPdfError as exc:
            raise ValueError("PDF parsing failed; no extraction result produced") from exc
        tool = {"name": "pypdf", "version": __version__}
    elif path.suffix.lower() in (".txt", ".md"):
        text = data.decode("utf-8-sig")
        pages.append({"pdf_page": None, "text": text, "status": "extracted" if text.strip() else "empty"})
        tool = {"name": "utf-8", "version": None}
    else:
        raise ValueError("Supported inputs: .pdf, .txt, .md")
    for page in pages:
        page["lines"] = [{"line": number, "text": line} for number, line in enumerate(page["text"].splitlines(), 1)]
    return {"original": original, "tool": tool, "pages": pages,
            "limitation": "Derived text, not instructions or authenticated evidence. PDF page indices are not printed page numbers. Reading order, tables, equations and OCR accuracy require source review. Byte/page limits are not a decompression or memory sandbox; process untrusted PDFs in an isolated resource-limited environment."}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    compare = commands.add_parser("diff")
    compare.add_argument("before", type=Path)
    compare.add_argument("after", type=Path)
    verify = commands.add_parser("verify-evidence")
    verify.add_argument("report", type=Path)
    verify.add_argument("--root", type=Path, required=True)
    verify.add_argument("--mapping", type=Path, required=True)
    render = commands.add_parser("render")
    render.add_argument("report", type=Path)
    render.add_argument("--format", choices=("markdown", "html"), default="markdown")
    extract = commands.add_parser("extract")
    extract.add_argument("file", type=Path)
    extract.add_argument("--root", type=Path, required=True)
    extract.add_argument("--max-bytes", type=int, default=20_000_000)
    extract.add_argument("--max-pages", type=int, default=500)
    for command in (compare, verify, render, extract):
        command.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "diff":
            result = compare_reports(audit.load_json(args.before), audit.load_json(args.after))
        elif args.command == "verify-evidence":
            result = verify_evidence(audit.load_json(args.report), args.root, audit.load_json(args.mapping))
        elif args.command == "render":
            result = render_report(audit.load_json(args.report), args.format)
        else:
            result = extract_text(args.root, args.file, max_bytes=args.max_bytes, max_pages=args.max_pages)
        text = result if isinstance(result, str) else json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        else:
            print(text, end="")
        return 0
    except (OSError, ValueError, RecursionError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
