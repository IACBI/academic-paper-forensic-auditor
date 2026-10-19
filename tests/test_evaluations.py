"""Evaluation plumbing must reject leakage, stale evidence and inflated scores.

Fabricated responses below test the scorer only, not scientific performance.
Actual independent outputs are stored in separately reviewed baseline records.
"""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evaluate", ROOT / "scripts/evaluate.py")
evaluation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluation)


def fake_run(variant="quick"):
    suite = evaluation.load_suite()
    text = "SCORER UNIT FIXTURE ONLY. This is not an actual scientific evaluation."
    return {
        "schema_version": "0.0.3", "suite_id": suite["id"], "suite_sha256": evaluation.digest(evaluation.SUITE.read_bytes()),
        "variant": variant, "recorded_at": "2026-10-18T12:00:00Z", "host": "Unit fixture, not a real host run", "model": None,
        "judge": {"identity": "Unit fixture", "kind": "model", "notes": "Fabricated annotations for scorer tests only."},
        "protocol_hashes": {name: evaluation.digest(path.read_bytes()) for name, path in evaluation.protocol_sources(variant).items()},
        "input_hashes": {case["id"]: evaluation.digest(evaluation.render_case(case).encode("utf-8")) for case in suite["cases"]},
        "responses": [{"case_id": case["id"], "text": text, "sha256": evaluation.digest(text.encode("utf-8"))} for case in suite["cases"]],
        "judgements": [{"case_id": case["id"], "observed_outcome": case["expected_outcome"],
                        "checks": [{"id": check["id"], "status": "pass", "quote": text, "rationale": "Fabricated unit-test annotation; no claim of scientific correctness."} for check in suite["common_checks"] + case["checks"]]} for case in suite["cases"]],
    }


class SuiteTests(unittest.TestCase):
    def test_suite_contains_controls_uncertainty_and_resolution(self):
        suite = evaluation.load_suite()
        classes = [case["expected_outcome"] for case in suite["cases"]]
        self.assertEqual(len(classes), 16)
        self.assertEqual(classes.count("concern"), 6)
        self.assertEqual(classes.count("clean"), 7)
        self.assertEqual(classes.count("insufficient_evidence"), 2)
        self.assertEqual(classes.count("resolved"), 1)

    def test_blind_packets_have_no_oracle_or_other_protocols(self):
        for variant in ("quick", "master", "skill"):
            with self.subTest(variant=variant), tempfile.TemporaryDirectory() as temp:
                packet = Path(temp) / "packet"
                manifest = evaluation.prepare(variant, packet)
                self.assertEqual(len(list((packet / "cases").glob("*.md"))), 16)
                self.assertEqual(set(manifest), {"suite_id", "suite_sha256", "variant", "protocol_hashes", "input_hashes"})
                self.assertFalse(list(packet.rglob("suite.json")))
                self.assertFalse(list(packet.rglob("run.schema.json")))
                for file in packet.rglob("*"):
                    if file.is_file():
                        self.assertNotIn('"expected_outcome"', file.read_text(encoding="utf-8"))
                if variant != "master":
                    self.assertFalse(list(packet.rglob("master_prompt.md")))
                if variant != "quick":
                    self.assertFalse(list(packet.rglob("QUICKSTART.md")))
                with self.assertRaises(FileExistsError):
                    evaluation.prepare(variant, packet)

    def test_fixture_sections_are_isolated(self):
        case = evaluation.load_suite()["cases"][0]
        text = evaluation.render_case(case)
        self.assertIn("F1. Proposition", text)
        self.assertNotIn("Q1. Twelve", text)

    def test_parent_paths_and_missing_sections_are_rejected(self):
        with self.assertRaises(ValueError):
            evaluation.source_path("../outside")
        case = copy.deepcopy(evaluation.load_suite()["cases"][0])
        case["inputs"][0]["section"] = "MISSING_SECTION"
        with self.assertRaisesRegex(ValueError, "Missing/ambiguous"):
            evaluation.render_case(case)

    def test_malformed_and_duplicate_suites_fail(self):
        suite = evaluation.load_suite()
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "suite.json"
            for value in [{}, {**suite, "cases": suite["cases"] + [suite["cases"][0]]}]:
                path.write_text(json.dumps(value), encoding="utf-8")
                with patch.object(evaluation, "SUITE", path), self.assertRaises(ValueError):
                    evaluation.load_suite()


