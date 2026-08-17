---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:OSCV
ticker: OSCV
exchange: Cboe BZX
fund: Opus Small Cap Value ETF
tracked_index: not applicable (active strategy)
benchmark: S&P 500 Total Return
management_benchmark: S&P SmallCap 600 Value Total Return Index
updated: 2026-08-17
performance_as_of: 2025-12-31
calendar_years_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/OSCV
  - geography/United-States
---

# OSCV Performance
> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

OSCV เป็น active-equity-long-only U.S. small-cap value/dividend ETF. Official
NAV Total Return ใน complete calendar window 2019-2025 ให้ cumulative 88.61%
และ rounded-input CAGR 9.49%; common 2021-2025 CAGR อยู่ที่ 7.13% เทียบกับ
S&P 500 Total Return 14.43%. Current NAV TR YTD อยู่ที่ 15.53% ณ
2026-07-31; active comparison กับ S&P SmallCap 600 Value TR ให้ Excess CAGR
-0.58 percentage points หลังตัด 2018 ซึ่งเป็น inception-year partial.

## Performance check

- entity_key: Cboe BZX:OSCV
- Inception: 2018-07-17 ตาม issuer product page และ SEC prospectus; factsheet ระบุ 2018-07-18 และเก็บเป็น one-day source conflict
- Expense ratio: 0.79% ณ 2026-08-14
- Metric: NAV Total Return รวม distributions ที่ reinvested และ fund expenses ตาม issuer convention; USD
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Management mode: active-equity-long-only
- Active process: fundamental-active with factor-based overlay, quality/growth/value selection and sell discipline
- Management benchmark: S&P SmallCap 600 Value Total Return Index; selected as the official strategy-aligned comparator because the prospectus calls it a more applicable comparison; S&P 500 remains the common reference benchmark
- 10-year NAV TR CAGR: not applicable (<10-year fund history)
- Available complete calendar window: 2019-01-01 to 2025-12-31; cumulative 88.61%; rounded-input CAGR 9.49%
- Common 2021-2025 window: cumulative 41.10%; rounded-input CAGR 7.13%; S&P 500 TR CAGR 14.43%
- Since-inception annualized NAV TR: 8.34% as of 2026-07-31; this is a separate launch-to-date metric and includes the partial 2018 inception period
- Current NAV TR YTD: 15.53% as of 2026-07-31; 1-year 17.99%, 3-year annualized 10.20%, 5-year annualized 6.81%, and since-inception cumulative 90.35% on the same issuer page
- Current NAV / market price: US$43.25 / US$43.24 as of 2026-08-14
- Coverage/source note: official Aptus calendar rows cover 2018-2025; the 2018 inception-year partial is excluded from rankings and active evidence. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31.

| ปี | ETF NAV TR | Benchmark |
|---|---:|---:|
| 2018 | -12.66%† | -4.38% |
| 2019 | 27.45% | 31.49% |
| 2020 | 4.88% | 18.40% |
| 2021 | 27.89% | 28.71% |
| 2022 | -11.36% | -18.11% |
| 2023 | 10.13% | 26.29% |
| 2024 | 11.44% | 25.02% |
| 2025 | 1.42% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ management benchmark ของ OSCV.
Management benchmark rows และ annual active returns ถูกเก็บใน source batch;
การคำนวณใช้ complete comparable years 2019-2025 เท่านั้น.

## Up years / Down years

- Up years / Down years: 6 / 1 in the complete 2019-2025 window
- Best: 2021, +27.89%
- Least positive: 2025, +1.42%
- Worst: 2022, -11.36%
- Least bad down year: 2022, -11.36%
- Current OSCV NAV TR YTD: +15.53% as of 2026-07-31

## Risk read-through

Annual-return volatility แบบ population standard deviation อยู่ที่ 13.00%
จาก complete 2019-2025 rows. Factsheet ณ 2026-06-30 รายงาน 3-year standard
deviation ของ OSCV 18.67% เทียบกับ S&P 600 Value 24.00%; จึงจัด
risk_evidence: positive ในเชิง relative volatility แต่ยังไม่ใช่หลักฐานว่า
ผลตอบแทนมี risk-adjusted superiority. Official daily NAV history ที่เพียงพอ
สำหรับ max drawdown และ recovery ยังไม่พบข้อมูลที่ยืนยันได้. Expense ratio คือ
0.79%; กองมี small-cap, value-regime, sector, liquidity และ active-management
risk.

## Active management read-through

management_mode: active-equity-long-only
active_process: fundamental-active
management_benchmark: S&P SmallCap 600 Value Total Return Index
track_record: established
management_evidence: negative
risk_evidence: positive

- Excess CAGR: -0.58 percentage points over complete 2019-2025, จาก OSCV CAGR 9.49% เทียบกับ management benchmark CAGR 10.07%.
- Complete-year hit rate: 42.86% (3/7 years with positive active return); annual active returns were +2.95, +2.40, -2.96, -0.27, -4.75, +3.89, -5.29 percentage points from 2019 to 2025.
- Cumulative relative wealth: -3.62% versus the management benchmark over 2019-2025; OSCV cumulative return was 88.61% versus benchmark 95.70%.
- Risk evidence: official factsheet 3-year standard deviation was lower than S&P 600 Value (18.67% vs 24.00%); this remains separate from return evidence.
- Expense ratio: 0.79%. Portfolio turnover: 25% for the fiscal year ended 2025-04-30.
- Strategy/adviser continuity: Aptus Capital Advisors combines factor-based analysis with fundamental research across quality, growth and valuation. SEC materials identify John D. Gardner as portfolio manager since November 2019 and Brad Rapking and David Wagner III since August 2020; attribution is to the verified adviser/team process, not an unsupported individual-manager skill claim.

## Sources

- [Aptus OSCV product page](https://aptusetfs.com/oscv/) — official identity, exchange, current fund facts, NAV/market price, distributions and monthly/quarterly performance; reviewed 2026-08-17.
- [OSCV Fact Sheet](https://f.hubspotusercontent20.net/hubfs/4896827/Content%20Hub/Fact%20Sheets%20and%20Performance/ETF%20Fact%20Sheets/OSCV%20Fact%20Sheet.pdf) — official calendar-year NAV rows, rolling returns, benchmark rows and risk fields as of 2026-06-30.
- [SEC Summary Prospectus](https://www.sec.gov/Archives/edgar/data/1540305/000089418925006694/opussmallcapvalueetfsummary.htm) — official Cboe BZX listing, active strategy, portfolio turnover, benchmark selection and adviser/team disclosures.
- [OSCV Annual Shareholder Report](https://aptusetfs.com/wp-content/uploads/2025/06/OSCV-4.30.25-TSR-Final-Web-Ready-Public.pdf) — official turnover and performance cross-check as of 2025-04-30.
- [S&P SmallCap 600 Value](https://www.spglobal.com/spdji/en/indices/equity/sp-smallcap-600-value/) — official management-benchmark identity and value methodology.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition; cached annual USD Total Return convention as of 2025-12-31.
