# Architecture principles

- Separate ingestion, retrieval, orchestration, and API boundaries.
- Validate structured outputs and tool arguments at trust boundaries.
- Enforce authorization and tenant isolation in data access.
- Use bounded retries, timeouts, idempotency, and explicit human approvals.
- Measure quality alongside latency, cost, and operational failures.
- Keep deterministic tests separate from opt-in paid provider evaluations.
- Document decisions, alternatives, and rollback paths before deployment.
