---
type: etf-performance-source-batch
workflow: check-etf-performance
batch_date: 2026-09-01
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
pre_save_review: PASS
---

# ETF Performance Sources — 2026-09-01

## FNDF — Schwab Fundamental International Equity ETF

- `entity_key`: `NYSE Arca:FNDF`; card input `FNDF` is the verified listed ticker, not an OTC alias. Schwab identifies the fund as `Schwab Fundamental International Equity ETF`, listed on NYSE Arca, with inception `2013-08-15`.
- Official issuer source: https://www.schwabassetmanagement.com/products/fndf — objective is to track the total return of large non-U.S. developed-market companies weighted by fundamental size and weight; current index is `RAFI Fundamental High Liquidity Developed ex US Large Index (Net)`, management style `Passive`, expense ratio `0.250%`, NAV `US$55.66`, bid/ask midpoint `US$55.53`, premium/discount `-0.17%`, net assets `US$26,178,552,634.28`, and holdings `906` as of `2026-08-31`; portfolio turnover `12.46%`, beta `1.00`, and standard deviation `13.99%` as of `2026-07-31`; current official NAV TR YTD `20.44%` and issuer rolling 10-year NAV TR `11.73%` as of `2026-07-31`.
- Official SEC source: https://www.sec.gov/Archives/edgar/data/1454889/000088454626000305/c497k.htm — the fund normally invests at least 90% of net assets in index stocks or depositary receipts, does not hedge foreign-currency exposure, and may use forwards for securities awaiting settlement; all figures assume distributions were reinvested; annual NAV total returns as of 12/31 are `2016 7.70%`, `2017 23.81%`, `2018 -14.19%`, `2019 18.41%`, `2020 4.02%`, `2021 14.52%`, `2022 -7.77%`, `2023 20.34%`, `2024 2.6504872%`, and `2025 40.733244%`; official 10-year average annual NAV TR as of `2025-12-31` is `9.98%`.
- Benchmark history: Schwab product page states that effective `2024-06-21` the benchmark changed from `Russell RAFI Developed ex US Large Company Index (Net)` to `RAFI Fundamental High Liquidity Developed ex US Large Index (Net)`. The current tracked-index metadata is retained without backfilling a separate annual benchmark series.
- Return basis: official NAV total return in USD, reinvested distributions, net of fund expenses. Market price is not mixed into the annual ranking. The latest issuer TTM distribution yield is `3.01%` as of `2026-07-31`; no forward payout is inferred.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years `2016-2025`, USD, dividends reinvested, as of `2025-12-31`; rows are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Cached S&P 500 TR source URLs: https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true ; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf ; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ ; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ ; index definition: https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- Calculations from official annual rows and cached S&P rows: FNDF product `2.5878305`, cumulative `158.78%`, normalized endpoints `100.00 → 258.78`, rounded-input 10-year calendar CAGR `9.97%`; official SEC 10-year average annual NAV TR is `9.98%`; 2021-2025 product `1.8362054`, cumulative `83.62%`, CAGR `12.92%`; S&P 500 2016-2025 cumulative `298.33%`, CAGR `14.82%`; S&P 500 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Calendar ranking: `8` positive and `2` negative complete years; best `2025 +40.73%`; least positive `2024 +2.65%`; worst `2018 -14.19%`; least-bad down year `2022 -7.77%`. No partial year is ranked.
- Primary region: `International`, because the underlying exposure is developed markets outside the U.S. and is not a single country or sub-region. Planned breadcrumb is `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; canonical tag is `geography/International`. The International navigation contains `65` unique performance links after the NUDM addition.
- Evidence gap: official daily NAV observations sufficient to calculate maximum drawdown, recovery duration, downside capture, or compatible risk-adjusted evidence were not verified; no market-price proxy is substituted.
- Planned durable paths: `wiki/analysis/performance/ETF_NYSE_ARCA_FNDF Performance.md` (create); `raw/imports/ETF_performance_sources_2026-09-01.md` (create); `wiki/analysis/comparisons/International ETF.md` (update); `wiki/analysis/comparisons/ETF Region Index.md` (update); `wiki/analysis/performance/ETF Performance Index.md` (update). `log.md` receives one workflow bullet but is not part of the scoped commit because it contains pre-existing unrelated working-tree changes.
- Scheduled-inline pre-save checklist: PASS — canonical ticker/exchange and fund identity, passive equity eligibility, NAV TR definition, official annual rows, cached benchmark basis/window, as-of dates, benchmark change, calculations, source links, one-region assignment, breadcrumb, canonical tag, and unresolved daily-NAV risk gap reconciled. `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`.

### research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official FNDF performance evidence passed scheduled-local review and durable outputs were prepared for the scoped commit.

## FNDF correction notice

This 2026-09-01 batch is retained as a historical source capture. Its FNDF
snapshot and rounded-row presentation are superseded for current performance
use by [[ETF_performance_sources_2026-09-02_recheck]], which records the
2026-08-31 snapshot, official SEC 10-year `9.98%` field, cached S&P source URLs,
and the rounded-row `9.97%` calculation separately. The canonical FNDF page now
points to the recheck.
