---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:BKIE
ticker: BKIE
exchange: NYSE Arca
updated: 2026-08-30
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return for official fields; secondary NAV/total-return proxy for rows marked *
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/BKIE
---

# BKIE Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

BKIE เป็น passive developed-markets ex-U.S. large-/mid-cap ETF ที่มีผลตอบแทน
เป็นบวก 4 จาก 5 complete calendar years ในช่วง 2021-2025; ปีดีที่สุดคือ 2025
ที่ `+31.93%*` และปีติดลบเพียงปีเดียวคือ 2022 ที่ `-13.74%*`. Secondary
NAV/total-return rows ให้ CAGR ช่วง 2021-2025 ที่ `9.89%*` เทียบกับ S&P 500
Total Return common reference ที่ `14.43%`; current official NAV TR YTD คือ
`+14.70%` ณ 2026-08-28.

## Performance check

- `entity_key: NYSE Arca:BKIE`
- Fund: `BNY Mellon International Equity ETF`; inception `2020-04-22`; listing `NYSE Arca`
- Metric: `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหัก fund expenses ตาม issuer convention
- Management mode: `passive-index`; กองทุนมุ่ง track `Solactive GBS Developed Markets ex United States Large & Mid Cap USD Index NTR`
- Issuer benchmark: `Solactive GBS Developed Markets ex United States Large & Mid Cap USD Index NTR`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ BKIE)
- Complete calendar window: `2021-2025` secondary NAV/total-return proxy compound `60.24%*` / rounded-input CAGR `9.89%*`
- S&P 500 common reference: compound `96.17%` / CAGR `14.43%`; BKIE terminal wealth ต่ำกว่าประมาณ `18.32%` ใน window เดียวกัน
- Current official fields: NAV `US$34.74`, market price `US$34.71`, NAV TR YTD `14.70%`, all as of `2026-08-28`
- Expense ratio: `0.04%` net/gross
- Coverage note: complete calendar rows ด้านล่างเป็น secondary NAV/total-return proxies จาก AAII และ POEMS (`*`) เพราะ issuer page ให้ current/rolling standardized fields แต่ annual calendar rows ที่อ่านได้ไม่ครบเป็นชุดเดียวกัน; 2020 เป็น inception partial จึงไม่ถูกนำมาคำนวณ
- Corporate-action note: BNY ระบุ 3-for-1 forward split ที่มีผลหลังปิดตลาด `2026-07-17` และเริ่ม post-split trading `2026-07-20`; current NAV/price จึงเป็น post-split และไม่ควรผสมกับ pre-split share-price history

| ปี | BKIE NAV/total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2021 | 13.48%* | 28.71% |
| 2022 | -13.74%* | -18.11% |
| 2023 | 18.31%* | 26.29% |
| 2024 | 4.88%* | 25.02% |
| 2025 | 31.93%* | 17.88% |

**Up years / Down years**

- Up / Down years: `4 / 1`
- Best proxy year: 2025, **+31.93%***
- Least positive proxy year: 2024, **+4.88%***
- Worst / only down proxy year: 2022, **-13.74%***
- Current official YTD: **+14.70% NAV TR**, as of **2026-08-28**
- BKIE proxy beat the S&P 500 common reference in 2022 and 2025 (`2 / 5` years); this arithmetic comparison is not a manager-skill claim

## Risk read-through

ประวัติ BKIE ยังไม่ครบ 10 ปีจาก inception `2020-04-22` จึงไม่มี 10-year NAV
CAGR ที่ใช้ได้; official since-inception NAV annualized return คือ `15.34%` ณ
2026-07-31 และ official rolling 5-year/3-year NAV TR คือ `10.06%`/`16.75%`
ตามลำดับ. Official snapshot ยังรายงาน holdings `976` และ turnover `7.28%` ณ
2026-07-31, net assets ประมาณ `US$1.345B` ณ 2026-08-28, P/E `16.20x`, P/B
`2.32x`, และ 30-day median bid/ask spread `0.17%`.

Secondary AAII snapshot รายงาน standard deviation `13.10%` ณ 2026-06-30.
PortfoliosLab ซึ่งเป็น secondary dividend-adjusted daily proxy รายงาน maximum
drawdown `-28.19%` ใน September 2022, recovery `10 months 22 days`, และช่วง
underwater ประมาณ `2 years 1 month` ถึง December 2023; ตัวเลขนี้ไม่ใช่ official
daily NAV series และไม่ถูกผสมเข้า NAV return record. ความเสี่ยงหลักคือประเทศและ
sector ของ developed markets นอกสหรัฐฯ, FX, financials/large-cap cycle,
tracking difference, premium/discount, liquidity และ foreign-market trading
calendar.

ข้อจำกัดสำคัญคือ official daily NAV history สำหรับยืนยัน drawdown/recovery และ
risk-adjusted persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้`; annual rows จึงคง
เครื่องหมาย `*` และไม่ใช้ถ้อยคำว่า alpha.

## Sources

- [BNY Mellon BKIE product page](https://www.bny.com/investments/us/en/intermediary/products/etf/fund/bny-mellon-international-equity-etf.html) — identity, NYSE Arca listing, passive objective, inception, index, expense ratio, current NAV/market price, holdings/assets, standardized returns, YTD, split and portfolio fields
- [BNY Mellon BKIE factsheet](https://www.bny.com/content/dam/im/documents/compliancedocs/factsheet/monthly/4854.pdf) — NAV Total Return convention, reinvestment/expense treatment, quarterly distribution, benchmark and official rolling fields as of 2026-03-31
- [AAII BKIE performance](https://www.aaii.com/etf/ticker/BKIE) — secondary annual NAV-return rows for 2021-2025 and standard deviation snapshot as of 2026-06-30
- [POEMS BKIE performance](https://www.poems.com.sg/etf-screener/NYSE-BKIE/) — secondary precision cross-check for annual return rows; the displayed series is not treated as an issuer NAV table
- [PortfoliosLab BKIE](https://portfolioslab.com/symbol/BKIE) — secondary dividend-adjusted daily drawdown/recovery proxy only
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2021-2025
- [[ETF_performance_sources_2026-08-30]] | [[International ETF]] | [[ETF Performance Index]]
