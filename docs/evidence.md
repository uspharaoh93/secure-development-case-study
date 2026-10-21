# Evidence and limitations

## Three evidence levels

| Level | Meaning | Example |
|---|---|---|
| Inspected configuration | A file or dependency exists in the reviewed checkout | Private test/build/scanner workflows |
| Reproduced demonstration | A command or user flow executed against the separate public application | Authorization tests and Chromium access checks |
| Recommendation | A practice described for future adoption | Approved production deployment with rollback and health checks |

The private checkout was inspected read-only for workflow categories and tool choices. No private source, configuration excerpts, commit references, URLs, paths, reports or runtime records are published. Its tests and hosted pipelines were not rerun for this case study.

The public portal's [verification record](https://github.com/uspharaoh93/secure-document-portal/blob/main/docs/verification.md) describes its actual checks. Its [Actions page](https://github.com/uspharaoh93/secure-document-portal/actions) supplies hosted run evidence. This repository's [Actions page](https://github.com/uspharaoh93/secure-development-case-study/actions) supplies documentation-check evidence.

There is no independent penetration test, ISO 27001 certification, production uptime assessment or compliance conclusion in either repository. No vulnerability is alleged in the private product. The two security scenarios belong to the public educational build.

Publication was prepared on October 21, 2026. Future changes and dependency updates require fresh checks; old successful runs apply only to the revision they tested.

## Public repository verification

The [initial published revision passed documentation and secret-scan jobs](https://github.com/uspharaoh93/secure-development-case-study/actions/runs/39678753586). The local checker and all six checker tests also passed. The scan covered the new repository's complete committed history; no private history was imported.

The `main` branch requires the **Verify documentation** and **Secret scan** checks, an up-to-date branch, a pull request and resolved review conversations. These rules apply to administrators, and force pushes and branch deletion are disabled. The required approving-review count is zero for this solo portfolio; a pull request is not evidence of independent human approval. The default workflow token is read-only, and private vulnerability reporting is enabled.

The linked run applies to its own commit. Use the status badge or Actions page to inspect later revisions.
