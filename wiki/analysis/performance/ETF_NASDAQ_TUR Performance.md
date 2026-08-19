---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:TUR
ticker: TUR
exchange: NASDAQ
fund: iShares MSCI Turkey ETF
tracked_index: MSCI Turkey IMI 25/50 Index (USD) (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-17
price_nav_as_of: 2026-08-18
fund_facts_as_of: 2026-08-18
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/TUR
  - geography/Turkey
---

# TUR Performance

> Navigation: [[ETF Region Index]] → [[Turkey ETF]] → [[ETF Performance Index]]

## Bottom line

TUR เป็น passive single-country Turkey equity ETF ที่ track `MSCI Turkey IMI
25/50 Index (USD) (Net)`. Official complete-calendar 2016-2025 NAV Total Return
สะสม `25.33%` และ rounded-input CAGR `2.28%`, เป็นบวก `4` ปีและลบ `6` ปี;
ดีที่สุดคือ 2022 ที่ `+106.42%` และแย่ที่สุดคือ 2018 ที่ `-41.42%`. Current
official NAV TR YTD คือ `+16.38%` ณ 2026-08-17 เทียบกับ S&P 500 Total Return
`+13.17%` ณ 2026-08-18 จาก secondary common-reference snapshot (คนละวัน)

## Performance check

- `entity_key: NASDAQ:TUR`; inception `2008-03-26`; exchange `NASDAQ`; CUSIP `464286715`.
- Metric: `NAV Total Return` in USD; รวมเงินปันผลและ capital gains reinvested และหัก fund expenses.
- Tracked index (issuer benchmark): `MSCI Turkey IMI 25/50 Index (USD) (Net)`; historical rows use the issuer's spliced benchmark history, with the current IMI 25/50 series from 2019-05-29.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ TUR).
- Management mode: `passive-index`; the fund seeks to track a broad-based index of Turkish equities and is not an active long-only product.
- Expense ratio `0.59%`; distribution frequency `semi-annual`; official NAV `US$39.58` ณ 2026-08-18 and closing price `US$39.43` ณ 2026-08-17.
- Official rolling 10-year window: `2026-06-30` endpoint pair `2016-06-30` to `2026-06-30`; cumulative NAV TR `28.97%`, `Start TR value: 100.00`, `End TR value: 128.97`, `Years: 10.00`.
- 10-year NAV TR CAGR: `2.58%` ณ 2026-06-30; Formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Coverage/source note: 2016-2020 fund rows use the official summary-prospectus chart to two decimals; 2016-2020 benchmark rows are the official iShares international calendar table rounded to one decimal; 2021-2025 fund/index rows use the official factsheet to two decimals. No proxy or partial-year marker is used.

| Year | TUR NAV TR | MSCI Turkey index | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -8.28% | -8.2% | 11.96% |
| 2017 | 37.45% | 37.8% | 21.83% |
| 2018 | -41.42% | -41.3% | -4.38% |
| 2019 | 13.94% | 14.5% | 31.49% |
| 2020 | -0.74% | -0.7% | 18.40% |
| 2021 | -27.51% | -27.68% | 28.71% |
| 2022 | 106.42% | 107.26% | -18.11% |
| 2023 | -9.16% | -8.80% | 26.29% |
| 2024 | 13.70% | 14.82% | 25.02% |
| 2025 | -2.91% | -2.57% | 17.88% |

**Up years / Down years**

- Complete fund rows 2016-2025: `4 / 6` up/down years; cumulative `25.33%`; rounded-input CAGR `2.28%`.
- Best: 2022, `+106.42%`; least positive: 2024, `+13.70%`.
- Worst: 2018, `-41.42%`; least bad down year: 2020, `-0.74%`.
- Common 2021-2025 window: TUR cumulative `50.05%` / rounded-input CAGR `8.45%`; tracked-index cumulative `52.93%` / rounded-input CAGR `8.87%`; approximate passive tracking gap is `-0.41 pp` CAGR.
- Current YTD: TUR NAV TR `+16.38%` ณ 2026-08-17. S&P 500 TR current YTD is `+13.17%` ณ 2026-08-18 from a secondary total-return snapshot; the date mismatch is retained.

## Risk read-through

Official rolling 10-year NAV TR CAGR คือ `2.58%` ณ 2026-06-30, แต่ annual
calendar profile มี dispersion สูงจาก 2022 ที่ `+106.42%` และ 2018 ที่
`-41.42%`; population standard deviation ของ annual rows คือ `38.83%`. Official
3-year standard deviation คือ `25.11%` และ equity beta `0.35` ณ 2026-07-31.
กองทุนมี single-country emerging-market risk, Turkish lira/USD และ valuation
ความเสี่ยงจาก sector concentration; ณ 2026-08-17 sectors ใหญ่สุดคือ Industrials
`27.62%`, Financials `16.56%`, Consumer Staples `13.18%`, Materials `11.70%`
และ Energy `9.05%`, จาก 73 holdings. Summary prospectus รายงาน best quarter
`+68.38%` ใน Q4 2022 และ worst quarter `-29.37%` ใน Q1 2020; ทั้งสองตัวเลข
ไม่ใช่ maximum drawdown. Official daily NAV maximum drawdown และ recovery date
ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

Expense ratio `0.59%`; latest four official cash distributions คือ
`US$0.479168` (2026-06-15), `US$0.359292` (2025-12-16), `US$0.466192`
(2025-06-16) และ `US$0.146027` (2024-12-17), รวม `US$1.450679` และเฉลี่ย
`US$0.362670` ต่อรอบ หรือประมาณ `0.92%` ต่อรอบเทียบ closing price `US$39.43`.
ตัวเลขนี้เป็น historical cash distribution ไม่ใช่การคาดการณ์; issuer 12m
trailing yield คือ `2.21%` ณ 2026-07-31. S&P 500 comparison เป็น common
reference เท่านั้น ไม่ใช่ evidence ของ alpha หรือ manager skill.

## Sources

- [iShares TUR U.S. product page](https://www.ishares.com/us/products/239689/ishares-msci-turkey-etf) — identity, NASDAQ listing, benchmark, current NAV/price, YTD, rolling performance, holdings, sectors, distributions and fees.
- [iShares TUR fact sheet](https://www.ishares.com/us/literature/fact-sheet/tur-ishares-msci-turkey-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/index rows, return definition, expense ratio and fund characteristics as of 2026-06-30.
- [iShares TUR summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-turkey-etf-8-31.pdf) — official 2016-2020 calendar rows, passive objective, index splice, risks and best/worst quarter.
- [iShares TUR international calendar page](https://www.ishares.com/ch/professionals/en/products/239689/ishares-msci-turkey-etf?switchLocale=Y) — official USD fund/benchmark calendar cross-check for 2016-2025.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` convention — USD Total Return annual rows 2016-2025, dividends reinvested, reference as of 2025-12-31.
- [Slickcharts S&P 500 YTD](https://www.slickcharts.com/sp500/returns/ytd) — secondary current S&P 500 Total Return YTD `13.17%` as of 2026-08-18.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
