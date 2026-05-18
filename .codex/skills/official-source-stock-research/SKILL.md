---
name: official-source-stock-research
description: Run official-source stock research for company deep dives, earnings reviews, thesis updates, and Obsidian entity notes using SEC filings, earnings transcripts, financial statements, then news.
---

# Official Source Stock Research

Use this skill for company deep dives, earnings reviews, thesis refreshes,
comparison memos, and ticker research inside `stock-second-brain`.

The output should become durable Obsidian knowledge when the user asks to save,
ingest, update, refresh, compare, audit, or build the stock brain.

## Source Priority

1. SEC filings and official company filings.
2. Earnings transcripts and call materials.
3. Financial statements and metrics.
4. News and web research.

Prefer official Investor Relations pages as discovery surfaces, but trust the
underlying filing, release, transcript, or data table more than a summary page.

## Language Standard

Follow `wiki/reference/output-contract.md`: write narrative thesis, risks,
catalysts, action reads, and caveats primarily in Thai, while preserving English
headings, ticker/source labels, metric names, and finance terms such as `DCF`,
`FCF`, `WACC`, `valuation`, `margin of safety`, and `upside/downside`.

## Research Checklist

Track progress internally:

```text
Official Source Research Progress:
- [ ] Step 1: Identify company, ticker, exchange, currency, and latest period
- [ ] Step 2: Build source map in priority order
- [ ] Step 3: Gather latest filing, transcript/call material, and financial data
- [ ] Step 4: Extract revenue, margins, EPS, cash flow, capex, balance sheet, guidance
- [ ] Step 5: Analyze segment drivers, profitability, capital allocation, and balance sheet
- [ ] Step 6: Extract management commentary and Q&A signals from transcript
- [ ] Step 7: Add news context only after official sources are covered
- [ ] Step 8: Cross-check important numbers across sources when possible
- [ ] Step 9: Update Obsidian entity/memo and log durable changes
- [ ] Step 10: State caveats, gaps, and what would change the thesis
```

## Analysis Guidance

For earnings reviews:

- Compare latest results with prior-year and prior-quarter figures when source
  labels support it.
- Separate operational drivers from one-time items.
- Highlight guidance, backlog/RPO, demand indicators, pricing, margin pressure,
  capex, and free cash flow.
- Explain whether cash flow confirms or contradicts earnings.

For thesis work:

- State bull case, bear case, and key debate.
- Separate facts from assumptions.
- Identify measurable KPIs.
- Include what would change the view.

For valuation work:

- Use source-backed financials, share count, net debt/cash, FCF, guidance, and
  scenario assumptions.
- Label valuation as a scenario, not a company-disclosed fact.
- Do not present a precise target price if source data is incomplete.

## Durable Output Rules

For a single company, update or create:

- `wiki/entities/TICKER.md`
- source note in `raw/imports/` when new sources were gathered
- normalized facts in `raw/financials/` when financial tables were extracted
- analysis memo in `wiki/analysis/` when the result is a decision, transcript
  digest, source audit, comparison, or thesis refresh
- `log.md`

## Entity Note Sections

Use this structure unless the existing entity page has a compatible local style:

- Snapshot
- Source Map
- Business Model
- Segments / Revenue Mix
- Financial Facts
- Charts
- Transcript / Management Commentary
- Thesis
- Risks
- Catalysts
- Valuation Watch Items
- Reports / Source Notes
- Follow-Up
- Missing / Unverified Data

## Answer Format

After file updates, answer briefly:

1. What was updated.
2. The current thesis/action read if relevant.
3. Important source gaps or caveats.
4. Paths to created/updated notes.
