# Lecture 11 — LangChain components and provider boundaries

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L11 · Day 20 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: What does a retriever return?
- Explain and demonstrate: Why pin integration packages?
- Explain and demonstrate: Which rules remain outside a framework?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Use a framework to compose known behaviors, not to obscure them. Separate documents, text splitters, embeddings, vector stores, retrievers, prompt/message construction, model invocation, and output validation. A document carries text plus metadata; a retriever selects documents; a model generates a response. These abstractions are not interchangeable.

Integration packages and provider interfaces evolve. Use current component documentation and pin versions during the later implementation pass. Older tutorials can teach concepts while showing outdated imports or methods. Importing an agent helper is unnecessary for a deterministic retrieval-then-answer flow and would pull Phase 5 work forward.

Keep the application’s evidence and error contracts independent of any provider response object. A framework adapter still needs the Phase 2 embedding compatibility manifest and Phase 1 validation boundaries. Switching integrations is a behavioral migration requiring tests, not merely renaming an import.

## Practical example and walkthrough

The manual pipeline returns a list of evidence records. The framework retriever should preserve those records and metadata rather than collapse them into an unlabeled text string.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [LangChain Vector Store Integrations](https://docs.langchain.com/oss/python/integrations/vectorstores/index) — Official component guide, free to read; selected document objects and add/delete/search interface; 15 min study estimate. Explains the abstraction without hiding collection compatibility.
- [LangChain Retriever Integrations](https://docs.langchain.com/oss/python/integrations/retrievers/index) — Official component guide, free to read; selected retriever role and integration categories; 15 min study estimate. Distinguish retrieval behavior from storage and generation.

Optional supplements/fallbacks:

- [LangChain Models](https://docs.langchain.com/oss/python/langchain/models) — Official documentation, free to read; selected invocation and structured outputs; skip agents/tools; 15 min study estimate. Review provider boundaries without pulling agent loops forward.
- [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) — Publisher repository with linked video playlist, free to read; selected indexing, retrieval, and generation introductory notebooks/videos; 20 min study estimate. Optional conceptual/video fallback; review old notebook APIs against current component documentation.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Map each manual component to a LangChain component and identify the business rules that stay in application code. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-06.md) as the practical follow-through.

## Debugging scenario

A tutorial’s import no longer exists. How can you preserve the architecture while finding the current component API?

## Knowledge check

1. What does a retriever return?
2. Why pin integration packages?
3. Which rules remain outside a framework?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../../../section-02-manual-rag-chunking/modules/module-03-provenance-lifecycle/lectures/lecture-10-ingestion-versions-idempotency-refresh-and-deletion.md) · [Next](lecture-12-messages-invocation-output-contracts-and-test-doubles.md)
