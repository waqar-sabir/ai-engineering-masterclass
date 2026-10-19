# Lecture 04 — Configuration, secrets, and validation

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L04 · Duration: 60 minutes · Material status: Approved · Learner completion: Planned.

## Learning objectives

Load configuration from environment variables; validate it once at startup; separate public config from secrets.

## Prerequisites

Complete Lecture 3 and its knowledge checks.

## Detailed theory

- Follow twelve-factor configuration: deploy-varying values come from the environment. `.env` is a local-development convenience, not a production secret store.
- Validate settings at the application boundary and fail fast with a useful error.
- Keep timeouts, retry limits, model IDs, base URLs, concurrency, and output budgets configurable.
- Redact API keys, authorization headers, raw private prompts, and sensitive outputs from logs.
- Provide `.env.example` with names and safe placeholders; rotate a key immediately if committed.

**Demonstration:** Extend `Settings` with `request_timeout_seconds`, `max_retries`, `max_concurrency`, and provider base URL. Add constraints such as positive values and a small retry ceiling.

## Technical explanations

Follow settings construction before client construction. Trace missing credentials and invalid timeout separately; neither should print a key.

## Real-world example

A staging service should fail at startup when its timeout is negative, rather than failing unpredictably during a customer request.

## Code walkthrough

Trace the Lab 1 Settings and first_call example. BaseSettings loads matching environment values, settings construction precedes the client, and the model field is configuration. Extend the design with positive timeout and bounded retry fields. Use a secret-aware field for the key and never dump the settings object into logs. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-3-4-resources) (Lecture 4 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Write a settings contract with timeout, retry, concurrency, and model fields. List invalid configurations and the expected startup failure.

## Knowledge checks

1. Why should settings validation occur at startup?
2. Which configuration values should be logged, and which must be redacted?
3. Why is `.env` unsuitable as a production secret manager?

## Completion criteria

An invalid timeout fails before the first network call; `.env.example` documents every required variable.

## Next lecture

[Previous lecture](lecture-03-python-project-structure-for-an-experienced-engineer.md) · [Next lecture](../../module-02-http-async-io/lectures/lecture-05-http-client-engineering.md)
