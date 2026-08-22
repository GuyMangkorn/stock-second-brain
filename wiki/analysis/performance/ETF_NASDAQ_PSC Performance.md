---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:PSC
ticker: PSC
exchange: Nasdaq
fund: Principal U.S. Small-Cap ETF
tracked_index: Russell 2000 (management comparison; active, not index-tracking)
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: rules-based-multi-factor
management_benchmark: Russell 2000
track_record: established-with-strategy-change
management_evidence: mixed-benchmark-relative
risk_evidence: issuer-fields
updated: 2026-08-17
performance_as_of: 2026-07-31
calendar_years_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return; official 2017-2025 rows; strategy changed 2022-07-08
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/PSC
  - geography/United-States
---

# PSC Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

PSC คือ Principal U.S. Small-Cap ETF ที่ใช้ active rules-based quality, momentum
และ value process กับหุ้น U.S. small-cap โดยใช้ Russell 2000 เป็น
management benchmark. Official NAV Total Return rows ปี 2017-2025 ให้
cumulative 133.00% และ rounded-input CAGR 9.85%; common 2021-2025 CAGR
อยู่ที่ 10.91%. Current official NAV TR YTD อยู่ที่ 18.52% ณ 2026-07-31
เทียบ Russell 2000 18.85%.

Principal ระบุว่ากลยุทธ์ก่อน 2022-07-08 แตกต่างจากกลยุทธ์ปัจจุบัน ดังนั้น
2017-2025 เป็น combined history และไม่ควรตีความเป็น pure live track record
ของ current active process.

## Performance check

- entity_key: NASDAQ:PSC
- Inception: 2016-09-21; Nasdaq listing ตาม official reference sheet
- Objective: long-term growth of capital; normally at least 80% in U.S. small-cap equity
- Expense ratio: 0.38% gross and net
- Metric: official NAV Total Return รวมการ reinvest distributions และ fund expenses; USD; market-price return แยกจาก NAV
- Management mode: active-equity-long-only
- Active process: rules-based-multi-factor; quality, momentum และ value พร้อมการหลีกเลี่ยง fundamentally distressed small caps
- Management benchmark: Russell 2000; S&P 500 Total Return เป็น common reference เท่านั้น
- Track-record maturity: established-with-strategy-change; strategy เปลี่ยนจาก passive เป็น active effective 2022-07-08
- Official current performance as of 2026-07-31: NAV YTD 18.52%, 1-year 29.43%, 3-year annualized 16.19%, 5-year annualized 9.54%, since-inception annualized 12.01%
- Russell 2000 comparison as of 2026-07-31: YTD 18.85%, 1-year 34.18%, 3-year annualized 15.08%, 5-year annualized 7.11%
- Complete 2017-2025 NAV TR: cumulative 133.00% / rounded-input CAGR 9.85%; 2021-2025 cumulative 67.84% / CAGR 10.91%
- Russell 2000 comparison from official annual rows: 2017-2025 cumulative 106.48% / CAGR 8.39%; 2021-2025 cumulative 34.41% / CAGR 6.09%
- S&P 500 reference: 2017-2025 cumulative 255.78% / CAGR 15.14%; 2021-2025 cumulative 96.17% / CAGR 14.43%

| Year | PSC NAV TR | Russell 2000 TR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 13.41% | 14.65% | 21.83% |
| 2018 | -9.23% | -11.01% | -4.38% |
| 2019 | 18.87% | 25.52% | 31.49% |
| 2020 | 13.45% | 19.96% | 18.40% |
| 2021 | 32.32% | 14.82% | 28.71% |
| 2022 | -15.99% | -20.44% | -18.11% |
| 2023 | 18.53% | 16.93% | 26.29% |
| 2024 | 12.34% | 11.54% | 25.02% |
| 2025 | 13.39% | 12.81% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ management benchmark ของ PSC;
annual S&P rows reuse the cached USD Total Return convention as of 2025-12-31.

## Up years / Down years

- Up years / Down years: 7 / 2 in the complete 2017-2025 NAV window
- Best: 2021, +32.32%
- Least positive: 2017, +13.41%
- Worst: 2022, -15.99%
- 2017-2025 rounded-input CAGR: 9.85%; 2021-2025: 10.91%
- Current official NAV TR YTD: +18.52% as of 2026-07-31

## Risk read-through

PSC มี small-cap, factor, value, momentum, quality, market-trading และ liquidity
risks. Official product page ณ 2026-08-14 รายงาน NAV US$70.73, market price
US$70.76, premium 0.04%, median bid/ask spread 0.17%, total assets
US$2.4B, shares 34,840,001 และ SEC yield 0.56% ณ 2026-07-31. Official
daily NAV history สำหรับคำนวณ maximum drawdown และ recovery ยังไม่พบข้อมูลที่
ยืนยันได้.

## Active management read-through

management_mode: active-equity-long-only  
active_process: rules-based-multi-factor  
management_benchmark: Russell 2000  
track_record: established-with-strategy-change  
management_evidence: mixed-benchmark-relative  
risk_evidence: issuer-fields

- Complete 2017-2025 annual active hit rate: 6 / 9; annual PSC minus Russell 2000 differences were -1.24, +1.78, -6.65, -6.51, +17.50, +4.45, +1.60, +0.80, and +0.58 percentage points.
- Cumulative relative wealth versus Russell 2000 was +24.91%; rounded-input Excess CAGR was +1.47 pp.
- These are benchmark-relative return observations, not alpha. The combined window includes the pre-2022-07-08 strategy, so current-process attribution remains provisional.
- Official Q2 2026 commentary reported PSC NAV return 22.52% for the quarter versus Russell 2000 21.49% as of 2026-06-30; this is a separate dated cross-check from the latest 2026-07-31 product-page snapshot.

## Sources

- [Principal PSC product page](https://www.principalam.com/us/fund/psc) — official identity, benchmark, active factor process, current NAV/price/fund facts and performance table as of 2026-07-31/2026-08-14.
- [Principal U.S. Small-Cap ETF Quarterly Commentary](https://brandassets.principal.com/m/2b8aa0c162042812/original/Principal-U-S-Small-Cap-ETF-Quarterly-Commentary.pdf) — official Q2 2026 performance, calendar-year NAV rows, benchmark rows and strategy-change caveat.
- [Principal ETF Reference Sheet](https://brandassets.principal.com/m/157c05db44e9d2ec/original/Principal-ETF-Reference-Sheet.pdf) — official inception, exchange, benchmark and expense cross-check.
- [SEC annual shareholder report](https://www.sec.gov/Archives/edgar/data/1572661/000139834425017144/fp0095168-1_ncsrixbrl.htm) — official fund objective, 80% small-cap policy and expense disclosure.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition and cached annual USD Total Return convention.
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
