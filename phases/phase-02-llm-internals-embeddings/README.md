# Phase 02 — LLM Internals + Embeddings

[Course home](../../README.md) · [Course syllabus](../../COURSE-SYLLABUS.md) · [Progress](../../PROGRESS.md)

## Phase overview

Days 8–14 · Intermediate · 24.5-hour target, 3.5 hours/day. Audience: experienced full-stack engineers transitioning to AI engineering.

**Materials: Approved. Learner completion and implementation: Planned.** This is a materials-only package. Examples and proposed file trees are instructions for future learner work; no search application is bundled.

## Prerequisites

Phase 1 typed Python, contract validation, HTTP/provider boundaries, error handling, testing, and secret hygiene. Basic vector/matrix notation is introduced in the math primer. Python 3.12+ and a CPU-capable machine are needed only when executing future exercises. No paid API key, GPU training, or framework experience is required for the mandatory local baseline.

## Learning objectives and skills gained

- Explain training vs inference, tokens, context, neural layers, attention, and causal masks.
- Distinguish token/sentence embeddings and compute cosine/dot/Euclidean behavior correctly.
- Define reproducible encoder, role, normalization, and snapshot contracts.
- Compare embedding models using requirements, model cards, frozen queries, and honest failure slices.
- Design local exact semantic search, stable top-k, and Recall@k/MRR evaluation.
- Estimate capacity, isolate artifact failures, and explain privacy/retention boundaries.

## Complete outline and schedule

[Detailed syllabus](syllabus.md) · [Seven-day study plan](study-plan.md) · [Math primer](resources/math-primer.md)

## Sections and modules

- [Section 2.1 — LLM internals](sections/section-01-llm-internals/README.md)
- [Section 2.2 — Embedding engineering](sections/section-02-embedding-engineering/README.md)
- [Section 2.3 — Semantic search and evaluation](sections/section-03-semantic-search/README.md)
- [Section 2.4 — Embedding system design](sections/section-04-system-design/README.md)

Four sections contain seven modules and fourteen individual lectures. Each module links required resources, a guided lab, an independent assignment, multiple-choice/conceptual/practical/debugging checks, and separate solutions.

## Lecture navigation

- [Lecture 01 — Training, inference, and the next-token objective](sections/section-01-llm-internals/modules/module-01-training-tokenization/lectures/lecture-01-training-inference-and-the-next-token-objective.md)
- [Lecture 02 — Tokenization, context budgets, and truncation](sections/section-01-llm-internals/modules/module-01-training-tokenization/lectures/lecture-02-tokenization-context-budgets-and-truncation.md)
- [Lecture 03 — Neural networks, tensor shapes, and representations](sections/section-01-llm-internals/modules/module-02-neural-networks-attention/lectures/lecture-03-neural-networks-tensor-shapes-and-representations.md)
- [Lecture 04 — Self-attention, causal masks, and Transformer blocks](sections/section-01-llm-internals/modules/module-02-neural-networks-attention/lectures/lecture-04-self-attention-causal-masks-and-transformer-blocks.md)
- [Lecture 05 — Token, sentence, and document embeddings](sections/section-02-embedding-engineering/modules/module-01-representations-geometry/lectures/lecture-05-token-sentence-and-document-embeddings.md)
- [Lecture 06 — Cosine, dot product, Euclidean distance, and normalization](sections/section-02-embedding-engineering/modules/module-01-representations-geometry/lectures/lecture-06-cosine-dot-product-euclidean-distance-and-normalization.md)
- [Lecture 07 — Text to vectors: encoder contracts and query/document modes](sections/section-02-embedding-engineering/modules/module-02-embedding-pipeline/lectures/lecture-07-text-to-vectors-encoder-contracts-and-query-document-modes.md)
- [Lecture 08 — Batching, persistence, and reproducible embedding artifacts](sections/section-02-embedding-engineering/modules/module-02-embedding-pipeline/lectures/lecture-08-batching-persistence-and-reproducible-embedding-artifacts.md)
- [Lecture 09 — Embedding model selection and practical constraints](sections/section-02-embedding-engineering/modules/module-03-model-selection/lectures/lecture-09-embedding-model-selection-and-practical-constraints.md)
- [Lecture 10 — Controlled comparisons, failure slices, and model changes](sections/section-02-embedding-engineering/modules/module-03-model-selection/lectures/lecture-10-controlled-comparisons-failure-slices-and-model-changes.md)
- [Lecture 11 — Exact semantic search and stable top-k ranking](sections/section-03-semantic-search/modules/module-01-exact-search-evaluation/lectures/lecture-11-exact-semantic-search-and-stable-top-k-ranking.md)
- [Lecture 12 — Relevance judgments, Recall@k, MRR, and honest results](sections/section-03-semantic-search/modules/module-01-exact-search-evaluation/lectures/lecture-12-relevance-judgments-recall-k-mrr-and-honest-results.md)
- [Lecture 13 — Versioned embedding and local search architecture](sections/section-04-system-design/modules/module-01-architecture-capacity/lectures/lecture-13-versioned-embedding-and-local-search-architecture.md)
- [Lecture 14 — Capacity, failure boundaries, and the Phase 3 handoff](sections/section-04-system-design/modules/module-01-architecture-capacity/lectures/lecture-14-capacity-failure-boundaries-and-the-phase-3-handoff.md)

