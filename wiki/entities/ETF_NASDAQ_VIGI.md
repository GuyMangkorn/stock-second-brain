---
type: entity
instrument_type: ETF
entity_key: NASDAQ:VIGI
ticker: VIGI
exchange: NASDAQ
fund: Vanguard International Dividend Appreciation ETF
market: U.S. listed international ETF
currency: USD
latest_holdings_as_of: 2026-05-31
source_gap_count: 2
source_gaps:
  - Current price/NAV and trading-date market data are not normalized in the vault.
  - Expense ratio and current distribution data are not captured in the tracker source set.
tags:
  - entity/etf
  - ticker/VIGI
  - exchange/NASDAQ
---

# VIGI - Vanguard International Dividend Appreciation ETF

## Snapshot

| Item | Value |
|---|---|
| Instrument key | `NASDAQ:VIGI` |
| Strategy | International dividend growth / quality |
| Role | Core candidate |
| Triage score | 7.7 / 10 |
| Dividend yield screen | 2.20%; Kiplinger secondary screen, May 2026 |
| Latest holdings snapshot | 2026-05-31; Vanguard official holdings API |
| Top-10 theme | Non-U.S. dividend growers across banks, health care, staples, industrials, and selected cyclicals |

## Thesis / Key Debate

- **Thesis:** VIGI adds international dividend-growth exposure and reduces reliance on a U.S.-only core dividend sleeve.
- **Key debate:** FX, country, sector, withholding-tax, and international bank/industrial exposure can overwhelm the quality screen in a difficult macro regime.
- **What would change the view:** Persistent dividend cuts, material country/sector concentration, or a portfolio that already has the same non-U.S. exposures elsewhere.

## Risks

- Foreign exchange and country-specific political, tax, and regulatory risk.
- International financials, industrials, and cyclicals can make income less defensive than the label implies.
- Holdings, distribution, and overlap change over time; refresh the official snapshot before trade.

## Valuation Watch Items

ETF valuation should be tracked through price/NAV, distribution yield, expense ratio, FX exposure, and holdings overlap. No DCF is created for this ETF in the current scope.

## Reports / Sources

- [[Dividend ETF Full Universe Triage 2026-06-28]]
- [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]]
- Vanguard official profile: https://investor.vanguard.com/investment-products/etfs/profile/vigi

## Follow-Up

- Refresh official holdings, distribution, expense-ratio, FX, and price/NAV data before treating VIGI as an actionable allocation.
- Compare VIGI's international exposure with the rest of the portfolio rather than treating it as a direct substitute for [[ETF_AMEX_VIG]].

## Missing / Unverified Data

- Current price/NAV and as-of date: `ไม่พบข้อมูลที่ยืนยันได้` in this entity pass.
- Expense ratio and current distribution schedule: `ไม่พบข้อมูลที่ยืนยันได้` in the captured tracker sources.
