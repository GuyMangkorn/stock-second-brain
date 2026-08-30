---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:AVDV
ticker: AVDV
exchange: NYSE Arca
fund: Avantis International Small Cap Value ETF
tracked_index: not applicable (active strategy)
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: fundamental-active
management_benchmark: MSCI World ex USA Small Cap Index (Net Dividends)
track_record: established
management_evidence: positive return-only
risk_evidence: not-verified
updated: 2026-08-30
performance_as_of: 2026-06-30 (official rolling) / 2026-07-31 (current YTD)
calendar_years_as_of: 2025-12-31 (secondary complete years) / 2026-08-28 (secondary current proxy)
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; annual rows are secondary dividend-reinvested proxy
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/AVDV
  - geography/International
---

# AVDV ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

AVDV เป็น `active-equity-long-only` ETF ที่ใช้กระบวนการ `fundamental-active` ลงทุนในหุ้น small-cap value นอกสหรัฐฯ และใช้ `MSCI World ex USA Small Cap Index (Net Dividends)` เป็น management benchmark. Official issuer รายงาน current NAV total return YTD `13.11%` ณ 2026-07-31 และ NAV/market price `US$112.00`/`US$112.42` ณ 2026-08-28. Secondary dividend-reinvested proxy รายงาน YTD `+21.36%` ถึง 2026-08-28 แต่เก็บแยกจาก official NAV เพราะ as-of date และวิธีวัดต่างกัน. สำหรับ complete years 2020-2025 proxy ให้ cumulative `104.35%` และ rounded-input CAGR `12.65%`, มี 5 ปีบวก/1 ปีลบ; ดีที่สุด 2025 `+49.37%` และแย่ที่สุด 2022 `-11.46%`. Official 5Y NAV TR `13.81%` เทียบ benchmark `6.03%` คิดเป็น Excess CAGR `+7.78 pp` ซึ่งเป็น return-only evidence ไม่ใช่ alpha.

## Fund and measurement

- กองทุน: Avantis International Small Cap Value ETF; `entity_key: NYSE Arca:AVDV`; inception `2019-09-24`; exchange `NYSE Arca`.
- Expense ratio `0.36%` และ dividend frequency รายไตรมาส; latest official AUM `US$19.2B` ณ 2026-06-30.
- Primary metric: NAV total return. Issuer factsheet ณ 2026-06-30 reports `NAV 3Y 26.06%`, `5Y 13.81%`, `ITD 14.76%`; corresponding management benchmark `16.51%`, `6.03%`, `9.35%`.
- Current official YTD ณ 2026-07-31: NAV TR `+13.11%`; market-price TR `+12.97%`. ณ 2026-08-28 NAV `US$112.00` และ market price `US$112.42`; 1-day market-price change `-0.63%` และ 1-day NAV change `-0.95%`.
- Secondary dividend-reinvested proxy current YTD คือ `+21.36%` ถึง 2026-08-28; ไม่ merge กับ official `+13.11%` เพราะคนละ as-of date และ source methodology.
- 10-year NAV TR: `not applicable (<10-year history)`.

## Annual performance

Annual rows below are a secondary dividend-reinvested total-return proxy; `*` marks secondary data and `†` marks the 2019 partial fund year. They are not an issuer-published numeric NAV calendar table.

| Calendar year | AVDV total-return proxy | S&P 500 Total Return |
|---|---:|---:|
| 2019 | +12.05%*† | +31.49% |
| 2020 | +5.01%* | +18.40% |
| 2021 | +15.80%* | +28.71% |
| 2022 | -11.46%* | -18.11% |
| 2023 | +16.93%* | +26.29% |
| 2024 | +8.67%* | +25.02% |
| 2025 | +49.37%* | +17.88% |

- Complete 2020-2025 proxy: cumulative `+104.35%`, rounded-input CAGR `12.65%`, annual-return population standard deviation `18.35%`, up/down `5/1`.
- Complete 2021-2025 proxy: cumulative `+94.60%`, rounded-input CAGR `14.24%`; S&P 500 TR over the same cached window was `+96.17%` cumulative / `14.43%` CAGR. This common reference is not evidence of manager skill.
- Up years: 2020, 2021, 2023, 2024, 2025. Down year: 2022. Best `2025 +49.37%*`; worst `2022 -11.46%*`.

## Risk read-through

Risk evidence is `not-verified` for official daily NAV max drawdown, recovery date, and recovery duration. The refreshed single-ticker secondary proxy through 2026-08-28 shows observed maximum drawdown `-43.01%` from the 2020-01-02 peak to 2020-03-23 and current drawdown `-0.63%` from the 2026-08-27 peak; this is not an official daily NAV series, and it is not merged with the prior narrower multi-ticker proxy window. Main exposures are foreign small-cap, value, country/FX, liquidity, and active-process risk. The SEC summary prospectus reports latest fiscal-year portfolio turnover of `4%`.

## Active-management read-through

- `management_mode`: `active-equity-long-only`
- `active_process`: `fundamental-active`; managers use financial and market data to assess value, profitability, and size, and make buy/sell/hold decisions.
- `management_benchmark`: `MSCI World ex USA Small Cap Index (Net Dividends)`; selected because the official materials identify it as the strategy-aligned comparator.
- `track_record`: `established` (inception 2019-09-24; more than five years of history).
- `management_evidence`: `positive return-only`; official 5Y NAV TR exceeds the management benchmark by `+7.78 pp` annualized. Compatible net benchmark annual rows and complete-year hit rate were not verified, so this is not called alpha.
- `risk_evidence`: `not-verified`; no official daily NAV drawdown/recovery evidence was captured. The disclosed team has four members from fund inception and one member joining in 2021; no individual attribution is claimed.

## Sources

- [Avantis product page](https://www.avantisinvestors.com/avantis-investments/avantis-international-small-cap-value-etf/) — current YTD NAV/market-price TR, fee, NAV/price snapshot, active strategy.
- [Avantis AVDV factsheet](https://res.avantisinvestors.com/docs/avantis-international-small-cap-value-avdv-etf-fact-sheet.pdf) — official rolling returns, benchmark, inception, exchange, AUM, team, and risk disclosures as of 2026-06-30.
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1710607/000171060725000402/acetftavdv497k.htm) — NYSE Arca identity, fees, strategy, active-management disclosure, and turnover.
- [Secondary dividend-reinvested return series](https://totalrealreturns.com/n/AVDV) — calendar proxy, current secondary YTD, and observed drawdown window through 2026-08-28; not official NAV evidence.
- [Schwab performance cross-check](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=avdv) — current price and rolling NAV/market-price cross-check as of 2026-07-31.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
