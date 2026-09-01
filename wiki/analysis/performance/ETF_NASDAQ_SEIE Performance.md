---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:SEIE
input_ticker: SEIE
ticker: SEIE
exchange: Nasdaq
fund: SEI Select International Equity ETF
tracked_index: not applicable; active strategy
benchmark: MSCI EAFE Index (Net) (USD)
management_mode: active-equity-long-only
active_process_subtype: integrated-multi-manager-quantitative
management_benchmark: MSCI EAFE Index (Net) (USD)
track_record: provisional
risk_evidence: not-verified
updated: 2026-09-01
performance_as_of: 2025-12-31 (calendar) / 2026-07-31 (fact sheet current)
current_ytd_as_of: 2026-07-31
market_price_as_of: 2026-08-27
nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-4.md
return_basis: NAV total return; distributions reinvested; net of fund expenses
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/SEIE
  - geography/International
  - geography/global-developed
  - style/active-equity
---

# SEIE Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

SEIE คือ SEI Select International Equity ETF บน Nasdaq เป็น active-equity-long-only
ETF ที่ลงทุนหลักในหุ้นต่างประเทศ โดยผสม proprietary quantitative portfolio ของ
SEI กับ model portfolios จาก fundamental sub-advisers. Official SEI factsheet
กำหนด `MSCI EAFE Index (Net) (USD)` เป็น benchmark ที่เหมาะกับ strategy.

ผลตอบแทนล่าสุดที่ยืนยันได้จาก issuer คือ NAV YTD `13.46%` เทียบ benchmark
`11.59%` ณ 31 ก.ค. 2026. ในปีปฏิทินเต็มปีแรก 2025 กองทุนทำได้ `38.96%` เทียบ
benchmark `31.89%`; since-inception annualized อยู่ที่ `24.66%` เทียบ `19.21%`
ณ 30 มิ.ย. 2026. หลักฐานยังเป็น `provisional` เพราะกองทุนเริ่มดำเนินงานในปี 2024
และมี complete calendar year เพียงหนึ่งปี.

## Performance check

- `entity_key: NASDAQ:SEIE`; `input_ticker: SEIE`; CUSIP `81589A700`; primary listing exchange: Nasdaq
- Official summary prospectus ระบุ commencement of operations `8 ต.ค. 2024`; SEI ETF page แสดง inception `10 ต.ค. 2024`. เก็บ discrepancy นี้ไว้และใช้ 8 ต.ค. เป็นวันที่จาก prospectus สำหรับ track-record assessment.
- Classification: `active-equity-long-only`; active process subtype: `integrated-multi-manager-quantitative`
- Strategy: ลงทุนอย่างน้อย 80% ใน equity securities, อย่างน้อย 40% นอกสหรัฐฯ, primarily developed markets แต่สามารถลงทุน emerging markets ได้
- Adviser/process: SEI Investments Management Corporation ผสาน quantitative factor model (Value, Momentum, Quality, Low Volatility) กับ sub-adviser model portfolios; latest factsheet allocation คือ SEI `70%`, Pzena `20%`, Brown Advisory `10%`
- Primary metric: USD NAV Total Return, reinvested dividends/capital gains, net of fund expenses; market-price return is kept separate
- Expense ratio: `0.50%`; latest summary prospectus portfolio turnover `70%` for the most recent fiscal year
- Management benchmark: `MSCI EAFE Index (Net) (USD)`; S&P 500 Total Return below is only a common USD reference, not evidence of manager skill

Official current and rolling fields have different as-of dates:

| Period | SEIE NAV TR | MSCI EAFE Net | As of |
|---|---:|---:|---|
| YTD | 13.46% | 11.59% | 2026-07-31 |
| 1 year | 23.57% | 20.23% | 2026-06-30 |
| Since inception annualized | 24.66% | 19.21% | 2026-06-30 |
| Since inception cumulative | 25.69% | 20.12% | 2026-07-31 |

The one-year and annualized fields are from the June 30 annualized column in the
July 2026 fact sheet; the YTD and cumulative fields are from its July 31
cumulative column. They are not merged into one single-date series.

## Calendar performance

The fund began in late 2024, so 2024 is a partial inception year and is excluded
from complete-year rankings. The July 31, 2026 summary prospectus provides the
first complete calendar-year observation. The S&P 500 row is the cached USD Total
Return convention and is not the fund's strategy-aligned benchmark.

