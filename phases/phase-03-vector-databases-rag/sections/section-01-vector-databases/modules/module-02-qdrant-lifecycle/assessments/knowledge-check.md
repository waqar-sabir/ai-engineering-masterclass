# Module 3.1.2 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: In Review. Learner submission and score: Planned. Formative review only; attempt before reading solutions.

## Multiple-choice questions

1. An existing collection has the wrong vector dimension. Best default?

   - A. Delete silently
   - B. Pad vectors
   - C. Ignore schema
   - D. Fail and use an explicitly compatible version

2. To show source text in query results, request:

   - A. Payload
   - B. A larger vector dimension
   - C. A new tokenizer
   - D. A model rewrite

## Conceptual questions

1. Why inspect an existing collection? Give a concrete counterexample and the expected safe behavior.
2. Why request payload explicitly? Explain the invariant and how a later test would detect its violation.

## Practical assignment

Complete [the module lab](../labs/lab-02.md); submit its artifact plus an independent failure fixture. Execution belongs to the later implementation pass.

## Debugging scenarios

Attempt both lecture debugging questions. For each, identify the earliest failing stage, the observed evidence, the safe response, and a regression test. Do not assume a model/framework/database change is the first fix.

## Review criteria

- Both multiple-choice answers correct and justified.
- The module-specific contract and counterexample are concrete.
- Lab and failure evidence cover every acceptance criterion.
- No unrun project test, quality score, or completion is claimed.

[Module solutions — after attempting](../../../../../assessments/module-solutions.md).
