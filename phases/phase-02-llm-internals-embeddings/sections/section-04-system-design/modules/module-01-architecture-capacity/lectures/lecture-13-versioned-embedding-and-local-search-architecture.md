# Lecture 13 — Versioned embedding and local search architecture

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L13 · Day 14 · Guided study: 20 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Separate offline encoding from online search.
- Design artifact activation, validation, and query contracts.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Separate offline encoding from online search.
- Design artifact activation, validation, and query contracts.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

Separate the corpus build path from the query path. The build path validates document IDs and lengths, encodes documents, checks vectors, and writes an immutable snapshot. The query path loads an approved snapshot, checks the query contract, encodes the query compatibly, scores candidates, and renders retrieved documents. A service that re-encodes every document on every query wastes work and complicates reproducibility.

A manifest acts as a compatibility contract, not as authentication. It records model/revision, roles or prompts, dimension, normalization, dtype, preprocessing version, document count, and corpus hash. A snapshot digest binds metadata to the artifact set. Choose explicit validation and failure behavior rather than accepting a dimension match as sufficient.

The mandatory deliverable is local and single-user. If a future API is introduced, caller identity and data authorization precede scoring and rendering. Do not rely on removing unauthorized hits after top-k. Queueing, distributed vector storage, sharding, and high availability are design extensions introduced later in the course.

## Practical example and walkthrough

A scheduled corpus refresh finishes while a user is searching. Immutable generation IDs let the request finish against one coherent version while later requests use the new validated snapshot.

Draw offline and online paths, then mark the only point where a new snapshot becomes current. Trace a query during a failed rebuild.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [SentenceTransformer API](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html) — Official API reference; encode_query, encode_document, and encode parameters; 20 min selected study. Documents query/document modes and batch settings.
- [Download files from the Hub](https://huggingface.co/docs/huggingface_hub/guides/download) — Official Hub guide; Revision pinning and local cache; 10 min selected study. Supports reproducible artifacts and offline reruns.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Official application guide; Symmetric/asymmetric search and exact search; 20 min selected study. Explains encode-query/document use without requiring a vector database.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Draw offline and online paths, then mark the only point where a new snapshot becomes current. Trace a query during a failed rebuild. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-07.md).

## Debugging scenario

Why can independent query and corpus deployments break search without any HTTP or schema error?

## Knowledge check

1. Why separate build from query?
2. What belongs in a manifest?
3. What does a manifest not authorize?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](../../../../section-03-semantic-search/modules/module-01-exact-search-evaluation/lectures/lecture-12-relevance-judgments-recall-k-mrr-and-honest-results.md) · [Next](lecture-14-capacity-failure-boundaries-and-the-phase-3-handoff.md)
