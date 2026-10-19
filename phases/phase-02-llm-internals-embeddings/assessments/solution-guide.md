# Phase 2 assessment solution guide

Attempt the assessment first. These are scoring anchors, not learner results or a bundled project implementation.

## Quiz key — 20 points

1. B. Inputs/context and activations vary; ordinary inference does not update model parameters.
2. C. IDs label entries in a tokenizer vocabulary; numerical ID differences do not measure meaning.
3. Relevant content can be removed, and the stored representation can silently differ from what the user believes was searched. Reject over-budget documents or apply an explicit policy; this phase defers chunking.
4. [3,5]. A causal mask controls which key positions each query position may attend to, preventing future-position leakage for autoregressive use.
5. A. Unit-vector dot product equals cosine; maximizing it agrees with minimizing squared Euclidean distance under the stated normalization.
6. Its norm is zero, so the cosine denominator is zero. Reject it or expose an explicit invalid-representation outcome, rather than allowing NaN scores into ranking.
7. False. Geometry depends on compatible model/revision, role/prompt, pooling, and preprocessing policies; equal dimensions do not establish compatibility.
8. Stable ordered document IDs and corpus digest bind rows to content; a manifest records model/tokenizer revisions, dimension, dtype, normalization, role/pooling, preprocessing, and snapshot identity.
9. Recall@2 = 1/2; reciprocal rank = 1/2 because the first relevant item is second.
10. Their recall is undefined; count/report them separately, with the chosen no-relevant behavior. Answerable queries with no relevant hit remain in the eligible set with zero recall/RR. Never silently drop failures.

## Practical solution characteristics — 35 points

Validate all artifact dimensions and ID mappings before serving a query. Reject non-finite values and zero norms. Enforce compatible embedding contracts, normalize deliberately, score correctly, and sort with stable ties. Clamp valid k to corpus size and record the actual return count. Join output text by stable ID, not an accidentally shuffled position.

Use deterministic hand-vector fixtures for arithmetic and identity tests. Include one invalid case per boundary. Test that an incomplete or mismatched snapshot does not replace a known-good generation. Do not repair incompatible model vectors by padding, truncating, or normalizing them into apparent compatibility.

A fake encoder tests application contracts; a separate real encoder run evaluates model behavior. A solution that only returns a ranked list but skips contract and artifact checks cannot receive full marks.

## Debugging guidance — 15 points

1. Equal width hid a geometry mismatch. Restore a coordinated query/corpus snapshot, re-encode the candidate corpus, and reject manifest mismatches before scoring. Regression: same-width incompatible revisions fail visibly.
2. Document/vector alignment was broken by an independent sort. Restore immutable ID-to-row identity and join snippets by the validated IDs. Regression: a controlled metadata permutation fails validation or still maps every ID to the correct text.
3. The report removed failures and leaked held-out feedback into tuning. Restore the full declared query set and metric rules; relabel the repeatedly consulted set development and obtain a fresh held-out set. Regression: fixed eligible-query counts, missing-result zeros, separate no-relevant counts, and versioned labels.

## System design scoring anchors — 20 points

0–5: only a model call and vague storage diagram. 6–10: separated build/query paths and basic exact ranking. 11–15: manifest integrity, atomic activation, bounded workloads, privacy, and failure handling. 16–20: clear arithmetic assumptions, measurement design, rollback/deletion policy, coordinated migration, and justified alternatives without unsupported scale claims.

For 100,000 vectors at width 384 and float32, raw vectors are 153,600,000 bytes, about 146.48 MiB; this excludes weights, metadata, temporary copies, and concurrent query work. This number is not a measured memory or latency result.

## Project review anchors — 10 points

Evidence must identify the corpus, query split, model revision, artifact contract, executed tests, actual rankings, and measurement method. No-result cases and failures stay visible. A well-described low score can be a useful baseline; a fabricated high score is not acceptable. Review setup and failure demonstrations in addition to the happy path.
