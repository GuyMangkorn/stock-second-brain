---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWT
ticker: EWT
exchange: NYSE Arca
issuer: iShares
fund: iShares MSCI Taiwan ETF
tracked_index: MSCI Taiwan 25/50 Index
benchmark: S&P 500 Total Return
inception: 2000-06-20
expense_ratio: 0.59%
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-20
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWT
  - geography/Taiwan
---

# EWT Performance

> Navigation: [[ETF Region Index]] → [[Taiwan ETF]] → [[ETF Performance Index]]

## Bottom line

EWT เป็น passive/index-tracking equity ETF ที่ให้ exposure ต่อ Taiwan แบบ single-country และติดตาม `MSCI Taiwan 25/50 Index`. Official NAV Total Return (รวม reinvested distributions และหัก fund expenses ตาม growth-of-$10,000 convention) ให้ cumulative `552.21%` และ CAGR `20.63%` ในช่วง 2016-06-30 ถึง 2026-06-30 หรือ `10.00 calendar years`. ช่วง 2021-2025 ให้ CAGR `12.01%` ต่ำกว่า S&P 500 Total Return ที่ `14.43%`; current NAV YTD ล่าสุดที่ยืนยันได้คือ `50.68%` ณ 2026-07-20.

## Performance check

- `entity_key`: `NYSE Arca:EWT`; issuer page ยืนยัน exchange เป็น NYSE Arca, asset class เป็น Equity, inception `2000-06-20` และ benchmark เป็น `MSCI Taiwan 25/50 Index`.
- `Metric`: official NAV Total Return; ไม่ผสมกับ market-price return. iShares ระบุว่า hypothetical growth สมมติ reinvestment ของ dividends/capital gains และหัก fund expenses.
- `Expense ratio`: `0.59%` ตาม current prospectus.
- `Current NAV`: `US$95.76` และ NAV TR YTD `50.68%` ณ 2026-07-20.
- `10-year NAV TR`: official cumulative `552.21%` และ average annual/CAGR `20.63%` ณ 2026-06-30.

### 10-year NAV TR window

| Field | Value |
|---|---:|
| Start date | 2026-06-30 minus 10 calendar years = 2016-06-30 |
| End date | 2026-06-30 |
| Start TR value | 100.00 (normalized index; raw NAV endpoint not disclosed) |
| End TR value | 652.21 (normalized from official cumulative 552.21%) |
| Actual years | 10.00 calendar years / 3,652 days |
| Cumulative NAV TR | 552.21% |
| CAGR | 20.63% |

Raw per-share NAV/TR endpoint levels are `not disclosed` in the compact issuer performance output; the 100.00 → 652.21 endpoints are a transparent normalization of the official cumulative return, not a claim about historical NAV prices.

### Calendar-year NAV TR vs S&P 500 Total Return

| Year | EWT NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 28.38% | 28.71% |
| 2022 | -28.75% | -18.11% |
| 2023 | 29.15% | 26.29% |
| 2024 | 16.79% | 25.02% |
| 2025 | 27.81% | 17.88% |

จาก annual rows ที่ issuer เปิดเผย EWT มี cumulative `76.34%` และ CAGR `12.01%` ใน 2021-2025 เทียบกับ S&P 500 TR cumulative `96.17%` และ CAGR `14.43%`; EWT ต่ำกว่าประมาณ `2.42 pp` ต่อปีในช่วง common window นี้. S&P row ใช้ cached USD Total Return convention, dividends reinvested, as-of 2025-12-31.

## Up years / Down years

- Up years / Down years: `4 / 1`
- Best: `2023`, `29.15%`
- Least positive: `2024`, `16.79%`
- Worst / least bad down year: `2022`, `-28.75%`

## Risk read-through

Taiwan และ sector concentration เป็นตัวขับหลัก: Information Technology `71.92%` ของ market value ณ 2026-07-20; fund มี 79 holdings. Official 3-year standard deviation คือ `23.22%` และ equity beta `1.28` ณ 2026-06-30. จึงเป็น equity-risk สูงและไวต่อ semiconductor/technology cycle, Taiwan country risk และ FX; 10-year CAGR ไม่ใช่ downside protection.

## Sources

- [iShares MSCI Taiwan ETF product page](https://www.ishares.com/us/products/239686/EWT) — identity, NYSE Arca listing, benchmark, inception, expense ratio, NAV TR, annual rows, current NAV/YTD and risk snapshot; accessed 2026-07-24.
- [S&P 500 Total Return reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD total-return benchmark convention used in the comparison.
- [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
