---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FENI
ticker: FENI
exchange: NYSE Arca
fund: Fidelity Enhanced International ETF
tracked_index: MSCI EAFE Index; enhanced active implementation
benchmark: MSCI EAFE Index (Net MA)
management_mode: active-equity-long-only
active_process: systematic-quantitative
active_process_subtype: quantitative enhanced-index selection against developed ex-U.S. large-/mid-cap equities
management_benchmark: MSCI EAFE Index (Net MA)
track_record: established-with-predecessor-history
management_evidence: positive-return-only
risk_evidence: issuer-fields; daily-NAV drawdown not verified
updated: 2026-08-30
performance_as_of: 2025-12-31 (official annual) / 2026-06-30 (official rolling)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31 (secondary)
price_nav_as_of: not used; current price/NAV pair not required for this performance check
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FENI
  - geography/International
---

# FENI Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

FENI เป็น active long-only ETF ของ Fidelity ที่ใช้ computer-aided quantitative
analysis เพื่อเพิ่มโอกาสให้ผลตอบแทนสูงกว่า MSCI EAFE โดยยังคง universe ของหุ้น
ต่างประเทศเป็นหลัก. Official predecessor-linked NAV Total Return ช่วง 2016-2025
สะสม `135.99%` หรือ rounded-input CAGR `8.97%`; มีปีบวก/ลบ `8 / 2` และผลตอบแทน
สูงกว่า management benchmark ใน `6/10` ปี. Official rolling 10-year NAV TR
คือ `10.53%` ณ 2026-06-30; current YTD ที่ตรวจได้คือ `13.07%*` ณ 2026-07-31
จาก secondary standardized capture.

## Performance check

- `entity_key: NYSE Arca:FENI`; fund `Fidelity Enhanced International ETF`; ETF listing `2023-11-20`; predecessor fund history is used for periods through 2023-11-17; the predecessor fund inception is `2007-12-20`.
- Exchange `NYSE Arca`; management style `actively managed`; official benchmark `MSCI EAFE Index (Net MA)`. Strategy normally invests at least 80% in common stocks included in the MSCI EAFE universe and uses computer-aided quantitative analysis.
- Expense ratios are `0.28%` gross and `0.28%` net as of 2026-06-30; portfolio assets were `US$10,288.9M`, holdings `395`, turnover `79%`, beta `0.98`, and 3-year standard deviation `13.27%` as of the same date.
- Metric: `NAV Total Return` includes changes in share price and reinvestment of dividends and capital gains and is net of expenses. Market-price returns are kept separate; the annual table below uses NAV returns.
- Management benchmark: `MSCI EAFE Index (Net MA)`, selected at hierarchy step 1 because Fidelity's official performance table names it as the fund benchmark and the strategy is explicitly designed to enhance that developed ex-U.S. universe.
- 10-year calendar window: `2015-12-31` to `2025-12-31`; rounded-input NAV TR CAGR `8.97%`; official issuer rolling 10-year NAV TR `10.53%` as of 2026-06-30. Formula for the calendar calculation: `(End TR / Start TR)^(1 / Years) - 1`.
- Coverage/source note: Fidelity's official factsheet marks the 2016-2025 annual rows as predecessor-linked through the 2023 ETF conversion; these are complete calendar-year returns, not an ETF inception-year partial.

| Year / window | FENI NAV TR | Management benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 1.89% | 1.21% | 11.96% |
| 2017 | 27.59% | 25.29% | 21.83% |
| 2018 | -14.72% | -13.60% | -4.38% |
| 2019 | 18.27% | 22.29% | 31.49% |
| 2020 | 7.66% | 8.02% | 18.40% |
| 2021 | 11.47% | 11.48% | 28.71% |
| 2022 | -13.98% | -14.27% | -18.11% |
| 2023 | 18.96% | 18.49% | 26.29% |
| 2024 | 6.78% | 4.07% | 25.02% |
| 2025 | 37.25% | 31.59% | 17.88% |
| 2016-2025 cumulative | 135.99% | 124.44% | 298.33% |
| 2016-2025 CAGR | 8.97% | 8.42% | 14.82% |
| 2021-2025 cumulative | 67.17% | 55.08% | 96.17% |
| 2021-2025 CAGR | 10.82% | 9.17% | 14.43% |

