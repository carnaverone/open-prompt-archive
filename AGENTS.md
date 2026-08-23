# AGENTS.md

## Repository mission

Open Prompt Archive is a provenance-first, license-aware archive of third-party AI prompts that may be redistributed under verified terms.

Only third-party material with evidence-backed redistribution rights belongs in this repository. First-party, private, proprietary, or otherwise out-of-scope collections must not be imported or published here.

## Instruction priority

When working in this repository, use the following order of authority:

1. explicit human instructions for the current task;
2. this `AGENTS.md`;
3. `docs/LICENSING_POLICY.md`;
4. path-specific repository instructions;
5. contributor and implementation documentation.

If instructions conflict with licensing or provenance evidence, stop the import and record the uncertainty instead of guessing.

## Public-facing quality

- Repository documentation, issue templates, code comments, schemas and metadata should use professional English unless a task explicitly requires another language.
- Prefer precise technical terminology over marketing language.
- Do not invent project status, test results, source counts, licenses, authors, compatibility or provenance.

## Dataset rules

Before prompt content enters `data/`:

1. register the upstream source in `sources/sources.yaml`;
2. identify the canonical source and owner or maintainer;
3. locate explicit redistribution or license evidence;
4. verify that the evidence covers the content being imported;
5. check whether the source aggregates third-party material;
6. preserve attribution and source identifiers;
7. assign an evidence-backed source status;
8. import only content from an `approved` source.

Never infer redistribution rights from public visibility, a badge, a filename, an AI-generated summary, or a software license whose scope over the prompt data is unclear.

## Provenance rules

- Preserve canonical source URLs.
- Record exact upstream revision, commit, tag or snapshot when practical.
- Record retrieval dates.
- Preserve record-level authorship and license differences when present.
- Do not deduplicate away independent provenance records.
- Set verification fields only after evidence has been checked.
- Quarantine ambiguous material instead of guessing.

## Media rules

Prompt-text licensing does not automatically license associated images, video, audio, likenesses, logos or trademarks. Do not mirror third-party media unless redistribution rights for that media have been independently verified.

## Code and tooling rules

- Prefer deterministic import, normalization and validation behavior.
- Keep canonical data separate from generated indexes and caches.
- Derived artifacts must be reproducible from canonical data.
- Never commit credentials, cookies, tokens, private datasets or local environment files.
- Do not add network scraping behavior that bypasses access controls, authentication, rate limits or upstream terms.
- Do not pre-approve arbitrary shell execution in agent skills.

## Source review output

A source audit should distinguish verified facts, unresolved questions, technical observations and the final repository status recommendation: `candidate`, `review`, `approved`, `quarantined` or `rejected`.

Approval is a governance decision. Do not claim a source is approved unless repository evidence supports that state.

## Pull request expectations

For data or source changes, explain what source is changing, what license evidence was checked, what content scope is covered, what revision was reviewed and what validation was performed.

For code changes, document deterministic validation steps and any new dependencies.
