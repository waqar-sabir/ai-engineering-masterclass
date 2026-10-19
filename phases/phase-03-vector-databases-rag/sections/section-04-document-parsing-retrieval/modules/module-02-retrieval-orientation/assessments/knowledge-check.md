# Module 3.4.2 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: In Review. Learner submission and score: Planned. Formative review only; attempt before reading solutions.

## Multiple-choice questions

1. A reranker can recover a relevant document absent from all candidates:

   - A. Always
   - B. No, not by reordering that set
   - C. Only with a lower c value
   - D. If citation labels are valid

2. Rank fusion is useful because:

   - A. All raw scores have the same units
   - B. It proves factuality
   - C. It combines ranks without assuming comparable raw scales
   - D. It removes the need for relevance labels

## Conceptual questions

1. Why retain the original query? Give a concrete counterexample and the expected safe behavior.
2. Why avoid raw-score addition? Explain the invariant and how a later test would detect its violation.

## Practical assignment

Complete [the module lab](../labs/lab-09.md); submit its artifact plus an independent failure fixture. Execution belongs to the later implementation pass.

## Debugging scenarios

Attempt both lecture debugging questions. For each, identify the earliest failing stage, the observed evidence, the safe response, and a regression test. Do not assume a model/framework/database change is the first fix.

## Review criteria

- Both multiple-choice answers correct and justified.
- The module-specific contract and counterexample are concrete.
- Lab and failure evidence cover every acceptance criterion.
- No unrun project test, quality score, or completion is claimed.

[Module solutions — after attempting](../../../../../assessments/module-solutions.md).
