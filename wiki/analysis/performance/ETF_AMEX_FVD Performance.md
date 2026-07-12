---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FVD
input_alias: AMEX:FVD
ticker: FVD
exchange: NYSE Arca
fund: First Trust Value Line® Dividend Index Fund
tracked_index: Value Line® Dividend Index
updated: 2026-07-12
performance_as_of: 2026-06-30
price_nav_as_of: 2026-07-10
expense_ratio_as_of: 2026-05-01
source_batch: raw/imports/ETF_performance_sources_2026-07-12.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FVD
---

# FVD Performance

## Bottom line

FVD ให้ `NAV Total Return` `+5.76%` YTD ณ 30 มิ.ย. 2026 และเป็นบวก 7 จาก 10
complete calendar years ในช่วง 2016-2025. ปีดีที่สุดคือ 2019 ที่ `+26.56%` และ
แย่ที่สุดคือ 2022 ที่ `-5.24%`; official rolling 10-year NAV CAGR อยู่ที่ `8.40%`
ณ 30 มิ.ย. 2026 และ latest completed year 2025 อยู่ที่ `+8.19%`.

## Performance check

- `entity_key: NYSE Arca:FVD` (`AMEX:FVD` เป็น input alias)
- Inception: 19 ส.ค. 2003
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Benchmark: `Value Line® Dividend Index`
- Fund type: passive equity-income index ETF; rebalance รายเดือน
- Expense ratio: `0.62%` ณ 1 พ.ค. 2026; contractual expense cap `0.70%` อย่างน้อยถึง 30 เม.ย. 2027
- Performance as-of: 30 มิ.ย. 2026; closing NAV/market price as-of: 10 ก.ค. 2026
- Coverage/source note: annual rows เป็น official complete calendar years 2016-2025; ไม่มี `*` หรือ `†`. Issuer ไม่แสดง Value Line benchmark เป็น calendar-year rows ใน current performance table จึงใช้ S&P 500 เป็น comparator context ที่ issuer แสดงไว้ และรายงาน Value Line benchmark แบบ rolling period แยกด้านล่าง

| ปี | FVD NAV TR | S&P 500 TR (context) |
|---|---:|---:|
| 2016 | 19.94% | 11.96% |
| 2017 | 12.48% | 21.83% |
| 2018 | -3.44% | -4.38% |
| 2019 | 26.56% | 31.49% |
| 2020 | -0.01% | 18.40% |
| 2021 | 24.86% | 28.71% |
| 2022 | -5.24% | -18.11% |
| 2023 | 4.10% | 26.29% |
| 2024 | 10.00% | 25.02% |
| 2025 | 8.19% | 17.88% |

**Up years / Down years**

- Best: 2019, `+26.56%`
- Least positive: 2023, `+4.10%`
- Worst: 2022, `-5.24%`
- Least bad down year: 2020, `-0.01%`
- Current YTD: `+5.76%` NAV ณ 30 มิ.ย. 2026
- Issuer benchmark `Value Line Dividend Index`: YTD `+6.16%`, 1-year `+11.20%`, 3-year CAGR `+9.58%`, 5-year CAGR `+7.03%`, 10-year CAGR `+9.23%`; FVD อยู่ต่ำกว่า benchmark ในทุกช่วง rolling ที่แสดง

## Risk read-through

2016-2025 CAGR ที่คำนวณจาก official annual returns อยู่ที่ `9.23%`; **10-year NAV
CAGR:** `8.40%` ณ 30 มิ.ย. 2026 ตาม First Trust official rolling return; common window
2021-2025 cumulative `46.58%` หรือ CAGR `7.95%`. Issuerรายงาน 3-year standard
deviation `11.07%`, beta `0.49` และ Sharpe ratio `0.41` ณ 30 มิ.ย. 2026.

Maximum daily drawdown และ recovery จาก official NAV total-return series:
`ไม่พบข้อมูลที่ยืนยันได้`. Worst complete calendar yearคือ `-5.24%` ใน 2022;
เมื่อใช้ annual end-point series ระดับก่อนปี 2022 ถูกทำจุดสูงสุดใหม่ภายใน 2024
(calculation จาก official annual returns). Structural = U.S. value/dividend income;
behavioral = utilities/financials-heavy, monthly-rebalanced และยังมี equity risk.

## Sources

- [First Trust FVD product page](https://www.ftportfolios.com/retail/etf/etfsummary.aspx?Ticker=FVD) — identity, NYSE Arca listing, current NAV/market price, rolling performance, benchmark, standard deviation, and sector exposure
- [First Trust FVD factsheet](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b7bf1eff-4e8d-4623-b4c4-65d7710cf1c2) — official 2016-2025 calendar-year returns and S&P 500 comparator; as of 31 มี.ค. 2026
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1329377/000144554626003287/etf1_fvd497k.htm) — index strategy, expense ratio, fee cap, exchange and official period return cross-check; dated 1 พ.ค. 2026
- [[ETF_performance_sources_2026-07-12]] | [[ETF Performance Index]]
