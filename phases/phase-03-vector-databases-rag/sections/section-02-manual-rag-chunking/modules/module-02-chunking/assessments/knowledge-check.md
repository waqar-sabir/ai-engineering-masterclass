# Module 3.2.2 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: In Review. Learner submission and score: Planned. Formative review only; attempt before reading solutions.

## Multiple-choice questions

1. With length_function=len, chunk_size counts:

   - A. Model tokens
   - B. Documents
   - C. Characters
   - D. Bytes in every encoding

2. Overlap should normally be:

   - A. Equal to size
   - B. Larger than size
   - C. Unbounded
   - D. Smaller than size

## Conceptual questions

1. Which unit does len count? Give a concrete counterexample and the expected safe behavior.
2. What happens as overlap approaches size? Explain the invariant and how a later test would detect its violation.

## Practical assignment

Complete [the module lab](../labs/lab-04.md); submit its artifact plus an independent failure fixture. Execution belongs to the later implementation pass.

## Debugging scenarios

Attempt both lecture debugging questions. For each, identify the earliest failing stage, the observed evidence, the safe response, and a regression test. Do not assume a model/framework/database change is the first fix.

## Review criteria

- Both multiple-choice answers correct and justified.
- The module-specific contract and counterexample are concrete.
- Lab and failure evidence cover every acceptance criterion.
- No unrun project test, quality score, or completion is claimed.

[Module solutions — after attempting](../../../../../assessments/module-solutions.md).
