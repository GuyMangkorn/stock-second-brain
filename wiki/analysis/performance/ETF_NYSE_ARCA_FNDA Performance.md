---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FNDA
ticker: FNDA
exchange: NYSE Arca
fund: Schwab Fundamental U.S. Small Company ETF
tracked_index: RAFI Fundamental High Liquidity US Small Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FNDA
  - geography/United-States
---

# FNDA Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

FNDA เป็น Schwab Fundamental U.S. Small Company ETF แบบ passive/index-tracking
บน NYSE Arca ที่ใช้ fundamental weighting กับหุ้น U.S. small-cap. Official Schwab
NAV 10-year annualized return คือ `11.53%` และ current NAV TR YTD คือ `21.18%`
ณ 2026-06-30. สำหรับ common calendar window, annual rows ที่ใช้เป็น secondary
dividend-adjusted total-return proxy ให้ 2016-2025 cumulative `159.56%` /
rounded-input CAGR `10.01%`; 2021-2025 CAGR `9.49%` ต่ำกว่า S&P 500 Total Return
`14.43%`. ตัวเลข proxy ไม่ถูก relabel เป็น official NAV rows.

## Performance check

- entity_key: `NYSE Arca:FNDA`
- Inception: 2013-08-15
- Expense ratio: 0.25%
- Metric: official Schwab NAV Total Return includes reinvested distributions and fund expenses; USD
- Tracked index (current issuer benchmark): RAFI Fundamental High Liquidity US Small Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: official annualized `11.53%` as of 2026-06-30; raw rolling endpoints are not disclosed
- Current official NAV TR YTD: `21.18%` as of 2026-06-30
- Common calendar window: 2016-2025 annual rows are secondary dividend-adjusted total-return observations; cumulative `159.56%` / rounded-input CAGR `10.01%`
- 2021-2025 secondary proxy cumulative `57.34%` / CAGR `9.49%`; S&P 500 cached 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Source-basis note: SEC material reports 2024 before-tax average annual return `8.96%`, while the secondary calendar proxy shows `8.99%`; the difference is retained rather than reconciled by invention.

| Year | FNDA secondary total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 23.54% | 11.96% |
| 2017 | 12.66% | 21.83% |
| 2018 | -12.10% | -4.38% |
| 2019 | 24.33% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 31.11% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 20.31% | 26.29% |
| 2024 | 8.99% | 25.02% |
| 2025 | 7.44% | 17.88% |

`*` Annual FNDA rows are ETFreplay dividend-adjusted total-return observations,
not issuer-published NAV rows. S&P 500 เป็น common reference benchmark ไม่ใช่
issuer benchmark ของ FNDA; annual S&P rows use the cached USD Total Return
convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 8 / 2 in the complete 2016-2025 proxy window
- Best: 2021, +31.11%*
- Least positive: 2025, +7.44%*
- Worst: 2022, -14.82%*
- Least bad down year: 2018, -12.10%*
- Current official FNDA NAV TR YTD: +21.18% as of 2026-06-30

## Risk read-through

FNDA มี small-cap, fundamental/value tilt, turnover, liquidity และ factor-regime
risk. Schwab รายงาน 3-year standard deviation `18.38%`, beta vs benchmark
`1.00`, holdings `920` และ portfolio turnover `24.76%` ณ 2026-06-30. SEC
summary prospectus ระบุ best quarter `+30.46%` ใน 4Q2020 และ worst quarter
`-35.49%` ใน 1Q2020. กองทุนเปลี่ยน comparative index จาก Russell RAFI US Small
Company Index เป็น RAFI Fundamental High Liquidity US Small Index มีผล 2024-06-21;
การอ่าน annual proxy ระยะยาวจึงต้องคำนึงถึง benchmark/methodology splice. Official
daily NAV history สำหรับคำนวณ max drawdown และ recovery ยังไม่พบข้อมูลที่ยืนยันได้.

## Sources

- [Official Schwab FNDA product page](https://www.schwabassetmanagement.com/products/fnda) — objective, index, passive style, fee, current NAV/YTD and risk/portfolio fields.
- [Official Schwab FNDA fact-sheet page](https://www.schwabassetmanagement.com/resource/fnda-fact-sheet) — issuer document entry, updated 2026-06-30.
- [SEC FNDA summary prospectus](https://www.sec.gov/Archives/edgar/data/1454889/000110465925063127/tm2513735-8_497k.htm) — passive objective, fees, index methodology change, annual-return risk quarters and official 2024 performance comparison.
- [ETFreplay FNDA annual total-return table](https://www.etfreplay.com/etf/fnda) (secondary dividend-adjusted annual proxy)
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- [S&P 500 historical reference](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
