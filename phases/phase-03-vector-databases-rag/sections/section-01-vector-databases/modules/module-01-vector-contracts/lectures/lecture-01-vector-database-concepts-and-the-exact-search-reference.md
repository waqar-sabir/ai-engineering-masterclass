# Lecture 01 — Vector database concepts and the exact-search reference

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L01 · Day 15 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: How do ANN recall and relevance recall differ?
- Explain and demonstrate: Which Phase 2 contract must remain unchanged?
- Explain and demonstrate: What does a vector database not verify?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Review the approved Phase 2 exact-search material; no completed implementation is assumed during material preparation.

## Core learning material

A vector database stores records whose numeric representations support nearest-neighbor queries, often alongside structured metadata. Keep the embedding function, vector schema, distance measure, and source identity distinct. The database does not make incompatible embeddings compatible, decide whether text is true, or generate an answer.

Phase 2’s exact search is a correctness reference. An approximate index trades search effort for candidate recall under a workload; it is not a different definition of relevance. Distinguish ANN recall against exact neighbors from relevance recall against human labels. A retriever can closely reproduce exact vector neighbors while still returning the wrong policy document.

Use small synthetic records first. Inspect IDs, vectors, payloads, and scores independently before adding model generation. A database operation succeeding proves that a request was accepted under its contract, not that a downstream answer is useful.

## Practical example and walkthrough

Compare an exact top-three list with an approximate list: two overlapping IDs yields neighbor-overlap recall 2/3. This says nothing yet about whether those IDs answer the user’s question.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Collections](https://qdrant.tech/documentation/manage-data/collections/) — Official documentation, free to read; selected collection vector schema and configuration; 15 min study estimate. Define dimension and distance before insertion.
- [Qdrant Indexing](https://qdrant.tech/documentation/manage-data/indexing/) — Official documentation, free to read; selected vector vs payload indexes; 15 min study estimate. Separate fast candidate search from metadata lookup requirements.

Optional supplements/fallbacks:

- [Qdrant Search](https://qdrant.tech/documentation/search/search/) — Official documentation, free to read; selected query api, payload return, and exact search; 20 min study estimate. Compare returned candidates with the Phase 2 exact baseline.
- [Qdrant Essentials Course](https://qdrant.tech/course/essentials/) — Publisher video-first course, free to read; selected selected collection/search lessons only; 20 min study estimate. Optional video alternative; full course is outside the phase timebox.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Define point, vector, payload, collection, distance, and index in a short architecture sketch. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-01.md) as the practical follow-through.

## Debugging scenario

Search has perfect ANN recall but poor answers. Which layer should be examined next?

## Knowledge check

1. How do ANN recall and relevance recall differ?
2. Which Phase 2 contract must remain unchanged?
3. What does a vector database not verify?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../../../../../phase-02-llm-internals-embeddings/README.md) · [Next](lecture-02-collections-points-payloads-and-identity-contracts.md)
