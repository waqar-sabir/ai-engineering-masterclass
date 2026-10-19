# Phase 1 assessment

[Phase home](../README.md)

Status: In Review (assessment material); no submission or score recorded. Try this assessment before reading the solution guide.

## Quiz — 20 points

Choose one answer unless stated otherwise. Questions 1–5 are worth 1 point each, Question 6 is worth 3 points (all correct selections required), and Questions 7–10 are worth 3 points each. Total: 20 points.

1. Which statement is correct?\
   A. Lower temperature guarantees factuality.\
   B. Pydantic proves model claims are true.\
   C. Structured decoding can enforce a supported schema, while factual checks remain separate.\
   D. Streaming makes partial JSON safe to execute.
2. A provider returns HTTP 401. Best default?\
   A. Retry five times. B. Fail fast and fix credentials. C. Switch models silently. D. Ignore it.
3. `asyncio` is most useful here for:\
   A. CPU-heavy matrix multiplication. B. Concurrent network waits. C. Runtime type validation. D. Secret storage.
4. Why reuse an HTTP client?\
   A. It makes responses deterministic. B. It preserves connection pooling. C. It removes rate limits. D. It validates facts.
5. The model requests a tool call. Who authorizes execution?\
   A. The model. B. The tool schema. C. The application. D. The user prompt alone.
6. Select two safe retry targets:\
   A. 401. B. Transient 503. C. Read timeout on an idempotent request. D. Schema validation failure repeated unchanged forever.
7. Why set `extra="forbid"` at an external boundary?
8. Name the three distinct checks for structured model output.
9. Explain why a delimiter is not a security boundary.
10. Give two pieces of metadata required to compare prompt/model versions in production.

## Practical coding assessment — 35 points

Implement `generate_validated(provider, request) -> CompanyBrief`:

- Provider dependency uses a `Protocol` (5).
- Request and result use strict Pydantic contracts (5).
- Timeout/refusal/invalid-output become distinct domain errors (7).
- Source references are limited to supplied URLs (6).
- Fake-provider tests cover success, refusal, malformed output, and fabricated URL (8).
- Code is typed, readable, and documented (4).

## Debugging scenarios — 15 points

1. Production logs reveal `Authorization: Bearer ...`. Diagnose the design failure and propose remediation/rotation.
2. `asyncio.gather` launches 5,000 requests and receives 429s/timeouts. Explain the feedback loop and fix.
3. Output is valid JSON but a total is wrong. Explain why schema validation passed and where the invariant belongs.

## System-design challenge — 20 points

Design a reliable inference gateway for the Research Assistant. Cover request contract, routing, deadlines, retries, idempotency, schema validation, redaction, rate limiting, observability, fallback, and three failure scenarios. Include one diagram and state assumptions.

## Project submission — 10 points

- Repository/readme/setup: 2
- Test evidence and evaluation fixtures: 2
- Architecture and trade-off record: 2
- Working demo and failure demo: 2
- Security/evidence limitations: 2

**Pass:** 75/100 overall, at least 20/35 on coding, and no committed secret. A committed live key is an automatic resubmission after rotation and history cleanup.

## Submission

Submit quiz responses, coding design or later implementation, failure analysis, gateway diagram, and project evidence. During the materials-only stage, coding and demo tasks are specifications for future learner work; they have not been completed here.

[Solution guide — open after attempting](solution-guide.md)
