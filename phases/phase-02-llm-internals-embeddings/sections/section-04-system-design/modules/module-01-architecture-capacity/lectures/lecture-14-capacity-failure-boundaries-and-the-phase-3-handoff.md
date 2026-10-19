# Lecture 14 — Capacity, failure boundaries, and the Phase 3 handoff

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L14 · Day 14 · Guided study: 25 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Estimate baseline storage and scoring work with explicit assumptions.
- Explain the point at which production retrieval requirements grow.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Estimate baseline storage and scoring work with explicit assumptions.
- Explain the point at which production retrieval requirements grow.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

Raw float32 storage for 10,000 vectors of dimension 384 is `10000*384*4 = 15360000` bytes, about 14.65 MiB. One exact query touches about 3.84 million vector components. Neither estimate predicts latency: hardware, memory access, encoding cost, sorting, batching, and process overhead still need measurement. Record assumptions beside every capacity calculation.

Bound text sizes, batch memory, query length, and k. Treat model-download failure, corrupt manifests, unavailable source files, zero vectors, invalid numeric values, and mismatched snapshots as distinct failure cases. Embeddings and search snippets inherit the sensitivity of their source documents. Deletion must remove the old text and derived artifacts, including retained snapshots under a stated policy.

Exact search gives an explainable baseline for later index-quality comparisons. Phase 3 adds document ingestion, chunking, vector databases, and RAG; Phase 4 adds stronger retrieval evaluation and isolation. Do not preempt these phases by implementing a distributed engine now. The current exercise should establish trustworthy contracts and measurements that make those later trade-offs intelligible.

## Practical example and walkthrough

A stakeholder asks whether a database is necessary at 10,000 short documents. Show the raw-vector estimate and measurement plan, then explain the missing requirements—concurrency, update frequency, filters, durability—before choosing infrastructure.

Design a capacity worksheet and failure table. State which evidence would justify replacing local exact search, and which evidence is still missing.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html) — Official performance guide; Batching and backend overview; advanced optimizations optional; 15 min selected study. Supports measured throughput decisions rather than assumed speedups.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Model Cards](https://huggingface.co/docs/hub/model-cards) — Official Hugging Face Hub documentation; Model-card metadata, intended uses, and limitations; 15 min selected study. Provides a checklist for model selection and licensing review.
- [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Official application guide; Symmetric/asymmetric search and exact search; 20 min selected study. Explains encode-query/document use without requiring a vector database.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Design a capacity worksheet and failure table. State which evidence would justify replacing local exact search, and which evidence is still missing. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-07.md).

## Debugging scenario

Why does a raw-vector-size estimate understate peak process memory?

## Knowledge check

1. How is float32 storage calculated?
2. Why is latency not derivable from storage alone?
3. Which capabilities belong to Phase 3?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](lecture-13-versioned-embedding-and-local-search-architecture.md) · [Next](../../../../../assessments/phase-02-assessment.md)
