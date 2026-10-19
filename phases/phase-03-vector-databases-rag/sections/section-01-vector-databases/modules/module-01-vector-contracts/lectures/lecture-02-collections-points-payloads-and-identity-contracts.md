# Lecture 02 — Collections, points, payloads, and identity contracts

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L02 · Day 15 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Which point ID forms are supported?
- Explain and demonstrate: Where should source provenance live?
- Explain and demonstrate: Why is deletion separate from upsert?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

A collection declares how its vectors are interpreted. Each point has a supported ID, its vector representation, and optional payload. Numeric dimensions belong to the schema; source path, document version, page, and chunk text belong to payload or a related metadata store. Payload indexes speed relevant field operations; they do not improve an incompatible embedding space.

Use deterministic IDs for repeatable ingestion. In Qdrant, supported point IDs include unsigned integers and UUIDs, so an arbitrary document string should remain payload unless mapped into a supported ID. A UUID derived from document version, parser/chunker version, and chunk position can be an application-level identity policy.

Decide whether a changed source creates a new version or replaces old points. Reusing IDs can prevent duplicate inserts, but it will not delete obsolete tail chunks when a document becomes shorter. Version activation and cleanup require their own explicit plan.

## Practical example and walkthrough

A document once had five chunks and now has three. Upserting the first three IDs alone leaves two stale points; an explicit version/deletion policy must remove them.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Points](https://qdrant.tech/documentation/manage-data/points/) — Official documentation, free to read; selected point ids, upsert, and retrieval; 20 min study estimate. Clarifies UUID/integer IDs and repeatable writes.
- [Qdrant Payload](https://qdrant.tech/documentation/manage-data/payload/) — Official documentation, free to read; selected json payload and data types; 15 min study estimate. Preserve source and chunk identity separately from vector coordinates.

Optional supplements/fallbacks:

- [Qdrant Collections](https://qdrant.tech/documentation/manage-data/collections/) — Official documentation, free to read; selected collection vector schema and configuration; 15 min study estimate. Define dimension and distance before insertion.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Design a minimal vector schema and payload contract with stable document, version, and locator fields. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-01.md) as the practical follow-through.

## Debugging scenario

Why does a successful upsert not guarantee old source versions disappeared?

## Knowledge check

1. Which point ID forms are supported?
2. Where should source provenance live?
3. Why is deletion separate from upsert?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-01-vector-database-concepts-and-the-exact-search-reference.md) · [Next](../../module-02-qdrant-lifecycle/lectures/lecture-03-qdrant-setup-and-controlled-collection-lifecycle.md)
