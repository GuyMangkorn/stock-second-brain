---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLCH
ticker: FLCH
exchange: NYSE Arca
fund: Franklin FTSE China ETF
tracked_index: FTSE China RIC Capped Index / FTSE China Capped Index
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-10
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLCH
  - geography/China
---

# FLCH Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

FLCH เป็น passive, indexed, physical China equity ETF ที่ติดตาม FTSE China RIC Capped Index และจดทะเบียนบน NYSE Arca. Inception `2017-11-02` ถึง latest complete month-end `2026-06-30` มีเพียง `8.657084` elapsed years จึงระบุชัดว่า `10-year NAV TR unavailable`. Official available-period NAV TR เป็น average annual `-0.24%`; current official NAV TR YTD ล่าสุดที่พบคือ `-10.65%` ณ `2026-07-10`.

## Performance check

- entity_key: `NYSE Arca:FLCH`
- ISIN: `US35473P8196`
- Inception: `2017-11-02`
- Asset class / structure: Equity; indexed; physical index exposure; semi-annual distributions
- Tracked index / issuer benchmark: FTSE China RIC Capped Index / FTSE China Capped Index-NR
- Metric: NAV Total Return including reinvested distributions and fund expenses; Franklin states total returns assume reinvestment of all distributions and deduction of all fund expenses
- Gross / net expense ratio: `0.19%` / `0.19%` as of prospectus `2025-08-01`
- 10-year NAV TR: `unavailable`; official 10-year field is `—`
- Available-period window: `2017-11-02` to `2026-06-30`; actual years `8.657084`
- Start TR value: `not disclosed`
- End TR value: `not disclosed`
- Official available-period NAV TR: average annual `-0.24%` as of `2026-06-30`; cumulative inception NAV TR is `not disclosed`
- Formula for a disclosed endpoint-based CAGR: `CAGR = (End TR / Start TR)^(1 / actual years) - 1`; no endpoint value or cumulative proxy is invented

Official calendar NAV rows below come from Franklin's June 2026 factsheet as of `2026-06-30`. 2017 is a partial inception year and is not ranked. S&P 500 rows reuse the cached USD Total Return convention for complete calendar years `2016-2025`; the common 2021-2025 comparison is therefore shown separately from the shorter fund history.

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2017† | not disclosed; partial inception year | 21.83% |
| 2018 | -18.28% | -4.38% |
| 2019 | 22.92% | 31.49% |
| 2020 | 30.60% | 18.40% |
| 2021 | -21.04% | 28.71% |
| 2022 | -22.25% | -18.11% |
| 2023 | -11.98% | 26.29% |
| 2024 | 19.17% | 25.02% |
| 2025 | 31.61% | 17.88% |
| 2026 YTD | -10.65% as of 2026-07-10 | not comparable; current year not cached |

## Up years / Down years

- Up years / Down years: `4 / 4` among complete calendar years `2018-2025`
- Best: `2025`, `+31.61%`
- Least positive: `2024`, `+19.17%`
- Worst: `2022`, `-22.25%`
- Least bad down year: `2021`, `-21.04%`
- 2018-2025 ETF NAV TR: cumulative `+11.18%`; CAGR `+1.33%`
- 2021-2025 ETF NAV TR: cumulative `-15.25%`; CAGR `-3.25%`
- 2021-2025 S&P 500 TR: cumulative `+96.17%`; CAGR `+14.43%`
- 2021-2025 CAGR gap versus S&P 500 TR: approximately `-17.68` percentage points
- Current NAV TR YTD: `-10.65%` as of `2026-07-10`
- Current NAV: `US$21.16` as of `2026-07-10`; this is a NAV level, not a return metric

## Risk read-through

FLCH ให้ broad China large-/mid-cap exposure แต่ยังมี country, policy, regulatory, geopolitical และ FX concentration สูง. As of `2026-06-30`, top issuers included Tencent `12.44%` and Alibaba `7.86%`; sector weights included consumer discretionary `21.42%`, financials `18.83%`, communication services `17.10%`, and information technology `13.63%`. Daily NAV history sufficient for max drawdown/recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Franklin product/performance page: https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26362/SINGLCLASS/franklin-ftse-china-etf/FLCH
- Official Franklin June 2026 factsheet: https://www.franklintempleton.com/forms-literature/download/FLCH-FF
- Official Franklin prospectus: https://www.franklintempleton.com/forms-literature/download/ETF5-P
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
