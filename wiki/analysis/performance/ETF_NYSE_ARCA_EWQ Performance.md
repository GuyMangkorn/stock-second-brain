---
type: etf-performance
instrument_type: ETF
entity_key: NYSE_ARCA:EWQ
input_ticker: EWQ
ticker: EWQ
exchange: NYSE Arca
fund: iShares MSCI France ETF
tracked_index: MSCI France Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-17
price_nav_as_of: 2026-08-18
fund_facts_as_of: 2026-08-18
risk_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; USD; net of expenses; distributions reinvested
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWQ
  - geography/France
---

# EWQ Performance

> Navigation: [[ETF Region Index]] → [[France ETF]] → [[ETF Performance Index]]

## Bottom line

EWQ คือ iShares MSCI France ETF ที่จดทะเบียนบน NYSE Arca และติดตาม
`MSCI France Index (Net)` แบบ passive. Official NAV Total Return ใน complete
calendar window 2016-2025 ให้ cumulative `142.69%` และ rounded-input CAGR
`9.27%`; เทียบ S&P 500 TR ที่ `298.33%` / `14.82%` ในช่วงเดียวกัน. ใน common
window 2021-2025 EWQ ให้ cumulative `57.27%` / CAGR `9.48%` เทียบ S&P ที่
`96.17%` / `14.43%`. Issuer rolling 10-year NAV TR คือ `10.09%` ณ 30 มิ.ย.
2026 และ current official NAV TR YTD คือ `+7.03%` ณ 17 ส.ค. 2026.

## Performance check

- `entity_key: NYSE_ARCA:EWQ`; fund inception `12 มี.ค. 1996`; asset class equities; distribution frequency semi-annual; CUSIP `464286707`.
- Classification: supported `passive-index` equity ETF. iShares states that EWQ seeks to track French equities; the prospectus describes an indexing approach and representative sampling against `MSCI France Index`.
- Metric: official `NAV Total Return` in USD with dividends and distributions reinvested; fund expenses are reflected in NAV return. Market-price returns remain separate.
- Tracked index: `MSCI France Index (Net)`, designed to measure the large- and mid-capitalization segments of the French equity market.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not EWQ's tracked index). Official MSCI France rows are shown separately below.
- Official current fields: NAV `US$46.57` and fund net assets `US$335.28m` as of `18 ส.ค. 2026`; 55 holdings as of `17 ส.ค. 2026`; expense ratio `0.50%`; current official NAV TR YTD `+7.03%` as of `17 ส.ค. 2026`.
- Official rolling fields as of `30 มิ.ย. 2026`: 1-year `9.25%`, 3-year annualised `8.81%`, 5-year annualised `7.36%`, 10-year annualised `10.09%`, and since-inception annualised `7.07%`.
- Official tracked-index rolling fields for the same period: 1-year `10.45%`, 3-year annualised `9.48%`, 5-year annualised `7.52%`, and 10-year annualised `10.62%`.
- Calendar rows 2016-2024 come from the official summary prospectus calendar-year chart; 2025 comes from the official iShares factsheet. The source split is preserved rather than inferred.

| Year | EWQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 4.98% | 11.96% |
| 2017 | 28.84% | 21.83% |
| 2018 | -12.69% | -4.38% |
| 2019 | 25.78% | 31.49% |
| 2020 | 3.89% | 18.40% |
| 2021 | 21.12% | 28.71% |
| 2022 | -12.23% | -18.11% |
| 2023 | 21.69% | 26.29% |
| 2024 | -5.29% | 25.02% |
| 2025 | 28.36% | 17.88% |

**Up years / Down years**

- Up years / Down years: `7 / 3` ใน 2016-2025
- Best: 2017, `+28.84%`
- Least positive: 2020, `+3.89%`
- Worst: 2018, `-12.69%`
- Least bad down year: 2024, `-5.29%`
- 2016-2025 cumulative/CAGR: EWQ `142.69%` / `9.27%`; S&P 500 TR `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: EWQ `57.27%` / `9.48%`; S&P 500 TR `96.17%` / `14.43%`

### Official tracked-index comparison

| Year | EWQ NAV TR | MSCI France Index (Net) | Fund minus index |
|---|---:|---:|---:|
| 2021 | 21.12% | 20.59% | +0.53 pp |
| 2022 | -12.23% | -12.67% | +0.44 pp |
| 2023 | 21.69% | 22.28% | -0.59 pp |
| 2024 | -5.29% | -4.60% | -0.69 pp |
| 2025 | 28.36% | 29.50% | -1.14 pp |

The issuer's benchmark rows are available for 2021-2025 in the reviewed
factsheet/product capture. Rolling fund-minus-index differences are `-1.20 pp`
for 1-year, `-0.67 pp` for 3-year annualised, `-0.16 pp` for 5-year annualised
and `-0.53 pp` for 10-year annualised as of 30 มิ.ย. 2026. These are passive
tracking observations, not alpha.

## Risk read-through

EWQ เป็น single-country France exposure และมี sector concentration. Official
sector weights ณ `17 ส.ค. 2026` ได้แก่ Industrials `32.88%`, Financials `14.00%`,
Consumer Discretionary `10.87%`, Health Care `8.30%`, Consumer Staples `7.93%`,
Energy `7.90%`, Materials `6.93%`, Utilities `3.41%`, Information Technology
`3.20%`, Communication `2.77%`, Real Estate `1.33%` และ Cash/Derivatives `0.49%`.
Factsheet ณ `30 มิ.ย. 2026` แสดง top holdings หลักคือ Schneider Electric `8.31%`,
TotalEnergies `7.12%`, LVMH `6.40%`, Safran `6.33%`, Airbus `6.14%`, Air Liquide
`5.87%`, BNP Paribas `5.38%`, L'Oréal `4.90%`, Sanofi `4.35%` และ AXA `3.65%`;
รวม top ten `58.45%`. Official 3-year standard deviation คือ `14.45%` ณ
`31 ก.ค. 2026`.

Prospectus ระบุ country/foreign-market, non-diversification, sector/industry,
currency, tracking-error, systematic fair-value และ market-trading risks.
Representative sampling และการถือ cash/derivatives เพื่อบริหาร tracking อาจทำให้
NAV กับ market-price returns ต่างกัน โดยเฉพาะเมื่อ French markets ปิดไม่พร้อม
NYSE Arca. Daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยัง
ไม่ถูกเปิดเผยใน reviewed official sources จึงรายงาน `risk-adjusted evidence:
not-verified` สำหรับ drawdown/recovery metric.

## Sources

- [iShares EWQ product page](https://www.ishares.com/us/products/239648/ishares-msci-france-etf) — official identity, NYSE Arca, tracked index, inception, current NAV/AUM, YTD, rolling returns, holdings, sectors, standard deviation and fees.
- [iShares EWQ factsheet](https://www.ishares.com/us/literature/fact-sheet/ewq-ishares-msci-france-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/benchmark rows, 2025 return, rolling fields, fund description, top holdings, sectors and risk snapshot; as of 30 Jun 2026.
- [iShares EWQ summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-france-etf-8-31.pdf) — official 2015-2024 calendar chart, index strategy, fees and principal risks; prospectus dated 30 Dec 2025.
- [iShares EWQ annual shareholder report](https://www.ishares.com/us/literature/annual-report/ar-ewq-en.pdf) — official 2025 reporting-period context, fund/index return comparison and portfolio concentration context; period ended 31 Aug 2025.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow convention — USD Total Return with dividends reinvested; reference window 2016-2025 as of 31 Dec 2025.
- ETF source batch: [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
