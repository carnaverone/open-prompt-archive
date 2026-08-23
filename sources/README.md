# Source Registry

`sources/sources.yaml` is the canonical registry of upstream prompt sources considered by Open Prompt Archive.

The registry is validated conceptually against [`schema/source.schema.json`](../schema/source.schema.json).

## Source states

- `candidate` — discovered or proposed, not yet reviewed.
- `review` — license/provenance evidence is being evaluated.
- `approved` — redistribution basis and intended import scope are verified.
- `quarantined` — unresolved rights/provenance concern; metadata only, no prompt corpus distribution.
- `rejected` — unsuitable for the main archive.

Only `approved` sources may contribute prompt records to `data/`.

## Minimum review information

A source record should identify:

- stable `source_id`;
- canonical name and URL;
- upstream owner/maintainer;
- source type;
- review status;
- license identifier;
- direct license evidence when available;
- whether the license scope was actually verified;
- attribution requirements;
- exact review/import scope;
- pinned revision when practical;
- discovery/review dates;
- media-mirroring decision.

## Human-readable reviews

Complex reviews should be documented under [`sources/reviews/`](reviews/) using the stable source ID as the filename.

Review notes should link to primary evidence and clearly distinguish facts from unresolved questions.
