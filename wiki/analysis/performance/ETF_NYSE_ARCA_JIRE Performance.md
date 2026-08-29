---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:JIRE
ticker: JIRE
exchange: NYSE Arca
fund: JPMorgan International Research Enhanced Equity ETF
tracked_index: not applicable (active strategy)
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: fundamental-active
active_process_subtype: research-enhanced benchmark-aware core international equity
management_benchmark: MSCI EAFE Index (net total return)
track_record: established-with-predecessor-history
management_evidence: mixed-return-only
risk_evidence: partial
updated: 2026-08-30
performance_as_of: 2026-07-31 (current YTD and calendar rows) / 2026-06-30 (annualized fields)
calendar_years_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: secondary market price 2026-08-26; official current NAV not readable
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and capital gains reinvested; fund expenses included; predecessor-linked through 2022-06-10
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/JIRE
  - geography/International
---

# JIRE ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

JIRE เป็น active long-only core international ETF ของ JPMorgan ที่ใช้
fundamental research และ disciplined portfolio construction เพื่อ overweight หุ้น
ที่เห็นว่ามี relative value ภายใน sector พร้อมพยายามคง sector/geographic risk ใกล้
กับ `MSCI EAFE Index (net total return)`. กองทุน ETF เริ่ม 10 มิ.ย. 2022 แต่ผลก่อน
วันนั้นเป็น predecessor mutual-fund/R6 history ที่ official factsheet ต่อเนื่องไว้
สำหรับการอ่าน track record ระยะยาว.

Official July 2026 factsheet รายงาน current NAV Total Return YTD `11.45%` เทียบกับ
index `11.59%` ณ 2026-07-31. Annualized NAV TR ณ 2026-06-30 อยู่ที่ `20.21%`
(1Y), `16.31%` (3Y), `9.85%` (5Y) และ `9.74%` (10Y) เทียบกับ benchmark
`20.23%`, `16.44%`, `9.05%` และ `9.66%`; return-only excess จึงเป็น `-0.02`,
`-0.13`, `+0.80` และ `+0.08 pp`. Evidence ของ active management จึงเป็น
`mixed-return-only` ไม่ใช่ข้อสรุปเรื่อง persistent skill หรือ alpha.

Official calendar rows 2016-2025 (predecessor-linked through 2022-06-10) ให้ NAV
compound `118.91%` และ rounded-input CAGR `8.15%`; 2021-2025 ให้ compound
`58.63%` และ CAGR `9.67%`. S&P 500 Total Return common reference ให้
`298.33%` / `14.82%` ใน 2016-2025 และ `96.17%` / `14.43%` ใน 2021-2025.

## Performance check

- `entity_key: NYSE Arca:JIRE`; fund: JPMorgan International Research Enhanced Equity ETF; inception: ETF `2022-06-10`, predecessor mutual fund `1992-10-28`; exchange `NYSE Arca`.
- Metric: `NAV Total Return` with dividends and capital gains reinvested and fund expenses included; currency USD. Market-price return is kept separate.
- Management mode: `active-equity-long-only`; active-process subtype: `fundamental-active`, research-enhanced and benchmark-aware core international equity.
- Management benchmark: `MSCI EAFE Index (net total return)`; selected from the official performance table and strategy disclosure because it is the stated developed-market comparator with similar risk characteristics.
- Official current YTD as of `2026-07-31`: NAV TR `+11.45%`; benchmark `+11.59%`; market-price TR `+11.46%`.
- Official annualized fields as of `2026-06-30`: 1Y `20.21%` vs `20.23%`; 3Y `16.31%` vs `16.44%`; 5Y `9.85%` vs `9.05%`; 10Y `9.74%` vs `9.66%`.
- Complete calendar window: official factsheet rows `2016-2025`, with predecessor-linked history before 2022-06-10. JIRE NAV compound `118.91%` / rounded-input CAGR `8.15%`; S&P 500 TR cache compound `298.33%` / CAGR `14.82%`.
- Common 2021-2025 window: JIRE NAV compound `58.63%` / rounded-input CAGR `9.67%`; S&P 500 TR cache compound `96.17%` / CAGR `14.43%`. This common reference is not the management benchmark and is not evidence of active skill.

