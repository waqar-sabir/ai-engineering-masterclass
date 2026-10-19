# Phase 3 comprehensive assessment

Material status: In Review. All learner submissions, scores, execution, and implementation: Planned. Attempt this page before reading the separate solution guide.

Total: 100 points. Pass at 75/100 overall with at least 20/35 on the practical task and safe credential/private-data handling. Material review is not a learner pass.

## Quiz — 20 points

Ten questions, two points each. For open responses, award one point for the correct mechanism and one for a concrete engineering consequence or example.

1. Which is a supported Qdrant point-ID approach? A. Any arbitrary string without mapping. B. A supported UUID or unsigned integer with source identity in payload. C. A floating-point similarity score. D. A new random ID on every retry.
2. Does perfect ANN recall prove that retrieved evidence answers the question? Explain the distinction.
3. A cited answer refers only to valid supplied labels. Which is established? A. Every claim is true. B. All sources are current. C. Citation membership; support still needs review. D. Prompt-injection resistance.
4. A splitter uses length_function=len and chunk_size=200. What unit is measured, and what additional model-boundary check is required?
5. For a simple sliding window of length 1000, chunk size 200, overlap 40, estimate the number of chunks. State why a recursive splitter may differ.
6. A source shrinks from five chunks to three and the first three IDs are upserted. What stale-data problem can remain?
7. Name suitable source locators for DOCX and CSV without inventing PDF pages.
8. A framework returns blank text from a populated vector collection. What adapter contract should be inspected before changing the model?
9. Can a reranker recover a relevant document that was never included in its candidate set? Explain.
10. Raw float32 vectors for 100 documents × 20 chunks × 384 dimensions require how many bytes? Name two omitted memory/storage components.

## Practical assessment — 35 points

Specify and later implement a cited-answer service over an injected retriever and fake generator, plus a generation-activation validator. Use deterministic source/chunk fixtures; no provider key is required for this coding assessment.

- Typed question/evidence/claim/result contracts; explicit answered/insufficient-evidence/conflict/error behavior: 6 points.
- Source version, chunk identity, format-specific locators, and compatible generation/encoder checks: 7 points.
- Bounded context with stable labels, deterministic unknown-label/missing-evidence rejection, and an explicit semantic-support review boundary: 7 points.
- Candidate generation validation, required-source completeness, idempotent identity/stale-point policy, and failure-preserving activation: 6 points.
- Tests for supported output, empty evidence, unknown label, valid-label unsupported claim fixture, malformed/refused/timed-out generation, stale version, and partial ingestion: 7 points.
- Readable code/design explanation and safe error/report handling: 2 points.

No code is provided or scored as executed during material preparation. Fake fixtures verify application behavior, not real model-quality or injection resistance.

## Debugging scenarios — 15 points

Five points each: root cause 2, safe fix 2, regression evidence 1.

1. A revised policy still returns paragraphs deleted from the original source. The ingestion rerun had no database errors.
2. Citation labels and JSON are valid, but the answer reverses a policy exception. Retrieval found the correct passage.
3. TXT/CSV questions work, while scanned PDF sources are marked successfully indexed with empty text. Reported corpus counts still include them.

## System design challenge — 20 points

Design the ingestion and query service for four-format document knowledge. Include separate ingestion/query paths and a diagram (4), versioned data/activation/deletion contracts (4), capacity assumptions and stage-level measurement (4), privacy/trust boundaries and failure isolation (4), and trade-offs/manual-framework parity plus the Phase 4 handoff (4).

State which properties belong to the local baseline and which would require production authorization, tenant isolation, queues, or deployment work. Do not claim those controls exist here.

## Project submission — 10 points

- Reproducible setup and source/parser/chunker/encoder manifests: 2.
- Four-format parsing/provenance evidence and tests during later execution: 2.
- Manual/framework parity plus frozen-query evaluation with failures preserved: 2.
- Architecture, security limits, refresh/deletion, and capacity assumptions: 2.
- Answered, insufficient-evidence/conflict, and typed-error demonstrations: 2.

The standalone project review rubric is separate from this ten-point component. No benchmark score is invented or required without a reviewed dataset.

## Submission instructions

Submit quiz answers, practical work/test evidence, debugging analysis, design package, and project artifacts. At the materials-only stage, implementation and live demonstrations remain future tasks. Record actual execution separately from proposed steps. Use the separate solution guide only after attempting the assessment.
