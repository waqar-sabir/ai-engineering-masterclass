# Lecture 06 — Cosine, dot product, Euclidean distance, and normalization

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L06 · Day 10 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Calculate similarities by hand.
- Choose correct sorting and normalization policies.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Calculate similarities by hand.
- Choose correct sorting and normalization policies.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

For vectors `a` and `b`, dot product is the sum of coordinate-wise products. Euclidean distance is the square root of the sum of squared coordinate differences. Cosine is `dot(a,b) / (norm(a) * norm(b))`; it compares direction after scaling out magnitude. A zero vector has no cosine direction, so reject it or define a visible invalid-input policy.

For unit vectors, dot product equals cosine and squared Euclidean distance equals `2 - 2*cosine`. Therefore maximizing cosine and minimizing Euclidean distance give the same order under these normalization conditions, apart from ties and numerical effects. Without normalization, magnitudes can change rankings. Ascending distance and descending similarity are different conventions.

Check dimensions, non-finite numbers, zero norms, and batch axes before ranking. Similarity is not a calibrated probability; a score of 0.8 does not mean an 80 percent chance of correctness. A universal threshold reused across different encoders is unjustified. Define stable tie-breaking, such as document ID ascending, so repeated exact-search fixtures are reproducible.

## Practical example and walkthrough

For query `[1,0]`, documents `[1,0]`, `[3,0]`, and `[0,1]` give different raw dot products even though the first two point in the same direction. Normalization makes their cosine scores equal.

Calculate cosine for identical, perpendicular, and opposite unit vectors. Then show why raw dot ranking favors `[3,0]` over `[1,0]`.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [numpy.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html) — Official NumPy API; One-dimensional and matrix behavior; 10 min selected study. Confirms shape conventions for scoring.
- [numpy.linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html) — Official NumPy API; Vector norm and axis argument; 10 min selected study. Supports explicit normalization and zero-vector handling.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Semantic Textual Similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html) — Official Sentence Transformers guide; Similarity metrics and normalization; 15 min selected study. Connects model output to the scoring metric.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Calculate cosine for identical, perpendicular, and opposite unit vectors. Then show why raw dot ranking favors `[3,0]` over `[1,0]`. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-03.md).

## Debugging scenario

A developer sorts cosine scores ascending. What will the top hit represent?

## Knowledge check

1. When does dot product equal cosine?
2. What happens for a zero vector?
3. How does Euclidean sorting differ?
4. Why are cross-model score thresholds unsafe?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](lecture-05-token-sentence-and-document-embeddings.md) · [Next](../../module-02-embedding-pipeline/lectures/lecture-07-text-to-vectors-encoder-contracts-and-query-document-modes.md)
