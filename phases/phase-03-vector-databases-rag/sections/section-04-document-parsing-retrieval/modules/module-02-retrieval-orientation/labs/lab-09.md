# Lab 09 — Retrieval variants and candidate-coverage worksheet

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Inspect rewriting, filtering, fusion, and reranking without building the Phase 4 stack. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Paper/JSON fixtures, Python standard library, and current retrieval documentation; optional later retriever implementation.

These are future learner instructions. Do not add exercise dependencies or application files to the course repository during material preparation. No service, parser model, vector index, provider call, or app has been executed for this package. Create a separate learner workspace when implementation is explicitly requested.

```text
learner-phase-03/
  notes/
  data/sources/
  experiments/
  tests/
  artifacts/
  reports/
```

For a later local exercise, create a virtual environment and install only the named packages after reviewing current publisher requirements. Record resolved versions and model/parser revisions.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install pytest
# Add only this lab's required packages during the later implementation pass.
```

## Step-by-step instructions

1. Use a fixed tiny corpus with a paraphrase question, an exact identifier, and category metadata.
2. Compare original and rewritten queries; reject rewrites that discard the identifier or add unsupported intent.
3. Apply one explicit category filter and list the eligible IDs before ranking. Treat it as relevance scoping, not production authorization.
4. Compute reciprocal-rank fusion for two fixed rankings with c=60. Deduplicate IDs and state tie/missing-ID policies.
5. Simulate reranking only the returned candidate set. Show a relevant missing candidate that cannot be recovered.
6. Propose a controlled development experiment and latency measurement plan. Full hybrid/reranker implementation and tuning are Phase 4 extensions.

## Educational example

```python
rankings = [["a", "b", "c"], ["d", "b", "a"]]
scores = {}
for ranking in rankings:
    for rank, doc_id in enumerate(ranking, 1):
        scores[doc_id] = scores.get(doc_id, 0) + 1 / (60 + rank)
fused = sorted(scores, key=lambda key: (-scores[key], key))
print(fused)  # ['a', 'b', 'd', 'c'] for this fixed fixture.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_09.py
python -m pytest tests/test_lab_09.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A rewrite/filter/fusion/rerank worksheet, not a quality benchmark. With these lists a narrowly outranks b; neither stage invents documents absent from the candidates.

## Common errors and troubleshooting

Do not sum dense and sparse raw scores without a justified calibration. If filters eliminate relevant evidence, inspect field types and missing values. Never call a reranker a substitute for initial recall.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
