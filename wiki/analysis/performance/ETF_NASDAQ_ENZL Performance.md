---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:ENZL
ticker: ENZL
exchange: NASDAQ
fund: iShares MSCI New Zealand ETF
tracked_index: MSCI New Zealand All Cap Top 25 Capped Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ENZL
  - geography/New-Zealand
---

# ENZL Performance

> Navigation: [[ETF Region Index]] → [[New Zealand ETF]] → [[ETF Performance Index]]

## Bottom line

ENZL เป็น iShares MSCI New Zealand ETF, canonical `NASDAQ:ENZL`, กองทุน passive,
index-tracking equity ETF ที่ติดตาม MSCI New Zealand All Cap Top 25 Capped Index
(Net). Official iShares standardized performance ยืนยัน rolling 10-year NAV TR
cumulative `38.78%` และ CAGR `3.33%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ
`10.00` elapsed years; normalized TR คือ 100.00 เป็น 138.78. Current official
NAV TR YTD คือ `3.45%` ณ 2026-07-21. Official calendar NAV rows ที่เปิดเผยใน
current factsheet มี 2021-2025; annual rows 2016-2020 และ annual benchmark rows
ไม่เปิดเผยใน reviewed official capture.

## Performance check

- entity_key: NASDAQ:ENZL
- Inception: 2010-09-01
- Metric: NAV Total Return including reinvested distributions and fund expenses; iShares' hypothetical-growth method reinvests dividends/capital gains and deducts fund expenses
- Tracked index (issuer benchmark): MSCI New Zealand All Cap Top 25 Capped Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR cumulative / CAGR: `38.78%` / `3.33%` (official iShares current standardized performance)
- Normalized NAV TR: start `100.00`; end `138.78` (official cumulative return; raw NAV endpoints are not disclosed)
- Available official calendar rows 2021-2025 compound to `-25.33%` / CAGR `-5.67%`; S&P 500 rows in the same window compound to `96.17%` / CAGR `14.43%`; ENZL trails by approximately `20.10 pp` CAGR
- Coverage/source note: rolling 10-year summary and standardized YTD table are as of 2026-06-30; current YTD is as of 2026-07-21; the benchmark's annual rows are not disclosed in the reviewed official capture

| Year | ENZL NAV TR | MSCI New Zealand Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | -10.86% | not disclosed | 28.71% |
| 2022 | -16.63% | not disclosed | -18.11% |
| 2023 | 3.53% | not disclosed | 26.29% |
| 2024 | -4.55% | not disclosed | 25.02% |
| 2025 | 1.68% | not disclosed | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ ENZL;
ตารางใช้ cached USD Total Return convention สำหรับ 2016-2025. Annual ENZL
rows 2021-2025 มาจาก official iShares factsheet; ไม่สร้าง proxy สำหรับ 2016-2020.

## Common-window comparison

- ENZL 2021-2025 NAV TR cumulative / CAGR: `-25.33%` / `-5.67%`
- S&P 500 2021-2025 TR cumulative / CAGR: `96.17%` / `14.43%`
- ENZL trails by approximately `20.10 pp` CAGR in the common calendar window.
- Up years / Down years in 2021-2025: `2 / 3`
- Best year: 2023, `3.53%`; worst year: 2022, `-16.63%`
- Current official NAV TR YTD: `3.45%` as of 2026-07-21; latest NAV `US$46.36` as of 2026-07-21

## Risk read-through

ENZL เป็น single-country New Zealand equity ETF; official factsheet ณ 2026-03-31
มี 25 holdings, expense ratio `0.50%`, 3-year standard deviation `15.48%`,
3-year beta `0.90`, และ sector exposureหลัก Health Care `29.00%`, Industrials
`22.47%`, Utilities `13.93%`, Real Estate `12.65%`, และ Financials `12.53%`.
Factsheet ระบุว่า benchmark เปลี่ยนจาก MSCI New Zealand IMI 25/50 Index (Net)
เป็น MSCI New Zealand All Cap Top 25 Capped Index (Net) ตั้งแต่ 2024-09-03;
จึงต้องอ่านผล rolling window ข้ามช่วงดังกล่าวด้วย caveat นี้. Daily NAV history
ที่ยืนยันได้เพียงพอสำหรับ max drawdown และ recovery คือ `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official iShares product and performance page: https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239672&seoSlug=ishares-msci-new-zealand-capped-etf
- Official iShares factsheet: https://www.ishares.com/us/literature/fact-sheet/enzl-ishares-msci-new-zealand-etf-fund-fact-sheet-en-us.pdf
- Official iShares summary prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-new-zealand-capped-etf-8-31.pdf
- Official iShares annual report: https://www.blackrock.com/us/individual/literature/annual-report/ar-enzl-en.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
