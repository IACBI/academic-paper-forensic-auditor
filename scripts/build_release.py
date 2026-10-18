"""Build deterministic prompt, skill or optional plugin ZIPs from explicit files."""

import argparse
import hashlib
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "academic-paper-audit"
# New distributable files must be consciously added here. Never glob the workspace
# or include evidence, reports, environments, cache files or untracked secrets.
SKILL_FILES = (
    "SKILL.md", "requirements.txt",
    "assets/report-template.md", "assets/report.schema.json",
    "references/core.md", "references/manuscript.md", "references/statistics.md",
    "references/images.md", "references/report.md", "scripts/audit_tools.py",
    "references/methods.md", "references/portability.md",
)
ROOT_FILES = ("plugin.json", "LICENSE", "VERSION")
PROMPT_FILES = {
    "QUICKSTART.md": ROOT / "QUICKSTART.md",
    "master_prompt.md": ROOT / "master_prompt.md",
    "LICENSE": ROOT / "LICENSE",
    "report.schema.json": SKILL / "assets/report.schema.json",
    "report-template.md": SKILL / "assets/report-template.md",
}


def release_members(kind):
    members = {}
    if kind == "prompt":
        members.update(PROMPT_FILES)
    elif kind == "plugin":
        members.update({name: ROOT / name for name in ROOT_FILES})
        members.update({f"skills/academic-paper-audit/{name}": SKILL / name for name in SKILL_FILES})
    elif kind == "skill":
        members.update({f"academic-paper-audit/{name}": SKILL / name for name in SKILL_FILES})
        members["academic-paper-audit/LICENSE"] = ROOT / "LICENSE"
    else:
        raise ValueError("kind must be prompt, skill or plugin")
    for name, path in members.items():
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Release source missing or linked: {name}")
        if not path.resolve().is_relative_to(ROOT):
            raise ValueError(f"Release source escapes workspace: {name}")
        relative = path.relative_to(ROOT)
        current = ROOT
        for part in relative.parts:
            current = current / part
            if current.is_symlink() or getattr(current.lstat(), "st_file_attributes", 0) & 0x400:
                raise ValueError(f"Linked/reparse release source: {name}")
    return members


def write_archive(path, members):
    path = Path(path)
    # Exclusive creation protects pre-existing outputs and evidence from overwrite.
    with zipfile.ZipFile(path, mode="x", compression=zipfile.ZIP_STORED) as archive:
        for name, source in sorted(members.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    with path.open("rb") as handle:
        digest = hashlib.sha256()
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--format", choices=("prompt", "skill", "plugin", "all"), default="prompt")
    args = parser.parse_args()
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        parser.exit(2, "VERSION must be a numeric semantic version.\n")
    # Preflight all selected packages before creating output files.
    kinds = ("prompt", "skill", "plugin") if args.format == "all" else (args.format,)
    packages = {kind: release_members(kind) for kind in kinds}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    paths = {kind: args.output_dir / f"academic-paper-auditor-{kind}-{version}.zip" for kind in packages}
    if any(path.exists() for path in paths.values()):
        parser.exit(2, "Release files already exist; choose a new output directory.\n")
    for kind, members in packages.items():
        digest = write_archive(paths[kind], members)
        print(f"{digest}  {paths[kind].name}")


if __name__ == "__main__":
    main()
