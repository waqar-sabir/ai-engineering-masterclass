# Lecture 10 — Ingestion versions, idempotency, refresh, and deletion

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L10 · Day 19 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Why separate write from activation?
- Explain and demonstrate: What invalidates a cached embedding?
- Explain and demonstrate: Which derived artifacts need deletion?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

An ingestion run has stages: discover an approved source, compute its version, parse, normalize, split, encode, write, validate, and activate. Record success or failure per source. An unchanged input with the same parser/chunker/encoder contract should be safely reusable; a new policy or source version needs a coherent rebuild.

Idempotency means repeated work has the intended final effect. Deterministic point IDs prevent simple duplicates but do not clean stale chunks, coordinate multiple files, or guarantee that partial writes stay invisible. For the small course project, build a fresh versioned collection or generation and switch only after checks pass.

Deletion must remove or deactivate source text and derived chunks, vectors, caches, and retained versions under a stated retention policy. A deletion flag in metadata is not enough if queries ignore it. Review counts and source mapping after refresh, and keep a rollback path that respects deletion obligations.

## Practical example and walkthrough

A revised guide shrinks from eight chunks to five. The new generation contains exactly the five active chunks; old versions cannot leak through a forgotten collection name.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Points](https://qdrant.tech/documentation/manage-data/points/) — Official documentation, free to read; selected point ids, upsert, and retrieval; 20 min study estimate. Clarifies UUID/integer IDs and repeatable writes.
- [Qdrant Collections](https://qdrant.tech/documentation/manage-data/collections/) — Official documentation, free to read; selected collection vector schema and configuration; 15 min study estimate. Define dimension and distance before insertion.

Optional supplements/fallbacks:

- [Qdrant Payload](https://qdrant.tech/documentation/manage-data/payload/) — Official documentation, free to read; selected json payload and data types; 15 min study estimate. Preserve source and chunk identity separately from vector coordinates.
- [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — Official security guidance, free to read; selected indirect prompt injection and layered controls; 20 min study estimate. Supports a clear trust boundary; delimiters alone do not establish security.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Write a state machine for source discovered, parsed, indexed, failed, and active, plus an explicit deleted state. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-05.md) as the practical follow-through.

## Debugging scenario

A retry after partial ingestion doubles chunks. Which operations were not actually idempotent?

## Knowledge check

1. Why separate write from activation?
2. What invalidates a cached embedding?
3. Which derived artifacts need deletion?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-09-metadata-provenance-and-document-hierarchy.md) · [Next](../../../../section-03-langchain-rag/modules/module-01-components/lectures/lecture-11-langchain-components-and-provider-boundaries.md)
