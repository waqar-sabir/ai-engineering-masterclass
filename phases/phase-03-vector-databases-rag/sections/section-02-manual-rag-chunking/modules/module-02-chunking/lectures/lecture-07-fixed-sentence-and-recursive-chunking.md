# Lecture 07 — Fixed, sentence, and recursive chunking

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L07 · Day 18 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Which unit does len count?
- Explain and demonstrate: What trade-off follows smaller chunks?
- Explain and demonstrate: Why inspect final inputs after adding headings?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Chunking chooses the retrieval unit. Fixed-size windows are simple and reproducible but may split a definition from its exception. Sentence/paragraph boundaries preserve more structure but can produce uneven lengths. Recursive splitting tries larger boundaries before smaller ones; it is a heuristic, not a guarantee of ideal semantic units.

Name the size unit explicitly. A splitter using Python len counts characters, not model tokens. After splitting, check each final embedding input, including added heading or source context, against the selected encoder budget. A paragraph or table longer than the budget still needs a visible fallback or review status.

Compare chunk strategies on the same source and query labels. Shorter chunks may isolate precise answers while losing context; longer chunks may dilute relevance and consume prompt space. There is no universally correct chunk size independent of source structure, model, and task.

## Practical example and walkthrough

A rule and its exception occur in neighboring sentences. A fixed boundary separates them; inspect whether sentence grouping or modest overlap preserves the complete condition.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [LangChain Text Splitter Integrations](https://docs.langchain.com/oss/python/integrations/splitters/index) — Official integration guide, free to read; selected splitter families and unit choices; 15 min study estimate. Choose splitters from document structure rather than a universal size.
- [Splitting Recursively](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter) — Official tutorial, free to read; selected separators, chunk_size, overlap, and length_function; 20 min study estimate. Avoid confusing character length with token length.

Optional supplements/fallbacks:

- [Docling Document](https://docling-project.github.io/docling/concepts/docling_document/) — Official data-model guide, free to read; selected document items, hierarchy, and provenance; 20 min study estimate. Retain structure/locators rather than flattening every source into untraceable text.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Mark chunks for a two-paragraph policy with a heading, an exception, and a long sentence using three strategies. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-04.md) as the practical follow-through.

## Debugging scenario

A 500-character chunk exceeds the encoder token budget. Why was the nominal size insufficient?

## Knowledge check

1. Which unit does len count?
2. What trade-off follows smaller chunks?
3. Why inspect final inputs after adding headings?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../module-01-manual-rag/lectures/lecture-06-evidence-labels-citations-context-budgets-and-abstention.md) · [Next](lecture-08-overlap-token-limits-and-chunk-policy-experiments.md)
