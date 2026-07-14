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

สำหรับ cached 10-year reference window 2016-2025, S&P 500 TR ให้ cumulative
`298.33%` หรือ CAGR ประมาณ `14.82%`. DGRO มี blended `10-year TR CAGR*`
ประมาณ `13.08%` จากปี 2016-2020 ที่เป็น secondary proxy และปี 2021-2025 ที่เป็น
official NAV TR; ตัวเลขนี้ไม่ใช่ official 10-year NAV CAGR.

## Performance check

- `entity_key: AMEX:DGRO`
- Inception: 10 มิ.ย. 2014
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): Morningstar US Dividend Growth Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference
  benchmark, not DGRO's tracked index)
- 10-year reference window: `2015-12-31` to `2025-12-31` (complete calendar
  years 2016-2025)
- S&P 500 cache: cumulative `298.33%`; CAGR `14.82%` from rounded annual inputs
- DGRO `10-year TR CAGR*`: `13.08%`; blended proxy, not official 10-year NAV TR
- Official annual table for DGRO: 2021-2025; supplemental S&P 500 cache:
  2016-2025; `*` คือ dividend-reinvested market-price proxy สำหรับ 2014-2020
  เพราะหน้า issuer ที่เก็บไว้ไม่แสดง annual table ช่วงนี้

- Annual NAV TR coverage: 2016-2020 secondary proxy*; 2021-2025 official NAV TR
| ปี | DGRO TR | S&P 500 TR |
|---|---:|---:|
| 2014* | 8.56% | — |
| 2015* | -0.69% | — |
| 2016* | 15.20% | 11.96% |
| 2017* | 23.00% | 21.83% |
| 2018* | -2.38% | -4.38% |
| 2019* | 29.87% | 31.49% |
| 2020* | 9.50% | 18.40% |
| 2021 | 26.56% | 28.71% |
| 2022 | -7.85% | -18.11% |
| 2023 | 10.43% | 26.29% |
| 2024 | 16.61% | 25.02% |
| 2025 | 15.74% | 17.88% |

S&P 500 TR ปี 2016-2025 ใช้ cached convention จาก `check-etf-performance`;
ปี 2021-2025 cross-check กับ official IVV factsheet (as of 31 มี.ค. 2026).
เป็น common reference benchmark ไม่ใช่ tracked index ของ DGRO. DGRO ปี 2016-2020
เป็น `*` secondary proxy จึงต้องแยกจาก official NAV read.

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
2023-2025; ส่วน blended `10-year TR CAGR*` ที่ `13.08%` ต่ำกว่า S&P 500 cache
ที่ `14.82%` ราว `1.74 percentage points` ต่อปี แต่ไม่ควรตีความเป็น official
NAV-vs-index tracking result เพราะช่วง 2016-2020 ของ DGRO เป็น proxy.

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
