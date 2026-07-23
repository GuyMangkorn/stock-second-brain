---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:AAXJ
ticker: AAXJ
exchange: NASDAQ
issuer: iShares
fund: iShares MSCI All Country Asia ex Japan ETF
tracked_index: MSCI AC Asia ex Japan Index (Net)
benchmark: S&P 500 Total Return
inception: 2008-08-13
expense_ratio: 0.72%
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/AAXJ
  - geography/Asia-ex-Japan
---

# AAXJ Performance

> Navigation: [[ETF Region Index]] → [[Asia ex Japan ETF]] → [[ETF Performance Index]]

## Bottom line

AAXJ เป็น passive/index-tracking equity ETF ของ iShares ที่ลงทุนในหุ้น large- และ mid-cap ของประเทศพัฒนาแล้วและ emerging Asia โดยไม่รวมญี่ปุ่น. Official rolling NAV Total Return ช่วง 2016-06-30 ถึง 2026-06-30 ให้ cumulative `164.36%` และ CAGR `10.21%`. ใน common calendar window 2021-2025 กองทุนให้ cumulative `15.04%` และ CAGR `2.84%`, ต่ำกว่า S&P 500 Total Return ที่ CAGR `14.43%`. Current official NAV คือ `US$113.07` และ NAV TR YTD คือ `21.30%` ณ 2026-07-22.

## Performance check

- entity_key: `NASDAQ:AAXJ`
- Classification: supported passive/index-tracking equity ETF
- Inception: `2008-08-13`
- Issuer benchmark: `MSCI AC Asia ex Japan Index (Net)`
- Metric: NAV Total Return รวมการ reinvest distributions และหัก fund expenses ตาม issuer methodology
- Expense ratio: `0.72%`
- Holdings: `941` ณ 2026-07-22
- 3-year standard deviation: `16.71%`; equity beta: `0.87` ณ 2026-06-30
- Benchmark comparison: S&P 500 Total Return เป็น common USD reference benchmark ไม่ใช่ tracked index ของ AAXJ

## Rolling 10-year NAV Total Return

Official issuer table ณ 2026-06-30 ครอบคลุม 10 complete calendar years. Raw NAV endpoint levels ไม่เปิดเผย จึงใช้ normalized TR endpoints จาก official cumulative return; ไม่ใช่ proxy.

| Start date | End date | Start normalized TR | End normalized TR | Actual years | Cumulative | CAGR |
|---|---|---:|---:|---:|---:|---:|
| 2016-06-30 | 2026-06-30 | 100.00 | 264.36 | 10.00 | 164.36% | 10.21% |

Formula: `(264.36 / 100.00)^(1 / 10.00) - 1 = 10.21%` โดย 264.36 มาจาก `100 × (1 + 164.36%)`. `ไม่พบข้อมูลที่ยืนยันได้` สำหรับ raw start/end NAV values และ exact June-to-June S&P 500 TR.

## Annual NAV Total Return vs S&P 500 Total Return

ตัวเลข AAXJ เป็น official issuer calendar-year NAV Total Return; S&P 500 เป็น cached USD Total Return convention ที่ reinvest dividends และใช้เป็น common comparison ณ 2025-12-31.

| Year | AAXJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | -5.89% | 28.71% |
| 2022 | -20.18% | -18.11% |
| 2023 | 4.94% | 26.29% |
| 2024 | 10.48% | 25.02% |
| 2025 | 32.09% | 17.88% |
| **2021-2025 cumulative / CAGR** | **15.04% / 2.84%** | **96.17% / 14.43%** |

AAXJ trailing S&P 500 by approximately `11.59 percentage points` in 2021-2025 CAGR. Up years / down years คือ `3 / 2`; best yearคือ 2025 `+32.09%`, least positiveคือ 2023 `+4.94%`, worstคือ 2022 `-20.18%`, และ least bad down yearคือ 2021 `-5.89%`.

## Current snapshot and risk read-through

- NAV: `US$113.07` ณ 2026-07-22; NAV TR YTD: `+21.30%` ณ 2026-07-22. Market-price return ไม่ถูกรวมกับ NAV TR.
- Exposure ณ 2026-07-22 กระจุกใน Taiwan `30.55%`, China `23.25%`, Korea (South) `22.59%`, India `12.73%`; Information Technology `46.29%` เป็น sector ใหญ่สุด.
- พฤติกรรมจึงไวต่อ Taiwan/Korea/China country risk, semiconductor/technology cycle, FX และ valuation; 2022 แสดง downside สูงกว่าปี 2021 ขณะที่ 2025 เป็น rebound ที่แรง.
- Daily NAV history สำหรับคำนวณ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture นี้.

## Sources

- Official issuer source: [iShares AAXJ product and performance page](https://www.ishares.com/us/products/239601/ishares-msci-all-country-asia-ex-japan-etf)
- Official S&P source: [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-23]]
- Cross-ETF index: [[ETF Performance Index]]
