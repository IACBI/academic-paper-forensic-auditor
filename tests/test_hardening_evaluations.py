"""Evaluation infrastructure tests; no fabricated model-performance claims."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


evaluation = module("hardening_evaluation", ROOT / "scripts/evaluate.py")
project = module("hardening_project", ROOT / "scripts/check_project.py")


class EvaluationHardeningTests(unittest.TestCase):
    def test_historical_baselines_match_actual_retained_bytes(self):
        for variant in ("quick", "master", "skill"):
            run = evaluation.AUDIT.load_json(ROOT / f"evaluations/baseline-{variant}.json")
            result = evaluation.score(run, historical=True)
            self.assertTrue(result["all_passed"])
            self.assertTrue(result["historical"])
            # Changed input case R16 prevents historical results certifying this tree.
            with self.assertRaises(ValueError):
                evaluation.score(run)
            run["protocol_hashes"][next(iter(run["protocol_hashes"]))] = "0" * 64
            with self.assertRaises(ValueError):
                evaluation.score(run, historical=True)

    def test_extended_suite_covers_language_injection_ocr_versions_and_length(self):
        with patch.object(evaluation, "SUITE", ROOT / "evaluations/suite-hardening.json"):
            suite = evaluation.load_suite()
            self.assertEqual(len(suite["cases"]), 24)
            methods = {case["method"] for case in suite["cases"]}
            self.assertTrue({"injection", "turkish", "turkish_control", "ocr", "versions", "metadata", "image", "long_context"} <= methods)
            turkish = next(case for case in suite["cases"] if case["method"] == "turkish")
            self.assertIn("protocol in Turkish", evaluation.render_case(turkish))
            long_case = next(case for case in suite["cases"] if case["method"] == "long_context")
            self.assertGreater(len(evaluation.render_case(long_case).split()), 7000)

    def test_isolated_packet_has_one_case_and_assembly_requires_distinct_sessions(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet = root / "packet"
            manifest = evaluation.prepare("quick", packet, isolated=True)
            self.assertEqual(manifest["execution_mode"], "isolated")
            for case_id in manifest["input_hashes"]:
                files = list((packet / case_id / "cases").glob("*.md"))
                self.assertEqual([file.name for file in files], [case_id + ".md"])
                self.assertFalse(list((packet / case_id).rglob("suite.json")))
            responses = root / "responses"
            responses.mkdir()
            text = "Infrastructure unit fixture only; no scientific evaluation occurred."
            judgements = []
            for case in evaluation.load_suite()["cases"]:
                (responses / f"{case['id']}.md").write_text(text, encoding="utf-8")
                judgements.append({"case_id": case["id"], "observed_outcome": case["expected_outcome"],
                                   "checks": [{"id": check["id"], "status": "pass", "quote": text, "rationale": "Unit fixture only"}
                                              for check in evaluation.load_suite()["common_checks"] + case["checks"]]})
            judge_file = root / "judge.json"
            judge_file.write_text(json.dumps(judgements), encoding="utf-8")
            args = (packet, responses, judge_file, "unit fixture", None,
                    {"identity": "unit fixture", "kind": "model", "notes": "Not actual judging"}, root / "result.json")
            with self.assertRaisesRegex(ValueError, "session IDs"):
                evaluation.assemble(*args)
            with self.assertRaisesRegex(ValueError, "distinct"):
                evaluation.assemble(*args, case_sessions={key: "same" for key in manifest["input_hashes"]})
            self.assertFalse((root / "result.json").exists())
            result = evaluation.assemble(*args, case_sessions={key: f"unit-{key}" for key in manifest["input_hashes"]})
            self.assertTrue(result["all_passed"])
            self.assertEqual(result["execution_mode"], "isolated")
            self.assertEqual(result["outcome_counts"]["concern"]["concern"], 6)

    def test_translation_command_coverage_catches_missing_and_changed_sections(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(project.translation_errors(text), [])
        self.assertTrue(project.translation_errors(text.replace("<!-- workflow:tr -->", "<!-- workflow:missing -->")))
        self.assertTrue(project.translation_errors(text.replace("audit_workflow.py extract", "audit_workflow.py broken", 1)))


if __name__ == "__main__":
    unittest.main()
