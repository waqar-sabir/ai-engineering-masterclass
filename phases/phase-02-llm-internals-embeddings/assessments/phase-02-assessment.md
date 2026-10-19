# Phase 2 comprehensive assessment

Materials: Approved. Learner submission and score: Planned. Attempt this page before opening the solution guide. Total: 100 points; pass at 75/100 with at least 20/35 on the practical task and no exposed credential/private data.

## Comprehensive quiz — 20 points

Ten questions, 2 points each. For open responses, award one point for the correct mechanism and one for a concrete consequence or example.

1. During ordinary inference, what normally changes? A. Model weights after every message. B. Input/context and activations. C. The tokenizer vocabulary. D. The training objective.
2. Token IDs should be treated as: A. Semantic coordinates. B. Calibrated probabilities. C. Vocabulary labels. D. Universal word counts.
3. What are the two main consequences of silently truncating a search document?
4. Q has shape [3,4] and K has shape [5,4]. What shape is QKᵀ, and what does a causal mask control?
5. For nonzero unit vectors, which is true? A. Dot equals cosine. B. Cosine is always nonnegative. C. Distance sorts descending. D. Dimensionality determines relevance.
6. Why is cosine undefined for a zero vector, and what should the application do?
7. Two 384-dimensional encoders can be mixed because shapes match. True or false? Justify.
8. What records preserve document/vector identity and model reproducibility in a snapshot?
9. Relevant IDs are {a,c}; ranked IDs are [b,c,a]. Compute Recall@2 and reciprocal rank.
10. How should queries with no relevant corpus document be handled in a recall report?

## Practical assessment — 35 points

Specify and later implement `search(snapshot, query_vector, k)` plus a snapshot loader. Use hand-authored vectors and an injected encoder for tests; a real model is not required for this coding assessment.

- Typed input and manifest contracts, finite numeric validation, nonempty corpus, valid k, and explicit clamp policy: 7 points.
- Dimension/normalization checks, zero-vector rejection, correct scoring direction, and stable document-ID ties: 8 points.
- Exact document/vector row identity, compatible model revision/policy, and fail-closed corrupt snapshot handling: 7 points.
- Tests for success, scaled vectors, ties, NaN/zero/dimension failure, bad row order, and incompatible manifest: 9 points.
- Clear result contract, original snippets/IDs, versions, and readable explanation: 4 points.

At the materials stage, this is an assignment specification. Do not report coding points as earned from a design-only submission.

## Debugging scenarios — 15 points

Five points each: root cause 2, safe fix 2, regression check 1.

1. A new query encoder deploys while the corpus still uses an older unrelated encoder, both width 384. No type errors occur, but retrieval quality collapses.
2. Search returns the correct top document ID with another document’s text after a batch job sorts metadata alphabetically.
3. A metric report improves after no-result and difficult queries disappear from the denominator; the team also tunes a threshold repeatedly against the held-out set.

## System design challenge — 20 points

Design the versioned local embedding/search service and a credible path toward 100,000 documents. Include offline/online paths and a Mermaid diagram (4), contracts/activation/rollback (4), capacity assumptions and a measurement plan (4), failure isolation and privacy/deletion policy (4), and exact-search alternatives/trade-offs without premature infrastructure claims (4).

## Project submission — 10 points

- Reproducible setup and model/corpus manifest: 2.
- Test specifications plus later executed evidence: 2.
- Frozen-query evaluation and lexical baseline, with failures preserved: 2.
- Architecture, capacity assumptions, and privacy limitations: 2.
- Normal and failed-query demonstrations plus honest readiness checklist: 2.

The project’s standalone quality rubric is separate from this submission component. No retrieval benchmark target is invented.

## Submission and review

Submit quiz answers, practical work and test evidence, debugging analysis, design record, and project artifacts. Record actual execution/model versions separately from proposed steps. A missing implementation or unrun project test remains incomplete, even when the teaching material is ready.

Review the separate solution guide after attempting the tasks. Phase 3 generation requires an explicit user instruction; material readiness does not imply learner mastery.
