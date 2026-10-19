# Lab 02 — Resilient async research-source client

[Phase home](../../../../../README.md) · [Module](../README.md)

Status: Approved (instructions). Learner execution: Planned.

## Objectives and prerequisites

Complete the owning module lectures, have Python 3.12+ available, and review the resource list. Submit reproducible evidence for the behavior described below.

## Setup and dependencies

Use a separate learner workspace when you begin implementation. The repository currently contains materials only. The commands below describe the future exercise; they have not been run as a live model integration. Do not install exercise dependencies into the repository tooling environment.

For Labs 2–4, reuse the learner package established in Lab 1. Add only the dependencies listed in the exercise and keep your own lockfile. Commands are suggestions, not bundled executables.

## Commands and implementation steps

**Time:** 2 hours

**Goal:** Build a reusable HTTP client used later by the capstone. It fetches explicitly supplied URLs; it does not crawl the web autonomously.

**Dependencies:** `httpx`, `pydantic`, `pytest`, `pytest-asyncio`.

### Steps

1. Define `SourceDocument(url, status_code, content_type, text, fetched_at)` as a Pydantic model.
2. Implement one long-lived `httpx.AsyncClient` with separate timeout values.
3. Require `https` URLs and reject private/link-local IP targets for the production extension; document SSRF as a known MVP risk if not implemented.
4. Use a semaphore with configurable concurrency.
5. Retry at most twice for timeout, 429, and selected 5xx responses. Never retry 401/403/404 automatically.
6. Cap downloaded bytes and accept only approved text content types.
7. Unit-test using `httpx.MockTransport`: success, timeout-then-success, 404-no-retry, invalid content type, oversized response.

**Expected behavior:** The result preserves the requested URL, final status, normalized text, and fetch time. Failures are typed and identify whether retry is safe.

**Troubleshooting:** If tests sleep, inject a `sleep` callable and use a no-op fake. If async tests are not discovered, confirm the plugin and marker. If connections leak, ensure the client closes once at application shutdown.

**Acceptance criteria:** Five tests pass; concurrency is bounded; errors are not converted to empty strings; secrets and response bodies are not logged by default.

## Expected output and test plan

Use MockTransport for success, timeout-then-success, 404 with no retry, unsupported content type, and oversized response. Inject sleep to avoid real waits. Add one bounded-concurrency check.

## Troubleshooting

Check the working directory, active environment, dependency versions, timeout configuration, and field names before changing prompts. Use fake providers and mocked HTTP to isolate domain failures. Redact credentials and private payloads from error reports.

## Acceptance criteria and submission

- [ ] Exercise-specific acceptance criteria above demonstrated.
- [ ] Tests and sanitized output captured in the learner submission.
- [ ] Failure behavior demonstrated without hiding invalid output.
- [ ] No secrets or real private invoices committed.
- [ ] Limitations explained in the learner README.

Connect the work to the [project specification](../../../../../../../projects/02-research-analyst/SPEC.md). A successful fake test verifies application behavior; it does not prove live model quality or prompt-injection resistance.
