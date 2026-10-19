# Module 3.1.1 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: In Review. Learner submission and score: Planned. Formative review only; attempt before reading solutions.

## Multiple-choice questions

1. Which is a valid Qdrant point-ID policy?

   - A. Arbitrary strings always
   - B. Supported UUID/integer IDs with source IDs in payload
   - C. Text embeddings as IDs
   - D. Random ID on every retry

2. ANN recall compares to:

   - A. Generated answer truth
   - B. CPU utilization
   - C. Exact neighbor results
   - D. Source licensing

## Conceptual questions

1. How do ANN recall and relevance recall differ? Give a concrete counterexample and the expected safe behavior.
2. Which point ID forms are supported? Explain the invariant and how a later test would detect its violation.

## Practical assignment

Complete [the module lab](../labs/lab-01.md); submit its artifact plus an independent failure fixture. Execution belongs to the later implementation pass.

## Debugging scenarios

Attempt both lecture debugging questions. For each, identify the earliest failing stage, the observed evidence, the safe response, and a regression test. Do not assume a model/framework/database change is the first fix.

## Review criteria

- Both multiple-choice answers correct and justified.
- The module-specific contract and counterexample are concrete.
- Lab and failure evidence cover every acceptance criterion.
- No unrun project test, quality score, or completion is claimed.

[Module solutions — after attempting](../../../../../assessments/module-solutions.md).
