# Lecture 05 — HTTP client engineering

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L05 · Duration: 75 minutes · Material status: Approved · Learner completion: Planned.

## Learning objectives

Build explicit request contracts; classify transport, protocol, and domain failures; choose safe retry behavior.

## Prerequisites

Complete Lecture 4 and its knowledge checks.

## Detailed theory

- Set connect/read/write/pool timeouts. A global timeout without semantics is harder to tune.
- Reuse clients to retain connection pools. Avoid constructing a client inside a hot loop.
- Classify failures:
  - **Transport:** DNS, connect failure, TLS, read timeout.
  - **Protocol:** non-2xx HTTP status, invalid content type.
  - **Provider/domain:** refusal, context limit, invalid schema, policy block.
- Retry only transient failures such as selected 429/5xx/timeouts, with exponential backoff and jitter. Honor `Retry-After` when provided.
- Retries can duplicate side effects. Require idempotency keys or explicit idempotent operations before retrying writes.
- Log attempt number, status/error class, provider request ID, and duration—but not secrets.

**Demonstration:** Wrap `httpx.Client` with timeouts and translate `HTTPStatusError`/`TimeoutException` to domain exceptions.

## Technical explanations

Trace one HTTPX request through raise_for_status and exception translation. Count attempts for 401, 429, and a read timeout.

## Real-world example

A source returns 404 permanently while a provider returns 503 transiently. The same retry policy should not be applied to both.

## Code walkthrough

Read an HTTPX request as four steps: configure timeouts, await or issue the request, check the HTTP status, and decode the expected payload. Place status and transport translation around these steps. Record attempt count separately from total deadline so nested retry layers do not multiply unnoticed. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-5-6-resources) (Lecture 5 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Build a retry decision matrix for 401, 404, 429, 503, and timeout. Explain the idempotency and deadline conditions.

## Knowledge checks

1. Why is retrying every 4xx response harmful?
2. What makes a write safe to retry?
3. Why reuse an HTTP client?

## Completion criteria

Given five failure examples, you can say whether to retry, fail fast, or ask for user action.

## Next lecture

[Previous lecture](../../module-01-types-boundaries-configuration/lectures/lecture-04-configuration-secrets-and-validation.md) · [Next lecture](lecture-06-async-python-and-bounded-concurrency.md)
