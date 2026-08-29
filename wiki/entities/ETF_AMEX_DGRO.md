---
type: entity
instrument_type: ETF
entity_key: NYSE Arca:DGRO
ticker: DGRO
exchange: NYSE Arca
fund: iShares Core Dividend Growth ETF
market: U.S. listed ETF
currency: USD
latest_holdings_as_of: 2026-08-27
source_gap_count: 1
source_gaps:
  - Official daily NAV Total Return history is not normalized for a reproducible drawdown/recovery calculation.
tags:
  - entity/etf
  - ticker/DGRO
  - exchange/AMEX
  - exchange/NYSE-Arca
---

# DGRO - iShares Core Dividend Growth ETF

## Snapshot

| Item | Value |
|---|---|
| Instrument key | `NYSE Arca:DGRO` |
| Strategy | U.S. dividend growth / quality equity |
| Role | Core candidate |
| Triage score | 8.1 / 10 |
| 12m trailing yield | 1.89% as of 2026-07-31; iShares official source |
| Current NAV / closing price | USD 79.27 / USD 79.28 as of 2026-08-27 |
| Latest holdings snapshot | 2026-08-27; 390 holdings; official iShares source |
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

- [[ETF_NYSE_ARCA_DGRO Performance]]
- [[ETF Performance Index]]

## Reports / Sources

- [[Dividend ETF Full Universe Triage 2026-06-28]]
- [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]]
- iShares official product page: https://www.ishares.com/us/products/264623/DGRO

## Follow-Up

- Refresh official holdings, distribution, expense-ratio, and price/NAV data before treating DGRO as an actionable allocation; the latest snapshot is recorded above and on the performance page.
- Compare current overlap with [[ETF_AMEX_VIG]] and the existing company entities referenced in the holdings tracker.

## Missing / Unverified Data

- Official daily NAV Total Return history for a reproducible max-drawdown/recovery calculation: `ไม่พบข้อมูลที่ยืนยันได้`.
