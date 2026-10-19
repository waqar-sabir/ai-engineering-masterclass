# Lecture 08 — Overlap, token limits, and chunk-policy experiments

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L08 · Day 18 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: What happens as overlap approaches size?
- Explain and demonstrate: When do chunk IDs need a new version?
- Explain and demonstrate: How should duplicate evidence be treated?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Overlap repeats part of a source across neighboring chunks to reduce boundary loss. It also increases storage, embedding work, duplicate hits, and repeated prompt tokens. Require overlap smaller than chunk size and count unique evidence coverage rather than treating repeated windows as independent support.

For a long sequence of L units, size c, and overlap o, a simple sliding-window estimate is roughly one plus the ceiling of max(0,L-c)/(c-o). Actual recursive boundaries change counts. If c=200 and o=40, the long-document duplication factor approaches 200/160=1.25, not a measured total-system overhead.

Version the chunk policy, including boundaries, length unit, normalization, heading context, and final token validation. A policy change requires re-encoding and updated chunk identity. Compare alternatives on development evidence first; preserve held-out queries for an honest final report.

## Practical example and walkthrough

A query returns five overlapping chunks covering one sentence. The apparent five-source agreement is one repeated passage, not five independent documents.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Splitting Recursively](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter) — Official tutorial, free to read; selected separators, chunk_size, overlap, and length_function; 20 min study estimate. Avoid confusing character length with token length.

Optional supplements/fallbacks:

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — Original research paper, free to read; selected abstract and reported position effects; 15 min study estimate. Motivates context inspection; not a claim about every current model.
- [LangChain Text Splitter Integrations](https://docs.langchain.com/oss/python/integrations/splitters/index) — Official integration guide, free to read; selected splitter families and unit choices; 15 min study estimate. Choose splitters from document structure rather than a universal size.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Calculate estimated window counts for L=1000, c=200, o=40 and contrast with no overlap; then inspect boundary quality. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-04.md) as the practical follow-through.

## Debugging scenario

Why can increasing overlap make generation worse even if retrieval coverage improves?

## Knowledge check

1. What happens as overlap approaches size?
2. When do chunk IDs need a new version?
3. How should duplicate evidence be treated?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-07-fixed-sentence-and-recursive-chunking.md) · [Next](../../module-03-provenance-lifecycle/lectures/lecture-09-metadata-provenance-and-document-hierarchy.md)
