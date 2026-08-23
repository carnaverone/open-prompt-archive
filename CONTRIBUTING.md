# Contributing to Open Prompt Archive

Thank you for helping improve Open Prompt Archive.

This project welcomes contributions, but prompt data is handled differently from ordinary source-code contributions. The archive is **source-first and license-aware**: public availability alone is not sufficient evidence that prompt content may be redistributed.

## Contribution paths

### 1. Propose an open prompt source

This is the preferred way to expand the archive.

Use the **Source proposal** issue form and provide as much of the following as possible:

- canonical source URL or repository;
- upstream owner/maintainer;
- source type;
- explicit license identifier;
- direct license-evidence URL or file path;
- whether the source appears to contain original or aggregated material;
- approximate scope of the prompt collection;
- relevant revision, release, tag, commit, or snapshot;
- attribution requirements;
- any uncertainty that should be reviewed.

Do not attach or paste a large prompt corpus while the source is still unreviewed.

### 2. Correct licensing or provenance

Use the **License / provenance correction** issue form when:

- a license changed;
- the recorded license scope is wrong;
- a source has a stronger canonical URL;
- attribution is incomplete;
- a revision or source identifier is incorrect;
- a source appears to aggregate third-party material that was not previously disclosed.

### 3. Report data-quality problems

Use the **Data-quality report** form for:

- malformed records;
- duplicate handling problems;
- broken source links;
- incorrect model/category metadata;
- schema violations;
- integrity or normalization errors.

### 4. Request review or removal

Use the **Removal / rights review** form for credible concerns involving:

- licensing;
- attribution;
- ownership;
- privacy or personal data;
- rights of publicity;
- content that should not be redistributed by the archive.

Do not publish sensitive personal information in the issue. Provide only the minimum evidence needed to identify the affected record/source.

## Prompt-data contribution rule

**Do not submit a prompt dump simply because it was found on a public website, social network, blog, Discord, forum, or GitHub repository.**

Before prompt content can enter `data/`:

1. the source must be registered in `sources/sources.yaml`;
2. the canonical source and owner must be identified;
3. redistribution/license evidence must be located;
4. the evidence must be checked for scope;
5. third-party aggregation risk must be reviewed;
6. attribution requirements must be recorded;
7. the source must be marked `approved`;
8. imported records must validate against `schema/prompt.schema.json`.

A candidate, quarantined, or rejected source may be documented at the metadata/review level, but its prompt corpus must not be redistributed by this repository.

## What we accept

Examples of welcome contributions:

- clearly licensed dataset proposals;
- public-domain source proposals with credible evidence;
- license-evidence improvements;
- provenance corrections;
- attribution corrections;
- schema improvements;
- dataset-card and policy improvements;
- data-quality fixes;
- reproducible normalization corrections;
- documentation improvements.

## What we do not accept

- copied prompt dumps with unknown rights;
- paywalled/private/leaked/access-controlled material;
- attempts to remove required attribution;
- knowingly false authorship, provenance, model, or license metadata;
- third-party media without independently verified redistribution rights;
- Carnaverone Studio first-party/proprietary prompts;
- secrets, credentials, API keys, session cookies, or private datasets.

## Pull requests

Pull requests should be narrow, reviewable, and evidence-based.

For data-related changes, include:

- affected source IDs;
- reason for the change;
- license/provenance evidence when relevant;
- whether prompt text itself changed;
- whether attribution changed;
- validation performed;
- known uncertainties.

Do not combine unrelated source imports or policy changes in one pull request unless there is a strong reason.

## Source review states

The registry uses these states:

- `candidate` — discovered but not reviewed;
- `review` — evidence is actively being evaluated;
- `approved` — redistribution basis and intended import scope are verified;
- `quarantined` — unresolved rights/provenance concern;
- `rejected` — not suitable for the main archive.

Only `approved` sources may contribute prompt content to the published dataset.

## Licensing of contributions

Repository-authored code/documentation contributions are accepted under the repository's applicable project license unless explicitly stated otherwise.

Third-party prompt content is **not relicensed by contribution**. It must retain its verified upstream license and attribution requirements.

If you are proposing material you personally created, do not assume that this repository automatically publishes it under a particular data license. Open Prompt Archive is currently optimized for reviewed third-party sources rather than direct first-party prompt submissions.

## Conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Before opening a contribution

Please read:

- [`DATASET_CARD.md`](DATASET_CARD.md)
- [`docs/LICENSING_POLICY.md`](docs/LICENSING_POLICY.md)
- [`docs/PROVENANCE_POLICY.md`](docs/PROVENANCE_POLICY.md)
- [`docs/SOURCE_REVIEW_PROCESS.md`](docs/SOURCE_REVIEW_PROCESS.md)
- [`docs/CONTENT_POLICY.md`](docs/CONTENT_POLICY.md)

When evidence is incomplete, **state the uncertainty instead of guessing**.
