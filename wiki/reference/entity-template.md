# Entity Template

This template is for operating companies. For an ETF use
`wiki/reference/etf-entity-template.md`; do not adapt company fields such as
business segments, corporate FCF, or DCF inputs to a fund.

Use the entity as a thin living hub. Keep detailed numbers and charts in the
linked fundamentals file and calculations in linked analysis memos.

```markdown
---
type: entity
ticker: TICKER
company: Company Name
market:
currency:
latest_period:
latest_period_end:
source_gap_count: 0
source_notes: []
normalized_markdown: raw/financials/TICKER_fundamentals.md
normalized_json:
tags:
  - entity/company
  - ticker/TICKER
---

# TICKER - Company Name

## Snapshot

| Item | Value |
|---|---|
| Ticker / Market | TICKER / MARKET |
| Latest verified period |  |
| Reporting currency |  |
| Fundamentals | [[TICKER_fundamentals]] |
| Latest decision |  |

## Business Model

One compact paragraph.

## Thesis / Key Debate

- **Thesis:**
- **Key debate:**
- **What would change the view:**

## Risks

Only current thesis-relevant risks.

## Catalysts

Only current measurable catalysts.

## Valuation Watch Items

Link the latest valuation or record the missing prerequisite.

## Reports / Sources

Links to source note, fundamentals, latest valuation, decision, and catalyst.

## Follow-Up

Measurable next checks.

## Missing / Unverified Data

Unresolved ticker-level gaps only. Extraction, normalization, valuation, and
decision-specific gaps stay in their owning files.
```

In lean mode change only affected sections and keep new narrative between 250
and 400 words. In full mode keep entity narrative at or below 700 words.
