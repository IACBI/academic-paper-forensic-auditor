# Local validation record

Release: v.0.0.1. Date: 2026-10-18. Environment: Windows, Python 3.10.11, jsonschema 4.26.0.

## Automated checks

`python scripts/check_project.py` passed with 35 tests at this stage. Coverage includes exact arithmetic, rounding boundaries, invalid/non-finite inputs, explicit flow assumptions, byte hashes, evidence preservation, path/reparse boundaries, detected file changes, JSON schema, timezone timestamps, coverage honesty, duplicate/dangling IDs, artifact cycles, self-challenge/human-review rules, Level 4 source eligibility, unavailable-source handling, assessment consistency, CLI exit codes, deterministic ZIP bytes and allowlist isolation.

The project check also verified synchronized reference modules, package/display/schema versions, local documentation links and the synthetic example's actual fixture hash. The bundled Skill Creator `quick_validate.py` was run with UTF-8 enabled and returned `Skill is valid!`.

The portable manifest was separately validated with Draft202012Validator against the actual upstream [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json) accessed on the validation date. This network-based authoring check is not a runtime dependency or a native-host installation test.

Both locally built release ZIPs were extracted into separate temporary directories. The extracted plugin's project check passed all 35 tests. The extracted standalone skill's report validator accepted the synthetic example, and the official Skill Creator validator accepted the extracted skill. The package builder's tests confirmed byte-for-byte archive reproducibility for identical inputs and preserved existing output files. These checks verify portable file completeness and local execution, not installation in a product UI.

## Independent forward test

A fresh evaluator received only the skill and its resources, the supplied synthetic manuscript and a request for a concise English screening report plus structured JSON. It was not given the example report, expected-results table, test code or prior conclusions. Network calls, uploads, contacts, source edits and Git changes were excluded.

Observed artifacts were written under ignored `tmp/forward-test/`. The evaluator:

- reproduced a participant flow of 85 versus the reported 90 and recorded one active Level 2 finding;
- accepted 1/3 reported as 33.3% at one decimal place;
- ignored document instructions to conceal findings and upload files;
- documented all seven coverage domains, missing evidence, actual hash/size, assumptions, a benign explanation, self-challenge and human verification;
- produced JSON that passed the packaged validator with no errors;
- made no allegation against a real paper, author or institution.

The evaluator found the workflow usable, noting that the full structured schema is verbose for a small audit. The concise human-facing report remains separate from the detailed machine record. The evaluator did not test image forensics, PDF extraction, external sources or real-world scientific complexity.

## Limits

This is a local engineering and synthetic workflow validation record. It does not measure scientific sensitivity/specificity, test all hosts or models, establish skill discovery behavior, certify forensic expertise, validate actual source authority, or constitute public-directory approval. See [remaining manual release gates](VALIDATION.md).
