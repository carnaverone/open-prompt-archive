# Security Policy

Open Prompt Archive is primarily a public dataset and curation repository, but security issues can still affect import tooling, automation, generated artifacts, links, and contribution workflows.

## Report privately when appropriate

Do not open a public issue containing:

- credentials, API keys, tokens, cookies, or secrets;
- exploitable vulnerability details that could affect contributors or downstream users;
- private personal information;
- malicious payloads that do not need to be published to reproduce the issue.

If GitHub private vulnerability reporting is enabled for this repository, use **Report a vulnerability**. Otherwise, contact the maintainer through a private method exposed on the maintainer's GitHub profile.

## In scope

Examples include:

- command or code execution through repository tooling;
- unsafe parsing of untrusted dataset files;
- path traversal or unsafe archive extraction;
- malicious source metadata causing unsafe downstream behavior;
- accidental inclusion of secrets or private data;
- dependency vulnerabilities in tooling maintained by this repository.

## Data and rights issues are not security vulnerabilities

Licensing, attribution, provenance, privacy, and removal concerns should normally use the repository's dedicated issue forms and [`docs/TAKEDOWN_POLICY.md`](docs/TAKEDOWN_POLICY.md).

If a privacy issue would expose sensitive personal information, report it privately instead of opening a public issue.

## Response

Maintainers will triage reports based on severity and reproducibility. Security-sensitive details may be withheld from public discussion until a reasonable mitigation is available.

No bounty program is currently offered.
