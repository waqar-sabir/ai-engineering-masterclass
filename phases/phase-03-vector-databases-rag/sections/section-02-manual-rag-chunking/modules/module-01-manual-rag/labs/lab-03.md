# Lab 03 — Manual RAG and cited-answer contract

[Phase home](../../../../../README.md) · [Module](../README.md)

## Objectives and prerequisites

Specify retrieval → context → generation → validation without a framework. Complete the owning module lectures and carry forward relevant Phase 1–2 contracts. Guided allocation: 75 minutes. Material status: In Review; all execution and implementation: Planned.

## Tools, dependencies, and setup

Python typing/JSON/Pydantic knowledge; later fake provider and local vectors; a live generation adapter is optional until implementation review.

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

1. Define Question, RetrievedChunk, CitedClaim, and AnswerResult contracts. Separate answered, insufficient_evidence, conflict, and error outcomes.
2. Create fixed retrieved chunks with labels C1/C2 and source versions/locators. Build context using those labels and bounded source text.
3. Design the instruction policy: answer only from supplied evidence, preserve uncertainty, treat source text as untrusted.
4. Use a fake generator result to trace a supported claim, an unknown citation, empty retrieval, and a refusal/error.
5. Require deterministic citation membership and nonempty evidence for answered outcomes. Plan a separate semantic-support review.
6. Submit an orchestration diagram and expected outcomes; do not claim fake output proves real model grounding.

## Educational example

```python
available = {"C1", "C2"}
claim = {"text": "Notice is required.", "citations": ["C1"]}
assert set(claim["citations"]) <= available
unknown = {"C9"} - available
assert unknown == {"C9"}
# Membership checks do not prove that C1 supports the claim.
```

This fragment illustrates the mechanism; it is not a bundled project implementation.

## Commands and test plan

After the learner creates the experiment and tests in their own workspace:

```sh
python experiments/lab_03.py
python -m pytest tests/test_lab_03.py -q
```

These files are future learner tasks, not files shipped here. Lab 10 can use only the capacity example as its Python fragment; its main submission is the design document.

## Expected output

A typed evidence/answer design, labeled context example, and failure test plan. Unknown labels fail; empty evidence cannot become a fabricated answered result.

## Common errors and troubleshooting

If valid citation IDs accompany an unsupported statement, inspect actual source text. If a provider fails, return a typed error rather than an insufficient-evidence success.

## Acceptance criteria

- [ ] Numbered tasks have reviewable artifacts and an independent counterexample.
- [ ] Correct behavior and failure behavior are specified separately.
- [ ] Any later run records actual versions, inputs, and observed output; no invented result.
- [ ] No credentials, private documents, destructive shared-collection operations, or unreviewed downloads.
- [ ] Limitations are explicit; pending implementation is not marked complete.

## Assignment and assessment

Submit the artifact and one original failure example, then attempt the [module assessment](../assessments/knowledge-check.md). Carry the contract into the [Enterprise Knowledge Assistant specification](../../../../../project/README.md).
