# Phase 2 math primer

## Shapes and products

Use row-vector convention consistently. A document matrix has shape `[N,d]`; a query vector has `[d]`. `D @ q` yields one score for each document. `Q @ K.T` in attention instead compares token positions. Label axes before calculating.

## Norm and cosine

For `a = [3,4]`, norm is 5 and the unit vector is `[0.6,0.8]`. For `b = [1,0]`, dot product is 3, cosine is 0.6, and Euclidean distance is `sqrt(20)`. Normalization divides by the norm; it is undefined for a zero vector. Reject non-finite values before attempting normalization.

## Softmax and masking

Subtract the largest allowed logit before exponentiating to improve numerical stability. For logits `[0,0]`, weights are `[0.5,0.5]`. Masking the second entry before softmax yields `[1,0]`. A row with no allowed entries needs an explicit failure or masking policy, rather than allowing NaN propagation.

## Retrieval example

Relevant IDs: `{a,c}`. Ranked IDs: `[b,c,a]`. Recall@1 = 0, Recall@2 = 1/2, Recall@3 = 1. Reciprocal rank = 1/2. A query with no relevant corpus document has undefined recall and belongs in a separately reported no-relevant slice.

## Capacity example

10,000 × 384 × 4 float32 bytes = 15,360,000 bytes = about 14.65 MiB for vectors only. Do not include model weights, text records, temporary arrays, or operating-system overhead in that number. No latency result is implied.

## Review

Calculate the same quantities for `[0,1]`, an opposite vector, and a zero vector. Explain each boundary case before using a library.
