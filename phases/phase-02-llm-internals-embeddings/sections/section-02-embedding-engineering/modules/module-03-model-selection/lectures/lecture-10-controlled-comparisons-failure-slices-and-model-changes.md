# Lecture 10 — Controlled comparisons, failure slices, and model changes

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L10 · Day 12 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Separate development tuning from final evaluation.
- Plan safe whole-corpus re-encoding after a model change.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Separate development tuning from final evaluation.
- Plan safe whole-corpus re-encoding after a model change.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

Use a small development set to choose the encoder and policy, then freeze them before examining held-out results. A test set that repeatedly guides prompt, threshold, or model choices has become development data. Small samples have high uncertainty; report counts and failure examples rather than declaring broad superiority from one or two improved queries.

Useful slices include paraphrases, exact identifiers, negation, mixed languages, ambiguous questions, and queries with no relevant document. Compare a simple lexical baseline as well as semantic ranking. Dense retrieval can improve paraphrase matching while underperforming exact-ID lookup. These observations motivate later retrieval improvements, not premature introduction of hybrid engines or rerankers.

A model migration changes the representation contract. Build a complete candidate corpus snapshot, validate it, compare on frozen queries, and activate query and corpus contracts together. Same dimensionality is not a shortcut. Retain the prior snapshot for rollback and record which revision produced each result. Artificially padding or truncating vectors does not make unrelated encoders compatible.

## Practical example and walkthrough

A candidate wins on three paraphrases but loses all ticket-number queries. Keep those slices visible and decide against requirements rather than hiding them in a single average.

Prepare a comparison worksheet with model/revision, dev score, held-out score, latency method, memory method, and failure slices. Leave observed results blank until measured.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Evaluation](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html) — Official API reference; InformationRetrievalEvaluator section; 15 min selected study. Maps query, corpus, and relevance judgments to retrieval evaluation.
- [Evaluation of ranked retrieval results](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html) — Author-hosted Stanford IR textbook; Precision/recall, ranked evaluation, and test collections; 20 min selected study. Gives the evaluation background for the course-defined small benchmark.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Model Cards](https://huggingface.co/docs/hub/model-cards) — Official Hugging Face Hub documentation; Model-card metadata, intended uses, and limitations; 15 min selected study. Provides a checklist for model selection and licensing review.
- [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — Official application guide; Symmetric/asymmetric search and exact search; 20 min selected study. Explains encode-query/document use without requiring a vector database.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Prepare a comparison worksheet with model/revision, dev score, held-out score, latency method, memory method, and failure slices. Leave observed results blank until measured. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-05.md).

## Debugging scenario

Why is comparing model A on one corpus and model B on a revised corpus an invalid experiment?

## Knowledge check

1. When has a test set become development data?
2. Why compare lexical retrieval?
3. How do query and corpus migrations coordinate?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](lecture-09-embedding-model-selection-and-practical-constraints.md) · [Next](../../../../section-03-semantic-search/modules/module-01-exact-search-evaluation/lectures/lecture-11-exact-semantic-search-and-stable-top-k-ranking.md)
