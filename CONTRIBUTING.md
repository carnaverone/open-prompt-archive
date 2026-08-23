# Contributing

Thank you for helping improve Open Prompt Archive.

The project accepts code, documentation, schema changes, provenance corrections, and prompt datasets whose redistribution basis can be verified.

## Before contributing prompt data

Do **not** submit a prompt collection only because it is publicly visible or stored in a public GitHub repository.

A candidate source must have:

1. a stable source URL;
2. a clearly identifiable upstream owner/maintainer;
3. explicit license or public-domain evidence that actually covers the submitted content;
4. enough provenance to reproduce the import;
5. no known conflict between the claimed license and the apparent origin of the material.

Read `docs/LICENSING_POLICY.md` before preparing an import.

## Required source metadata

New sources should be registered in `sources/sources.yaml` before data is merged.

At minimum record:

- source identifier;
- source name;
- canonical URL/repository;
- upstream license SPDX identifier where possible;
- URL/path to license evidence;
- revision, tag, or commit used for the import when available;
- attribution requirements;
- review status;
- notes about scope or uncertainty.

## Dataset rules

- Keep original prompt text unless normalization is explicitly documented.
- Never remove required attribution.
- Never fabricate an author, model, date, license, or verification state.
- Do not collapse two provenance records merely because their prompt text is identical.
- Do not mirror associated images/media unless their redistribution rights are independently verified.
- Quarantine ambiguous records instead of guessing.

## Canonical format

Normalized prompt records must validate against `schema/prompt.schema.json`.

Prefer deterministic JSON/JSONL serialization and stable identifiers. Derived databases and indexes should be reproducible from canonical source data.

## Code contributions

Keep importers and validators deterministic where practical. Network-facing import code should respect upstream terms, rate limits, and caching requirements.

Never commit credentials, API keys, access tokens, cookies, private datasets, or local environment files.

## Review principle

A source may be technically accessible and still be unsuitable for redistribution. In this repository, **provenance and license confidence take priority over dataset size**.