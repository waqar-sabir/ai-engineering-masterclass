# Lecture 10 — Function/tool calling as a controlled protocol

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L10 · Duration: 75 minutes · Material status: Approved · Learner completion: Planned.

## Learning objectives

Explain tool selection and execution; validate arguments; keep authorization and side effects in application code.

## Prerequisites

Complete Lecture 9 and its knowledge checks.

## Detailed theory

- The model proposes a tool name and arguments. The application validates, authorizes, executes, and returns a result. The model never receives ambient authority merely because it named a function.
- Tool descriptions affect selection; schemas constrain arguments; neither replaces permission checks.
- Use allowlists, least privilege, timeouts, output-size limits, and audit events. Require confirmation for material side effects.
- Distinguish **structured final output** (format the answer) from **function calling** (request an external action or data operation).
- Tool results are untrusted context too. Delimit data and prevent retrieved text from redefining developer instructions.

**Demonstration:** Define a read-only `fetch_source(url)` tool. Validate its argument with Pydantic, enforce an allowlist, execute through the Lab 2 client, and return a bounded result.

## Technical explanations

Trace a proposed fetch_source argument through schema validation, explicit URL approval, the HTTP client, and bounded tool-result serialization.

## Real-world example

A model can request a fetch of an internal host. The application must reject it even if the tool arguments satisfy JSON Schema.

## Code walkthrough

Write a fetch_source call envelope with a name and url argument. Parse arguments with a strict model, compare the full URL with the caller-approved set, then dispatch a bounded HTTP fetch. Return a bounded result as untrusted context. Do not execute a function merely because the model named it. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-9-10-resources) (Lecture 10 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Design an unauthorized-host example and show where execution is denied. Distinguish a read-only tool request from final structured output.

## Knowledge checks

1. Who decides whether a proposed tool call is allowed?
2. Why can tool results contain prompt injection?
3. When should structured output be used instead of a tool?

## Completion criteria

An unauthorized domain is rejected even when the model selects the tool correctly.

## Next lecture

[Previous lecture](lecture-09-pydantic-json-schema-and-structured-model-output.md) · [Next lecture](../../module-03-prompt-engineering/lectures/lecture-11-zero-shot-few-shot-delimiters-and-prompt-contracts.md)
