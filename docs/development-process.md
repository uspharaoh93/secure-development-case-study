# Development process

## Begin with an observable user outcome

A useful requirement describes what a person can do and what must be prevented. For the public portal: an employee can read assigned records, and changing a URL must not reveal another employee's records. That statement gives development and testing a shared target.

The private application has a larger scope. This case study deliberately omits its workflows and structure. The process below is reusable; the portal is the inspectable example.

## Work in small, reviewable changes

1. Define the intended behavior, inputs, failure cases and confidentiality boundary.
2. Inspect existing code and configuration before claiming that a feature already exists. Separate working code from fixtures, placeholders and external integrations that have not been exercised.
3. Keep a focused branch or isolated checkout. A passing check on one branch is not evidence for another branch.
4. Write a test that exposes the missing behavior. For authorization, use separate identities and real request handlers. A test of a mocked permission function would not prove the route enforces that permission.
5. Implement the smallest change that satisfies the requirement. Use established framework authentication and CSRF features instead of inventing replacements.
6. Run the relevant checks and the full application suite. Investigate failed checks before editing assertions. Sometimes a test is wrong: in this build, one accidentally replaced its own session cookie, while another compared randomized CSRF tokens byte for byte. Both were corrected without weakening the access requirement.
7. Exercise the user flow in a real browser. Check successful use, denied access and the return path after an error.
8. Record what ran, what passed and what remains untested. Review the staged files before publishing.

## Treat security as behavior

The public portal demonstrates an access decision at every document view and download. Audit events record the decision without copying the request payload. Tests cover revoked access, reviewer isolation, CSRF protection and unavailable audit storage. The purpose is to make the rule observable, not merely to add a scanner badge.

The private repository contains testing and security-scanning configuration. Those files show which checks are defined; they do not prove the checks are active on every development branch. The case study does not publish private test names, failure details or environment settings.

## Use coding assistance with verification

AI tools can help draft plans, code, tests and explanations. Generated output can also introduce incorrect assumptions, overbroad permissions or unsupported claims. The workflow therefore checks behavior using the same application paths a user exercises and inspects the final public file set. AI review is not an independent audit, and passing tests do not replace owner review of confidentiality or licensing.

## Keep a recovery path

The portal's backup tool creates a new SQLite file and refuses to overwrite an existing destination. The recovery check compares a backup with a separately restored copy. This is a reproducible exercise, not a claim that a production disaster-recovery program exists.

[NIST's SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) provides a public framework for integrating security practices into software development. This case study uses it as a reference, not as a certification or statement that every practice has been implemented.
