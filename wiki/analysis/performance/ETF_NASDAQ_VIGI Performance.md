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

VIGI มีผลตอบแทนเป็นบวก 7 จาก 9 ปีเต็มช่วง 2017-2025; 1-year NAV Total Return
อยู่ที่ `+6.06%` ณ 30 มิ.ย. 2026 และ 2026 YTD อยู่ที่ `+4.64%` ณ 8 ก.ค.
2026. ปีดีที่สุดคือ 2017 ที่ `+27.80%` และแย่ที่สุดคือ 2022 ที่ `-16.71%`.
ตัวเลข current NAV มาจาก [Vanguard advisor product page](https://advisors.vanguard.com/investments/products/vigi/vanguard-international-dividend-appreciation-etf). 10-year NAV CAGR อยู่ที่ `8.13%` ณ 31 พ.ค. 2026.

## Performance check

- `entity_key: NASDAQ:VIGI`
- Inception: 25 ก.พ. 2016
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Benchmark: Spliced S&P Global Ex-U.S. Dividend Growers Index in USD NTR
- Coverage/source note: annual rows เป็น official Vanguard returns ถึง 2025; 2016
  เป็น official inception-year partial และ 2026 YTD เป็น official NAV ณ 8 ก.ค.
  2026. Vanguard ยังไม่แสดง benchmark YTD ล่าสุดในฐานเดียวกัน
- `†` คือ official inception-year partial; complete-year ranking เริ่ม 2017

Annual table จาก [Vanguard product performance](https://investor.vanguard.com/investment-products/etfs/profile/vigi)
โดยใช้ NAV Total Return เทียบกับ benchmark เดียวกัน:

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
- 2026 YTD: **+4.64% NAV**, as of 8 ก.ค. 2026

## Risk read-through

CAGR ที่คำนวณจาก official annual NAV returns อยู่ที่ `8.95%` สำหรับ 2017-2025
และ `5.46%` สำหรับ common window 2021-2025; Vanguard รายงาน since-inception
annualized return `8.91%` ณ 31 พ.ค. 2026. Official 3-year monthly standard
deviation อยู่ที่ `12.01%` ณ 31 มี.ค. 2026. Expense ratio `0.07%` ณ 27 ก.พ.
2026 และ distribution schedule เป็น quarterly. [Vanguard factsheet](https://fund-docs.vanguard.com/F4415.pdf)

Maximum drawdown ประมาณ `-31.01%` ใน COVID crash (23 มี.ค. 2020) และใช้ `114`
trading sessions เพื่อฟื้นกลับจุดสูงสุดเดิม ตาม secondary adjusted-price
total-return proxy; ตัวเลขนี้ไม่ใช่ official NAV series. [PortfoliosLab](https://portfolioslab.com/symbol/VIGI)

**10-year NAV CAGR:** `8.13%` ณ 31 พ.ค. 2026 จาก Vanguard official average annual
total return.

**Classification:** passive international equity ETF, large-cap dividend growth,
ครอบคลุม developed และ emerging markets excluding U.S.; ความเสี่ยงหลักคือ FX,
country/region และ sector exposure. ข้อจำกัดของรอบนี้คือ as-of dates ต่างกัน
ระหว่าง YTD, month-end performance และ secondary drawdown data.

## Sources

- [Vanguard VIGI product page](https://investor.vanguard.com/investment-products/etfs/profile/vigi)
- [Vanguard advisor product page](https://advisors.vanguard.com/investments/products/vigi/vanguard-international-dividend-appreciation-etf)
- [Vanguard VIGI factsheet](https://fund-docs.vanguard.com/F4415.pdf)
- [S&P Global Ex-U.S. Dividend Growers Index](https://www.spglobal.com/spdji/en/indices/dividends-factors/sp-global-ex-us-dividend-growers-index/)
- [S&P Dividend Growers Index Series Methodology](https://www.spglobal.com/spdji/en/documents/methodologies/methodology-sp-dividend-growers-index-series.pdf)
- [PortfoliosLab](https://portfolioslab.com/symbol/VIGI) — secondary adjusted-price drawdown/recovery context
- [[ETF_performance_sources_2026-07-12]] | [[ETF Performance Index]]
