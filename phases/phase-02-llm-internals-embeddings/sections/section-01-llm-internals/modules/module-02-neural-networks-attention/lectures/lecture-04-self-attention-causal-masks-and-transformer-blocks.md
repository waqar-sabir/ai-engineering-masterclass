# Lecture 04 — Self-attention, causal masks, and Transformer blocks

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L04 · Day 9 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Trace queries, keys, values, and attention shapes.
- Explain masking and the role of the surrounding Transformer block.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Trace queries, keys, values, and attention shapes.
- Explain masking and the role of the surrounding Transformer block.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

For self-attention, projections of one input sequence supply queries, keys, and values. If `Q` and `K` have width `d_k`, scaled scores are `Q Kᵀ / sqrt(d_k)`; row-wise softmax creates mixing weights, which multiply `V`. Cross-attention instead draws queries and key/value inputs from different sequences. Similar names do not make this computation the same as embedding retrieval.

A causal mask prevents a position from attending to later positions during autoregressive processing. Padding masks address artificial batch padding. Multi-head attention learns several projections, combines their outputs, and passes them through the rest of the block. Feed-forward transformations, residual paths, normalization, and positional information are also necessary to understand the architecture.

For a toy row of equal logits, softmax gives equal weight to every allowed position. Masking one position removes it before normalization; setting it to zero probability after softmax without renormalizing changes the computation. Attention weights describe an internal mixing operation; they are not a guaranteed faithful explanation of a final claim.

## Practical example and walkthrough

In a search encoder, bidirectional context can represent a short passage. In an autoregressive decoder, access to future target tokens would leak the answer during training. The mask follows the task.

With two tokens and equal allowed scores, calculate the first row with and without a causal mask, then compute the weighted value vector.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Attention Scoring Functions](https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html) — Author-maintained textbook; Scaled dot-product attention and masking; 20 min selected study. Provides equations and mask behavior for a hand calculation.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Original research paper; Sections 3.1–3.3 in linked PDF; 25 min selected study. Optional historical architecture reference; modern models vary.
- [Hugging Face general Transformer architecture video](https://www.youtube-nocookie.com/embed/H39Z_720T5s) — Official course embedded video; Architecture walkthrough linked from R01; 15 min selected study. Optional visual explanation when the architecture text is unclear.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

With two tokens and equal allowed scores, calculate the first row with and without a causal mask, then compute the weighted value vector. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-02.md).

## Debugging scenario

A decoder appears perfect on its training examples but fails when generating token by token. How could a missing causal mask cause this?

## Knowledge check

1. What is the shape of QKᵀ?
2. Why divide by sqrt(d_k)?
3. What does a causal mask prevent?
4. What components surround attention in a Transformer block?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](lecture-03-neural-networks-tensor-shapes-and-representations.md) · [Next](../../../../section-02-embedding-engineering/modules/module-01-representations-geometry/lectures/lecture-05-token-sentence-and-document-embeddings.md)
