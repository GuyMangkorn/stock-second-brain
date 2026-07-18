---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWG
ticker: EWG
exchange: NYSE Arca
fund: iShares MSCI Germany ETF
tracked_index: MSCI Germany Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-13
price_nav_as_of: 2026-07-14
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWG
  - geography/Germany
---

# EWG Performance

## Bottom line

EWG ให้ cumulative `NAV Total Return` ประมาณ `103.85%` ในปี 2016-2025 หรือ
CAGR `7.38%`; บวก 8 ปีและลบ 2 ปี เทียบ S&P 500 TR CAGR `14.82%`. ปีดีที่สุด
คือ 2025 `+35.15%`; แย่ที่สุดคือ 2018 `-22.30%`. 2026 YTD ของ EWG คือ
`-0.85%` ณ 13 ก.ค.; S&P 500 TR `+9.64%` ณ 17 ก.ค. จึงไม่ใช่ same-date comparison.

## Performance check

- `entity_key: NYSE Arca:EWG`
- Inception: 12 มี.ค. 1996
- Metric: `NAV Total Return` (USD), distributions reinvested หลังหัก fund expenses
- Tracked index (issuer benchmark): `MSCI Germany Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ EWG)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `8.22%`; Start TR value: `100.00`; End TR value:
  `220.25`; Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; End TR เป็น normalized
  calculation จาก official cumulative `120.25%`, ไม่ใช่ raw index level
- Annual coverage: official complete calendar years 2016-2025; ไม่มี `*` หรือ `†`.
  ปี 2016-2020 มาจาก issuer table ที่ปัดเศษหนึ่งตำแหน่ง; 2021-2025 ใช้ official
  U.S. fact sheet แบบสองตำแหน่ง
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` จาก rounded annual inputs

| ปี | EWG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.60% | 11.96% |
| 2017 | 27.40% | 21.83% |
| 2018 | -22.30% | -4.38% |
| 2019 | 20.60% | 31.49% |
| 2020 | 11.30% | 18.40% |
| 2021 | 4.85% | 28.71% |
| 2022 | -22.17% | -18.11% |
| 2023 | 22.90% | 26.29% |
| 2024 | 10.32% | 25.02% |
| 2025 | 35.15% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+35.15%`
- Least positive: 2016, `+2.60%`
- Worst: 2018, `-22.30%`
- Least bad down year: 2022, `-22.17%`
- 2021-2025 common-window cumulative: EWG `49.53%`, CAGR `8.38%`; S&P 500 TR
  `96.17%`, CAGR `14.43%`
- Current YTD: EWG `-0.85%` NAV as of 13 ก.ค. 2026; S&P 500 TR `+9.64%` as of
  17 ก.ค. 2026 (different dates)

## Risk read-through

**10-year NAV CAGR:** `8.22%` ณ 30 มิ.ย. 2026. EWG เป็น Germany single-country
equity ที่กระจุกใน Industrials, Financials และ Information Technology พร้อม
EUR/USD exposure จึงไวต่อ country cycle, sector concentration และ FX. Official
3-year standard deviation คือ `16.00%`; worst quarter คือ `-27.07%` ใน Q1 2020
แต่ไม่ใช่ maximum drawdown. Official NAV TR max drawdown/recovery ยัง
`ไม่พบข้อมูลที่ยืนยันได้`. Expense ratio `0.49%` เป็น cost drag สำคัญ.

## Sources

- [iShares EWG product page](https://www.ishares.com/us/products/239650/ishares-msci-germany-etf) — fund facts and current metrics
- [iShares EWG fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewg-ishares-msci-germany-etf-fund-fact-sheet-en-us.pdf) — 2021-2025 NAV returns
- [BlackRock EWG calendar-year performance](https://www.blackrock.com/fi/professionals/products/239650/ishares-msci-germany-etf) — 2016-2025 NAV returns
- [SEC-hosted EWG summary prospectus](https://www.sec.gov/Archives/edgar/data/930667/000119312525336658/d175829d497k.htm) — policy and quarter risk
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — current USD Total Return
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
