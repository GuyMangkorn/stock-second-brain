# Official Source Stock Research Skill

> GPT-ready export from `.codex/skills/official-source-stock-research/SKILL.md`.

## How To Use In GPT

Paste this entire file into a Custom GPT instruction, Project instruction, or the first message of a GPT chat. If GPT does not have filesystem, browser, or market-data access, it must ask the user to provide the relevant source files, URLs, tables, excerpts, or current data instead of pretending it can inspect them.

## Global Stock Research Rules

- Source before writing. Collect source facts first, then write analysis or durable notes.
- Do not invent, smooth, backfill, or complete missing financial values.
- Every durable number must have a URL, local path, filing reference, or shown calculation from sourced inputs.
- Separate facts, calculations, assumptions, and judgment.
- If a value cannot be verified, write `ไม่พบข้อมูลที่ยืนยันได้` or `not disclosed`.
- If sources conflict, record the conflict and choose the higher-quality source only with explanation, or keep both.
- Prices, valuation multiples, analyst targets, news, laws, and current market data must be freshly checked before use.
- Preserve raw source meaning. Do not add new factual claims unless separately sourced.
- Source priority: SEC filings / official filings; earnings transcripts and call materials; financial statements and metrics; reputable news; X/Twitter sentiment only as lower-priority context.
- Write narrative analysis, thesis, risks, catalysts, action reads, caveats, and final chat answers primarily in Thai. Keep headings, filenames, ticker names, source titles, table labels, formulas, metric names, and finance terms in English when precision or searchability matters.

## Original Skill Metadata

- Original folder: `official-source-stock-research`
- Original name: `official-source-stock-research`
- Description: Run official-source stock research for company deep dives, earnings reviews, thesis updates, and Obsidian entity notes using SEC filings, earnings transcripts, financial statements, then news.

## Skill Instructions


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
- analysis memo in the relevant `wiki/analysis/<category>/` folder when the
  result is a decision, transcript digest, source audit, comparison, or thesis
  refresh
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
