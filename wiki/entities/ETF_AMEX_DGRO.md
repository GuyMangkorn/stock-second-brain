---
type: entity
instrument_type: ETF
entity_key: AMEX:DGRO
ticker: DGRO
exchange: AMEX
fund: iShares Core Dividend Growth ETF
market: U.S. listed ETF
currency: USD
latest_holdings_as_of: 2026-06-30
source_gap_count: 2
source_gaps:
  - Current price/NAV and trading-date market data are not normalized in the vault.
  - Current distribution data are not normalized in the entity pass.
tags:
  - entity/etf
  - ticker/DGRO
  - exchange/AMEX
---

# DGRO - iShares Core Dividend Growth ETF

## Snapshot

| Item | Value |
|---|---|
| Instrument key | `AMEX:DGRO` |
| Strategy | Broad dividend equity / dividend growth |
| Role | Core candidate |
| Triage score | 8.1 / 10 |
| 12m trailing yield | 1.96% as of 2026-05-31; iShares official source |
| Latest holdings snapshot | 2026-06-30; official holdings found |
| Top-10 theme | U.S. large-cap dividend payers across technology, health care, financials, staples, and industrials |

## Thesis / Key Debate

- **Thesis:** DGRO balances dividend growth, quality, and broad U.S. large-cap exposure without relying only on the highest-yield names.
- **Key debate:** Its broad mega-cap overlap with VIG and other U.S. dividend ETFs can create hidden concentration in the same quality/technology names.
- **What would change the view:** A material change in index methodology, sustained dividend-growth deterioration, or an allocation-level overlap problem.

## Risks

- U.S. large-cap and factor concentration can make the fund less diversified than its row count suggests.
- Dividend-growth exposure can still be rate-sensitive when long-duration quality stocks reprice.
- Yield, holdings, and overlap change over time; the latest official snapshot must be refreshed before an allocation decision.

## Valuation Watch Items

ETF valuation should be tracked through price/NAV, distribution yield, expense ratio, and holdings overlap. No DCF is created for this ETF in the current scope.

## Performance

- [[ETF_AMEX_DGRO Performance]]
- [[ETF Performance Regime Matrix]]

## Reports / Sources

- [[Dividend ETF Full Universe Triage 2026-06-28]]
- [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]]
- iShares official product page: https://www.ishares.com/us/products/264623/ishares-core-dividend-growth-etf

## Follow-Up

- Refresh official holdings, distribution, expense-ratio, and price/NAV data before treating DGRO as an actionable allocation.
- Compare current overlap with [[ETF_AMEX_VIG]] and the existing company entities referenced in the holdings tracker.

## Missing / Unverified Data

- Current price/NAV and as-of date: `ไม่พบข้อมูลที่ยืนยันได้` in this entity pass.
- Expense ratio and current distribution schedule: `ไม่พบข้อมูลที่ยืนยันได้` in the captured tracker sources.
