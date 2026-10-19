# Lecture 20 — Capacity, evaluation, failure recovery, and the Phase 4 handoff

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L20 · Day 24 · Guided notes/example: 20 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: What does raw vector storage omit?
- Explain and demonstrate: Why separate stage-level evaluation?
- Explain and demonstrate: What belongs in Phase 4 rather than this MVP?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Estimate capacity from chunks, not just files. If 100 documents yield 20 chunks each at dimension 384 float32, raw vectors occupy 2000*384*4 = 3,072,000 bytes, about 2.93 MiB. Payload text, indexes, models, temporary batches, and duplicate generations are additional. Overlap changes chunk count and prompt duplication; it is not free context.

Evaluate parsing fidelity, retrieval coverage, answer support, citation integrity, and insufficient-evidence behavior separately. An answerable question with no useful retrieved evidence is a failure case to preserve, while a question outside the corpus should visibly abstain. Freeze queries before final evaluation and record small-sample limitations.

Phase 4 deepens retrieval metrics, reranking, query transformations, tenant filtering, and RAG security. Carry forward a reproducible manual/framework baseline and failure evidence rather than introducing all production machinery now. Material approval is not evidence that the planned implementation, model quality, or service targets have been achieved.

## Practical example and walkthrough

A five-chunk answer budget consumes 5*180=900 source tokens before labels and question text. Compare that with the actual generator limit and keep the embedding model’s input budget separate.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — Original research paper, free to read; selected abstract and reported position effects; 15 min study estimate. Motivates context inspection; not a claim about every current model.
- [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — Official security guidance, free to read; selected indirect prompt injection and layered controls; 20 min study estimate. Supports a clear trust boundary; delimiters alone do not establish security.

Optional supplements/fallbacks:

- [Qdrant Indexing](https://qdrant.tech/documentation/manage-data/indexing/) — Official documentation, free to read; selected vector vs payload indexes; 15 min study estimate. Separate fast candidate search from metadata lookup requirements.
- [Qdrant Hybrid Search with Reranking](https://qdrant.tech/documentation/tutorials-basics/reranking-hybrid-search/) — Official tutorial, free to read; selected candidate retrieval vs reranking roles; 20 min study estimate. Shows the ordering of stages; optional extension rather than baseline requirement.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Write a capacity worksheet and a five-stage evaluation matrix; leave measured values blank until execution. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-10.md) as the practical follow-through.

## Debugging scenario

How can a high citation-validity percentage coexist with poor factual support?

## Knowledge check

1. What does raw vector storage omit?
2. Why separate stage-level evaluation?
3. What belongs in Phase 4 rather than this MVP?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-19-enterprise-knowledge-architecture-and-ingestion-boundaries.md) · [Next](../../../../../assessments/phase-03-assessment.md)
