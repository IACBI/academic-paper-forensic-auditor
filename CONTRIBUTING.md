# Contributing

Keep changes evidence-based and focused. Do not commit real papers, confidential audit reports, participant data, secrets or allegations about identifiable people as test fixtures.

## Sources of truth

- `master_prompt.md` is the canonical review policy and standalone prompt.
- `scripts/build_references.py` derives the skill's five reference modules; edit the master and regenerate rather than editing generated references.
- `skills/academic-paper-audit/SKILL.md` defines routing, invocation and tool use.
- `skills/academic-paper-audit/assets/report.schema.json` defines the structured contract; `audit_tools.py` adds evidence-link and assessment invariants.
- `VERSION` uses numeric semantic versioning. The manifest, skill metadata, schema/tool/example versions and display labels must agree. Documentation displays `v.` before the numeric version.

Preserve the 12-language standalone guide when changing packaging documentation. Explain externally sourced technical changes with primary documentation. Do not broaden clinical, legal or scientific claims beyond tested capability.

## Verification

Use Python 3.10+ and install `requirements-validation.txt` in a local virtual environment. Run:

```text
python scripts/build_references.py
python scripts/check_project.py
```

Add behavior tests when arithmetic, file boundaries, schemas, validators or packaging behavior changes. A new review rule should have a realistic acceptance case and, where warranted, a fresh evaluator test. Do not replace substantive checks with tests that merely match headings or wording.

The examples intentionally use synthetic inputs. If changing the synthetic manuscript, recompute its example artifact identity with the inventory command and review the report; do not silently update a hash to hide a change. Review active/resolved findings, rounding assumptions, source claims and coverage.

## Commits and releases

Use focused commits with clear purposes, such as `feat(audit)`, `feat(tools)`, `test`, `build` or `docs`. Inspect staged diffs and run relevant checks before committing. Do not create remotes, push or publish without owner instruction.

After checks pass, build into a fresh release directory. The explicit allowlist in `build_release.py` is a deliberate distribution boundary; update it only when new files actually belong in a release. Native host installation and scientific validation remain separate from unit tests. See [validation](docs/VALIDATION.md) and [publication](docs/PUBLICATION.md).
