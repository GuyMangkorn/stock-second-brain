---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:DFIS
ticker: DFIS
exchange: Cboe BZX
fund: Dimensional International Small Cap ETF
tracked_index: no specific index; actively managed
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: systematic-active
management_benchmark: MSCI World ex USA Small Cap Index (net dividends)
track_record: provisional
management_evidence: positive
risk_evidence: not-verified
updated: 2026-08-17
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-08-12
price_nav_as_of: 2026-08-13
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DFIS
  - geography/International
---

# DFIS Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DFIS เป็น active long-only international small-cap ETF ของ Dimensional ที่ใช้
systematic-active process และไม่ได้มุ่ง replicate ดัชนีใดโดยเฉพาะ. Official
complete calendar rows ที่ยืนยันได้คือ 2023-2025: NAV Total Return cumulative
64.16% และ rounded-input CAGR 17.97%. กองทุนชนะ management benchmark ที่เลือก
คือ MSCI World ex USA Small Cap Index (net dividends) ในทั้งสามปี โดยมี Excess
CAGR +2.20 percentage points และ relative wealth +5.80%; หลักฐานนี้เป็น
return-only management evidence ไม่ใช่ alpha claim. Current YTD `14.18%*` ณ
2026-08-12 เป็น secondary market-price + cash-distribution proxy ไม่ใช่
official NAV Total Return.

## Performance check

- entity_key: Cboe BZX:DFIS
- Inception: 2022-03-23; listing venue Cboe BZX Exchange
- Expense ratio: 0.39% total annual fund operating expenses; management fee 0.35% and other expenses 0.04% in the 2026 summary prospectus
- Metric: official NAV Total Return รวม reinvested distributions และ fund expenses; market-price return remains separate; currency USD
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- management_mode: active-equity-long-only
- active_process: systematic-active; official SEC strategy combines integrated research, portfolio design, portfolio management and trading
- management_benchmark: MSCI World ex USA Small Cap Index (net dividends), selected because the official performance table identifies it as an additional index with a similar investment universe; the broader MSCI World ex USA Index and S&P 500 remain reference context only
- track_record: provisional; official since-inception observation runs from 2022-03-23 to 2025-12-31, approximately 3.78 elapsed years, with three complete comparable calendar years
- management_evidence: positive; annual active differences were +2.42 pp in 2023, +1.03 pp in 2024, and +3.42 pp in 2025; Excess CAGR +2.20 pp and hit rate 3/3
- risk_evidence: not-verified; official daily NAV history sufficient for reproducible maximum drawdown and recovery was not captured
- 10-year window: not applicable (<10 years of history)
- Coverage/source note: official annual chart covers 2023-2025. The 2022 inception-year partial is excluded. Current 2026 YTD is marked `*` because it is a secondary proxy.

| Year / window | DFIS NAV TR | Management benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2023 | 15.04% | 12.62% | 26.29% |
| 2024 | 3.79% | 2.76% | 25.02% |
| 2025 | 37.49% | 34.07% | 17.88% |
| 2023-2025 cumulative | 64.16% | 55.16% | 86.12% |
| 2023-2025 CAGR | 17.97% | 15.77% | 23.01% |

S&P 500 เป็น common reference benchmark ไม่ใช่ management benchmark ของ DFIS;
annual comparison ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 3 / 0 ใน complete official 2023-2025 rows
- Best: 2025, +37.49%
- Least positive: 2024, +3.79%
- Worst: ไม่พบ down year ใน complete official rows
- Least bad down year: ไม่พบข้อมูลที่ยืนยันได้
- 2023-2025 cumulative / CAGR: 64.16% / 17.97%; management benchmark 55.16% / 15.77%; S&P 500 TR 86.12% / 23.01%
- Annual active differences versus management benchmark: +2.42 pp, +1.03 pp, +3.42 pp
- Current date-to-date YTD*: 14.18% as of 2026-08-12, calculated as `(37.27 + 0.4222) / 32.94 - 1`; this uses secondary closing price plus one cash distribution and is not NAV TR

## Risk read-through

DFIS มี developed ex-U.S. small-cap exposure และ official prospectus ระบุ
small-company, foreign securities/currencies, geographic, value, profitability,
market-trading และ international closed-market risks. Population standard
deviation ของ official 2023-2025 annual rows อยู่ที่ 14.01% แต่มีเพียงสามปี
จึงเป็นเพียง short-window descriptor. Official highest quarter คือ +17.37%
ใน Q2 2025 และ lowest quarter -7.85% ใน Q4 2024. Schwab reports a secondary
price snapshot of US$37.34 at 11:12am ET on 2026-08-13, previous close
US$37.27, and closing NAV US$37.18 on 2026-08-12; premium/discount was +0.24%.
Official daily NAV history for a reproducible maximum drawdown and recovery was
not verified. The latest summary also reports 3,461 holdings and 9% turnover.

## Active management read-through

- management_mode: active-equity-long-only
- active_process: systematic-active
- management_benchmark: MSCI World ex USA Small Cap Index (net dividends)
- track_record: provisional
- management_evidence: positive return-only
- risk_evidence: not-verified
- Annual active differences were +2.42 pp, +1.03 pp and +3.42 pp; the 2023-2025 Excess CAGR was +2.20 pp, hit rate 3/3 = 100%, and relative wealth was +5.80%.
- The selected benchmark is strategy-aligned small-cap international exposure from the official performance table. S&P 500 TR is retained only as a common reference and is not used to infer manager skill.
- The official manager continuity block names Jed S. Fogdall, Joseph F. Hohn and Joel P. Schneider since inception, with Brendan J. McAndrews since 2025. The strategy is described as an integrated research, portfolio-design, portfolio-management and trading process.
- These are benchmark-relative return observations over a provisional three-year live window, not alpha. Risk evidence remains incomplete because compatible daily NAV data for drawdown and recovery was not verified.

## Sources

- Official SEC summary prospectus: https://www.sec.gov/Archives/edgar/data/1816125/000181612526000070/c497k.htm
- Official Dimensional fund page: https://www.dimensional.com/us-en/funds/dfis/international-small-cap-etf
- Official Dimensional ETF Quick Guide: https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf
- Official Cboe listing: https://www.cboe.com/us/equities/listings/listed_products/symbols/DFIS/
- Secondary current price/NAV/distribution cross-check: https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=dfis
- Secondary historical closing-price cross-check: https://chartexchange.com/symbol/bats-dfis/historical/
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
