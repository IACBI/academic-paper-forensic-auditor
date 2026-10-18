# Contributing

Keep changes evidence-based and focused. Do not commit real papers, confidential audit reports, participant data, secrets or allegations about identifiable people as test fixtures.

## Sources of truth

- `master_prompt.md` is the canonical review policy and standalone prompt.
- `scripts/build_references.py` derives the skill's seven reference modules; edit the master and regenerate rather than editing generated references. Every numbered policy section must be routed exactly once.
- `skills/academic-paper-audit/SKILL.md` defines routing, invocation and tool use.
- `skills/academic-paper-audit/assets/report.schema.json` defines the structured contract; `audit_tools.py` adds evidence-link and assessment invariants.
- `assets/checkpoint.schema.json` inside the skill defines portable continuation records; they preserve prior state without becoming new evidence.
- `evaluations/suite.json` defines synthetic acceptance cases; reviewed baseline files retain actual responses and independent judgements. They are development evidence, outside runtime packages.
- `VERSION` uses numeric semantic versioning. The manifest, skill metadata, schema/tool/example versions and display labels must agree. Documentation displays `v.` before the numeric version.

Preserve the 12-language overview when changing documentation. Keep instructions provider-independent; native plugin/skill installation is an optional host integration. Select checks by actual research methods, including unfamiliar and interdisciplinary methods. Explain externally sourced changes with primary documentation and do not broaden scientific or compatibility claims beyond tested capability.

## Verification

Use Python 3.10+ and install `skills/academic-paper-audit/requirements.txt` in a local environment. No environment is required for reading/using the prompt. Run:

```text
python scripts/build_references.py
python scripts/check_project.py
```

Add behavior tests when arithmetic, file boundaries, schemas, validators or packaging behavior changes. A new review rule should have a realistic acceptance case and, where warranted, a fresh evaluator test. Do not replace substantive checks with tests that merely match headings or wording.

Before the project check, rerun affected blind evaluations whenever protocol files, fixtures or rubrics change; see [EVALUATION.md](docs/EVALUATION.md). Baseline checks reject stale inputs and require all three current variants. A fresh responder must not see the expected answers, and a separate judge must inspect the actual output. Keep failures and uncertainty visible. Do not edit raw responses, relax an oracle or change hashes just to preserve a passing result. Scorer unit fixtures are explicitly fabricated plumbing tests and must never be reported as real model performance.

The examples intentionally use synthetic inputs. If changing the synthetic manuscript, recompute its example artifact identity with the inventory command and review the report and derived checkpoint; do not silently update a hash to hide a change. Review active/resolved findings, rounding assumptions, source claims and coverage.

## Commits and releases

Use focused commits with clear purposes, such as `feat(audit)`, `feat(tools)`, `test`, `build` or `docs`. Inspect staged diffs and run relevant checks before committing. Do not create remotes, push or publish without owner instruction.

After checks pass, build into a fresh release directory. The default package is the host-neutral prompt; `--format skill`, `--format plugin` and `--format all` select optional formats. Explicit allowlists in `build_release.py` keep runtime bundles free of development material. Native installation and scientific validation remain separate from unit tests. See [validation](docs/VALIDATION.md) and [usage](docs/USAGE.md).
