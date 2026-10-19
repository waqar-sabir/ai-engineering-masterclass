# Module 2.2.2 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: Approved. Learner submission: Planned. This is formative; no learner score is recorded.

## Multiple-choice questions

1. Two embeddings have the same length but different models. They are:

   - A. Always compatible
   - B. Compatible after sorting
   - C. Compatible if both float32
   - D. Not proven compatible

2. When should a new snapshot become current?

   - A. After the first vector is written
   - B. After all artifact checks pass
   - C. Before the corpus is frozen
   - D. Whenever query traffic is low

## Conceptual questions

1. List the complete compatibility contract for query and corpus embeddings, including revisions, roles, pooling, and normalization.
2. Explain how a partial snapshot write or independently sorted metadata can corrupt results without producing a numeric error.

## Practical assignment

Complete [the module lab](../labs/lab-04.md). Submit its worksheet, proposed tests, and the independent failure example. Code execution belongs to later learner work, not to material preparation.

## Debugging scenario

Attempt both lecture debugging scenarios. Identify the failure boundary, a reproducible minimal case, the expected safe behavior, and the test that would prevent regression.

## Review criteria

- Both multiple-choice answers correct and justified.
- Conceptual answers connect the mechanism to a concrete failure.
- Lab acceptance criteria and counterexample are reviewable.
- No invented model-quality, latency, or completion result.

[Solutions — open after attempting](../../../../../assessments/module-solutions.md).
