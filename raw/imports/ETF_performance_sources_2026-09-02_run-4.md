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
- Calculations from the cached S&P rows: 2017-2025 product `3.5577805598`, cumulative `255.7781%`, rounded-input CAGR `15.1442%`; 2021-2025 product `1.9616961801`, cumulative `96.1696%`, CAGR `14.4264%`. WNRG’s arithmetic CAGR comparison is `-9.2270 pp` for 2017-2025 and `+5.3804 pp` for 2021-2025; these are reference comparisons, not alpha.
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

## WHEA evidence packet

- Input ticker: `SWOOF`; canonical identity: `Euronext Amsterdam:WHEA`; fund: State Street SPDR MSCI World Health Care UCITS ETF; ISIN `IE00BYTRRB94`. State Street lists Euronext Amsterdam `WHEA` as the primary listing, with EUR trading currency; the OTC `SWOOF` label is retained only as the input alias.
- Official classification: `passive-index` equity ETF. State Street says the fund tracks health-care companies across developed markets globally and tracks the `MSCI World Health Care 35/20 Capped Index`; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified. The fund is replicated and accumulating.
- Official identity/facts as of `2026-09-01`: inception `2016-04-29`, TER `0.30%`, base/share-class currency USD, AUM `USD 707.92M`, official NAV `USD 72.38` as of `2026-08-31`, EUR closing price `EUR 62.31` and 113 holdings as of `2026-08-31`. The price is retained separately from the USD NAV return series.
- Official performance table as of `2026-07-31`: Fund Net NAV TR YTD `3.29%`, 1-year annualized `21.21%`, 3-year `6.75%`, 5-year `4.24%`, 10-year `8.10%`; 10-year cumulative NAV TR is `117.79%`. The retrieved table does not disclose raw endpoint levels, so no endpoint value is invented.
- Official complete calendar rows from the same State Street table: 2016 `-6.89%`, 2017 `19.69%`, 2018 `2.48%`, 2019 `23.34%`, 2020 `13.26%`, 2021 `19.59%`, 2022 `-5.56%`, 2023 `3.63%`, 2024 `1.02%`, 2025 `14.78%`. State Street says returns before May 2016 reflect the predecessor SSGA Health Care Index Equity Fund I USD Shares; 2016 is marked `†` and excluded from complete-year ranking.
- Index continuity: the issuer states that linked returns use MSCI World Health Care Index from fund inception through `2020-11-30` and MSCI World Health Care 35/20 Capped Index from `2020-11-30` onward. The fund changed name before `2026-02-19`, but the share class/ISIN remains the same.
- Return basis: USD NAV Total Return, net of all fees, with income reinvested through the accumulating share class. EUR listing market price is not mixed into the NAV series.
- Cached common benchmark: S&P 500 Total Return in USD with dividends reinvested, as of `2025-12-31`; rows for 2016-2025 are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations from complete 2017-2025 fund rows: product `2.3253450856`, cumulative `132.5345%`, rounded-input CAGR `9.8300%`; complete 2021-2025 product `1.3570939895`, cumulative `35.7094%`, CAGR `6.2972%`; `8 / 1` up/down years; best `2019 +23.34%`; least positive `2024 +1.02%`; worst `2022 -5.56%`.
- Calculations from the cached S&P rows: 2017-2025 product `3.5577805598`, cumulative `255.7781%`, rounded-input CAGR `15.1442%`; 2021-2025 product `1.9616961801`, cumulative `96.1696%`, CAGR `14.4264%`. WHEA’s arithmetic CAGR comparison is `-5.3143 pp` for 2017-2025 and `-8.1292 pp` for 2021-2025; these are reference comparisons, not alpha.
- Issuer risk fields as of `2026-07-31`: 3-year standard deviation `13.03%` and annualized tracking error `0.04%`. Industry allocation as of `2026-08-31`: Pharmaceuticals `46.76%`, Biotechnology `17.27%`, Health Care Equipment & Supplies `14.69%`, Health Care Providers & Services `12.92%`, Life Sciences Tools & Services `7.78%`, and Health Care Technology `0.57%`. Official daily NAV history sufficient for maximum drawdown and recovery was not verified.
- Source map: official product `https://www.ssga.com/nl/en_gb/institutional/etfs/state-street-spdr-msci-world-health-care-ucits-etf-whea-na`; official factsheet `https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-whea-na.pdf`; S&P official index `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P source URLs are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official identity, primary exchange, OTC alias handling, passive equity eligibility, linked index history, fee/income structure, NAV TR basis, annual rows, rolling/current fields, risk dates and separate EUR price/NAV currency reconcile.
- Calculation review: PASS — complete-year subset, cumulative returns, CAGRs, benchmark comparisons, year counts and best/worst rankings were recomputed from the stated rows; the predecessor-linked 2016 context row was excluded from ranking.
- Format and graph review: PASS — Thai-first performance page, one annual table, required sections, canonical `geography/International` and `geography/global-developed` tags, and the breadcrumb to existing region/index targets are present.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_WHEA Performance.md`; extend this source batch; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, and append one `log.md` workflow bullet.
- Planned graph/index changes: assign exactly one primary region, `International`, because the underlying exposure is global developed-market health care rather than the listing exchange; add one International navigation row, increment the region count from `66` to `67`, add the performance-index coverage bullet, and preserve the bidirectional breadcrumb.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## WHEA research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive global health-care identity, canonical primary listing, current NAV/YTD, linked annual NAV total returns, calculations and scheduled-local review passed with predecessor-history and daily drawdown gaps disclosed.
```

## IQDG evidence packet

- Input ticker: `IQDG`; canonical identity: `Cboe:IQDG`; fund: WisdomTree International Quality Dividend Growth Fund; CUSIP `97717X131`. WisdomTree and Cboe identify IQDG as the Cboe-listed fund; the fund's inception date is `2016-04-07`.
- Official classification: `passive-index` equity ETF. WisdomTree says IQDG seeks to track the WisdomTree International Quality Dividend Growth Index, which covers dividend-paying companies with growth characteristics in developed markets excluding Canada and the United States. The current product page states `Options Available: No`.
- Official identity/facts as of `2026-09-01`: net expense ratio `0.42%`, total assets `USD 715.013M`, official NAV `USD 44.273` as of `2026-09-01`; closing market price `USD 44.370` as of `2026-08-31`. WisdomTree also reports distribution yield `5.48%` and SEC 30-day yield `2.03%` as of `2026-08-31`; these yield fields are not substituted for total return.
- Official performance table as of `2026-07-31`: NAV Returns YTD `7.12%`, 1-year annualized `17.72%`, 3-year `10.21%`, 5-year `4.27%`, 10-year `7.95%`, since inception `8.14%`; cumulative since inception NAV return `124.22%`.
- Official calendar NAV-return rows from WisdomTree's presentation as of `2026-03-31`: 2017 `31.39%`, 2018 `-17.04%`, 2019 `29.91%`, 2020 `16.64%`, 2021 `12.38%`, 2022 `-20.15%`, 2023 `20.85%`, 2024 `-2.70%`, 2025 `23.46%`. The reviewed presentation does not show a 2016 annual return, so no 2016 value is backfilled.
- Issuer benchmark: `WisdomTree International Quality Dividend Growth Index`; the official index description says the index selects the top 300 companies from the WisdomTree International Equity Index using combined growth and quality ranks and weights them by annual cash dividends. The benchmark is retained as metadata; the common comparison below uses the cached S&P 500 TR convention.
- Return basis: USD NAV Total Return from WisdomTree's issuer NAV Returns field; IQDG is a distributing fund, and market-price returns are kept separate.
- Cached common benchmark: S&P 500 Total Return in USD with dividends reinvested, as of `2025-12-31`; rows for 2017-2025 are `21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations from complete 2017-2025 IQDG rows: product `2.1516462237`, cumulative `115.1646%`, rounded-input CAGR `8.8866%`; complete 2021-2025 product `1.3027159061`, cumulative `30.2716%`, CAGR `5.4314%`; `6 / 3` up/down years; best `2017 +31.39%`; least positive `2021 +12.38%`; worst `2022 -20.15%`; least-bad down year `2024 -2.70%`.
- Calculations from the cached S&P rows: 2017-2025 product `3.5577805598`, cumulative `255.7781%`, rounded-input CAGR `15.1442%`; 2021-2025 product `1.9616961801`, cumulative `96.1696%`, CAGR `14.4264%`. IQDG's arithmetic CAGR comparison is `-6.2576 pp` for 2017-2025 and `-8.9950 pp` for 2021-2025; these are reference comparisons, not alpha.
- Official portfolio context as of `2026-08-31`: country weights Japan `20.08%`, United Kingdom `15.34%`, France `13.50%`, Germany `9.78%`, Spain `7.36%`, Netherlands `7.24%`, Switzerland `6.40%`; sector weights Industrials `25.07%`, Consumer Discretionary `20.13%`, Financials `17.58%`, Information Technology `9.42%`, Health Care `8.87%`, Communication Services `5.27%`, Materials `4.76%`, Consumer Staples `4.06%`, Energy `3.79%`, Utilities `0.72%`, Real Estate `0.32%`. WisdomTree's presentation risk snapshot as of `2026-03-31` reports since-inception standard deviation `15.96%` and beta `1.01`; official daily NAV history sufficient for maximum drawdown and recovery was not verified.
- Source map: official product `https://www.wisdomtree.com/us/products/equity/iqdg`; official factsheet `https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/iqdg-factsheet.pdf?la=en`; official presentation `https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/presentations/equity/iqdg-presentation.pdf`; Cboe listing `https://www.cboe.com/us/equities/listings/listed_products/symbols/IQDG/`; S&P official index `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P source URLs are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official identity, Cboe listing, passive equity eligibility, index methodology, distributing treatment, NAV TR basis, separate market price, annual rows, rolling/current fields and as-of dates reconcile.
- Calculation review: PASS — complete-year subset, cumulative returns, CAGRs, benchmark comparisons, year counts and best/worst rankings were recomputed from the stated rows; the undisclosed 2016 row was not inferred.
- Format and graph review: PASS — Thai-first performance page, one annual table, required sections, canonical `geography/International` and `geography/developed-markets` tags, and breadcrumb to existing region/index targets are present.
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_CBOE_IQDG Performance.md`; extend this source batch; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, and append one `log.md` workflow bullet.
- Planned graph/index changes: assign exactly one primary region, `International`, because the underlying exposure is developed international equity outside the United States and Canada; add one International navigation row, increment the region count from `67` to `68`, add the performance-index coverage bullet, and preserve the bidirectional breadcrumb.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## IQDG research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive international equity identity, current NAV/YTD, official linked annual NAV total returns, calculations and scheduled-local review passed with undisclosed 2016 annual row and daily drawdown gaps disclosed.
```
