# DCF Valuation Skill

> GPT-ready export from `.codex/skills/dcf-valuation/SKILL.md`.

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

- Original folder: `dcf-valuation`
- Original name: `dcf-valuation`
- Description: Build a source-backed DCF valuation memo for a ticker using verified financial facts, official filings, market data, WACC assumptions, sensitivity tables, and explicit caveats.

## Skill Instructions


# DCF Valuation

Use this skill when the user asks for fair value, intrinsic value, DCF,
valuation, upside/downside, price target, undervalued/overvalued analysis, or
"what is TICKER worth".

This is adapted from Dexter's DCF workflow, but made Obsidian-native and
source-integrity-first.

## Non-Negotiables

- Do not calculate a precise fair value unless the core inputs are source-backed.
- Label every assumption and scenario.
- Use current price only after a fresh market-data check.
- Do not treat a DCF output as a company-disclosed fact.
- If FCF, share count, cash, debt, or WACC basis is missing, stop and list the
  missing inputs instead of forcing a valuation.

## Required References

Read before writing:

- `wiki/reference/source-hierarchy.md`
- `wiki/reference/financial-ratios.md`
- `wiki/reference/valuation-assumptions.md`
- `wiki/reference/output-contract.md`

Follow the output contract's language standard: Thai-first narrative with
English finance terms, headings, formulas, and metric labels preserved.

## Required Inputs

Minimum viable DCF inputs:

- latest current stock price and date/time checked
- historical free cash flow or operating cash flow and capex
- latest cash and short-term investments
- latest total debt or debt-like obligations
- diluted shares outstanding or weighted diluted shares
- sector / business model for WACC range
- terminal growth assumption
- explicit forecast growth assumptions

Preferred inputs:

- 3-5 years of annual FCF
- latest trailing twelve-month FCF
- management guidance
- segment trend and capex commentary
- ROIC or operating margin trend
- net debt / cash calculation

## Workflow Checklist

```text
DCF Valuation Progress:
- [ ] Step 1: Read existing entity and fundamentals files
- [ ] Step 2: Freshly check current price and market data
- [ ] Step 3: Gather or verify FCF, capex, cash, debt, shares, and guidance
- [ ] Step 4: Choose WACC from source-backed sector/business risk
- [ ] Step 5: Choose growth assumptions and terminal growth
- [ ] Step 6: Project FCF for Years 1-5
- [ ] Step 7: Calculate terminal value and present value
- [ ] Step 8: Calculate equity value and fair value per share
- [ ] Step 9: Build sensitivity matrix
- [ ] Step 10: Run sanity checks and write caveats
- [ ] Step 11: Save memo and update entity/log when durable
```

## Calculation Rules

Free cash flow:

```text
FCF = operating cash flow - capex spend
```

When source reports capex as a cash outflow, convert to positive spend for the
formula and label it.

Enterprise value:

```text
EV = PV of projected FCF + PV of terminal value
```

Equity value:

```text
Equity value = EV + cash and short-term investments - total debt
```

Fair value per share:

```text
Fair value per share = equity value / diluted shares
```

Terminal value:

```text
Terminal value = Year 5 FCF * (1 + terminal growth) / (WACC - terminal growth)
```

## Assumption Discipline

- Mature companies: default terminal growth range 2.0%-3.0%.
- High-growth companies: fade growth toward a sustainable terminal range.
- Cap sustained FCF growth assumptions unless management guidance and history
  justify otherwise.
- If terminal value is more than 85%-90% of total EV, explicitly warn that the
  valuation is assumption-heavy.
- Compare implied FCF yield, P/E, EV/FCF, or EV/Revenue to the company's own
  history and peers when source data exists.

## Output File

Save durable valuation work as:

```text
wiki/analysis/valuations/TICKER DCF Valuation YYYY-MM-DD.md
```

Update `wiki/entities/TICKER.md` only when the valuation changes the thesis,
valuation watch items, or follow-up list.

Append `log.md`.

## Memo Sections

Use this structure:

- `# TICKER DCF Valuation - YYYY-MM-DD`
- `## Bottom Line`
- `## Source Map`
- `## Input Table`
- `## Base Case Assumptions`
- `## FCF Projection`
- `## Valuation Summary`
- `## Sensitivity Matrix`
- `## Sanity Checks`
- `## What Would Change The Valuation`
- `## Missing / Unverified Data`
- `## Entity Update`

## Sensitivity Matrix

Build at least a 3x3 table:

- WACC: base -1%, base, base +1%
- terminal growth: 2.0%, 2.5%, 3.0% unless sector context says otherwise

## Stop Conditions

Stop and report missing inputs when:

- current price cannot be freshly checked
- free cash flow cannot be verified or calculated
- share count is missing
- cash/debt inputs are missing
- WACC basis is unsupported
- the business is too cyclical or financial-sector-specific for a simple DCF
  without a different valuation model
