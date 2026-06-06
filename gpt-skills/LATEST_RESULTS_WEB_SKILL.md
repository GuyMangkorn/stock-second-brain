# Latest Results Web Skill

> GPT-ready export from `.codex/skills/latest-results-web/SKILL.md`.

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

- Original folder: `latest-results-web`
- Original name: `latest-results-web`
- Description: Find official latest company result sources for stock-second-brain, prioritizing SEC filings, earnings transcripts, financial statements/metrics, then news, and save a traceable raw source note before ingest.

## Skill Instructions


# Latest Results Web

Use this skill when the user asks for latest results, latest quarter, recent
earnings, current official sources, or wants a ticker ingested without providing
a local source file.

## Source Priority

1. SEC filings and official company filings: 10-K, 10-Q, 8-K, 20-F, annual
   report, quarterly report, official IR filing pages.
2. Earnings transcripts and call materials: official webcast transcript,
   prepared remarks, Q&A, shareholder letter, earnings presentation.
3. Financial statements and metrics: official financial tables, company data
   books, structured market data with clear source/date.
4. News and web research: reputable news only for context or recent events not
   yet reflected in official documents.

## Language Standard

Follow `wiki/reference/output-contract.md`. Source maps, source titles, filing
labels, table columns, and extracted source facts should stay close to the
source language. Thai summaries are allowed for commentary and handoff notes,
but they must not alter the source meaning.

## Required Workflow

1. Identify ticker, company, exchange, reporting currency, and fiscal calendar.
2. Search official sources first:
   - `site:sec.gov TICKER 10-Q 10-K 8-K`
   - `TICKER investor relations quarterly results`
   - `Company earnings transcript latest quarter`
   - `Company annual report investor relations`
3. Save a source note before normalization:
   - quarterly default: `raw/imports/TICKER_latest_results_source.md`
   - annual requested: `raw/imports/TICKER_latest_annual_source.md`
4. Include source URLs, source kind, publication date, reporting periods,
   currency, units, reporting basis, extracted facts, and gaps.
5. Write a clear `Handoff For Ingest` section for `financial-facts-ingest`.
   Do not normalize statements or update the entity page in this skill unless
   the user explicitly asks for a one-step source discovery plus ingest.
6. If official sources cannot be found, stop and report
   `ไม่พบข้อมูลที่ยืนยันได้`.

## Raw Source Note Shape

```markdown
---
type: source-note
ticker: TICKER
company: Company Name
source_kind: latest-results
search_date: YYYY-MM-DD
reporting_scope:
currency:
normalized_output: raw/financials/TICKER_fundamentals.md
entity: "[[TICKER]]"
tags:
  - source/latest-results
  - ticker/TICKER
---

# TICKER - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|

## Reporting Scope

## Currency / Units

## Extracted Facts

## Transcript / Commentary

## Financial Tables

## Missing / Unverified Data

## Handoff For Ingest
```

## Stop Conditions

Stop when:

- ticker identity is ambiguous
- no official source can be found
- source period labels, currency, or units are unclear
- all available sources are secondary summaries with no primary trail
