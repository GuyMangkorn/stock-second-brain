---
type: etf-performance
instrument_type: ETF
entity_key: AMEX:VIG
ticker: VIG
updated: 2026-07-12
source_batch: raw/imports/ETF_performance_sources_2026-07-12.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VIG
---

# VIG Performance

## Bottom line

VIG มีผลตอบแทนเป็นบวก 15 จาก 19 ปีเต็มช่วง 2007-2025 โดยปีดีที่สุดคือ 2019
และแย่ที่สุดคือ 2008*. Official 2011-2025 ให้ภาพ quality dividend-growth ที่
ฟื้นตัวดีหลังวิกฤติ แต่ปี 2022 ยังติดลบ `-9.79%`. 10-year NAV CAGR อยู่ที่
`13.13%` ณ 30 มิ.ย. 2026. 2026 YTD snapshot ที่บันทึกไว้คือ `+7.19%` ณ 31 พ.ค.
2026.

## Performance check

- `entity_key: AMEX:VIG`
- Inception: 21 เม.ย. 2006
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Benchmark: Spliced S&P U.S. Dividend Growers Index TR
- ปี 2011-2025 ใช้ official NAV return ของ Vanguard; `*` คือ
  dividend-reinvested proxy สำหรับปี 2006-2010 ที่หน้า Vanguard ปัจจุบันไม่แสดง
  annual table ย้อนหลังถึง 2006

| ปี | VIG TR | Benchmark |
|---|---:|---:|
| 2006* | 8.55% | — |
| 2007* | 5.63% | — |
| 2008* | -26.69% | — |
| 2009* | 19.58% | — |
| 2010* | 14.74% | — |
| 2011 | 6.21% | 6.32% |
| 2012 | 11.61% | 11.73% |
| 2013 | 28.99% | 29.03% |
| 2014 | 10.06% | 10.12% |
| 2015 | -1.95% | -1.88% |
| 2016 | 11.84% | 11.93% |
| 2017 | 22.22% | 22.29% |
| 2018 | -2.02% | -1.98% |
| 2019 | 29.71% | 29.75% |
| 2020 | 15.46% | 15.62% |
| 2021 | 23.64% | 23.71% |
| 2022 | -9.79% | -9.70% |
| 2023 | 14.46% | 14.52% |
| 2024 | 17.02% | 17.07% |
| 2025 | 14.18% | 14.24% |

**Up years / Down years**

- Best: 2019, **+29.71%**
- Least positive: 2007*, **+5.63%**
- Worst: 2008*, **-26.69%**
- Least bad down year: 2015, **-1.95%**
- 2026 YTD snapshot: **+7.19% NAV**, as of 31 พ.ค. 2026

## Risk read-through

Average monthly return `+0.88%`, positive months `67%`. Secondary maximum drawdown
ประมาณ `-46.81%` ใน 9 มี.ค. 2009 และใช้ `491` trading sessions เพื่อฟื้นกลับ
จุดสูงสุดเดิม. COVID drawdown อยู่ที่ `-31.72%`. Expense ratio `0.04%`.
**10-year NAV CAGR:** `13.13%` ณ 30 มิ.ย. 2026 จาก Vanguard official average
annual total return.

**Classification:** Structural = U.S. dividend appreciation / quality large-cap.
Behavioral = ค่อนข้าง defensive เมื่อเทียบกับ broad equity แต่ dividend history
ไม่ใช่ crisis hedge.

## Driver notes

- **2022, confirmed event:** Fed tightening และ high inflation กดดัน equity
  multiples; quality/large-cap ช่วยจำกัดความเสียหายแต่ยังติดลบ `-9.79%`.
- **2020, confirmed event:** COVID ทำให้เกิด drawdown `-31.72%` แม้มี monetary
  support อย่างรวดเร็ว.
- **2008-2009, secondary:** drawdown ลึกและ recovery ยาวกว่าช่วง 2022 อย่างมาก;
  ใช้เป็น historical risk context ไม่ใช่ direct four-way comparison.

## Sources

- [Vanguard VIG product page](https://investor.vanguard.com/investment-products/etfs/profile/vig)
- [PortfoliosLab](https://portfolioslab.com/symbol/VIG) และ [Total Real Returns](https://totalrealreturns.com/n/VIG)
- [[ETF_performance_sources_2026-07-12]] | [[ETF Performance Index]]
