---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DTH
input_ticker: DTH
input_alias: DTH
ticker: DTH
exchange: NYSE Arca
fund: WisdomTree International High Dividend Fund
tracked_index: WisdomTree International High Dividend Index
benchmark: S&P 500 Total Return
issuer_benchmark: WisdomTree International High Dividend Index
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
  - ticker/DTH
  - geography/International
  - geography/developed-markets
---

# DTH Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DTH เป็น passive, distributing international equity ETF ที่ติดตาม WisdomTree
International High Dividend Index และลงทุนในหุ้น dividend-paying นอกสหรัฐฯ และ
แคนาดา. ใช้ USD NAV Total Return เป็นฐานหลัก โดยไม่ผสมกับ market-price return.
Official rolling 10-year NAV TR annualized อยู่ที่ `9.26%` และ current YTD อยู่ที่
`14.82%` ณ `2026-07-31`; ช่วง complete 2016-2025 ให้ CAGR `7.97%` เทียบ S&P 500
TR `14.82%`, ขณะที่ช่วง 2021-2025 ให้ CAGR `12.22%` เทียบ `14.43%`.

## Performance check

- `entity_key`: `NYSE Arca:DTH`; input ticker: `DTH`; listing: NYSE Arca
- CUSIP: `97717W802`; fund inception `2006-06-16`
- Net expense ratio: `0.58%`; distributing fund; U.S.-dollar NAV; WisdomTree states `Options Available: No`
- Current official NAV: `$58.397` as of `2026-09-01`; closing market price `$58.510` as of `2026-08-31`; total assets `$662.804M` as of `2026-09-01`
- Portfolio characteristics as of `2026-08-31`: dividend yield `4.36%`, P/E `13.29`, P/B `1.61`; distribution yield `8.35%` and SEC 30-day yield `3.41%` are separate issuer yield fields, not total return
- Metric: issuer `NAV Returns` / NAV Total Return including the fund's distribution treatment; market-price return is separate
- Issuer benchmark: `WisdomTree International High Dividend Index`
- Official rolling 10-year NAV TR: `9.26%` annualized as of `2026-07-31`; raw endpoint levels are `not disclosed` in the retrieved issuer table
- Current official NAV TR YTD: `14.82%` as of `2026-07-31`; the `2026-09-01` NAV and `2026-08-31` market price are separate current observations
- Calendar rows are from WisdomTree's official presentation dated `2026-03-31`; S&P 500 TR uses the cached USD dividend-reinvested convention for 2016-2025.

| Year | DTH NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | 5.10% | 11.96% |
| 2017 | 20.33% | 21.83% |
| 2018 | -12.57% | -4.38% |
| 2019 | 17.74% | 31.49% |
| 2020 | -7.05% | 18.40% |
| 2021 | 8.62% | 28.71% |
| 2022 | -2.12% | -18.11% |
| 2023 | 15.19% | 26.29% |
| 2024 | 2.03% | 25.02% |
| 2025 | 42.41% | 17.88% |

## Up years / Down years

- Complete 2016-2025 window: `7 / 3` up/down years
- Best complete year: 2025, `+42.41%`
- Least positive: 2024, `+2.03%`
- Worst complete year: 2018, `-12.57%`
- Least-bad down year: 2022, `-2.12%`
- Complete 2016-2025 cumulative return / rounded-input CAGR: `115.33% / 7.97%`
- Complete 2021-2025 cumulative return / rounded-input CAGR: `77.95% / 12.22%`
- Current official NAV TR YTD: `+14.82%` as of `2026-07-31`; no same-date current S&P 500 TR observation is asserted.

## Risk read-through

DTH เป็น international high-dividend equity ที่มี country และ sector concentration:
ณ `2026-08-31` น้ำหนักประเทศสูงสุดคือ United Kingdom `17.14%`, Japan `12.40%`,
France `10.43%`, Spain `8.68%`, Italy `8.53%`, Australia `7.41%`, Hong Kong
`5.61%`, Germany `5.29%`, Norway `5.14%` และ Switzerland `4.54%`. Sector
allocation สูงสุดคือ Financials `27.15%`, Industrials `14.31%`, Utilities `11.03%`,
Energy `9.24%`, Materials `8.14%` และ Consumer Staples `7.64%`. WisdomTree
presentation ณ `2026-06-30` รายงาน standard deviation `17.60%` และ beta `1.01`;
เป็น risk snapshot คนละช่วงกับ current YTD. Official daily NAV history sufficient
for maximum drawdown and recovery was not verified, so those values remain
`ไม่พบข้อมูลที่ยืนยันได้`. Dividend, foreign-currency, financials and
developed-market risks remain relevant.

## Sources

- [WisdomTree official DTH product page](https://www.wisdomtree.com/us/products/equity/dth) — identity, passive objective, current NAV/price/assets, expense/yield fields, holdings/sector and official July 2026 total-return table; observations through `2026-09-01`
- [WisdomTree DTH factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dth-1058.pdf) — fund identity, NYSE Arca listing, distribution treatment and historical disclosure
- [WisdomTree DTH presentation](https://www.wisdomtree.com/us/media/dth-presentation) — official 2016-2025 calendar NAV returns and risk snapshot as of `2026-03-31` / `2026-06-30`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references and calculation convention: [[ETF_performance_sources_2026-09-02_run-4]]
