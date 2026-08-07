---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VIG
ticker: VIG
updated: 2026-08-07
source_batch: raw/imports/ETF_performance_sources_2026-07-13.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/United-States
  - ticker/VIG
---

# VIG Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VIG มีผลตอบแทนเป็นบวก 15 จาก 19 ปีเต็มช่วง 2007-2025 โดยปีดีที่สุดคือ 2019
และแย่ที่สุดคือ 2008*. Official 2011-2025 ให้ภาพ quality dividend-growth ที่
ฟื้นตัวดีหลังวิกฤติ แต่ปี 2022 ยังติดลบ `-9.79%`. 10-year NAV CAGR อยู่ที่
`13.13%` ณ 30 มิ.ย. 2026. ใน cached common window 2016-2025 VIG ให้ cumulative
`242.14%` หรือ CAGR `13.09%` เทียบกับ S&P 500 TR ที่ `298.33%` หรือ `14.82%`.
2026 YTD snapshot ที่บันทึกไว้คือ `+7.19%` ณ 31 พ.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:VIG`
- Inception: 21 เม.ย. 2006
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): Spliced S&P U.S. Dividend Growers Index TR
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference,
  not VIG's tracked index)
- ปี 2011-2025 ใช้ official NAV return ของ Vanguard; `*` คือ
  dividend-reinvested proxy สำหรับปี 2006-2010 ที่หน้า Vanguard ปัจจุบันไม่แสดง
  annual table ย้อนหลังถึง 2006

- Annual NAV TR coverage: official 2016-2025 NAV TR

| ปี | VIG TR | S&P 500 TR |
|---|---:|---:|
| 2006* | 8.55% | — |
| 2007* | 5.63% | — |
| 2008* | -26.69% | — |
| 2009* | 19.58% | — |
| 2010* | 14.74% | — |
| 2011 | 6.21% | — |
| 2012 | 11.61% | — |
| 2013 | 28.99% | — |
| 2014 | 10.06% | — |
| 2015 | -1.95% | — |
| 2016 | 11.84% | 11.96% |
| 2017 | 22.22% | 21.83% |
| 2018 | -2.02% | -4.38% |
| 2019 | 29.71% | 31.49% |
| 2020 | 15.46% | 18.40% |
| 2021 | 23.64% | 28.71% |
| 2022 | -9.79% | -18.11% |
| 2023 | 14.46% | 26.29% |
| 2024 | 17.02% | 25.02% |
| 2025 | 14.18% | 17.88% |

S&P 500 TR rows use the cached common-reference convention as of 2025-12-31;
the issuer benchmark remains metadata and is not silently substituted.

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
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity
- [PortfoliosLab](https://portfolioslab.com/symbol/VIG) และ [Total Real Returns](https://totalrealreturns.com/n/VIG)
- [[ETF_performance_sources_2026-07-13]] | [[ETF_performance_sources_2026-07-12]] | [[ETF Performance Index]]
