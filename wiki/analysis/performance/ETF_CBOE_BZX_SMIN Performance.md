---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:SMIN
ticker: SMIN
exchange: Cboe BZX
fund: iShares MSCI India Small-Cap ETF
tracked_index: MSCI India Small Cap Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SMIN
  - geography/India
---

# SMIN Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

SMIN เป็น passive/index-tracking small-cap equity ETF ของ iShares ที่ติดตาม
MSCI India Small Cap Index (Net) และจดทะเบียนบน Cboe BZX. Official rolling
10-year NAV Total Return ณ 2026-06-30 อยู่ที่ cumulative 152.70% และ CAGR
9.71%; latest current date-to-date NAV Total Return YTD อยู่ที่ 2.50% ณ
2026-08-13. ตัวเลขหลักเป็น NAV Total Return ที่รวมการ reinvest dividends/capital
gains และหัก fund expenses ตามคำอธิบายของ issuer.

## Performance check

- entity_key: Cboe BZX:SMIN
- Inception: 2012-02-08
- Expense ratio: 0.74% (current prospectus; exact fee as-of date not disclosed)
- Metric: NAV Total Return รวม reinvested distributions และ fund expenses; issuer ระบุว่า Growth of Hypothetical $10,000 หัก fund expenses แล้ว
- Tracked index (issuer benchmark): MSCI India Small Cap Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year coverage: official rolling performance from 2016-06-30 to 2026-06-30; actual years 10.00
- Start TR value: 100.00 normalized; End TR value: 252.70 normalized, derived from official cumulative return 152.70%; raw NAV endpoints are not disclosed
- 10-year NAV TR CAGR: 9.71% issuer-reported average annual NAV Total Return
- Formula: (End TR / Start TR)^(1 / Years) - 1 = (252.70 / 100.00)^(1 / 10.00) - 1 = approximately 9.71%
- Coverage/source note: official page provides rolling 10-year cumulative/average annual returns as of 2026-06-30 and calendar rows 2021-2025. The normalized endpoint is derived from the rounded official cumulative metric, not a proxy or market-price return.

| Year | SMIN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 44.69% | 28.71% |
| 2022 | -13.98% | -18.11% |
| 2023 | 34.80% | 26.29% |
| 2024 | 17.34% | 25.02% |
| 2025 | -6.82% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ SMIN;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31. ช่วง annual
comparison ที่เปิดเผยตรงกันคือ 2021-2025.

## Up years / Down years

- Up years / Down years: 6 / 5 ใน complete 2015-2025 rows ที่ issuer เปิดเผย
- Best: 2017, +61.78%
- Least positive: 2015, +2.02%
- Worst: 2018, -25.43%
- Least bad down year: 2016, -0.42%
- 2021-2025 cumulative / CAGR: 83.44% / 12.90%; S&P 500 TR: 96.17% / 14.43%
- Current date-to-date YTD: 2.50% NAV as of 2026-08-13
- Standardized month-end YTD: -0.02% NAV as of 2026-06-30; kept separate from the later date-to-date observation

## Risk read-through

SMIN มี small-cap India exposure และมี official 461 holdings ณ 2026-08-13.
Official 3-year standard deviation อยู่ที่ 18.82% และ equity beta 0.46 ณ
2026-07-31. ความเสี่ยงหลักคือ small-cap liquidity, India country/sector
concentration และ valuation/FX sensitivity. Daily NAV history สำหรับคำนวณ
max drawdown และ recovery: ไม่พบข้อมูลที่ยืนยันได้.

## 2026-08-17 Refresh

- Official iShares page reports NAV Total Return YTD 2.50% as of 2026-08-13, NAV US$71.42 and closing price US$71.43 as of 2026-08-14, 30-day SEC yield -0.07% as of 2026-07-31, and 461 holdings as of 2026-08-13.
- The official summary prospectus supplies calendar NAV rows for 2015-2024 and the official June 2026 factsheet supplies 2025; the available 2015-2025 compound is 153.86% cumulative / rounded-input CAGR 8.84%. The strict common comparison remains the issuer-published 2021-2025 rows: 83.44% cumulative / 12.90% CAGR.
- The MSCI India Small Cap Index (Net) is the issuer benchmark. For 2021-2025, SMIN's annual benchmark-relative returns were -6.44, -0.55, -7.83, -5.29 and +1.10 percentage points; the five-year excess CAGR was -3.17 percentage points. This is tracking evidence, not alpha.
- The current 2026-08-13 YTD has no same-date official benchmark pair in the captured sources; the 2026-06-30 standardized page remains separate at -0.02% NAV versus benchmark +1.08%.

## Sources

- Official iShares product and performance page: https://www.ishares.com/us/products/239660/ishares-msci-india-smallcap-etf
- Official iShares SMIN factsheet: https://www.ishares.com/us/literature/fact-sheet/smin-ishares-msci-india-small-cap-etf-fund-fact-sheet-en-us.pdf
- Official iShares SMIN Summary Prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-india-small-cap-etf-8-31.pdf
- Official MSCI India Small Cap Index factsheet: https://www.msci.com/documents/10199/255599/msci-india-small-cap-index.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
