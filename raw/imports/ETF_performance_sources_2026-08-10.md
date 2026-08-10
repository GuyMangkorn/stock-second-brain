---
type: etf-performance-source-batch
workflow: check-etf-performance
ticker: VB
entity_key: NYSE Arca:VB
collected: 2026-08-10
performance_as_of: 2026-08-07
benchmark_current_as_of: 2026-08-05
return_basis: NAV total return
currency: USD
---

# VB ETF Performance Sources — 2026-08-10

## Scope

- Research-bearing durable check-etf-performance invocation delegated by trello-etf-batch; mode: lean.
- Canonical identity: NYSE Arca:VB; current fund name Vanguard Morningstar Small-Cap ETF; legacy name Vanguard Small-Cap ETF.
- Primary region: USA; canonical tag: geography/United-States.
- Input list snapshot was used only for queue construction; displayed price/AUM/return/holdings/expense ratio were not evidence.

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| [Vanguard VB product page](https://investor.vanguard.com/investment-products/etfs/profile/vb) | official issuer product page | accessed 2026-08-10; annual table 2025-12-31; YTD 2026-08-07; historical-price table 2016-08-31 to 2026-07-31 | identity, annual NAV TR, current NAV/price, rolling return, price proxy |
| [Vanguard F0969 factsheet](https://fund-docs.vanguard.com/F0969.pdf) | official issuer factsheet | 2026-06-30 | NAV TR definition, passive/full replication, 36-month standard deviation, fund facts |
| [Vanguard AR969 annual report](https://fund-docs.vanguard.com/AR969.pdf) | official issuer shareholder report | 2025-12-31 | 2016-2025 return path and cumulative/CAGR cross-check |
| [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/36405/000003640526000206/f44854d1.htm) | regulator filing | 2026-04-28 | expense ratio, structure, strategy, lowest quarterly-return context |
| [Vanguard name-change list](https://advisors.vanguard.com/content/dam/fas/pdfs/MRSTR.pdf) | official issuer PDF | effective 2026-07-29 | current fund name and benchmark transition |
| [Vanguard benchmark transition notice](https://www.vanguardmexico.com/es/inicio/noticias/name-changes-for-vanguard-equity-index-funds-and-crsp-morningstar-benchmarks) | official issuer notice | effective 2026-07-29 | CRSP → Morningstar naming transition |
| [Morningstar US Small Cap Index](https://indexes.morningstar.com/indexes/details/morningstar-us-small-cap-FS00009VTW?currency=USD&tab=overview&variant=TR) | official index provider | accessed 2026-08-10 | benchmark identity only; methodology/performance data not used |
| [S&P DJI dashboard](https://www.spglobal.com/spdji/en/documents/performance-reports/dashboard-daily-global-markets.pdf) | official benchmark source | 2026-08-05 | current S&P 500 gross TR YTD 13.58% |
| [S&P methodology](https://www.spglobal.com/spdji/en/methodology/article/index-mathematics-methodology/) | official benchmark methodology | accessed 2026-08-10 | gross total-return/dividends-reinvested definition |
| Cached S&P 500 TR source set | official S&P DJI documents | reference as-of 2025-12-31 | annual 2016-2025 gross benchmark rows; no new search |
| Project check-etf-performance cache | local skill instructions | reference window 2016-2025 | cached annual S&P TR rows and URLs |

## Raw observations

- Exchange-qualified key: NYSE Arca:VB; fund Vanguard Morningstar Small-Cap ETF; legacy name retained in older sources.
- Inception 2004-01-26; passive/full replication; SEC target-index stock exposure threshold at least 80% of net assets plus investment borrowings.
- Expense ratio 0.03%; SEC breakdown management fee 0.02% plus other expenses 0.01%; prospectus date 2026-04-28; currency USD.
- NAV Total Return is pre-tax NAV performance including reinvested dividends and capital-gains distributions, net of fund expenses. Under-one-year periods are cumulative; longer periods average annual.
- Issuer benchmark current Morningstar US Small Cap Index; legacy CRSP US Small Cap Index in older factsheet/report; transition effective 2026-07-29. Management continuity is not claimed.
- Official trailing 10-year average annual NAV return 10.90% as of 2026-07-31; earlier factsheet snapshot 11.75% as of 2026-06-30 is a different month-end window.

### Official complete calendar-year NAV total return

| Year | VB NAV TR | S&P 500 TR cache |
|---|---:|---:|
| 2016 | 18.31% | 11.96% |
| 2017 | 16.24% | 21.83% |
| 2018 | -9.30% | -4.38% |
| 2019 | 27.37% | 31.49% |
| 2020 | 19.08% | 18.40% |
| 2021 | 17.72% | 28.71% |
| 2022 | -17.60% | -18.11% |
| 2023 | 18.21% | 26.29% |
| 2024 | 14.23% | 25.02% |
| 2025 | 8.83% | 17.88% |

- VB annual rows are official complete calendar-year NAV TR as of 2025-12-31; market-price rows remain separate.
- S&P 500 cache is USD gross index TR with dividends reinvested and no fund-expense deduction; reference as-of 2025-12-31; cumulative 298.33%; CAGR 14.82%.
- Cached URLs: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/).

## Current period and risk observations

- VB NAV TR YTD 19.48% as of 2026-08-07; market-price return 19.47%; official NAV price $306.05 and market price $306.09 on the same date; product-page source.
- S&P 500 TR YTD 13.58%, USD gross index return, as of 2026-08-05; exact same-day 2026-08-07 official observation not located.
- VB rolling 10-year average annual NAV TR 10.90% as of 2026-07-31; raw TR endpoints not disclosed.
- VB official 36-month monthly standard deviation 17.26% as of 2026-06-30.
- Quarter-end NAV-TR calculation from Vanguard official quarter-end observations: high-water index 1.58849 at 2019-12-31; trough index 1.11067 at 2020-03-31; 1.11067 / 1.58849 - 1 = -30.08%; index 1.89154 at 2020-12-31 confirms prior-peak recovery. This is not a daily maximum series.
- Monthly NAV-price-only proxy from Vanguard product-page historical-price table: peak $165.69 at 2018-08-31; trough $115.42 at 2020-03-31; recovery $181.97 at 2020-11-30; -30.34%. It excludes distributions and is not NAV TR.

## Calculations

- 2016-2025 VB cumulative 169.68%; CAGR (2.6968128)^(1/10.00) - 1 = 10.43%.
- 2021-2025 VB cumulative 42.55%; CAGR 7.35%.
- 2016-2025 S&P cache cumulative 298.33%; CAGR 14.82%.
- 2021-2025 S&P cache cumulative 96.17%; CAGR 14.43%.
- Positive/negative years 8 / 2; best 2019 +27.37%; least positive 2025 +8.83%; worst 2022 -17.60%; least bad down year 2018 -9.30%.
- Annual-return dispersion from rounded VB rows: population SD 13.25%; sample SD 13.97%; not used as headline risk metric.
- Official issuer trailing-monthly standard deviation 17.26% as of 2026-06-30.

## Gaps and conflicts

- No official current S&P 500 TR YTD field through 2026-08-07 was located; 13.58% through 2026-08-05 is latest official field; do not present as same-day.
- No daily distribution-reinvested NAV-TR max-drawdown series was disclosed; quarter-end high-water/trough calculation and separately labelled monthly price proxy are used.
- CRSP/Morningstar transition is disclosed; methodology-source as-of date is not disclosed, and Morningstar page was used for identity only.
- No latest cash-distribution schedule was needed; latest distribution as-of date is not disclosed. NAV TR definition includes reinvested distributions.
- Input Markdown snapshot was not evidence.
## Pre-save review

- Reviewer: project-scoped source_verifier; first review CHANGES_REQUIRED (High/Medium) on 2026-08-10; corrections applied; re-review PASS on 2026-08-10. Reviewer made no file changes.
