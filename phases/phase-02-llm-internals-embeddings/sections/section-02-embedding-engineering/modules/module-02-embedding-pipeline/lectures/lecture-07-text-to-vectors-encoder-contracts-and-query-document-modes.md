# Lecture 07 — Text to vectors: encoder contracts and query/document modes

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L07 · Day 11 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Define an embedding request/result contract.
- Match model, revision, prompts, and pooling across both sides of search.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Define an embedding request/result contract.
- Match model, revision, prompts, and pooling across both sides of search.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

An embedding pipeline accepts bounded text and returns a finite vector of the declared dimension together with enough metadata to reproduce it. A useful contract records model ID and revision, input policy, query/document role, output dtype, dimension, normalization, and preprocessing version. Model equality by display name is insufficient when an unpinned artifact changes.

Some retrieval encoders distinguish short queries from longer passages through prompts or task routing. Use the model’s documented query and document entry points. For models without role-specific behavior, these can be equivalent. Do not assume arbitrary “query:” prefixes improve every model. Mixing unrelated encoders in the same-dimensional space remains invalid.

Use a synthetic or licensed corpus. Embeddings can retain sensitive information and should be treated as derived data, not as anonymous hashes. A local baseline avoids sending text to a third-party embedding service, but model downloads still need provenance and license review. Credentials are unnecessary for a public local model when access remains ungated.

## Practical example and walkthrough

Two services both return 384-dimensional arrays but use different encoder revisions. Their shapes pass validation while their geometry is incompatible. A manifest mismatch should stop search before ranking.

Design EmbedRequest(texts, role) and EmbedResult(vectors, manifest). Trace one query and two documents through the same encoder family with role-specific settings.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [SentenceTransformer API](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html) — Official API reference; encode_query, encode_document, and encode parameters; 20 min selected study. Documents query/document modes and batch settings.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Model Cards](https://huggingface.co/docs/hub/model-cards) — Official Hugging Face Hub documentation; Model-card metadata, intended uses, and limitations; 15 min selected study. Provides a checklist for model selection and licensing review.
- [Download files from the Hub](https://huggingface.co/docs/huggingface_hub/guides/download) — Official Hub guide; Revision pinning and local cache; 10 min selected study. Supports reproducible artifacts and offline reruns.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Design EmbedRequest(texts, role) and EmbedResult(vectors, manifest). Trace one query and two documents through the same encoder family with role-specific settings. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-04.md).

## Debugging scenario

Search quality drops after only the query service updates its model. Which manifest fields should reveal the incompatibility?

## Knowledge check

1. Does equal dimensionality imply compatibility?
2. When do query/document prompts matter?
3. Which data can an embedding reveal?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](../../module-01-representations-geometry/lectures/lecture-06-cosine-dot-product-euclidean-distance-and-normalization.md) · [Next](lecture-08-batching-persistence-and-reproducible-embedding-artifacts.md)
