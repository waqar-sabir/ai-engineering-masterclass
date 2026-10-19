# Lecture 08 — Batching, persistence, and reproducible embedding artifacts

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L08 · Day 11 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Preserve document/vector alignment through batching.
- Design validated, restartable local artifacts.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Preserve document/vector alignment through batching.
- Design validated, restartable local artifacts.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

Corpus encoding is offline work that can be reused for many queries. Batch size trades memory pressure against throughput; it must be measured on the actual hardware and text lengths. Keep each vector aligned with a stable document ID regardless of batch boundaries, failures, or sorting. A shuffled vector matrix paired with the old document list creates plausible but incorrect results.

Persist an immutable snapshot: document records, an `[N,d]` vector matrix, and a manifest containing the corpus digest and embedding contract. Write into a temporary generation, validate row counts and dimensions, then make that generation current. Never expose a half-written snapshot as a successful build. Rebuilds are safer than silently mixing old and new vectors.

Use JSON for metadata and a numeric array format with object/pickle loading disabled when later implementing it. Record encoding time separately from query time and model loading. Cache only when input hash, model revision, role, and preprocessing contract all match. A cache hit is not evidence that the source text is current.

## Practical example and walkthrough

An interrupted build leaves documents.json with 40 entries and vectors.npy with 39 rows. Startup must fail clearly instead of returning the neighboring row’s text as a search result.

Sketch snapshot creation, validation, and activation. Design a test that deliberately swaps two document rows while leaving vector rows unchanged.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html) — Official performance guide; Batching and backend overview; advanced optimizations optional; 15 min selected study. Supports measured throughput decisions rather than assumed speedups.
- [Download files from the Hub](https://huggingface.co/docs/huggingface_hub/guides/download) — Official Hub guide; Revision pinning and local cache; 10 min selected study. Supports reproducible artifacts and offline reruns.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [SentenceTransformer API](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html) — Official API reference; encode_query, encode_document, and encode parameters; 20 min selected study. Documents query/document modes and batch settings.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Sketch snapshot creation, validation, and activation. Design a test that deliberately swaps two document rows while leaving vector rows unchanged. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-04.md).

## Debugging scenario

Why can a successful file write still leave an unusable search artifact?

## Knowledge check

1. Which IDs must survive batching?
2. What makes a cache key safe?
3. When should a snapshot become visible?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](lecture-07-text-to-vectors-encoder-contracts-and-query-document-modes.md) · [Next](../../module-03-model-selection/lectures/lecture-09-embedding-model-selection-and-practical-constraints.md)
