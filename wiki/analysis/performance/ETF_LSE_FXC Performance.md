---
type: etf-performance
instrument_type: ETF
entity_key: LSE:FXC
ticker: IHRPF
listing_ticker: FXC
exchange: LSE
fund: iShares China Large Cap UCITS ETF
tracked_index: FTSE China 50 Index - USD Net Div (USD)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IHRPF
  - geography/China
---

# IHRPF Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

IHRPF คือ OTC alias ของ USD listing `LSE:FXC` ใน iShares China Large Cap UCITS ETF ซึ่งเป็น passive, physical, index-tracking China equity ETF. Official NAV Total Return 10-year window (`2016-06-30` ถึง `2026-06-30`, `10.00` years) ให้ cumulative `18.61%` และ annualized CAGR `1.72%`. Current official NAV TR YTD คือ `-17.31%` ณ `2026-06-30`.

## Performance check

- Input ticker: `IHRPF` (OTC alias)
- Canonical entity key: `LSE:FXC` (official USD London Stock Exchange line; ISIN `IE00B02KXK85`)
- Inception/share-class launch: `2004-10-21`
- Asset class / structure: Equity; physical replication; distributing
- Tracked index: FTSE China 50 Index - USD Net Div (USD)
- Metric: NAV Total Return; iShares states that performance is on a NAV basis with gross income reinvested where applicable, after fund expenses
- TER: `0.74%`
- 10-year NAV TR window: `2016-06-30` to `2026-06-30`; actual years `10.00`
- Start TR value: `not disclosed`
- End TR value: `not disclosed`
- Official cumulative NAV TR: `18.61%`
- Official 10-year NAV TR CAGR: `1.72%`
- Formula: `CAGR = (End TR / Start TR)^(1 / actual years) - 1`; endpoint levels are not disclosed by the issuer, so no endpoint value is invented

Official annual rows below use the issuer factsheet's two-decimal NAV TR observations as of `2026-03-31`; the current iShares performance page confirms the same `2016-2025` calendar series rounded to one decimal and supplies the more recent rolling 10-year/YTD observations as of `2026-06-30`. S&P 500 rows reuse the cached USD Total Return convention for complete calendar years `2016-2025`.

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.80% | 11.96% |
| 2017 | 34.51% | 21.83% |
| 2018 | -12.39% | -4.38% |
| 2019 | 13.76% | 31.49% |
| 2020 | 10.06% | 18.40% |
| 2021 | -20.70% | 28.71% |
| 2022 | -20.01% | -18.11% |
| 2023 | -13.57% | 26.29% |
| 2024 | 31.03% | 25.02% |
| 2025 | 28.16% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 4`
- Best: `2017`, `+34.51%`
- Least positive: `2019`, `+13.76%`
- Worst: `2021`, `-20.70%`
- Least bad down year: `2022`, `-20.01%`
- 2016-2025 ETF NAV TR: cumulative `+38.28%`; CAGR `+3.29%`
- 2021-2025 ETF NAV TR: cumulative `-7.93%`; CAGR `-1.64%`
- 2021-2025 S&P 500 TR: cumulative `+96.17%`; CAGR `+14.43%`
- 2021-2025 CAGR gap versus S&P 500 TR: approximately `-16.07` percentage points
- Current NAV TR YTD: `-17.31%` as of `2026-06-30`
- Latest reported NAV: `US$91.61` as of `2026-07-02`; this is NAV level, not a return metric

## Risk read-through

การกระจุกตัวอยู่ในหุ้นจีน large-cap 50 บริษัทและความเสี่ยงประเทศ/นโยบาย/ค่าเงินสูงกว่าดัชนีหุ้นสหรัฐฯ ในช่วง 2016-2025 กองทุนมีปีบวก 6 ปีและปีลบ 4 ปี และผลตอบแทน 2021-2025 ต่ำกว่า S&P 500 TR อย่างมาก. iShares ระบุว่ากองทุนเปลี่ยน benchmark จาก FTSE China 25 เป็น FTSE China 50 มีผล ณ close `2014-09-19`; จึงต้องอ่านประวัติผลตอบแทนระยะยาวโดยคำนึงถึง benchmark splice นี้. Daily NAV history สำหรับคำนวณ max drawdown/recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official iShares product page: https://www.ishares.com/ch/individual/en/products/251798/ishares-china-large-cap-ucits-etf
- Official iShares factsheet: https://www.ishares.com/ch/professionals/en/literature/fact-sheet/fxc-ishares-china-large-cap-ucits-etf-fund-fact-sheet-en-ch-institutional.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
