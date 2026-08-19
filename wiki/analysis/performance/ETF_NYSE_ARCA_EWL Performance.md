---
type: etf-performance
instrument_type: ETF
entity_key: NYSE_ARCA:EWL
input_ticker: EWL
ticker: EWL
exchange: NYSE Arca
fund: iShares MSCI Switzerland ETF
tracked_index: MSCI Switzerland 25/50 Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-19
performance_as_of: 2025-12-31
available_period_as_of: 2026-08-17
current_ytd_as_of: 2026-08-17
price_nav_as_of: 2026-08-18
fund_facts_as_of: 2026-08-18
risk_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; USD; net of expenses; distributions reinvested
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWL
  - geography/Switzerland
---

# EWL Performance

> Navigation: [[ETF Region Index]] → [[Switzerland ETF]] → [[ETF Performance Index]]

## Bottom line

EWL คือ iShares MSCI Switzerland ETF ที่จดทะเบียนบน NYSE Arca และติดตาม
`MSCI Switzerland 25/50 Index (Net)` แบบ passive. Official NAV Total Return ใน
complete calendar window 2016-2025 ให้ cumulative `136.56%` และ rounded-input
CAGR `8.99%`; เทียบ S&P 500 TR ที่ `298.33%` / `14.82%` ในช่วงเดียวกัน. ใน
common window 2021-2025 EWL ให้ `47.10%` / `8.02%` เทียบ S&P ที่ `96.17%` /
`14.43%`. Issuer rolling 10-year NAV TR คือ `10.04%` ณ 30 มิ.ย. 2026 และ
current official NAV TR YTD คือ `+7.02%` ณ 17 ส.ค. 2026.

## Performance check

- `entity_key: NYSE_ARCA:EWL`; fund inception `12 มี.ค. 1996`; asset class equities; distribution frequency semi-annual; CUSIP `464286749`.
- Classification: supported `passive-index` equity ETF. iShares states that EWL seeks to track an index of Swiss equities and the prospectus identifies the underlying index as the free-float-adjusted, capped `MSCI Switzerland 25/50 Index (Net)`.
- Metric: official `NAV Total Return` in USD with dividends and distributions reinvested; fund expenses are reflected in NAV return. Market-price returns remain separate.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not EWL's tracked index). Official benchmark rows are shown separately for 2021-2025.
- Official current fields: NAV `US$62.86` and fund net assets `US$2.389bn` as of `18 ส.ค. 2026`; 40 holdings as of `17 ส.ค. 2026`; expense ratio `0.50%`; current official NAV TR YTD `+7.02%` as of `17 ส.ค. 2026`.
- Official rolling fields as of `30 มิ.ย. 2026`: 1-year `16.53%`, 3-year annualised `12.91%`, 5-year annualised `7.39%`, 10-year annualised `10.04%`, and since-inception annualised `7.68%`.
- Calendar rows 2016-2024 come from the official summary prospectus calendar-year chart; 2025 comes from the official iShares factsheet/product page. The source split is preserved rather than inferred.

| Year | EWL NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -3.04% | 11.96% |
| 2017 | 23.37% | 21.83% |
| 2018 | -9.78% | -4.38% |
| 2019 | 32.27% | 31.49% |
| 2020 | 12.66% | 18.40% |
| 2021 | 19.27% | 28.71% |
| 2022 | -18.57% | -18.11% |
| 2023 | 17.37% | 26.29% |
| 2024 | -2.64% | 25.02% |
| 2025 | 32.54% | 17.88% |

**Up years / Down years**

- Up years / Down years: `6 / 4` ใน 2016-2025
- Best: 2025, `+32.54%`
- Least positive: 2020, `+12.66%`
- Worst: 2022, `-18.57%`
- Least bad down year: 2024, `-2.64%`
- 2016-2025 cumulative/CAGR: EWL `136.56%` / `8.99%`; S&P 500 TR `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: EWL `47.10%` / `8.02%`; S&P 500 TR `96.17%` / `14.43%`

### Official tracked-index comparison

| Year | EWL NAV TR | MSCI Switzerland 25/50 Index (Net) | Fund minus index |
|---|---:|---:|---:|
| 2021 | 19.27% | 19.86% | -0.59 pp |
| 2022 | -18.57% | -18.79% | +0.22 pp |
| 2023 | 17.37% | 17.32% | +0.05 pp |
| 2024 | -2.64% | -2.10% | -0.54 pp |
| 2025 | 32.54% | 32.89% | -0.35 pp |

The issuer's benchmark rows are available for 2021-2025 in the reviewed
factsheet/product capture. These fund-minus-index differences are passive
tracking observations, not alpha. The product page also shows benchmark YTD
`6.15%` as of `30 มิ.ย. 2026`, which is not mixed with EWL's newer `7.02%` YTD
as of `17 ส.ค. 2026`.

## Risk read-through

EWL เป็น single-country Switzerland exposure และมี sector concentration. Official
sector weights ณ `17 ส.ค. 2026` ได้แก่ Health Care `37.30%`, Financials `18.26%`,
Industrials `13.15%`, Consumer Staples `13.13%`, Materials `7.26%` และ Consumer
Discretionary `6.19%`. Factsheet ณ `30 มิ.ย. 2026` แสดง top holdings หลักคือ
Roche `12.84%`, Novartis `12.67%`, Nestlé `11.64%`, ABB `6.34%` และ Richemont
`5.04%`. Official 3-year standard deviation คือ `15.30%` ณ `31 ก.ค. 2026`.

Prospectus ระบุ systematic fair-value timing, foreign-market, non-diversification,
tracking-error และ valuation risks. NAV กับ market-price returns จึงอาจต่างกัน
เมื่อ Swiss markets ปิดไม่พร้อม NYSE Arca หรือเมื่อ fair-value methodology มีผล.
Daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยังไม่ถูกเปิดเผย
ใน reviewed official sources จึงรายงาน `risk-adjusted evidence: not-verified`
สำหรับ drawdown/recovery metric.

## Sources

- [iShares EWL product page](https://www.ishares.com/us/products/239685/ishares-msci-switzerland-etf) — official identity, NYSE Arca, benchmark, inception, current NAV/AUM, YTD, rolling returns, holdings, sectors, standard deviation and fees.
- [iShares EWL factsheet](https://www.ishares.com/us/literature/fact-sheet/ewl-ishares-msci-switzerland-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/benchmark rows, 2025 return, 10-year/rolling fields, fund description, top holdings, sectors and risk notes; as of 30 Jun 2026.
- [iShares EWL summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-switzerland-capped-etf-8-31.pdf) — official 2015-2024 calendar chart, index strategy, fees and principal risks; prospectus dated 30 Dec 2025.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow convention — USD Total Return with dividends reinvested; reference window 2016-2025 as of 31 Dec 2025.
- ETF source batch: [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
