# Lecture 17 — Query rewriting and metadata filtering: controlled introduction

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L17 · Day 23 · Guided notes/example: 30 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Why retain the original query?
- Explain and demonstrate: How do filters differ from semantic scores?
- Explain and demonstrate: Why is user-supplied scope not authorization?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

A query rewrite can clarify wording or decompose a question, but it can also invent intent, erase identifiers, or omit constraints. Preserve the original question, log the transformation version, and compare retrieval against the unrevised baseline. The source wording remains the authority for what the user asked.

Metadata filters constrain eligible documents by known fields such as category, source type, or version. A filter is not the same as a keyword similarity feature. Pass structured conditions through the retrieval interface and test missing fields/types explicitly. A public local corpus can use these constraints for relevance; production authorization must derive policy from a trusted caller, not arbitrary query-supplied tenant IDs.

Day 23 introduces these mechanisms with a small controlled exercise. Full query-transformation evaluation, advanced filtering strategies, and secure multi-tenant retrieval are Phase 4 work. Keep one change at a time so a local improvement can be attributed correctly.

## Practical example and walkthrough

The question includes SKU-401. A rewrite substitutes a generic product category and loses the exact identifier. Compare both retrieval traces and retain the original constraint.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Filtering](https://qdrant.tech/documentation/search/filtering/) — Official documentation, free to read; selected must/should/must-not and field conditions; 15 min study estimate. Makes metadata constraints explicit and testable.

Optional supplements/fallbacks:

- [LangChain Retriever Integrations](https://docs.langchain.com/oss/python/integrations/retrievers/index) — Official component guide, free to read; selected retriever role and integration categories; 15 min study estimate. Distinguish retrieval behavior from storage and generation.
- [Qdrant Hybrid and Multi-Stage Queries](https://qdrant.tech/documentation/search/hybrid-queries/) — Official documentation, free to read; selected prefetch and reciprocal-rank fusion overview; 20 min study estimate. Day 23 orientation; implementation/deeper tuning belongs to Phase 4.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Prepare original/rewritten query pairs and a category filter with explicit expected eligible IDs. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-09.md) as the practical follow-through.

## Debugging scenario

A metadata filter removes every relevant chunk. Which fields and assumptions should be inspected before changing the embedding model?

## Knowledge check

1. Why retain the original query?
2. How do filters differ from semantic scores?
3. Why is user-supplied scope not authorization?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../module-01-docling-formats/lectures/lecture-16-structure-tables-reading-order-and-parsing-quality-checks.md) · [Next](lecture-18-hybrid-retrieval-rank-fusion-and-reranking-controlled-introduction.md)
