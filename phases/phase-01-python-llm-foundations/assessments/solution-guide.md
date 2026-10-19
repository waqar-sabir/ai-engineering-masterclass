# Phase 1 solution guide

[Assessment](phase-01-assessment.md) · [Phase home](../README.md)

Use after attempting the questions. No learner score has been assigned.

## Quiz

1. C.
2. B.
3. B.
4. B.
5. C.
6. B and C, with bounded retries, backoff/jitter, and an overall deadline.
7. It rejects undeclared fields rather than silently accepting/ignoring contract drift or unwanted data.
8. JSON syntax/decoding, schema/type validation, and semantic/factual/domain validation.
9. Delimiters help the model parse sections but do not remove malicious instructions or change application authorization; untrusted data remains untrusted.
10. Any two of prompt version, model/snapshot, schema version, provider, request ID, evaluation-set version, and relevant inference parameters.

## Coding solution characteristics

- Domain service accepts `LLMProvider`, never constructs the real SDK client internally.
- Provider adapter maps provider-specific refusal/incomplete/timeout data into domain errors.
- Pydantic validates the result; a second validator checks that `source.url` is in `request.source_urls` and supported sections exist.
- Tests inject a fake provider and do not require network or an API key.

## Debugging solutions

1. Logging middleware captured headers without redaction. Stop logging secrets, revoke/rotate the key, scrub accessible logs according to policy, audit access, and add a regression test.
2. Unbounded concurrency overwhelms quotas and connections; retries amplify load. Add a semaphore/queue, rate-aware admission control, bounded exponential backoff with jitter, and a global deadline.
3. JSON Schema validates shape/types, not arithmetic truth. Recompute with `Decimal` in deterministic application code and surface a mismatch.

## System-design scoring anchors

- 0–5: vague diagram or direct provider call only.
- 6–10: contracts, timeout, basic validation, and logs.
- 11–15: bounded retries/concurrency, redaction, idempotency, typed failures, useful telemetry.
- 16–20: explicit SLO/capacity assumptions, safe fallback policy, retry-storm prevention, evidence/security boundaries, and trade-offs.
