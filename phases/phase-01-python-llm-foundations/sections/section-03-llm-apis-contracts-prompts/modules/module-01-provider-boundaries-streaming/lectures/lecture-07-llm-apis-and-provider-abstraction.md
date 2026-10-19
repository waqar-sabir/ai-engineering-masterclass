# Lecture 07 — LLM APIs and provider abstraction

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L07 · Duration: 75 minutes · Material status: In Review · Learner completion: Planned.

## Learning objectives

Call the Responses API; design a minimal provider-neutral interface; distinguish portable behavior from provider-specific capability.

## Prerequisites

Complete Lecture 6 and its knowledge checks.

## Detailed theory

- Model APIs commonly expose text/multimodal inputs, instructions/messages, output limits, sampling controls, tool definitions, structured formats, streaming, and usage.
- “OpenAI-compatible” usually means a similar HTTP shape, not identical semantics. Models differ in instruction hierarchy, schema subsets, tool behavior, tokenization, error codes, and streaming events.
- Keep the provider adapter thin. Your domain service should receive typed requests and return typed results; it should not depend on a provider response object everywhere.
- Preserve provider request IDs and usage metadata for debugging and cost analysis.
- Pin known-good model snapshots in production when supported, and run regressions before upgrades.

**Demonstration:** Define `GenerationRequest`, `GenerationResult`, and `LLMProvider` protocol. Implement `OpenAIProvider`; test domain services with `FakeProvider`.

## Technical explanations

Design the GenerationRequest and GenerationResult signatures. Trace a fake-provider response through the same service path as a real provider response.

## Real-world example

An application may swap providers while keeping CompanyBrief unchanged. The adapter must expose differences in refusals, usage, and schema support.

## Code walkthrough

Sketch GenerationRequest(instructions, input, output_contract) and GenerationResult(text, model, response_id, provider_request_id, usage). Follow a fake result through the domain validator. Provider-specific errors are translated once in the adapter, while source and evidence rules stay in the service. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-7-8-resources) (Lecture 7 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Define provider-neutral request/result contracts and a list of capabilities that need adapter-specific tests.

## Knowledge checks

1. What should remain outside a provider adapter?
2. Why is API-shape compatibility not behavioral compatibility?
3. Which metadata should cross the adapter boundary?

## Completion criteria

The CLI can switch between a real and fake provider without changing business logic.

## Next lecture

[Previous lecture](../../../../section-02-production-python/modules/module-02-http-async-io/lectures/lecture-06-async-python-and-bounded-concurrency.md) · [Next lecture](lecture-08-streaming-cancellation-and-user-experience.md)
