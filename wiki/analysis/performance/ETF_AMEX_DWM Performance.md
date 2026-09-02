---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DWM
input_ticker: DWM
input_alias: DWM
ticker: DWM
exchange: NYSE Arca
fund: WisdomTree International Equity Fund
tracked_index: WisdomTree International Equity Index
benchmark: S&P 500 Total Return
issuer_benchmark: WisdomTree International Equity Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: long-running-fund
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
  - ticker/DWM
  - geography/International
  - geography/developed-markets
---

# DWM Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DWM เป็น passive, distributing international equity ETF ที่ติดตาม WisdomTree
International Equity Index และลงทุนในบริษัทที่จ่ายเงินปันผลใน developed world
นอกสหรัฐฯ และแคนาดา. ใช้ USD NAV Total Return เป็นฐานหลัก โดยไม่ผสมกับ
market-price return. Official rolling 10-year NAV TR annualized อยู่ที่ `8.74%`
และ current YTD อยู่ที่ `11.05%` ณ `2026-07-31`; ช่วง complete 2016-2025 ให้
CAGR `7.74%` เทียบ S&P 500 TR `14.82%`, ขณะที่ช่วง 2021-2025 ให้ CAGR `10.46%`
เทียบ `14.43%`.

## Performance check

- `entity_key`: `NYSE Arca:DWM`; input ticker: `DWM`; listing: NYSE Arca
- CUSIP: `97717W703`; fund inception `2006-06-16`
- Net expense ratio: `0.48%`; distributing fund; U.S.-dollar NAV; WisdomTree states `Options Available: No`
- Current official NAV: `$76.161` as of `2026-09-01`; closing market price `$76.107` as of `2026-08-31`; total assets `$689.254M` as of `2026-09-01`
- Metric: issuer `NAV Returns` / NAV Total Return including the fund's distribution treatment; market-price return is separate
- Issuer benchmark: `WisdomTree International Equity Index`; the index covers dividend-paying companies in the developed world excluding the United States and Canada
- Official rolling 10-year NAV TR: `8.74%` annualized as of `2026-07-31`; raw endpoint levels are `not disclosed` in the retrieved issuer table
- Current official NAV TR YTD: `11.05%` as of `2026-07-31`; the `2026-09-01` NAV and `2026-08-31` market price are separate current observations
- Calendar rows are from WisdomTree's official presentation dated `2026-03-31`; S&P 500 TR uses the cached USD dividend-reinvested convention for 2016-2025.

| Year | DWM NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | 2.88% | 11.96% |
| 2017 | 23.46% | 21.83% |
| 2018 | -13.54% | -4.38% |
| 2019 | 19.07% | 31.49% |
| 2020 | -1.94% | 18.40% |
| 2021 | 10.44% | 28.71% |
| 2022 | -9.11% | -18.11% |
| 2023 | 16.56% | 26.29% |
| 2024 | 4.56% | 25.02% |
| 2025 | 34.40% | 17.88% |

## Up years / Down years

- Complete 2016-2025 window: `7 / 3` up/down years
- Best complete year: 2025, `+34.40%`
- Least positive: 2024, `+4.56%`
- Worst complete year: 2018, `-13.54%`
- Least-bad down year: 2020, `-1.94%`
- Complete 2016-2025 cumulative return / rounded-input CAGR: `110.83% / 7.74%`
- Complete 2021-2025 cumulative return / rounded-input CAGR: `64.42% / 10.46%`
- Current official NAV TR YTD: `+11.05%` as of `2026-07-31`; no same-date current S&P 500 TR observation is asserted.

## Risk read-through

DWM เป็น broad international dividend equity แต่ยังมี country และ sector
concentration: ณ `2026-08-31` น้ำหนักประเทศสูงสุดคือ Japan `25.43%`, United
Kingdom `13.26%`, France `8.75%`, Switzerland `7.78%`, Germany `6.47%`,
Australia `6.32%`, Spain `6.32%` และ Italy `5.50%`. Sector allocation สูงสุดคือ
Financials `22.82%`, Industrials `19.98%`, Consumer Discretionary `10.54%`,
Information Technology `8.24%`, Health Care `8.16%` และ Consumer Staples
`7.37%`. WisdomTree presentation ณ `2026-03-31` รายงาน since-inception standard
deviation `16.71%` และ beta `0.98`; เป็น risk snapshot คนละช่วงกับ current YTD.
Official daily NAV history sufficient for maximum drawdown and recovery was not
verified, so those values remain `ไม่พบข้อมูลที่ยืนยันได้`. Dividend, foreign-
currency and developed-market risks remain relevant.

## Sources

- [WisdomTree official DWM product page](https://www.wisdomtree.com/us/products/equity/dwm) — identity, passive objective, current NAV/price/assets, expense/yield fields, holdings/sector and official July 2026 total-return table; observations through `2026-09-01`
- [WisdomTree DWM factsheet](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dwm-1059.pdf) — fund identity, NYSE Arca listing, distribution treatment and historical disclosure
- [WisdomTree DWM presentation](https://www.wisdomtree.com/us/media/dwm-presentation) — official 2016-2025 calendar NAV returns and risk snapshot as of `2026-03-31`
- [WisdomTree International Equity Index](https://www.wisdomtree.com/us/indexes/wtdfa) — issuer benchmark description
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references and calculation convention: [[ETF_performance_sources_2026-09-02_run-4]]
