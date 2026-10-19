# Contributing

The repository foundation belongs on `main`. Phase 1 resources and teaching materials have been requested on `course/phase-01-foundations`. Application implementation is deferred by the owner. Create phase branches only when work begins:

- `course/phase-01-foundations`
- `course/phase-02-embeddings`
- `course/phase-03-rag`
- `course/phase-04-advanced-rag`
- `course/phase-05-agents`
- `course/phase-06-multi-agent`
- `course/phase-07-mcp-context`
- `course/phase-08-model-optimization`
- `course/phase-09-llmops`
- `course/phase-10-capstone`

For each phase: generate curriculum, lectures and resources; add labs and assessments; implement the agreed projects; validate Markdown links; run applicable tests; review the phase; wait for explicit owner approval; merge only after approval. Record the approval in the PR. Do not create all branches in advance.

Use the [templates](templates/README.md), relative links, and factual status labels. Keep API keys, private data, model weights, and local environments out of Git. Use `.env.example` with empty values and document every variable. Add deterministic tests with code; paid integrations must be opt-in. Run the checks in [environment setup](docs/environment-setup.md).

Configure GitHub branch protection manually after publication: require PRs, an owner review, and the four foundation checks. CI cannot substitute for course-owner approval. The initial workflow does not deploy services.
