# Lecture 12 — Prompt versioning and regression testing

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L12 · Duration: 75 minutes · Material status: Approved · Learner completion: Planned.

## Learning objectives

Treat prompts as code; build a small evaluation set; compare versions without relying on anecdotes.

## Prerequisites

Complete Lecture 11 and its knowledge checks.

## Detailed theory

- Store prompts in code or plain text under version control. Name a prompt ID/version in telemetry. Review prompt changes like application changes.
- Test deterministic properties: schema validity, prohibited content absence, required sections, source coverage, length bounds, and refusal handling.
- For semantic quality, use a small human-reviewed dataset and rubric. Model-based grading may assist but must itself be calibrated.
- Because outputs are nondeterministic, distinguish single-run bugs from distributional regressions. Later phases add formal evaluation and observability.
- Never put secrets or private production content in committed fixtures.

**Demonstration:** Create five company-research fixtures and a rubric: completeness 25, evidence discipline 30, factual consistency with supplied sources 25, clarity 10, contract compliance 10.

## Technical explanations

Trace a fixture through the service, schema validator, evidence validator, and rubric. Record prompt/schema/model versions without asserting that a fake test proves real model quality.

## Real-world example

A new prompt looks clearer on one example but drops uncertainty warnings on another. Versioned fixtures reveal the regression before release.

## Code walkthrough

Create a conceptual fixture with input sources, fake provider JSON, expected contract behavior, and prompt_version. Trace it through parsing and source-integrity checks. Then define a separate human-scored live-model evaluation; the fake fixture proves application behavior, while the live evaluation measures generated content. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-11-12-resources) (Lecture 12 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Plan five fixtures and score two prompt versions with the same rubric. Leave result cells blank until measured.

## Knowledge checks

1. Which checks can be fully deterministic?
2. Why is “the answer looked good once” insufficient?
3. What metadata enables comparing prompt versions?

## Completion criteria

Running `pytest` evaluates the prompt service against five fixtures with a fake provider and records the version under test.

## Next lecture

[Previous lecture](lecture-11-zero-shot-few-shot-delimiters-and-prompt-contracts.md) · [Phase assessment](../../../../../assessments/phase-01-assessment.md)
