---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FNDC
ticker: FNDC
exchange: NYSE Arca
fund: Schwab Fundamental International Small Equity ETF
tracked_index: RAFI Fundamental High Liquidity Developed ex US Small Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-09-02
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28 / 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-1.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FNDC
  - geography/International
---

# FNDC Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

FNDC ให้ cumulative NAV Total Return `118.08%` หรือ rounded-input CAGR `8.11%`
ใน complete calendar years 2016-2025. ช่วง 2021-2025 ให้ cumulative `48.65%`
และ CAGR `8.25%`, เทียบ S&P 500 TR ที่ `96.17%` / `14.43%` ในช่วงเดียวกัน.
ผลตอบแทนรายปีเป็นบวก 8 ปีและลบ 2 ปี; ปีที่ดีที่สุดคือ 2025 ที่ `35.79%` และ
แย่ที่สุดคือ 2018 ที่ `-18.77%`. Current YTD NAV TR ล่าสุดจาก issuer คือ
`10.96%` ณ 31 ก.ค. 2026; NAV ล่าสุดคือ `$51.52` และ market price คือ `$51.34`
ณ 28 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:FNDC`; fund: Schwab Fundamental International Small Equity ETF
- Inception: `2013-08-15`; exchange: `NYSE Arca`
- Expense ratio: `0.390%`
- Metric: `NAV Total Return` รวม distributions ที่ reinvested และ fund expenses; currency USD
- Tracked index: `RAFI Fundamental High Liquidity Developed ex US Small Index (Net)`; product page ระบุ management style เป็น `Passive` และ SEC ระบุว่าเป็น index fund ที่ใช้ sampling
- Index history caveat: ก่อน 21 มิ.ย. 2024 ใช้ `Russell RAFI Developed ex US Small Company Index (Net)`; หลังจากนั้นใช้ RAFI Fundamental High Liquidity Developed ex US Small Index (Net). Annual fund NAV rows จึงยังใช้ต่อเนื่องได้ แต่ issuer benchmark history มีการเปลี่ยน
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; ใช้เป็น reference benchmark ไม่ใช่ issuer benchmark)
- Official rolling 10-year NAV TR: `8.48%` average annual return ณ 31 ก.ค. 2026; issuer ไม่เปิดเผย raw rolling endpoints ใน capture ที่ตรวจ
- Calendar-window calculation: 2016-01-01 ถึง 2025-12-31; Start TR index `100.00`, End TR index `218.08`, Years `10.00`; สูตร `(218.08 / 100.00)^(1 / 10.00) - 1 = 8.11%`. เป็น rounded-input approximation จาก annual rows ทางการ 10 แถว โดยค่า source precision ของ 2024 และ 2025 ถูกเก็บใน source batch
- Current official snapshot: NAV `$51.52`, market price `$51.34`, premium/discount `-0.35%`, net assets `$3.189B`, and `1,588` holdings as of 28 ส.ค. 2026; portfolio turnover `25.61%` as of 31 ก.ค. 2026. These dates are separate from the YTD field.
- Coverage: annual NAV TR rows ครบ 2016-2025 ไม่มี proxy หรือ partial-year marker; current YTD เป็น month-end 31 ก.ค. 2026 และ quote/NAV snapshot เป็น 28 ส.ค. 2026

| ปี | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 8.87% | 11.96% |
| 2017 | 29.04% | 21.83% |
| 2018 | -18.77% | -4.38% |
| 2019 | 20.02% | 31.49% |
| 2020 | 7.11% | 18.40% |
| 2021 | 9.83% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 15.21% | 26.29% |
| 2024 | 1.57% | 25.02% |
| 2025 | 35.79% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2`
- Best: `2025`, `35.79%`
- Least positive: `2024`, `1.57%`
- Worst: `2018`, `-18.77%`
- Least bad down year: `2022`, `-14.82%`
- 2021-2025: FNDC cumulative `48.65%`, CAGR `8.25%`; S&P 500 cumulative `96.17%`, CAGR `14.43%`
- Current YTD: FNDC `10.96%` NAV TR ณ 31 ก.ค. 2026. Official S&P 500 TR current fieldที่ตรวจพบคือ `14.04%` ณ 10 ส.ค. 2026; วันอ้างอิงไม่ตรงกัน จึงไม่สรุปเป็น same-date spread

## Risk read-through

Schwab รายงาน 3-year standard deviation `15.14%` ณ 31 ก.ค. 2026; sample standard
deviation ที่คำนวณจาก annual NAV rows 2016-2025 คือ `17.24%` และไม่ใช่ daily
volatility. Year-end-observation drawdown approximation อยู่ที่ประมาณ `-18.77%`
ในปี 2018 จากจุดสูงสุดสิ้นปี 2017 และ cumulative year-end กลับเหนือจุดสูงสุดเดิม
ได้ภายในสิ้นปี 2020; นี่ไม่ใช่ daily maximum drawdown.

FNDC เป็น developed ex-U.S. small-cap fundamental/value-tilt ETF จึงมีความเสี่ยง
จาก small-cap liquidity, foreign currency, country/sector concentration, factor
underperformance และ tracking/index-reconstitution risk. Distribution yield `3.65%`
ณ 31 ก.ค. 2026 เป็นคนละ metric กับ NAV total return.

## Driver notes

- Fundamental index ใช้ adjusted sales, retained operating cash flow และ dividends plus buybacks แทน market capitalization เพื่อจัดอันดับและถ่วงน้ำหนัก
- Index reconstitution ทำเป็น annual selection และ partial quarterly rebalancing ตาม prospectus; fund ใช้ sampling และอาจถือหลักทรัพย์นอก index เพื่อการติดตาม
- 2018 เป็น down year ที่แย่ที่สุดในช่วงที่ตรวจ; 2025 เป็นปีที่ดีที่สุด ขณะที่ 2022 สะท้อน small-cap/foreign-equity cycle sensitivity

## Sources

- [Schwab FNDC product page](https://www.schwabassetmanagement.com/products/fndc) — fund identity, passive style, index, fees, NAV, rolling/YTD return, risk fields, and portfolio snapshot
- [Schwab FNDC documents](https://www.schwabassetmanagement.com/products/fndc/documents?page=0) — issuer document hub and performance-summary/factsheet links
- [Schwab ETF Investment Performance Summary](https://www.schwabassetmanagement.com/resource/etf-investment-performance-summary) — official performance-report entry updated 31 ก.ค. 2026
- [SEC FNDC summary prospectus](https://www.sec.gov/Archives/edgar/data/1454889/000088454626000301/c497k.htm) — annual total returns, index methodology, passive/index-fund treatment, benchmark change, and return definitions
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- [S&P 500 current return page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page) — official current S&P 500 TR field `14.04%` displayed for 10 ส.ค. 2026
- [S&P 500 cached source 1](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [source 2](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [source 3](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-2021/), [source 4](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — cached 2016-2025 USD gross S&P 500 TR rows
- Source batch: [[ETF_performance_sources_2026-09-02_run-1]]