**Up years / Down years — complete 2016-2025 window**

- Up years / Down years: `8 / 2`.
- Best: 2017, `+27.59%`.
- Least positive: 2016, `+1.89%`.
- Worst: 2018, `-14.72%`.
- Least bad down year: 2022, `-13.98%`.
- Current YTD: `+13.07%*` as of 2026-07-31; same-date S&P 500 Total Return common reference `+10.14%`. The asterisk identifies a secondary current-period field; official latest month-end factsheet YTD was `+10.99%` as of 2026-06-30.

## Risk read-through

Official issuer risk fields as of 2026-06-30 show 3-year standard deviation
`13.27%` and beta `0.98`. The reviewed secondary standardized capture reports
the best 3-month return as `+19.5%` from 2020-10-31 to 2021-01-31 and the worst
as `-22.8%` from 2019-12-31 to 2020-03-31. Compatible official daily NAV
history sufficient to calculate maximum drawdown, recovery duration, downside
capture, or tracking error was not verified; risk evidence therefore remains
`issuer-fields; daily-NAV drawdown not verified`. Main risks are foreign country
and currency exposure, Japan concentration, active deviations from MSCI EAFE,
quantitative-model behavior, turnover and trading costs, and ETF
premium/discount/liquidity.

## Active management read-through

- `management_mode`: `active-equity-long-only`
- `active_process`: `systematic-quantitative`; Fidelity describes computer-aided quantitative analysis that selects stocks with potential to provide higher total return than the MSCI EAFE Index.
- `management_benchmark`: `MSCI EAFE Index (Net MA)`; selected at the official strategy-aligned comparator step. S&P 500 TR remains a common cross-ETF reference and is not management-skill evidence.
- `track_record`: `established-with-predecessor-history`; the ETF listed in 2023 while the predecessor history extends to 2007.
- `management_evidence`: `positive-return-only`; official annual return differences are `+0.68, +2.30, -1.12, -4.02, -0.36, -0.01, +0.29, +0.47, +2.71, +5.66 pp` for 2016-2025. The rounded-input 10-year Excess CAGR is `+0.55 pp`, 2021-2025 Excess CAGR is `+1.65 pp`, and the annual hit rate is `6/10`. These are benchmark-relative return observations, not alpha or proof of persistent skill.
- `risk_evidence`: `issuer-fields; daily-NAV drawdown not verified`; the issuer provides beta and standard deviation but not a compatible daily NAV series for full drawdown/recovery and risk-adjusted persistence analysis.

## Sources

- [Fidelity Enhanced International ETF factsheet](https://institutional.fidelity.com/app/proxy/content?literatureURL=/9911746.PDF) — official June 30, 2026 identity, benchmark, annual NAV/benchmark rows, rolling returns, expenses, holdings, turnover, beta, standard deviation, and predecessor conversion disclosure.
- [Fidelity ETF performance table](https://institutional.fidelity.com/advisors/investment-solutions/performance/fidelity-etfs?tab=performance) — official product performance access point; the reviewed table was used as a current-period cross-check.
- [FENI SEC supplement](https://www.sec.gov/Archives/edgar/data/945908/000094590826000149/filing12064.htm) and [FENI SEC prospectus](https://www.sec.gov/Archives/edgar/data/945908/000094590825000631/filing9951.htm) — official fund/ticker and active ETF structure sources.
- [Schwab FENI performance](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=feni) — secondary standardized NAV YTD `+13.1%` as of 2026-07-31; marked `*` and kept separate from official June 30 factsheet fields.
- [State Street SPY performance](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) — official same-date S&P 500 Index TR YTD `+10.14%` as of 2026-07-31 and `+10.21%` as of 2026-06-30.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for complete 2016-2025 calendar years.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
