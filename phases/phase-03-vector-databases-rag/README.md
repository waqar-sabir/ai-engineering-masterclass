# Phase 03 — Vector Databases + RAG

[Course home](../../README.md) · [Course syllabus](../../COURSE-SYLLABUS.md) · [Progress](../../PROGRESS.md)

## Phase overview

Days 15–24 · Intermediate · 35-hour target, 3.5 hours/day. Audience: experienced software engineers transitioning into AI engineering.

**Materials: In Review. All implementations and learner completion: Planned.** The user has deferred implementation until the whole course’s materials are ready. Code fragments, proposed commands, and file trees here are instructional material, not a bundled application.

## Prerequisites

Approved Phase 1–2 materials: typed Python, provider/error/output boundaries, prompt contracts, tokenization, embeddings, exact search, similarity metrics, manifests, and evaluation. Prior applications are still Planned; use contracts/fakes during this preparation pass. Later execution requires a reviewed learner environment and synthetic/licensed sources; model/provider credentials are not needed to read the course.

## Learning objectives and skills gained

- Explain vector collections, supported point IDs, payloads, indexes, and exact/approximate search.
- Design Qdrant insert/query/version contracts without silently recreating shared data.
- Trace manual RAG, budget/labeled context, citation integrity, semantic support, and explicit non-answer/error states.
- Choose/version chunk policies and preserve source hierarchy/locators across ingestion.
- Build a component map and parity plan for LangChain RAG without agents.
- Specify PDF/DOCX/TXT/CSV parsing with clear limits and quality checks.
- Introduce rewriting/filtering/hybrid/reranking, then hand deeper work to Phase 4.
- Design and evaluate a local Enterprise Knowledge Assistant baseline with traceable sources.

## Complete outline and schedule

[Detailed syllabus](syllabus.md) · [Ten-day study plan](study-plan.md) · [Contracts/evaluation primer](resources/contracts-and-evaluation.md)

## Sections and modules

- [Section 3.1 — Vector databases and Qdrant](sections/section-01-vector-databases/README.md)
- [Section 3.2 — Manual RAG, chunking, and metadata](sections/section-02-manual-rag-chunking/README.md)
- [Section 3.3 — LangChain components and RAG](sections/section-03-langchain-rag/README.md)
- [Section 3.4 — Document parsing and retrieval orientation](sections/section-04-document-parsing-retrieval/README.md)
- [Section 3.5 — System design and project integration](sections/section-05-system-design-project/README.md)

Five sections contain ten modules and twenty lectures. Every module links its resources, guided lab, independent assignment, multiple-choice/conceptual/practical/debugging assessment, and separate solutions.

## Lecture navigation

- [Lecture 01 — Vector database concepts and the exact-search reference](sections/section-01-vector-databases/modules/module-01-vector-contracts/lectures/lecture-01-vector-database-concepts-and-the-exact-search-reference.md)
- [Lecture 02 — Collections, points, payloads, and identity contracts](sections/section-01-vector-databases/modules/module-01-vector-contracts/lectures/lecture-02-collections-points-payloads-and-identity-contracts.md)
- [Lecture 03 — Qdrant setup and controlled collection lifecycle](sections/section-01-vector-databases/modules/module-02-qdrant-lifecycle/lectures/lecture-03-qdrant-setup-and-controlled-collection-lifecycle.md)
- [Lecture 04 — Upsert, query, payload return, and reproducible search](sections/section-01-vector-databases/modules/module-02-qdrant-lifecycle/lectures/lecture-04-upsert-query-payload-return-and-reproducible-search.md)
- [Lecture 05 — Manual RAG: retrieval, context assembly, and generation](sections/section-02-manual-rag-chunking/modules/module-01-manual-rag/lectures/lecture-05-manual-rag-retrieval-context-assembly-and-generation.md)
- [Lecture 06 — Evidence labels, citations, context budgets, and abstention](sections/section-02-manual-rag-chunking/modules/module-01-manual-rag/lectures/lecture-06-evidence-labels-citations-context-budgets-and-abstention.md)
- [Lecture 07 — Fixed, sentence, and recursive chunking](sections/section-02-manual-rag-chunking/modules/module-02-chunking/lectures/lecture-07-fixed-sentence-and-recursive-chunking.md)
- [Lecture 08 — Overlap, token limits, and chunk-policy experiments](sections/section-02-manual-rag-chunking/modules/module-02-chunking/lectures/lecture-08-overlap-token-limits-and-chunk-policy-experiments.md)
- [Lecture 09 — Metadata, provenance, and document hierarchy](sections/section-02-manual-rag-chunking/modules/module-03-provenance-lifecycle/lectures/lecture-09-metadata-provenance-and-document-hierarchy.md)
- [Lecture 10 — Ingestion versions, idempotency, refresh, and deletion](sections/section-02-manual-rag-chunking/modules/module-03-provenance-lifecycle/lectures/lecture-10-ingestion-versions-idempotency-refresh-and-deletion.md)
- [Lecture 11 — LangChain components and provider boundaries](sections/section-03-langchain-rag/modules/module-01-components/lectures/lecture-11-langchain-components-and-provider-boundaries.md)
- [Lecture 12 — Messages, invocation, output contracts, and test doubles](sections/section-03-langchain-rag/modules/module-01-components/lectures/lecture-12-messages-invocation-output-contracts-and-test-doubles.md)
- [Lecture 13 — RAG with LangChain and Qdrant: integration contracts](sections/section-03-langchain-rag/modules/module-02-integration-parity/lectures/lecture-13-rag-with-langchain-and-qdrant-integration-contracts.md)
- [Lecture 14 — Pipeline parity, failure traces, and layered evaluation](sections/section-03-langchain-rag/modules/module-02-integration-parity/lectures/lecture-14-pipeline-parity-failure-traces-and-layered-evaluation.md)
- [Lecture 15 — Document parsing with Docling and format-specific adapters](sections/section-04-document-parsing-retrieval/modules/module-01-docling-formats/lectures/lecture-15-document-parsing-with-docling-and-format-specific-adapters.md)
- [Lecture 16 — Structure, tables, reading order, and parsing quality checks](sections/section-04-document-parsing-retrieval/modules/module-01-docling-formats/lectures/lecture-16-structure-tables-reading-order-and-parsing-quality-checks.md)
- [Lecture 17 — Query rewriting and metadata filtering: controlled introduction](sections/section-04-document-parsing-retrieval/modules/module-02-retrieval-orientation/lectures/lecture-17-query-rewriting-and-metadata-filtering-controlled-introduction.md)
- [Lecture 18 — Hybrid retrieval, rank fusion, and reranking: controlled introduction](sections/section-04-document-parsing-retrieval/modules/module-02-retrieval-orientation/lectures/lecture-18-hybrid-retrieval-rank-fusion-and-reranking-controlled-introduction.md)
- [Lecture 19 — Enterprise knowledge architecture and ingestion boundaries](sections/section-05-system-design-project/modules/module-01-architecture/lectures/lecture-19-enterprise-knowledge-architecture-and-ingestion-boundaries.md)
- [Lecture 20 — Capacity, evaluation, failure recovery, and the Phase 4 handoff](sections/section-05-system-design-project/modules/module-01-architecture/lectures/lecture-20-capacity-evaluation-failure-recovery-and-the-phase-4-handoff.md)

