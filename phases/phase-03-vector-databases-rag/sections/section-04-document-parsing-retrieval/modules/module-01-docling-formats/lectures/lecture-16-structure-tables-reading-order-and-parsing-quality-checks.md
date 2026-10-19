# Lecture 16 — Structure, tables, reading order, and parsing quality checks

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L16 · Day 22 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: Why retain structure when possible?
- Explain and demonstrate: Which checks detect table corruption?
- Explain and demonstrate: When does a parser change require re-indexing?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

A document’s reading order, headings, tables, and page provenance affect what can be retrieved and cited. A flattened text export may join unrelated columns or detach a table value from its headers. Keep structured parser output when it helps preserve those relationships, and inspect a small gold excerpt before trusting bulk ingestion.

Define source-specific checks: expected headings for DOCX, page/reading-order checks for PDF, encoding/line ranges for TXT, and header/row preservation for CSV. Do not use extraction character count as the sole quality metric. More text can include repeated headers, footers, and layout noise.

Store parser version/options and conversion warnings with the source manifest. If a parser update changes normalized content, its downstream chunks and embeddings belong to a new generation. Table-heavy, OCR, or ambiguous layouts can be optional extensions with explicit limits rather than pretending the baseline solves them.

## Practical example and walkthrough

A two-column PDF interleaves the refund policy with an unrelated invoice example. Correct vector retrieval over the corrupted text cannot reconstruct the original meaning.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Docling Document](https://docling-project.github.io/docling/concepts/docling_document/) — Official data-model guide, free to read; selected document items, hierarchy, and provenance; 20 min study estimate. Retain structure/locators rather than flattening every source into untraceable text.
- [Docling Document Converter](https://docling-project.github.io/docling/reference/document_converter/) — Official API reference, free to read; selected conversion status and result handling; 15 min study estimate. Check failure/partial conversion rather than treating empty exports as success.

Optional supplements/fallbacks:

- [Docling Quickstart](https://docling-project.github.io/docling/getting_started/quickstart/) — Official tutorial, free to read; selected documentconverter and local document export; 20 min study estimate. Establishes conversion independently of retrieval.
- [Python csv Module](https://docs.python.org/3/library/csv.html) — Official standard-library documentation, free to read; selected dictreader, newline handling, quoting, and dialects; 15 min study estimate. Preserves row/column meaning; CSV is not a pile of whitespace-delimited words.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Create a parsing review rubric: completeness, order, headings, table semantics, and locator integrity, with a concrete failed fixture. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-08.md) as the practical follow-through.

## Debugging scenario

A parser upgrade improves text length but breaks citations. Which evidence should be compared before activation?

## Knowledge check

1. Why retain structure when possible?
2. Which checks detect table corruption?
3. When does a parser change require re-indexing?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](lecture-15-document-parsing-with-docling-and-format-specific-adapters.md) · [Next](../../module-02-retrieval-orientation/lectures/lecture-17-query-rewriting-and-metadata-filtering-controlled-introduction.md)
