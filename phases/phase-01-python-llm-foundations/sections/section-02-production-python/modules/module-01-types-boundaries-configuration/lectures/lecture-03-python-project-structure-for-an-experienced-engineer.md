# Lecture 03 — Python project structure for an experienced engineer

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L03 · Duration: 75 minutes · Material status: In Review · Learner completion: Planned.

## Learning objectives

Translate familiar TypeScript architecture into Python conventions; use packages, functions, classes, protocols, type hints, dataclasses, and file/JSON I/O deliberately.

## Prerequisites

Complete Lecture 2 and its knowledge checks.

## Detailed theory

- Prefer a `src/` layout, small modules, explicit imports, and dependency injection at composition roots.
- Python type hints aid static analysis but are not runtime validation. Use `dataclass` for trusted internal data and Pydantic for untrusted boundaries.
- A `Protocol` expresses structural behavior similar to a TypeScript interface. It is useful for provider abstractions without a framework.
- Use `pathlib.Path` for filesystem paths, context managers for files/resources, and UTF-8 explicitly.
- Exceptions should communicate failure semantics. Catch errors where you can add context, recover, translate to a domain error, or clean up; avoid `except Exception: pass`.

### Demonstration

```python
from typing import Protocol

class TextModel(Protocol):
    def generate(self, *, instructions: str, input_text: str) -> str: ...

def summarize(model: TextModel, text: str) -> str:
    return model.generate(instructions="Summarize faithfully.", input_text=text)
```

## Technical explanations

Read the Protocol example below. Replace the implementation mentally with a fake returning fixed text; identify which caller does not need to change.

## Real-world example

A service tested against a fake provider can diagnose domain failures without waiting for an upstream API or paying for tokens.

## Code walkthrough

In the Protocol example, generate is a keyword-only method returning text. summarize accepts behavior rather than constructing a concrete client. Sketch a FakeTextModel implementing the same signature, then trace summarize(fake, text). Explain why this makes a unit test independent of network access. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-3-4-resources) (Lecture 3 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Sketch a package with a provider Protocol and fake. Explain the difference between static typing and runtime validation.

## Knowledge checks

1. When should a dataclass be preferred over a Pydantic model?
2. Do type hints reject invalid runtime JSON by themselves?
3. What architectural benefit does a `Protocol` provide?

## Completion criteria

You can create a typed package and substitute a fake model in a unit test.

## Next lecture

[Previous lecture](../../../../section-01-ai-engineering-foundations/modules/module-01-llm-application-lifecycle/lectures/lecture-02-llm-request-lifecycle-tokens-and-model-access.md) · [Next lecture](lecture-04-configuration-secrets-and-validation.md)
