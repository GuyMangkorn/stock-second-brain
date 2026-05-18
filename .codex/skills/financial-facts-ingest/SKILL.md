---
name: financial-facts-ingest
description: Ingest source notes, filings, transcripts, financial tables, Markdown, or CSV into Obsidian financial facts and entity pages without inventing missing values.
---

# Financial Facts Ingest

Use this skill to normalize source-backed company facts into the
`stock-second-brain` vault.

## Non-Negotiables

- Never make up financial values, segment labels, period labels, or denominator
  assumptions.
- If a value cannot be verified, write `ไม่พบข้อมูลที่ยืนยันได้`.
- Every number must trace back to a source path, URL, or explicit calculation.
- Derive reporting scope from source titles, headers, tables, or filing periods.
- Support `annual`, `quarterly`, or `mixed` output when the source supports it.

## Required References

Read these before writing durable output:

- `wiki/reference/source-hierarchy.md`
- `wiki/reference/output-contract.md`
- `wiki/reference/financial-ratios.md`
- `wiki/reference/chart-conventions.md`
- `wiki/reference/entity-template.md`

Follow the output contract's language standard. Keep structured fields,
financial tables, JSON keys, headings, and metric labels in English; use Thai
mainly for explanatory notes, missing-data explanations, thesis commentary, and
judgment sections.

## Required Workflow

1. Confirm the input file exists or the source URL is accessible.
2. Identify ticker, company name, market, currency, period type, reporting
   scope, and period labels.
3. Extract financial facts into source-declared periods.
4. Record provenance for each extracted block.
5. Compute only ratios whose inputs are complete and period-compatible.
6. Write or update:
   - `raw/financials/TICKER_fundamentals.md`
   - optional `raw/financials/TICKER_fundamentals.json`
   - `wiki/entities/TICKER.md`
   - `log.md`
7. Keep entity pages idempotent: update existing sections instead of duplicating
   them.
8. Audit for unsupported numbers before finishing.

## Markdown Output Sections

`raw/financials/TICKER_fundamentals.md` should contain:

- `## Snapshot`
- `## Provenance`
- `## Reporting Scope`
- `## Financial Table`
- `## Key Ratios`
- `## Quarterly YoY Comparison` when same-quarter data exists
- `## Quarterly Trend` when sequential quarterly data exists
- `## YTD Comparison` when year-to-date comparable periods exist
- `## Annual Trend` when complete fiscal-year data exists
- `## Segment Revenue Chart`
- `## Cash Flow And Capex Chart` when cash flow data exists
- `## Balance Sheet Snapshot Chart` when balance sheet snapshots exist
- `## Missing / Unverified Data`

## Chart Rules

- Plot every comparable verified dataset that helps compare quarters or years.
- Keep single-quarter, year-to-date, annual, and balance-sheet snapshot periods
  in separate charts.
- Do not mix `FY26 Q3` with `9M FY26` or full-year `FY2026` in the same chart
  unless the chart title explicitly says it is a mixed-scope chart. Prefer
  separate charts.
- For same-quarter comparisons, use labels like `FY25 Q3` and `FY26 Q3`.
- For annual trends, use only complete fiscal years such as `FY2023`, `FY2024`,
  and `FY2025`.
- Use source labels exactly as reported.
- If there is no comparable data, write a short note under
  `Missing / Unverified Data` instead of drawing a placeholder chart.

## Entity Update Rules

Update `wiki/entities/TICKER.md` with:

- source map
- latest verified period
- financial facts summary
- chart blocks or chart links for comparable quarterly, YTD, annual, segment,
  cash-flow, and balance-sheet data
- transcript or management commentary summary when relevant
- missing/unverified data
- links to raw source note and normalized financial facts
- follow-up items

## Stop Conditions

Stop and report gaps when:

- input file is missing
- ticker is ambiguous
- units or currency are unclear
- ratio inputs are incomplete
- source data conflicts and cannot be resolved
- segment taxonomy makes comparison unsafe
