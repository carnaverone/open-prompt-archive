# Dataset Publication Checklist

Use this checklist before publishing any new Open Prompt Archive source snapshot or materially updated source snapshot.

A source being `approved` is necessary but not sufficient for publication. Publication also requires reproducible transformation, schema-valid records, verified counts/checksums, and an auditable release record.

## 1. Source authorization

- [ ] Source exists in `sources/sources.yaml`.
- [ ] Source status is `approved`.
- [ ] `license.scope_verified` is `true`.
- [ ] A human-readable source review exists.
- [ ] The intended import stays strictly within the approved source scope.
- [ ] The reviewed upstream revision/snapshot is pinned.
- [ ] Associated media is excluded unless separately approved.

## 2. Acquisition integrity

- [ ] Canonical upstream location is used rather than an unnecessary mirror.
- [ ] Acquisition source is pinned to the reviewed revision/snapshot.
- [ ] Retrieval/import date is recorded.
- [ ] Original acquisition format is identified.
- [ ] Upstream integrity/hash metadata is retained when available.
- [ ] No credentials, session tokens, or private access methods are required for the published source.

## 3. Field mapping

- [ ] Every retained upstream field has a documented destination or purpose.
- [ ] Every deliberately excluded upstream field is documented when material.
- [ ] No unsupported metadata is smuggled into semantically unrelated fields.
- [ ] Model names are not converted into unsupported compatibility claims.
- [ ] Contributor/author information is preserved when required for attribution or useful provenance.

## 4. Prompt fidelity

- [ ] Prompt text is not silently rewritten, summarized, translated, or "improved".
- [ ] Transport-only normalization is deterministic.
- [ ] Any semantic modification is explicitly marked as modified and documented.
- [ ] Duplicate handling does not erase source relationships.

## 5. Identifier stability

- [ ] Record identifier algorithm is deterministic.
- [ ] Identifier generation rules are documented.
- [ ] Re-running the import against the same pinned input produces the same IDs.
- [ ] Materially different records cannot accidentally inherit the same ID.

## 6. Licensing and attribution

- [ ] Effective license is recorded for every published record.
- [ ] SPDX identifier is used when applicable.
- [ ] Required attribution is present and complete.
- [ ] Share-alike/change-notice obligations are preserved when applicable.
- [ ] Root repository license is not substituted for upstream prompt-data licensing.

## 7. Content and privacy review

- [ ] Repository content policy has been applied.
- [ ] Obvious secrets/credentials are excluded.
- [ ] Unnecessary sensitive/private personal data is excluded.
- [ ] Source-specific filtering rules are documented.
- [ ] Exclusion counts are generated where filtering occurred.
- [ ] Problematic records are excluded rather than silently rewritten into different prompts.

## 8. Schema validation

- [ ] Every canonical JSONL record validates against `schema/prompt.schema.json`.
- [ ] Source registry still validates conceptually against `schema/source.schema.json`.
- [ ] Dataset manifest validates against `schema/manifest.schema.json`.
- [ ] No publication-state field is set to a stronger status than evidence supports.

## 9. Artifact integrity

- [ ] Final resources are generated deterministically from the pinned input.
- [ ] Exact record count is computed from final resources.
- [ ] Exact byte size is computed for every resource.
- [ ] SHA-256 checksum is generated for every resource.
- [ ] Manifest totals match the resources actually published.
- [ ] Compression format is recorded where used.
- [ ] Canonical record IDs are unique across all source shards.
- [ ] No canonical `part-*.jsonl` shard exists without a corresponding manifest resource entry.

## 10. Independent publication validation

The final candidate directory must be checked independently of the importer that generated it.

- [ ] `python scripts/validate_publication.py <source-dir>` returns `PASS` for the exact candidate directory.
- [ ] The validator confirms the source is **still** `approved` at validation time.
- [ ] The validator confirms manifest revision equals the current reviewed source revision.
- [ ] The validator recomputes bytes and SHA-256 from final resource files.
- [ ] The validator parses and schema-validates every JSONL record from final resources.
- [ ] The validator independently reconciles per-resource and total record counts.
- [ ] For a final canonical publication, `python scripts/validate_publication.py <source-dir> --require-published` returns `PASS`.

An importer validating its own in-memory output is not sufficient evidence for this section.

## 11. Distribution

- [ ] Artifact placement follows `docs/DISTRIBUTION_POLICY.md`.
- [ ] Git-tracked shards remain reasonably sized and reviewable.
- [ ] Large snapshot artifacts use a versioned release instead of bloating normal Git history.
- [ ] Quarantined/candidate/review/rejected source content is absent from Git and release assets.

## 12. Public documentation

- [ ] `DATASET_CARD.md` accurately describes the new published composition.
- [ ] `CHANGELOG.md` records source additions/removals and material curation changes.
- [ ] README source status/count claims are derived from repository data.
- [ ] Citation information remains correct.
- [ ] Known limitations are documented.
- [ ] Takedown/correction route remains available.

## 13. Release record

For a versioned dataset release:

- [ ] Dataset version is assigned.
- [ ] Release tag is immutable after publication except for a documented corrective process.
- [ ] Release notes list included source revisions.
- [ ] Release notes list record counts by source.
- [ ] Release notes identify licensing/provenance changes since the previous release.
- [ ] Release notes include or link to checksums.
- [ ] Manifest publication state is `published` only after artifacts actually exist.

## Final rule

**Do not publish because an import "looks right." Publish only when the source, transformation, records, counts, and artifacts are independently auditable from repository evidence.**
