# Lab 01 — First LLM call with usage telemetry

[Phase home](../../../../../README.md) · [Module](../README.md)

Status: Approved (instructions). Learner execution: Planned.

## Objectives and prerequisites

Complete the owning module lectures, have Python 3.12+ available, and review the resource list. Submit reproducible evidence for the behavior described below.

## Setup and dependencies

Use a separate learner workspace when you begin implementation. The repository currently contains materials only. The commands below describe the future exercise; they have not been run as a live model integration. Do not install exercise dependencies into the repository tooling environment.

For Labs 2–4, reuse the learner package established in Lab 1. Add only the dependencies listed in the exercise and keep your own lockfile. Commands are suggestions, not bundled executables.

## Commands and implementation steps

**Time:** 1h 30m

**Objectives:** Create an isolated project, make one LLM call, record latency and request metadata, and avoid leaking secrets.

**Tools:** Python 3.12+, `venv`, `openai`, `pydantic-settings`, `pytest`.

### Setup

```bash
mkdir ai-foundations && cd ai-foundations
python -m venv .venv
source .venv/bin/activate
python -m pip install openai pydantic pydantic-settings pytest
```

Create `.gitignore` with `.venv/`, `.env`, `__pycache__/`, and `.pytest_cache/`. Put `OPENAI_API_KEY=...` in `.env`; never commit it.

### Folder checkpoint

```text
ai-foundations/
├── .env.example
├── .gitignore
├── pyproject.toml
├── src/ai_foundations/
│   ├── __init__.py
│   ├── config.py
│   └── first_call.py
└── tests/
```

### Implementation

```python
# src/ai_foundations/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    model: str = "set-a-model-available-to-your-account"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
```

```python
# src/ai_foundations/first_call.py
from time import perf_counter
from openai import OpenAI
from .config import Settings

def main() -> None:
    settings = Settings()
    client = OpenAI(api_key=settings.openai_api_key)
    started = perf_counter()
    response = client.responses.create(
        model=settings.model,
        instructions="Answer accurately and in no more than three sentences.",
        input="Explain why an LLM response must be validated by an application.",
    )
    elapsed_ms = round((perf_counter() - started) * 1000)
    print(response.output_text)
    print({"request_id": response.id, "latency_ms": elapsed_ms})

if __name__ == "__main__":
    main()
```

Run with `PYTHONPATH=src python -m ai_foundations.first_call`.

**Expected output:** A short answer plus a response/request identifier and positive latency value. Exact wording varies.

### Common errors and fixes

- `ModuleNotFoundError`: activate `.venv` and use `PYTHONPATH=src`, or install the project in editable mode.
- Authentication failure: confirm `.env` is in the working directory and the variable name matches the settings field.
- Model unavailable: set `MODEL` to a model available to your provider/account.
- Rate limit or timeout: preserve the provider error; do not silently loop. Add bounded retries in Lab 2.

**Acceptance criteria:** Secret is absent from Git; a real response is received; latency/request ID are printed; README states the configured provider/model.

## Expected output and test plan

Use a fake response for formatting checks. For a later opt-in live run, record the configured model, response ID, and latency; never record the API key.

## Troubleshooting

Check the working directory, active environment, dependency versions, timeout configuration, and field names before changing prompts. Use fake providers and mocked HTTP to isolate domain failures. Redact credentials and private payloads from error reports.

## Acceptance criteria and submission

- [ ] Exercise-specific acceptance criteria above demonstrated.
- [ ] Tests and sanitized output captured in the learner submission.
- [ ] Failure behavior demonstrated without hiding invalid output.
- [ ] No secrets or real private invoices committed.
- [ ] Limitations explained in the learner README.

Connect the work to the [project specification](../../../../../../../projects/02-research-analyst/SPEC.md). A successful fake test verifies application behavior; it does not prove live model quality or prompt-injection resistance.
