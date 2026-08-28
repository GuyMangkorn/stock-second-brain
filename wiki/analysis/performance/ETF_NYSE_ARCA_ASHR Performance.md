---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ASHR
ticker: ASHR
exchange: NYSE Arca
fund: Xtrackers Harvest CSI 300 China A-Shares ETF
tracked_index: CSI 300 Index
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-28
performance_as_of: 2026-06-30
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/ASHR
  - geography/China
---

# ASHR Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

ASHR เป็น passive/index-tracking China A-share equity ETF ของ Xtrackers/Harvest
ติดตาม `CSI 300 Index` และเริ่มกองทุนเมื่อ 2013-11-05. Official Q2 factsheet
ณ 2026-06-30 รายงาน NAV Total Return 3-month `13.88%`, rolling 1-year
`35.88%`, 3-year annualized `13.23%`, 5-year annualized `-0.51%` และ
10-year annualized `5.84%`. ช่วง 10-year คือ 2016-06-30 ถึง 2026-06-30
ครบ `10.00` ปี; raw endpoints และ cumulative rolling return ไม่ได้เปิดเผย
จึง normalize ได้เพียงประมาณ 176.40 จาก 100.00. Current NAV TR YTD คือ
`ไม่พบข้อมูลที่ยืนยันได้` เพราะ reviewed current factsheet ไม่ได้เปิดเผย YTD.

## Performance check

- `entity_key`: `NYSE Arca:ASHR`
- Fund: Xtrackers Harvest CSI 300 China A-Shares ETF; asset class `Equity`; net expense ratio `0.65%`
- Inception: `2013-11-05`
- Metric: official NAV Total Return, รวม reinvested distributions และหัก fund expenses แล้ว
- Issuer benchmark: CSI 300 Index; 300 large- and mid-cap China A-share stocks listed on Shenzhen or Shanghai, free-float/capitalization-weighted index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Type note: DWS prospectus explicitly describes a passive/indexing approach and an at-least-80% exposure policy to A-shares or qualifying exposure instruments; derivatives and other instruments are permitted for implementation/risk management but the fund is not derivative-heavy by the reviewed strategy description.
- Current official Q2 factsheet fields as of 2026-06-30: NAV TR 3-month 13.88%, 1-year 35.88%, 3-year annualized 13.23%, 5-year annualized -0.51%, 10-year annualized 5.84%, and since ETF inception 6.30%; no current NAV/market-price snapshot or current YTD field was disclosed in the reviewed factsheet.

### Official 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2016-06-30 | 2026-06-30 | 10.00 | 100.00 (normalized) | approx. 176.40 (calculated from official CAGR) | approx. 76.40% (calculated) | 5.84% | Raw start/end and cumulative rolling NAV TR not disclosed |

สูตร normalized endpoint: `100.00 × (1 + 5.84%)^10.00 = 176.40`; ค่านี้เป็นการคำนวณจาก issuer-reported 10-year CAGR ไม่ใช่ raw NAV และไม่ใช่ proxy.

### Annual NAV Total Return

| Year | ASHR NAV TR | CSI 300 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -15.06% | not disclosed | 11.96% |
| 2017 | 31.81% | not disclosed | 21.83% |
| 2018 | -28.05% | not disclosed | -4.38% |
| 2019 | 35.57% | not disclosed | 31.49% |
| 2020 | 37.42% | not disclosed | 18.40% |
| 2021 | -2.17% | not disclosed | 28.71% |
| 2022 | -26.98% | not disclosed | -18.11% |
| 2023 | -13.07% | not disclosed | 26.29% |
| 2024 | 12.55% | not disclosed | 25.02% |
| 2025 | not disclosed | not disclosed | 17.88% |
| 2026 YTD | not disclosed | not disclosed | not comparable; current year not cached |

### Official rolling comparison

| Window ended 2026-06-30 | ASHR NAV TR | CSI 300 Index TR | Difference |
|---|---:|---:|---:|
| 3-month | 13.88% | 14.68% | -0.80 pp |
| 1-year | 35.88% | 36.47% | -0.59 pp |
| 3-year annualized | 13.23% | 14.21% | -0.98 pp |
| 5-year annualized | -0.51% | 0.30% | -0.81 pp |
| 10-year annualized | 5.84% | 6.65% | -0.81 pp |
| Since ETF inception | 6.30% | 7.24% | -0.94 pp |

The CSI 300 Index returns are gross of fees; the differences are tracking and
fee-related comparisons, not alpha.

ASHR NAV rows `2016-2024` come from the official DWS prospectus calendar-year table for the period ended `2024-12-31`; the current Q2 2026 factsheet provides the rolling 10-year result but does not disclose 2025 calendar NAV rows in the reviewed capture. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`; no value is invented for ASHR 2025 or current YTD.

### Window calculations and ranking

- Complete disclosed calendar window `2016-2024`: ASHR NAV TR cumulative `4.89%`, CAGR `0.53%` over 9 complete years.
- Common disclosed window `2021-2024`: ASHR NAV TR cumulative `-30.11%`, CAGR `-8.57%`; S&P 500 TR cumulative `66.41%`, CAGR `13.58%`; ASHR trails by approximately `22.15 pp` CAGR.
- Up years / down years in `2016-2024`: `4 / 5`.
- Best disclosed complete year: `2020`, `37.42%`; least positive: `2024`, `12.55%`.
- Worst disclosed complete year: `2018`, `-28.05%`; least bad down year: `2021`, `-2.17%`.
- Current NAV TR YTD: `ไม่พบข้อมูลที่ยืนยันได้`; no current date-to-date value is used.

## Risk read-through

ASHR เป็น single-country China A-share exposure. Q2 2026 official factsheet reports `288` holdings, net assets about `$1.64B`, and expense ratio `0.65%` as of `2026-06-30`. A-share access, Stock Connect/QFI implementation, China policy/geopolitical risk, currency, liquidity, sector concentration and possible government restrictions can increase volatility. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official DWS Q2 2026 factsheet: https://etf.dws.com/download/asset/e73aaa93-92c6-4a51-9233-38ccb329e09b
- Official DWS prospectus (October 1, 2025): https://etf.dws.com/en-us/AssetDownload/Index/ce51b065-fc18-496f-9b88-8996a37d16b3/CHINA-1-Prospectus.pdf
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-28]]
- Navigation: [[China ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
