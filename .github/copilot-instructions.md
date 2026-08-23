# Open Prompt Archive — Copilot Instructions

Open Prompt Archive is a public, provenance-first and license-aware archive of **third-party openly redistributable AI prompts** plus tooling for normalizing, validating, indexing and searching those datasets.

## Scope

- Do not add Carnaverone Studio first-party/private prompt collections to this repository.
- Do not treat public accessibility as permission to redistribute.
- Do not import third-party prompt data until its source is registered and its redistribution basis is verified.
- Do not mirror third-party images, video or audio unless those media rights are independently verified.

## Repository map

- `README.md` — public project overview and scope.
- `AGENTS.md` — repository-wide agent governance.
- `docs/LICENSING_POLICY.md` — source acceptance and provenance policy.
- `sources/sources.yaml` — source registry and approval states.
- `schema/prompt.schema.json` — canonical normalized prompt schema.
- `data/` — canonical approved prompt data only.
- `scripts/` — deterministic import/normalization/validation/index tooling.
- `.github/skills/` — task-specific Agent Skills.

## Working rules

1. Read `AGENTS.md` and the licensing policy before changing source or dataset files.
2. Use professional English for repository-facing content unless explicitly instructed otherwise.
3. Never invent source counts, licenses, authors, dates, model compatibility, test results or verification states.
4. Preserve canonical URLs, revisions, attribution and provenance identifiers.
5. Prefer quarantine/review over guessing when rights or provenance are ambiguous.
6. Keep canonical data separate from generated caches/indexes.
7. Make normalization and validation deterministic and reproducible.
8. Never commit credentials, cookies, tokens, private datasets or local environment files.

## Data changes

For changes under `data/` or `sources/`, confirm that:

- the source has a stable upstream identity;
- license evidence exists and covers the intended content;
- third-party aggregation risk has been evaluated;
- attribution obligations are represented;
- exact revision/snapshot is recorded when practical;
- the source status is evidence-backed;
- prompt records validate against the canonical schema.

Do not collapse duplicate prompt text if doing so would erase independent provenance.

## Quality bar

Repository documentation should be concise, technically accurate, machine-readable where appropriate and naturally discoverable through descriptive terminology such as AI prompt dataset, prompt engineering, generative AI, image prompts, video prompts, LLM prompts, AI agents, open data, provenance and licensing. Avoid SEO keyword stuffing.
