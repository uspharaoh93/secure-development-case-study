# Publication boundary

## Material included

- Original explanations of development methods and their trade-offs.
- Public tool names and links to official guidance.
- Generic process diagrams that do not depict the private application's design.
- Links to separately written demonstration code with fictional data.
- Evidence labels that distinguish inspected files from executed checks and recommendations.

## Material excluded

- Private source code, repository history and internal commit identifiers.
- Product names, customer identities, real documents and business-specific rules.
- Internal data models, endpoints, network diagrams, integration settings and infrastructure addresses.
- Credentials, tokens, environment files, application databases and local paths.
- Private screenshots, incident details, scan reports and contracts.

## Review procedure

1. Write the public material from a blank repository. Do not copy a private repository and attempt to clean its history afterward.
2. Inspect every tracked file and image, including titles, comments, metadata and links.
3. Look for confidential meaning as well as recognizable names. Renaming a product does not make copied architecture public.
4. Run the documentation checker and full-history secret scan. Review findings; do not add broad scanner exemptions to make checks pass.
5. Publish only the reviewed file set, then verify the public repository and hosted checks.
6. Reapply this process to every later update. Avoid uploading internal evidence to answer public issues.

Automated scans do not establish confidentiality or permission to publish third-party material. This repository minimizes that risk by using new prose and generic examples, but contractual obligations still depend on the owner's actual agreements.
