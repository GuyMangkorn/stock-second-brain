---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:JPXN
ticker: JPXN
exchange: NYSE Arca
issuer: iShares
fund: iShares JPX-Nikkei 400 ETF
tracked_index: JPX-Nikkei Index 400 (Net)
benchmark: S&P 500 Total Return
inception: 2001-10-23
expense_ratio: 0.48%
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/JPXN
  - geography/Japan
---

# JPXN Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

JPXN เป็น passive/index-tracking equity ETF ที่ให้ exposure ต่อหุ้นญี่ปุ่นและติดตาม `JPX-Nikkei Index 400 (Net)`. Official NAV Total Return รวม reinvested distributions และหัก fund expenses ให้ cumulative `142.85%` และ CAGR `9.28%` ในช่วง 2016-06-30 ถึง 2026-06-30 หรือ `10.00 calendar years`. ช่วง 2021-2025 ให้ CAGR `6.19%` เทียบกับ S&P 500 Total Return `14.43%`; current NAV TR YTD ล่าสุดที่ยืนยันได้คือ `15.60%` ณ 2026-07-21.

## Performance check

- `entity_key`: `NYSE Arca:JPXN`; official U.S. iShares page ยืนยัน ticker JPXN, exchange NYSE Arca, asset class Equity, fund launch `2001-10-23` และ benchmark `JPX-Nikkei Index 400`.
- `Metric`: official NAV Total Return in USD; ไม่ผสมกับ market-price return. iShares ระบุว่า hypothetical growth สมมติ reinvestment ของ dividends/capital gains และหัก fund expenses.
- `Issuer benchmark`: `JPX-Nikkei Index 400 (Net)` ตาม official factsheet; product page แสดงชื่อ benchmark แบบย่อว่า `JPX-Nikkei Index 400`.
- `Expense ratio`: `0.48%` ตาม current prospectus.
- `Current NAV`: `US$98.72` ณ 2026-07-22; NAV TR YTD `15.60%` ณ 2026-07-21.
- `10-year NAV TR`: official cumulative `142.85%` และ average annual/CAGR `9.28%` ณ 2026-06-30.

### 10-year NAV TR window

| Field | Value |
|---|---:|
| Start date | 2016-06-30 |
| End date | 2026-06-30 |
| Start TR value | 100.00 (normalized index; raw NAV endpoint not disclosed) |
| End TR value | 242.85 (normalized from official cumulative 142.85%) |
| Actual years | 10.00 calendar years / 3,652 days |
| Cumulative NAV TR | 142.85% |
| CAGR | 9.28% |

Raw per-share NAV/TR endpoint levels are `not disclosed` in the compact issuer performance output; the 100.00 → 242.85 endpoints are a transparent normalization of the official cumulative return, not a claim about historical NAV prices.

### Calendar-year NAV TR vs S&P 500 Total Return

| Year | JPXN NAV TR (USD) | S&P 500 TR (USD) |
|---|---:|---:|
| 2021 | 0.40% | 28.71% |
| 2022 | -16.04% | -18.11% |
| 2023 | 19.47% | 26.29% |
| 2024 | 6.37% | 25.02% |
| 2025 | 26.05% | 17.88% |

จาก annual rows ที่ issuer เปิดเผย JPXN มี cumulative `35.03%` และ CAGR `6.19%` ใน 2021-2025 เทียบกับ S&P 500 TR cumulative `96.17%` และ CAGR `14.43%`; JPXN ต่ำกว่าประมาณ `8.24 pp` ต่อปีในช่วง common window นี้. S&P row ใช้ cached USD Total Return convention, dividends reinvested, as-of 2025-12-31.

## Up years / Down years

- Up years / Down years: `4 / 1`
- Best: `2025`, `26.05%`
- Least positive: `2021`, `0.40%`
- Worst / least bad down year: `2022`, `-16.04%`
- Current YTD: `15.60%` as of 2026-07-21; current NAV `US$98.72` as of 2026-07-22.

## Risk read-through

JPXN เป็น broad Japan equity ETF ที่มี 389 holdings ณ 2026-07-22 และ expense ratio `0.48%`. Sector exposure หลักคือ Industrials `25.78%`, Information Technology `17.62%`, Financials `15.77%` และ Consumer Discretionary `13.31%` ณ วันเดียวกัน. Official 3-year standard deviation คือ `13.54%` และ equity beta `0.66` ณ 2026-06-30. ความเสี่ยงหลักจึงอยู่ที่ Japan country/FX exposure และวัฏจักร industrials/technology; 10-year CAGR ไม่ใช่ downside protection.

## Sources

- [iShares JPXN U.S. product and performance page](https://www.blackrock.com/us/financial-professionals/products/239831/ishares-japan-largecap-etf) — identity, NYSE Arca listing, benchmark, launch date, expense ratio, NAV TR, annual rows, current NAV/YTD and risk snapshot; accessed 2026-07-24.
- [iShares JPXN factsheet](https://www.blackrock.com/us/individual/literature/fact-sheet/jpxn-ishares-japan-largecap-etf-fund-fact-sheet-en-us.pdf) — benchmark wording and NAV TR convention; factsheet as of 2026-03-31, used only for corroboration.
- [S&P 500 Total Return reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD total-return benchmark convention used in the comparison.
- [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
