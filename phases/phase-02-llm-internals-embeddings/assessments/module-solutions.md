# Phase 2 module solutions

Attempt the module assessments first. These are review anchors; no learner score or execution result is claimed.

## Module 2.1.1 — Training, inference, and tokenization

MCQ 1: **B**. MCQ 2: **C**. Training updates parameters; request-time messages change inputs. Tokenizer and encoder limits must both be checked.

Conceptual/practical review: use the invariants, counterexamples, and expected outputs from the module lab. The learner should identify the failure before proposing a library or infrastructure change.

Debugging guidance: Inspect whether weights, prompts, and external memory were confused. Tokenizer counts and encoder limits must be checked independently; preserve relevant text or reject it visibly.

## Module 2.1.2 — Neural networks and attention

MCQ 1: **A**. MCQ 2: **B**. The shared feature width contracts; query and key-position axes remain. Causal masking prevents future-position leakage.

Conceptual/practical review: use the invariants, counterexamples, and expected outputs from the module lab. The learner should identify the failure before proposing a library or infrastructure change.

Debugging guidance: A mistaken transpose changes semantic axes even when multiplication succeeds. A missing causal mask can expose future targets; fix the mask and retest token-by-token generation.

## Module 2.2.1 — Representations and geometry

MCQ 1: **C**. MCQ 2: **A**. Identical nonzero directions have cosine one. Unit-vector dot equals cosine; zero vectors remain invalid.

Conceptual/practical review: use the invariants, counterexamples, and expected outputs from the module lab. The learner should identify the failure before proposing a library or infrastructure change.

Debugging guidance: High similarity can occur for contradiction. For wrong top hits, inspect score direction and normalization before changing models; explicitly reject zero/non-finite vectors.

## Module 2.2.2 — Embedding pipeline and persistence

MCQ 1: **D**. MCQ 2: **B**. Geometry depends on the encoder contract, not just array shape. Activate a snapshot only after all files and mappings validate.

Conceptual/practical review: use the invariants, counterexamples, and expected outputs from the module lab. The learner should identify the failure before proposing a library or infrastructure change.

Debugging guidance: A shape match cannot detect a model-revision mismatch. Reject mismatched manifests and ID/vector alignment failures before exposing a snapshot.

## Module 2.2.3 — Model selection and comparison

MCQ 1: **C**. MCQ 2: **B**. Freeze the evaluation inputs. Re-encode the full corpus and coordinate activation; do not mix unrelated embedding spaces.

Conceptual/practical review: use the invariants, counterexamples, and expected outputs from the module lab. The learner should identify the failure before proposing a library or infrastructure change.

Debugging guidance: Hold corpus and relevance judgments fixed. Treat repeatedly consulted test queries as development data and obtain a fresh held-out set. Re-encode fully for migration.

## Module 2.3.1 — Exact search and evaluation

MCQ 1: **B**. MCQ 2: **C**. One of two relevant documents is in the first two positions. Reciprocal rank uses one divided by first relevant rank.

Conceptual/practical review: use the invariants, counterexamples, and expected outputs from the module lab. The learner should identify the failure before proposing a library or infrastructure change.

Debugging guidance: Inspect sorting direction and row identity. Report all fixed queries, correct denominators, and no-relevant cases; do not improve a result by quietly deleting failures.

## Module 2.4.1 — Architecture, capacity, and failure analysis

MCQ 1: **A**. MCQ 2: **D**. The raw array calculation excludes all other memory. Immutable generations preserve coherent reads and permit rollback.

Conceptual/practical review: use the invariants, counterexamples, and expected outputs from the module lab. The learner should identify the failure before proposing a library or infrastructure change.

Debugging guidance: Raw vector bytes do not predict latency or peak memory. Separate measurement from estimates and preserve the previous snapshot if a build fails.
