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

    def test_conversion_preserves_method_context_and_domain_limits_without_aliasing(self):
        context = {
            "disciplines": ["Mixed research"], "method_families": ["Interpretive", "Quantitative"],
            "applicability_notes": "Do not impose inferential tests on interpretive claims.",
        }
        self.report["audit"]["research_context"] = context
        self.report["coverage"][1].update(status="partial", limitations="Only unweighted flow was checked.")
        result = audit.checkpoint_from_report(self.report)
        self.assertEqual(result["research_context"], context)
        for prior, carried in zip(self.report["coverage"], result["coverage"]):
            self.assertEqual(carried["limitations"], prior["limitations"])
            descriptions = [check["description"] for check in result["completed_checks"] if check["id"] in carried["check_ids"]]
            self.assertEqual(descriptions, prior["checks"])
        self.assertEqual(audit.checkpoint_warnings(result), [])
        result["research_context"]["disciplines"].append("Changed only in checkpoint")
        self.assertEqual(context["disciplines"], ["Mixed research"])

    def test_assessed_coverage_cannot_survive_without_checks_or_evidence(self):
        for key in ("artifacts", "sources", "completed_checks", "findings"):
            self.checkpoint[key] = []
        for item in self.checkpoint["coverage"]:
            item["status"] = "completed"
            item.pop("check_ids")  # Also reject this claim in the legacy format.
        self.assertTrue(any("requires completed checks" in error for error in audit.validate_checkpoint(self.checkpoint)))

    def test_domain_links_reject_missing_unknown_and_orphaned_checks(self):
        self.checkpoint["coverage"][0]["check_ids"] = []
        self.assertTrue(audit.validate_checkpoint(self.checkpoint))
        self.checkpoint["coverage"][0]["check_ids"] = ["MISSING"]
        self.assertTrue(any("unknown check_ids" in error for error in audit.validate_checkpoint(self.checkpoint)))
        self.checkpoint = audit.checkpoint_from_report(self.report)
        orphan = copy.deepcopy(self.checkpoint["completed_checks"][0])
        orphan["id"] = "ORPHAN_CHECK"
        self.checkpoint["completed_checks"].append(orphan)
        self.assertTrue(any("linked to assessed coverage" in error for error in audit.validate_checkpoint(self.checkpoint)))

    def test_unassessed_domain_cannot_claim_checks_and_partial_needs_a_reason(self):
        self.checkpoint["coverage"][0]["status"] = "not_assessed"
        self.assertTrue(audit.validate_checkpoint(self.checkpoint))
        self.checkpoint = audit.checkpoint_from_report(self.report)
        self.checkpoint["coverage"][0].update(status="partial", limitations="   ")
        self.assertTrue(audit.validate_checkpoint(self.checkpoint))

    def test_legacy_checkpoint_is_readable_with_explicit_missing_history_warnings(self):
        for item in self.checkpoint["coverage"]:
            item.pop("limitations")
            item.pop("check_ids")
        self.assertEqual(audit.validate_checkpoint(self.checkpoint), [])
        warnings = audit.checkpoint_warnings(self.checkpoint)
        self.assertTrue(any("Research context was not recorded" in warning for warning in warnings))
        self.assertTrue(any("reasons/limitations were not recorded" in warning for warning in warnings))
        self.assertTrue(any("domain coverage cannot be confirmed" in warning for warning in warnings))

    def test_no_assessable_material_can_be_carried_without_inventing_completed_work(self):
        for key in ("artifacts", "sources", "completed_checks", "findings"):
            self.checkpoint[key] = []
        for item in self.checkpoint["coverage"]:
            item.update(status="not_assessed", check_ids=[], limitations="No research material supplied.")
        self.assertEqual(audit.validate_checkpoint(self.checkpoint), [])

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
                item["check_ids"] = []
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
            legacy = json.loads(result.stdout)
            for item in legacy["coverage"]:
                item.pop("limitations")
                item.pop("check_ids")
            path.write_text(json.dumps(legacy), encoding="utf-8")
            legacy_result = subprocess.run([sys.executable, str(TOOL), "validate-checkpoint", str(path)], capture_output=True, text=True)
            self.assertEqual(legacy_result.returncode, 0, legacy_result.stderr)
            self.assertTrue(any("domain coverage cannot be confirmed" in warning for warning in json.loads(legacy_result.stdout)["warnings"]))
            path.write_text("{}", encoding="utf-8")
            invalid = subprocess.run([sys.executable, str(TOOL), "validate-checkpoint", str(path)], capture_output=True, text=True)
            self.assertEqual(invalid.returncode, 1)
            self.assertIsNone(json.loads(invalid.stdout)["pending_steps"])
            self.assertIsNone(json.loads(invalid.stdout)["warnings"])


if __name__ == "__main__":
    unittest.main()
