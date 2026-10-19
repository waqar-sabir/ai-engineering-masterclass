# Lecture 03 — Qdrant setup and controlled collection lifecycle

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L03 · Day 16 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Why inspect an existing collection?
- Explain and demonstrate: What does local mode not benchmark?
- Explain and demonstrate: Which schema settings must match the encoder?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Start with a client-local in-memory or persistent sandbox for contract exercises; a server/container can be a later optional parity check. Record which mode was used. Local-mode behavior, concurrency, durability, and performance cannot be assumed identical to a deployed server. Exposing a development server publicly adds authentication and network obligations.

Create a collection with a dimension and distance compatible with the Phase 2 encoder manifest. Avoid destructive recreate helpers in ordinary runs. If a collection exists, inspect its schema and either reuse it under a compatible contract or choose a new versioned collection. Changing a model should not silently reinterpret old vectors.

A planned smoke test creates an isolated collection, inserts a few deterministic points, queries, inspects returned payloads, and reopens persistent state if that mode is chosen. Cleanup is limited to the learner-owned sandbox, never a shared collection.

## Practical example and walkthrough

A second run finds a collection with the same name but the wrong vector width. Fail visibly instead of deleting it or padding vectors.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Local Quickstart](https://qdrant.tech/documentation/quickstart/) — Official tutorial, free to read; selected local setup, collection, insert, and query; 20 min study estimate. A small local exercise before infrastructure tuning.
- [Qdrant Collections](https://qdrant.tech/documentation/manage-data/collections/) — Official documentation, free to read; selected collection vector schema and configuration; 15 min study estimate. Define dimension and distance before insertion.

Optional supplements/fallbacks:

- [LangChain Qdrant Integration](https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant) — Official integration guide, free to read; selected qdrantvectorstore, local mode, and dense retrieval; 20 min study estimate. Map adapter behavior to the manual pipeline and preserve payload schema.
- [Qdrant Essentials Course](https://qdrant.tech/course/essentials/) — Publisher video-first course, free to read; selected selected collection/search lessons only; 20 min study estimate. Optional video alternative; full course is outside the phase timebox.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Write a setup checklist distinguishing client-local, local server, and managed service modes. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-02.md) as the practical follow-through.

## Debugging scenario

An example recreates a collection on every run. Which data-loss risk does this introduce?

## Knowledge check

1. Why inspect an existing collection?
2. What does local mode not benchmark?
3. Which schema settings must match the encoder?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../module-01-vector-contracts/lectures/lecture-02-collections-points-payloads-and-identity-contracts.md) · [Next](lecture-04-upsert-query-payload-return-and-reproducible-search.md)
