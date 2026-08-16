---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:CALF
ticker: CALF
exchange: Cboe BZX
fund: Pacer US Small Cap Cash Cows ETF
former_fund_name: Pacer US Small Cap Cash Cows 100 ETF
fund_name_change: 2025-03-10
tracked_index: Pacer US Small Cap Cash Cows Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2026-06-22
annual_rows_as_of: 2025-12-31
current_ytd_as_of: "2026-06-22; separate stale snapshot also reported 2026-06-16"
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CALF
  - geography/United-States
---

# CALF Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

CALF ยังมีประวัติไม่ครบ 10 ปี: annual NAV TR ที่ยืนยันได้เป็น 2018-2024 และ issuer 1 Year/YTD field ที่สิ้นสุด 2025-12-31. ช่วง 2018-2025 ให้ cumulative 90.45% และ rounded-input annualized return ประมาณ 8.39%; ช่วง 2021-2025 ให้ cumulative 52.99% และ rounded-input CAGR ประมาณ 8.88%. ในช่วง 2021-2025 มี 3 ปีบวกและ 2 ปีลบ โดยปีดีที่สุดคือ 2021 ที่ +40.50% และแย่ที่สุดคือ 2022 ที่ -15.18%. Current official NAV YTD ที่ตรวจพบเป็นคนละ stale snapshot: 10.60% ณ 2026-06-22 และ 12.78% ณ 2026-06-16; ไม่พบตัวเลขที่เป็น as-of 2026-08-16 จึงไม่รวมเป็น current-date claim เดียว.

## Performance check

- entity_key: Cboe BZX:CALF
- Fund: Pacer US Small Cap Cash Cows ETF; former name: Pacer US Small Cap Cash Cows 100 ETF; name change effective 2025-03-10
- Classification: passive index-tracking U.S. small-cap equity ETF
- Inception: 2017-06-16; Cboe BZX listing: 2017-06-19
- Expense ratio: 0.59%; confirmed by the [Pacer product page](https://www.paceretfs.com/products/CALF) and [summary prospectus](https://docs.paceretfs.com/assets/pdfs/Pacer_CALF_Summary.pdf) dated 2025-08-31
- Issuer benchmark: Pacer US Small Cap Cash Cows Index
- Index methodology: starts from S&P US SmallCap, applies liquidity, projected free-cash-flow and earnings/listing screens, ranks the eligible universe by TTM free cash flow divided by enterprise value, selects the top 200 and weights by free cash flow subject to caps; S&P DJI is the administrator from 2024-11-18. V1/V2 variants launched 2025-09-30 with the same methodology from 2025-06-20
- NAV Total Return: USD NAV return with dividends and capital-gain distributions reinvested; expenses reflected in NAV; issuer index excludes fund fees
- Common benchmark: S&P 500 Total Return, USD, dividends reinvested; cached reference as of 2025-12-31
- Annual NAV TR source: official [Pacer performance sheet](https://www.paceretfs.com/media/why_calf.pdf); 2018-2024 are complete calendar rows. The 2025 2.34% observation is labelled by the issuer as 1 Year/YTD ending 2025-12-31 and is retained with that caveat, not silently relabelled as a separately disclosed calendar-year row
- 2018-2025: cumulative 90.45%; rounded-input annualized return approximately 8.39%
- 2021-2025: cumulative 52.99%; rounded-input CAGR approximately 8.88%; average positive year 26.13%
- Current official performance snapshots: NAV TR YTD 10.60% as of 2026-06-22 from the [Pacer product page](https://www.paceretfs.com/products/CALF); a separate Pacer product-listing snapshot reports NAV TR YTD 12.78% as of 2026-06-16. These are different stale as-of dates, not a same-date conflict; no 2026-08-16 figure was located
- Additional issuer fields: NAV TR 1 Year 21.46% and 10-year n/a as of 2026-03-31; since-inception NAV TR 8.44% as of 2026-03-31
- Current quote snapshot: NAV 50.50 USD and market price 50.51 USD as of 2026-06-12
- Recent distributions total 0.6071575 USD across the 2025-09-04 to 2026-06-04 observations; indicative 0.6071575 / 50.50 = 1.20%, not a total-return or issuer distribution-yield claim

### Annual NAV TR

| Year | CALF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | -9.71% | -4.38% |
| 2019 | 18.54% | 31.49% |
| 2020 | 16.31% | 18.40% |
| 2021 | 40.50% | 28.71% |
| 2022 | -15.18% | -18.11% |
| 2023 | 35.54% | 26.29% |
| 2024 | -7.45% | 25.02% |
| 2025 | 2.34%† | 17.88% |

2018-2025 CALF annualized return approximately 8.39% versus S&P 500 TR CAGR 14.33% over the same eight-row calculation window. 2021-2025 CALF rounded-input CAGR approximately 8.88% versus S&P 500 TR CAGR 14.43%, a -5.55 percentage-point spread. Calculations use rounded official annual inputs; the 2025 CALF input carries the issuer 1 Year/YTD label caveat.

## Up years / Down years

- 2018-2025: 5 up years and 3 down years
- 2021-2025: 3 up years and 2 down years
- Best year in 2021-2025: 2021, +40.50%
- Least-positive year in 2021-2025: 2025, +2.34%†
- Worst year in 2021-2025: 2022, -15.18%
- Least-bad down year in 2021-2025: 2024, -7.45%

## Risk read-through

CALF เป็น small-cap equity ETF ที่มีความเสี่ยงจาก free-cash-flow/valuation factor, sector concentration, turnover, liquidity, passive tracking, ETF premium/discount และ market drawdown. Issuer reports the best quarter as +35.33% in 2Q2020 and the worst quarter as -35.46% in 1Q2020. Official daily NAV history sufficient for maximum drawdown and recovery is not verified; no numeric secondary proxy is saved.

## Recent distributions

| Ex-date | Payable date | Distribution (USD) |
|---|---|---:|
| 2026-06-04 | 2026-06-08 | 0.0447590 |
| 2026-03-05 | 2026-03-09 | 0.0709307 |
| 2025-12-30 | 2026-01-05 | 0.3314134 |
| 2025-09-04 | 2025-09-10 | 0.1600544 |

Distributions เป็น cash-flow ที่แยกจาก NAV TR ซึ่งคำนวณโดยสมมติ reinvestment.

## Sources

- [Pacer CALF product page](https://www.paceretfs.com/products/CALF)
- [Pacer CALF product-listing snapshot](https://www.paceretfs.com/products)
- [Pacer CALF summary prospectus](https://docs.paceretfs.com/assets/pdfs/Pacer_CALF_Summary.pdf)
- [Pacer CALF performance sheet](https://www.paceretfs.com/media/why_calf.pdf)
- [Cboe listed symbols / CALF listing reference](https://www.cboe.com/us/equities/market_statistics/listed_symbols/)
- [Cboe name-change circular reference](https://cdn.cboe.com/resources/regulation/circulars/products/IC-2025-139.pdf)
- [S&P DJI Pacer US Small Cap Cash Cows Index methodology](https://www.spglobal.com/spdji/en/indices/strategy/pacer-us-small-cap-cash-cows-index/)
- [Pacer distribution schedule](https://www.paceretfs.com/resources/distributions)
- [S&P 500 index reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Source batch: [[ETF_performance_sources_2026-08-16]]