class ScoringTests(unittest.TestCase):
    def test_complete_annotations_are_counted_without_accuracy_claim(self):
        result = evaluation.score(fake_run())
        self.assertTrue(result["all_passed"])
        self.assertEqual(result["cases_total"], 16)
        self.assertEqual(result["checks_passed"], 48)
        self.assertIn("not measured scientific accuracy", result["limitation"])

    def test_unassessed_checks_and_mismatched_outcomes_never_pass(self):
        run = fake_run()
        run["judgements"][0]["checks"][0]["status"] = "not_assessed"
        result = evaluation.score(run)
        self.assertFalse(result["all_passed"])
        self.assertEqual(result["checks_not_assessed"], 1)
        self.assertEqual(result["checks_passed"], 47)
        run = fake_run()
        run["judgements"][6]["observed_outcome"] = "concern"
        self.assertFalse(evaluation.score(run)["cases"][6]["passed"])

    def test_omitted_duplicate_or_unknown_cases_cannot_improve_score(self):
        for field in ("responses", "judgements"):
            for action in ("omit", "duplicate", "unknown"):
                with self.subTest(field=field, action=action):
                    run = fake_run()
                    if action == "omit":
                        run[field].pop()
                    elif action == "duplicate":
                        run[field].append(copy.deepcopy(run[field][0]))
                    else:
                        run[field][0]["case_id"] = "R99"
                    with self.assertRaises(ValueError):
                        evaluation.score(run)

    def test_stale_suite_protocol_inputs_and_response_are_rejected(self):
        for field in ("suite_sha256", "protocol_hashes", "input_hashes", "responses"):
            with self.subTest(field=field):
                run = fake_run()
                if field == "suite_sha256":
                    run[field] = "0" * 64
                elif field in ("protocol_hashes", "input_hashes"):
                    run[field][next(iter(run[field]))] = "0" * 64
                else:
                    run[field][0]["text"] += " Altered text."
                with self.assertRaises(ValueError):
                    evaluation.score(run)

    def test_quotes_must_exist_and_passing_checks_need_evidence(self):
        for quote in (None, "This phrase does not occur in the response"):
            run = fake_run()
            run["judgements"][0]["checks"][0]["quote"] = quote
            with self.assertRaises(ValueError):
                evaluation.score(run)

    def test_missing_or_duplicate_rubric_checks_are_rejected(self):
        run = fake_run()
        run["judgements"][0]["checks"].pop()
        with self.assertRaises(ValueError):
            evaluation.score(run)
        run = fake_run()
        run["judgements"][0]["checks"].append(copy.deepcopy(run["judgements"][0]["checks"][0]))
        with self.assertRaises(ValueError):
            evaluation.score(run)

    def test_tampered_packet_is_rejected_before_reading_responses(self):
        with tempfile.TemporaryDirectory() as temp:
            packet = Path(temp) / "packet"
            manifest = evaluation.prepare("quick", packet)
            manifest["input_hashes"]["../../.env"] = "0" * 64
            (packet / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "no responses were read"):
                evaluation.assemble(packet, Path(temp) / "missing", Path(temp) / "missing.json", "host", None, {}, Path(temp) / "out.json")
            self.assertFalse((Path(temp) / "out.json").exists())

    def test_changed_packet_bytes_are_rejected_despite_unchanged_manifest(self):
        for name in ("instructions.md", "cases/R01.md", "protocol/QUICKSTART.md"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp:
                packet = Path(temp) / "packet"
                evaluation.prepare("quick", packet)
                path = packet / name
                path.write_bytes(path.read_bytes() + b"\nALTERED\n")
                with self.assertRaisesRegex(ValueError, "Packet file altered"):
                    evaluation.assemble(packet, Path(temp) / "missing", Path(temp) / "missing.json", "host", None, {}, Path(temp) / "out.json")
                self.assertFalse((Path(temp) / "out.json").exists())

    def test_assembly_binds_raw_responses_and_preserves_existing_output(self):
        run = fake_run()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet = root / "packet"
            evaluation.prepare("quick", packet)
            responses = root / "responses"
            responses.mkdir()
            for response in run["responses"]:
                (responses / f"{response['case_id']}.md").write_text(response["text"], encoding="utf-8")
            judgements = root / "judgements.json"
            judgements.write_text(json.dumps(run["judgements"]), encoding="utf-8")
            output = root / "run.json"
            args = (packet, responses, judgements, run["host"], None, run["judge"], output)
            result = evaluation.assemble(*args)
            self.assertTrue(result["all_passed"])
            assembled = evaluation.AUDIT.load_json(output)
            self.assertEqual(assembled["responses"], run["responses"])
            before = output.read_bytes()
            with self.assertRaises(FileExistsError):
                evaluation.assemble(*args)
            self.assertEqual(output.read_bytes(), before)

    def test_cli_distinguishes_acceptance_failure_from_invalid_input(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "run.json"
            run = fake_run()
            values = [(run, 0)]
            failed = copy.deepcopy(run)
            failed["judgements"][0]["checks"][0]["status"] = "fail"
            values.extend([(failed, 1), ({}, 2)])
            for value, expected_code in values:
                with self.subTest(expected_code=expected_code):
                    path.write_text(json.dumps(value), encoding="utf-8")
                    result = subprocess.run([sys.executable, str(ROOT / "scripts/evaluate.py"), "score", str(path)], capture_output=True, text=True)
                    self.assertEqual(result.returncode, expected_code, result.stderr)
                    if expected_code == 2:
                        self.assertIn("Error:", result.stderr)
                    else:
                        self.assertEqual(json.loads(result.stdout)["all_passed"], expected_code == 0)


if __name__ == "__main__":
    unittest.main()
