---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VBR
ticker: VBR
exchange: NYSE Arca
fund: Vanguard Small-Cap Value ETF
tracked_index: CRSP US Small Cap Value Index
benchmark: S&P 500 Total Return
updated: 2026-08-12
performance_as_of: 2026-06-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-06-18
source_batch: raw/imports/ETF_performance_sources_2026-08-12.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VBR
  - geography/United-States
---

# VBR Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VBR เป็น passive/index-tracking U.S. small-cap value equity ETF ที่ติดตาม CRSP US Small Cap Value Index. Official annual NAV Total Return 2016-2025 compound เป็น `162.85%` หรือ CAGR `10.15%` จาก rounded annual rows เทียบกับ S&P 500 TR `298.33%` หรือ CAGR `14.82%`. Rolling 10-year NAV TR annualized ของ issuer คือ `10.99%` ณ 2026-06-30 และ current NAV YTD คือ `15.83%` ณ วันเดียวกัน.

## Performance check

- entity_key: NYSE Arca:VBR
- Inception: 2004-01-26
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): CRSP US Small Cap Value Index (Bloomberg ticker `CRSPSCVT`)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 2016-2025 calendar NAV TR: cumulative `162.85%`; CAGR `10.15%` calculated from published rounded annual returns
- 2021-2025 calendar NAV TR: cumulative `65.22%`; CAGR `10.56%` calculated from published rounded annual returns
- Rolling 10-year NAV TR CAGR: `10.99%` (official Vanguard annualized return for the period ended 2026-06-30; raw rolling endpoints are not disclosed in the reviewed capture)
- Coverage/source note: Vanguard annual rows are official NAV Total Return, pre-tax, net of expenses, with dividends and capital-gains distributions reinvested, as of 2025-12-31. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | VBR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 24.80% | 11.96% |
| 2017 | 11.79% | 21.83% |
| 2018 | -12.22% | -4.38% |
| 2019 | 22.76% | 31.49% |
| 2020 | 5.82% | 18.40% |
| 2021 | 28.07% | 28.71% |
| 2022 | -9.29% | -18.11% |
| 2023 | 16.00% | 26.29% |
| 2024 | 12.39% | 25.02% |
| 2025 | 9.09% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2021, `28.07%`
- Least positive: 2020, `5.82%`
- Worst: 2018, `-12.22%`
- Least bad down year: 2022, `-9.29%`
- 2016-2025 CAGR: `10.15%`; 2021-2025 CAGR: `10.56%`
- Current YTD: NAV `15.83%`, market-price `15.92%`, and issuer benchmark `15.86%`, all for the period ended 2026-06-30
- Latest captured quote: market price `US$238.40`, NAV `US$238.46`, price/NAV discount `-0.03%` (calculated from `238.40 / 238.46 - 1`) as of 2026-06-18; quote inputs are from the [Vanguard VBR profile](https://investor.vanguard.com/investment-products/etfs/profile/vbr)

## Risk read-through

VBR เป็น small-cap value exposure ที่มี factor/cyclicality risk สูงกว่า broad U.S. large-cap benchmarks. Expense ratio คือ `0.05%` ณ 2026-06-30 และกองทุนใช้ passive full replication. NAV YTD ต่ำกว่า tracked-index YTD `15.86%` อยู่ `0.03 pp`; market-price YTD `15.92%` สูงกว่า NAV YTD เล็กน้อย แต่เป็นคนละ basis และไม่ถูกนำไปปนกับ annual NAV ranking.

Rolling 10-year NAV TR annualized `10.99%` ณ 2026-06-30 ต่างจาก 2016-2025 calendar CAGR `10.15%` เพราะเป็นคนละ endpoint/window. Max drawdown, recovery และ volatility ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` จาก reviewed official capture; no daily NAV history was supplied.

## Driver notes

- Confirmed structure: passive full-replication exposure to the CRSP US Small Cap Value Index.
- Benchmark continuity gap: the reviewed Vanguard factsheet names CRSP US Small Cap Value Index; any later benchmark-name change or effective date is not disclosed in this evidence packet, so no rebranding conclusion is made.
- Observed regime points: 2018 was the worst complete year at `-12.22%`; 2021 was the best at `+28.07%`. These are return observations, not causal event attribution.

## Sources

- [Vanguard VBR factsheet](https://institutional.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F0937.pdf) — fund facts and standardized performance; period ended 2026-06-30
- [Vanguard VBR performance page](https://investor.vanguard.com/investment-products/etfs/profile/vbr) — official calendar NAV Total Return rows and quote inputs; annual rows as of 2025-12-31, quote as of 2026-06-18
- [SEC shareholder report](https://www.sec.gov/Archives/edgar/data/36405/000110465926021502/R2.htm) and [SEC prospectus](https://www.sec.gov/Archives/edgar/data/36405/000168386323004080/f25242d1.htm) — fund structure and benchmark context
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-12]] | [[ETF Performance Index]]
