# Lab 10 — Knowledge assistant architecture and readiness review

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Integrate ingestion, query, citation, capacity, failure, and evaluation contracts. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 45 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Markdown/Mermaid editor, calculator, phase case study, and project specification; no deployed infrastructure.

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

1. Draw separate ingestion and query paths with candidate-generation activation and source/citation lookup.
2. Define whole-generation success and explicit source failure/needs-review status. Explain how a failed rebuild preserves a prior valid generation.
3. Calculate raw vector storage for 100 sources × 20 chunks × 384 dimensions × 4 bytes. List omitted memory and storage components.
4. Plan stage-level evaluation for parsing, retrieval, context coverage, answer support, citation integrity, and abstention.
5. Review source deletion, redacted telemetry, local-single-user scope, and the production controls reserved for later phases.
6. Submit a diagram, capacity worksheet, failure table, and handoff checklist. Mark all live/implementation evidence unexecuted for now.

## Educational example

```python
sources, chunks_each, dim, bytes_each = 100, 20, 384, 4
raw = sources * chunks_each * dim * bytes_each
print(raw)  # 3072000 bytes, about 2.93 MiB of vectors only.
context_tokens = 5 * 180
print(context_tokens)  # 900 source tokens before labels/instructions/question.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_10.py
python -m pytest tests/test_lab_10.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A complete architecture review package with clearly labeled estimates and unmeasured targets. No production deployment, security property, or latency SLO is claimed achieved.

## Common errors and troubleshooting

A source count alone understates chunk/index storage. Valid citations can still misrepresent evidence. If an ingestion failure disappears from the report, the pipeline’s success status is misleading.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
