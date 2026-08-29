---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:AVDE
ticker: AVDE
exchange: NYSE Arca
fund: Avantis International Equity ETF
tracked_index: not applicable (active strategy)
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: systematic-active
active_process_subtype: systematic value/profitability tilt with daily active oversight
management_benchmark: MSCI World ex USA IMI Index (Net Dividends)
track_record: established-under-10-years
management_evidence: positive return-only
risk_evidence: not-verified
updated: 2026-08-30
performance_as_of: 2026-06-30 (official rolling) / 2026-07-31 (current YTD)
calendar_years_as_of: official complete calendar rows not readable in reviewed capture
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-26 (assets) / 2026-07-31 (holdings and characteristics)
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/AVDE
  - geography/International
---

# AVDE ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

AVDE เป็น `active-equity-long-only` ETF ของ Avantis ที่ลงทุนแบบ all-cap ใน
developed markets นอกสหรัฐฯ โดยใช้ systematic value/profitability tilt และมี daily
active oversight. Official product page รายงาน current NAV Total Return YTD
`12.39%` ณ 2026-07-31; NAV `US$93.64` และ market price `US$93.82` ณ 2026-08-28.
กองทุนเริ่ม 24 ก.ย. 2019 จึงยังไม่ครบ 10-year history.

Official factsheet ณ 2026-06-30 รายงาน NAV Total Return แบบ annualized 1-year
`23.83%`, 3-year `19.36%`, 5-year `10.49%` และ since-inception `11.87%` เทียบกับ
management benchmark `20.76%`, `16.85%`, `8.84%` และ `10.43%` ตามลำดับ. ส่วนต่าง
แบบ return-only อยู่ที่ `+3.07`, `+2.51`, `+1.65` และ `+1.44 pp`; ยังไม่ใช่
ข้อสรุปเรื่อง persistent manager skill หรือ alpha. Official complete calendar
annual rows ที่ยืนยันได้ไม่ปรากฏใน reviewed capture จึงไม่คำนวณ 2021-2025 CAGR,
best/worst year หรือ hit rate และไม่ใช้ secondary proxy มาเติมช่องว่าง.

## Fund and measurement

- กองทุน: Avantis International Equity ETF; `entity_key: NYSE Arca:AVDE`; inception `2019-09-24`; exchange `NYSE Arca`.
- Expense ratio `0.23%` และ dividend frequency รายไตรมาส. Total assets `US$19,185,290,809` ณ 2026-08-26; holdings `3,300` และ weighted average market cap `US$66.07B` ณ 2026-07-31.
- Primary metric: NAV Total Return รวม dividends/capital gains ที่ reinvested และหัก fund expenses; currency USD.
- Current official YTD ณ 2026-07-31: NAV TR `+12.39%`; market-price TR `+12.39%`. Current NAV/market price ณ 2026-08-28: `US$93.64` / `US$93.82`.
- 10-year NAV TR: `not applicable (<10-year history)`; factsheet reports no 10-year field.

## Official rolling performance

| Window | AVDE NAV TR | MSCI World ex USA IMI (Net Dividends) | Return-only excess |
|---|---:|---:|---:|
| YTD as of 2026-06-30 | 10.20% | 8.96% | +1.24 pp |
| 1-year as of 2026-06-30 | 23.83% | 20.76% | +3.07 pp |
| 3-year annualized as of 2026-06-30 | 19.36% | 16.85% | +2.51 pp |
| 5-year annualized as of 2026-06-30 | 10.49% | 8.84% | +1.65 pp |
| Since inception annualized as of 2026-06-30 | 11.87% | 10.43% | +1.44 pp |

The current 2026 YTD field `+12.39%` is a later official product-page snapshot
than the synchronized factsheet table above; no later benchmark value was
inferred.

## Calendar-year completeness

| Evidence item | Status |
|---|---|
| Complete 2021-2025 official NAV annual rows | not disclosed in reviewed official capture |
| 2021-2025 NAV CAGR | not calculated |
| Best / worst calendar year and up/down hit rate | not calculated |
| Official daily NAV series for maximum drawdown and recovery | not verified |

The 2019 inception year is partial and the available official materials do not
provide a readable complete annual table for the requested calendar window.
Using a secondary price or distribution proxy would mix return bases with the
official NAV record, so no proxy is substituted.

## Risk read-through

Risk evidence is `not-verified` for official daily NAV maximum drawdown, recovery
date, recovery duration, standard deviation, and beta in the reviewed sources.
Key risks are developed ex-U.S. country and currency exposure, all-cap and
small-/mid-cap liquidity, value/profitability factor regimes, sector concentration,
and active-process/benchmark risk. The official factsheet lists 3,277 holdings as
of 2026-06-30; the newer product page lists 3,300 holdings as of 2026-07-31.

## Active-management read-through

- `management_mode`: `active-equity-long-only`
- `active_process`: `systematic-active`; Avantis combines valuation and profitability information with daily portfolio oversight across developed ex-U.S. all-cap stocks.
- `management_benchmark`: `MSCI World ex USA IMI Index (Net Dividends)`; selected because the official factsheet identifies it as the strategy-aligned comparator.
- `track_record`: `established-under-10-years` (inception 2019-09-24; more than five years, less than ten years).
- `management_evidence`: `positive return-only`; official NAV TR exceeds the management benchmark over the synchronized 1Y, 3Y, 5Y, and since-inception periods. Calendar hit rate and persistence were not verified.
- `risk_evidence`: `not-verified`; no official daily NAV drawdown/recovery series or risk-adjusted manager-skill evidence was captured.

## Sources

- [Avantis AVDE trading details](https://www.avantisinvestors.com/avantis-investments/avantis-international-equity-etf/trading-details/) — official current NAV/market-price snapshot, current YTD return, assets, holdings, characteristics, fee, exchange, and product description.
- [Avantis AVDE factsheet](https://res.avantisinvestors.com/docs/avantis-international-equity-avde-etf-fact-sheet.pdf) — official rolling NAV/market-price returns, management benchmark, inception, fee, distribution frequency, and fund facts as of 2026-06-30.
- [SEC AVDE summary prospectus](https://www.sec.gov/Archives/edgar/data/1710607/000171060725000399/acetftavde497k.htm) — official NYSE Arca identity, active all-cap developed ex-U.S. strategy, objective, and benchmark context.
- S&P 500 Total Return cached convention from the workflow was not used for a calendar comparison because official AVDE calendar rows were not readable as a complete matching window.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
