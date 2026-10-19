# Lecture 13 — RAG with LangChain and Qdrant: integration contracts

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L13 · Day 21 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Which variables must remain fixed for parity?
- Explain and demonstrate: Why inspect payload mappings?
- Explain and demonstrate: Where should citation labels be assigned?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Rebuild the already-understood pipeline with a vector-store/retriever adapter while holding corpus, encoder revision, chunk policy, question set, and output contract fixed. This lets you attribute differences to integration behavior rather than a different dataset or model. A framework version is not automatically better RAG.

Check the integration’s payload schema. Direct Qdrant points and framework-created document records may put text and metadata under different keys. An adapter must configure or transform them explicitly. Do not point a wrapper at an existing collection and assume it will infer source-field names correctly.

Keep citation labels and context assembly in the application. Compare retrieved IDs/text/locators before comparing generated prose, and inspect filter pass-through. A successful framework call that drops version or provenance fields is a contract regression even when the answer looks fluent.

## Practical example and walkthrough

The direct index stores text at payload.text, while a wrapper expects page_content. The collection can be numerically valid but render empty documents until the adapter mapping is fixed.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [LangChain Qdrant Integration](https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant) — Official integration guide, free to read; selected qdrantvectorstore, local mode, and dense retrieval; 20 min study estimate. Map adapter behavior to the manual pipeline and preserve payload schema.

Optional supplements/fallbacks:

- [LangChain Vector Store Integrations](https://docs.langchain.com/oss/python/integrations/vectorstores/index) — Official component guide, free to read; selected document objects and add/delete/search interface; 15 min study estimate. Explains the abstraction without hiding collection compatibility.
- [LangChain Retriever Integrations](https://docs.langchain.com/oss/python/integrations/retrievers/index) — Official component guide, free to read; selected retriever role and integration categories; 15 min study estimate. Distinguish retrieval behavior from storage and generation.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Write a parity checklist comparing manual and framework retrieval on the same hand-vector fixtures. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-07.md) as the practical follow-through.

## Debugging scenario

Why can manual retrieval work while a framework returns blank document content from the same collection?

## Knowledge check

1. Which variables must remain fixed for parity?
2. Why inspect payload mappings?
3. Where should citation labels be assigned?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../module-01-components/lectures/lecture-12-messages-invocation-output-contracts-and-test-doubles.md) · [Next](lecture-14-pipeline-parity-failure-traces-and-layered-evaluation.md)
