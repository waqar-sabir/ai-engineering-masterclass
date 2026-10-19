# Lecture 03 — Neural networks, tensor shapes, and representations

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L03 · Day 9 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Trace a learned transformation through tensor dimensions.
- Distinguish parameters, activations, token embeddings, and sentence embeddings.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Trace a learned transformation through tensor dimensions.
- Distinguish parameters, activations, token embeddings, and sentence embeddings.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

A neural layer applies a learned transformation followed, often, by a nonlinear function. With row-vector convention, `X` shaped `[tokens, input_width]` multiplied by `W` shaped `[input_width, output_width]` produces `[tokens, output_width]`; a bias broadcasts across rows. A multilayer network composes these transformations. Activations depend on the current input; parameters are the learned matrices and biases.

An embedding lookup selects one learned row per token ID. Later layers combine context, so the same surface token can have different contextual representations in different sentences. A contextual token vector, however, is not automatically a useful document-search vector. A pooling strategy and retrieval-suitable training objective define the final sentence representation.

Batch dimensions add another axis. Distinguish `[batch, tokens, hidden]` from `[batch, embedding_dimension]`; averaging the batch axis accidentally mixes documents. A reliable engineering review writes shapes beside every operation before optimizing it. Full gradient derivations and training a network are optional; shape literacy is mandatory.

## Practical example and walkthrough

A matrix multiplication succeeds after an accidental transpose, but the result now compares tokens instead of documents. Shape compatibility alone does not prove that the operation has the intended meaning.

Trace `[2, 5, 8]` token states into `[2, 8]` sentence vectors. Identify the token axis, batch axis, and padding mask before taking a mean.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Build the Neural Network](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) — Official PyTorch tutorial; Layers and forward pass; omit training implementation; 20 min selected study. Makes tensor dimensions and learned parameters concrete.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Creating Custom Models](https://sbert.net/docs/sentence_transformer/usage/custom_models.html) — Official Sentence Transformers documentation; Transformer, Pooling, and Normalize modules; 15 min selected study. Shows the representation pipeline; no custom training is required.
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/) — University syllabus and lecture links; Word vectors, neural networks, and Transformers selections; 20 min selected study. Optional mathematical/video fallback; a full university course is outside this week.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Trace `[2, 5, 8]` token states into `[2, 8]` sentence vectors. Identify the token axis, batch axis, and padding mask before taking a mean. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-02.md).

## Debugging scenario

A service returns one vector for a batch of 20 documents. What axis error could explain it?

## Knowledge check

1. Which values are learned parameters?
2. Why can a token have multiple contextual representations?
3. Why is a pooled hidden state not automatically a good retriever?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](../../module-01-training-tokenization/lectures/lecture-02-tokenization-context-budgets-and-truncation.md) · [Next](lecture-04-self-attention-causal-masks-and-transformer-blocks.md)
