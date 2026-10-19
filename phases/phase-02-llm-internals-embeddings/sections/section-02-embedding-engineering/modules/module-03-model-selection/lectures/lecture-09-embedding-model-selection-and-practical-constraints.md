# Lecture 09 — Embedding model selection and practical constraints

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L09 · Day 12 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Compare encoders using requirements and a model card.
- Account for truncation, language, licensing, and hardware.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Compare encoders using requirements and a model card.
- Account for truncation, language, licensing, and hardware.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

Start with the intended retrieval task: short-question matching, question-to-passage search, language coverage, domain terms, and text length. Review the model’s training purpose, license, input policy, output dimension, and expected query/document formatting. A larger dimension or parameter count does not by itself establish better ranking quality.

The course baseline is a short-text local encoder, not a claim of production superiority. The all-MiniLM-L6-v2 card describes a 384-dimensional sentence/short-paragraph representation and default truncation beyond 256 word pieces. Pin and inspect the selected revision; do not transfer these limits to other encoders or assume raw tokenizer capacity equals the sentence encoder’s configured limit.

Compare candidates on the same development queries and corpus. Keep preprocessing and relevance labels fixed. Record cold-start time, warm query latency, corpus encoding time, resident memory, and task quality separately. Optional alternative models require their own dependency, license, and prompt review. Choose a defensible baseline first; do not expand the course week into an open-ended model leaderboard exercise.

## Practical example and walkthrough

A compact encoder performs adequately on English support text but misses Urdu queries and product identifiers. The right conclusion is a workload mismatch to investigate, not that bigger dimensions automatically solve it.

Write a one-page selection record covering task, language, input cap, revision, license, dimensions, CPU feasibility, and a fallback if the model download is unavailable.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [all-MiniLM-L6-v2 model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — Publisher model card; Intended uses, dimensionality, truncation, and usage; 15 min selected study. A concrete short-text baseline with documented limits, not a universal recommendation.
- [Model Cards](https://huggingface.co/docs/hub/model-cards) — Official Hugging Face Hub documentation; Model-card metadata, intended uses, and limitations; 15 min selected study. Provides a checklist for model selection and licensing review.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html) — Official performance guide; Batching and backend overview; advanced optimizations optional; 15 min selected study. Supports measured throughput decisions rather than assumed speedups.
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/) — University syllabus and lecture links; Word vectors, neural networks, and Transformers selections; 20 min selected study. Optional mathematical/video fallback; a full university course is outside this week.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Write a one-page selection record covering task, language, input cap, revision, license, dimensions, CPU feasibility, and a fallback if the model download is unavailable. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-05.md).

## Debugging scenario

A model advertises a long sequence limit while the installed wrapper truncates earlier. Which two configurations must be checked?

## Knowledge check

1. Why is parameter count insufficient?
2. Which limits are model-specific?
3. What belongs in a fallback plan?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](../../module-02-embedding-pipeline/lectures/lecture-08-batching-persistence-and-reproducible-embedding-artifacts.md) · [Next](lecture-10-controlled-comparisons-failure-slices-and-model-changes.md)
