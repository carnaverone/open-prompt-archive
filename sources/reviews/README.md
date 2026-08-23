# Source Review Records

This directory contains human-readable review notes for prompt sources that require more context than fits cleanly in `sources/sources.yaml`.

A review record may document:

- canonical source and owner;
- exact revision reviewed;
- license evidence;
- license-scope analysis;
- third-party aggregation concerns;
- attribution requirements;
- approved import scope;
- media-handling decision;
- unresolved questions;
- status changes and re-review history.

## Naming

Use stable source identifiers, for example:

```text
sources/reviews/<source_id>.md
```

## Important

A review file is **not** an approval by itself. The canonical status is the evidence-backed status recorded in `sources/sources.yaml`.

For `candidate`, `quarantined`, or `rejected` sources, review files must not contain a copied prompt corpus. Keep only the metadata and limited evidence necessary to document the decision.
