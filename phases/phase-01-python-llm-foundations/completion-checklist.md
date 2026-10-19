# Phase 1 completion checklist

[Phase home](README.md)

All checkboxes describe future learner work. Course material preparation does not mark any item complete.

## Knowledge

- [ ] I can explain tokens, context, sampling, time-to-first-token, and total latency.
- [ ] I can distinguish API compatibility from behavioral compatibility.
- [ ] I can explain schema validity versus semantic/factual validity.
- [ ] I can defend retry, timeout, concurrency, and idempotency decisions.
- [ ] I can explain why model/tool output is untrusted.

## Labs

- [ ] Lab 1: first call and telemetry.
- [ ] Lab 2: resilient bounded async client.
- [ ] Lab 3: streaming CLI with cancellation.
- [ ] Lab 4: invoice extraction plus deterministic arithmetic validation.

## Project

- [ ] Research Assistant emits validated JSON and Markdown.
- [ ] Evidence references are constrained to fetched sources.
- [ ] Five evaluation fixtures and failure cases are documented.
- [ ] Architecture, security, limitations, latency, and measured usage are in README.
- [ ] Repository contains no secrets or sensitive fixtures.

## Git milestones

- [ ] `chore: bootstrap typed Python project`
- [ ] `feat: add resilient async source client`
- [ ] `feat: add provider adapter and structured contracts`
- [ ] `test: add prompt and evidence regression fixtures`
- [ ] `docs: add architecture, demo, and limitations`

## Ready for Phase 2 when

You can implement and test a typed LLM application without a framework, explain every request/response boundary, and diagnose provider, validation, and concurrency failures. Do not proceed merely because the happy-path demo works.
