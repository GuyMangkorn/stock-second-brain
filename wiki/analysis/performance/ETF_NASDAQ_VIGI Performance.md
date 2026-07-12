---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:VIGI
ticker: VIGI
updated: 2026-07-12
source_batch: raw/imports/ETF_performance_sources_2026-07-12.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VIGI
---

# VIGI Performance

## Bottom line

VIGI มีผลตอบแทนเป็นบวก 7 จาก 9 ปีเต็มช่วง 2017-2025 และ CAGR ใน common window
2021-2025 อยู่ที่ `5.46%`. ปีดีที่สุดคือ 2017 และแย่ที่สุดคือ 2022 ที่
`-16.71%`. ใน pilot VIGI เป็นกองที่ไวต่อ FX, country และ regional risk มากที่สุด.
2026 YTD snapshot ที่บันทึกไว้คือ `+4.12%` ณ 31 พ.ค. 2026.

## Performance check

- `entity_key: NASDAQ:VIGI`
- Inception: 25 ก.พ. 2016
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Benchmark: Spliced S&P Global Ex-U.S. Dividend Growers Index in USD NTR
- `†` คือ official inception-year partial; complete-year ranking เริ่ม 2017

| ปี | VIGI TR | Benchmark |
|---|---:|---:|
| 2016† | 6.64% | — |
| 2017 | 27.80% | 27.64% |
| 2018 | -11.32% | -11.34% |
| 2019 | 27.04% | 27.32% |
| 2020 | 15.11% | 15.35% |
| 2021 | 12.42% | 12.82% |
| 2022 | -16.71% | -16.81% |
| 2023 | 16.16% | 16.25% |
| 2024 | 2.62% | 2.87% |
| 2025 | 16.89% | 16.37% |

**Up years / Down years**

- Best: 2017, **+27.80%**
- Least positive: 2024, **+2.62%**
- Worst: 2022, **-16.71%**
- Least bad down year: 2018, **-11.32%**
- 2026 YTD snapshot: **+4.12% NAV**, as of 31 พ.ค. 2026

## Risk read-through

Average monthly return `+0.77%`, positive months `66%`. Secondary maximum drawdown
ประมาณ `-31.01%` ใน COVID crash (23 มี.ค. 2020) และใช้ `114` trading sessions
เพื่อฟื้นกลับจุดสูงสุดเดิม. Expense ratio `0.07%`.

**Classification:** Structural = international dividend growth, developed และ
emerging markets excluding U.S. Behavioral = FX/country-sensitive, upside ต่ำกว่า
U.S. dividend-growth pair ใน common window และ downside สูงกว่า.

## Driver notes

- **2022, confirmed event:** global inflation, Ukraine war และ global rate
  tightening สร้าง risk-off regime; non-U.S. currency และ regional exposure
  ขยายผลขาดทุนเป็น `-16.71%`.
- **2020, confirmed event:** COVID ทำให้เกิด drawdown `-31.01%`; recovery เร็วกว่า
  VIG full-history แต่ initial shock ยังมีนัยสำคัญ.
- **2025, probable:** international/value และ currency support ช่วยให้บวก
  `16.89%`; ต้องดู holdings attribution ก่อนสรุปว่าเป็น edge ที่ทำซ้ำได้.

## Sources

- [Vanguard VIGI product page](https://investor.vanguard.com/investment-products/etfs/profile/vigi)
- [PortfoliosLab](https://portfolioslab.com/symbol/VIGI) และ [Total Real Returns](https://totalrealreturns.com/n/VIGI)
- [[ETF_performance_sources_2026-07-12]] | [[ETF Performance Index]]
