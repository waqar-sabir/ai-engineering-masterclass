# Module 3.2.3 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: In Review. Learner submission and score: Planned. Formative review only; attempt before reading solutions.

## Multiple-choice questions

1. Upserting the new first three chunks of an old five-chunk source:

   - A. Always removes the remaining two
   - B. Does not by itself remove stale tail chunks
   - C. Changes the tokenizer
   - D. Proves activation is atomic

2. A CSV locator should preserve:

   - A. Invented PDF page
   - B. Only a score
   - C. Row/header identity and source version
   - D. No provenance

## Conceptual questions

1. Why record source versions? Give a concrete counterexample and the expected safe behavior.
2. Why separate write from activation? Explain the invariant and how a later test would detect its violation.

## Practical assignment

Complete [the module lab](../labs/lab-05.md); submit its artifact plus an independent failure fixture. Execution belongs to the later implementation pass.

## Debugging scenarios

Attempt both lecture debugging questions. For each, identify the earliest failing stage, the observed evidence, the safe response, and a regression test. Do not assume a model/framework/database change is the first fix.

## Review criteria

- Both multiple-choice answers correct and justified.
- The module-specific contract and counterexample are concrete.
- Lab and failure evidence cover every acceptance criterion.
- No unrun project test, quality score, or completion is claimed.

[Module solutions — after attempting](../../../../../assessments/module-solutions.md).
