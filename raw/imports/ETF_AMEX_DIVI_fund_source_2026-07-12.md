---
type: source
instrument_type: ETF
entity_key: AMEX:DIVI
ticker: DIVI
fund: Franklin International Core Dividend Tilt Index ETF
vault_exchange_label: AMEX
official_listing_venue: NYSE Arca
source_profile: official ETF refresh
accessed: 2026-07-12
latest_factsheet_as_of: 2026-06-30
latest_holdings_as_of: 2026-06-30
latest_issuer_market_data_as_of: 2026-06-24
tags:
  - source/etf
  - ticker/DIVI
  - exchange/AMEX
---

# DIVI Official ETF Source Note - 2026-07-12

## Source Map

| Priority | Source | Publication / access | Data as-of | Use |
|---:|---|---|---|---|
| 1 | [Franklin product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/21412/SINGLCLASS/franklin-international-core-dividend-tilt-index-etf/DIVI) | accessed 2026-07-12 | 2026-06-24 for issuer price/NAV; holdings page 2026-06-23 | Identity, official listing, price/NAV, spread, AUM, yield, holdings count and portfolio breakdown |
| 1 | [Franklin factsheet DIVI-FF](https://www.franklintempleton.com/forms-literature/download/DIVI-FF) | factsheet dated June 2026 | 2026-06-30 | Latest official fund facts, top issuers, geography, sectors, performance and risk statistics |
| 1 | [Franklin Dividend Tilt ETFs prospectus](https://www.franklintempleton.com/forms-literature/download/ETF3-P) | prospectus dated 2025-08-01; supplement noted 2026-04-29 | prospectus disclosures | Passive status, index construction, constraints, implementation and risks |
| 1 | [Franklin 2026 annual report](https://www.franklintempleton.com/forms-literature/download-preview/ETF-AFSOI) | published 2026 | fiscal year ended 2026-03-31 | Audited portfolio and financial context; older than the factsheet for current holdings |
| 4 | [StockAnalysis DIVI history/profile](https://stockanalysis.com/etf/divi/) | accessed 2026-07-12 | 2026-07-08 close in captured result | Secondary market-price context only; not used to replace official fund facts |
| local | [[ETF_top10_holdings_sources_2026-07-01]] | historical batch | 2026-07-01 | Prior lookup-failed record; superseded for DIVI by this refresh |

## Reporting Scope

รอบนี้ refresh เฉพาะ passive, index-tracking equity ETF `AMEX:DIVI` ตาม
request `instrument_type: ETF`, `mode: lean`. Identity ใน vault คงเป็น
`AMEX:DIVI` ตาม exchange-qualified key เดิม ขณะที่ Franklin ระบุ official
listing venue เป็น NYSE Arca จึงบันทึกสอง label แยกกัน ไม่สร้าง entity ซ้ำ.

## Currency / Units

- USD unless stated otherwise; percentages are portfolio weights or annualized
  rates as defined by the source.
- `Price/NAV` เป็น per-share USD; `AUM` เป็น total net assets.
- Performance is total return with reinvested distributions and fund expenses
  deducted unless the source states otherwise.
- SEC yield, distribution rate, and trailing distribution are not interchangeable;
  only the dated definition supplied by the source is retained.

## Extracted Facts

### Identity & Structure

| Field | Verified fact | As-of / source |
|---|---|---|
| Fund | Franklin International Core Dividend Tilt Index ETF | Factsheet 2026-06-30 |
| Vault identity | `AMEX:DIVI` | User / existing vault identity |
| Official listing | NYSE Arca; ticker `DIVI` | Product page / factsheet |
| Sponsor / index provider | Franklin Templeton / Morningstar | Product page / prospectus |
| Asset class | Equity; indexed/passive | Factsheet / prospectus |
| Inception | 2016-06-01 | Factsheet / product page |
| Benchmark | Morningstar Developed Markets ex-North America Dividend Enhanced Select Index-NR | Factsheet / prospectus |

### Fund Facts

- Total expense ratio: `0.09%`.
- Total net assets: `$2.56B`; shares outstanding: `60.10M`.
- Number of holdings: `417`.
- 30-Day SEC Yield: `2.88%`.
- The fund targets developed markets excluding North America and the top 85%
  of the parent investable universe by float-adjusted market capitalization.

### Portfolio Snapshot

Top equity issuers from the official factsheet dated 2026-06-30:

| Rank | Issuer | Weight |
|---:|---|---:|
| 1 | ASML Holding NV | 3.28% |
| 2 | HSBC Holdings PLC | 1.48% |
| 3 | Nestle SA | 1.39% |
| 4 | Roche Holding AG | 1.36% |
| 5 | AstraZeneca PLC | 1.28% |
| 6 | Siemens AG | 1.17% |
| 7 | Novartis AG | 1.16% |
| 8 | Tokyo Electron Ltd | 1.07% |
| 9 | BHP Group Ltd | 1.06% |
| 10 | British American Tobacco PLC | 1.04% |

Top-10 weight is `14.29%`, calculated as the sum of the ten official
factsheet weights above. Sector allocation is led by Financials `29.13%`,
Industrials `16.53%`, and Information Technology `11.48%`. Geographic
allocation is led by Japan `23.93%`, United Kingdom `12.47%`, France `8.99%`,
and Australia `8.84%`.

### Methodology & Implementation

The index applies an optimizer to the Morningstar developed ex-North America
parent index to seek higher trailing-twelve-month dividend yield while limiting
expected tracking error. Quarterly reconstitution applies stock, sector,
country, and turnover constraints. The prospectus identifies the fund as using
a passive/indexing approach, with replication or representative sampling, and
permits equity futures, total-return swaps, and foreign-currency forwards for
implementation, liquidity, or tracking purposes.

### Performance & Market Check

- Factsheet through 2026-06-30: 1-year NAV return `24.65%` versus underlying
  index `24.58%`; 3-year average annual NAV return `18.01%` versus `17.86%`;
  5-year `13.68%` versus `13.68%`; since inception `11.02%` versus `11.26%`.
- Issuer product page as of 2026-06-24: NAV `$42.72`, market price `$42.81`,
  market-price premium at close `0.21%`, 30-day median bid/ask spread `0.14%`.
- Secondary market context captured for 2026-07-08: close `$42.41`; no same-day
  issuer NAV was captured with that close.

## Missing / Unverified Data

- `ไม่พบข้อมูลที่ยืนยันได้` for a same-day issuer NAV/market-price pair newer
  than 2026-06-24; do not infer a July premium/discount from the July 8 price.
- The complete downloadable holdings file was not captured in the current page
  surface. The factsheet provides a verified 417-holding count and top-10
  weights; full overlap work still requires the dated holdings file.
- `ไม่พบข้อมูลที่ยืนยันได้` for a current tax/withholding outcome for a specific
  investor; this is account- and jurisdiction-dependent.

## Handoff For Ingest

- Normalize the June 30 factsheet as the latest fund-facts snapshot.
- Keep price/NAV, AUM, holdings, distributions, performance, and methodology
  dates separate.
- Treat the old `official_lookup_failed` tracker row as superseded by this
  official factsheet refresh.
- Hand off to the ETF decision branch; no company P1/P4/P6/P7/P11 or DCF stage.
