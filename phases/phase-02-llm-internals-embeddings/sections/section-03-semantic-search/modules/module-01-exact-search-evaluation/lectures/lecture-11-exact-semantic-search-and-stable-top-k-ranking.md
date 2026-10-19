# Lecture 11 — Exact semantic search and stable top-k ranking

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L11 · Day 13 · Guided study: 30 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Design small-corpus brute-force retrieval.
- Preserve identity, metadata, ranking direction, and tie behavior.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Design small-corpus brute-force retrieval.
- Preserve identity, metadata, ranking direction, and tie behavior.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

For a small local corpus, exact search is a useful reference implementation: encode the query under the corpus manifest, calculate one score per document vector, and return the highest similarities or lowest distances. With normalized vectors and cosine scoring, a matrix-vector multiplication produces the scores. Stable secondary sorting by document ID makes equal-score cases predictable.

Query scoring costs approximately `O(N*d)` arithmetic and raw vector storage is `N*d*bytes_per_value`. Sorting all candidates costs `O(N log N)`; a later implementation may use a partial selection operation while preserving tie semantics. These estimates exclude model weights, metadata, temporary arrays, and loading costs.

Return document IDs, scores, snippets, and the snapshot/model versions. Never fabricate a generated answer or a citation. An empty corpus, invalid k, blank query, mismatched manifest, non-finite score, or unknown document ID must fail visibly. An optional relevance threshold must come from development evidence and should not be represented as a probability of correctness.

## Practical example and walkthrough

A query for cancelling a subscription returns three short policy documents and their scores. It does not write a new policy summary; that distinction keeps the Phase 2 milestone separate from RAG.

Given four normalized document vectors and one query, calculate scores, sort descending with document-ID ties, and check k larger than the corpus size under an explicit clamp-or-reject policy.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Official application guide; Symmetric/asymmetric search and exact search; 20 min selected study. Explains encode-query/document use without requiring a vector database.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [numpy.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html) — Official NumPy API; One-dimensional and matrix behavior; 10 min selected study. Confirms shape conventions for scoring.
- [Semantic Textual Similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html) — Official Sentence Transformers guide; Similarity metrics and normalization; 15 min selected study. Connects model output to the scoring metric.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Given four normalized document vectors and one query, calculate scores, sort descending with document-ID ties, and check k larger than the corpus size under an explicit clamp-or-reject policy. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-06.md).

## Debugging scenario

The right vector ranks first but the displayed snippet belongs to another document. Which invariant was broken?

## Knowledge check

1. What is the exact-search complexity?
2. Which way do cosine scores sort?
3. Why return snapshot metadata?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](../../../../section-02-embedding-engineering/modules/module-03-model-selection/lectures/lecture-10-controlled-comparisons-failure-slices-and-model-changes.md) · [Next](lecture-12-relevance-judgments-recall-k-mrr-and-honest-results.md)
