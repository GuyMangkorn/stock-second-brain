---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWC
ticker: EWC
exchange: NYSE Arca
fund: iShares MSCI Canada ETF
tracked_index: MSCI Canada Custom Capped Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-13
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-09
price_nav_as_of: 2026-07-10
source_batch: raw/imports/ETF_performance_sources_2026-07-13.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWC
  - geography/Canada
---

# EWC Performance

> Navigation: [[ETF Region Index]] → [[Canada ETF]] → [[ETF Performance Index]]

## Bottom line

EWC ให้ cumulative `NAV Total Return` ประมาณ `210.78%` ใน complete calendar years
2016-2025 หรือ CAGR `12.01%` จาก annual rows ที่ issuer เปิดเผย; เป็นบวก 8 ปีและ
ลบ 2 ปี. ปีดีที่สุดคือ 2025 ที่ `+36.03%` และแย่ที่สุดคือ 2018 ที่ `-17.20%`.
2026 YTD ล่าสุดคือ `+8.78%` ณ 9 ก.ค. 2026 เทียบกับ S&P 500 TR `+9.98%` ในวันเดียวกัน.
ตัวเลข cumulative 2016-2025 ใช้ 2021-2025 จาก fact sheet แบบสองตำแหน่ง และ 2016-2020
จาก issuer web table ที่ปัดเศษหนึ่งตำแหน่ง จึงควรอ่านเป็นค่าประมาณ.

## Performance check

- `entity_key: NYSE Arca:EWC`
- Inception: 12 มี.ค. 1996
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): `MSCI Canada Custom Capped Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ EWC)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `11.25%`; Start TR value: `100.00`; End TR value: `290.39`;
  Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; official cumulative return ใน
  rolling window คือ `190.39%`
- Annual coverage: official complete calendar years 2016-2025; ไม่มี `*` หรือ `†`.
  แถว 2016-2020 เป็นค่าที่ provider แสดงแบบปัดเศษหนึ่งตำแหน่ง; 2021-2025 ใช้
  ตัวเลข NAV จาก fact sheet ทางการ.
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` จาก rounded annual inputs

- Annual NAV TR coverage: official 2016-2025 NAV TR

| ปี | EWC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 24.30% | 11.96% |
| 2017 | 16.00% | 21.83% |
| 2018 | -17.20% | -4.38% |
| 2019 | 27.40% | 31.49% |
| 2020 | 5.60% | 18.40% |
| 2021 | 26.74% | 28.71% |
| 2022 | -12.77% | -18.11% |
| 2023 | 14.62% | 26.29% |
| 2024 | 12.25% | 25.02% |
| 2025 | 36.03% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+36.03%`
- Least positive: 2020, `+5.60%`
- Worst: 2018, `-17.20%`
- Least bad down year: 2022, `-12.77%`
- 2021-2025 common-window cumulative: EWC `93.49%`, CAGR `14.11%`; S&P 500 TR
  `96.17%`, CAGR `14.43%`
- Current YTD: `+8.78%` NAV as of 9 ก.ค. 2026; S&P 500 TR `+9.98%` as of the same date

## Risk read-through

**10-year NAV CAGR:** `11.25%` ณ 30 มิ.ย. 2026. EWC เป็น single-country equity
สำหรับแคนาดา และมี exposure กระจุกใน Financials, Energy และ Materials; จึงไวต่อ
วัฏจักร commodity, credit และ CAD/USD มากกว่า broad global equity. 3-year standard
deviation อยู่ที่ `13.78%` ณ 30 มิ.ย. 2026. Secondary data รายงาน 5-year maximum
drawdown `-24.75%` และ drawdown duration `834` วัน ณ 30 มิ.ย. 2026; all-time
maximum drawdown ยัง `ไม่พบข้อมูลที่ยืนยันได้` จาก issuer. Expense ratio คือ `0.50%`.

**Classification:** Structural = Canada single-country broad equity. Behavioral =
financials/energy/materials concentrated, country/commodity/FX-sensitive และยังมี
equity risk เต็มรูปแบบ; ไม่ควรตีความเป็น crisis hedge.

## Sources

- [iShares EWC product page](https://www.ishares.com/us/products/239615/ishares-msci-canada-etf) — identity, NYSE Arca, inception, issuer benchmark, current NAV/price, YTD, expense ratio, standard deviation, and sector exposure
- [iShares EWC fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewc-ishares-msci-canada-etf-fund-fact-sheet-en-us.pdf) — official NAV calendar returns 2021-2025, return definition, and fund facts
- [BlackRock EWC calendar-year performance](https://www.blackrock.com/fi/professionals/products/239615/ishares-msci-canada-etf) — official calendar return rows 2016-2025 and rolling performance
- [S&P 500 DJI returns page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization) — S&P 500 TR current YTD comparator as of 9 ก.ค. 2026
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and total-return series identity
- [ETF Central EWC](https://www.etfcentral.com/fund/EWC) — secondary 5-year maximum drawdown and duration, data as of 30 มิ.ย. 2026
- [[ETF_performance_sources_2026-07-13]] | [[ETF Performance Index]]
