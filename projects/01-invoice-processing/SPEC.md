# Invoice Processing Workflow — Phase 1 lab specification

Material status: In Review. Implementation: Planned.

[Lab 4 instructions](../../phases/phase-01-python-llm-foundations/sections/section-03-llm-apis-contracts-prompts/modules/module-02-structured-output-tool-contracts/labs/lab-04.md) · [Phase 1](../../phases/phase-01-python-llm-foundations/README.md)

**Time:** 2h 15m\
**Purpose:** Integrate Python, model I/O, Pydantic, structured output, and domain validation. This is Project 1 from the extended portfolio list, scoped to Phase 1.

**Mandatory MVP:** Extract from supplied invoice text. **Optional extension:** send a PDF/image to a vision-capable model after checking provider documentation and data-handling requirements.

## Contract

- Input: invoice text plus `document_id`.
- Output: vendor, invoice number, issue/due dates, currency, line items, subtotal, tax, total, missing fields, arithmetic status, and warnings.
- Rules: currency must be a 3-letter code; quantities/prices are non-negative; recompute subtotal and total with `Decimal`; never use binary float for money; flag rather than invent missing values.

## Suggested structure

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

## Steps

1. Create strict Pydantic models using `Decimal` and `date`.
2. Write instructions that prohibit guessing and require `missing_fields`.
3. Request structured output from the provider and parse it.
4. Independently recompute arithmetic; do not ask the model to be the source of truth.
5. Add fixtures: valid invoice, missing tax, incorrect stated total, duplicate invoice number, adversarial instruction inside invoice text.
6. Test with a fake provider first, then one real call.

**Expected outputs:** Valid invoice → `arithmetic_status="valid"`; incorrect total → `arithmetic_status="mismatch"` with expected total; absent due date → field is null and listed in `missing_fields`.

**Common errors:** float rounding (use `Decimal`); schema too complex (simplify nesting); date ambiguity (preserve uncertainty or require ISO); invoice text says “ignore instructions” (treat it as data, not authority).

**Acceptance criteria:** All fixtures produce valid contracts; arithmetic is deterministic; adversarial text cannot change the output schema or reveal secrets; README distinguishes extraction from verification.

## Business requirements

Extract a reviewable invoice record from supplied text, preserve missing fields, and distinguish extraction from arithmetic verification. Use synthetic invoices and never invent absent data.

## Architecture and technology

Text input → versioned prompt → provider adapter → Pydantic contract → deterministic Decimal validator → JSON result. Python 3.12+, Pydantic, Decimal, an optional model SDK, and pytest are planned learner tools.

## Data storage and API

No database or HTTP service is required. Persist local sanitized artifacts only. Input is document_id plus text; output follows the contract above. Duplicate invoice-number detection requires an explicit supplied batch or session history; one isolated extraction cannot detect global duplicates.

## Testing and evaluation

Test shape/type validity separately from arithmetic, source consistency, missing-field handling, and adversarial-input behavior. Fake-provider tests establish application behavior only. A later live test is needed to assess extraction quality; do not claim injection immunity from a fake fixture.

## Security, deployment, and trade-offs

Keep invoice text out of logs, use synthetic data, and redact credentials. Local execution is sufficient. Vision, OCR, database persistence, duplicate-payment detection, deployment, and production approval workflows are outside this mandatory text-only lab.

## Completion criteria

The lab rubric governs future learner completion. No extraction code, test results, or live outputs are included at this materials stage.
