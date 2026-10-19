# Lecture 14 — Pipeline parity, failure traces, and layered evaluation

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L14 · Day 21 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: What belongs in a stage trace?
- Explain and demonstrate: Why compare evidence before prose?
- Explain and demonstrate: Can retrieval recall prove answer grounding?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

A RAG failure can start in parsing, chunking, encoding, retrieval, context assembly, generation, or citation rendering. Capture an evidence trace so these stages can be inspected separately. The trace should identify the corpus and source versions, selected chunks/scores, prompt/schema versions, and stage durations without leaking private document bodies by default.

Compare manual and framework paths first with fake deterministic outputs and exact retrieval. Equal final wording is not the primary invariant; identity, evidence coverage, error semantics, and output contract matter. Later real-model comparisons need a frozen evaluation set and documented generation settings.

Distinguish retrieval metrics from answer-support metrics. A relevant chunk retrieved at rank one can still be omitted from context due to a bug, or misinterpreted by the model. Avoid reporting one end-to-end score as proof that every subsystem works.

## Practical example and walkthrough

Both paths retrieve the right refund policy, but one formatter truncates the exception before generation. The retriever metric stays high while answer correctness falls.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [LangChain Qdrant Integration](https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant) — Official integration guide, free to read; selected qdrantvectorstore, local mode, and dense retrieval; 20 min study estimate. Map adapter behavior to the manual pipeline and preserve payload schema.
- [LangChain Models](https://docs.langchain.com/oss/python/langchain/models) — Official documentation, free to read; selected invocation and structured outputs; skip agents/tools; 15 min study estimate. Review provider boundaries without pulling agent loops forward.

Optional supplements/fallbacks:

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — Original research paper, free to read; selected abstract and reported position effects; 15 min study estimate. Motivates context inspection; not a claim about every current model.
- [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) — Publisher repository with linked video playlist, free to read; selected indexing, retrieval, and generation introductory notebooks/videos; 20 min study estimate. Optional conceptual/video fallback; review old notebook APIs against current component documentation.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Design one failure fixture for each stage and identify the earliest observable evidence of the problem. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-07.md) as the practical follow-through.

## Debugging scenario

A final answer regresses after a prompt-budget change. Why should retrieval not be blamed first?

## Knowledge check

1. What belongs in a stage trace?
2. Why compare evidence before prose?
3. Can retrieval recall prove answer grounding?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-13-rag-with-langchain-and-qdrant-integration-contracts.md) · [Next](../../../../section-04-document-parsing-retrieval/modules/module-01-docling-formats/lectures/lecture-15-document-parsing-with-docling-and-format-specific-adapters.md)
