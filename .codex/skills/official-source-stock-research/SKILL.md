---
name: official-source-stock-research
description: Use when the user asks for a company deep dive, earnings review, thesis update, business-model analysis, new-ticker research, or an existing-ticker thesis refresh using official sources.
---

# Official Source Stock Research

## Instrument Boundary

Use this skill for operating companies. If the entity has
`instrument_type: ETF`, do not analyze it through business segments,
profitability, capital allocation, or company guidance. Route a passive,
index-tracking equity ETF to `official-source-etf-research`.
For bond, commodity, multi-asset, active, leveraged, inverse, or derivative-
heavy ETFs, stop with `unsupported ETF type` and create no artifacts.

## Source Priority

Use official filings, earnings materials/transcripts, financial statements, then
reputable news. Treat the underlying document as stronger evidence than an IR
summary page.

## Profiles

| Profile | Trigger | Output |
|---|---|---|
| `chat` | general ticker question without save/update intent | <=400 words, no files |
| `thesis-delta` / P7 | existing ticker refresh | changed entity sections; memo only if decision-changing |
| `deep-dive` / P6 | explicit full or new-ticker deep dive | complete thin entity plus one useful analysis memo |

Do not use `deep-dive` merely because this skill appears inside a pipeline. Read
existing vault context and choose the lightest profile.

## Workflow

1. Identify company, ticker, exchange, currency, latest period, and profile.
2. Build a compact source map and gather the minimum filing, call material, and
   financial data needed for the research question.
3. Analyze business model, segment drivers, profitability, capital allocation,
   balance sheet, management commentary, and material Q&A signals.
4. Separate facts from assumptions. State thesis, key debate, measurable KPIs,
   risks, catalysts, and what changes the view.
5. Use news only after official coverage and cross-check decision-changing
   numbers.
6. Update the entity once, by delta. Link source, fundamentals, valuation, and
   decision files instead of copying their tables or source maps.
7. Create one category memo only when the result has durable analysis not owned
   by another file. Append one workflow bullet to `log.md`.

## Earnings Read

Compare only compatible prior periods, separate operational drivers from
one-time items, and connect guidance, demand, margins, capex, and FCF. Explain
whether cash flow confirms earnings.

## Valuation Boundary

Use source-backed financials and assumptions, but route a full valuation to
`dcf-valuation`. Do not restate its input table or calculate a precise target
from incomplete data.

## Entity Budget

Keep a lean delta at 250-400 narrative words and full entity narrative at or
below 700 words. Omit empty legacy sections; preserve compatible existing local
structure when updating an old page.

## Chat Handoff

After durable work, answer in under 200 words: updated files, current thesis or
action implication, and the most important caveat.
