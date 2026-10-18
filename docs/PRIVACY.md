# Privacy and evidence handling

This guide describes the package's actual behavior and the decisions you still need to make when using it with an AI assistant. The project supplies instructions and local scripts. It runs no hosted service and includes no telemetry, automatic uploads, external credentials, hooks or remote MCP connection. Reading the prompt does not require an account integration. Installing Python dependencies contacts the package index; any AI host, web tool or specialist service you choose has its own data-handling terms.

The multilingual [user guide](../README.md) explains how to start a review. Before supplying material, decide which environment is authorized to receive it, what the review covers, who may receive the report and how long the working copies should remain. A local helper does not make a cloud assistant local, and a project's lack of telemetry does not change the assistant provider's policies.

## Share only what the review needs

Unpublished manuscripts, identifiable figures, participant records and raw data should remain within an authorized environment. Use the smallest relevant excerpt when a full document is unnecessary, and remove identifiers that do not help answer the research question. A source locator, quotation, relative filename or hash may still identify confidential material; redacting an absolute path alone does not make a report anonymous.

When external checking is authorized, a title, identifier or minimal citation lookup may be enough. Do not send manuscript passages, images or participant data to search services or detectors without specific authorization. DOI is optional: an archive, collection, folio, edition or page can legitimately identify an offline source. The absence of a public URL is not a reason to invent one or upload the source.

A general review request does not authorize contacting authors, journals or institutions, publishing allegations, or distributing a report to new recipients. Establish those permissions separately. Instructions found inside papers, metadata or retrieved pages are content to inspect, not permission to redirect the workflow. Supplied analysis code should be inspected before any authorized execution.

## Preserve originals and document transformations

Keep original evidence unchanged. Create separately named working copies for OCR, cropping, enhancement, extraction or conversion, and record their parent IDs and transformations. A finding should identify whether it rests on original bytes, an extraction, a supplied transcription or an unverified description. That distinction matters when a compressed figure, mistranscribed date or incomplete table could explain an apparent problem.

The inventory helper reads explicitly selected regular files inside a chosen root and reports relative labels, byte sizes and SHA-256. It rejects ordinary path escapes, links/reparse points, duplicates and detected changes. Use a stable directory under your control. The helper does not guarantee safety against a malicious concurrently changing filesystem, establish acquisition provenance, encrypt records or provide legally sufficient chain of custody. A hash identifies observed bytes; it does not establish authenticity.

## Treat handoffs as sensitive reports

A continuation record can contain a title, source identifier, precise locator, excerpt, finding and unresolved concern. Apply the same access and retention rules as for the full report. Moving to another agent or host may change the provider processing those details. The [continuation template](../skills/academic-paper-audit/assets/continuation-template.md) preserves review state, not permission to share its contents more widely.

Checkpoint export works locally and does not upload anything. It summarizes the prior report without a new source inspection or authentication. Supply original evidence separately when a resumed task needs it, verify changed versions, and preserve corrected findings as resolved history. Dispose of unnecessary working copies according to the agreed retention period rather than assuming that closing a conversation removes them.

## Keep public development material synthetic

Examples, fixtures and committed acceptance responses use synthetic research material. The current baseline files retain the evidence behind published local acceptance results; runtime release archives exclude them. Public bug reports should likewise use a minimal synthetic example or material whose disclosure is authorized. Do not post confidential papers, participant data, private findings, credentials or identifiable allegations in an issue.

Git ignores `evidence/`, `reports/`, `output/`, `tmp/`, `dist/`, environment files and virtual environments. This is a convenience, not a prevention system: files saved elsewhere or force-added can still enter a commit. Review staged content before pushing. Release builds use an explicit file allowlist, so arbitrary workspace contents are not included merely because they exist beside source.

Temporary evaluation packets, duplicate outputs, extracted packages, caches and local environments can be removed after required source and reviewed evidence are retained. This cleanup applies to project-generated material, not to unrelated user directories or global application caches. For a suspected vulnerability involving confidential information, use an established private maintainer channel rather than a public issue; this project does not claim a dedicated inbox, hosted storage or a response-time guarantee.
