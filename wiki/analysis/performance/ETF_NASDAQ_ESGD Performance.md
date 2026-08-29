---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:ESGD
ticker: ESGD
exchange: NASDAQ
updated: 2026-08-30
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/ESGD
---

# ESGD Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

ESGD ให้ผลตอบแทนเป็นบวก `4 / 5` complete calendar years ในช่วง 2021-2025 โดยปีดีที่สุดคือ 2025 ที่ `+29.98%` และแย่ที่สุดคือ 2022 ที่ `-14.96%`. Official rolling 10-year NAV Total Return อยู่ที่ `9.77%` annualized หรือ cumulative `154.00%` ณ 2026-06-30; current official NAV TR YTD อยู่ที่ `+14.42%` ณ 2026-08-21. ใน common window 2021-2025 ESGD ให้ cumulative `51.20%` หรือ CAGR `8.62%` เทียบกับ S&P 500 Total Return ที่ `96.17%` หรือ `14.43%`.

## Performance check

- `entity_key: NASDAQ:ESGD`
- Fund: `iShares ESG Aware MSCI EAFE ETF`; inception: 28 มิ.ย. 2016; asset class: `Equity`
- Metric: `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหัก fund expenses ตาม iShares convention
- Management mode: `passive-index`
- Tracked index (issuer benchmark): `MSCI EAFE Extended ESG Focus Index (Net)`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ ESGD)
- 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `9.77%`; Start TR index: `100.00`; End TR index: `254.00`; Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; normalized endpoints `254.00 / 100.00` มาจาก official cumulative `154.00%`
- Common window: `2021-2025` ESGD compound `51.20%` / rounded-input CAGR `8.62%`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: annual rows 2021-2025 เป็น official iShares NAV Total Return; index history is spliced, with MSCI EAFE ESG Focus Index (Net) through 2018-05-31 and MSCI EAFE Extended ESG Focus Index (Net) from 2018-06-01. ไม่มี secondary proxy ในตารางนี้.

| ปี | ESGD TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 11.60% | 28.71% |
| 2022 | -14.96% | -18.11% |
| 2023 | 18.08% | 26.29% |
| 2024 | 3.80% | 25.02% |
| 2025 | 29.98% | 17.88% |

**Up years / Down years**

- Best: 2025, **+29.98%**
- Least positive: 2024, **+3.80%**
- Worst: 2022, **-14.96%**
- Least bad down year: 2022, **-14.96%**
- Current YTD: **+14.42% NAV**, as of **2026-08-21**
- ESGD beat the S&P 500 common reference in 2025 only (`1 / 5` complete years); this is not a manager-skill claim.

## Risk read-through

Annual NAV TR ของ ESGD มี downside ชัดเจนใน 2022 แต่ฟื้นตัวแรงใน 2025. Official 10-year NAV TR อยู่ที่ `9.77%` annualized ณ 2026-06-30. Official 3-year standard deviation อยู่ที่ `12.86%` และ equity beta `0.67` ณ 2026-07-31; holdings `354` ณ 2026-08-24. Expense ratio คือ `0.20%`, 12-month trailing yield `3.26%`, และ distribution frequency เป็น semi-annual ณ 2026-07-31.

Latest official NAV คือ `US$106.92` และ closing price `US$107.04` ณ 2026-08-24. Official daily NAV Total Return series ที่เปิดเผยเพียงพอสำหรับคำนวณ maximum drawdown และ recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่แทนที่ด้วย market-price หรือ secondary proxy. โครงสร้างคือ developed-market equities นอกสหรัฐฯ และแคนาดาที่ผ่าน ESG screens; ความเสี่ยงหลักคือ foreign-market, country, currency, sector และ ESG methodology/index-construction risk.

## Sources

- [iShares ESGD product and performance page](https://www.ishares.com/us/products/283778/ishares-esg-msci-eafe-etf-fund_2) — identity, exchange, inception, current NAV/YTD, rolling performance, characteristics and distributions
- [iShares ESGD fact sheet](https://www.ishares.com/us/literature/fact-sheet/esgd-ishares-esg-aware-msci-eafe-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 calendar NAV rows, benchmark, return definition and fee
- [iShares ESGD summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-esg-msci-eafe-etf-8-31.pdf) — objective, index splice and risks
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2021-2025
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
