---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:ESML
ticker: ESML
exchange: Cboe BZX
fund: iShares ESG Aware MSCI USA Small-Cap ETF
tracked_index: MSCI USA Small Cap Extended ESG Focus Index
benchmark: S&P 500 Total Return
updated: 2026-08-15
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-13
source_batch: raw/imports/ETF_performance_sources_2026-08-15.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ESML
  - geography/United-States
---

# ESML Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

ESML เป็น iShares ESG Aware MSCI USA Small-Cap ETF, passive/index-tracking
U.S. small-cap equity ETF บน Cboe BZX ที่ติดตาม MSCI USA Small Cap Extended ESG
Focus Index. Official complete calendar-year NAV Total Return ที่ยืนยันได้ครอบคลุม
2019-2025: cumulative 120.70% และ CAGR ประมาณ 11.97% จาก rounded annual inputs.
Current official NAV TR YTD อยู่ที่ +23.07% ณ 2026-08-13 เทียบกับ S&P 500 Gross
Total Return +14.04% ณ 2026-08-10; วันที่ benchmark ใกล้สุดต่างกันสามวัน.

## Performance check

- entity_key: Cboe BZX:ESML
- Inception: 2018-04-10
- Expense ratio: 0.17%
- Metric: NAV Total Return รวม reinvested distributions และ fund expenses; USD
- Tracked index (issuer benchmark): MSCI USA Small Cap Extended ESG Focus Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: not applicable (<10 years); inception-year 2018 partial return ไม่พบข้อมูลที่ยืนยันได้
- Available official complete calendar rows: 2019-2025; 2021-2025 cumulative 43.37% / CAGR 7.47%
- S&P 500 2021-2025 cached TR: cumulative 96.17% / CAGR 14.43%
- Coverage/source note: annual NAV rows use official iShares sources; current ESML NAV/YTD is as of 2026-08-13; current S&P 500 Gross TR YTD is as of 2026-08-10.

| Year | ESML NAV TR | MSCI USA Small Cap Extended ESG Focus Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2019 | 28.53% | 28.70% | 31.49% |
| 2020 | 19.77% | 20.00% | 18.40% |
| 2021 | 19.31% | 19.54% | 28.71% |
| 2022 | -17.22% | -17.22% | -18.11% |
| 2023 | 17.31% | 17.26% | 26.29% |
| 2024 | 11.86% | 12.08% | 25.02% |
| 2025 | 10.62% | 10.83% | 17.88% |

2019-2020 issuer-benchmark values are displayed rounded to one decimal in the
official source. S&P 500 annual rows reuse the cached USD Total Return convention
with dividends reinvested, as of 2025-12-31; it is not ESML's issuer benchmark.

## Up years / Down years

- Up years / Down years: 6 / 1 in the available complete rows 2019-2025
- Best: 2019, +28.53%
- Least positive: 2025, +10.62%
- Worst: 2022, -17.22%
- Least bad down year: 2022, -17.22%
- Current ESML NAV TR YTD: +23.07% as of 2026-08-13
- S&P 500 Gross TR YTD: +14.04% as of 2026-08-10; nearest official benchmark date

## Risk read-through

ESML มี U.S. small-cap และ ESG-screen exposure จึงยังมี equity, cyclicality และ
small-cap liquidity risk แม้เป็น passive fund. Official evidence ระบุ worst quarter
-30.78% ใน Q1 2020 และ best quarter +29.31% ใน Q4 2020. จาก annual NAV path
หลัง 2021 year-end ที่ 100.00, สิ้นปี 2022 อยู่ที่ 82.78, 2023 ที่ 97.11,
2024 ที่ 108.63 และ 2025 ที่ 120.16; จึงกลับมาเหนือระดับสิ้นปี 2021 ได้ภายใน
สิ้นปี 2024. นี่ไม่ใช่ official daily NAV maximum drawdown หรือ exact recovery date;
ข้อมูลดังกล่าว: ไม่พบข้อมูลที่ยืนยันได้. Secondary price-based drawdown/recovery
จาก Trefis แยกไว้ต่างหากและไม่ปะปนกับ NAV Total Return.

## Sources

- [Official iShares ESML product page](https://www.ishares.com/us/products/296644/ESML)
- [Official iShares ESML professional performance page](https://www.ishares.com/ch/professionals/en/products/296644/ishares-esg-aware-msci-usa-small-cap-etf-fund)
- [Official iShares factsheet](https://www.ishares.com/us/literature/fact-sheet/esml-ishares-esg-aware-msci-usa-small-cap-etf-fund-fact-sheet-en-us.pdf)
- [Official iShares summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-msci-usa-small-cap-esg-optimized-etf-8-31.pdf)
- [Official S&P DJI August Index Returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page)
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- [Trefis ESML performance](https://www.trefis.com/data/companies/ESML) (secondary, price-based drawdown context only)
- ETF source batch: [[ETF_performance_sources_2026-08-15]] | [[ETF Performance Index]]
