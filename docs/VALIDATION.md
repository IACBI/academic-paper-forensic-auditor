# Validation and reproducible evaluation

This guide explains what the project has actually checked, how to repeat those checks, and which conclusions the evidence supports. The multilingual [README](../README.md) is the complete user guide. Validation is a maintenance resource: it establishes software contracts and bounded workflow behavior, while scientific findings still need independent human verification.

## Software checks and recorded execution

From the repository root, in an environment with `skills/academic-paper-audit/requirements.txt` installed, run:

```text
python scripts/check_project.py
```

The command checks versions, all 35 numbered protocol sections, generated-reference synchronization, report and continuation contracts, example identity, current evaluation baselines, local documentation links and release inputs. It then runs the 81 behavior tests. Those tests cover arithmetic assumptions, input errors, path containment, linked/reparse files, evidence references, coverage, source eligibility, resolved findings, checkpoint conversion, evaluation integrity and deterministic packaging. An invalid report cannot masquerade as a report with zero findings.

The local execution record is Windows, Python 3.10.11 and jsonschema 4.26.0 on 18 October 2026. All 70 tests passed. The published v.0.0.1 commit, `97f2010`, also passed the [four-job GitHub run](https://github.com/IACBI/academic-paper-forensic-auditor/actions/runs/39166102414): Windows and Ubuntu, each with Python 3.10 and 3.14. Every job checked the project and built all three distribution formats. The archive hashes matched the local builds across all four environments.

The first external run revealed that a Windows temporary directory could use an 8.3 path alias in a test fixture. The fixture was corrected to use the resolved root, matching production behavior; the containment check remained intact. The [workflow](../.github/workflows/validate.yml) uses official actions pinned to verified commits and read-only repository permissions. It runs for main-branch pushes, pull requests and manual dispatch. The current workflow page provides subsequent run results; the recorded release run above remains a fixed reference.

Local packages were also extracted and compared byte-for-byte with their explicit allowlists: 7 prompt files, 15 standalone-skill files and 17 plugin files. Both extracted skill formats validated the synthetic report and checkpoint and reproduced checkpoint conversion. Skill frontmatter validation passed. These checks establish package completeness and helper execution in the tested environments, rather than native installation in every AI product.

The link check resolves local file paths; it does not validate remote URLs or fragment targets. JSON Schema validation checks structure and additional local invariants, not source truth, authority, actual access or honest tool use. A matching file hash identifies bytes, not authenticity or legal chain of custody.

### Windows timestamp compatibility in v.0.0.2

The Windows/Python 3.14 failure in [run 39168957314](https://github.com/IACBI/academic-paper-forensic-auditor/actions/runs/39168957314) was reproduced locally with the official Python 3.14.8 Windows build. A stable rewritten file had the same identity, size and modification time through both APIs, but path-based `stat()` and descriptor-based `fstat()` returned different `st_ctime_ns` values. The old comparison rejected that file before hashing. [CPython issue 157671](https://github.com/python/cpython/issues/157671) documents the underlying difference in timestamp meaning.

Version v.0.0.2 compares identity, size and modification time across the two APIs, while comparing change-time fields only within the same API before and after reading. It retains both descriptor and path stability checks. The same Python 3.14.8 reproduction passed after the fix. Three added regression tests cover differing API timestamp meanings, a descriptor-side timestamp change and a path-side timestamp change; all 73 tests passed locally on Windows/Python 3.10.11. The four-environment CI workflow separately exercises the full suite and all package formats.

The fix does not turn inventory into a transaction or guarantee safety against a hostile concurrently changing filesystem. Use a stable evidence directory under your control. Historical v.0.0.1 packages retain the old behavior; install the v.0.0.2 helper rather than relying on a previously green run of the old release.

### Continuation preservation in v.0.0.3

The updated exporter copies recorded `research_context` without sharing mutable lists with the report. Each coverage entry retains its `limitations` and `check_ids`, linking its actual completed work to the checkpoint check registry. Unknown research context remains absent rather than being inferred. The example checkpoint is regenerated from its source report.

Validation rejects assessed coverage without completed evidence-linked work, unknown or missing declared check links, checks assigned to unassessed domains, and orphaned checks in fully linked records. Six new regression tests also cover partial-scope reasons, preservation without mutation, empty-evidence claims, legitimate unassessed records and legacy handling. All 79 software tests passed locally on Windows/Python 3.10.11 with jsonschema 4.26.0 on 19 October 2026.

The v.0.0.3 reader also accepts consistent v.0.0.2 checkpoints without changing their version or historical claims. `validate-checkpoint` returns a separate `warnings` list identifying absent context, domain reasons or per-domain links. Valid structure with warnings is not confirmation of the missing history. The Python API preserves `validate_checkpoint()`'s error-list contract; callers can obtain the same warnings with `checkpoint_warnings()` after successful validation. New v.0.0.3 records require domain reasons and check links, and schema/protocol versions must match. Research context is copied only when it was recorded. Two release-compatibility regression tests cover these version rules and unchanged legacy reads, bringing the suite to 81 tests. The checkpoint published at the original v.0.0.2 tag was also read successfully without relabeling. New reports use the v.0.0.3 contract; retain previous reports with their matching release helper. Older helpers do not understand new records. The v.0.0.1 and v.0.0.2 tags and assets remain unchanged.

The v.0.0.3 project check and all 81 tests passed locally on Windows/Python 3.10.11 with jsonschema 4.26.0 on 19 October 2026. All three archives were built, and both extracted skill formats validated the report/checkpoint and reproduced the saved checkpoint exactly. The published v.0.0.2 checkpoint also remained readable through the new helper.

## Behavioral suite and current results

The acceptance suite is defined in [suite.json](../evaluations/suite.json), with its [suite schema](../evaluations/suite.schema.json) and [run schema](../evaluations/run.schema.json). It contains synthetic material only:

| Case group | Count | Required distinction |
| --- | --- | --- |
| Material concerns | 6 | Find a supplied formal, qualitative, archival, computational, engineering or synthesis inconsistency and bound the inference |
| Legitimate controls | 7 | Accept the corresponding consistent methods/claims and declared shared-control reuse without inventing a violation |
| Insufficient evidence | 2 | Request missing image/research material without inventing findings or granting clearance |
| Continuation with a correction | 1 | Preserve F001 as resolved history, retain prior scope and checks, and exclude it from active findings |

Each case has grounding, calibration and decision criteria. Grounding requires claims to stay within supplied evidence and actual capabilities. Calibration requires method-appropriate limits, explicit independent-human-review framing and, for material concerns, a locator, benign alternative and next check. The decision criterion addresses the actual case. Absence of evidence cannot be interpreted as authenticity.

| Route and retained record | Cases passed | Criteria passed | Failed / not assessed |
| --- | --- | --- | --- |
| [Quick request](../evaluations/baseline-quick.json) | 16/16 | 48/48 | 0 / 0 |
| [Full protocol](../evaluations/baseline-master.json) | 16/16 | 48/48 | 0 / 0 |
| [Skill](../evaluations/baseline-skill.json) | 16/16 | 48/48 | 0 / 0 |

These records contain 48 actual responses and 144 model-judged criteria across the three routes. Fresh responders did not receive expected answers. A separate local model judge inspected their responses; this was not domain-expert adjudication. Each route used one fresh conversation whose cases shared that conversation, so the cases are not independent statistical trials. Exact model identities were not observed and remain null. The records disclose host, mode, judge and review limitations in their metadata.

The v.0.0.3 baselines are fresh local-subagent evaluations of the actual release protocol and case snapshots, with separate model judging. Exact responder/judge models remain unknown. Reported tool evidence and its limitations are retained in the records where applicable; none of these local-subagent passes certifies a native host. Earlier real CLI observations remain separately preserved at their tested v.0.0.2 source versions below.

An earlier strict review found missing explicit human-review framing in two otherwise correctly classified responses. The reporting instruction was clarified and fresh blind evaluations were run. The correction and historical evidence remain available in [commit 3590ec8](https://github.com/IACBI/academic-paper-forensic-auditor/commit/3590ec8).

The counts above are synthetic acceptance results. They do not estimate sensitivity, specificity or misconduct probability. CI checks the saved records and software contracts; it does not call models or perform a new scientific review.

## Prepare a blind evaluation

Install the validation dependency in your development environment, then create new packet directories:

```text
python scripts/evaluate.py prepare --variant quick --output-dir tmp/evaluation/quick
python scripts/evaluate.py prepare --variant master --output-dir tmp/evaluation/master
python scripts/evaluate.py prepare --variant skill --output-dir tmp/evaluation/skill
```

Preparation preserves existing directories. A packet contains the selected protocol, the case material and instructions, without the oracle, rubric or other variants. The quick route uses only QUICKSTART's copyable request; the master route uses the full protocol; the skill route uses SKILL.md and relevant linked resources. The continuation case includes the prior checkpoint because carrying that state is the task.

Give a fresh evaluator only its packet. Do not supply this guide, suite.json, source tests, expected results, prior responses or another route. Ask it to treat cases separately and save one actual English Markdown response as R01.md through R16.md. The 220-word target is advisory; essential scope and verification requirements take priority. Do not substitute a hand-written expected answer for an observed response.

The exercise is offline and text-readable. Reading/writing files can transport the task, but it does not justify claims of web access, source authentication, scientific execution, image inspection, hashing or clock observations. No uploads, external contact or original-material changes are part of this exercise. Native installation and specialist tools need their own evaluation.

## Judge actual responses and assemble a record

A separate human or model judge reads the actual response files and the suite. For every case, record the observed outcome and every common/case-specific criterion: its ID, `pass`, `fail` or `not_assessed`, an exact response excerpt or null, and a substantive rationale. Every passing criterion needs a verbatim excerpt present in that response. The excerpt supports inspection of the judgement; it does not prove that the judgement itself is correct.

Judge the whole requirement rather than a convenient part of it. A correct case outcome does not excuse missing human-review framing, invented tool use or an unsupported scope claim. Record uncertainty and failures honestly. The responder must not rewrite its output after seeing the oracle, and a judge must not silently relax requirements or promote an unassessed criterion to pass.

The annotations file is the `judgements` array from the run schema. Once the raw responses and annotations are final, assemble them:

```text
python scripts/evaluate.py assemble --packet tmp/evaluation/quick --responses tmp/evaluation/quick-responses --judgements tmp/evaluation/quick-judgements.json --host "Actual host and execution mode" --judge "Actual judge identity" --judge-kind human --judge-notes "Actual scope and qualifications" --output evaluations/new-quick-run.json
```

Use `--judge-kind model` for a model judge. Supply `--model` only if its exact responder identity was observed; omission stores null. Assembly records its own actual timestamp, which is not a claim that the responder observed a clock. Do not describe one local test as a different provider or a native installation test.

Before reading responses, assembly verifies the manifest and actual protocol, case and instruction bytes. It also checks response hashes, quote identity and complete case/rubric coverage, and refuses to overwrite an existing output. The resulting record embeds raw responses and annotations, so temporary transport copies can be removed without losing the evidence.

## Score, compare and maintain evidence

```text
python scripts/evaluate.py score evaluations/baseline-quick.json
python scripts/evaluate.py compare evaluations/baseline-quick.json evaluations/baseline-master.json evaluations/baseline-skill.json
python scripts/check_project.py
```

A case passes only when the observed outcome matches the expected classification and every criterion passes. Missing, duplicate or unknown cases, incomplete criteria, unsupported quotes and stale protocol/input hashes cannot improve the score. Failed and unassessed criteria remain visible in the denominator. Comparison rejects duplicate route/host/model identities and states whether all three routes are covered; a successful single-route result is not a complete comparison.

Exit codes are 0 for successful preparation/all acceptance checks passed, 1 for a valid run that fails acceptance, and 2 for malformed, stale, incomplete or unreadable input. Changes to protocol files, rendered inputs or rubrics require a fresh evaluation of the affected routes. Do not edit hashes or old responses just to preserve a passing baseline. Scorer unit fixtures are explicitly fabricated plumbing tests and must never be presented as model-performance evidence.

Keep the three current reviewed baselines, their suite/contracts and synthetic fixtures. They are the evidence required by the project check and are excluded from runtime packages. Keep originals of any authorized real research outside public test data. Temporary packets, environments, extracted archives and duplicate outputs can be removed after the reviewed records are safely retained.

## Observed native-host tests — 19 October 2026

The [compatibility record](../evaluations/compatibility.json) retains the earlier v.0.0.2-source native observations: original failed runs, exact response excerpts and judgements, protocol hashes, historical quick protocol snapshots, complete executed-command lists and relevant original metadata stdout. Other read stdout is represented by hashes; temporary full JSONL transport is not retained. Workspace paths are normalized. The original successful quick record is embedded with its actual snapshot, not relabeled as a v.0.0.3 run or linked to a replacement baseline. The observations below used Codex CLI **0.163.0 on Windows**, fresh ephemeral sessions, a read-only sandbox and `approval_policy=never`. The resolved server model identifier was not exposed and remains unknown. These historical results do not establish a new native-host test of v.0.0.3.

| Real CLI exercise | Observation | Acceptance result |
| --- | --- | --- |
| ZIP skill installed at `.agents/skills/academic-paper-audit`; explicit invocation and 16 cases | The CLI read the installed skill and linked resources. Clock, hashes, byte counts and arithmetic claims matched original executed tools. | 15/16 cases, 47/48 criteria. R16 resolved F001 but omitted part of the prior text-review history. |
| Same installed skill; one relevant request without naming it | The CLI selected and read the skill and relevant resources. | Implicit selection observed once; no activation-rate claim. |
| Ordinary meeting-summary request | One-sentence summary, no skill read and no tool calls. | Non-activation observed once. |
| Pasted quick instructions; tool calls forbidden by the task | A bounded participant-flow review with no tool calls. | Text-only behavior observed; tools were not mechanically removed from the harness. |
| Full master protocol; 16 cases | All case decisions and calibration requirements passed, but reports claimed a clock read unsupported by the complete original command trace. | 0/16 fully passing cases, 32/48 criteria. Grounding failed in all 16. |
| Initial quick request; 16 cases | Correct case outcomes; R05 omitted the explicit reverse conversion required by the rubric. | 15/16 cases, 47/48 criteria. |
| Clarified quick request; fresh 16-case session | Relevant unit conversions are requested in both directions; no oracle or failed answers were supplied to the responder. | 16/16 cases, 48/48 criteria. |

The unchanged rubric was judged by a separate local model. The initial quick, native master and native skill failures remain in the compatibility record; they were not rewritten, hidden or retried until green. The separate local regression passes above use another harness. Installation/discovery worked in these Codex runs, while the native master/skill outputs did not meet full behavioral acceptance. Use the deterministic JSON exporter to retain continuation state rather than relying on a short narrative to reproduce every prior check. Independently verify claimed operations before consequential use.

Claude Code **2.1.301** was available, but `claude auth status --json` reported `loggedIn=false` and `authMethod=none`; model execution and native installation remain untested pending user sign-in. No `dsh` or `deepseek` executable was found on PATH, so DeepSeek Harness execution remains untested. No provider secrets were inspected or credentials changed. These are test preconditions, not evidence that the project is incompatible with either host.

To repeat the Codex test, build a fresh standalone-skill archive, extract its `academic-paper-audit` folder into an isolated workspace's `.agents/skills`, and prepare a fresh blind packet. The [official Codex skills guide](https://learn.chatgpt.com/docs/build-skills) describes local discovery. Invoke an explicit request with literal `$academic-paper-audit`, a relevant request without naming the skill, and an ordinary unrelated summary in separate sessions. A representative command, run from the test workspace, is:

```text
codex exec --skip-git-repo-check --ephemeral --sandbox read-only -c approval_policy=never --json -o response.txt 'Use $academic-paper-audit to review the supplied synthetic case.' > events.jsonl
```

Quote the prompt for the shell in use: PowerShell needs single quotes around the literal `$academic-paper-audit` prompt to prevent variable expansion. Store original JSONL output and inspect actual tool calls, not just the final self-report. For route evaluations, keep the prepared manifest/protocol/case bytes and use the unchanged judging/assembly procedure above. The test used the installed skill for native invocation rather than merely reading its alternative `protocol/` copy. No user-wide installation or configuration was changed. Claude project skills instead use `.claude/skills/academic-paper-audit`, as described in its [official skills guide](https://code.claude.com/docs/en/skills); installation there is not a tested result here.

## What still requires external validation

Text portability, host integration and scientific adequacy are separate questions. The project offers a text path and capability-based fallbacks; that design does not certify every future agent. Windows/Ubuntu helper and packaging execution and the bounded Codex native observations above have been tested. macOS, other native hosts, plugin loading, context-limit stress and native execution of the Python helper remain unverified. The included helpers do not implement OCR, image forensics or formal proof-checking engines.

Before making host-specific claims, test actual installation, explicit invocation, relevant automatic activation, ordinary-summary non-activation, context limits and missing-tool behavior in that host. Record observed model/version, date, mode, capabilities, hashes, outcomes and failures. Before making scientific accuracy claims, obtain authorized literature, qualified independent reviewers, legitimate and ambiguous controls, and appropriate metrics by domain and evidence quality. Language and specialist terminology need their own expert assessment. No current record supports a blanket accuracy claim across research fields, languages or modalities.
