# Secure Software Development Case Study

[![Documentation checks](https://github.com/uspharaoh93/secure-development-case-study/actions/workflows/docs.yml/badge.svg)](https://github.com/uspharaoh93/secure-development-case-study/actions/workflows/docs.yml)

A public account of development methods used while working on a private web application, paired with an independent runnable security demonstration. The focus is how requirements, testing, security checks and delivery controls fit together.

This repository contains original documentation and generic examples. It does not disclose the private product's source, data model, business rules, internal architecture, infrastructure or customer information. The examples are not a blueprint of that product.

## Start here

1. [Development process](docs/development-process.md): from a user requirement to an implemented and checked change.
2. [Tools and skills](docs/tools-and-skills.md): what was inspected, what was reproduced, and what each tool contributes.
3. [CI/CD reference](docs/ci-cd.md): a generic pipeline, implemented public checks and the additional controls a production release would need.
4. [Evidence and limits](docs/evidence.md): the difference between configuration, execution evidence and recommendations.
5. [Publication boundary](docs/publication-boundary.md): what was excluded and how public material was reviewed.

For working code, open the separate [Secure Document Portal](https://github.com/uspharaoh93/secure-document-portal). It demonstrates per-document authorization, minimal audit logging, browser tests and backup verification with fictional data.

## What this work demonstrates

- Turning a broad security objective into testable access rules.
- Testing direct requests and failure paths rather than relying on visible UI controls.
- Separating confidential implementation details from reusable engineering explanations.
- Distinguishing a workflow file from a successful run, and a successful run from an enforced merge gate.
- Building a small reproducible demonstration that employers can inspect and run.

The private codebase was inspected read-only for this case study. Its application tests were not rerun for this publication, and no claim is made that its production deployment is secure or compliant. The public demonstration has its own tests and evidence.

AI-assisted planning, coding and documentation were part of this work. The repositories expose the resulting source, checks and limitations so the work can be assessed directly. This is not an independent penetration-test report or an ISO certification claim.

## Check this repository

```sh
python3 scripts/check_docs.py
python3 -m unittest discover -s tests
```

The documentation checker verifies local Markdown links and rejects forbidden local artifact types. Gitleaks scans committed history in CI. Neither check can reliably identify all proprietary ideas; manual content review remains necessary.

## License

MIT for the original material here. Third-party names identify tools, not endorsements. The license grants no rights to the private application.