## Curated learning resources

[Catalog: direct URLs, types, free access, selections, time estimates, reasons, and fallbacks](resources/README.md) · [Lecture-resource map](resources/lecture-resource-map.md) · [Source and verification notes](resources/source-notes.md)

## Guided labs and assignments

- [Lab 01 — Vector store and identity contracts](sections/section-01-vector-databases/modules/module-01-vector-contracts/labs/lab-01.md)
- [Lab 02 — Qdrant lifecycle and querying](sections/section-01-vector-databases/modules/module-02-qdrant-lifecycle/labs/lab-02.md)
- [Lab 03 — Manual RAG and evidence contracts](sections/section-02-manual-rag-chunking/modules/module-01-manual-rag/labs/lab-03.md)
- [Lab 04 — Chunk boundaries and token budgets](sections/section-02-manual-rag-chunking/modules/module-02-chunking/labs/lab-04.md)
- [Lab 05 — Provenance and ingestion lifecycle](sections/section-02-manual-rag-chunking/modules/module-03-provenance-lifecycle/labs/lab-05.md)
- [Lab 06 — LangChain components and model boundaries](sections/section-03-langchain-rag/modules/module-01-components/labs/lab-06.md)
- [Lab 07 — LangChain RAG and parity checks](sections/section-03-langchain-rag/modules/module-02-integration-parity/labs/lab-07.md)
- [Lab 08 — Docling and multi-format parsing](sections/section-04-document-parsing-retrieval/modules/module-01-docling-formats/labs/lab-08.md)
- [Lab 09 — Filtering, rewriting, fusion, and reranking](sections/section-04-document-parsing-retrieval/modules/module-02-retrieval-orientation/labs/lab-09.md)
- [Lab 10 — Knowledge assistant architecture and review](sections/section-05-system-design-project/modules/module-01-architecture/labs/lab-10.md)

Each lab includes objectives, prerequisites, tools/dependencies, setup, proposed folder structure, ordered steps, an educational example, future commands/tests, expected outcomes, troubleshooting, acceptance criteria, and an independent counterexample.

## AI system design

[Document ingestion and grounded knowledge retrieval case study](../../system-design/03-document-ingestion/README.md) · [Phase design guide](system-design/README.md)

Requirements, Mermaid architecture, data flow, storage/API choices, capacity, privacy/security, failure responses, evaluation/telemetry, trade-offs, and an interview challenge are included. Production multi-tenancy and deployment are explicitly outside the local baseline.

## Phase project

[Enterprise Knowledge Assistant guide](project/README.md) · [Canonical complete specification](../../projects/03-company-knowledge-agent/SPEC.md)

Twelve small valid sources span PDF, DOCX, TXT, and CSV. The planned assistant uses compatible Qdrant generations, manual/framework RAG, cited claims, and honest stage-specific evaluation. The existing Company Knowledge Agent portfolio folder hosts this knowledge foundation; later agent/pgvector capabilities remain future extensions.

## Assessments

[Final phase assessment](assessments/phase-03-assessment.md) · [Phase solutions — attempt first](assessments/solution-guide.md) · [Module solutions — attempt first](assessments/module-solutions.md)

100 points: quiz 20, practical 35, debugging 15, system design 20, project submission 10. Pass at 75 overall and at least 20 practical with safe data handling. No learner score or execution is claimed.

## Completion and material review

[Future learner checklist](completion-checklist.md) · [Material validation notes](validation.md)

- [ ] Owner reviews and approves Phase 3 materials.
- [ ] Implementation begins only after a later explicit course-wide implementation instruction.
- [ ] Learner execution, assessments, and project evidence reviewed during that later pass.

## Phase 4 preview

Phase 4 deepens retrieval metrics, reranking, query transformation, metadata/tenant filtering, and RAG security. It builds on this phase’s baseline and failure traces. [Phase 4 overview](../phase-04-advanced-rag/README.md) remains Planned; no detailed Phase 4 material is generated here.
