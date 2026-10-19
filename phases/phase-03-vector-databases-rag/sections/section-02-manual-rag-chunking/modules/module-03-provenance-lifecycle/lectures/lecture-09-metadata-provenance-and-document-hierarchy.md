# Lecture 09 — Metadata, provenance, and document hierarchy

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L09 · Day 19 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Why record source versions?
- Explain and demonstrate: Which formats have natural page locators?
- Explain and demonstrate: Does a correct locator establish factual support?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

A retrieved chunk must remain traceable after parsing, splitting, embedding, and storage. Record document ID, source version/hash, parser and chunker versions, chunk ID, title, and a format-appropriate locator. PDF page numbers, DOCX heading paths, CSV row identifiers, and TXT line ranges describe different source structures; never invent a page number for a format that has none.

Keep parent document and section relationships so a narrow hit can be interpreted without losing its original context. Extra headings can help a representation but must not silently change the evidence text or consume uncounted tokens. Preserve both normalized text used for retrieval and a stable source locator for inspection.

Do not assume that an export to Markdown preserves exact byte offsets or original pagination. The citation contract should state which locators are available and which are approximate. Provenance is a data-integrity requirement, not a promise that the source itself is authoritative or current.

## Practical example and walkthrough

A CSV row says plan=A, limit=100. Flattening column headers away leaves an uninterpretable number and makes the eventual citation misleading.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Qdrant Payload](https://qdrant.tech/documentation/manage-data/payload/) — Official documentation, free to read; selected json payload and data types; 15 min study estimate. Preserve source and chunk identity separately from vector coordinates.
- [Docling Document](https://docling-project.github.io/docling/concepts/docling_document/) — Official data-model guide, free to read; selected document items, hierarchy, and provenance; 20 min study estimate. Retain structure/locators rather than flattening every source into untraceable text.
- [Python csv Module](https://docs.python.org/3/library/csv.html) — Official standard-library documentation, free to read; selected dictreader, newline handling, quoting, and dialects; 15 min study estimate. Preserves row/column meaning; CSV is not a pile of whitespace-delimited words.

Optional supplements/fallbacks:

- [Qdrant Points](https://qdrant.tech/documentation/manage-data/points/) — Official documentation, free to read; selected point ids, upsert, and retrieval; 20 min study estimate. Clarifies UUID/integer IDs and repeatable writes.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Define source locators for PDF, DOCX, TXT, and CSV and test a chunk-to-source round trip on paper. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-05.md) as the practical follow-through.

## Debugging scenario

The displayed PDF page is off by one. Which indexing conventions and export stages must be reviewed?

## Knowledge check

1. Why record source versions?
2. Which formats have natural page locators?
3. Does a correct locator establish factual support?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../module-02-chunking/lectures/lecture-08-overlap-token-limits-and-chunk-policy-experiments.md) · [Next](lecture-10-ingestion-versions-idempotency-refresh-and-deletion.md)
