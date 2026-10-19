# Module 2.2.3 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: Approved. Learner submission: Planned. This is formative; no learner score is recorded.

## Multiple-choice questions

1. Which is a fair model comparison?

   - A. Different corpora and hand-picked queries
   - B. One successful example each
   - C. Same frozen corpus/labels with separate dev and held-out queries
   - D. Larger dimension wins

2. A model migration requires:

   - A. Only changing the query model
   - B. Coordinated query/corpus compatibility and re-encoding
   - C. Padding old vectors with zeros
   - D. Reusing the same threshold without testing

## Conceptual questions

1. Design a fair model comparison with a fixed corpus, labeled queries, development choices, and held-out reporting.
2. Explain why a model change requires full corpus re-encoding and coordinated activation rather than dimensionality padding.

## Practical assignment

Complete [the module lab](../labs/lab-05.md). Submit its worksheet, proposed tests, and the independent failure example. Code execution belongs to later learner work, not to material preparation.

## Debugging scenario

Attempt both lecture debugging scenarios. Identify the failure boundary, a reproducible minimal case, the expected safe behavior, and the test that would prevent regression.

## Review criteria

- Both multiple-choice answers correct and justified.
- Conceptual answers connect the mechanism to a concrete failure.
- Lab acceptance criteria and counterexample are reviewable.
- No invented model-quality, latency, or completion result.

[Solutions — open after attempting](../../../../../assessments/module-solutions.md).
