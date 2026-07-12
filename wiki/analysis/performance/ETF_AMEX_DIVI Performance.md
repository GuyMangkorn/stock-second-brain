---
type: etf-performance
instrument_type: ETF
entity_key: AMEX:DIVI
ticker: DIVI
updated: 2026-07-12
source_batch: raw/imports/ETF_performance_sources_2026-07-12.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DIVI
---

# DIVI Performance

## Bottom line

DIVI มีผลตอบแทนเป็นบวก 7 จาก 9 ปีเต็มช่วง 2017-2025 และให้ CAGR ใน common
window 2021-2025 ที่ `13.59%`, สูงสุดใน pilot. ปีดีที่สุดคือ 2025 ที่ `+34.51%`
และแย่ที่สุดคือ 2018 ที่ `-6.18%`. 2026 YTD snapshot ที่บันทึกไว้คือ `+11.38%`
ณ 30 มิ.ย. 2026.

## Performance check

- `entity_key: AMEX:DIVI`
- Inception: 1 มิ.ย. 2016
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Benchmark: Morningstar Developed Markets ex-North America Dividend Enhanced
  Select Index-NR
- Official complete-year table เริ่ม 2017; 2016 เป็น inception-year ที่ issuer
  ไม่แสดง return ที่ใช้เทียบได้

| ปี | DIVI TR | Benchmark |
|---|---:|---:|
| 2017 | 12.82% | 13.21% |
| 2018 | -6.18% | -5.75% |
| 2019 | 22.66% | 23.21% |
| 2020 | 1.55% | 1.86% |
| 2021 | 17.22% | 17.63% |
| 2022 | -1.74% | -1.43% |
| 2023 | 19.23% | 18.96% |
| 2024 | 2.36% | 2.28% |
| 2025 | 34.51% | 34.32% |

**Up years / Down years**

- Best: 2025, **+34.51%**
- Least positive: 2024, **+2.36%**
- Worst: 2018, **-6.18%**
- Least bad down year: 2022, **-1.74%**
- 2026 YTD snapshot: **+11.38% NAV**, as of 30 มิ.ย. 2026

## Risk read-through

Average monthly return `+0.92%`, positive months `64%`. Secondary maximum drawdown
ประมาณ `-27.76%` ใน COVID crash (12 มี.ค. 2020) และใช้ `207` trading sessions
เพื่อฟื้นกลับจุดสูงสุดเดิม. Expense ratio `0.09%`.

**Classification:** Structural = developed markets ex-North America dividend/value
tilt with optimizer. Behavioral = beta ต่ำกว่า, แต่ไวต่อ value, financials, FX,
country และ international cyclicality.

## Driver notes

- **2022, confirmed event:** inflation, war-related energy pressure และ rate hikes
  สร้าง risk-off regime; value/financials และ ex-North-America exposure น่าจะช่วย
  offset duration pressure จนผลตอบแทนติดลบเพียง `-1.74%`.
- **2020, confirmed event:** COVID ทำให้เกิด drawdown `-27.76%`, ตื้นสุดใน pilot
  แต่ยังไม่ใช่หลักฐานว่าเป็น crisis protection.
- **2025, probable:** international/value/FX rebound สอดคล้องกับผลตอบแทน
  `+34.51%`; ต้องดู holdings attribution ก่อนใช้เป็น forecast.

## Sources

- [Franklin DIVI factsheet](https://www.franklintempleton.com/forms-literature/download/DIVI-FF)
- [PortfoliosLab](https://portfolioslab.com/symbol/DIVI) | [[ETF_performance_sources_2026-07-12]]
- [[ETF_AMEX_DIVI_fund_facts]] | [[ETF Performance Index]]
