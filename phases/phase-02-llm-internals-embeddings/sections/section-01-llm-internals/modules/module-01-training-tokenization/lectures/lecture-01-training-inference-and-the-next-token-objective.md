# Lecture 01 — Training, inference, and the next-token objective

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L01 · Day 8 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Separate learned weights from request-time context.
- Explain pretraining, adaptation, and inference at an engineering level.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Review vector notation in the math primer when needed. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Separate learned weights from request-time context.
- Explain pretraining, adaptation, and inference at an engineering level.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

A generative language model estimates a distribution over the next token, conditioned on earlier tokens. Training changes parameters to reduce prediction loss across examples. During ordinary inference, a forward pass uses existing parameters; user prompts and conversation state are inputs, not weight updates. An application may persist messages outside the model, but that is a separate storage decision.

Pretraining learns broad patterns. Supervised adaptation and preference optimization alter behavior through additional training. Do not confuse these with providing an example in a prompt. Phase 8 studies adaptation; Phase 2 only establishes the distinction. A useful loss intuition is `L = -sum(log p(target_token | prefix)) / token_count`: a confidently wrong prediction is penalized more than a mildly wrong one.

Inference has a prompt-processing stage and iterative generation. A KV cache retains intermediate attention keys/values to avoid recomputing the entire prefix at every generated step; it is neither durable user memory nor a cache of verified answers. Longer inputs and outputs affect different parts of latency. Quality, throughput, memory, and context limits remain workload-dependent.

## Practical example and walkthrough

For a company-summary request, identify which information came from fixed parameters, supplied source text, application storage, or a generated guess. A follow-up message does not imply that the model learned the company permanently.

Draw pretraining → model artifact → inference and label every location where weights change.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [How do Transformers work?](https://huggingface.co/learn/llm-course/en/chapter1/4) — Hugging Face course; Training, transfer learning, and architecture sections; 20 min selected study. Grounds model lifecycle terminology; skip model-release chronology.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Original research paper; Sections 3.1–3.3 in linked PDF; 25 min selected study. Optional historical architecture reference; modern models vary.
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/) — University syllabus and lecture links; Word vectors, neural networks, and Transformers selections; 20 min selected study. Optional mathematical/video fallback; a full university course is outside this week.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Draw pretraining → model artifact → inference and label every location where weights change. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-01.md).

## Debugging scenario

If an application claims a model learned yesterday’s private document after one prompt, which boundaries must you inspect?

## Knowledge check

1. What changes in training but normally not inference?
2. How does next-token loss differ from factual correctness?
3. Why is a KV cache not long-term memory?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](../../../../../../phase-01-python-llm-foundations/README.md) · [Next](lecture-02-tokenization-context-budgets-and-truncation.md)
