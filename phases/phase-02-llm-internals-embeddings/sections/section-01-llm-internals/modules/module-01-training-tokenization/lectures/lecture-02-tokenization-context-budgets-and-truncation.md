# Lecture 02 — Tokenization, context budgets, and truncation

[Phase home](../../../../../README.md) · [Module](../README.md)

## Lecture metadata

ID: P02-L02 · Day 8 · Guided study: 40 minutes · Difficulty: Intermediate.

Material status: Approved. Learner completion: Planned. Time includes these notes and the worked example; resource selection time is budgeted separately in the study plan.

## Learning objectives

- Explain subword tokens and special-token overhead.
- Identify truncation and tokenizer/model compatibility failures.

## Prerequisites

Phase 1 typed Python, API contracts, and validation concepts. Complete the preceding Phase 2 lecture. [Math primer](../../../../../resources/math-primer.md).

## Lecture syllabus

- Explain subword tokens and special-token overhead.
- Identify truncation and tokenizer/model compatibility failures.
- Work through the example, distinguish assumptions from measurements, and complete the module lab.

## Core learning material

Tokenization maps text to discrete IDs using a model-specific vocabulary and preprocessing rules. Tokens can represent words, word fragments, punctuation, or byte sequences. Their numeric IDs are category labels, not measurements of meaning; subtracting token IDs does not measure semantic distance. Encoding and decoding also involve whitespace, normalization, and special-token conventions.

A sequence enters an embedding lookup before contextual processing. Keep vocabulary/tokenizer version aligned with the model. A tokenizer mismatch may produce syntactically valid IDs with the wrong interpretation. Padding fills a batch to a common shape; attention masks prevent padded positions from participating where appropriate. Truncation removes real content and needs an explicit policy.

Count actual tokens instead of assuming a fixed words-to-tokens ratio. Reserve space for instructions, formatting overhead, and generated output. Encoder input limits differ from generation context limits. For the Phase 2 corpus, reject documents beyond the chosen encoder budget rather than silently dropping their ending. Phase 3 will teach chunking.

## Practical example and walkthrough

A 90-word document can tokenize differently from a 90-word code sample or Urdu text. If an important cancellation policy is at the end of a long document, silent truncation can hide the only relevant evidence.

Create four strings: prose, punctuation-heavy code, accented text, and mixed-language text. Record character count, token count, special tokens, and truncation behavior.

This is instructional material for future learner work. No application implementation or model run is included.

## Learning resources

Required selections (free to read; durations are course estimates):

- [Tokenizers](https://huggingface.co/learn/llm-course/en/chapter2/4) — Hugging Face course/documentation; Subword tokenization and encoding/decoding; 20 min selected study. Explains the tokenization boundary and special tokens.

Optional supplementary/fallback selections (free to read; skip unless needed):

- [Byte-Pair Encoding tokenization](https://huggingface.co/learn/llm-course/en/chapter6/5) — Hugging Face tutorial; The merge algorithm and examples; 20 min selected study. Optional deeper explanation of vocabulary construction.
- [all-MiniLM-L6-v2 model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — Publisher model card; Intended uses, dimensionality, truncation, and usage; 15 min selected study. A concrete short-text baseline with documented limits, not a universal recommendation.

Video alternative: [Stanford CS224N lecture playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D), selected through the [university syllabus](https://web.stanford.edu/class/cs224n/). Use a relevant word-vector/neural-network/Transformer segment for background; for implementation-specific topics, the official documentation above is primary. Optional 15–20 minute selection replaces extra reading; do not watch the full playlist this week.

## Independent exercise

Create four strings: prose, punctuation-heavy code, accented text, and mixed-language text. Record character count, token count, special tokens, and truncation behavior. Record the input, intermediate shapes or decisions, and expected failure behavior in a short learner note. Then connect the result to [the module lab](../labs/lab-01.md).

## Debugging scenario

Why does character-length validation fail to protect an embedding model’s input budget?

## Knowledge check

1. Are token IDs semantic coordinates?
2. How do padding and truncation differ?
3. Which tokenizer metadata belongs in a reproducibility record?

## Completion criteria

- [ ] Explain both learning objectives without relying on library names.
- [ ] Produce the worked example or decision artifact and explain the failure scenario.
- [ ] Complete the [module assessment](../assessments/knowledge-check.md) before reading its solution guidance.

## Next lecture

[Previous](lecture-01-training-inference-and-the-next-token-objective.md) · [Next](../../module-02-neural-networks-attention/lectures/lecture-03-neural-networks-tensor-shapes-and-representations.md)
