---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FJP
ticker: FJP
exchange: NASDAQ
fund: First Trust Japan AlphaDEX Fund
tracked_index: Nasdaq AlphaDEX Japan Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FJP
  - geography/Japan
---

# FJP Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

FJP เป็น First Trust Japan AlphaDEX Fund, canonical `NASDAQ:FJP`, กองทุน
passive, index-tracking equity ETF ที่ติดตาม Nasdaq AlphaDEX Japan Index.
Official First Trust standardized performance ยืนยัน rolling 10-year NAV TR CAGR
`7.55%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ `10.00` elapsed years; raw
endpoints และ official rolling cumulative endpoint ไม่เปิดเผย. Annual rows
2016-2025 จาก official factsheet compound เป็น `76.82%` / CAGR `5.87%`.
Current standardized NAV TR YTD คือ `14.26%` ณ 2026-06-30.

## Performance check

- entity_key: NASDAQ:FJP
- Inception: 2011-04-18
- Metric: NAV Total Return including reinvested distributions and fund expenses; First Trust defines NAV return as including reinvested distributions at NAV
- Tracked index (issuer benchmark): Nasdaq AlphaDEX Japan Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR CAGR: `7.55%` (official First Trust; raw rolling endpoints not disclosed)
- Available official calendar rows 2016-2025 compound to `76.82%` / CAGR `5.87%`; S&P 500 rows in the same window compound to `298.33%` / CAGR `14.82%`
- Common 2021-2025 FJP NAV TR compound / CAGR: `49.56%` / `8.38%`; S&P 500 common-window compound / CAGR: `96.17%` / `14.43%`; FJP trails by approximately `6.04 pp` CAGR
- Coverage/source note: rolling 10-year and YTD summary are as of 2026-06-30; current NAV is as of 2026-07-21; the underlying index changed from Defined Japan Index to Nasdaq AlphaDEX Japan Index on 2015-07-14, so pre-change history has a methodology caveat

| Year | FJP NAV TR | Nasdaq AlphaDEX Japan TR | MSCI Japan TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2016 | 2.91% | not disclosed | 2.38% | 11.96% |
| 2017 | 26.70% | not disclosed | 23.99% | 21.83% |
| 2018 | -17.66% | not disclosed | -12.88% | -4.38% |
| 2019 | 8.27% | not disclosed | 19.61% | 31.49% |
| 2020 | 1.71% | not disclosed | 14.48% | 18.40% |
| 2021 | -0.69% | not disclosed | 1.71% | 28.71% |
| 2022 | -12.04% | not disclosed | -16.65% | -18.11% |
| 2023 | 22.42% | not disclosed | 20.32% | 26.29% |
| 2024 | 5.84% | not disclosed | 8.31% | 25.02% |
| 2025 | 32.14% | not disclosed | 24.60% | 17.88% |

S&P 500 และ MSCI Japan เป็น common reference benchmarks ไม่ใช่ issuer
benchmark ของ FJP; ตารางใช้ cached USD Total Return convention ของ S&P สำหรับ
2016-2025. Annual FJP/MSCI rows มาจาก official First Trust factsheet ณ
2026-03-31; annual Nasdaq AlphaDEX rows ไม่เปิดเผยใน reviewed official capture.

## Common-window comparison

- FJP 2021-2025 NAV TR cumulative / CAGR: `49.56%` / `8.38%`
- S&P 500 2021-2025 TR cumulative / CAGR: `96.17%` / `14.43%`
- FJP trails by approximately `6.04 pp` CAGR in the common calendar window.
- Up years / Down years in 2021-2025: `3 / 2`
- Best year: 2025, `32.14%`; worst year: 2022, `-12.04%`
- Current official NAV TR YTD: `14.26%` as of 2026-06-30; latest NAV `US$73.56` as of 2026-07-21

## Risk read-through

FJP เป็น Japan factor-tilted equity ETF; official data ณ 2026-07-21 มี 100
holdings, expense ratio `0.80%`, 3-year standard deviation `15.64%`, beta `0.95`,
และ sector exposureหลัก Industrials `30.93%`, Consumer Discretionary `19.69%`,
Information Technology `14.96%`, Financials `11.35%`, และ Materials `7.90%`.
กองทุน reconstitute/rebalance semi-annually และมี value/growth selection risk,
Japan/country, sector, currency และ methodology-change risk. Daily NAV history
ที่ยืนยันได้เพียงพอสำหรับ max drawdown และ recovery คือ `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official First Trust FJP summary page: https://www.ftportfolios.com/Retail/etf/etfsummary.aspx?Ticker=FJP
- Official First Trust FJP factsheet: https://www.ftportfolios.jp/content/funds/etf/fjp/firsttrustjapanfactsheetinstitutional
- SEC summary prospectus (May 1, 2026): https://www.sec.gov/Archives/edgar/data/1510337/000144554626003319/fjp_497k.htm
- SEC annual report / N-CSR performance cross-check: https://www.sec.gov/Archives/edgar/data/1510337/000144554626001916/adex2_ncsr.htm
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
