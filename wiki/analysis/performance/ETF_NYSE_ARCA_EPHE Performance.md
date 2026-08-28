---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EPHE
ticker: EPHE
exchange: NYSE Arca
fund: iShares MSCI Philippines ETF
tracked_index: MSCI Philippines IMI 25/50 Index (USD) (Net)
benchmark: S&P 500 Total Return
inception: 2010-09-28
management_mode: passive-index
updated: 2026-08-28
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
nav_as_of: 2026-08-26
market_price_as_of: 2026-08-26
holdings_as_of: 2026-08-26
risk_as_of: 2026-07-31
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EPHE
  - geography/Philippines
---

# EPHE Performance

> Navigation: [[ETF Region Index]] → [[Philippines ETF]] → [[ETF Performance Index]]

## Bottom line

EPHE เป็น passive/index-tracking Philippines equity ETF ที่ติดตาม `MSCI
Philippines IMI 25/50 Index (USD) (Net)`. Official rolling 10-year NAV Total
Return จาก `2016-06-30` ถึง `2026-06-30` มี cumulative return `-28.05%` และ CAGR
`-3.24%`; available complete calendar rows 2021-2025 สะสม `-15.95%` หรือ CAGR
`-3.42%`. Latest official current-page NAV TR YTD คือ `1.80%` ณ
`2026-08-26`; เลือกค่าที่ใหม่กว่าการ capture ก่อนหน้าที่ `2.66%` ณ 25 ส.ค.

## Performance check

- `entity_key: NYSE Arca:EPHE`
- Fund: iShares MSCI Philippines ETF; inception `2010-09-28`; expense ratio
  `0.59%`; distribution frequency semi-annual
- Metric: official `NAV Total Return` ใน USD รวม distributions reinvested และหัก
  fund expenses
- Issuer benchmark: `MSCI Philippines IMI 25/50 Index (USD) (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ EPHE)
- Management mode: `passive-index`; official objective คือ track a broad-based
  index composed of Philippine equities
- Index-history caveat: EPHE began tracking the current IMI 25/50 index on
  `2020-12-01`; earlier index history is for the MSCI Philippines Investable
  Market Index and is not treated as perfectly like-for-like
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`, `10.00 elapsed
  years`; NAV TR cumulative `-28.05%`, CAGR `-3.24%`. Raw NAV endpoints are not
  disclosed; normalized representation is Start `100.00`, End `71.95` from the
  issuer cumulative return, not a market-price proxy
- Current official snapshot: NAV `$24.88`, closing market price `$24.62`, and
  1-day NAV change `-$0.21 (-0.84%)` as of `2026-08-26`; NAV TR YTD `1.80%` as of
  `2026-08-26`
- Annual coverage: 2021-2025 complete official rows; 2016-2020 annual NAV rows
  remain `not disclosed` in the reviewed U.S. factsheet capture

| ปี | EPHE NAV TR | MSCI Philippines IMI 25/50 Index (Net) | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | -2.10% | -1.44% | 28.71% |
| 2022 | -14.37% | -14.05% | -18.11% |
| 2023 | -0.27% | 0.81% | 26.29% |
| 2024 | 1.08% | 2.11% | 25.02% |
| 2025 | -0.54% | -0.06% | 17.88% |

S&P 500 rows ใช้ cached USD Total Return convention, dividends reinvested,
reference as-of `2025-12-31`. EPHE 2021-2025 cumulative/CAGR คือ `-15.95%` /
`-3.42%`; tracked index คือ `-12.85%` / `-2.71%`; arithmetic fund-minus-index
CAGR gap คือ `-0.70 pp` และไม่เรียกว่า alpha. S&P 500 TR คือ `96.17%` /
`14.43%`; EPHE มี arithmetic gap `-17.85 pp` เทียบ common reference นี้.

## Up years / Down years

- Disclosed 2021-2025 rows: up `1`, down `4`
- Best disclosed year: 2024, `+1.08%`
- Worst disclosed year: 2022, `-14.37%`
- Full 10-year best/worst ranking is not claimed because 2016-2020 annual NAV
  rows are not disclosed in the reviewed source table
- Current YTD: EPHE `+1.80%` NAV TR ณ `2026-08-26`

## Risk read-through

EPHE เป็นกอง single-country Philippines equity; sector exposure ณ 25 ส.ค. 2026
คือ Industrials `40.52%`, Financials `20.27%`, Utilities `11.68%`, Real Estate
`10.69%`, Consumer Staples `6.67%` และ Communication `4.47%`. มี `34` holdings
ณ 26 ส.ค.; P/E `9.19` และ P/B `1.17` ณ 25 ส.ค.; 3-year standard deviation
`18.24%` และ beta `0.15` ณ 31 ก.ค. 2026; 30-day SEC yield `1.88%` และ 12-month
trailing yield `2.69%` ณ 31 ก.ค. 2026.

จึงมี country, FX, liquidity, policy และ emerging-market risk สูงกว่ากอง broad
developed-market และมี sector concentration เพิ่มเติม. Fund-minus-index gap ต้อง
อ่านเป็น tracking/fee/timing evidence ไม่ใช่ manager skill; current YTD เป็น
partial period และไม่ใช้แทน rolling 10-year result. Official daily NAV TR series
สำหรับคำนวณ maximum drawdown และ recovery โดยตรง: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Official iShares EPHE product/performance page](https://www.ishares.com/us/products/239675/EPHE) — latest current-page NAV/price, YTD NAV TR, exchange, benchmark, holdings, exposure, fees and performance table; current search capture through 2026-08-26
- [Official EPHE factsheet](https://www.ishares.com/us/literature/fact-sheet/ephe-ishares-msci-philippines-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 annual NAV/index rows, rolling 10-year NAV TR and risk facts as of 2026-06-30
- [Official EPHE summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-philippines-etf-8-31.pdf) — passive objective, NYSE Arca listing, benchmark and index-history caveat
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity; annual rows reuse the cached skill convention
- [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
