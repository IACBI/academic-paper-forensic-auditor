"""Contract regressions and observable local workflow behavior."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills/academic-paper-audit/scripts"
sys.path.insert(0, str(SCRIPTS))
import audit_tools as audit
import audit_workflow as workflow


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.report = audit.load_json(ROOT / "examples/synthetic-report.json")

    def test_registered_but_unassessed_artifact_cannot_support_active_finding(self):
        artifact = copy.deepcopy(self.report["artifacts"][0])
        artifact.update(id="A002", label="uninspected.md")
        self.report["artifacts"].append(artifact)
        self.report["findings"][0]["artifact_ids"] = ["A002"]
        self.assertTrue(any("assessed domain" in error for error in audit.validate_report(self.report)))
        self.report["coverage"][1]["artifact_ids"].append("A002")
        self.assertEqual(audit.validate_report(self.report), [])

    def test_closure_requires_reason_and_known_evidence(self):
        finding = self.report["findings"][0]
        for status in ("resolved", "withdrawn"):
            finding["status"] = status
            self.report["assessment"]["status"] = "no_significant_anomaly"
            self.assertTrue(audit.validate_report(self.report))
        finding["closure"] = {"reason": "Reconciled against supplied correction", "artifact_ids": ["A001"], "source_ids": []}
        self.assertEqual(audit.validate_report(self.report), [])
        finding["closure"]["artifact_ids"] = ["UNKNOWN"]
        self.assertTrue(audit.validate_report(self.report))
        finding["closure"]["artifact_ids"] = []
        self.assertTrue(audit.validate_report(self.report))
        finding["closure"]["artifact_ids"] = ["A001"]
        finding["closure"]["reason"] = " "
        self.assertTrue(audit.validate_report(self.report))

    def test_active_finding_cannot_keep_closure(self):
        self.report["findings"][0]["closure"] = {"reason": "Old closure", "artifact_ids": ["A001"], "source_ids": []}
        self.assertTrue(audit.validate_report(self.report))

    def test_human_review_is_explicit_and_separate_from_model_finding(self):
        review = {"status": "pending", "reviewer": None, "reviewed_at": None, "notes": "Awaiting domain reviewer"}
        self.report["findings"][0]["human_review"] = review
        self.assertEqual(audit.validate_report(self.report), [])
        review["status"] = "confirmed"
        self.assertTrue(audit.validate_report(self.report))
        review.update(reviewer="Synthetic reviewer", reviewed_at="2026-10-20T08:00:00Z")
        self.assertEqual(audit.validate_report(self.report), [])
        self.assertEqual(self.report["findings"][0]["level"], 2)

    def test_checkpoint_preserves_every_field_and_detects_tampering(self):
        self.report["findings"][0]["issue_kind"] = "reproducible_inconsistency"
        checkpoint = audit.checkpoint_from_report(self.report)
        self.assertEqual(checkpoint["source_report"]["report"], self.report)
        self.assertEqual(audit.validate_checkpoint(checkpoint), [])
        checkpoint["source_report"]["report"]["findings"][0]["assumptions"].append("tampered")
        self.assertTrue(any("digest" in error for error in audit.validate_checkpoint(checkpoint)))
        self.assertNotIn("tampered", self.report["findings"][0]["assumptions"])

    def test_checkpoint_summary_cannot_disagree_with_source(self):
        checkpoint = audit.checkpoint_from_report(self.report)
        checkpoint["findings"][0]["observation"] = "Contradictory summary"
        self.assertTrue(any("differs" in error for error in audit.validate_checkpoint(checkpoint)))

    def test_legacy_summary_has_missing_source_warning(self):
        checkpoint = audit.checkpoint_from_report(self.report, include_source=False)
        self.assertEqual(audit.validate_checkpoint(checkpoint), [])
        self.assertTrue(any("Full source report" in warning for warning in audit.checkpoint_warnings(checkpoint)))


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.report = audit.load_json(ROOT / "examples/synthetic-report.json")

    def test_diff_closure_reopening_missing_history_and_identity(self):
        after = copy.deepcopy(self.report)
        finding = after["findings"][0]
        finding.update(status="resolved", closure={"reason": "Correction", "artifact_ids": ["A001"], "source_ids": []})
        after["assessment"]["status"] = "no_significant_anomaly"
        self.assertEqual(workflow.compare_reports(self.report, after)["findings"][0]["transition"], "resolved")
        self.assertEqual(workflow.compare_reports(after, self.report)["findings"][0]["transition"], "reopened")
        after["findings"] = []
        self.assertEqual(workflow.compare_reports(self.report, after)["findings"][0]["transition"], "removed_history")
        after["audit"]["id"] = "OTHER"
        with self.assertRaises(ValueError):
            workflow.compare_reports(self.report, after)

    def test_evidence_changed_missing_unknown_and_unchanged(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "paper.md"
            content = (ROOT / "tests/fixtures/synthetic_manuscript.md").read_bytes()
            path.write_bytes(content)
            result = workflow.verify_evidence(self.report, temp, {"A001": "paper.md"})
            self.assertEqual(result["recheck_finding_ids"], [])
            path.write_bytes(b"changed")
            self.assertEqual(workflow.verify_evidence(self.report, temp, {"A001": "paper.md"})["recheck_finding_ids"], ["F001"])
            path.unlink()
            self.assertEqual(workflow.verify_evidence(self.report, temp, {"A001": "paper.md"})["artifacts"][0]["status"], "missing")
            path.write_bytes(content)
            self.report["artifacts"][0].update(sha256=None, limitation="Unknown original digest")
            self.assertEqual(workflow.verify_evidence(self.report, temp, {"A001": "paper.md"})["artifacts"][0]["status"], "previous_hash_unknown")

    def test_changed_parent_propagates_to_derived_evidence(self):
        derived = copy.deepcopy(self.report["artifacts"][0])
        derived.update(id="A002", kind="derived", derived_from=["A001"], transformations=["Extraction"])
        self.report["artifacts"].append(derived)
        self.report["coverage"][1]["artifact_ids"].append("A002")
        self.report["findings"][0]["artifact_ids"] = ["A002"]
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / "copy.md").write_bytes((ROOT / "tests/fixtures/synthetic_manuscript.md").read_bytes())
            result = workflow.verify_evidence(self.report, temp, {"A002": "copy.md"})
            self.assertEqual(result["recheck_artifact_ids"], ["A001", "A002"])
            self.assertEqual(result["recheck_finding_ids"], ["F001"])

    def test_mapping_cannot_escape_or_select_unknown_ids(self):
        for mapping in ({"A001": "../secret"}, {"UNKNOWN": "paper.md"}, {}, {"A001": 2}):
            with self.subTest(mapping=mapping), self.assertRaises(ValueError):
                workflow.verify_evidence(self.report, ROOT, mapping)

    def test_related_findings_are_flagged_even_with_one_way_link(self):
        artifact = copy.deepcopy(self.report["artifacts"][0])
        artifact["id"] = "A002"
        self.report["artifacts"].append(artifact)
        self.report["coverage"][1]["artifact_ids"].append("A002")
        other = copy.deepcopy(self.report["findings"][0])
        other["id"] = "F002"
        other["artifact_ids"] = ["A002"]
        self.report["findings"][0]["related_findings"] = ["F002"]
        self.report["findings"].append(other)
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / "unchanged.md").write_bytes((ROOT / "tests/fixtures/synthetic_manuscript.md").read_bytes())
            result = workflow.verify_evidence(self.report, temp, {"A001": "missing.md", "A002": "unchanged.md"})
            self.assertEqual(result["recheck_artifact_ids"], ["A001"])
            self.assertEqual(result["recheck_finding_ids"], ["F001", "F002"])

    def test_render_is_inert_and_retains_full_record(self):
        self.report["findings"][0]["observation"] = '<script>alert(1)</script> ![secret](https://example.invalid/x)'
        rendered = workflow.render_report(self.report, "html")
        self.assertNotIn("<script>", rendered)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertIn("Content-Security-Policy", rendered)
        self.assertNotIn("<img", rendered)
        markdown = workflow.render_report(self.report)
        self.assertIn("\\!\\[secret\\]", markdown)
        self.assertIn("Complete validated record", markdown)
        self.assertIn("self_challenge", markdown)

    def test_text_extraction_retains_unicode_lines_and_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            data = "Başlık\n100 kişi\n".encode("utf-8")
            (Path(temp) / "paper.txt").write_bytes(data)
            result = workflow.extract_text(temp, "paper.txt")
            self.assertEqual(result["original"]["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual(result["pages"][0]["lines"][1], {"line": 2, "text": "100 kişi"})
            with self.assertRaises(ValueError):
                workflow.extract_text(temp, "paper.txt", max_bytes=1)
            with self.assertRaises(ValueError):
                workflow.extract_text(temp, "paper.txt", max_pages=0)

    def test_cli_preserves_existing_output(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "report.html"
            command = [sys.executable, str(SCRIPTS / "audit_workflow.py"), "render", str(ROOT / "examples/synthetic-report.json"), "--format", "html", "--output", str(output)]
            first = subprocess.run(command, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            original = output.read_bytes()
            second = subprocess.run(command, capture_output=True)
            self.assertEqual(second.returncode, 2)
            self.assertEqual(output.read_bytes(), original)


class PdfTests(unittest.TestCase):
    def setUp(self):
        try:
            import pypdf
        except ImportError:
            self.skipTest("Optional pypdf dependency not installed")
        self.pdf = pypdf

    def test_actual_pdf_text_and_locators_without_modifying_original(self):
        # Minimal synthetic PDF with an explicit text stream and correct xref.
        stream = b"BT /F1 12 Tf 20 100 Td (Synthetic evidence 85) Tj ET"
        objects = [b"<< /Type /Catalog /Pages 2 0 R >>",
                   b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
                   b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
                   b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
                   b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream"]
        data = b"%PDF-1.4\n"
        offsets = [0]
        for number, content in enumerate(objects, 1):
            offsets.append(len(data))
            data += str(number).encode() + b" 0 obj\n" + content + b"\nendobj\n"
        xref = len(data)
        data += b"xref\n0 6\n0000000000 65535 f \n"
        data += b"".join(f"{offset:010d} 00000 n \n".encode() for offset in offsets[1:])
        data += b"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n" + str(xref).encode() + b"\n%%EOF\n"
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "text.pdf"
            path.write_bytes(data)
            result = workflow.extract_text(temp, "text.pdf")
            self.assertEqual(result["pages"][0]["text"], "Synthetic evidence 85")
            self.assertEqual(result["pages"][0]["lines"][0]["line"], 1)
            self.assertEqual(result["pages"][0]["pdf_page"], 1)
            self.assertEqual(path.read_bytes(), data)

    def test_blank_pdf_requires_review_and_encrypted_pdf_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            writer = self.pdf.PdfWriter()
            writer.add_blank_page(width=200, height=200)
            path = Path(temp) / "blank.pdf"
            with path.open("wb") as handle:
                writer.write(handle)
            result = workflow.extract_text(temp, "blank.pdf")
            self.assertEqual(result["pages"][0]["pdf_page"], 1)
            self.assertEqual(result["pages"][0]["status"], "no_text_ocr_or_visual_review_needed")
            writer.encrypt("test-password")
            with path.open("wb") as handle:
                writer.write(handle)
            with self.assertRaisesRegex(ValueError, "Encrypted"):
                workflow.extract_text(temp, "blank.pdf")

    def test_malformed_pdf_fails_without_result(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / "broken.pdf").write_bytes(b"not a pdf")
            with self.assertRaisesRegex(ValueError, "parsing failed"):
                workflow.extract_text(temp, "broken.pdf")


if __name__ == "__main__":
    unittest.main()
