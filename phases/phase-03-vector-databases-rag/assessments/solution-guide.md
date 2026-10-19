# Phase 3 assessment solution guide

Attempt the assessment first. These are review/scoring anchors, not recorded learner results or an application implementation.

## Quiz answers — 20 points

1. B. Use supported stable IDs such as UUIDs and preserve human/source identifiers in payload. Random IDs on each retry permit duplicates.
2. No. ANN recall compares candidate neighbors to exact vector neighbors. Task relevance compares retrieved source evidence to independently labeled question needs. Exact vector neighbors can still be irrelevant.
3. C. Supplied-label membership is structurally valid; it does not prove entailment, source truth/freshness, or security.
4. Characters. Check the final actual encoder-token count, including added headings/special-token overhead under the selected encoder contract.
5. Six windows: `1 + ceil((1000-200)/(200-40)) = 6`. Recursive boundaries depend on separators/content, so this is an estimate for the stated sliding-window rule, not its guaranteed count.
6. The old fourth/fifth chunk points remain unless explicitly removed or excluded by a fresh active generation/version. Upsert does not implicitly delete stale tails.
7. DOCX: stable heading/block/paragraph path under a source version. CSV: stable row identifier/range plus header context and source version. Do not invent pagination.
8. Text/payload-key and metadata mapping between direct records and the framework’s expected document representation; also verify the intended collection/generation.
9. No. Reordering a supplied set cannot retrieve an absent candidate. Improve candidate coverage separately, then evaluate reranking.
10. 3,072,000 bytes, about 2.93 MiB of raw vectors. Omitted components include text/payload, indexes, parser/model state, temporary batches, candidate/old generations, and application overhead.

## Practical review characteristics — 35 points

Contracts make source identity, active generation, evidence labels, and output states explicit. Required-source completeness is checked before activation; partial ingestion cannot overwrite a known-good generation. A changed source or policy produces a coherent representation and stale-point cleanup/deactivation strategy. Stable IDs alone are not a whole-corpus transaction.

The answer service validates input and compatibility, retrieves evidence, assembles a bounded labeled context, invokes an injected generator, validates output/citation membership, and maps sources from the same version. It does not use a provider timeout as an insufficient-evidence success. It does not claim valid labels prove support; an unsupported-claim fixture must be rejected or flagged by the declared semantic-review path.

Tests cover both happy path and failure boundaries, including partial ingestion and stale versions. Fake generation and hand vectors isolate orchestration; separate later real parsing/embedding/generation checks measure model behavior. A solution with fluent output but missing provenance/unknown-label checks cannot receive full credit.

## Debugging guidance — 15 points

1. Old chunks survived an incomplete replacement policy, or queries target the wrong active version. Build/validate a coherent generation or explicitly remove obsolete points, then verify source membership/locators. Regression: a five-to-three-chunk source update exposes no old tail passages.
2. Citation integrity and retrieval were insufficient to verify semantic interpretation. Inspect context assembly for a lost exception, then review claim support against the complete source. Regression: a rule-plus-exception fixture is preserved and the declared support check flags a reversed claim; valid labels alone do not pass it.
3. Parsing status/quality were conflated with indexing success. Mark image-only sources needs-review/OCR/unsupported under the baseline, exclude empty vectors/text from success, and fail activation when a required valid source is missing. Regression: empty/partial/scanned fixtures never count as successful required-source ingestion.

## System design scoring anchors — 20 points

0–5: a model call with a generic database diagram. 6–10: recognizable ingestion/query flow and basic source labels. 11–15: versioned chunk/vector contracts, candidate activation, failure isolation, real provenance, redaction, and honest scope. 16–20: explicit completeness/deletion/rollback policy, stage-specific evaluation, measured-vs-proposed capacity distinctions, manual/framework parity, and justified advanced-retrieval/production boundaries.

For 10,000 sources averaging 20 chunks at 384 float32 dimensions, raw vectors use 307,200,000 bytes, about 292.97 MiB. Indexes, payloads, models, copies, and concurrency make actual memory/storage higher or differently placed; no latency follows from this arithmetic.

## Project review anchors — 10 points

Evidence identifies the corpus, source/parser/chunker/encoder versions, all four formats, conversion outcomes, locators, active generation, fixed queries, real executed tests, and actual model outputs. Failure and no-evidence cases remain visible. A low or mixed measured result is acceptable evidence for improvement; an invented benchmark is not.
