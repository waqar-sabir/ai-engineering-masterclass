# Lecture 18 — Hybrid retrieval, rank fusion, and reranking: controlled introduction

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L18 · Day 23 · Guided notes/example: 30 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Why avoid raw-score addition?
- Explain and demonstrate: What inputs does fusion require?
- Explain and demonstrate: What can a reranker not recover?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Dense retrieval compares learned representations; a sparse/lexical retriever emphasizes matching terms under its scoring model. Combining them can help when semantic paraphrases and exact identifiers both matter, but their raw scores are not necessarily comparable. Rank-based fusion is one way to combine candidate orderings without pretending score scales match.

Reciprocal-rank fusion gives a document a contribution like `1/(c+rank)` from each ranked list, using an explicitly chosen constant c and a missing-item policy. This is an algorithmic example, not a universal optimal setting. Candidate deduplication and stable identity are prerequisites to meaningful fusion.

A reranker rescans a candidate set against the query; it cannot retrieve a relevant item absent from that set. Reranking adds latency and may still misjudge evidence. Day 23 requires a hand-worked comparison and experiment plan; complete hybrid/reranker implementations and tuning are deferred to Phase 4. No advanced score improvement is claimed.

## Practical example and walkthrough

Dense ranks [a,b,c] and lexical ranks [d,b,a] share b and a. With c=60, b contributes 1/62 twice; compare total contributions before deciding the fused order.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Hybrid and Multi-Stage Queries](https://qdrant.tech/documentation/search/hybrid-queries/) — Official documentation, free to read; selected prefetch and reciprocal-rank fusion overview; 20 min study estimate. Day 23 orientation; implementation/deeper tuning belongs to Phase 4.
- [Qdrant Hybrid Search with Reranking](https://qdrant.tech/documentation/tutorials-basics/reranking-hybrid-search/) — Official tutorial, free to read; selected candidate retrieval vs reranking roles; 20 min study estimate. Shows the ordering of stages; optional extension rather than baseline requirement.

Optional supplements/fallbacks:

- [Qdrant Search](https://qdrant.tech/documentation/search/search/) — Official documentation, free to read; selected query api, payload return, and exact search; 20 min study estimate. Compare returned candidates with the Phase 2 exact baseline.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Compute a toy fused ranking and show a relevant document outside both candidate lists that reranking cannot recover. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-09.md) as the practical follow-through.

## Debugging scenario

A reranker fails to return a missing policy passage. Why can more reranking compute not fix absent candidates?

## Knowledge check

1. Why avoid raw-score addition?
2. What inputs does fusion require?
3. What can a reranker not recover?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-17-query-rewriting-and-metadata-filtering-controlled-introduction.md) · [Next](../../../../section-05-system-design-project/modules/module-01-architecture/lectures/lecture-19-enterprise-knowledge-architecture-and-ingestion-boundaries.md)
