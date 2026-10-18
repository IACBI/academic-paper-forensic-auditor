# Usage and installation

Display release: **v.0.0.1**. Machine-readable versions use `0.0.1` to satisfy semantic-version fields. Python 3.10+ is required only for local helper commands. Reading or pasting the prompt needs no Python environment.

## Choose a format

| Format | Use | Contents |
| --- | --- | --- |
| Standalone prompt | Paste into a capable AI system | Root `master_prompt.md`; edit its final USER INPUT defaults |
| Standalone skill | Install in a compatible skill host | Entire `skills/academic-paper-audit/` folder, including references, assets, scripts and requirements |
| Plugin | Package the workflow for compatible plugin hosts | Root `plugin.json` and `skills/`; no MCP server, credentials, hooks or remote service |

The skill and prompt express the same audit rules. References are generated from the master prompt; the skill loads relevant modules selectively. Do not paste every reference when only a focused check is needed. A host still needs appropriate file, image, computation and web tools for the requested checks. Installation does not create those capabilities.

## Standalone prompt

1. Copy all of `master_prompt.md` to the AI system.
2. Set language, audience, length, depth and priority in USER INPUT, or state these explicitly in your request.
3. Attach the paper and, where authorized, supplementary files or original evidence.
4. Request a report bounded by actual capabilities and available evidence.

An English or Turkish request can override the English default without editing the source. Short output still includes scope, limitations and evidence against concerns. Never supply confidential material to a service unless its use is authorized for that material.

## Local skill

Use the host's supported local skill installer, or copy the entire `skills/academic-paper-audit` directory into its skill directory. For Codex, a user-level location is `~/.codex/skills/academic-paper-audit`. Do not copy only `SKILL.md`; its linked resources are part of the skill. The release builder supplies LICENSE in the standalone skill ZIP.

Example invocation:

```text
Use $academic-paper-audit to screen this paper in Turkish. Focus on participant
flow and Figures 2-4. Give a concise report with coverage, reproducible findings,
benign explanations and the original evidence needed for further review.
```

The skill permits normal automatic discovery for integrity-audit requests. It is not intended to activate for ordinary summaries, rewriting or general scientific explanations. No global installation or host configuration changes are performed by this repository's build scripts.

## Local helper setup

From the project root on Windows PowerShell:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements-validation.txt
.venv/Scripts/python.exe scripts/check_project.py
```

On macOS/Linux use `.venv/bin/python` in place of `.venv/Scripts/python.exe`. A standalone skill installation can install its own `requirements.txt` into an appropriate environment. Only the JSON validator requires the pinned `jsonschema` package; hashing and arithmetic use Python's standard library. There is no telemetry or runtime network dependency. Dependency installation itself contacts the configured package index.

## Evidence inventory

Supply an explicit root and explicit files; there is no recursive discovery:

```powershell
.venv/Scripts/python.exe skills/academic-paper-audit/scripts/audit_tools.py inventory --root evidence paper.pdf figures/figure1.tif
```

The command reads bytes and prints a JSON inventory with relative labels, byte sizes, SHA-256 and an observation timestamp. It rejects duplicate paths, paths outside the root, symlinks/reparse points, non-regular files and detected changes during hashing. Use a stable local evidence directory under your control; this is not a secure reader for a concurrently hostile filesystem or a legal chain-of-custody system. Hashes prove neither experiment authenticity nor provenance. Preserve existing artifact IDs when adding another inventory to a report.

These helpers do not extract PDF text, inspect EXIF, perform OCR, compare image pixels or detect AI imagery. Record those checks as unavailable unless separate appropriate tools actually run. Preserve originals and record every derived image's parent, crop coordinates, coordinate origin, scale and transformations.

## Arithmetic

```powershell
.venv/Scripts/python.exe skills/academic-paper-audit/scripts/audit_tools.py percentage --count 1 --total 3 --reported 33.3 --places 1
.venv/Scripts/python.exe skills/academic-paper-audit/scripts/audit_tools.py flow --initial 100 --excluded 10 --dropouts 5 --analyzed 90 --disjoint
```

Percentage compatibility uses exact rational arithmetic and a conservative half-unit rounding interval (percentage points), including boundary ties. It supports 0-12 decimal places. Establish unweighted counts, the actual denominator and nearest rounding before interpreting the result. Weighted percentages, multiple-response categories and truncation require different reasoning.

Flow requires disjoint exclusions/dropouts in the same population/timepoint. If this is not established, omit the test rather than asserting the assumption. Results expose inputs, assumptions and limitations; they do not assign finding levels. A mismatch is returned as successful calculation output, not a software failure.

## Reports

Use the packaged Markdown template or JSON schema. A worked [synthetic JSON report](../examples/synthetic-report.json) corresponds to [synthetic text](../tests/fixtures/synthetic_manuscript.md); it implicates no real publication.

```powershell
.venv/Scripts/python.exe skills/academic-paper-audit/scripts/audit_tools.py validate-report examples/synthetic-report.json
```

The validator checks Draft 2020-12 schema, timezone-bearing timestamps, unique IDs, evidence references, coverage, derivation cycles, challenge requirements, source eligibility and some assessment contradictions. It derives active finding counts; resolved/withdrawn findings are excluded. It cannot verify factual truth, source authority, actual source access, honest tool use, proper scientific interpretation or completeness of free text. A valid JSON file is not a verified scientific finding.

Exit codes: `0` successful command/valid report; `1` structurally or semantically invalid report; `2` invalid input, unreadable file or unavailable validator dependency. Errors go to stderr; results go to stdout. Output JSON escapes non-ASCII characters for portable Windows piping. Choose an appropriate UTF-8 writer if saving human-readable Unicode output from other tools.

## Rebuild and package

```powershell
.venv/Scripts/python.exe scripts/build_references.py
.venv/Scripts/python.exe scripts/check_project.py
.venv/Scripts/python.exe scripts/build_release.py
```

The release builder produces plugin and standalone skill ZIPs in `dist/`. It uses an explicit file allowlist and stable ZIP metadata so identical inputs yield identical archives. It refuses to overwrite existing archives; use a fresh `--output-dir` for a rebuild. Run project checks first. No evidence, reports, environments, Git metadata or secrets are packaged. A release ZIP is an installation candidate, not an approved public listing. See [publication](PUBLICATION.md) and [validation](VALIDATION.md).
