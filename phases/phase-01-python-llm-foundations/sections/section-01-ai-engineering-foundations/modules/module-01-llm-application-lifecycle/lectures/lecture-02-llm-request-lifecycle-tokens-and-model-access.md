# Lecture 02 — LLM request lifecycle, tokens, and model access

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L02 · Duration: 75 minutes · Material status: Approved · Learner completion: Planned.

## Learning objectives

Explain tokenization and context budgets; compare API-hosted and self-hosted inference; understand sampling controls without treating them as guarantees.

## Prerequisites

Complete Lecture 1 and its knowledge checks.

## Detailed theory

- A request typically becomes: authenticated API call → input normalization/tokenization → scheduling/batching → model inference → decoding → streamed or buffered output → usage metadata.
- A **token** is a model vocabulary unit, not reliably a word or character. Both instructions and user/context data consume input tokens; output consumes a separate budget. Context limits constrain the total model-visible sequence.
- Latency can be decomposed into queue time, time-to-first-token, and generation time. Cost commonly scales with input/output tokens and provider pricing.
- **Temperature** reshapes the probability distribution. Lower values generally reduce variation; they do not make answers true. Output-token limits cap generation; they do not guarantee a complete answer.
- Hosted APIs reduce infrastructure work and provide managed scaling. Self-hosting increases control and may improve unit economics at sustained scale, but introduces GPU scheduling, serving, quantization, upgrades, security, and capacity planning.
- Prefer a capability-and-SLO decision: quality, structured-output support, latency, cost, privacy, region, rate limits, and operational burden.

**Practical demonstration:** Estimate worst-case request cost from an assumed input/output token budget, then identify which prompt sections are stable, variable, or unnecessary. Use the provider’s tokenizer/cost calculator when available; do not hard-code pricing into the course.

## Technical explanations

Annotate a provider request with model, instructions, input, and output budget. Calculate input_tokens × input_rate + output_tokens × output_rate using assumed rates, and label the assumption.

## Real-world example

A short interactive response needs low time-to-first-token; a batch report can favor cost. Compare them using explicit input/output budgets rather than character counts.

## Code walkthrough

Inspect a request dictionary without executing it. Identify the configured model, instruction text, user input, and output limit. Add input/output usage fields to a sample response, then compute an assumed bill using clearly labeled rates. Compare buffered latency with time-to-first-token; do not confuse response.id with an HTTP request ID. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lecture-2-resources) (Lecture 2 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Design two request budgets for interactive and batch use. Explain the assumptions and which measurements would invalidate your model choice.

## Knowledge checks

1. Why can two strings of equal character length use different token counts?
2. Which latency measure matters most for a streaming UI?
3. When might self-hosting be justified?
4. Why should model names and limits be configuration, not scattered constants?

## Completion criteria

You can draw the request lifecycle and defend a hosted-vs-self-hosted choice using explicit requirements.

## Next lecture

[Previous lecture](lecture-01-what-an-ai-engineer-builds.md) · [Next lecture](../../../../section-02-production-python/modules/module-01-types-boundaries-configuration/lectures/lecture-03-python-project-structure-for-an-experienced-engineer.md)
