# Governance

Open Prompt Archive uses a **maintainer-led governance model** appropriate for an early-stage public dataset.

## Maintainer responsibilities

Maintainers are responsible for:

- approving, quarantining, or rejecting sources;
- interpreting repository licensing and provenance policies;
- reviewing corrections and takedown requests;
- deciding dataset schema and metadata conventions;
- protecting attribution and provenance integrity;
- preparing dataset releases;
- enforcing the Code of Conduct;
- documenting material policy changes.

## Decision principles

Repository decisions should prioritize, in order:

1. legal and provenance clarity;
2. integrity of attribution and source history;
3. data quality and reproducibility;
4. usefulness to downstream users;
5. corpus growth.

Dataset size is never a reason to weaken source verification.

## Source approval

A source may be approved only after the intended import scope and redistribution basis have been reviewed. Approval applies to the reviewed scope/revision, not automatically to every future version of the upstream source.

Maintainers may move a previously approved source to `review` or `quarantined` if new evidence creates uncertainty.

## Policy changes

Material changes to licensing, provenance, contribution, content, or takedown policy should be:

- documented in the relevant policy file;
- reflected in `CHANGELOG.md` when they affect users or contributors;
- applied prospectively and, when necessary, used to re-review existing data.

## Contributions and review

External contributions are welcome. Merge authority remains with maintainers.

A contributor's reputation, popularity, or relationship with the project does not replace evidence requirements. The same source-review rules apply to maintainer-discovered and community-proposed sources.

## Conflicts of interest

A maintainer who has a material conflict regarding a source should disclose it in the review record when practical and rely on verifiable public evidence rather than unsupported assertions.

## Future governance

If the project develops a substantial maintainer or contributor community, this governance model may be expanded to define additional reviewer roles, voting rules, release stewardship, or specialist license/data-quality review.

Until then, Open Prompt Archive remains a maintainer-led project operated by **Carnaverone Studio**.
