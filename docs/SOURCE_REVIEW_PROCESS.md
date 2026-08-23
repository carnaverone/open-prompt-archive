# Source Review Process

This document defines the operational review process for adding a third-party prompt source to Open Prompt Archive.

## Review states

- `candidate` — discovered or proposed, not yet reviewed.
- `review` — evidence is actively being evaluated.
- `approved` — redistribution basis and intended import scope have been verified.
- `quarantined` — unresolved licensing, provenance, attribution, or rights concern.
- `rejected` — unsuitable for the main archive.

Only `approved` sources may contribute prompt content to the published dataset.

## Step 1 — Identify the canonical source

Record:

- source name;
- canonical URL/repository;
- upstream owner/maintainer;
- source type;
- exact revision/tag/commit/snapshot when practical;
- discovery date.

Do not begin with a mirror when the canonical source is available.

## Step 2 — Locate license evidence

Prefer primary evidence in this order:

1. explicit license file/declaration from the rights holder covering the dataset/content;
2. official dataset card or documentation with redistribution terms;
3. repository license whose scope clearly includes the prompt content;
4. authoritative public-domain dedication.

Record a direct evidence URL/path rather than only a license name.

## Step 3 — Verify license scope

Ask:

- Does the license actually cover the prompts?
- Is it limited to code, documentation, or another asset class?
- Does the source aggregate prompts from third parties?
- Are individual records governed by different licenses?
- Are attribution/share-alike requirements preserved?
- Are associated media governed separately?

A top-level GitHub license badge is not sufficient evidence by itself when the repository contains aggregated third-party material.

## Step 4 — Review provenance

Check whether the source identifies:

- creators/authors where required;
- original publication locations;
- revisions/releases;
- collection method;
- third-party upstream sources;
- transformations performed by the aggregator.

Unresolved provenance can be grounds for quarantine even when a license file exists.

## Step 5 — Define import scope

Approval must define what is being approved.

Examples:

- all prompt text authored by the upstream project at revision X;
- only records explicitly marked CC0;
- metadata only, excluding images;
- one specific dataset release rather than the entire repository history.

Avoid vague approvals such as “the whole website is open.”

## Step 6 — Decide status

### Approved

Use only when the intended prompt import has a sufficiently clear redistribution basis and provenance chain.

### Quarantined

Use when evidence conflicts, ownership is unclear, the license scope is ambiguous, or important provenance is unresolved.

Quarantine means **metadata/review record only**. Do not publish the disputed prompt corpus in `data/`.

### Rejected

Use when redistribution is clearly not permitted, the source is unsuitable, or the project cannot obtain a credible rights basis.

## Step 7 — Register evidence

Update `sources/sources.yaml` with:

- stable source ID;
- canonical URL;
- owner/maintainer;
- review status;
- license identifier;
- license-evidence URL/path;
- pinned revision if available;
- review date;
- attribution requirements;
- scope notes;
- media policy;
- uncertainty/reviewer notes when relevant.

A human-readable review may also be created under `sources/reviews/` for complex sources.

## Step 8 — Import only after approval

After approval:

- preserve original prompt text unless transformation is documented;
- map source identifiers into the canonical schema;
- preserve attribution;
- validate records;
- compute integrity hashes when practical;
- deduplicate without erasing provenance;
- keep imported media separate unless independently approved.

## Re-review triggers

Re-review a source when:

- its license changes;
- ownership/maintainer changes materially;
- the source begins aggregating third-party content;
- upstream removes or disputes licensing evidence;
- a credible takedown or attribution dispute is received;
- a new source version materially changes collection scope;
- new evidence contradicts the original approval.

## Review principle

When the evidence is incomplete, record the uncertainty and stop. The archive prefers a smaller defensible dataset over a larger corpus with unclear rights.
