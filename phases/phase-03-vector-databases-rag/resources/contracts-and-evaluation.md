# Phase 3 contracts and evaluation primer

## Source-to-answer identity chain

Source ID/version → normalized blocks and format-specific locators → chunk ID/policy → supported point ID and encoder contract → active collection/generation → retrieved evidence labels → cited claims → original source rendering. A failure at any join can create a plausible but wrong source display.

## Format locators

- PDF: source version, stated page-number convention, and block/table locator when preserved.
- DOCX: source version plus heading/block/paragraph path; no invented page number.
- TXT: source version and line range under a stated newline/normalization policy.
- CSV: source version, row ID/range, and column-header context; preserve quoted delimiters.

## Chunk arithmetic

For a simple sliding window, estimated count is `1 + ceil(max(0,L-c)/(c-o))` when the input is nonempty and `0 <= o < c`. Empty input must have its own policy. For L=1000, c=200, o=40, the estimate is 6; recursive splitter boundaries can differ. Length units must be explicit and final encoder tokens rechecked.

## Retrieval metrics and evidence units

ANN neighbor recall compares approximate to exact vector neighbors; task relevance compares to human-labeled evidence. Chunk Recall@k requires labels aligned with the exact chunk policy. If chunking changes, use stable source-passage labels or relabel the chunks rather than comparing unrelated chunk IDs.

## Citation integrity versus answer support

Citation integrity: every supplied label resolves to a retrieved chunk and source version with a valid locator. Answer support: the cited text actually supports the claim, including exceptions, time scope, and uncertainty. A structurally valid citation can accompany a false claim. Separate these checks in evaluation and never treat a schema as a fact checker.

## Evaluation record template

For each query, record its split, question, relevant source passages, retrieved chunks/scores, selected context, answer status/claims/citations, support review, known failures, generation/model/prompt/schema IDs, and actual stage timings if executed. Leave observed results blank until measured. Do not treat fake-provider outputs as a real-model benchmark.

## Capacity example

100 × 20 × 384 × 4 = 3,072,000 bytes, about 2.93 MiB of raw float32 vectors. Index/payload/model/parser/candidate-generation memory is additional. Five context chunks of 180 tokens consume 900 source tokens before labels, instructions, the question, and output reserve. Encoder and generator token budgets are different contracts.
