# Tools, methods and evidence

“Observed” means a dependency, script or workflow was inspected in the private checkout. It does not mean a private hosted run was verified. “Demonstrated” points to executable work in the public portal.

| Tool or method | Role | Evidence boundary |
|---|---|---|
| Git and isolated checkouts | Separate changes and inspect diffs before publication | Observed locally; both portfolio repositories start with fresh histories |
| TypeScript, React and a Node.js web stack | Application implementation and build-time checks | Dependencies and scripts observed; product-specific structure withheld |
| Vitest and ESLint | Automated behavior checks and code checks | Configuration observed; no private pass rate claimed |
| Playwright | Exercise browser flows | Private configuration observed; public Chromium walkthrough reproduced separately |
| Container-based test environments | Bring up disposable service dependencies | Private workflow configuration observed; no production hosting claim |
| GitHub Actions | Run defined checks on supported events | Private configuration observed; public repository runs are separately inspectable |
| CodeQL | Static code analysis | Private workflow definition observed; results and coverage not asserted here |
| Gitleaks | Detect secret patterns in Git history | Private configuration observed; used on both new public histories |
| OpenSSF Scorecard | Review repository security indicators | Private configuration observed; no score or certification claimed |
| Python, Django and SQLite | Small standalone document portal | Implemented in the public demonstration, not a description of the private product |
| Ruff, Bandit and pip-audit | Python checks, static security rules and advisory lookup | Executed for the public portal; findings apply to scanned inputs at the time of the run |
| AI-assisted planning and coding | Help produce code, tests and documentation | Used during development; output requires verification |
| Threat modeling and negative testing | Translate misuse into requests that should fail | Demonstrated by cross-account requests, revocation and log-access tests |
| Recovery testing | Verify restored data rather than assuming a backup works | Demonstrated with separate SQLite copies; production recovery not assessed |

## Engineering skills represented

1. **Requirements analysis:** reduce an ambiguous security objective to clear allowed and denied actions.
2. **Access-control design:** separate authentication, assignment checks and audit-review permission.
3. **Test design:** use independent users and real request paths; cover direct downloads and failure conditions.
4. **Debugging:** distinguish implementation defects from test setup errors using reproduced evidence.
5. **Delivery engineering:** pin dependencies and actions, limit token permissions, gate artifacts on verification and keep runtime data out of source archives.
6. **Technical writing:** document exploitation, impact, remediation and residual risk without presenting scenarios as discoveries.
7. **Confidentiality review:** publish original examples and generalized methods rather than redacting names from copied private source.

## What scanners cannot establish

A secret scanner can miss unfamiliar secret formats. Static analysis can miss authorization mistakes. A dependency audit checks known advisories, not every defect. A browser suite covers its scripted paths. These tools complement focused review and testing; their successful execution does not certify security.
