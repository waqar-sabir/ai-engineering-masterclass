# Lecture 05 — Token, sentence, and document embeddings

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L05 · Day 10 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Distinguish representation levels and retrieval objectives.
- Explain pooling and the limits of semantic similarity.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Distinguish representation levels and retrieval objectives.
- Explain pooling and the limits of semantic similarity.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

A token embedding represents one vocabulary item or contextual token position. A sentence or document embedding is a fixed-width representation intended for comparison at that level. A retrieval encoder maps text into coordinates learned from its training task. A single coordinate is not generally a stable human-labeled attribute such as profitability or safety.

Pooling aggregates token states, for example with a mask-aware mean. Unmasked averaging includes padding and can move the representation when unrelated batch members change length. A retrieval-trained encoder can use pooling as part of its architecture, but copying a pooling recipe onto an arbitrary language model does not establish search quality.

Similarity expresses model-relative relatedness, not logical entailment, truth, recency, or authorization. “Refunds are available” and “Refunds are not available” share much vocabulary and topic. Embedding results still need task-specific evaluation. In the project, short curated documents fit the encoder window; long-document aggregation remains a Phase 3 concern.

## Practical example and walkthrough

A cancellation-policy query retrieves a document about making bookings because the broad topic is similar. The rank is a candidate suggestion, not proof that the policy exists in that document.

Compare a token-vector matrix with one pooled sentence vector. Explain how the mask affects the mean and why changing pooling requires re-encoding the corpus.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Creating Custom Models](https://sbert.net/docs/sentence_transformer/usage/custom_models.html) — Official Sentence Transformers documentation; Transformer, Pooling, and Normalize modules; 15 min selected study. Shows the representation pipeline; no custom training is required.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084) — Original research paper; Abstract and Sections 1–3 in linked PDF; 20 min selected study. Explains why sentence-level retrieval representations need an appropriate objective.
- [all-MiniLM-L6-v2 model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — Publisher model card; Intended uses, dimensionality, truncation, and usage; 15 min selected study. A concrete short-text baseline with documented limits, not a universal recommendation.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Compare a token-vector matrix with one pooled sentence vector. Explain how the mask affects the mean and why changing pooling requires re-encoding the corpus. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-03.md).

## Debugging scenario

Similarity is high for two contradictory statements. Why is the encoder not necessarily malfunctioning?

## Knowledge check

1. How do token and sentence embeddings differ?
2. Why must padding be excluded from a mean?
3. Can a cosine score establish truth?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](../../../../section-01-llm-internals/modules/module-02-neural-networks-attention/lectures/lecture-04-self-attention-causal-masks-and-transformer-blocks.md) · [Next](lecture-06-cosine-dot-product-euclidean-distance-and-normalization.md)
