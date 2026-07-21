# ETF Entity Template

Use the ETF entity as a thin living hub. Detailed holdings and metrics belong
in the linked fund-facts file; calculations and comparisons belong in analysis
memos.

```markdown
---
type: entity
instrument_type: ETF
entity_key: EXCHANGE:TICKER
ticker: TICKER
exchange: EXCHANGE
fund: Fund Name
sponsor:
market:
currency:
benchmark:
latest_holdings_as_of:
source_gap_count: 0
source_notes: []
normalized_fund_facts: raw/funds/ETF_EXCHANGE_TICKER_fund_facts.md
tags:
  - entity/etf
  - ticker/TICKER
  - exchange/EXCHANGE
---

# TICKER - Fund Name

## Snapshot

| Item | Value |
|---|---|
| Instrument key | `EXCHANGE:TICKER` |
| Strategy / benchmark |  |
| Portfolio role |  |
| Latest holdings snapshot |  |
| Fund facts | [[ETF_EXCHANGE_TICKER_fund_facts]] |
| Latest decision |  |

## Strategy / Methodology

One compact paragraph linking mandate to the index rules that shape exposure.

## Thesis / Key Debate

- **Thesis:**
- **Key debate:**
- **What would change the view:**

## Risks

Only current structure-, exposure-, tracking-, cost-, liquidity-, and FX-relevant risks.

## Valuation / Cost / Tracking Watch Items

Link current peer or decision analysis. Never create a corporate DCF for an ETF.

## Reports / Sources

Links to source note, fund facts, latest comparison, decision, and catalyst.

## Follow-Up

Measurable next checks with required as-of dates.

## Missing / Unverified Data

Unresolved instrument-level gaps only. Extraction, normalization, comparison,
and decision-specific gaps stay in their owning files.
```

In lean mode change only affected sections and keep new narrative between 250
and 400 words. In full mode keep entity narrative at or below 700 words.
