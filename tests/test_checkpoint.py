"""Continuation preserves evidence/status and never turns summaries into new work."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "skills/academic-paper-audit/scripts/audit_tools.py"
SPEC = importlib.util.spec_from_file_location("checkpoint_tools", TOOL)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.report = audit.load_json(ROOT / "examples/synthetic-report.json")
        self.checkpoint = audit.checkpoint_from_report(self.report)

    def test_conversion_preserves_identity_scope_time_status_and_original(self):
        original = copy.deepcopy(self.report)
        result = audit.checkpoint_from_report(self.report)
        self.assertEqual(self.report, original)
        self.assertEqual(result["audit_id"], original["audit"]["id"])
        self.assertEqual(result["scope"], original["audit"]["scope"])
        self.assertEqual(result["last_observed_at"], original["audit"]["created_at"])
        self.assertEqual(result["artifacts"][0]["sha256"], original["artifacts"][0]["sha256"])
        self.assertEqual(result["findings"][0]["id"], "F001")
        self.assertEqual(result["findings"][0]["status"], "active")
        self.assertTrue(any("no new source inspection" in text for text in result["limitations"]))
        self.assertEqual(audit.validate_checkpoint(result), [])

    def test_saved_example_is_the_conversion_of_its_report(self):
        self.assertEqual(self.checkpoint, audit.load_json(ROOT / "examples/synthetic-checkpoint.json"))

    def test_editing_checkpoint_does_not_mutate_prior_report(self):
        original = copy.deepcopy(self.report)
        self.checkpoint["findings"][0]["artifact_ids"].append("NEW")
        self.checkpoint["completed_checks"][0]["artifact_ids"].clear()
        self.assertEqual(self.report, original)

    def test_unknown_time_and_hash_need_limits(self):
        self.checkpoint["last_observed_at"] = None
        self.checkpoint["artifacts"][0]["sha256"] = None
        self.checkpoint["limitations"] = []
        self.assertTrue(audit.validate_checkpoint(self.checkpoint))
        self.checkpoint["limitations"] = ["No clock or file hashing capability was available."]
        self.assertEqual(audit.validate_checkpoint(self.checkpoint), [])

    def test_dangling_ids_duplicates_and_unassessed_findings_fail(self):
        self.checkpoint["findings"][0]["artifact_ids"] = ["MISSING"]
        self.assertTrue(any("unknown artifact_ids" in error for error in audit.validate_checkpoint(self.checkpoint)))
        self.checkpoint = audit.checkpoint_from_report(self.report)
        self.checkpoint["artifacts"].append(copy.deepcopy(self.checkpoint["artifacts"][0]))
        self.assertTrue(any("Duplicate" in error for error in audit.validate_checkpoint(self.checkpoint)))
        self.checkpoint = audit.checkpoint_from_report(self.report)
        for item in self.checkpoint["coverage"]:
            if item["domain"] == "statistics_data":
                item["status"] = "not_assessed"
        self.assertTrue(any("requires assessed coverage" in error for error in audit.validate_checkpoint(self.checkpoint)))

    def test_resolved_finding_retains_history(self):
        finding = self.checkpoint["findings"][0]
        finding["status"] = "resolved"
        finding["verification_notes"] += " Supplied version-2 correction changes 90 to 85."
        self.assertEqual(audit.validate_checkpoint(self.checkpoint), [])
        self.assertEqual(finding["id"], "F001")
        self.assertIn("90", finding["observation"])

    def test_check_id_collision_is_handled(self):
        self.report["artifacts"][0]["id"] = "CHECK_001"
        for item in self.report["coverage"]:
            item["artifact_ids"] = ["CHECK_001" if value == "A001" else value for value in item["artifact_ids"]]
        self.report["findings"][0]["artifact_ids"] = ["CHECK_001"]
        result = audit.checkpoint_from_report(self.report)
        self.assertNotEqual(result["completed_checks"][0]["id"], "CHECK_001")
        self.assertEqual(audit.validate_checkpoint(result), [])

    def test_invalid_report_cannot_be_exported(self):
        del self.report["disclaimer"]
        with self.assertRaisesRegex(ValueError, "invalid report"):
            audit.checkpoint_from_report(self.report)

    def test_cli_conversion_and_validation(self):
        result = subprocess.run([sys.executable, str(TOOL), "checkpoint", str(ROOT / "examples/synthetic-report.json")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "checkpoint.json"
            path.write_text(result.stdout, encoding="utf-8")
            validated = subprocess.run([sys.executable, str(TOOL), "validate-checkpoint", str(path)], capture_output=True, text=True)
            self.assertEqual(validated.returncode, 0, validated.stderr)
            self.assertTrue(json.loads(validated.stdout)["valid"])
            path.write_text("{}", encoding="utf-8")
            invalid = subprocess.run([sys.executable, str(TOOL), "validate-checkpoint", str(path)], capture_output=True, text=True)
            self.assertEqual(invalid.returncode, 1)
            self.assertIsNone(json.loads(invalid.stdout)["pending_steps"])


if __name__ == "__main__":
    unittest.main()
