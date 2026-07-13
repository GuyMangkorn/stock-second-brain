---
type: etf-performance
instrument_type: ETF
entity_key: AMEX:DGRO
ticker: DGRO
updated: 2026-07-13
source_batch: raw/imports/ETF_performance_sources_2026-07-13.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DGRO
---

# DGRO Performance

## Bottom line

DGRO มีผลตอบแทนเป็นบวก 8 จาก 11 ปีเต็มช่วง 2015-2025 โดยปีดีที่สุดคือ 2019*
และแย่ที่สุดคือ 2022. 10-year NAV CAGR อยู่ที่ `13.38%` ณ 30 มิ.ย. 2026 และใน
common window 2021-2025 DGRO ให้ cumulative `73.82%` หรือ CAGR `11.69%`
เทียบกับ S&P 500 Total Return ที่ `96.17%` หรือ `14.43%`; DGRO lagged
`22.35 percentage points` แบบ cumulative. 2026 YTD snapshot ที่บันทึกไว้คือ
`+10.22%` ณ 30 มิ.ย. 2026.

## Performance check

- `entity_key: AMEX:DGRO`
- Inception: 10 มิ.ย. 2014
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): Morningstar US Dividend Growth Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference
  benchmark, not DGRO's tracked index)
- Official annual table: 2021-2025; `*` คือ dividend-reinvested market-price
  proxy สำหรับ 2014-2020 เพราะหน้า issuer ที่เก็บไว้ไม่แสดง annual table ช่วงนี้

| ปี | DGRO TR | S&P 500 TR |
|---|---:|---:|
| 2014* | 8.56% | — |
| 2015* | -0.69% | — |
| 2016* | 15.20% | — |
| 2017* | 23.00% | — |
| 2018* | -2.38% | — |
| 2019* | 29.87% | — |
| 2020* | 9.50% | — |
| 2021 | 26.56% | 28.71% |
| 2022 | -7.85% | -18.11% |
| 2023 | 10.43% | 26.29% |
| 2024 | 16.61% | 25.02% |
| 2025 | 15.74% | 17.88% |

S&P 500 TR ใช้ official benchmark rows จาก IVV factsheet (as of 31 มี.ค. 2026)
และเป็น common reference benchmark; ไม่ใช่ tracked index ของ DGRO. เนื่องจาก
DGRO ปี 2014-2020 เป็น `*` secondary proxy จึงไม่เติม comparator ย้อนหลังในช่วงนั้น.

**Up years / Down years**

- Best: 2019*, **+29.87%**
- Least positive: 2023, **+10.43%**
- Worst: 2022, **-7.85%**
- Least bad down year: 2015*, **-0.69%**
- 2026 YTD snapshot: **+10.22% NAV**, as of 30 มิ.ย. 2026
- Common-window read: DGRO beat S&P 500 only in 2022 by **+10.26 percentage
  points**; it lagged in 2021, 2023, 2024, and 2025.

## Risk read-through

Average monthly return `+1.05%`, positive months `67%`. Secondary maximum drawdown
ประมาณ `-35.10%` ใน COVID crash (23 มี.ค. 2020) และใช้ `161` trading sessions
เพื่อฟื้นกลับจุดสูงสุดเดิม. Expense ratio `0.08%`. **10-year NAV CAGR:** `13.38%`
ณ 30 มิ.ย. 2026 จาก iShares official average annual total return. เทียบ S&P 500
แล้ว DGRO มี downside ดีกว่าในปี 2022 แต่ participation ต่ำกว่าในปี 2021 และ
2023-2025; นี่เป็น observed-return read-through ไม่ใช่การยืนยันว่าจะเกิดซ้ำ.

**Classification:** Structural = U.S. dividend growth / quality. Behavioral =
quality large-cap ที่ downside ปานกลาง แต่ยังไวต่อ equity และ rate repricing.

## Driver notes

- **2022, confirmed event:** inflation, Ukraine-related uncertainty และ Fed
  tightening สร้างแรงกดดันต่อ equity multiples; DGRO ลดลงแต่ยังดีกว่า VIGI.
- **2020, confirmed event:** COVID ทำให้เกิด drawdown เร็วและลึก แม้มี policy
  support; dividend growth ไม่ได้แปลว่า capital protection.
- **2025, probable:** U.S. quality/dividend-growth participation ช่วยให้บวก
  `15.74%`; ยังไม่ใช่หลักฐานว่า outperformance จะเกิดซ้ำ.

## Sources

- [iShares product page](https://www.ishares.com/us/products/264623/ishares-core-dividend-growth-etf)
- [iShares factsheet](https://www.ishares.com/us/literature/fact-sheet/dgro-ishares-core-dividend-growth-etf-fund-fact-sheet-en-us.pdf)
- [iShares IVV factsheet](https://www.ishares.com/us/literature/fact-sheet/ivv-ishares-core-s-p-500-etf-fund-fact-sheet-en-us.pdf) — S&P 500 TR comparator, as of 31 มี.ค. 2026
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and total-return series
- [PortfoliosLab](https://portfolioslab.com/symbol/DGRO) และ [Total Real Returns](https://totalrealreturns.com/n/DGRO%2CSPY)
- [[ETF_performance_sources_2026-07-13]] | [[ETF_performance_sources_2026-07-12]] | [[ETF Performance Index]]
