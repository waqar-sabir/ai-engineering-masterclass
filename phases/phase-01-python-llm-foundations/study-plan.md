# Phase 1 study plan

## Prerequisites

- Comfortable with APIs, JSON, Git, HTTP, and automated testing.
- Python 3.12+ installed. Python syntax knowledge is helpful but not required.
- For later live labs only: one LLM provider API key. OpenAI examples use the Responses API; validate capabilities separately before substituting another endpoint. Reading and planning do not require a key.
- A Git repository and terminal.

## Learning objectives

By the end of Phase 1, you will be able to:

1. Explain an LLM request lifecycle and the trade-offs between hosted APIs and self-hosted models.
2. Build a production-shaped Python package with isolated dependencies, typed settings, and secret-safe configuration.
3. Implement synchronous and asynchronous HTTP clients with authentication, timeouts, retries, and bounded concurrency.
4. Call an LLM through a provider abstraction and distinguish instructions, user input, generated text, structured output, and tool calls.
5. Define strict Pydantic contracts, emit JSON Schema, validate untrusted model output, and handle refusals or malformed responses.
6. Design zero-shot and few-shot prompts, version them in code, and regression-test observable behavior.
7. Build, test, document, and demo a reliable research-assistant MVP without pretending it is RAG or a fully autonomous agent.

## Skills gained

- Python typing, modules, dataclasses, protocols, Pydantic, settings, exceptions, and pytest.
- HTTPX sync/async usage, error taxonomy, retry policy, rate-limit handling, and concurrency control.
- LLM API fundamentals: tokens, context, sampling, streaming, structured outputs, and tool schemas.
- Prompt contracts, prompt injection awareness, cost/latency instrumentation, and evidence boundaries.
- Architecture communication through requirements, API contracts, failure analysis, and trade-offs.

## Seven-day schedule

- **Day 1 — 3h 15m:** AI engineering mindset, request lifecycle, first LLM call.
- **Day 2 — 3h 30m:** Python project structure, typing, settings, files/JSON, tests.
- **Day 3 — 3h 30m:** HTTP, authentication, async I/O, errors, retries.
- **Day 4 — 3h 15m:** LLM APIs, provider abstraction, streaming CLI assistant.
- **Day 5 — 3h 45m:** Pydantic structured outputs, JSON Schema, tool calling, invoice workflow.
- **Day 6 — 3h 15m:** Prompt engineering, prompt versioning, regression tests.
- **Day 7 — 4h 30m:** System design, Research Assistant capstone, assessment, documentation.

## Timebox guidance

The seven daily budgets total 25 hours. Lecture estimates, lab estimates, required readings, project work, and review overlap; do not add all listed estimates and expect a strict 25-hour ceiling. Experienced learners should skim familiar topics and use optional readings only to resolve gaps. Extend the calendar when needed to satisfy acceptance criteria.

## Day-to-material navigation

- Day 1: [Lecture 1](sections/section-01-ai-engineering-foundations/modules/module-01-llm-application-lifecycle/lectures/lecture-01-what-an-ai-engineer-builds.md), [Lecture 2](sections/section-01-ai-engineering-foundations/modules/module-01-llm-application-lifecycle/lectures/lecture-02-llm-request-lifecycle-tokens-and-model-access.md); [Lab 1](sections/section-01-ai-engineering-foundations/modules/module-01-llm-application-lifecycle/labs/lab-01.md).
- Day 2: [Lecture 3](sections/section-02-production-python/modules/module-01-types-boundaries-configuration/lectures/lecture-03-python-project-structure-for-an-experienced-engineer.md), [Lecture 4](sections/section-02-production-python/modules/module-01-types-boundaries-configuration/lectures/lecture-04-configuration-secrets-and-validation.md); package and settings exercise.
- Day 3: [Lecture 5](sections/section-02-production-python/modules/module-02-http-async-io/lectures/lecture-05-http-client-engineering.md), [Lecture 6](sections/section-02-production-python/modules/module-02-http-async-io/lectures/lecture-06-async-python-and-bounded-concurrency.md); [Lab 2](sections/section-02-production-python/modules/module-02-http-async-io/labs/lab-02.md).
- Day 4: [Lecture 7](sections/section-03-llm-apis-contracts-prompts/modules/module-01-provider-boundaries-streaming/lectures/lecture-07-llm-apis-and-provider-abstraction.md), [Lecture 8](sections/section-03-llm-apis-contracts-prompts/modules/module-01-provider-boundaries-streaming/lectures/lecture-08-streaming-cancellation-and-user-experience.md); [Lab 3](sections/section-03-llm-apis-contracts-prompts/modules/module-01-provider-boundaries-streaming/labs/lab-03.md).
- Day 5: [Lecture 9](sections/section-03-llm-apis-contracts-prompts/modules/module-02-structured-output-tool-contracts/lectures/lecture-09-pydantic-json-schema-and-structured-model-output.md), [Lecture 10](sections/section-03-llm-apis-contracts-prompts/modules/module-02-structured-output-tool-contracts/lectures/lecture-10-function-tool-calling-as-a-controlled-protocol.md); [Lab 4](sections/section-03-llm-apis-contracts-prompts/modules/module-02-structured-output-tool-contracts/labs/lab-04.md).
- Day 6: [Lecture 11](sections/section-03-llm-apis-contracts-prompts/modules/module-03-prompt-engineering/lectures/lecture-11-zero-shot-few-shot-delimiters-and-prompt-contracts.md), [Lecture 12](sections/section-03-llm-apis-contracts-prompts/modules/module-03-prompt-engineering/lectures/lecture-12-prompt-versioning-and-regression-testing.md); prompt and fixture planning.
- Day 7: [gateway case study](../../system-design/02-inference-gateway/README.md), [project specification](../../projects/02-research-analyst/SPEC.md), and [assessment](assessments/phase-01-assessment.md).
