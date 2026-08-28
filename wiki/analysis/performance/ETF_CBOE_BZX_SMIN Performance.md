---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:SMIN
ticker: SMIN
exchange: Cboe BZX
fund: iShares MSCI India Small-Cap ETF
tracked_index: MSCI India Small Cap Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-28
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-25
price_nav_as_of: 2026-08-25
fund_facts_as_of: 2026-08-25
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return; gross income reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SMIN
  - geography/India
---

# SMIN Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

SMIN เป็น passive/index-tracking small-cap equity ETF ของ iShares ที่ติดตาม
`MSCI India Small Cap Index (Net)` และจดทะเบียนบน Cboe BZX. Official rolling
10-year NAV Total Return ณ 2026-06-30 อยู่ที่ cumulative `152.70%` และ CAGR
`9.71%`; latest current date-to-date NAV Total Return YTD อยู่ที่ `2.57%` ณ
2026-08-25. ตัวเลขหลักเป็น NAV Total Return ที่รวมการ reinvest dividends/capital
gains และหัก fund expenses ตามคำอธิบายของ issuer.

## Performance check

- `entity_key`: `Cboe BZX:SMIN`
- Fund: iShares MSCI India Small-Cap ETF; asset class `Equity`; expense ratio `0.74%`
- Inception: `2012-02-08`
- Metric: official NAV Total Return, รวม reinvested distributions และหัก fund expenses แล้ว
- Tracked index (issuer benchmark): `MSCI India Small Cap Index (Net)`
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Management mode: `passive-index`
- 10-year coverage: official rolling performance from `2016-06-30` to `2026-06-30`; actual years `10.00`
- Start TR value: `100.00` normalized; end TR value: `252.70` normalized, derived from official cumulative return `152.70%`; raw NAV endpoints are not disclosed
- 10-year NAV TR CAGR: `9.71%` issuer-reported average annual NAV Total Return as of `2026-06-30`
- Formula: `(End TR / Start TR)^(1 / Years) - 1 = (252.70 / 100.00)^(1 / 10.00) - 1`, approximately `9.71%`
- Official rolling annualised NAV TR fields as of `2026-06-30`: 1-year `-7.02%`, 3-year `9.79%`, 5-year `7.42%`, 10-year `9.71%`, and since inception `9.00%`
- Current snapshot: NAV `USD 71.90`, closing price `USD 72.13`, net assets `USD 772,891,256`, and `461` holdings, all as of `2026-08-25`; current NAV TR YTD is `2.57%` as of `2026-08-25`.
- Coverage/source note: the official page provides rolling and current date-to-date fields; the June 2026 factsheet provides 2021-2025 calendar rows. The normalized endpoint is derived from the rounded official cumulative metric, not a proxy or market-price return.

| Year | SMIN NAV TR | MSCI India Small Cap Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | 44.69% | 51.13% | 28.71% |
| 2022 | -13.98% | -13.43% | -18.11% |
| 2023 | 34.80% | 42.63% | 26.29% |
| 2024 | 17.34% | 22.63% | 25.02% |
| 2025 | -6.82% | -7.92% | 17.88% |
| 2026 YTD (month-end) | -0.02% | 1.08% | not comparable; current year not cached |

MSCI India Small Cap Index (Net) เป็น issuer benchmark ของ SMIN; S&P 500 เป็น
common reference benchmark ไม่ใช่ issuer benchmark. ตาราง S&P ใช้ cached USD
Total Return convention ณ 2025-12-31. ช่วง annual comparison ที่เปิดเผยตรงกัน
คือ 2021-2025. Month-end 2026 YTD เป็นข้อมูล ณ 2026-06-30 และ current
product-page YTD ถูกเก็บแยกเป็นข้อมูล ณ 2026-08-25.

## Up years / Down years

- Up years / Down years: `6 / 5` in complete 2015-2025 rows assembled from the official prospectus and June 2026 factsheet
- Best: 2017, `+61.78%`
- Least positive: 2015, `+2.02%`
- Worst: 2018, `-25.43%`
- Least bad down year: 2016, `-0.42%`
- 2015-2025 cumulative / rounded-input CAGR: `153.86%` / `8.84%`; 2021-2025 cumulative / CAGR: `83.44%` / `12.90%`
- MSCI India Small Cap Index (Net) 2021-2025 cumulative / CAGR: `110.71%` / `16.07%`; SMIN trails by approximately `3.17 pp` CAGR, a tracking comparison rather than alpha.
- S&P 500 TR 2021-2025 cumulative / CAGR: `96.17%` / `14.43%`; SMIN trails the common reference by approximately `1.53 pp` CAGR.
- Current date-to-date YTD: `2.57%` NAV as of `2026-08-25`
- Standardized month-end YTD: `-0.02%` NAV as of `2026-06-30`; kept separate from the later date-to-date observation

## Risk read-through

SMIN มี small-cap India exposure และมี official `461` holdings ณ 2026-08-25.
Official 3-year standard deviation อยู่ที่ `18.82%` และ equity beta `0.46` ณ
2026-07-31; P/B `3.59` และ P/E `32.69` ณ 2026-08-25. Sector exposure ล่าสุด
นำโดย Industrials `19.70%`, Financials `17.14%`, Health Care `15.14%`, Consumer
Discretionary `14.73%` และ Materials `11.84%` ณ 2026-08-25. ความเสี่ยงหลักคือ
small-cap liquidity, India country/sector concentration และ valuation/FX
sensitivity. Daily NAV history สำหรับคำนวณ max drawdown และ recovery:
`ไม่พบข้อมูลที่ยืนยันได้`.

## 2026-08-17 Refresh

- Official iShares page reports NAV Total Return YTD 2.50% as of 2026-08-13, NAV US$71.42 and closing price US$71.43 as of 2026-08-14, 30-day SEC yield -0.07% as of 2026-07-31, and 461 holdings as of 2026-08-13.
- The official summary prospectus supplies calendar NAV rows for 2015-2024 and the official June 2026 factsheet supplies 2025; the available 2015-2025 compound is 153.86% cumulative / rounded-input CAGR 8.84%. The strict common comparison remains the issuer-published 2021-2025 rows: 83.44% cumulative / 12.90% CAGR.
- The MSCI India Small Cap Index (Net) is the issuer benchmark. For 2021-2025, SMIN's annual benchmark-relative returns were -6.44, -0.55, -7.83, -5.29 and +1.10 percentage points; the five-year excess CAGR was -3.17 percentage points. This is tracking evidence, not alpha.
- The current 2026-08-13 YTD has no same-date official benchmark pair in the captured sources; the 2026-06-30 standardized page remains separate at -0.02% NAV versus benchmark +1.08%.

## Sources

- Official iShares product and performance page: https://www.ishares.com/us/products/239660/SMIN
- Official iShares SMIN factsheet: https://www.ishares.com/us/literature/fact-sheet/smin-ishares-msci-india-small-cap-etf-fund-fact-sheet-en-us.pdf
- Official iShares SMIN Summary Prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-india-small-cap-etf-8-31.pdf
- Official MSCI India Small Cap Index factsheet: https://www.msci.com/documents/10199/255599/msci-india-small-cap-index.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
