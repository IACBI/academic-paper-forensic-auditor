# Reproducible synthetic acceptance evaluation

The suite tests whether a response follows the audit workflow on supplied synthetic material. It is not an expert-adjudicated scientific benchmark and does not estimate real-world sensitivity/specificity. The scoring program does not understand research content: an independent human or model judge must inspect the actual responses against the rubric.

## Cases and isolation

`evaluations/suite.json` defines 16 cases: six material concerns, seven legitimate/consistent controls, two insufficient-evidence cases and one continuation resolved by a correction. It records method, fixture section, expected outcome and observable checks. Input material is synthetic and contains no real people or unpublished papers.

The three protocol routes are quick (only QUICKSTART's copyable request), master (full prompt) and skill (the open folder and linked resources). `prepare` copies only the selected protocol and case material. It does not include expected outcomes, rubric requirements or other variants. Each case is reviewed independently. The continuation case necessarily supplies the prior finding record because resuming it is the task.

Protocol files, rendered inputs, suite and actual response text are hashed. An annotation cannot quietly replace an input, omit difficult cases, quote text absent from a response, duplicate easy cases or count unassessed checks as passing. A changed protocol/fixture/rubric makes its baseline stale. Source changes therefore require rerunning the relevant evaluation rather than editing hashes to preserve a passing result.

## Prepare a blind packet

In a development environment with the skill's requirements installed:

```text
python scripts/evaluate.py prepare --variant quick --output-dir tmp/evaluation/quick
python scripts/evaluate.py prepare --variant master --output-dir tmp/evaluation/master
python scripts/evaluate.py prepare --variant skill --output-dir tmp/evaluation/skill
```

Use fresh output directories; preparation preserves existing files. Give the chosen assistant only that packet's instructions, protocol and case files. Do not give it suite.json, this guide, expected results, old baselines or another variant. Save one actual Markdown response as R01.md through R16.md. Do not have the assistant grade itself against hidden answers.

The packet uses a text-readable offline task to make variants comparable. An evaluator may read/write files to transport the exercise but must not claim clock, web, hashing, scientific execution or image operations that did not occur. Native installation, automatic discovery and specialist tools require separate tests.

## Independent judgement and evidence

A separate judge reads the raw responses and suite. For every case it records observed_outcome and one entry for each common/case-specific check: id, status (pass/fail/not_assessed), an exact response quote or null, and a substantive rationale. Every passing check needs an actual response excerpt. Quotes must occur verbatim in that response; a relevant quote is not by itself proof that the judge interpreted it correctly.

The judge must record failures and uncertainty honestly. It must not rewrite a response, substitute an expected answer, silently relax the rubric or upgrade not_assessed to pass. Review disagreements against the raw text. Missing rubric coverage fails the case; unknown source/model facts stay unknown. Record whether the judge is human or model; model judgement is not an independent domain expert's adjudication.

The initial strict review found that quick R04 and master R08 omitted explicit independent-human-review framing, despite correct case classifications. [reviewed-regressions.json](../evaluations/reviewed-regressions.json) retains those actual responses, corrected annotations and protocol hashes verified against commit `ce29b19`. The prompt instructions were then clarified for short reports and reports with no findings, and fresh blind packets prepared. Historical failures are not rescored as current baselines or silently erased by replacing their response text.

Use `evaluations/run.schema.json` for the result contract. The judgements input is its judgements array; raw responses remain individual Rxx.md files until assembly:

```text
python scripts/evaluate.py assemble --packet tmp/evaluation/quick --responses tmp/evaluation/quick-responses --judgements tmp/evaluation/quick-judgements.json --host "Actual host and execution mode" --judge "Actual judge identity" --judge-kind human --judge-notes "Actual scope and qualifications" --output evaluations/baseline-quick.json
```

Use `--judge-kind model` for model judges. Supply `--model` only when the exact responder model identity was observed; omission stores null. The command observes its own assembly timestamp; this does not imply the responder observed a clock. Do not label a local agent test as a different provider or native installation test.

Assembly verifies the manifest and actual protocol, case and instruction bytes before reading responses. It refuses altered/stale packets and preserves an existing output file. Retain only reviewed baselines needed to support published local results; they embed the actual raw responses and judgement excerpts so the record remains inspectable after temporary packets are cleaned.

## Score and compare

```text
python scripts/evaluate.py score evaluations/baseline-quick.json
python scripts/evaluate.py compare evaluations/baseline-quick.json evaluations/baseline-master.json evaluations/baseline-skill.json
python scripts/check_project.py
```

A case passes only when its observed outcome matches the expected classification and every rubric check passes. A complete run covers every case exactly once. Summary counts retain failed and not-assessed checks; they do not disappear from the denominator. Comparison rejects duplicate variant/host/model identities and states whether all three variants are covered. Passing one variant is not an all-format comparison.

Exit codes: 0 all checks passed/preparation succeeded; 1 a valid scored run failed acceptance; 2 malformed, stale, incomplete or unreadable input. These are engineering acceptance outcomes, not misconduct probabilities or scientific detection rates.

## Compatibility and scientific release gates

The committed local baselines document only their recorded host/mode/model and judge. Textual use of a skill is distinct from successful native installation; multiple runs on one local host are distinct from cross-provider validation. Record each actual host, observed model/version, date, context/file capabilities, protocol hash, native-versus-text mode, outcomes and failures before making a host-specific compatibility claim.

Broader claims require authorized real literature, qualified reviewers, negative and ambiguous cases, multiple languages/modalities and appropriate metrics. No prompt test can certify all research disciplines or future agents. These are external validation gates for those claims, not reasons to fabricate measurements or add mandatory vendor dependencies to this workflow.
