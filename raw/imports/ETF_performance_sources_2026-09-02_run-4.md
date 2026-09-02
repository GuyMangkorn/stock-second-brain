---
type: source-batch
workflow: check-etf-performance
scope: research-queue
updated: 2026-09-02
execution_profile: scheduled-inline
window: available complete calendar years plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---

# ETF Performance Sources — 2026-09-02 Run 4

This dated batch records the source-backed evidence, calculations and
scheduled-local pre-save review for cards processed sequentially under one
retained `research-queue-manager` project lease. The S&P 500 reference uses the
cached USD dividend-reinvested convention for complete calendar years
`2016-2025`.

## WNRG evidence packet

- Input ticker: `SMWFF`; canonical identity: `Euronext Amsterdam:WNRG`; fund: State Street SPDR MSCI World Energy UCITS ETF; ISIN `IE00BYTRR863`. State Street lists Euronext Amsterdam `WNRG` as the primary listing, with EUR trading currency; the OTC `SMWFF` label is retained only as the input alias.
- Official classification: `passive-index` equity ETF. State Street says the fund tracks energy-sector companies across developed markets globally and tracks the `MSCI World Energy 35/20 Capped Index`; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified. The fund is replicated and accumulating.
- Official identity/facts as of `2026-09-01`: inception `2016-04-29`, TER `0.30%`, base/share-class currency USD, AUM `USD 574.72M`, official NAV `USD 78.07` as of `2026-08-31`, 52 holdings as of `2026-08-31`. State Street lists trading currencies EUR, GBP, MXN and USD.
- Official performance table as of `2026-07-31`: Fund Net NAV TR YTD `33.61%`, 1-year annualized `41.47%`, 3-year `16.10%`, 5-year `21.55%`, 10-year `9.57%`; 10-year cumulative NAV TR is `149.29%`. The retrieved table does not disclose raw endpoint levels, so no endpoint value is invented.
- Official complete calendar rows from the same State Street table: 2016 `26.33%`, 2017 `5.24%`, 2018 `-15.80%`, 2019 `11.37%`, 2020 `-31.10%`, 2021 `40.49%`, 2022 `46.31%`, 2023 `2.79%`, 2024 `2.88%`, 2025 `13.56%`. State Street says returns before May 2016 reflect the predecessor SSGA Energy Index Equity Fund I USD Shares; 2016 is marked `†` and excluded from complete-year ranking.
- Index continuity: the issuer states that linked returns use MSCI World Energy Index from fund inception through `2020-11-30` and MSCI World Energy 35/20 Capped Index from `2020-11-30` onward. The fund changed name before `2026-02-19`, but the share class/ISIN remains the same.
- Return basis: USD NAV Total Return, net of all fees, with income reinvested through the accumulating share class. EUR listing market price is not mixed into the NAV series.
- Cached common benchmark: S&P 500 Total Return in USD with dividends reinvested, as of `2025-12-31`; rows for 2016-2025 are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations from complete 2017-2025 fund rows: product `1.6783915361`, cumulative `67.8392%`, rounded-input CAGR `5.9172%`; complete 2021-2025 product `2.4684614390`, cumulative `146.8461%`, CAGR `19.8068%`; `7 / 2` up/down years; best `2022 +46.31%`; least positive `2023 +2.79%`; worst `2020 -31.10%`; least-bad down year `2018 -15.80%`.
- Calculations from the cached S&P rows: 2017-2025 product `2.5577809671`, cumulative `155.7781%`, rounded-input CAGR `15.1442%`; 2021-2025 product `1.9616961801`, cumulative `96.1696%`, CAGR `14.4264%`. WNRG’s arithmetic CAGR comparison is `-9.2270 pp` for 2017-2025 and `+5.3804 pp` for 2021-2025; these are reference comparisons, not alpha.
- Issuer risk fields as of `2026-07-31`: 3-year standard deviation `18.06%` and annualized tracking error `0.08%`. Sector allocation as of `2026-08-31`: Oil, Gas & Consumable Fuels `94.03%`; Energy Equipment & Services `5.97%`. Official daily NAV history sufficient for maximum drawdown and recovery was not verified.
- Source map: official product `https://www.ssga.com/ie/en_gb/institutional/etfs/state-street-spdr-msci-world-energy-ucits-etf-wnrg-na`; official factsheet `https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-wnrg-na.pdf`; S&P official index `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P source URLs are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official identity, primary exchange, OTC alias handling, passive equity eligibility, linked index history, fee/income structure, NAV TR basis, annual rows, rolling/current fields, and risk dates reconcile.
- Calculation review: PASS — complete-year subset, cumulative returns, CAGRs, benchmark comparisons, year counts and best/worst rankings were recomputed from the stated rows; the predecessor-linked 2016 context row was excluded from ranking.
- Format and graph review: PASS — Thai-first performance page, one annual table, required sections, canonical `geography/International` and `geography/global-developed` tags, and the breadcrumb to existing region/index targets are present.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_WNRG Performance.md`; create this source batch; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, and append one `log.md` workflow bullet.
- Planned graph/index changes: assign exactly one primary region, `International`, because the underlying exposure is global developed-market energy rather than the listing exchange; add one International navigation row, increment the region count from `65` to `66`, add the performance-index coverage bullet, and preserve the bidirectional breadcrumb.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## WNRG research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive global energy identity, canonical primary listing, current NAV/YTD, linked annual NAV total returns, calculations and scheduled-local review passed with predecessor-history and daily drawdown gaps disclosed.
```
