# Lab 04 — Invoice Processing Workflow MVP

[Phase home](../../../../../README.md) · [Module](../README.md)

Status: Approved (instructions). Learner execution: Planned.

## Objectives and prerequisites

Complete the owning module lectures, have Python 3.12+ available, and review the resource list. Submit reproducible evidence for the behavior described below.

## Setup and dependencies

Use a separate learner workspace when you begin implementation. The repository currently contains materials only. The commands below describe the future exercise; they have not been run as a live model integration. Do not install exercise dependencies into the repository tooling environment.

For Labs 2–4, reuse the learner package established in Lab 1. Add only the dependencies listed in the exercise and keep your own lockfile. Commands are suggestions, not bundled executables.

## Commands and implementation steps

**Time:** 2h 15m\
**Purpose:** Integrate Python, model I/O, Pydantic, structured output, and domain validation. This is Project 1 from the extended portfolio list, scoped to Phase 1.

**Mandatory MVP:** Extract from supplied invoice text. **Optional extension:** send a PDF/image to a vision-capable model after checking provider documentation and data-handling requirements.

### Contract

- Input: invoice text plus `document_id`.
- Output: vendor, invoice number, issue/due dates, currency, line items, subtotal, tax, total, missing fields, arithmetic status, and warnings.
- Rules: currency must be a 3-letter code; quantities/prices are non-negative; recompute subtotal and total with `Decimal`; never use binary float for money; flag rather than invent missing values.

### Suggested structure

```text
src/invoice_workflow/
├── models.py
├── prompt.py
├── extractor.py
├── validators.py
└── cli.py
tests/invoice_workflow/
├── fixtures/
├── test_extractor.py
└── test_validators.py
```

### Steps

1. Create strict Pydantic models using `Decimal` and `date`.
2. Write instructions that prohibit guessing and require `missing_fields`.
3. Request structured output from the provider and parse it.
4. Independently recompute arithmetic; do not ask the model to be the source of truth.
5. Add fixtures: valid invoice, missing tax, incorrect stated total, duplicate invoice number, adversarial instruction inside invoice text.
6. Test with a fake provider first, then one real call.

**Expected outputs:** Valid invoice → `arithmetic_status="valid"`; incorrect total → `arithmetic_status="mismatch"` with expected total; absent due date → field is null and listed in `missing_fields`.

**Common errors:** float rounding (use `Decimal`); schema too complex (simplify nesting); date ambiguity (preserve uncertainty or require ISO); invoice text says “ignore instructions” (treat it as data, not authority).

**Acceptance criteria:** All fixtures produce valid contracts; arithmetic is deterministic; adversarial text cannot change the output schema or reveal secrets; README distinguishes extraction from verification.

## Expected output and test plan

Use synthetic fixtures for valid amounts, missing tax, wrong stated total, repeated invoice number, and embedded hostile instructions. Assert deterministic arithmetic separately from extraction quality.

## Troubleshooting

Check the working directory, active environment, dependency versions, timeout configuration, and field names before changing prompts. Use fake providers and mocked HTTP to isolate domain failures. Redact credentials and private payloads from error reports.

## Acceptance criteria and submission

- [ ] Exercise-specific acceptance criteria above demonstrated.
- [ ] Tests and sanitized output captured in the learner submission.
- [ ] Failure behavior demonstrated without hiding invalid output.
- [ ] No secrets or real private invoices committed.
- [ ] Limitations explained in the learner README.

Connect the work to the [project specification](../../../../../../../projects/01-invoice-processing/SPEC.md). A successful fake test verifies application behavior; it does not prove live model quality or prompt-injection resistance.
