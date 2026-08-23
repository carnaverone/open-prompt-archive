---
applyTo: "data/**/*,sources/**/*,schema/**/*"
---

# Dataset and source-registry instructions

These paths contain licensing-sensitive canonical data, source evidence and schema definitions.

Before editing them:

1. Read `AGENTS.md` and `docs/LICENSING_POLICY.md`.
2. Confirm whether the change affects source approval, redistribution scope, attribution or provenance.
3. Do not add Carnaverone Studio first-party/private prompts.
4. Do not infer a prompt-content license from repository visibility or a software license without checking scope.
5. Do not mark a source `approved` or a record `verified: true` without evidence.
6. Preserve source URL, author/owner, license identifier/evidence, revision and retrieval metadata when available.
7. Keep ambiguous content out of the canonical dataset; use `review` or `quarantined` instead of guessing.
8. Do not mirror third-party media unless its own redistribution rights are independently verified.
9. Schema changes must not remove the ability to represent provenance, attribution, modifications or verification status.
10. Deduplication must preserve independent provenance records.

When proposing a data change, summarize the exact source, evidence reviewed, content scope, status decision and validation performed.
