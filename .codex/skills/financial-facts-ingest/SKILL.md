---
name: financial-facts-ingest
description: Use when the user asks to ingest or normalize a source note, filing, transcript, financial table, Markdown file, CSV, or verified company facts into the stock-second-brain vault.
---

# Financial Facts Ingest

## Required References

Read `source-hierarchy.md`, `output-contract.md`, `financial-ratios.md`,
`chart-conventions.md`, and `entity-template.md` from `wiki/reference/`.

## Non-Negotiables

- Never invent values, period labels, segments, units, or denominators.
- Trace every number to a source path, URL, or shown calculation.
- Compute only complete, period-compatible ratios.
- Put market quotes outside normalized company facts.

## Workflow

1. Confirm the input exists or is accessible and identify ticker, company,
   market, currency, scope, units, and source periods.
2. Normalize verified facts into source-declared periods and record provenance
   once per source block.
3. Write or update `raw/financials/TICKER_fundamentals.md`.
4. Create `TICKER_fundamentals.json` only when the user requests it or a named
   downstream machine workflow requires it.
5. Update `wiki/entities/TICKER.md` once using the thin entity template and only
   changed sections. Link the fundamentals table and chart rather than copying.
6. Add the single most decision-relevant chart in `lean`; add at most three in
   `full`. Omit unsupported chart sections.
7. Audit unsupported numbers and append one workflow bullet to `log.md`.

## Fundamentals Shape

Required:

- `Snapshot`
- `Provenance`
- `Reporting Scope`
- `Financial Table`
- supported `Key Ratios`
- normalization-specific `Missing / Unverified Data`

Add a quarterly, YTD, annual, segment, cash-flow, or balance-sheet comparison
only when the periods are compatible. The table is the source of truth; a chart
is a view.

## Entity Delta

Update latest period, compact financial read, thesis-relevant management
commentary, report links, follow-up, and unresolved ticker-level gaps. Keep new
lean narrative between 250 and 400 words. Detailed numbers remain in
fundamentals.

## Stop Conditions

Stop on missing input, ambiguous ticker, unclear units/currency, incompatible
ratio periods, unresolved source conflict, or unsafe segment comparison. Record
the gap instead of forcing normalization.