| Year | SEIE NAV TR (USD) | MSCI EAFE Net (USD) | S&P 500 TR (USD reference) |
|---|---:|---:|---:|
| 2025 | 38.96% | 31.89% | 17.88% |

From the compatible official 2025 rows, return-only excess return versus the
management benchmark is `+7.07 pp` (`38.96% - 31.89%`). The official current
factsheet also shows a `+1.87 pp` YTD gap and a `+5.45 pp` since-inception
annualized gap, but these are date-specific observations and do not establish
persistent manager skill.

## Up years / Down years

- Complete calendar years available: `1`
- Up/down among complete years: `1 / 0`
- Best complete year: 2025, `+38.96%`
- Least positive complete year: 2025, `+38.96%`
- Worst down year: `ไม่พบข้อมูลที่ยืนยันได้` เพราะไม่มี complete down year
- 2024 is a partial inception year and is not ranked

## Active-management evidence

- `management_mode`: `active-equity-long-only`
- `active_process_subtype`: integrated quantitative + multi-manager model-portfolio approach
- `management_benchmark`: MSCI EAFE Index (Net) (USD)
- `track_record_maturity`: provisional; one complete calendar year and roughly two years of live history
- `management_evidence`: positive return-only observation: 2025 `+7.07 pp`, current YTD `+1.87 pp`, and since-inception annualized `+5.45 pp` versus the official strategy-aligned benchmark at their respective as-of dates
- `risk_evidence`: not-verified for full daily volatility, maximum drawdown, recovery duration, downside capture and risk-adjusted persistence; the issuer reports beta `0.94` but standard deviation is `N/A` in the reviewed factsheet

The 2025 outperformance is compatible with the disclosed factor/sub-adviser
process, but the sample is too short for a persistence conclusion. It is not
called alpha.

## Risk read-through

SEI's issuer page snapshot as of 27 ส.ค. 2026 reports NAV `$37.03`, closing price
`$37.18`, net assets approximately `$1.31bn`, `35,375,000` shares outstanding,
`357` holdings and 30-day SEC yield `2.12%`. The July factsheet reports portfolio
weighted capitalization `$78.7bn`, `346` holdings, price-to-book `1.90x`, median
forward P/E `14.02x`, and beta `0.94`; these date differences are preserved.

ความเสี่ยงหลักคือ foreign-market and currency exposure, developed/emerging-market
political and liquidity risk, factor rotation (value/momentum/quality/low
volatility), active manager and sub-adviser selection risk, quantitative model
and implementation risk, turnover/tax drag, market drawdown, and ETF
premium/discount or bid-ask spread. The fund may use participation notes and
depositary receipts, which add counterparty and replication risk, but the
strategy is still an active long-only equity ETF rather than a leveraged,
inverse, option-income, bond, commodity, currency, multi-asset or
derivative-defined payoff fund.

## Sources

- [SEI Select International Equity ETF official page](https://www.seic.com/financial-advisors/flexible-investment-solutions/etfs/select-etfs/sei-select-international-equity-etf-seie) — issuer strategy description
- [SEI SEIE official ETF page](https://seietfs.filepoint.live/seie) — official current NAV/price, AUM, holdings, benchmark and date-stamped performance fields
- [SEIE official fact sheet, July 31 2026](https://seietfs.filepoint.live/assets/pdfs/SEIE_FactSheet.pdf) — current YTD, rolling/since-inception returns, benchmark, process, allocations and portfolio characteristics
- [SEIE official summary prospectus, July 31 2026](https://seidocs.filepoint.live/assets/pdfs/Summary_Prospectuses/SEIE_Summary-Prospectus.pdf) — objective, fees, turnover, active strategy, risks, 2025 calendar return and manager list
- [SEC annual shareholder report, March 31 2026](https://www.sec.gov/Archives/edgar/data/1888997/000139834426010415/fp0099233-1_ncsrixbrl.htm) — Nasdaq identity, annual reporting period and active-management discussion
- [SEIE secondary price history](https://stockanalysis.com/etf/seie/history/) — latest market-price cross-check only; not used for NAV performance
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD Total Return reference
- [[ETF_performance_sources_2026-09-01_run-4]] | [[ETF Performance Index]]