| Calendar year | JIRE NAV TR | MSCI EAFE Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 2.07% | 1.00% | 11.96% |
| 2017 | 23.23% | 25.03% | 21.83% |
| 2018 | -14.66% | -13.79% | -4.38% |
| 2019 | 21.96% | 22.01% | 31.49% |
| 2020 | 5.41% | 7.82% | 18.40% |
| 2021 | 12.90% | 11.26% | 28.71% |
| 2022 | -13.68% | -14.45% | -18.11% |
| 2023 | 19.67% | 18.24% | 26.29% |
| 2024 | 2.96% | 3.82% | 25.02% |
| 2025 | 32.11% | 31.22% | 17.88% |

The JIRE and MSCI rows are official JPMorgan factsheet values. Rows through the
predecessor period are not adjusted to the ETF's lower expenses and could have
differed had the predecessor been structured as an ETF.

- Best JIRE year: 2025, **+32.11%**. Worst JIRE year: 2018, **-14.66%**. Up/down years: `8 / 2`.
- In the 2021-2025 official calendar subset, JIRE beat the management benchmark in `4 / 5` years; 2021-2025 cumulative relative wealth versus the benchmark is approximately `+3.46%` from rounded rows. This is return-only evidence with predecessor-linked limitations, not alpha.
- JIRE beat the S&P 500 common reference in 2022 and 2025, but this arithmetic comparison does not establish active-management value.

## Risk read-through

The July 2026 official factsheet reports 3-year Sharpe ratio `0.86`, beta `0.92`,
P/E `16.32x`, weighted average market cap `138.70` (issuer display; unit not
specified in the reviewed capture) and 207 holdings as of
2026-07-31. These provide partial risk evidence; official standard deviation,
tracking error, daily NAV maximum drawdown, and recovery duration were not verified
in the reviewed capture. Main risks are foreign securities, country/region and
currency exposure, sector/financials concentration, active-management and
valuation risk, plus ETF premium/discount and liquidity risk. The SEC prospectus
also allows futures for exposure/cash management and currency forwards for partial
hedging; these are incidental tools within an equity strategy, not a payoff-defining
leveraged or inverse structure.

## Active management read-through

- `management_mode`: `active-equity-long-only`
- `active_process`: `fundamental-active`; JPMorgan uses a global research platform, stock-specific valuation work, and disciplined portfolio construction intended to keep risk characteristics near MSCI EAFE.
- `management_benchmark`: `MSCI EAFE Index (net total return)`; official strategy-aligned comparator selected before reviewing the performance spread. The S&P 500 remains only the common cross-ETF reference.
- `track_record`: `established-with-predecessor-history`; ETF share class history is under five years, while the official record includes the predecessor mutual fund from 1992 and portfolio-manager continuity for the disclosed team from 2016/2020/2022.
- `management_evidence`: `mixed-return-only`; latest synchronized 1Y/3Y periods are slightly below the management benchmark, 5Y/10Y are above, and 2021-2025 calendar hit rate is 4/5. No persistent skill or alpha claim is made.
- `risk_evidence`: `partial`; official Sharpe and beta are available, but daily NAV drawdown/recovery and full risk-adjusted persistence evidence remain unverified.

## Sources

- [JPMorgan JIRE factsheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JIRE.PDF) — official July 31, 2026 NAV/market-price/calendar performance, benchmark, current YTD, expenses, predecessor note, holdings, beta, Sharpe, and portfolio characteristics.
- [JPMorgan JIRE summary prospectus, SEC](https://www.sec.gov/Archives/edgar/data/1485894/000119312526071675/d19543d497k.htm) — official active strategy, MSCI EAFE comparator, ETF/predecessor history, fees, derivatives role, manager continuity, and risks.
- [JPMorgan JIRE Fund Story](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fund-story/STO-JIRE.pdf) — official March 31, 2026 strategy context and an earlier 3-year active comparison, retained as context rather than replacing the newer factsheet.
- [Secondary JIRE quote](https://stockanalysis.com/etf/jire/) — market price `US$85.30` as of 2026-08-26 only; no secondary return series is used.
- S&P 500 Total Return cached convention from the workflow — USD dividends-reinvested common reference for 2016-2025 and 2021-2025.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
