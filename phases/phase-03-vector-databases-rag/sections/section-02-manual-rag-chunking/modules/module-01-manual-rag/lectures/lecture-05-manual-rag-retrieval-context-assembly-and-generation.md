# Lecture 05 — Manual RAG: retrieval, context assembly, and generation

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L05 · Day 17 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: How does RAG differ from semantic search?
- Explain and demonstrate: Why start without a framework?
- Explain and demonstrate: What can fake-provider tests establish?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

A basic application RAG pipeline retrieves candidate source passages, assembles bounded context, and asks a model to answer using that context. Keep each stage observable. Retrieval is a candidate-selection operation; generation is probabilistic output under instructions and supplied evidence. Neither stage proves that every resulting statement is supported.

Implement the conceptual flow manually before using a framework: validate question, embed, query the compatible collection, select evidence, label passages, build a prompt, generate, validate output, and render citations. A fake generator can test orchestration and refusal/error paths without a provider call. It cannot demonstrate model grounding quality.

When there is no adequate evidence, return an explicit insufficient-evidence result rather than asking the model to fill gaps. The corpus is bounded and versioned; a RAG answer is not a fresh web search or exhaustive company investigation.

## Practical example and walkthrough

A question asks about refunds, but retrieved chunks only describe billing dates. A valid JSON answer asserting a refund entitlement still fails evidence review.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — Original research paper, free to read; selected abstract and retrieval/generation architecture; 20 min study estimate. Historical conceptual grounding; the course uses an application pipeline, not training the paper’s model.
- [Qdrant Search](https://qdrant.tech/documentation/search/search/) — Official documentation, free to read; selected query api, payload return, and exact search; 20 min study estimate. Compare returned candidates with the Phase 2 exact baseline.

Optional supplements/fallbacks:

- [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) — Publisher repository with linked video playlist, free to read; selected indexing, retrieval, and generation introductory notebooks/videos; 20 min study estimate. Optional conceptual/video fallback; review old notebook APIs against current component documentation.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Draw the manual pipeline and define the input/output contract at each boundary. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-03.md) as the practical follow-through.

## Debugging scenario

The generator invents an answer when retrieval is empty. Which deterministic gate can stop this path?

## Knowledge check

1. How does RAG differ from semantic search?
2. Why start without a framework?
3. What can fake-provider tests establish?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../../../section-01-vector-databases/modules/module-02-qdrant-lifecycle/lectures/lecture-04-upsert-query-payload-return-and-reproducible-search.md) · [Next](lecture-06-evidence-labels-citations-context-budgets-and-abstention.md)
