"""Packaging must be reproducible and exclude arbitrary workspace contents."""

import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_release", ROOT / "scripts/build_release.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_identical_inputs_create_identical_archives(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source.txt"
            source.write_bytes(b"stable\n")
            first = root / "first.zip"
            second = root / "second.zip"
            one = release.write_archive(first, {"folder/source.txt": source})
            two = release.write_archive(second, {"folder/source.txt": source})
            self.assertEqual(one, two)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(one, hashlib.sha256(first.read_bytes()).hexdigest())

    def test_existing_archive_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / "existing.zip"
            output.write_bytes(b"keep this file")
            with self.assertRaises(FileExistsError):
                release.write_archive(output, {})
            self.assertEqual(output.read_bytes(), b"keep this file")

    def test_explicit_allowlist_excludes_secrets_reports_and_caches(self):
        with tempfile.TemporaryDirectory() as temp:
            # Windows TEMP may use an 8.3 alias; mirror the canonical runtime ROOT.
            root = Path(temp).resolve()
            skill = root / "skills/academic-paper-audit"
            for name in release.ROOT_FILES:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("release content", encoding="utf-8")
            for name in release.SKILL_FILES:
                path = skill / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("skill content", encoding="utf-8")
            for relative in [".env", "evidence/secret.pdf", "reports/private.json", "skills/academic-paper-audit/scripts/__pycache__/cache.pyc", "skills/academic-paper-audit/private.txt"]:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"must not ship")
            with patch.object(release, "ROOT", root), patch.object(release, "SKILL", skill):
                members = release.release_members("plugin")
                output = root / "release.zip"
                release.write_archive(output, members)
                with zipfile.ZipFile(output) as archive:
                    self.assertIn("plugin.json", archive.namelist())
                    self.assertIn("skills/academic-paper-audit/SKILL.md", archive.namelist())
                    self.assertFalse(any(b"must not ship" in archive.read(name) for name in archive.namelist()))
                standalone = release.release_members("skill")
                self.assertIn("academic-paper-audit/LICENSE", standalone)
                self.assertNotIn("plugin.json", standalone)

    def test_actual_package_sources_are_present(self):
        for kind in ("prompt", "skill", "plugin"):
            with self.subTest(kind=kind):
                members = release.release_members(kind)
                self.assertTrue(members)
                self.assertTrue(all(path.is_file() for path in members.values()))

    def test_prompt_needs_no_native_skill_or_vendor_metadata(self):
        members = release.release_members("prompt")
        self.assertIn("QUICKSTART.md", members)
        self.assertIn("master_prompt.md", members)
        self.assertFalse(any(name.endswith(".py") or "plugin.json" in name or "openai" in name for name in members))

    def test_skill_and_plugin_do_not_ship_developer_materials(self):
        for kind in ("skill", "plugin"):
            with self.subTest(kind=kind):
                members = release.release_members(kind)
                self.assertTrue(any(name.endswith("references/methods.md") for name in members))
                self.assertTrue(any(name.endswith("references/portability.md") for name in members))
                self.assertFalse(any(name.startswith(("tests/", "examples/", "docs/")) or "agents/openai.yaml" in name for name in members))

    def test_linked_sources_are_rejected(self):
        with patch.object(Path, "is_symlink", return_value=True):
            with self.assertRaisesRegex(ValueError, "linked"):
                release.release_members("skill")

    def test_default_cli_builds_only_the_portable_prompt_and_preserves_outputs(self):
        with tempfile.TemporaryDirectory() as temp:
            command = [sys.executable, str(ROOT / "scripts/build_release.py"), "--output-dir", temp]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            files = list(Path(temp).glob("*.zip"))
            self.assertEqual([path.name for path in files], ["academic-paper-auditor-prompt-0.0.1.zip"])
            original = files[0].read_bytes()
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(second.returncode, 2)
            self.assertEqual(files[0].read_bytes(), original)

    def test_all_formats_cli_keeps_their_boundaries(self):
        with tempfile.TemporaryDirectory() as temp:
            result = subprocess.run([sys.executable, str(ROOT / "scripts/build_release.py"), "--format", "all", "--output-dir", temp], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(list(Path(temp).glob("*.zip"))), 3)
            for kind in ("prompt", "skill", "plugin"):
                with zipfile.ZipFile(Path(temp) / f"academic-paper-auditor-{kind}-0.0.1.zip") as archive:
                    self.assertEqual(set(archive.namelist()), set(release.release_members(kind)))
                    self.assertIsNone(archive.testzip())


if __name__ == "__main__":
    unittest.main()
