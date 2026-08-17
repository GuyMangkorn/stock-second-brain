---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWI
ticker: EWI
exchange: NYSE Arca
fund: iShares MSCI Italy ETF
tracked_index: MSCI Italy 25/50 Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWI
  - geography/Italy
---

# EWI Performance

> Navigation: [[ETF Region Index]] → [[Italy ETF]] → [[ETF Performance Index]]

## Bottom line

EWI เป็น passive single-country Italy equity ETF ที่ track `MSCI Italy 25/50
Index (Net)`. Official rolling table ณ 2026-06-30 รายงาน 10-year NAV Total
Return annualised `14.40%` และ cumulative `283.84%` เทียบ benchmark `14.48%`
และ `286.83%`; current official NAV TR YTD คือ `+18.73%` ณ 2026-08-14. จาก
complete fund NAV rows 2016-2025 EWI ให้ cumulative `173.66%` และ rounded-input
CAGR `10.59%`, โดย 2025 ดีที่สุด `+55.51%` และ 2018 แย่ที่สุด `-17.51%`.

## Performance check

- `entity_key: NYSE Arca:EWI`; inception `1996-03-12`; exchange `NYSE Arca`; CUSIP `46434G830`.
- Metric: `NAV Total Return` in USD; official prospectus states returns assume reinvestment of dividends and distributions.
- Tracked index: `MSCI Italy 25/50 Index (Net)`; benchmark rows in the current page are available for 2021-2025, while the reviewed 2016-2020 prospectus chart did not expose annual benchmark rows.
- Expense ratio `0.50%`; management fee `0.49%`; semi-annual distributions; official NAV `US$63.17`, closing price `US$63.27`, net assets `US$1.161B`, and 25 holdings as of 2026-08-14.
- Official rolling performance as of 2026-06-30: NAV `1Y 27.21%`, `3Y 27.34%`, `5Y 17.16%`, `10Y 14.40%`, inception `6.44%`; tracked benchmark `27.17%`, `27.34%`, `17.19%`, `14.48%`; rolling 10Y tracking gap `-0.08 pp`.
- Official annual NAV rows use the summary prospectus for 2016-2020 and the current product page for 2021-2025; the source date boundary is disclosed rather than treated as one single document.
- S&P 500 TR is a common reference benchmark only; it is not EWI's tracked index and is not used as manager-skill evidence.

| Year | EWI NAV TR | MSCI Italy 25/50 | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -9.40% | ไม่พบข้อมูลที่ยืนยันได้ | 11.96% |
| 2017 | 28.47% | ไม่พบข้อมูลที่ยืนยันได้ | 21.83% |
| 2018 | -17.51% | ไม่พบข้อมูลที่ยืนยันได้ | -4.38% |
| 2019 | 27.19% | ไม่พบข้อมูลที่ยืนยันได้ | 31.49% |
| 2020 | 2.56% | ไม่พบข้อมูลที่ยืนยันได้ | 18.40% |
| 2021 | 13.80% | 14.15% | 28.71% |
| 2022 | -14.19% | -14.59% | -18.11% |
| 2023 | 30.34% | 30.66% | 26.29% |
| 2024 | 10.39% | 10.66% | 25.02% |
| 2025 | 55.51% | 56.28% | 17.88% |

## Up years / Down years

- Complete fund rows 2016-2025: `7 / 3` up/down years; cumulative `173.66%`; rounded-input CAGR `10.59%`; population annual-return standard deviation `21.99%`.
- Best: 2025, `+55.51%`; worst: 2018, `-17.51%`; average positive year `24.04%`.
- Common 2021-2025 window: EWI cumulative `118.50%` / rounded-input CAGR `16.92%`; tracked benchmark cumulative `120.30%` / CAGR `17.11%`; return-only tracking gap approximately `-0.19 pp` CAGR. Up/down is `4 / 1`.
- Cached S&P 500 TR common-window cumulative `96.17%` / CAGR `14.43%`; EWI's arithmetic difference of approximately `+2.49 pp` is a reference comparison, not alpha.
- Current YTD: EWI NAV TR `+18.73%` as of 2026-08-14. A same-date S&P 500 current-YTD pairing was not used.

## Risk read-through

EWI มี concentration แบบ single-country และ sector สูง: Financials `54.88%`,
Utilities `15.98%`, Consumer Discretionary `8.75%`, Industrials `7.81%` และ
Energy `6.84%` ณ 2026-08-14. Official risk snapshot รายงาน 3-year standard
deviation `15.16%`, beta `0.63`, P/E `15.84` และ P/B `2.14`; prospectus ระบุ
Italy-specific political, currency, economic, mid-cap, market, liquidity และ
tracking-error risks. Official best/worst quarter คือ `+27.29%` ใน Q4 2022 และ
`-29.51%` ใน Q1 2020. Daily NAV maximum drawdown และ recovery date ยัง `ไม่พบ
ข้อมูลที่ยืนยันได้`.

Latest four official cash distributions were `US$1.173545` (2026-06-15),
`US$0.702133` (2025-12-16), `US$0.821604` (2025-06-16), and `US$0.559282`
(2024-12-17): sum `US$3.256564`, average `US$0.814141`; issuer 12m trailing
yield is `3.05%` as of 2026-07-31.

## Sources

- [iShares EWI product page](https://www.ishares.com/us/products/239664/ishares-msci-italy-etf) — current NAV/YTD, rolling returns, 2021-2025 annual rows, holdings, exposures, distributions and fund facts.
- [EWI summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-italy-capped-etf-8-31.pdf) — 2016-2020 annual NAV rows, return definition, index strategy, risks and best/worst quarter.
- [S&P 500 Total Return report](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=df8ec300-24ad-4c70-81d3-a3dcce0200e2&sourceIdentifier=index-family-specialization) — current cross-check only; dates do not match EWI YTD.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
