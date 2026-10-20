# Changelog

## v.0.0.4 — 2026-10-20

- Reject active findings whose evidence is outside the assessed domain, closed findings without evidence-backed reasons, and whitespace-only evaluation excerpts. Add independent human-review records without changing model evidence levels.
- Embed the complete source report and a canonical JSON digest in checkpoint exports; reject conflicting/tampered summaries and warn on missing legacy source history. Existing released archives/tags remain unchanged. Older reports needing closure history must be corrected from actual evidence; do not invent migration data.
- Add explicit-path evidence rechecking with dependency propagation, same-audit report differences, inert Markdown/HTML output, and optional local PDF/UTF-8 extraction with page/line locators. PDF extraction is not OCR, image analysis or a sandbox.
- Add a 24-case robustness suite and isolated per-case packet preparation/session bookkeeping. Preserve original v.0.0.3 model baselines with their actual source snapshots; new model/expert evaluations remain pending.
- Extend regression and optional PDF integration tests, CI and all 12 user guides. Check translated workflow command coverage and reference-style local links.

## v.0.0.3 — 2026-10-19

### Reliable continuation records

Preserve recorded research context, domain limitations and completed-check links when exporting a JSON continuation record. Reject completed or partial coverage without completed evidence-linked work and reject inconsistent declared links. New v.0.0.3 checkpoints require domain reasons and check links with matching schema/protocol versions. Keep consistent v.0.0.2 checkpoints readable without relabeling them, with explicit warnings for missing history. Eight added regression tests bring the software suite to 81 tests. Update the continuation example and all 12 user guides.

### Observed agent behavior

Run isolated real Codex CLI checks for native skill discovery, explicit and implicit use, ordinary-summary non-activation, text-only operation and the three synthetic review routes. Retain failures rather than presenting format compatibility as complete behavioral acceptance. Clarify the quick request's numerical-comparison instructions after an observed omission of a required reverse unit conversion.

### Release contracts and distribution

Publish v.0.0.3 prompt, skill and plugin archives with SHA-256 checksums. Refresh all three blind acceptance routes against their actual v.0.0.3 snapshots. Preserve earlier native-host observations at their tested v.0.0.2 source versions, including the original successful quick response record, rather than pointing historical evidence to a replaced baseline. New reports use the v.0.0.3 contract; retain older reports with their matching release helper. Previous tags and release assets remain unchanged.

## v.0.0.2 — 2026-10-19

### Windows inventory correction

Correct a false file-change error on Windows/Python 3.14, where path-based and descriptor-based stat calls can assign different meanings to the change-time field. Compare identity, size and modification time across APIs, and retain full before/after stability checks within each API. Add three regression tests for unchanged files with different timestamp meanings and actual path/descriptor changes, bringing the suite to 73 tests. The original failure was reproduced on the official Windows Python 3.14.8 build before the fix and passed afterward.

### Documentation

Restore complete, equivalent user guides in all 12 README languages, with inline language navigation directly below the title. Each guide covers setup, request settings, delivery formats, research methods, report interpretation, privacy, continuation and optional local tools. Consolidate user instructions into the README and evaluation procedures into the validation guide; remove the superseded usage manual, internal project review and obsolete standalone regression output.

Present version, license and live CI status as centered badges with rounded corners. Remove the author badge and localize each end-of-language link as “Back to top.” Clarify analysis-depth and descriptive settings in every language.

### Distribution and evaluation

Publish new v.0.0.2 prompt, skill and plugin packages with matching checksums. Preserve the original v.0.0.1 tag and assets. Refresh blind evaluations against the actual v.0.0.2 protocol snapshots rather than changing hashes in old response records. Structured examples and contracts identify v.0.0.2; retain historical v.0.0.1 records with their matching version rather than relabeling old observations as newly verified evidence.

## v.0.0.1 — 2026-10-19

### Review protocol

The initial release provides a standalone master protocol, a short request, a modular Agent Skills folder and an optional skills-only plugin. Plain-text review requires no vendor integration or Python setup. Checks adapt to quantitative, qualitative, computational, formal, engineering, archival, synthesis, conceptual and interdisciplinary research, including unfamiliar methods.

The evidence contract records source identity, version, scope, coverage, reproducible observations, benign alternatives and human-review requirements. It separates reporting gaps, methodological limits and integrity concerns, supports offline source identifiers, and preserves resolved findings across sessions. Metadata, notices and numerical anomalies are interpreted within their evidentiary limits rather than treated as automatic misconduct verdicts.

### Local helpers and structured records

Optional Python helpers provide explicit-file inventory, exact percentage compatibility, participant-flow arithmetic, report validation and continuation export/validation. The report and checkpoint schemas enforce structured records alongside local cross-reference and assessment checks. Synthetic examples demonstrate the workflow, while templates support human-readable output when strict structured data or observed timestamps are unavailable.

### Verification and distribution

The release includes 70 behavior tests, reference synchronization, version/link checks, and deterministic allowlisted prompt, skill and plugin archives. A balanced blind evaluation covers 16 synthetic cases per route with separate quote-backed model judgements; current baselines retain actual responses and source snapshots. The scorer rejects stale inputs, altered packets, incomplete criteria and unsupported excerpts.

GitHub distribution provides three archives, SHA-256 checksums, a bug-report form and pinned CI on Windows/Ubuntu with Python 3.10/3.14. The Windows packaging-test fixture resolves temporary-path aliases consistently with the production root. Native host installation and scientific detection performance remain separate from these tested software and synthetic acceptance results.

This release does not claim professional certification, comprehensive forensic detection or verified scientific accuracy.
