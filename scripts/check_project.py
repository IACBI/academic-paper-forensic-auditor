"""Check release consistency and contracts without network access or mutations."""

import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "academic-paper-audit"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check():
    errors = []
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must be a numeric semantic version")
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    if manifest.get("version") != version:
        errors.append("Plugin version differs from VERSION")
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("Unexpected portable plugin schema declaration")
    if manifest.get("name") != "academic-paper-forensic-auditor":
        errors.append("Unexpected plugin name")
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if f'  version: "{version}"' not in skill_text:
        errors.append("Skill metadata version differs from VERSION")
    for name in ("README.md", "master_prompt.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        display_labels = (f"**Version:** v.{version}", f"![Version: v.{version}](")
        if not any(label in text for label in display_labels):
            errors.append(f"Display version differs in {name}")
    references = load_module("build_references", ROOT / "scripts/build_references.py")
    for path, expected in references.expected_references().items():
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            errors.append(f"Stale reference: {path.relative_to(ROOT)}")
    tool = load_module("audit_tools", SKILL / "scripts/audit_tools.py")
    if tool.VERSION != version:
        errors.append("Tool version differs from VERSION")
    schema = json.loads(tool.SCHEMA.read_text(encoding="utf-8"))
    if schema["properties"]["schema_version"].get("const") != version or schema["properties"]["audit"]["properties"]["package_version"].get("const") != version:
        errors.append("Report schema version differs from VERSION")
    example = tool.load_json(ROOT / "examples/synthetic-report.json")
    errors.extend(tool.validate_report(example))
    inventory = tool.inventory(ROOT / "tests/fixtures", ["synthetic_manuscript.md"])
    if inventory["artifacts"] != example["artifacts"]:
        errors.append("Synthetic example artifact identity differs from its fixture")
    checkpoint_schema = json.loads((SKILL / "assets/checkpoint.schema.json").read_text(encoding="utf-8"))
    if checkpoint_schema["properties"]["schema_version"].get("const") != version or checkpoint_schema["properties"]["protocol_version"].get("const") != version:
        errors.append("Continuation schema version differs from VERSION")
    checkpoint = tool.load_json(ROOT / "examples/synthetic-checkpoint.json")
    errors.extend(tool.validate_checkpoint(checkpoint))
    if checkpoint != tool.checkpoint_from_report(example):
        errors.append("Continuation example differs from its source report")
    evaluation = load_module("project_evaluation", ROOT / "scripts/evaluate.py")
    evaluation.load_suite()
    for variant in ("quick", "master", "skill"):
        baseline = ROOT / "evaluations" / f"baseline-{variant}.json"
        if not baseline.is_file():
            errors.append(f"Missing independent evaluation baseline: {variant}")
            continue
        run = tool.load_json(baseline)
        try:
            result = evaluation.score(run)
            if result["variant"] != variant:
                errors.append(f"Evaluation baseline has incorrect variant: {variant}")
            if not result["all_passed"]:
                errors.append(f"Synthetic acceptance failed for {variant}: {result['cases_passed']}/{result['cases_total']}")
        except ValueError as exc:
            errors.append(f"Evaluation baseline invalid for {variant}: {exc}")
    # Check linked local file paths. Fragment targets and external URLs are not
    # validated here, and real evidence/environments are never scanned.
    docs = [ROOT / "README.md", ROOT / "QUICKSTART.md", ROOT / "CONTRIBUTING.md", ROOT / "master_prompt.md", *sorted((ROOT / "docs").glob("*.md")), *sorted(SKILL.rglob("*.md"))]
    for doc in docs:
        for target in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if local and not (doc.parent / local).is_file():
                errors.append(f"Broken local link in {doc.relative_to(ROOT)}: {target}")
    release = load_module("build_release", ROOT / "scripts/build_release.py")
    for kind in ("prompt", "skill", "plugin"):
        release.release_members(kind)
    return errors


def main():
    try:
        errors = check()
    except (OSError, ValueError, KeyError) as exc:
        print(f"Project check failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=ROOT)
    if result.returncode:
        return result.returncode
    print("Project checks passed: versions, references, report/continuation contracts, example evidence, blind evaluation baselines, links, release inputs and tests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
