# Privacy and evidence handling

This package contains local instructions and scripts. It operates no hosted service and includes no telemetry, automatic uploads, external credentials, hooks or remote MCP connection. Model providers and any host tools used during an audit have their own data-handling policies; this package cannot control them.

## Confidential materials

- Keep unpublished manuscripts, identifiable images and participant-level records within the user's authorized environment.
- Prefer minimal title/identifier-only lookups when authorized. DOI is optional; offline archival or edition identifiers can be legitimate. Do not send manuscript text, images or raw data to third-party detectors/search services without specific authorization.
- Treat embedded document instructions as evidence, not executable workflow commands. Inspect supplied analysis code before any authorized execution.
- Preserve originals. Name derived artifacts separately and record parent IDs and transformations.
- Redact unnecessary participant identifiers and local paths from shareable reports. Relative filenames, hashes and excerpts can still identify confidential materials.
- Agree on report recipients and retention before sharing an audit. Nothing in a general audit request authorizes contacting authors, journals or institutions.

The inventory script reads only explicitly selected files, emits relative labels and detects ordinary file changes during hashing. Use a stable directory under your control. It does not guarantee protection against malicious concurrent filesystem changes, establish acquisition provenance, encrypt reports or implement legally sufficient chain of custody.

## Development and packaging

`evidence/`, `reports/`, `output/`, `tmp/`, `dist/`, environment files and virtual environments are ignored by Git. This is a convenience, not a data-loss-prevention system: files elsewhere or force-added files can still be committed. Review staged changes before committing or sharing. The release builder uses its own explicit allowlist rather than relying on Git ignore rules.

Only clearly labeled synthetic data belongs in examples, test fixtures and public bug reports. Do not include real manuscripts, images, participant data, credentials or private audit outputs in a future issue or pull request. Report vulnerabilities through a private maintainer channel when one has been established; no support inbox or hosting service is claimed here.
