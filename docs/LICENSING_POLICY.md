# Licensing Policy

This policy governs whether third-party prompt/data content may enter the main Open Prompt Archive dataset and how licensing information must be preserved after publication.

## Repository scope

Open Prompt Archive is a **third-party open prompt archive**.

Carnaverone Studio first-party, private, internal, or proprietary prompt collections are intentionally outside this repository's scope and must not be published here.

## Core rule

**Publicly accessible does not mean redistributable.**

A source is accepted only when the project can identify a credible redistribution basis and preserve the obligations attached to the exact content being imported.

## Evidence hierarchy

Preferred evidence, strongest first:

1. an explicit license file or license declaration from the rights holder covering the dataset/content;
2. an official dataset card or documentation that clearly states redistribution terms;
3. a repository license whose scope clearly includes the prompt content being imported;
4. a public-domain dedication or equivalent authoritative statement.

A repository-level license alone is not sufficient when the repository appears to aggregate third-party material from websites, social networks, blogs, forums, or other creators without evidence that those materials are covered by the same license.

## Licenses eligible for review

The main archive may accept content under licenses such as:

- `CC0-1.0`;
- `CC-BY-4.0`;
- `CC-BY-SA-4.0` when share-alike obligations can be preserved correctly;
- `MIT`;
- `Apache-2.0`;
- `BSD-2-Clause`;
- `BSD-3-Clause`;
- clearly documented public-domain material.

This is an **allowlist for review, not automatic approval**. A valid license identifier does not prove that the source had authority to apply that license to every prompt it contains.

## Excluded from the main dataset by default

- Carnaverone Studio first-party/private/proprietary prompts;
- `UNKNOWN` or `NOASSERTION` licensing status;
- no license;
- `All Rights Reserved`;
- non-commercial-only licenses such as `CC-BY-NC-*`;
- custom terms that prohibit redistribution;
- content whose claimed license scope is unclear;
- copied/aggregated material with unresolved third-party rights;
- private, paywalled, leaked, stolen, or access-controlled content.

These sources may be documented for review at the metadata level, but their prompt corpus must not be redistributed by the main archive while rights remain unresolved.

## Source approval

Each reviewed source should record:

- stable `source_id`;
- canonical source name and URL;
- upstream owner/maintainer;
- source type;
- SPDX license identifier where available;
- direct URL/path for license evidence;
- whether license scope was actually verified;
- exact reviewed revision/commit/tag/snapshot where practical;
- discovery/review date;
- attribution requirements;
- explicit import scope;
- review status;
- media-mirroring decision;
- notes for material uncertainty.

See [`schema/source.schema.json`](../schema/source.schema.json) and [`docs/SOURCE_REVIEW_PROCESS.md`](SOURCE_REVIEW_PROCESS.md).

## Multi-license data model

Open Prompt Archive is intentionally **multi-license at the data layer**.

The repository's root `LICENSE` applies only to repository-authored material within its stated scope. It does **not** relicense imported third-party prompt data.

Every published prompt record must retain the effective upstream license and attribution metadata that apply to that record. If a source contains multiple licenses or creators, those differences must remain expressible at record level.

## SPDX identifiers

Use SPDX license identifiers whenever the applicable license exists in the SPDX License List.

Examples:

```text
CC0-1.0
CC-BY-4.0
CC-BY-SA-4.0
MIT
Apache-2.0
BSD-3-Clause
```

For public-domain or custom licensing situations that cannot be represented cleanly by a standard SPDX identifier, the review record must contain direct authoritative evidence and enough notes to explain the redistribution basis.

Do not convert an unknown license into a familiar SPDX identifier merely for normalization convenience.

## Repository-authored files

Repository-authored documentation, schemas, templates, and tooling are licensed separately from imported data. The project may use SPDX/REUSE-compatible metadata for those files.

Where REUSE metadata is used, it must not be allowed to override or misrepresent the distinct licenses attached to imported prompt data.

## Per-record obligations

Every imported prompt must remain traceable to an approved source registry entry.

A record must preserve, as applicable:

- effective license;
- attribution requirement;
- attribution text/author;
- canonical source reference;
- upstream record identifier;
- reviewed source revision;
- modification/change notice.

Never silently replace an upstream license with the repository's root software/documentation license.

## Attribution

When attribution is required, preserve enough information for downstream users to comply without having to reconstruct the source history manually.

Attribution should remain linked to the relevant source or record. Do not collapse multiple creators into a misleading single attribution when upstream requirements distinguish them.

## Modifications

If imported prompt text is semantically modified:

- set the record's modification state to true;
- retain the original source reference;
- record the transformation when practical;
- satisfy any attribution/change-notice requirements of the upstream license.

Deterministic normalization that does not alter semantic prompt content should still be reproducible and documented.

## Deduplication

Prompt-text deduplication must not erase licensing or provenance.

When identical text occurs in multiple verified sources, the archive must either:

- preserve separate records; or
- maintain one content object with multiple explicit provenance/source relationships.

A deduplicated index must not imply that every occurrence shares one author or license unless the evidence supports that conclusion.

## Associated media

Licensing of prompt text does not automatically license associated images, video, audio, likenesses, trademarks, or other media.

Default policy:

- archive approved prompt text and metadata;
- retain external preview links when useful and lawful;
- do not automatically rehost third-party media;
- require independent rights verification before mirroring media assets.

## Quarantine

`quarantined` means the archive has a material unresolved rights/provenance concern.

A quarantined source may retain:

- source identifier;
- canonical URL;
- license/provenance evidence references;
- review notes;
- decision history.

It must **not** retain or redistribute the disputed prompt corpus in a public quarantine directory merely for convenience.

## Re-review

Approval is scoped to the evidence and source revision reviewed. Re-review is required when material facts change, including:

- license changes;
- ownership changes;
- substantial source restructuring;
- newly discovered third-party aggregation;
- credible rights disputes;
- upstream withdrawal or correction of licensing evidence.

## Takedown and correction

Credible licensing or attribution disputes may result in prompt quarantine/removal while evidence is reviewed. Metadata necessary to document the correction history may be retained without continuing to redistribute disputed prompt text.

See [`docs/TAKEDOWN_POLICY.md`](TAKEDOWN_POLICY.md).

---

This policy is a dataset-governance rule for the project and is not legal advice.
