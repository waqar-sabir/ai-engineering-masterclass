# Module 2.1.1 assessment

[Module home](../README.md) · [Phase home](../../../../../README.md)

Material status: Approved. Learner submission: Planned. This is formative; no learner score is recorded.

## Multiple-choice questions

1. Which step normally changes model weights?

   - A. Adding a user message
   - B. Training with parameter updates
   - C. Rendering a response
   - D. Writing a JSON log

2. A tokenizer limit guarantees the embedding wrapper accepts equally long input.

   - A. Always true
   - B. Only on a GPU
   - C. False; check the actual encoder configuration
   - D. True if IDs are integers

## Conceptual questions

1. Explain why a prompt can change an answer without changing weights. Distinguish model parameters, input context, activations, and application memory.
2. Given an important sentence near the end of a long document, specify how you would detect and prevent silent encoder truncation.

## Practical assignment

Complete [the module lab](../labs/lab-01.md). Submit its worksheet, proposed tests, and the independent failure example. Code execution belongs to later learner work, not to material preparation.

## Debugging scenario

Attempt both lecture debugging scenarios. Identify the failure boundary, a reproducible minimal case, the expected safe behavior, and the test that would prevent regression.

## Review criteria

- Both multiple-choice answers correct and justified.
- Conceptual answers connect the mechanism to a concrete failure.
- Lab acceptance criteria and counterexample are reviewable.
- No invented model-quality, latency, or completion result.

[Solutions — open after attempting](../../../../../assessments/module-solutions.md).
