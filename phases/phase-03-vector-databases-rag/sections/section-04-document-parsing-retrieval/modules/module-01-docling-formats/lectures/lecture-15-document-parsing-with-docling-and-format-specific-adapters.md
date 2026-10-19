# Lecture 15 — Document parsing with Docling and format-specific adapters

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P03-L15 · Day 22 · Guided notes/example: 40 minutes · Difficulty: Intermediate.

Material status: In Review. Learner completion and implementation: Planned. Selected external reading has a separate allocation in the study plan.

## Learning objectives and syllabus

- Explain and demonstrate: How does parsing differ from chunking?
- Explain and demonstrate: What is the baseline scanned-PDF policy?
- Explain and demonstrate: Why use a CSV-specific adapter?
- Trace the worked example, identify a failure boundary, and carry the invariant into the module lab.

## Prerequisites

Phase 1 typed interfaces, validation, prompting, and provider errors; Phase 2 encoder compatibility, exact search, similarity, and evaluation. Complete the preceding Phase 3 lecture.

## Core learning material

Document conversion produces an intermediate representation from a source format. Parsing is not chunking, embedding, retrieval, or factual verification. Use a parser result and status before exporting text; empty or partial output needs a visible handling policy. Preserve format and source version throughout conversion.

For the mandatory small corpus, use selectable-text PDFs and simple DOCX files through Docling after checking the installed format support. TXT is read directly with explicit UTF-8 handling; CSV can use the standard library to preserve headers and row identities. A scanned PDF may require OCR and should be marked needs-review/unsupported in the baseline rather than silently indexed as empty.

Parser/model dependencies can download assets or require substantial memory. In the later implementation pass, document cache/version behavior and approved options. The current phase prepares instructions only; conversion success across every possible PDF or office file is not claimed.

## Practical example and walkthrough

A PDF opens normally in a viewer but contains only scanned images. A text-first converter may return no useful text; route it to an explicit OCR/review extension instead of declaring ingestion successful.

Trace inputs, intermediate evidence/metadata, outputs, and the earliest point where a failed invariant can be detected. The module lab adds a small educational code fragment or worked calculation; no application is bundled.

## Learning resources

Required selections (free to read; choose excerpts within the daily budget):

- [Docling Supported Formats](https://docling-project.github.io/docling/usage/supported_formats/) — Official format reference, free to read; selected input/export formats and limitations; 10 min study estimate. Verify PDF/DOCX/CSV support; use native UTF-8 input for TXT.
- [Docling Quickstart](https://docling-project.github.io/docling/getting_started/quickstart/) — Official tutorial, free to read; selected documentconverter and local document export; 20 min study estimate. Establishes conversion independently of retrieval.
- [Python csv Module](https://docs.python.org/3/library/csv.html) — Official standard-library documentation, free to read; selected dictreader, newline handling, quoting, and dialects; 15 min study estimate. Preserves row/column meaning; CSV is not a pile of whitespace-delimited words.

Optional supplements/fallbacks:

- [Docling Document Converter](https://docling-project.github.io/docling/reference/document_converter/) — Official API reference, free to read; selected conversion status and result handling; 15 min study estimate. Check failure/partial conversion rather than treating empty exports as success.

Video alternative: [Qdrant Essentials](https://qdrant.tech/course/essentials/) for storage/search concepts, or the introductory video playlist linked in [LangChain RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) for retrieval/generation concepts. For parsing/provenance, official Docling text is primary; the RAG videos are background only. Optional 15–20 minute selections replace other optional study, not additional mandatory hours. Historical notebook APIs must be checked against current component docs.

## Independent assignment

Choose one simple source of each required format and define expected status, text fields, and locators. Include one original counterexample, the invariant it violates, and the expected safe behavior. Complete [the module lab](../labs/lab-08.md) as the practical follow-through.

## Debugging scenario

Why should an empty parser export not produce a successful searchable document?

## Knowledge check

1. How does parsing differ from chunking?
2. What is the baseline scanned-PDF policy?
3. Why use a CSV-specific adapter?

## Completion criteria

- [ ] Explain the mechanism and its prerequisites in your own words.
- [ ] Submit the worked example, independent counterexample, and failure analysis.
- [ ] Attempt the [module assessment](../assessments/knowledge-check.md) before its separate solution guide.
- [ ] Label proposed behavior separately from any later executed result.

## Next lecture

[Previous](../../../../section-03-langchain-rag/modules/module-02-integration-parity/lectures/lecture-14-pipeline-parity-failure-traces-and-layered-evaluation.md) · [Next](lecture-16-structure-tables-reading-order-and-parsing-quality-checks.md)
