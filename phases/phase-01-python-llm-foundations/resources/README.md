# Phase 1 learning resources

Resources are adapted from the supplied Phase 1 material. Formats, access labels, and reading estimates are supplied by that material; they are not an independent availability audit. Provider capabilities and model access change. Check official documentation before each live exercise.

## Lecture 1 resources

- **Full Stack Deep Learning — LLM Bootcamp:** course/video, free, optional, 60–90m selected lecture. <https://fullstackdeeplearning.com/llm-bootcamp/> — selected for product-to-production framing.
- **Chip Huyen, Designing Machine Learning Systems:** book, paid (sample material may be free), optional, 45m selected chapters. <https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/> — selected for production system thinking; do not attempt the whole book this week.

## Lecture 2 resources

- **OpenAI text generation guide:** official docs, free, required, 30m. <https://developers.openai.com/api/docs/guides/text> — current Responses API request concepts.
- **Hugging Face LLM Course:** maintained course, free, optional, 45m selected introduction. <https://huggingface.co/learn/llm-course/chapter1/1> — fallback/open-model perspective.

## Lectures 3-4 resources

- **Python tutorial:** official docs, free, required selection, 60m. <https://docs.python.org/3/tutorial/> — focus on control flow, data structures, modules, files, exceptions, and classes; skip elementary material already mastered.
- **Python virtual environments:** official docs, free, required, 20m. <https://docs.python.org/3/tutorial/venv.html>
- **Python typing:** official docs, free, required, 30m. <https://docs.python.org/3/library/typing.html>
- **Python dataclasses:** official docs, free, required, 20m. <https://docs.python.org/3/library/dataclasses.html>
- **Pydantic models:** official docs, free, required, 35m. <https://docs.pydantic.dev/latest/concepts/models/>
- **Pydantic settings:** official docs, free, required, 25m. <https://docs.pydantic.dev/latest/concepts/pydantic_settings/>
- **CS50P exceptions:** Harvard lecture notes/video, free, optional, 45m. <https://cs50.harvard.edu/python/notes/3/> — useful practical fallback if Python exceptions feel unfamiliar.

## Lectures 5-6 resources

- **HTTPX async support:** official docs, free, required, 25m. <https://www.python-httpx.org/async/>
- **HTTPX timeouts:** official docs, free, required, 20m. <https://www.python-httpx.org/advanced/timeouts/>
- **Python asyncio:** official docs, free, required selection, 45m. <https://docs.python.org/3/library/asyncio.html>
- **HTTP Semantics (RFC 9110):** standard, free, optional, 30m selected sections on methods/status codes. <https://www.rfc-editor.org/rfc/rfc9110>

## Lectures 7-8 resources

- **OpenAI Python SDK:** official repository, free, required, 30m. <https://github.com/openai/openai-python>
- **OpenAI Responses API guide:** official docs, free, required, 35m. <https://developers.openai.com/api/docs/guides/text>
- **Gemini API quickstart:** official docs, free to read; API usage may incur cost, optional, 25m. <https://ai.google.dev/gemini-api/docs/quickstart> — provider comparison/fallback.
- **Groq quickstart:** official docs, free to read; API terms/pricing vary, optional, 20m. <https://console.groq.com/docs/quickstart> — OpenAI-compatible comparison/fallback.

## Lectures 9-10 resources

- **OpenAI Structured Outputs:** official docs, free to read; API usage paid, required, 45m. <https://developers.openai.com/api/docs/guides/structured-outputs>
- **OpenAI function calling:** official docs, free to read; API usage paid, required, 45m. <https://developers.openai.com/api/docs/guides/function-calling>
- **Official Python structured-output example:** repository example, free, required, 15m. <https://github.com/openai/openai-python/blob/main/examples/responses/structured_outputs.py>
- **Gemini structured output:** official docs, free to read; optional fallback, 25m. <https://ai.google.dev/gemini-api/docs/structured-output>
- **Groq structured outputs:** official docs, free to read; optional fallback, 20m. <https://console.groq.com/docs/structured-outputs>

## Lectures 11-12 resources

- **OpenAI prompt engineering:** official docs, free, required, 45m. <https://developers.openai.com/api/docs/guides/prompt-engineering>
- **OpenAI prompting/versioning guidance:** official docs, free, required, 25m. <https://developers.openai.com/api/docs/guides/prompting>
- **OpenAI safety best practices:** official docs, free, required selection, 25m. <https://developers.openai.com/api/docs/guides/safety-best-practices>
- **pytest getting started:** official docs, free, required, 30m. <https://docs.pytest.org/en/stable/getting-started.html>
- **OpenAI Cookbook:** maintained official examples, free, optional, 30m targeted browsing. <https://github.com/openai/openai-cookbook>

**Recommended order:** Read only the required resource beside its lecture, complete the lab, then use optional resources to close a specific gap. This preserves the 25-hour budget.

## Reading and API notes

The repository requires Python 3.12+. Read only the required selections needed for the day's objectives; the schedule is a timebox, not a promise that every optional resource fits within 25 hours. Source lecture/lab estimates overlap with project work and are not additional to the daily timeboxes.

API examples require a model available to your account. Keep the model configurable; the original source's illustrative model name is not an availability guarantee. Live API calls can incur cost. Reading and assessment preparation do not need an API key.

The official [structured outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs) and [streaming guide](https://developers.openai.com/api/docs/guides/streaming-responses) were opened during preparation on 2026-10-19. Other links were retained from the supplied material and were not independently revalidated. Some providers support different schemas and stream events.

## Rubric scope

The prompt-comparison rubric in Lecture 12 is a formative exercise. The project-specification rubric measures the future project output. The final phase assessment has its own 100-point distribution and passing threshold; do not combine the three scores.
