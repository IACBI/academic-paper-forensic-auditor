"""Detect policy loss when numbered source sections are changed or misrouted."""

import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_references", ROOT / "scripts/build_references.py")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class ReferenceTests(unittest.TestCase):
    def source(self):
        return "\n\n".join(f"# {number}. Topic {number}\nUnique policy {number}." for number in range(35))

    def generate(self, text, groups=None):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "master_prompt.md").write_text(text, encoding="utf-8")
            with patch.object(builder, "ROOT", root), patch.object(builder, "GROUPS", groups or builder.GROUPS):
                return builder.expected_references()

    def test_routes_every_policy_once(self):
        outputs = self.generate(self.source())
        joined = "\n".join(outputs.values())
        for number in range(35):
            self.assertEqual(joined.count(f"Unique policy {number}."), 1)

    def test_duplicate_source_section_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.generate(self.source() + "\n# 8. Shadow policy\nBad replacement")

    def test_missing_source_section_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "0 through 34"):
            self.generate(self.source().replace("# 8. Topic 8", "## Missing section"))

    def test_duplicate_routing_is_rejected(self):
        groups = {key: list(value) for key, value in builder.GROUPS.items()}
        groups["core"].append(33)
        with self.assertRaisesRegex(ValueError, "exactly once"):
            self.generate(self.source(), groups)


if __name__ == "__main__":
    unittest.main()
