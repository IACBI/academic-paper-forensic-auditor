"""Behavioral tests for arithmetic, evidence boundaries and report contracts."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "skills" / "academic-paper-audit" / "scripts" / "audit_tools.py"
SPEC = importlib.util.spec_from_file_location("audit_tools", TOOL)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)
EXAMPLE = ROOT / "examples" / "synthetic-report.json"


class ArithmeticTests(unittest.TestCase):
    def test_rounded_third_is_compatible(self):
        result = audit.percentage_check(1, 3, "33.3", 1)
        self.assertTrue(result["compatible"])
        self.assertEqual(result["exact_percentage_fraction"], "100/3")

    def test_mismatch_and_boundary(self):
        self.assertFalse(audit.percentage_check(1, 3, "33.4", 1)["compatible"])
        self.assertTrue(audit.percentage_check(1, 8, "12", 0)["boundary_tie"])
        self.assertTrue(audit.percentage_check(1, 8, "13", 0)["compatible"])

    def test_percentage_endpoints(self):
        self.assertTrue(audit.percentage_check(0, 10, "0.0", 1)["compatible"])
        self.assertTrue(audit.percentage_check(10, 10, "100", 0)["compatible"])

    def test_invalid_percentage_inputs(self):
        cases = [(1, 0, "0", 0), (2, 1, "10", 0), (-1, 3, "0", 0),
                 (True, 3, "0", 0), (1, 3, "NaN", 1), (1, 3, "Infinity", 1),
                 (1, 3, "101", 1), (1, 3, "33.33", 1), (1, 3, "text", 1),
                 (1, 3, "33", 13), (1, 3, "1e-999999999", 1)]
        for values in cases:
            with self.subTest(values=values), self.assertRaises(ValueError):
                audit.percentage_check(*values)

    def test_flow(self):
        self.assertTrue(audit.flow_check(100, 10, 5, 85, disjoint=True)["reconciles"])
        result = audit.flow_check(100, 10, 5, 90, disjoint=True)
        self.assertFalse(result["reconciles"])
        self.assertEqual(result["difference"], 5)

    def test_flow_requires_applicability(self):
        with self.assertRaises(ValueError):
            audit.flow_check(100, 10, 5, 85)
        for values in [(10, 8, 3, 0), (10, 0, 0, 11), (-1, 0, 0, 0)]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                audit.flow_check(*values, disjoint=True)


class InventoryTests(unittest.TestCase):
    def test_hashes_bytes_without_modification(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = b"\x00Synthetic evidence\xff\n"
            (root / "evidence.bin").write_bytes(payload)
            before = (root / "evidence.bin").stat().st_mtime_ns
            item = audit.inventory(root, ["evidence.bin"])["artifacts"][0]
            self.assertEqual(item["sha256"], hashlib.sha256(payload).hexdigest())
            self.assertEqual(item["size_bytes"], len(payload))
            self.assertEqual(item["label"], "evidence.bin")
            self.assertEqual((root / "evidence.bin").read_bytes(), payload)
            self.assertEqual((root / "evidence.bin").stat().st_mtime_ns, before)

    def test_order_is_stable_and_empty_files_supported(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "z").write_bytes(b"")
            (root / "a").write_bytes(b"a")
            first = audit.inventory(root, ["z", "a"])["artifacts"]
            second = audit.inventory(root, ["a", "z"])["artifacts"]
            self.assertEqual(first, second)
            self.assertEqual(first[1]["sha256"], hashlib.sha256(b"").hexdigest())

    def test_rejects_escape_duplicate_directory_and_missing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "item").write_text("safe", encoding="utf-8")
            for names in [["../outside"], ["item", "./item"], ["."], ["missing"], []]:
                with self.subTest(names=names), self.assertRaises((ValueError, OSError)):
                    audit.inventory(root, names)

    def test_rejects_reparse_points_even_without_symlink_privilege(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "item").write_text("safe", encoding="utf-8")
            with patch.object(Path, "is_symlink", return_value=True):
                with self.assertRaisesRegex(ValueError, "Symlinks"):
                    audit.inventory(root, ["item"])

    def test_changed_evidence_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "item").write_text("safe", encoding="utf-8")
            with patch.object(audit, "_file_signature", side_effect=[(1,), (1,), (1,), (2,)]):
                with self.assertRaisesRegex(ValueError, "changed"):
                    audit.inventory(root, ["item"])


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.report = audit.load_json(EXAMPLE)

    def assert_invalid(self, report, message):
        self.assertTrue(any(message in error for error in audit.validate_report(report)), message)

    def test_example_is_valid(self):
        self.assertEqual(audit.validate_report(self.report), [])

    def test_schema_rejects_missing_and_extra_fields(self):
        del self.report["disclaimer"]
        self.assert_invalid(self.report, "disclaimer")
        self.report = audit.load_json(EXAMPLE)
        self.report["fraud_probability"] = 0.99
        self.assert_invalid(self.report, "Additional properties")

    def test_timestamp_requires_timezone_and_real_date(self):
        for value in ["2026-10-18T12:00:00", "yesterday", "2026-02-30T12:00:00Z"]:
            with self.subTest(value=value):
                self.report["audit"]["created_at"] = value
                self.assert_invalid(self.report, "date-time")

    def test_unknown_evidence_and_duplicate_ids(self):
        self.report["findings"][0]["artifact_ids"] = ["UNKNOWN"]
        self.assert_invalid(self.report, "unknown artifact_ids")
        self.report = audit.load_json(EXAMPLE)
        self.report["artifacts"].append(copy.deepcopy(self.report["artifacts"][0]))
        self.assert_invalid(self.report, "Duplicate artifact")

    def test_duplicate_domains_do_not_count_as_coverage(self):
        self.report["coverage"][-1] = copy.deepcopy(self.report["coverage"][0])
        self.assert_invalid(self.report, "exactly once")

    def test_unassessed_is_not_a_clean_report(self):
        self.report["findings"] = []
        for item in self.report["coverage"]:
            item.update(status="not_assessed", checks=[], limitations="No material inspected")
        self.report["assessment"]["status"] = "no_significant_anomaly"
        self.assert_invalid(self.report, "insufficient_evidence")
        self.report["assessment"]["status"] = "insufficient_evidence"
        self.assertEqual(audit.validate_report(self.report), [])

    def test_partial_and_unassessed_require_honest_coverage(self):
        self.report["coverage"][0].update(status="partial", limitations="", checks=[])
        self.assertTrue(audit.validate_report(self.report))
        self.report = audit.load_json(EXAMPLE)
        self.report["coverage"][0]["status"] = "not_assessed"
        self.assertTrue(audit.validate_report(self.report))

    def test_level_two_requires_challenge_and_human_review(self):
        self.report["findings"][0]["self_challenge"]["outcome"] = "not_performed"
        self.report["findings"][0]["human_review_required"] = False
        errors = audit.validate_report(self.report)
        self.assertTrue(any("self-challenge" in error for error in errors))
        self.assertTrue(any("human review" in error for error in errors))

    def test_resolved_cannot_remain_active(self):
        self.report["findings"][0]["self_challenge"]["outcome"] = "resolved"
        self.assert_invalid(self.report, "cannot remain active")

    def test_level_four_needs_read_matched_authoritative_source(self):
        self.report["findings"][0]["level"] = 4
        self.report["assessment"]["status"] = "externally_documented_issue"
        self.assert_invalid(self.report, "read authoritative")
        source = {
            "id": "S001", "url": "https://example.invalid/synthetic-notice",
            "title": "SYNTHETIC notice", "issuer": "Fictional publisher",
            "accessed_at": "2026-10-18T12:00:00Z", "authoritative": True,
            "article_match": True, "access_status": "read",
            "statement": "Synthetic assertion used only to exercise validation.", "limitations": "Not a real notice or verification."
        }
        self.report["sources"] = [source]
        self.report["findings"][0]["source_ids"] = ["S001"]
        self.assertEqual(audit.validate_report(self.report), [])
        for field, value in [("authoritative", False), ("article_match", False), ("access_status", "metadata_only")]:
            changed = copy.deepcopy(self.report)
            changed["sources"][0][field] = value
            self.assert_invalid(changed, "read authoritative")

    def test_source_credentials_are_rejected(self):
        self.report["sources"] = [{
            "id": "S001", "url": "https://name:secret@example.invalid/notice",
            "title": "Synthetic", "issuer": "Synthetic", "accessed_at": "2026-10-18T12:00:00Z",
            "authoritative": False, "article_match": False, "access_status": "unavailable",
            "statement": "Not retrieved", "limitations": "Synthetic only"
        }]
        self.assert_invalid(self.report, "embedded credentials")

    def test_derivation_requires_parents_and_detects_cycles(self):
        item = self.report["artifacts"][0]
        item.update(kind="derived", derived_from=[item["id"]], transformations=["Synthetic transform"])
        self.assert_invalid(self.report, "cycle")
        item["derived_from"] = []
        self.assert_invalid(self.report, "requires parent")

    def test_hash_unavailability_requires_explanation(self):
        self.report["artifacts"][0]["sha256"] = None
        self.report["artifacts"][0]["limitation"] = ""
        self.assert_invalid(self.report, "requires a limitation")

    def test_assessment_cannot_hide_material_findings(self):
        self.report["assessment"]["status"] = "no_significant_anomaly"
        self.assert_invalid(self.report, "contradicts")


class CommandTests(unittest.TestCase):
    def run_tool(self, *args):
        return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True, encoding="utf-8")

    def test_validation_cli_and_active_counts(self):
        result = self.run_tool("validate-report", str(EXAMPLE))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["active_finding_counts"], {"1": 0, "2": 1, "3": 0, "4": 0})

    def test_invalid_report_returns_one(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.json"
            path.write_text("{}", encoding="utf-8")
            result = self.run_tool("validate-report", str(path))
            self.assertEqual(result.returncode, 1)
            self.assertFalse(json.loads(result.stdout)["valid"])

    def test_invalid_input_returns_two_without_traceback(self):
        result = self.run_tool("flow", "--initial", "10", "--excluded", "1", "--dropouts", "1", "--analyzed", "8")
        self.assertEqual(result.returncode, 2)
        self.assertIn("--disjoint", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_json_rejects_duplicates_and_nonfinite_values(self):
        for content in ['{"x": 1, "x": 2}', '{"x": NaN}']:
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / "bad.json"
                path.write_text(content, encoding="utf-8")
                result = self.run_tool("validate-report", str(path))
                self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
