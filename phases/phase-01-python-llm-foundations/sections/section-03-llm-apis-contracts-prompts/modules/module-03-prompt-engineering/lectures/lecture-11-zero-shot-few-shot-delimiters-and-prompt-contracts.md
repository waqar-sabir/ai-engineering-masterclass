# Lecture 11 — Zero-shot, few-shot, delimiters, and prompt contracts

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L11 · Duration: 75 minutes · Material status: Approved · Learner completion: Planned.

## Learning objectives

Start with the simplest prompt; add context/examples based on measured failures; define authority and success criteria.

## Prerequisites

Complete Lecture 10 and its knowledge checks.

## Detailed theory

- A useful prompt contract states: task, authoritative instructions, supplied context, constraints, output shape, uncertainty policy, and success criteria.
- Try zero-shot first. Add few-shot examples only for recurring ambiguous behavior, and ensure examples exactly match the desired contract.
- Separate instructions from untrusted data using explicit sections or XML-style delimiters. Delimiting does not neutralize malicious content; application policy still controls authority.
- Avoid asking for hidden chain-of-thought. Request the needed answer, concise justification, evidence, or verifiable intermediate artifacts.
- Prompts cannot guarantee truth. Grounding, validation, evaluation, and user-visible uncertainty remain necessary.

**Demonstration:** Evolve a vague company-summary prompt into a versioned contract that returns only claims supported by supplied source text and marks unsupported fields.

## Technical explanations

Compare the company-summary prompt before and after adding an evidence policy. Check that examples match the schema and no sensitive data is embedded.

## Real-world example

A source page includes “ignore prior instructions.” Treat this as untrusted document text; application authorization remains unchanged.

## Code walkthrough

Compare two prompt drafts with the same schema. In the second draft label authoritative instructions, source data, uncertainty rules, and required evidence. If adding an example, verify every example field against the contract. Keep user text out of the authoritative instruction section. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-11-12-resources) (Lecture 11 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Create zero-shot and few-shot prompt drafts for the same schema. Explain the observed failure that would justify an example.

## Knowledge checks

1. When is few-shot prompting justified?
2. What is the difference between a delimiter and a security boundary?
3. Why should uncertainty behavior be explicit?

## Completion criteria

A prompt has a named goal, authority boundaries, output contract, and three representative test cases.

## Next lecture

[Previous lecture](../../module-02-structured-output-tool-contracts/lectures/lecture-10-function-tool-calling-as-a-controlled-protocol.md) · [Next lecture](lecture-12-prompt-versioning-and-regression-testing.md)
