---
type: entity
instrument_type: ETF
entity_key: AMEX:VIG
ticker: VIG
exchange: AMEX
fund: Vanguard Dividend Appreciation ETF
market: U.S. listed ETF
currency: USD
latest_holdings_as_of: 2026-05-31
source_gap_count: 2
source_gaps:
  - Current price/NAV and trading-date market data are not normalized in the vault.
  - Current distribution data are not normalized in the entity pass.
tags:
  - entity/etf
  - ticker/VIG
  - exchange/AMEX
---

# VIG - Vanguard Dividend Appreciation ETF

## Snapshot

| Item | Value |
|---|---|
| Instrument key | `AMEX:VIG` |
| Strategy | U.S. dividend growth / quality |
| Role | Core candidate |
| Triage score | 8.2 / 10 |
| Dividend yield screen | 1.70%; Kiplinger secondary screen, May 2026 |
| Latest holdings snapshot | 2026-05-31; Vanguard official holdings API |
| Top-10 theme | U.S. quality compounders across technology, health care, financials, energy, and consumer staples |

## Thesis / Key Debate

- **Thesis:** VIG is a low-yield, quality-oriented dividend-growth core that avoids making maximum yield the primary selection rule.
- **Key debate:** Lower income yield and mega-cap overlap may make the fund less attractive for an income mandate despite strong long-term quality characteristics.
- **What would change the view:** A breakdown in dividend-growth quality, methodology change, or excessive overlap with other core holdings.

## Risks

- U.S. market and mega-cap quality-factor concentration.
- Lower starting yield can make total-return assumptions sensitive to valuation and growth.
- Holdings, distribution, and overlap change over time; the official snapshot must be refreshed before trade.

## Valuation Watch Items

ETF valuation should be tracked through price/NAV, distribution yield, expense ratio, and holdings overlap. No DCF is created for this ETF in the current scope.

## Performance

- [[ETF_AMEX_VIG Performance]]
- [[ETF Performance Regime Matrix]]

## Reports / Sources

- [[Dividend ETF Triage 2026-06-28]]
- [[Dividend ETF Full Universe Triage 2026-06-28]]
- [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]]
- Vanguard official profile: https://investor.vanguard.com/investment-products/etfs/profile/vig

## Follow-Up

- Refresh official holdings, distribution, expense-ratio, and price/NAV data before treating VIG as an actionable allocation.
- Compare current overlap with [[ETF_AMEX_DGRO]] and the existing company entities referenced in the holdings tracker.

## Missing / Unverified Data

- Current price/NAV and as-of date: `ไม่พบข้อมูลที่ยืนยันได้` in this entity pass.
- Expense ratio and current distribution schedule: `ไม่พบข้อมูลที่ยืนยันได้` in the captured tracker sources.
