# Lecture 12 — Messages, invocation, output contracts, and test doubles

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L12 · Day 20 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Does invoke mean provider equivalence?
- Explain and demonstrate: Where do evidence instructions belong?
- Explain and demonstrate: How can fake tests stay free of credentials?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

A chat-model abstraction accepts structured messages and returns a model-specific response represented through the framework. Keep stable policy instructions separate from the question and retrieved source data. Inspect response content and usage deliberately; do not assume every provider returns plain text in exactly the same place.

An invocation method standardizes how to call a component, but does not establish identical model capabilities, timeout behavior, token accounting, structured-output support, or refusal handling. Translate errors at the adapter boundary and keep an overall deadline so nested retry layers cannot multiply unchecked.

Test a composed service with fixed retrieved documents and a fake model result. Verify message roles, source labels, budget decisions, output parsing, and unknown-citation rejection. Live generation quality remains a separate task. No key is required for material review or deterministic exercise design.

## Practical example and walkthrough

A fake model returns malformed cited JSON. The same output validator should reject it whether the caller used a manual adapter or a LangChain model wrapper.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [LangChain Models](https://docs.langchain.com/oss/python/langchain/models) — Official documentation, free to read; selected invocation and structured outputs; skip agents/tools; 15 min study estimate. Review provider boundaries without pulling agent loops forward.
- [LangChain Messages](https://docs.langchain.com/oss/python/langchain/messages) — Official documentation, free to read; selected message roles and response content; 15 min study estimate. Keep instructions separate from retrieved untrusted source text.

Optional supplements/fallbacks:

- [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — Official security guidance, free to read; selected indirect prompt injection and layered controls; 20 min study estimate. Supports a clear trust boundary; delimiters alone do not establish security.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Specify a fake-model fixture and the messages it should receive for one answerable and one insufficient-evidence question. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-06.md) as the practical follow-through.

## Debugging scenario

The framework changes response content shape after an upgrade. Which adapter test should catch this?

## Knowledge check

1. Does invoke mean provider equivalence?
2. Where do evidence instructions belong?
3. How can fake tests stay free of credentials?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-11-langchain-components-and-provider-boundaries.md) · [Next](../../module-02-integration-parity/lectures/lecture-13-rag-with-langchain-and-qdrant-integration-contracts.md)
