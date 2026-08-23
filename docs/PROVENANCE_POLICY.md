# Provenance Policy

Open Prompt Archive treats provenance as a first-class property of every published prompt record.

## Purpose

A user should be able to answer, as far as the upstream evidence allows:

- where a prompt came from;
- who published or maintains the source;
- which source revision was reviewed;
- what license evidence supports redistribution;
- whether the archived prompt text was modified;
- which attribution obligations apply;
- whether identical content appears in more than one verified source.

## Required source provenance

An approved source should record:

- stable `source_id`;
- canonical source name;
- canonical URL/repository;
- upstream owner/maintainer;
- source type;
- exact revision, commit, tag, release, or snapshot when practical;
- retrieval/review date;
- license identifier;
- direct license-evidence location;
- review status;
- reviewer notes where necessary.

## Required record provenance

Published prompt records must reference an approved source entry and should preserve, when available:

- upstream record identifier;
- upstream author/creator;
- upstream URL or item URL;
- source revision;
- retrieval date;
- integrity hash;
- modification state;
- normalization/transformation notes;
- attribution data.

## Canonical-source preference

Prefer the original upstream source over mirrors, reposts, screenshots, scraped copies, or secondary aggregators.

A mirror may be recorded as supporting evidence, but it should not replace a resolvable canonical source without a documented reason.

## Revision pinning

When a source is versioned, reviews and imports should pin the exact revision used whenever practical. A later upstream revision is not automatically covered by an earlier approval.

Material changes to licensing, provenance, ownership, or dataset composition may require re-review.

## Transformations

If prompt text is semantically modified:

- preserve the original source reference;
- set the record's modification state accordingly;
- record the transformation when practical;
- preserve any upstream change-notice requirements.

Whitespace normalization, line-ending normalization, deterministic encoding fixes, and other non-semantic transformations should be reproducible and documented by the importer or release process.

## Deduplication

Text equality does not imply provenance equality.

When identical prompt text appears in multiple verified sources, the archive must either:

- preserve separate records; or
- maintain one canonical content object with multiple explicit provenance relationships.

Deduplication must never erase source or attribution history.

## Integrity

Where practical, the project should record cryptographic hashes for imported source artifacts or canonicalized records. Hashes demonstrate integrity of the reviewed/imported representation; they do not prove authorship or licensing by themselves.

## Broken or disappearing sources

If an upstream URL later disappears, retain the source record and the previously captured evidence references when lawful and available. Do not replace history silently.

A dead link should be marked or supplemented with archival evidence rather than rewritten to imply a different origin.

## Uncertain provenance

When provenance cannot be established confidently:

- do not guess;
- do not invent an author;
- do not infer ownership from popularity or reposting;
- move the source/record to review or quarantine as appropriate;
- stop redistribution if the uncertainty is material to rights or attribution.
