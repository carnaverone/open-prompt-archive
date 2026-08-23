# AGENTS.md

## Repository mission

Open Prompt Archive is a provenance-first, license-aware archive of third-party AI prompts that may be redistributed under verified terms.

This repository is **not** the publication location for Carnaverone Studio first-party prompts. Do not add, migrate, expose, summarize into the dataset, or otherwise publish Carnaverone Studio private/proprietary prompt collections here.

## Instruction priority

When working in this repository, use the following order of authority:

1. explicit human instructions for the current task;
2. this `AGENTS.md`;
3. `docs/LICENSING_POLICY.md`;
4. path-specific repository instructions;
5. contributor and implementation documentation.

If instructions conflict with licensing or provenance evidence, stop the import and record the uncertainty instead of guessing.

## Language and public-facing quality

- Repository-facing documentation, issue templates, code comments, schemas and metadata should be written in professional English unless a task explicitly requires another language.
- Prefer precise technical terminology over marketing language.
- Keep README and documentation useful to both humans and search/code-indexing systems without keyword stuffing.
- Do not invent project status, test results, source counts, licenses, authors, model compatibility or provenance.

## Dataset rules

Before any prompt content enters `data/`:

1. register the upstream source in `sources/sources.yaml`;
2. identify canonical source and owner/maintainer;
3. locate explicit redistribution/license evidence;
4. verify that the evidence actually covers the prompt content being imported;
5. check whether the source is itself aggregating third-party material;
6. preserve attribution and source identifiers;
7. assign an evidence-backed source status;
8. import only content from an `approved` source.

Never infer redistribution rights from public visibility, a repository badge, a filename, an AI-generated summary, or a repository-level software license whose scope over the prompt data is unclear.

## Provenance rules

- Preserve canonical source URLs.
- Record exact upstream revision, commit, tag or snapshot when practical.
- Record retrieval dates.
- Preserve record-level authorship/license differences when present.
- Do not deduplicate away independent provenance records.
- Set verification fields only after evidence has actually been checked.
- Quarantine ambiguous material instead of guessing.

## Media rules

Prompt-text licensing does not automatically license associated images, video, audio, likenesses, logos or trademarks.

Do not mirror third-party media unless redistribution rights for that media have been independently verified. External preview URLs may be retained as metadata when appropriate.

## Code and tooling rules

- Prefer deterministic import, normalization and validation behavior.
- Keep canonical data separate from generated indexes and caches.
- Derived SQLite, FTS, Parquet or RAG artifacts must be reproducible from canonical data.
- Never commit credentials, cookies, tokens, private datasets or local environment files.
- Do not add network scraping behavior that bypasses access controls, authentication, rate limits or upstream terms.
- Do not pre-approve arbitrary shell execution in agent skills.

## Schema changes

Changes to `schema/prompt.schema.json` should preserve provenance and licensing expressiveness. Avoid schema simplifications that make it impossible to represent multiple sources, attribution requirements, modification state or verification evidence.

## Source review output

A source audit should clearly distinguish:

- facts directly supported by upstream evidence;
- unresolved questions;
- inferred technical observations;
- final repository status recommendation: `candidate`, `review`, `approved`, `quarantined` or `rejected`.

Approval is a governance decision. Do not claim a source is approved unless the repository record and evidence support that state.

## Pull request expectations

For data/source changes, explain:

- what source is being added or changed;
- what license evidence was checked;
- what exact content scope is covered;
- what revision/snapshot was reviewed;
- whether media is excluded or separately licensed;
- what validation was performed.

For code changes, document deterministic validation steps and any new dependencies.
