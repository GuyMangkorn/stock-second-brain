---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:EWJV
ticker: EWJV
exchange: NASDAQ
fund: iShares MSCI Japan Value ETF
tracked_index: MSCI Japan Value Index (USD) (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWJV
  - geography/Japan
---

# EWJV Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

EWJV เป็น passive/index-tracking NASDAQ equity ETF ที่ track MSCI Japan Value Index (USD) (Net). Fund inception คือ 2019-03-05 จึงยังไม่มี 10-year NAV Total Return: `10-year NAV TR unavailable`. Official iShares page ณ 2026-06-30 รายงาน available-period NAV TR since-inception annualized `12.13%` จาก 2019-03-05 ถึง 2026-06-30 หรือประมาณ `7.32` elapsed years. Raw NAV endpoints ไม่ได้เปิดเผย; normalized TR start `100.00` และ end ประมาณ `231.22` เป็นค่าคำนวณจาก CAGR ที่ issuer ปัดเศษ. Official calendar rows ที่ยืนยันได้คือ 2021-2025; current NAV TR YTD คือ `18.04%` ณ 2026-07-22.

## Performance check

- entity_key: NASDAQ:EWJV
- Inception: 2019-03-05
- Metric: NAV Total Return; distributions reinvested and fund expenses deducted in the standard NAV total-return presentation; market-price return is separate
- Tracked index: MSCI Japan Value Index (USD) (Net)
- Structure: passive/index-tracking equity ETF; semi-annual distributions; expense ratio `0.15%`
- 10-year NAV TR coverage: unavailable because actual fund history is under 10 years
- Status: `completed_available_period_no_10Y`
- Available-period NAV TR: 2019-03-05 to 2026-06-30; actual years approximately `7.32`; official since-inception annualized return `12.13%`
- Normalized available-period TR: start `100.00`; end `231.22` (calculated as `100 × (1 + 12.13%)^7.32`; raw endpoints not disclosed)
- Coverage/source note: official calendar rows are available for 2021-2025. This page does not label the available period as 10-year and does not backfill 2019-2020 calendar rows.

| Year | EWJV NAV TR | MSCI Japan Value Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | 6.16% | 5.88% | 28.71% |
| 2022 | -5.68% | -5.26% | -18.11% |
| 2023 | 23.05% | 23.11% | 26.29% |
| 2024 | 11.77% | 12.76% | 25.02% |
| 2025 | 33.56% | 32.00% | 17.88% |

## Up years / Down years

- Up years / Down years: `4 / 1` over the five complete calendar years 2021-2025
- Best complete calendar year: 2025, `33.56%`
- Least positive complete calendar year: 2021, `6.16%`
- Worst complete calendar year: 2022, `-5.68%`
- Least bad down year: 2022, `-5.68%`
- 2021-2025 NAV rows compound to `83.93%` / CAGR `12.96%`; this is a five-year calendar window, not a 10-year result
- S&P 500 common-window CAGR is `14.43%`, so EWJV trails by approximately `1.47 pp` CAGR over 2021-2025
- Current NAV TR YTD: `18.04%` as of 2026-07-22; NAV `US$46.21` as of 2026-07-22

## Risk read-through

EWJV เป็น Japan value-factor equity ETF with meaningful financials and industrials exposure. Official holdings มี `109` ตัว ณ 2026-07-22; financials `33.95%`, industrials `18.91%`, consumer discretionary `14.97%`; 3-year standard deviation `12.83%` และ beta `0.42` ณ 2026-06-30. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Official iShares EWJV product and performance page](https://www.ishares.com/us/products/307263/ishares-msci-japan-value-etf)
- [Official iShares EWJV factsheet](https://www.ishares.com/us/literature/fact-sheet/ewjv-ishares-msci-japan-value-etf-fund-fact-sheet-en-us.pdf)
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
