# Foundation validation

Validated locally on 2026-10-19:

- Ten phase directories, eleven project specifications, and ten design placeholders exist.
- All foundation files are nonempty; every course phase remains Planned.
- Markdown lint passes across the repository.
- Local Markdown file links and heading anchors pass.
- Ruff passes; Python test runner explicitly skips absent course tests.
- TypeScript lint/test runners explicitly skip absent packages.
- All six workflow and issue-template YAML files parse successfully.
- Common credential pattern scan found no matches; this is not an exhaustive secret audit.
- Both dependency lockfiles are included.

## Limitations and follow-up

Mermaid flowchart source was reviewed, but graphical rendering was not verified. External URL availability was not checked comprehensively; CI link checking validates repository targets and anchors only. GitHub-hosted workflow execution and branch protection require verification after publication. YAML parsing does not fully validate the GitHub Actions schema.

The current Markdown development tool dependency tree reports nine npm audit findings: five high, one moderate, and three low. Both the current release and npm's suggested downgrade were tried; the downgrade did not resolve them. These concern authoring tools, and no application is deployed. Review upstream fixes before processing untrusted contributions. Run `npm audit` for current details. No forced transitive dependency overrides were applied.

No course implementations or course tests exist yet. They must be added with the corresponding approved phase.
