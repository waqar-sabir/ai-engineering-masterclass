# Lab 03 — Streaming CLI assistant

[Phase home](../../../../../README.md) · [Module](../README.md)

Status: Approved (instructions). Learner execution: Planned.

## Objectives and prerequisites

Complete the owning module lectures, have Python 3.12+ available, and review the resource list. Submit reproducible evidence for the behavior described below.

## Setup and dependencies

Use a separate learner workspace when you begin implementation. The repository currently contains materials only. The commands below describe the future exercise; they have not been run as a live model integration. Do not install exercise dependencies into the repository tooling environment.

For Labs 2–4, reuse the learner package established in Lab 1. Add only the dependencies listed in the exercise and keep your own lockfile. Commands are suggestions, not bundled executables.

## Commands and implementation steps

**Time:** 1h 45m

### Steps

1. Add `cli.py` with an input loop and `/quit` command.
2. Put stable behavior in provider instructions and the user’s question in input.
3. Stream plain text, handle Ctrl+C, and print a clear incomplete marker on failure.
4. Record request ID, model, latency, and (when available) input/output usage after completion.
5. Add a `--no-stream` mode used by deterministic tests.
6. Test command parsing, fake-provider output, cancellation, and redaction.

**Acceptance criteria:** The assistant handles three turns, exits cleanly, never prints the API key, and distinguishes incomplete from completed output.

## Expected output and test plan

Test fake-provider rendering, /quit, three independent turns, cancellation, partial-stream failure, and secret redaction. --no-stream must use the same input contract.

## Troubleshooting

Check the working directory, active environment, dependency versions, timeout configuration, and field names before changing prompts. Use fake providers and mocked HTTP to isolate domain failures. Redact credentials and private payloads from error reports.

## Acceptance criteria and submission

- [ ] Exercise-specific acceptance criteria above demonstrated.
- [ ] Tests and sanitized output captured in the learner submission.
- [ ] Failure behavior demonstrated without hiding invalid output.
- [ ] No secrets or real private invoices committed.
- [ ] Limitations explained in the learner README.

Connect the work to the [project specification](../../../../../../../projects/02-research-analyst/SPEC.md). A successful fake test verifies application behavior; it does not prove live model quality or prompt-injection resistance.
