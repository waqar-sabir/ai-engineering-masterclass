# Phase 3 module solution guide

Attempt each module assessment first. These are review anchors, not learner scores or implementation results.

## Module 3.1.1 — Vector store and identity contracts

MCQ 1: **B**. MCQ 2: **C**. Use supported stable point IDs; keep source identity separately. Neighbor overlap and human relevance measure different things.

Practical and debugging anchors: Use a valid arbitrary payload ID but an invalid point-ID shape to distinguish the two contracts. Test wrong vector width and incompatible encoder revision even when numeric widths match.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.1.2 — Qdrant lifecycle and querying

MCQ 1: **D**. MCQ 2: **A**. Compatibility is explicit; never destroy shared data to hide a mismatch. Source display requires returned payload or a validated metadata lookup.

Practical and debugging anchors: Check installed client/server versions and mode. Missing text may be an omitted payload or wrong key. Collection recreation must not be used to hide a compatibility mismatch.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.2.1 — Manual RAG and evidence contracts

MCQ 1: **B**. MCQ 2: **A**. Reject unknown labels. Membership alone cannot verify entailment, source authority, or freshness.

Practical and debugging anchors: If valid citation IDs accompany an unsupported statement, inspect actual source text. If a provider fails, return a typed error rather than an insufficient-evidence success.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.2.2 — Chunk boundaries and token budgets

MCQ 1: **C**. MCQ 2: **D**. Name the length unit and validate final encoder tokens. Overlap duplicates evidence and must not eliminate forward progress.

Practical and debugging anchors: Do not interpret len as token count. Increasing overlap may increase duplicates without adding unique evidence. Separate fixed-window arithmetic from observed recursive-splitter output.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.2.3 — Provenance and ingestion lifecycle

MCQ 1: **B**. MCQ 2: **C**. Refresh must handle obsolete points explicitly. Locator semantics depend on the source format.

Practical and debugging anchors: A correct hash does not guarantee correct parsing or authorization. If a refreshed source still returns old passages, inspect active generation, collection selection, and stale-point cleanup.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.3.1 — LangChain components and model boundaries

MCQ 1: **A**. MCQ 2: **D**. Keep retrieval, model generation, and application validation separate; fake fixtures test code paths, not real generated quality.

Practical and debugging anchors: Old tutorial imports may refer to different package versions. Resolve through official component documentation, and test response-shape translation rather than assuming all provider wrappers are equivalent.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.3.2 — LangChain RAG and parity checks

MCQ 1: **C**. MCQ 2: **B**. Adapters can map different text/metadata keys. Change integration wiring while holding the experiment inputs fixed.

Practical and debugging anchors: Blank framework documents can come from payload-key mismatch. Different hits may come from filters, embedding roles, search parameters, or collection selection; inspect these before changing prompts.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.4.1 — Docling and multi-format parsing

MCQ 1: **D**. MCQ 2: **A**. Format-specific adapters and explicit conversion outcomes preserve evidence. OCR is an optional extension, not assumed success.

Practical and debugging anchors: Scanned PDFs may require OCR outside the text-first baseline. CSV headers and embedded delimiters need a format-aware reader. A longer export can contain layout noise; compare reading order and source locators.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.4.2 — Filtering, rewriting, fusion, and reranking

MCQ 1: **B**. MCQ 2: **C**. Candidate recall precedes reranking. Fusion combines evidence about order, not factual truth or universal calibrated scores.

Practical and debugging anchors: Do not sum dense and sparse raw scores without a justified calibration. If filters eliminate relevant evidence, inspect field types and missing values. Never call a reranker a substitute for initial recall.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.

## Module 3.5.1 — Knowledge assistant architecture and review

MCQ 1: **A**. MCQ 2: **C**. Raw vector math omits many components. Activation follows explicit completeness/integrity checks, not the first successful write.

Practical and debugging anchors: A source count alone understates chunk/index storage. Valid citations can still misrepresent evidence. If an ingestion failure disappears from the report, the pipeline’s success status is misleading.

Review the lab’s expected output and failure cases before accepting the submission. The learner must explain identity, version, and trust boundaries rather than only name a library.