## Curated resources

[Full catalog with URLs, types, access, selections, time estimates, and fallbacks](resources/README.md) · [Lecture-resource map](resources/lecture-resource-map.md) · [Source and verification notes](resources/source-notes.md)

## Guided labs and assignments

- [Lab 1 — Tokenization and request budgets](sections/section-01-llm-internals/modules/module-01-training-tokenization/labs/lab-01.md)
- [Lab 2 — Attention and tensor shapes](sections/section-01-llm-internals/modules/module-02-neural-networks-attention/labs/lab-02.md)
- [Lab 3 — Vector geometry and ranking](sections/section-02-embedding-engineering/modules/module-01-representations-geometry/labs/lab-03.md)
- [Lab 4 — Embedding snapshots and persistence](sections/section-02-embedding-engineering/modules/module-02-embedding-pipeline/labs/lab-04.md)
- [Lab 5 — Model-card review and comparison](sections/section-02-embedding-engineering/modules/module-03-model-selection/labs/lab-05.md)
- [Lab 6 — Exact search and metric audit](sections/section-03-semantic-search/modules/module-01-exact-search-evaluation/labs/lab-06.md)
- [Lab 7 — Architecture and capacity review](sections/section-04-system-design/modules/module-01-architecture-capacity/labs/lab-07.md)

## AI system design

[Versioned embedding search service case study](system-design/embedding-search-case-study.md): architecture, requirements, Mermaid diagram, data flow, storage/API contracts, capacity, privacy, failure scenarios, trade-offs, and interview exercise.

## Phase project and final deliverable

[Document Semantic Search specification](project/README.md). Plan a reproducible local exact-search CLI with stable document identity, immutable embedding snapshots, a lexical baseline, and frozen-query evaluation. The planned deliverable returns ranked documents rather than generated answers. Project implementation remains deferred.

## Assessments

[Comprehensive phase assessment](assessments/phase-02-assessment.md) · [Phase solution guide — attempt first](assessments/solution-guide.md) · [Module solution guide — attempt first](assessments/module-solutions.md)

100 points: quiz 20, practical 35, debugging 15, design 20, project submission 10. Pass at 75 overall with at least 20 on the practical task and no exposed credentials/private data. No learner score is claimed.

## Completion and review

[Learner completion checklist](completion-checklist.md) · [Material validation notes](validation.md)

- [ ] Lectures, required selections, labs, and assignments completed by learner.
- [ ] Real embedding/search evidence and honest evaluation submitted later.
- [ ] Final assessment and system design reviewed.
- [ ] Explicit owner approval recorded before merge/next phase.

## Phase 3 preview

Phase 3 introduces document ingestion, chunking, Qdrant/vector databases, and RAG. It builds on this phase’s encoder compatibility, exact-search reference, artifact identity, and relevance labels. [Phase 3 overview](../phase-03-vector-databases-rag/README.md) now has materials In Review following the owner’s instruction. All implementations remain Planned.
