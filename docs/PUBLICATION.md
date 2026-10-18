# Packaging and future publication

The local package is a **skills-only plugin** and can also be distributed as a standalone skill or prompt. There is no remote repository, remote MCP server, account integration, automatic deployment or public directory submission in this project setup.

## Local release

Run checks and then `python scripts/build_release.py` as described in [usage](USAGE.md). Keep the plugin ZIP's `plugin.json` and `skills/` at the archive root. The standalone skill ZIP has an `academic-paper-audit/` top-level folder, including LICENSE. Both archives use the numeric machine version from `VERSION`; documentation displays v.0.0.1.

The manifest uses the portable Agent Plugins schema linked by current OpenAI documentation. Local checks verify the manifest identity/version and files; they do not replace a host's manifest/schema validation or successful installation. Native host validation remains a manual release gate. No synthetic website, support address, screenshots, domain, review credential or repository URL is inserted into the manifest.

## Before a public submission

- Complete the native host checks and independent domain evaluations in [validation](VALIDATION.md).
- Confirm the publisher identity and actual support/privacy information required by the chosen distribution channel.
- Review all packaged files and license notices; keep evidence and private reports outside the bundle.
- Confirm current submission rules, supported surfaces and whether the proposed future tool architecture changes the submission path.
- Submit only when the owner explicitly requests publication. Packaging does not submit or approve a listing.

The OpenAI submission documentation accessed on 2026-10-18 states that adding an MCP server to an existing skills-only plugin is not currently supported. A future hosted tool service should therefore be planned before a public listing is created; local evolution of this source package is separate from public migration support.

## Documentation consulted

The Context7 MCP tool was not exposed in the authoring environment; current primary documentation was used directly.

- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills) — skill structure, supporting resources and evaluation.
- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins) — portable root manifest and package layout.
- [OpenAI: Plugin architecture](https://developers.openai.com/plugins/concepts/plugins) — skills-only workflows and optional MCP tools.
- [OpenAI: Upload and submit](https://developers.openai.com/plugins/deploy/submission) — review/publication workflow and migration limitations.
- [jsonschema: Validation](https://python-jsonschema.readthedocs.io/en/stable/validate/) — Draft 2020-12 validator, schema checks and format validation limits.

Access date: 2026-10-18. These are implementation references, not endorsement, certification or publication approval.
