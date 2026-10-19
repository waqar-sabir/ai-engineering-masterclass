# Phase 01 — Python + LLM Foundations

[Course home](../../README.md) · [Syllabus](../../COURSE-SYLLABUS.md) · [Progress](../../PROGRESS.md)

## Overview

Days 1–7 · Suggested daily timeboxes: 25 hours total · Foundation to intermediate.

**Material status: Approved. Learner completion: Planned. Implementation: Planned.** This phase contains teaching material only. Code blocks and commands are examples and future exercises, not a bundled application.

Build the knowledge needed to design a tested CLI Research Assistant and a text-only Invoice Extraction workflow. Embeddings, RAG, vector databases, autonomous agent loops, and LangGraph remain in later phases.

## Prerequisites

Experienced software engineering, HTTP/JSON, Git, automated testing, and a terminal. Python 3.12+ for later exercises. No API key is needed to read the course; later live labs require a provider account, a configured model, and spending limits.

## Learning objectives

By the end of Phase 1, you will be able to:

1. Explain an LLM request lifecycle and the trade-offs between hosted APIs and self-hosted models.
2. Build a production-shaped Python package with isolated dependencies, typed settings, and secret-safe configuration.
3. Implement synchronous and asynchronous HTTP clients with authentication, timeouts, retries, and bounded concurrency.
4. Call an LLM through a provider abstraction and distinguish instructions, user input, generated text, structured output, and tool calls.
5. Define strict Pydantic contracts, emit JSON Schema, validate untrusted model output, and handle refusals or malformed responses.
6. Design zero-shot and few-shot prompts, version them in code, and regression-test observable behavior.
7. Build, test, document, and demo a reliable research-assistant MVP without pretending it is RAG or a fully autonomous agent.

## Sections and modules

- [Section 1.1 — AI engineering foundations](sections/section-01-ai-engineering-foundations/README.md)
- [Section 1.2 — Production-shaped Python for AI](sections/section-02-production-python/README.md)
- [Section 1.3 — LLM APIs, structured outputs, and prompts](sections/section-03-llm-apis-contracts-prompts/README.md)

Each section links its modules, lectures, resources, labs, formative assessments, and project contribution.

## Lecture navigation

- [Lecture 01 — What an AI engineer builds](sections/section-01-ai-engineering-foundations/modules/module-01-llm-application-lifecycle/lectures/lecture-01-what-an-ai-engineer-builds.md)
- [Lecture 02 — LLM request lifecycle, tokens, and model access](sections/section-01-ai-engineering-foundations/modules/module-01-llm-application-lifecycle/lectures/lecture-02-llm-request-lifecycle-tokens-and-model-access.md)
- [Lecture 03 — Python project structure for an experienced engineer](sections/section-02-production-python/modules/module-01-types-boundaries-configuration/lectures/lecture-03-python-project-structure-for-an-experienced-engineer.md)
- [Lecture 04 — Configuration, secrets, and validation](sections/section-02-production-python/modules/module-01-types-boundaries-configuration/lectures/lecture-04-configuration-secrets-and-validation.md)
- [Lecture 05 — HTTP client engineering](sections/section-02-production-python/modules/module-02-http-async-io/lectures/lecture-05-http-client-engineering.md)
- [Lecture 06 — Async Python and bounded concurrency](sections/section-02-production-python/modules/module-02-http-async-io/lectures/lecture-06-async-python-and-bounded-concurrency.md)
- [Lecture 07 — LLM APIs and provider abstraction](sections/section-03-llm-apis-contracts-prompts/modules/module-01-provider-boundaries-streaming/lectures/lecture-07-llm-apis-and-provider-abstraction.md)
- [Lecture 08 — Streaming, cancellation, and user experience](sections/section-03-llm-apis-contracts-prompts/modules/module-01-provider-boundaries-streaming/lectures/lecture-08-streaming-cancellation-and-user-experience.md)
- [Lecture 09 — Pydantic, JSON Schema, and structured model output](sections/section-03-llm-apis-contracts-prompts/modules/module-02-structured-output-tool-contracts/lectures/lecture-09-pydantic-json-schema-and-structured-model-output.md)
- [Lecture 10 — Function/tool calling as a controlled protocol](sections/section-03-llm-apis-contracts-prompts/modules/module-02-structured-output-tool-contracts/lectures/lecture-10-function-tool-calling-as-a-controlled-protocol.md)
- [Lecture 11 — Zero-shot, few-shot, delimiters, and prompt contracts](sections/section-03-llm-apis-contracts-prompts/modules/module-03-prompt-engineering/lectures/lecture-11-zero-shot-few-shot-delimiters-and-prompt-contracts.md)
- [Lecture 12 — Prompt versioning and regression testing](sections/section-03-llm-apis-contracts-prompts/modules/module-03-prompt-engineering/lectures/lecture-12-prompt-versioning-and-regression-testing.md)

## Learning resources

[Curated resource list](resources/README.md) · [Study plan](study-plan.md) · [Source and adaptation notes](resources/source-notes.md)

## Labs

- [Lab 01 — First LLM call with usage telemetry](sections/section-01-ai-engineering-foundations/modules/module-01-llm-application-lifecycle/labs/lab-01.md)
- [Lab 02 — Resilient async research-source client](sections/section-02-production-python/modules/module-02-http-async-io/labs/lab-02.md)
- [Lab 03 — Streaming CLI assistant](sections/section-03-llm-apis-contracts-prompts/modules/module-01-provider-boundaries-streaming/labs/lab-03.md)
- [Lab 04 — Invoice Processing Workflow MVP](sections/section-03-llm-apis-contracts-prompts/modules/module-02-structured-output-tool-contracts/labs/lab-04.md)

## System design exercises

[LLM application architecture](../../system-design/01-llm-application-architecture/README.md) · [Multi-provider inference gateway](../../system-design/02-inference-gateway/README.md)

## Phase project

[AI Research Assistant specification](../../projects/02-research-analyst/SPEC.md) · [Invoice Processing lab specification](../../projects/01-invoice-processing/SPEC.md)

Both are specifications for later implementation. The Research Assistant uses 2–5 user-approved sources and validates references; it is not an autonomous research agent.

## Assessments

[Phase assessment](assessments/phase-01-assessment.md) · [Solution guide — attempt first](assessments/solution-guide.md)

Pass: 75/100 overall and at least 20/35 on coding, with no committed secret. No submission, score, or pass is claimed.

## Completion checklist

[Full learner checklist](completion-checklist.md)

- [ ] Lectures, resources, exercises, and labs completed by learner.
- [ ] Project and failure demonstrations submitted.
- [ ] Assessment passed and system design reviewed.
- [ ] Material review and explicit owner approval recorded.

[Material validation notes](validation.md).

## Next phase

[Phase 2 overview](../phase-02-llm-internals-embeddings/README.md). Phase 2 materials are now Approved following the user’s explicit request to continue. Phase 1 learner completion is still Planned.
