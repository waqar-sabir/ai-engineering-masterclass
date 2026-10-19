# Lecture 04 — Upsert, query, payload return, and reproducible search

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L04 · Day 16 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Why request payload explicitly?
- Explain and demonstrate: What does exact search help validate?
- Explain and demonstrate: Why is corpus activation broader than an upsert?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Plan insertion as bounded batches with deterministic point IDs and source-version metadata. Track attempted and accepted records; retry only operations whose application semantics remain safe. Idempotent point replacement does not by itself provide atomic activation of an entire multi-batch corpus.

Use the current query interface and explicitly request the payload needed for source display. Inspect result IDs, scores, and metadata before generating prose. Compare exact-query mode with Phase 2 hand-vector expectations, allowing documented floating-point and tie differences. Never treat an undocumented score scale as a confidence probability.

Validate vector length, finite values, collection identity, filter policy, and returned source IDs. A missing payload should not be repaired by inventing a title or page. A query to an empty collection and a query that cannot find relevant evidence need distinguishable review outcomes.

## Practical example and walkthrough

A query returns the correct point but payload is omitted. The retrieval trace is incomplete; do not fabricate a citation from an assumed file order.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Points](https://qdrant.tech/documentation/manage-data/points/) — Official documentation, free to read; selected point ids, upsert, and retrieval; 20 min study estimate. Clarifies UUID/integer IDs and repeatable writes.
- [Qdrant Search](https://qdrant.tech/documentation/search/search/) — Official documentation, free to read; selected query api, payload return, and exact search; 20 min study estimate. Compare returned candidates with the Phase 2 exact baseline.

Optional supplements/fallbacks:

- [Qdrant Payload](https://qdrant.tech/documentation/manage-data/payload/) — Official documentation, free to read; selected json payload and data types; 15 min study estimate. Preserve source and chunk identity separately from vector coordinates.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Specify a three-point insert/query/delete smoke test and expected document IDs using toy vectors. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-02.md) as the practical follow-through.

## Debugging scenario

Counts increase on every ingestion rerun. Which ID and versioning decisions should be audited?

## Knowledge check

1. Why request payload explicitly?
2. What does exact search help validate?
3. Why is corpus activation broader than an upsert?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-03-qdrant-setup-and-controlled-collection-lifecycle.md) · [Next](../../../../section-02-manual-rag-chunking/modules/module-01-manual-rag/lectures/lecture-05-manual-rag-retrieval-context-assembly-and-generation.md)
