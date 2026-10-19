# Phase 3 curated resource catalog

All 26 selected pages were opened during preparation on 2026-10-19. Access labels describe reading the referenced pages, not paid API calls, hosted services, compute, certificates, or model downloads. Study times are course estimates for selected excerpts, not asserted video runtimes. No paid course is mandatory.

## R01 — Qdrant Collections

- Direct resource: [Qdrant Collections](https://qdrant.tech/documentation/manage-data/collections/).
- Type: Official documentation. Reading access: Free.
- Exact selection: Collection vector schema and configuration. Study allocation: 15 minutes.
- Reason: Define dimension and distance before insertion.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R02 — Qdrant Points

- Direct resource: [Qdrant Points](https://qdrant.tech/documentation/manage-data/points/).
- Type: Official documentation. Reading access: Free.
- Exact selection: Point IDs, upsert, and retrieval. Study allocation: 20 minutes.
- Reason: Clarifies UUID/integer IDs and repeatable writes.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R03 — Qdrant Payload

- Direct resource: [Qdrant Payload](https://qdrant.tech/documentation/manage-data/payload/).
- Type: Official documentation. Reading access: Free.
- Exact selection: JSON payload and data types. Study allocation: 15 minutes.
- Reason: Preserve source and chunk identity separately from vector coordinates.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R04 — Qdrant Local Quickstart

- Direct resource: [Qdrant Local Quickstart](https://qdrant.tech/documentation/quickstart/).
- Type: Official tutorial. Reading access: Free.
- Exact selection: Local setup, collection, insert, and query. Study allocation: 20 minutes.
- Reason: A small local exercise before infrastructure tuning.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R05 — Qdrant Search

- Direct resource: [Qdrant Search](https://qdrant.tech/documentation/search/search/).
- Type: Official documentation. Reading access: Free.
- Exact selection: Query API, payload return, and exact search. Study allocation: 20 minutes.
- Reason: Compare returned candidates with the Phase 2 exact baseline.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R06 — Qdrant Indexing

- Direct resource: [Qdrant Indexing](https://qdrant.tech/documentation/manage-data/indexing/).
- Type: Official documentation. Reading access: Free.
- Exact selection: Vector vs payload indexes. Study allocation: 15 minutes.
- Reason: Separate fast candidate search from metadata lookup requirements.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R07 — Qdrant Filtering

- Direct resource: [Qdrant Filtering](https://qdrant.tech/documentation/search/filtering/).
- Type: Official documentation. Reading access: Free.
- Exact selection: Must/should/must-not and field conditions. Study allocation: 15 minutes.
- Reason: Makes metadata constraints explicit and testable.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R08 — LangChain Text Splitter Integrations

- Direct resource: [LangChain Text Splitter Integrations](https://docs.langchain.com/oss/python/integrations/splitters/index).
- Type: Official integration guide. Reading access: Free.
- Exact selection: Splitter families and unit choices. Study allocation: 15 minutes.
- Reason: Choose splitters from document structure rather than a universal size.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R09 — Splitting Recursively

- Direct resource: [Splitting Recursively](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter).
- Type: Official tutorial. Reading access: Free.
- Exact selection: Separators, chunk_size, overlap, and length_function. Study allocation: 20 minutes.
- Reason: Avoid confusing character length with token length.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R10 — LangChain Models

- Direct resource: [LangChain Models](https://docs.langchain.com/oss/python/langchain/models).
- Type: Official documentation. Reading access: Free.
- Exact selection: Invocation and structured outputs; skip agents/tools. Study allocation: 15 minutes.
- Reason: Review provider boundaries without pulling agent loops forward.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R11 — LangChain Messages

- Direct resource: [LangChain Messages](https://docs.langchain.com/oss/python/langchain/messages).
- Type: Official documentation. Reading access: Free.
- Exact selection: Message roles and response content. Study allocation: 15 minutes.
- Reason: Keep instructions separate from retrieved untrusted source text.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R12 — LangChain Vector Store Integrations

- Direct resource: [LangChain Vector Store Integrations](https://docs.langchain.com/oss/python/integrations/vectorstores/index).
- Type: Official component guide. Reading access: Free.
- Exact selection: Document objects and add/delete/search interface. Study allocation: 15 minutes.
- Reason: Explains the abstraction without hiding collection compatibility.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R13 — LangChain Retriever Integrations

- Direct resource: [LangChain Retriever Integrations](https://docs.langchain.com/oss/python/integrations/retrievers/index).
- Type: Official component guide. Reading access: Free.
- Exact selection: Retriever role and integration categories. Study allocation: 15 minutes.
- Reason: Distinguish retrieval behavior from storage and generation.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R14 — LangChain Qdrant Integration

- Direct resource: [LangChain Qdrant Integration](https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant).
- Type: Official integration guide. Reading access: Free.
- Exact selection: QdrantVectorStore, local mode, and dense retrieval. Study allocation: 20 minutes.
- Reason: Map adapter behavior to the manual pipeline and preserve payload schema.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R15 — Docling Supported Formats

- Direct resource: [Docling Supported Formats](https://docling-project.github.io/docling/usage/supported_formats/).
- Type: Official format reference. Reading access: Free.
- Exact selection: Input/export formats and limitations. Study allocation: 10 minutes.
- Reason: Verify PDF/DOCX/CSV support; use native UTF-8 input for TXT.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R16 — Docling Quickstart

- Direct resource: [Docling Quickstart](https://docling-project.github.io/docling/getting_started/quickstart/).
- Type: Official tutorial. Reading access: Free.
- Exact selection: DocumentConverter and local document export. Study allocation: 20 minutes.
- Reason: Establishes conversion independently of retrieval.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R17 — Docling Document

- Direct resource: [Docling Document](https://docling-project.github.io/docling/concepts/docling_document/).
- Type: Official data-model guide. Reading access: Free.
- Exact selection: Document items, hierarchy, and provenance. Study allocation: 20 minutes.
- Reason: Retain structure/locators rather than flattening every source into untraceable text.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R18 — Docling Document Converter

- Direct resource: [Docling Document Converter](https://docling-project.github.io/docling/reference/document_converter/).
- Type: Official API reference. Reading access: Free.
- Exact selection: Conversion status and result handling. Study allocation: 15 minutes.
- Reason: Check failure/partial conversion rather than treating empty exports as success.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R19 — Python csv Module

- Direct resource: [Python csv Module](https://docs.python.org/3/library/csv.html).
- Type: Official standard-library documentation. Reading access: Free.
- Exact selection: DictReader, newline handling, quoting, and dialects. Study allocation: 15 minutes.
- Reason: Preserves row/column meaning; CSV is not a pile of whitespace-delimited words.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R20 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- Direct resource: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401).
- Type: Original research paper. Reading access: Free.
- Exact selection: Abstract and retrieval/generation architecture. Study allocation: 20 minutes.
- Reason: Historical conceptual grounding; the course uses an application pipeline, not training the paper’s model.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R21 — Lost in the Middle: How Language Models Use Long Contexts

- Direct resource: [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172).
- Type: Original research paper. Reading access: Free.
- Exact selection: Abstract and reported position effects. Study allocation: 15 minutes.
- Reason: Motivates context inspection; not a claim about every current model.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R22 — Qdrant Hybrid and Multi-Stage Queries

- Direct resource: [Qdrant Hybrid and Multi-Stage Queries](https://qdrant.tech/documentation/search/hybrid-queries/).
- Type: Official documentation. Reading access: Free.
- Exact selection: Prefetch and reciprocal-rank fusion overview. Study allocation: 20 minutes.
- Reason: Day 23 orientation; implementation/deeper tuning belongs to Phase 4.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R23 — Qdrant Hybrid Search with Reranking

- Direct resource: [Qdrant Hybrid Search with Reranking](https://qdrant.tech/documentation/tutorials-basics/reranking-hybrid-search/).
- Type: Official tutorial. Reading access: Free.
- Exact selection: Candidate retrieval vs reranking roles. Study allocation: 20 minutes.
- Reason: Shows the ordering of stages; optional extension rather than baseline requirement.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R24 — OWASP LLM Prompt Injection Prevention Cheat Sheet

- Direct resource: [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).
- Type: Official security guidance. Reading access: Free.
- Exact selection: Indirect prompt injection and layered controls. Study allocation: 20 minutes.
- Reason: Supports a clear trust boundary; delimiters alone do not establish security.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R25 — LangChain RAG from Scratch

- Direct resource: [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch).
- Type: Publisher repository with linked video playlist. Reading access: Free.
- Exact selection: Indexing, retrieval, and generation introductory notebooks/videos. Study allocation: 20 minutes.
- Reason: Optional conceptual/video fallback; review old notebook APIs against current component documentation.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## R26 — Qdrant Essentials Course

- Direct resource: [Qdrant Essentials Course](https://qdrant.tech/course/essentials/).
- Type: Publisher video-first course. Reading access: Free.
- Exact selection: Selected collection/search lessons only. Study allocation: 20 minutes.
- Reason: Optional video alternative; full course is outside the phase timebox.
- Priority: follow required/optional labels in each lecture.
- Verification: reference page opened; playback, nested links, model downloads, and all code examples were not executed.

## Reading order and fallbacks

Read the course notes, then the named required excerpt, then attempt the lab and module assessment. Reuse a source already studied rather than adding its duration repeatedly. The daily schedule reserves 30 minutes of external reading on most days; catalog times are a menu, not an instruction to read every entry.

If a video is unavailable, use the matching official text resource. If a legacy integration tutorial diverges from current documentation, preserve the manual pipeline contracts and update the adapter only after checking the official component documentation. If a model, parser asset, or Qdrant runtime cannot be downloaded during later implementation, complete hand-vector/fixture exercises and explicitly leave real execution pending.

Qdrant concept URLs now redirect to manage-data/search paths; canonical successful pages are linked here. The former LangChain retrieval page redirected toward an agent-focused page, so this phase uses explicit component documentation instead. An inaccessible prompt API reference and an unavailable Docling chunking URL were not selected. TXT is handled natively rather than asserted as a Docling input format.
