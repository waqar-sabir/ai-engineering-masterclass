# Lecture 08 — Streaming, cancellation, and user experience

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L08 · Duration: 60 minutes · Material status: In Review · Learner completion: Planned.

## Learning objectives

Understand streamed events, partial output, cancellation, and the difference between display text and validated final output.

## Prerequisites

Complete Lecture 7 and its knowledge checks.

## Detailed theory

- Streaming improves perceived latency but creates partial state. A stream can fail after showing tokens.
- Buffer structured output until the full schema validates. Do not execute actions from incomplete JSON.
- Expose cancellation and close the stream/client. Record completion status separately from displayed text.
- A CLI renderer should isolate terminal concerns from the provider adapter and business service.

**Demonstration:** Stream a plain-text answer to the terminal; then compare with non-streamed structured output that is validated before display.

## Technical explanations

Trace response.output_text.delta events, completion, and cancellation. Buffer final structured data; partial display text is not a validated result.

## Real-world example

A user cancels a streamed answer after the first sentence. Release the stream and mark it incomplete rather than recording a successful report.

## Code walkthrough

Read the streaming guide beside this lecture. Trace text-delta events to terminal display, a terminal completion event to usage recording, and cancellation to stream closure. Keep a separate completed flag so displayed partial text never becomes a successful structured artifact. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-7-8-resources) (Lecture 8 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Write the observable behavior for successful completion, Ctrl+C, and stream interruption. Compare streamed text with buffered structured output.

## Knowledge checks

1. Why should structured JSON usually be buffered?
2. What should the UI show if a stream fails halfway?
3. Which latency metric improves with streaming?

## Completion criteria

A cancelled stream leaves no “success” record and releases its network resources.

## Next lecture

[Previous lecture](lecture-07-llm-apis-and-provider-abstraction.md) · [Next lecture](../../module-02-structured-output-tool-contracts/lectures/lecture-09-pydantic-json-schema-and-structured-model-output.md)
