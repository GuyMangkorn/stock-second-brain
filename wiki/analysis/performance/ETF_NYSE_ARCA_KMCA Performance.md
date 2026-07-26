---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KMCA
ticker: KMCA
exchange: NYSE Arca
fund: PLUS Korea Manufacturing Core Alliance Index ETF
tracked_index: Akros Korea Manufacturing Core Alliance Index
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KMCA
  - geography/South-Korea
---

# KMCA Performance

> Navigation: [[ETF Region Index]] → [[South Korea ETF]] → [[ETF Performance Index]]

## Bottom line

KMCA เป็น passive/index-tracking South Korea equity ETF ที่จดทะเบียนบน NYSE
Arca และติดตาม `Akros Korea Manufacturing Core Alliance Index`. กองทุนเริ่ม
วันที่ `2026-05-06` จึงมี `10-year NAV TR unavailable` และยังไม่มี complete
calendar year. Official Fund NAV Total Return ที่ยืนยันได้สำหรับช่วงเริ่มกองทุน
ถึง `2026-06-30` คือ `-5.14%` cumulative; ไม่ annualize ช่วงเวลาต่ำกว่าหนึ่งปี.

## Performance check

- entity_key: `NYSE Arca:KMCA`
- Inception: `2026-05-06`
- Structure: passive/index-tracking, non-diversified South Korea equity ETF;
  SEC prospectus states the fund is not actively managed and normally invests
  at least 80% of net assets in index securities.
- Metric: official Fund NAV performance / NAV Total Return basis; market-price
  return is kept separate.
- Tracked index: `Akros Korea Manufacturing Core Alliance Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark, not KMCA's tracked index)
- 10-year NAV TR: `unavailable`; the legal fund has only a partial 2026 history.
- Available-period window: `2026-05-06` to `2026-06-30`
- Actual elapsed time: `55 days` / `365.25 = 0.150582 years`
- Normalized start/end TR values: `100.00` / `94.86`; issuer raw NAV index
  endpoints are `not disclosed`. End value is calculated as
  `100 × (1 - 5.14%)` from the official cumulative Fund NAV return.
- Available-period NAV TR: `-5.14%` cumulative; no CAGR is reported because
  the official performance table says returns under one year are not annualized.
- Latest official current NAV: `US$18.78` as of `2026-07-23`; latest official
  numeric NAV TR YTD remains `-5.14%` as of `2026-06-30`.

| Period | KMCA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2026 YTD / since inception (2026-05-06 to 2026-06-30) | -5.14% | not disclosed for the same official date window |

There are no complete calendar-year NAV TR observations yet. The S&P 500
comparison is retained as the required common reference, but no same-window
numeric S&P 500 Total Return is inserted because it was not disclosed in the
reviewed official benchmark capture; the cached S&P rows begin with complete
calendar years and are not a valid substitute for KMCA's 55-day window.

## Up years / Down years

- Complete calendar years: `not applicable` — fund inception was `2026-05-06`
- Up years / Down years: `not applicable`
- Best / worst / least positive / least bad down year: `not applicable`
- Current NAV TR YTD: `-5.14%` as of `2026-06-30`; this is also the available
  since-inception return, not a 10-year figure.

## Risk read-through

KMCA is a new, non-diversified, single-country thematic ETF concentrated in
Korea's manufacturing industries. The prospectus describes approximate index
weights of 40% AI semiconductors and roughly 12% each for rechargeable
batteries, shipbuilding, defense, power grid and nuclear energy, and robotics
and humanoids; exposures can change at rebalance. Total annual fund operating
expenses are `0.65%`. Official daily NAV Total Return drawdown and recovery data
are `not disclosed`; no secondary proxy is substituted.

## Sources

- [Official PLUS KMCA product and performance page](https://plusetf.com/kmca) — identity, primary exchange, inception, index description, fee, holdings snapshot, NAV, official month-end/quarter-end NAV and market-price performance, and as-of dates
- [Official SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1547950/000121390026047871/ea0286568-02_497k.htm) — NYSE Arca listing, index objective, 80% policy, passive/non-active classification, fee, risks and no-performance-history disclosure
- [Official SEC prospectus and SAI filing](https://www.sec.gov/Archives/edgar/data/1547950/000121390026047633/ea0286568-01_485bpos.htm) — formal listing, index methodology, concentration and risk disclosures
- [Official NYSE Arca listing circular](https://www.nasdaqtrader.com/content/newsalerts/2026/infocircular/KMCA_Circular.pdf) — listing-market and ticker cross-check
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
