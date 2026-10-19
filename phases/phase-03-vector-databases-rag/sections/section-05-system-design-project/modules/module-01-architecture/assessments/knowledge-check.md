# Module 3.5.1 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: In Review. Learner submission and score: Planned. Formative review only; attempt before reading solutions.

## Multiple-choice questions

1. 100×20×384 float32 vectors occupy raw bytes of:

   - A. 3,072,000
   - B. 384
   - C. Exactly the peak process memory
   - D. Zero if indexed

2. A complete generation becomes active:

   - A. After the first point
   - B. Before parser status checks
   - C. After source/payload/vector validation and required smoke checks
   - D. After any nonempty model response

## Conceptual questions

1. What should be versioned end to end? Give a concrete counterexample and the expected safe behavior.
2. What does raw vector storage omit? Explain the invariant and how a later test would detect its violation.

## Practical assignment

Complete [the module lab](../labs/lab-10.md); submit its artifact plus an independent failure fixture. Execution belongs to the later implementation pass.

## Debugging scenarios

Attempt both lecture debugging questions. For each, identify the earliest failing stage, the observed evidence, the safe response, and a regression test. Do not assume a model/framework/database change is the first fix.

## Review criteria

- Both multiple-choice answers correct and justified.
- The module-specific contract and counterexample are concrete.
- Lab and failure evidence cover every acceptance criterion.
- No unrun project test, quality score, or completion is claimed.

[Module solutions — after attempting](../../../../../assessments/module-solutions.md).
