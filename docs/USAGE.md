# Use with your preferred AI agent

Display release: **v.0.0.1**; machine version: `0.0.1`.

## Start without installation

Copy the request in [QUICKSTART.md](../QUICKSTART.md), or paste/attach [master_prompt.md](../master_prompt.md), into the chosen assistant. Supply readable material and state language, scope and length. A scoped text review needs no Python, plugin, API key, native skill loader or vendor command.

If a file is unreadable, paste targeted excerpts. For limited context, use bounded passes and retain article/version, evidence IDs, inspected locations, findings, limitations and next steps. Do not treat an excerpt or a summary as the unseen full paper. The quick request is an orientation; the master contains the full protocol.

## Select checks by method

Identify claims, methods and evidence first. Routes cover quantitative, qualitative, mixed, computational, formal/theoretical, engineering/measurement, archival/humanities, synthesis and conceptual/practice-based work, with an explicit route for other/unfamiliar methods. Use disciplinary standards only when scope, version and applicability are established.

The seven coverage domains are stable report categories, not seven mandatory experiments. Proofs need not have p-values, qualitative work need not report inter-rater agreement, narrative reviews need not pool effects, and archival sources need not have URLs. Distinguish not_applicable from relevant but not_assessed. A reporting gap or disagreement is not automatically an integrity concern.

## Capability-based compatibility

| Host capability | Actual operation | Limitation |
| --- | --- | --- |
| Text only | Supplied claims, arguments, excerpts and shown arithmetic | No unseen files, original metadata, pixels or live sources |
| Document/file reading | Actually read content | OCR/layout/equations need checking; file access does not authenticate it |
| Vision | Visible features in supplied renderings | No pixel/AI-provenance claim without actual tools |
| Computation | Executed calculations/hash checks | Unexecuted code and missing data remain unverified |
| Web/databases | Actually read sources or retrieved metadata | Inaccessible sources and unqueried databases remain unverified |
| Specialist tools | Actually run proof/domain-tool outputs | Tool assumptions and scope still limit the conclusion |

Packaging compatibility is separate from capability. A standard folder does not make every host recognize, invoke or execute it. Cross-provider behavior is not established by one local evaluator.

## Optional open-format skill

Load the complete `skills/academic-paper-audit/` folder through the chosen host's supported mechanism. It follows the [Agent Skills specification](https://agentskills.io/specification) using standard frontmatter and relative paths. Paths, native commands and discovery are host-specific; do not assume one user directory or `$...` command works everywhere. The plain-text path remains available.

Keep linked references/assets and optional scripts together. No vendor metadata, provider SDK or MCP service is required. Generated references are necessary runtime resources inside the portable skill folder, not independently maintained policy copies.

## Optional local helpers

Python 3.10+ is needed only for helpers/development. Report/checkpoint validation and checkpoint conversion need the pinned jsonschema dependency. Hashing/arithmetic use the standard library. Helpers make no runtime network request and contain no telemetry; dependency installation contacts the package index.

Use a suitable environment, for example `python -m venv .venv`. Its interpreter is `.venv/Scripts/python.exe` on Windows or `.venv/bin/python` on macOS/Linux; `python` below means the chosen interpreter:

```text
python -m pip install -r skills/academic-paper-audit/requirements.txt
python skills/academic-paper-audit/scripts/audit_tools.py inventory --root evidence paper.pdf
python skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
python skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
python skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
```

Inventory reads explicit regular files within a root and emits relative labels, sizes and SHA-256. It rejects path escapes, links/reparse points, duplicate paths and detected changes. Use stable directories under your control: this is not a secure reader for a hostile concurrent filesystem or legal chain of custody. Preserve existing evidence IDs when merging inventories.

Percentage compatibility uses exact rational arithmetic and a conservative half-unit nearest-rounding interval including ties (0-12 places). It assumes ordinary unweighted counts and the intended denominator; truncation, weights and multiple-response percentages require different reasoning. Flow requires disjoint losses in one population/timepoint. Helpers assign neither evidence levels nor intent.

These tools do not extract PDFs/EXIF, perform OCR, compare image pixels, run proof checkers or detect AI material. Use a verified host equivalent if actually available. Otherwise continue applicable checks and disclose the missing operation.

## Output contract

Markdown/plain text is the default portable output: disclaimer, method context, coverage, evidence-backed findings, evidence against concerns, limits and next checks. The [template](../skills/academic-paper-audit/assets/report-template.md) is scalable; omit irrelevant empty sections. Short human reports may group domains sharing the same status/reason.

JSON is optional. The [schema](../skills/academic-paper-audit/assets/report.schema.json) uses seven domains, stable IDs and explicit nulls where supported. Optional audit.research_context and finding.issue_kind accept existing reports. Offline sources use `url: null` and a nonempty identifier (archive/collection/folio or edition/page), never a fabricated URL. Strict timestamps require observed time; if unavailable, use a human report and disclose it.

Validation checks structure, timezones, links, coverage, derivation cycles, challenge/review requirements, source eligibility and some contradictions. It cannot establish truth, actual source access, authority, honest tool use or scientific accuracy. Invalid reports have null finding counts, not misleading zeros. The [synthetic example](../examples/synthetic-report.json) is a worked text/arithmetic case, not an accuracy benchmark.

Exit codes: 0 successful command/valid report or checkpoint, 1 invalid report or checkpoint, 2 invalid input/unreadable file/missing dependency. An arithmetic mismatch is successful computation output, not a software failure.

## Continue with another session or agent

Use the [continuation template](../skills/academic-paper-audit/assets/continuation-template.md) for a plain-text handoff. Supply the source material separately. Preserve article/version, scope, evidence/source IDs, inspected locations, completed checks, finding IDs/status, limitations and pending work. Verify changed evidence before updating a finding; retain resolved findings as history and exclude them from active counts. Recheck relevant changes rather than automatically repeating unrelated completed work.

An optional [checkpoint schema](../skills/academic-paper-audit/assets/checkpoint.schema.json) supports unknown timestamps/hashes with explicit limitations. From a valid structured report:

```text
python skills/academic-paper-audit/scripts/audit_tools.py checkpoint examples/synthetic-report.json
python skills/academic-paper-audit/scripts/audit_tools.py validate-checkpoint examples/synthetic-checkpoint.json
```

The first command prints JSON; save stdout as UTF-8 in an authorized location when needed. The [worked checkpoint](../examples/synthetic-checkpoint.json) summarizes the existing synthetic report without a new inspection or clock observation. Conversion preserves the prior record's time, identity and scope. A checkpoint is a resumable summary, not fresh evidence, authentication or permission to access new material.

## Optional distribution

```text
python scripts/build_references.py
python scripts/check_project.py
python scripts/build_release.py
python scripts/build_release.py --format skill --output-dir dist/skill
python scripts/build_release.py --format plugin --output-dir dist/plugin
```

The default archive contains the quick start, master, optional report/checkpoint schemas and templates, and MIT license. Skill archives contain runtime resources and LICENSE. Optional plugin.json targets compatible Agent Plugins hosts; it is not the universal entry point. Explicit allowlists, stable ZIP metadata and exclusive creation prevent arbitrary workspace inclusion and preserve existing outputs. Use a fresh output directory for rebuilding.

No script installs globally, configures accounts, creates remotes or publishes. Native installation/approval and actual publisher identity/support/privacy information are separate gates. Recheck current listing and migration rules before publication, especially before adding hosted tools. See [validation](VALIDATION.md), [privacy](PRIVACY.md) and [detailed review](REVIEW_TR.md).
