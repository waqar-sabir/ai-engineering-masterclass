# Module 2.1.2 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: Approved. Learner submission: Planned. This is formative; no learner score is recorded.

## Multiple-choice questions

1. For Q shaped [2,3] and K shaped [4,3], QKᵀ has shape:

   - A. [2,4]
   - B. [3,3]
   - C. [4,2]
   - D. [2,3]

2. What should a causal mask prevent?

   - A. All padding everywhere
   - B. A position reading future token positions
   - C. Weight updates
   - D. Similar documents ranking together

## Conceptual questions

1. Trace dimensions through a learned projection and QK-transpose. Identify what each remaining axis represents.
2. Explain causal vs padding masks and why a correct attention mechanism still needs positions, residual paths, normalization, and feed-forward layers.

## Practical assignment

Complete [the module lab](../labs/lab-02.md). Submit its worksheet, proposed tests, and the independent failure example. Code execution belongs to later learner work, not to material preparation.

## Debugging scenario

Attempt both lecture debugging scenarios. Identify the failure boundary, a reproducible minimal case, the expected safe behavior, and the test that would prevent regression.

## Review criteria

- Both multiple-choice answers correct and justified.
- Conceptual answers connect the mechanism to a concrete failure.
- Lab acceptance criteria and counterexample are reviewable.
- No invented model-quality, latency, or completion result.

[Solutions — open after attempting](../../../../../assessments/module-solutions.md).
