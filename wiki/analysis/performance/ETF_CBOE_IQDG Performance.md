---
type: etf-performance
instrument_type: ETF
entity_key: Cboe:IQDG
input_ticker: IQDG
input_alias: IQDG
ticker: IQDG
exchange: Cboe
fund: WisdomTree International Quality Dividend Growth Fund
tracked_index: WisdomTree International Quality Dividend Growth Index
benchmark: S&P 500 Total Return
issuer_benchmark: WisdomTree International Quality Dividend Growth Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: post-inception-annual-table
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-02
performance_as_of: 2026-07-31
calendar_years_as_of: 2026-03-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-09-01
fund_facts_as_of: 2026-09-01
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-4.md
return_basis: USD NAV total return; distributing share class; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IQDG
  - geography/International
  - geography/developed-markets
---

# IQDG Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IQDG เป็น passive, distributing international equity ETF ที่ติดตาม WisdomTree
International Quality Dividend Growth Index และลงทุนในบริษัท dividend-paying
ที่มี quality/growth characteristics ใน developed markets นอกสหรัฐฯ และแคนาดา.
ใช้ USD NAV Total Return เป็นฐานหลัก โดยไม่ผสมกับ market-price return. Official
rolling 10-year NAV TR annualized อยู่ที่ `7.95%` และ current YTD อยู่ที่ `7.12%`
ณ `2026-07-31`; ช่วง complete 2017-2025 ให้ CAGR `8.89%` เทียบ S&P 500 TR
`15.14%`, ขณะที่ช่วง 2021-2025 ให้ CAGR `5.43%` เทียบ `14.43%`.

## Performance check

- `entity_key`: `Cboe:IQDG`; input ticker: `IQDG`; listing: Cboe
- CUSIP: `97717X131`; fund inception `2016-04-07`; the reviewed official annual table starts in 2017 and does not disclose a 2016 annual NAV-return row
- Net expense ratio: `0.42%`; distributing fund; U.S.-dollar NAV; WisdomTree states `Options Available: No`
- Current official NAV: `$44.273` as of `2026-09-01`; closing market price `$44.370` as of `2026-08-31`; total assets `$715.013M` as of `2026-09-01`
- Metric: issuer `NAV Returns` / NAV Total Return including the fund's distribution treatment; market-price return is separate
- Issuer benchmark: `WisdomTree International Quality Dividend Growth Index`; the index selects dividend-paying developed-market companies using growth and quality factors and weights companies by annual cash dividends
- Official rolling 10-year NAV TR: `7.95%` annualized as of `2026-07-31`; raw endpoint levels are `not disclosed` in the retrieved issuer table
- Current official NAV TR YTD: `7.12%` as of `2026-07-31`; the `2026-09-01` NAV and `2026-08-31` market price are separate current observations
- Calendar rows are from WisdomTree's official presentation dated `2026-03-31`; `2016` is not shown in the reviewed annual table and is not backfilled. S&P 500 TR uses the cached USD dividend-reinvested convention for 2017-2025.

| Year | IQDG NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2017 | 31.39% | 21.83% |
| 2018 | -17.04% | -4.38% |
| 2019 | 29.91% | 31.49% |
| 2020 | 16.64% | 18.40% |
| 2021 | 12.38% | 28.71% |
| 2022 | -20.15% | -18.11% |
| 2023 | 20.85% | 26.29% |
| 2024 | -2.70% | 25.02% |
| 2025 | 23.46% | 17.88% |

## Up years / Down years

- Complete 2017-2025 window: `6 / 3` up/down years
- Best complete year: 2017, `+31.39%`
- Least positive: 2021, `+12.38%`
- Worst complete year: 2022, `-20.15%`
- Least-bad down year: 2024, `-2.70%`
- Complete 2017-2025 cumulative return / rounded-input CAGR: `115.16% / 8.89%`
- Complete 2021-2025 cumulative return / rounded-input CAGR: `30.27% / 5.43%`
- Current official NAV TR YTD: `+7.12%` as of `2026-07-31`; no same-date current S&P 500 TR observation is asserted.

## Risk read-through

IQDG กระจายหลายประเทศแต่ยังมี factor และ country concentration: ณ `2026-08-31`
น้ำหนักประเทศสูงสุดคือ Japan `20.08%`, United Kingdom `15.34%`, France `13.50%`,
Germany `9.78%`, Spain `7.36%`, Netherlands `7.24%` และ Switzerland `6.40%`.
Sector allocation สูงสุดคือ Industrials `25.07%`, Consumer Discretionary
`20.13%`, Financials `17.58%`, Information Technology `9.42%` และ Health Care
`8.87%`. WisdomTree presentation ณ `2026-03-31` รายงาน since-inception
standard deviation `15.96%` และ beta `1.01`; เป็น risk snapshot คนละช่วงกับ
current YTD. Official daily NAV history sufficient for maximum drawdown and
recovery was not verified, so those values remain `ไม่พบข้อมูลที่ยืนยันได้`.
Dividend, quality/growth factor, foreign-currency and developed-market risks
ยังทำให้ผลตอบแทนต่างจาก broad-market ETF ได้.

## Sources

- [WisdomTree official IQDG product page](https://www.wisdomtree.com/us/products/equity/iqdg) — identity, passive objective, current NAV/price/assets, expense/yield fields, holdings/sector and official July 2026 total-return table; observations through `2026-09-01`
- [WisdomTree IQDG factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/iqdg-factsheet.pdf?la=en) — fund identity, Cboe listing, distribution treatment and historical disclosure
- [WisdomTree IQDG presentation](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/presentations/equity/iqdg-presentation.pdf) — official 2017-2025 calendar NAV returns and risk snapshot as of `2026-03-31`
- [Cboe official IQDG listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/IQDG/) — exchange-qualified listing context
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references and calculation convention: [[ETF_performance_sources_2026-09-02_run-4]]
