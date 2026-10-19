# Lecture 19 — Enterprise knowledge architecture and ingestion boundaries

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L19 · Day 24 · Guided notes/example: 20 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: What should be versioned end to end?
- Explain and demonstrate: Which enterprise controls are outside the local MVP?
- Explain and demonstrate: Why separate ingestion and serving?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Separate ingestion from query serving. Ingestion validates sources, parses, normalizes, splits, encodes, writes a candidate generation, and validates provenance/counts before activation. Query serving validates the question, selects one active compatible generation, retrieves evidence, assembles bounded context, calls the generator, validates citations, and renders source locators.

The mandatory project is a local single-user knowledge assistant, despite its roadmap title “Enterprise Knowledge Assistant.” Production multi-tenancy, authorization, deployment, high availability, and compliance guarantees are not implemented or asserted. The architecture should identify where those controls would belong before exposing any shared service.

Version each boundary and classify failures. A failed source cannot be indexed as successful empty text; a failed generation cannot become an uncited answer. Ingestion status, corpus generation, and evidence trace let reviewers distinguish stale data from parsing, retrieval, and generation faults.

## Practical example and walkthrough

During an interrupted rebuild, current queries use the prior complete generation. A new generation becomes visible only after source completeness and retrieval smoke checks succeed.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Collections](https://qdrant.tech/documentation/manage-data/collections/) — Official documentation, free to read; selected collection vector schema and configuration; 15 min study estimate. Define dimension and distance before insertion.
- [Docling Document](https://docling-project.github.io/docling/concepts/docling_document/) — Official data-model guide, free to read; selected document items, hierarchy, and provenance; 20 min study estimate. Retain structure/locators rather than flattening every source into untraceable text.

Optional supplements/fallbacks:

- [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — Official security guidance, free to read; selected indirect prompt injection and layered controls; 20 min study estimate. Supports a clear trust boundary; delimiters alone do not establish security.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Draw the ingestion and query paths, activation boundary, citation mapping, and per-stage error routes. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-10.md) as the practical follow-through.

## Debugging scenario

Why must a partial source conversion not silently count as successful corpus activation?

## Knowledge check

1. What should be versioned end to end?
2. Which enterprise controls are outside the local MVP?
3. Why separate ingestion and serving?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../../../section-04-document-parsing-retrieval/modules/module-02-retrieval-orientation/lectures/lecture-18-hybrid-retrieval-rank-fusion-and-reranking-controlled-introduction.md) · [Next](lecture-20-capacity-evaluation-failure-recovery-and-the-phase-4-handoff.md)
