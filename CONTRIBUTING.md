# Contributing

Thank you for helping improve Open Prompt Archive.

The project accepts code, documentation, schema changes, provenance corrections and **third-party prompt datasets whose redistribution basis can be verified**.

## Scope rule

Open Prompt Archive is not the publication location for Carnaverone Studio first-party/private prompt collections.

Do **not** submit or migrate Carnaverone Studio proprietary, internal or first-party prompt libraries into this repository. Those materials belong in separate repositories/products. This archive is intended to index and redistribute eligible third-party open prompt sources with preserved provenance.

## Before contributing prompt data

Do **not** submit a prompt collection only because it is publicly visible or stored in a public GitHub repository.

A candidate source must have:

1. a stable canonical source URL;
2. a clearly identifiable upstream owner/maintainer;
3. explicit license or public-domain evidence that actually covers the submitted prompt content;
4. enough provenance to reproduce the import;
5. no unresolved conflict between the claimed license and the apparent origin of the material.

Read `AGENTS.md` and `docs/LICENSING_POLICY.md` before preparing an import.

## Required source metadata

New sources should be registered in `sources/sources.yaml` before prompt data is merged.

At minimum record:

- source identifier;
- source name;
- canonical URL/repository;
- upstream owner/maintainer;
- upstream license SPDX identifier where possible;
- URL/path to license evidence;
- revision, tag, commit or snapshot used for the import when available;
- attribution requirements;
- review status;
- notes about license scope, third-party aggregation or uncertainty;
- whether associated media may be mirrored independently of prompt text.

## Dataset rules

- Import prompt data only from sources whose intended content scope is `approved`.
- Keep original prompt text unless normalization is explicitly documented.
- Never remove required attribution.
- Never fabricate an author, model, date, license, source count or verification state.
- Do not collapse two provenance records merely because their prompt text is identical.
- Do not mirror associated images/media unless their redistribution rights are independently verified.
- Quarantine ambiguous records instead of guessing.

## Canonical format

Normalized prompt records must validate against `schema/prompt.schema.json`.

Prefer deterministic JSON/JSONL serialization and stable identifiers. Derived databases and indexes should be reproducible from canonical source data.

## Agent-assisted source review

The repository includes the project Agent Skill at:

`.github/skills/source-license-audit/SKILL.md`

Use it as a repeatable review procedure when evaluating a new repository, dataset, website or prompt collection. Agent output is evidence-gathering support; it does not override repository governance or turn an unresolved source into an approved one.

## Code contributions

Keep importers and validators deterministic where practical. Network-facing import code must respect upstream terms, access controls, rate limits and caching requirements.

Never commit credentials, API keys, access tokens, cookies, private datasets or local environment files.

## Public documentation

Repository-facing documentation should be written in professional English unless a contribution specifically requires another language. Use accurate descriptive terminology and avoid unsupported marketing claims or keyword stuffing.

## Review principle

A source may be technically accessible and still be unsuitable for redistribution. In this repository, **provenance and license confidence take priority over dataset size**.
