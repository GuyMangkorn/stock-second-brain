---
type: entity
instrument_type: ETF
entity_key: AMEX:DIVI
ticker: DIVI
exchange: AMEX
official_listing_venue: NYSE Arca
fund: Franklin International Core Dividend Tilt Index ETF
sponsor: Franklin Templeton
market: U.S. listed ETF
currency: USD
benchmark: Morningstar Developed Markets ex-North America Dividend Enhanced Select Index-NR
latest_holdings_as_of: 2026-06-30
source_gap_count: 2
source_gaps:
  - Latest issuer price/NAV pair captured only through 2026-06-24; a same-day July pair is not verified.
  - Complete current holdings XLS was not captured; full overlap work needs the dated file.
normalized_fund_facts: raw/funds/ETF_AMEX_DIVI_fund_facts.md
tags:
  - entity/etf
  - ticker/DIVI
  - exchange/AMEX
---

# DIVI - Franklin International Core Dividend Tilt Index ETF

## Snapshot

| Item | Value |
|---|---|
| Instrument key | `AMEX:DIVI` |
| Official listing | NYSE Arca |
| Strategy / benchmark | Developed ex-North America equity with dividend tilt / Morningstar Dividend Enhanced Select |
| Portfolio role | Satellite international dividend tilt; core ex-U.S. sleeve only when intentional |
| Latest holdings snapshot | 2026-06-30; 417 holdings |
| Fund facts | [[ETF_AMEX_DIVI_fund_facts]] |
| Latest decision | [[ETF_AMEX_DIVI Decision Memo 2026-07-12]] |

## Strategy / Methodology

DIVI is a passive indexed equity ETF that starts from Morningstar's large- and
mid-cap developed-markets ex-North America parent universe and uses an optimizer
to seek higher trailing dividend yield while constraining expected tracking
error, sector/country drift, stock weights, and turnover. It is a dividend tilt,
not a pure maximum-yield portfolio.

## Thesis / Key Debate

- **Thesis:** `0.09%` cost, `417` holdings, low top-10 concentration (`14.29%`),
  and a rules-based ex-North America mandate make DIVI a credible low-cost
  international dividend-tilt vehicle.
- **Key debate:** Financials are `29.13%` and Japan `23.93%`; the income label
  does not remove country, FX, or financial-sector cyclicality. The latest
  30-Day SEC Yield is `2.88%`, so this is not a high-cash-yield substitute.
- **What would change the view:** A persistent tracking gap, material increase
  in financial/country concentration, weaker dividend quality, or a portfolio
  overlap problem after user holdings are supplied.

## Risks

- International equity, FX, withholding-tax, country, and local-market liquidity
  risk.
- Financial-sector concentration and value/dividend-factor cyclicality.
- Quarterly optimizer/reconstitution, sampling, and permitted derivatives can
  produce tracking difference.
- Distribution amount is not guaranteed; some index constituents may not pay a
  current dividend.

## Valuation / Cost / Tracking Watch Items

ETF valuation is monitored through price/NAV, premium/discount, expense drag,
look-through multiples, yield, and tracking difference. The official 2026-06-24
pair was NAV `$42.72` versus market price `$42.81` (`+0.21%` premium), with a
`0.14%` 30-day median spread. The official factsheet reports 1-year NAV return
`24.65%` versus index `24.58%`; since inception NAV return is `11.02%` versus
index `11.26%`. No corporate DCF is applicable.

## Reports / Sources

- [[ETF_AMEX_DIVI_fund_source_2026-07-12]]
- [[ETF_AMEX_DIVI_fund_facts]]
- [[ETF_AMEX_DIVI Decision Memo 2026-07-12]]
- [[Dividend ETF Top 10 Holdings Tracker 2026-07-01]]
- [Franklin official product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/21412/SINGLCLASS/franklin-international-core-dividend-tilt-index-etf/DIVI)
- [Franklin official factsheet](https://www.franklintempleton.com/forms-literature/download/DIVI-FF)

## Follow-Up

- Refresh issuer price/NAV and premium/discount as of the next trading day.
- Capture the complete official holdings XLS before any overlap or portfolio-fit
  conclusion.
- Reassess after the next quarterly index reconstitution and distribution update.

## Missing / Unverified Data

- Same-day official NAV/market price newer than 2026-06-24: `ไม่พบข้อมูลที่ยืนยันได้`.
- Complete current holdings XLS in the captured source map:
  `ไม่พบข้อมูลที่ยืนยันได้`.
