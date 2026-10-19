# Lecture 12 — Relevance judgments, Recall@k, MRR, and honest results

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L12 · Day 13 · Guided study: 30 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Create independent relevance labels and compute ranked metrics.
- Distinguish invalid input, no relevant document, and low confidence.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Create independent relevance labels and compute ranked metrics.
- Distinguish invalid input, no relevant document, and low confidence.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

Retrieval evaluation needs queries, a fixed corpus, and human-reviewed relevance judgments. Define relevance for the task before inspecting scores. Recall@k is relevant retrieved documents divided by all relevant corpus documents for that query. Precision@k is relevant retrieved documents divided by the number of returned positions, with the denominator convention fixed in advance.

Reciprocal rank is `1/r` for the first relevant result at rank r, or zero when none is found. MRR averages reciprocal ranks across a declared eligible query set. Queries with no relevant corpus document have undefined recall; evaluate them separately for abstention or inappropriate-result behavior. Do not silently remove failures from an average.

For a relevant set `{d1,d3}` and ranking `[d2,d3,d1]`, Recall@2 is 1/2 and reciprocal rank is 1/2. If the output has no relevant item, both first-hit success and reciprocal rank are zero. Keep the individual rankings, labels, and metric rules in the report. A tiny synthetic benchmark teaches mechanics; it is not evidence of enterprise retrieval quality.

## Practical example and walkthrough

An irrelevant answer appears at rank one but a relevant document is second. Recall@3 may look strong while the first user-visible hit is poor. Use multiple metrics and inspect failures.

Compute Recall@1, Recall@3, and MRR for a fixed list of queries. Explain which denominator changes for a no-relevant query and how it is reported separately.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Evaluation of ranked retrieval results](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html) — Author-hosted Stanford IR textbook; Precision/recall, ranked evaluation, and test collections; 20 min selected study. Gives the evaluation background for the course-defined small benchmark.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Evaluation](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html) — Official API reference; InformationRetrievalEvaluator section; 15 min selected study. Maps query, corpus, and relevance judgments to retrieval evaluation.
- [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Official application guide; Symmetric/asymmetric search and exact search; 20 min selected study. Explains encode-query/document use without requiring a vector database.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Compute Recall@1, Recall@3, and MRR for a fixed list of queries. Explain which denominator changes for a no-relevant query and how it is reported separately. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-06.md).

## Debugging scenario

A score improves after deleting difficult queries. What reporting change makes the comparison misleading?

## Knowledge check

1. What labels does recall require?
2. How does MRR treat a first hit at rank four?
3. How should no-relevant queries be reported?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](lecture-11-exact-semantic-search-and-stable-top-k-ranking.md) · [Next](../../../../section-04-system-design/modules/module-01-architecture-capacity/lectures/lecture-13-versioned-embedding-and-local-search-architecture.md)
