# Open Prompt Archive — Copilot Instructions

Open Prompt Archive is a public, provenance-first and license-aware archive of third-party openly redistributable AI prompts plus tooling for normalizing, validating, indexing and searching those datasets.

## Scope

- Only third-party material with evidence-backed redistribution rights belongs in this repository.
- First-party, private, proprietary or otherwise out-of-scope collections must not be imported.
- Public accessibility is not permission to redistribute.
- Do not import prompt data until its source is registered and its redistribution basis is verified.
- Do not mirror third-party images, video or audio unless those media rights are independently verified.

## Repository map

- `README.md` — public project overview and scope.
- `AGENTS.md` — repository-wide automation guidance.
- `docs/LICENSING_POLICY.md` — source acceptance and provenance policy.
- `sources/sources.yaml` — source registry and approval states.
- `schema/prompt.schema.json` — canonical normalized prompt schema.
- `data/` — canonical approved prompt data only.
- `scripts/` — deterministic import, normalization, validation and index tooling.

## Working rules

1. Read `AGENTS.md` and the licensing policy before changing source or dataset files.
2. Use professional English for repository-facing content unless explicitly instructed otherwise.
3. Never invent source counts, licenses, authors, dates, model compatibility, test results or verification states.
4. Preserve canonical URLs, revisions, attribution and provenance identifiers.
5. Prefer quarantine or review over guessing when rights or provenance are ambiguous.
6. Keep canonical data separate from generated caches and indexes.
7. Make normalization and validation deterministic and reproducible.
8. Never commit credentials, cookies, tokens, private datasets or local environment files.

## Data changes

For changes under `data/` or `sources/`, confirm the source identity, license evidence, content scope, third-party aggregation risk, attribution obligations, reviewed revision and evidence-backed status. Prompt records must validate against the canonical schema.

Do not collapse duplicate prompt text when doing so would erase independent provenance.
