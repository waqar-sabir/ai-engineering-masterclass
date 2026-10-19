# Lecture 09 — Pydantic, JSON Schema, and structured model output

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P01-L09 · Duration: 90 minutes · Material status: In Review · Learner completion: Planned.

## Learning objectives

Turn a domain contract into JSON Schema; use strict structured output where available; validate syntax and semantics.

## Prerequisites

Complete Lecture 8 and its knowledge checks.

## Detailed theory

- JSON validity, schema validity, and factual correctness are separate properties.
- Define nested Pydantic models with field descriptions and constraints. Prefer `extra="forbid"` at strict boundaries.
- Many model providers support only a subset of JSON Schema. Keep schemas shallow, explicit, and provider-tested.
- A schema-conforming answer can still contain invented facts. Add semantic checks: URL scheme, totals, allowed enums, date ranges, source coverage, and cross-field invariants.
- Handle refusal/incomplete states separately from validation failures. Retrying the same request unchanged is rarely a complete recovery policy.

### Demonstration

```python
from pydantic import BaseModel, ConfigDict, Field, HttpUrl

class SourceRef(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: HttpUrl
    supports: list[str] = Field(min_length=1)

class CompanyBrief(BaseModel):
    model_config = ConfigDict(extra="forbid")
    company: str = Field(min_length=1)
    overview: str
    industry: str
    products: list[str]
    competitors: list[str]
    recent_developments: list[str]
    summary: str
    sources: list[SourceRef]
```

## Technical explanations

Read the nested model example below, then trace valid JSON, a missing field, and a fabricated URL through the three distinct validation stages.

## Real-world example

A generated brief can satisfy every JSON field and still invent a product. Validate references and review actual evidence separately.

## Code walkthrough

In SourceRef, HttpUrl checks URL syntax but not caller approval. In CompanyBrief, field types check shape but not truth. Parse a sample JSON value, reject an extra field, then perform an allowed-URL check in a second function. Extend that check to require coverage for every nonempty section. This is a teaching walkthrough; implementation is deferred.

## Learning resources

[Required and optional resources](../../../../../resources/README.md#lectures-9-10-resources) (Lecture 9 grouping). Read required selections alongside the lecture; optional resources close specific gaps.

## Hands-on exercise

Add a semantic rule rejecting an unsupported source URL. Explain why extra="forbid" alone cannot enforce it.

## Knowledge checks

1. Can strict decoding prove factual correctness?
2. Why use `extra="forbid"`?
3. Name two semantic validations for a company brief.
4. How should a refusal differ from malformed output in telemetry?

## Completion criteria

Valid sample output parses; missing and extra fields fail; a semantic error is caught after schema validation.

## Next lecture

[Previous lecture](../../module-01-provider-boundaries-streaming/lectures/lecture-08-streaming-cancellation-and-user-experience.md) · [Next lecture](lecture-10-function-tool-calling-as-a-controlled-protocol.md)
