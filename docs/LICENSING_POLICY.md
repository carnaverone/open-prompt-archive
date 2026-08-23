# Licensing and Provenance Policy

This policy governs whether third-party prompt/data content may enter the main Open Prompt Archive dataset.

## Repository scope

Open Prompt Archive is a **third-party open prompt archive**.

Carnaverone Studio first-party, private, internal or proprietary prompt collections are intentionally outside this repository's scope and must not be published here. Those materials should remain in separate first-party/private repositories or products.

## Core rule

**Publicly accessible does not mean redistributable.**

A source is accepted only when the project can identify a credible redistribution basis and preserve the obligations attached to that source.

## Evidence hierarchy

Preferred evidence, strongest first:

1. an explicit license file or license declaration from the rights holder covering the dataset/content;
2. a dataset card or official documentation that clearly states redistribution terms;
3. a repository license whose scope clearly includes original content in that repository;
4. a public-domain dedication or equivalent authoritative statement.

A repository-level license alone is not sufficient when the repository appears to aggregate third-party material from other websites, social networks, blogs or creators without evidence that those materials are covered by the same license.

## Initial main-dataset allowlist

The following licenses may be accepted after scope/provenance verification:

- `CC0-1.0`
- `CC-BY-4.0`
- `CC-BY-SA-4.0` when share-alike obligations can be preserved correctly
- `MIT`
- `Apache-2.0`
- `BSD-2-Clause`
- `BSD-3-Clause`
- clearly documented public-domain material

This is an allowlist for review, **not automatic approval**.

## Excluded from the main dataset by default

- Carnaverone Studio first-party/private/proprietary prompt collections;
- `UNKNOWN`;
- `NOASSERTION`;
- no license;
- `All Rights Reserved`;
- non-commercial-only licenses such as `CC-BY-NC-*`;
- custom terms that prohibit redistribution;
- content whose claimed license scope is unclear;
- copied/aggregated material with unresolved third-party rights;
- private, paywalled, leaked or access-controlled content.

Such third-party sources may be documented as candidates, but their prompt contents should not be redistributed by the main archive until the rights question is resolved.

## Source approval record

Each approved source should record:

- stable `source_id`;
- name and canonical URL;
- owner/maintainer;
- source type;
- SPDX license identifier where available;
- URL/path for license evidence;
- exact revision/commit/tag/snapshot where practical;
- retrieval date;
- attribution requirements;
- review status and reviewer notes;
- whether associated media may be mirrored independently of prompt text.

## Per-record obligations

Every imported prompt must remain traceable to a source registry entry. If records within one source have different authors or licenses, the record-level metadata must preserve those differences.

Never silently replace an upstream license with the repository's root software license.

## Modifications

If imported prompt text is modified:

- set `provenance.modified` to `true`;
- retain the original source reference;
- record the transformation where practical;
- satisfy any attribution/change-notice requirements of the upstream license.

Normalization that does not alter semantic prompt content should still be reproducible and documented by the importer.

## Deduplication

Prompt-text deduplication must not erase provenance.

When identical text occurs in multiple verified sources, implementations should either:

- preserve separate records; or
- maintain one content object with multiple explicit provenance/source references.

## Images, video, audio, likenesses and trademarks

Licensing of prompt text does not automatically license associated media or resolve rights of publicity, trademark, privacy or other rights.

The default archive policy is therefore:

- store prompt text and verified metadata;
- retain links to external previews when useful;
- do not automatically rehost third-party media;
- require separate verification before mirroring media assets.

## Verification states

Recommended source states:

- `candidate` — discovered but not reviewed;
- `review` — evidence is being checked;
- `approved` — redistribution basis and scope have been verified for the intended import;
- `quarantined` — unresolved conflict or rights concern;
- `rejected` — unsuitable for the main archive.

`approved` should never be inferred automatically from a filename, GitHub license badge or repository visibility.

## Takedown and correction

Credible licensing or attribution disputes should result in prompt quarantine/removal while the evidence is reviewed. Provenance metadata should be retained internally when necessary to explain the correction history, without continuing to redistribute disputed content.

---

This policy is a dataset-governance rule for the project and is not legal advice.
