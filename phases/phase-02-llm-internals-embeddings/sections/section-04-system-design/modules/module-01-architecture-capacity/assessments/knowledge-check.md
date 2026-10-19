# Module 2.4.1 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: Approved. Learner submission: Planned. This is formative; no learner score is recorded.

## Multiple-choice questions

1. 10,000 × 384 float32 components require raw vector storage of:

   - A. 15,360,000 bytes
   - B. 3,840 bytes
   - C. 384 MiB
   - D. Exactly the peak process memory

2. Which statement describes a safe rebuild?

   - A. Rewrite active files row by row
   - B. Ignore failed rows
   - C. Activate before validation
   - D. Build a validated immutable generation then switch

## Conceptual questions

1. Draw offline and online paths and explain why each request must see one coherent snapshot.
2. Estimate raw float32 vector storage and scoring work, then list the additional evidence needed before claiming a latency or peak-memory target.

## Practical assignment

Complete [the module lab](../labs/lab-07.md). Submit its worksheet, proposed tests, and the independent failure example. Code execution belongs to later learner work, not to material preparation.

## Debugging scenario

Attempt both lecture debugging scenarios. Identify the failure boundary, a reproducible minimal case, the expected safe behavior, and the test that would prevent regression.

## Review criteria

- Both multiple-choice answers correct and justified.
- Conceptual answers connect the mechanism to a concrete failure.
- Lab acceptance criteria and counterexample are reviewable.
- No invented model-quality, latency, or completion result.

[Solutions — open after attempting](../../../../../assessments/module-solutions.md).
