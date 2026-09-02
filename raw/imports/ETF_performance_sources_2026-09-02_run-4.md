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

## DWM evidence packet

- Input ticker: `DWM`; canonical identity: `NYSE Arca:DWM`; fund: WisdomTree International Equity Fund; CUSIP `97717W703`. WisdomTree and its factsheet identify DWM as the NYSE Arca-listed fund, with inception `2006-06-16`.
- Official classification: `passive-index` equity ETF. WisdomTree says DWM seeks to track the WisdomTree International Equity Index, covering dividend-paying companies in the developed world excluding the United States and Canada. The current product page states `Options Available: No`.
- Official identity/facts as of `2026-09-01`: net expense ratio `0.48%`, total assets `USD 689.254M`, official NAV `USD 76.161` as of `2026-09-01`; closing market price `USD 76.107` as of `2026-08-31`. WisdomTree also reports distribution yield `5.67%` and SEC 30-day yield `2.16%` as of `2026-09-01`; these yield fields are not substituted for total return.
- Official performance table as of `2026-07-31`: NAV Returns YTD `11.05%`, 1-year annualized `22.90%`, 3-year `17.20%`, 5-year `10.74%`, 10-year `8.74%`, since inception `5.78%`; cumulative since inception NAV return `210.08%`.
- Official calendar NAV-return rows from WisdomTree's presentation as of `2026-03-31`: 2016 `2.88%`, 2017 `23.46%`, 2018 `-13.54%`, 2019 `19.07%`, 2020 `-1.94%`, 2021 `10.44%`, 2022 `-9.11%`, 2023 `16.56%`, 2024 `4.56%`, 2025 `34.40%`.
- Issuer benchmark: `WisdomTree International Equity Index`; the official index description covers dividend-paying companies in the industrialized world excluding Canada and the United States. The benchmark is retained as metadata; the common comparison below uses the cached S&P 500 TR convention.
- Return basis: USD NAV Total Return from WisdomTree's issuer NAV Returns field; DWM is a distributing fund, and market-price returns are kept separate.
- Cached common benchmark: S&P 500 Total Return in USD with dividends reinvested, as of `2025-12-31`; rows for 2016-2025 are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations from complete 2016-2025 DWM rows: product `2.1082571670`, cumulative `110.8257%`, rounded-input CAGR `7.7438%`; complete 2021-2025 product `1.6442084788`, cumulative `64.4208%`, CAGR `10.4565%`; `7 / 3` up/down years; best `2025 +34.40%`; least positive `2024 +4.56%`; worst `2018 -13.54%`; least-bad down year `2020 -1.94%`.
- Calculations from the cached S&P rows: 2016-2025 product `3.9832911148`, cumulative `298.3291%`, rounded-input CAGR `14.8218%`; 2021-2025 product `1.9616961801`, cumulative `96.1696%`, CAGR `14.4264%`. DWM's arithmetic CAGR comparison is `-7.0779 pp` for 2016-2025 and `-3.9699 pp` for 2021-2025; these are reference comparisons, not alpha.
- Official portfolio context as of `2026-08-31`: country weights Japan `25.43%`, United Kingdom `13.26%`, France `8.75%`, Switzerland `7.78%`, Germany `6.47%`, Australia `6.32%`, Spain `6.32%`, Italy `5.50%`; sector weights Financials `22.82%`, Industrials `19.98%`, Consumer Discretionary `10.54%`, Information Technology `8.24%`, Health Care `8.16%`, Consumer Staples `7.37%`, Materials `5.71%`, Communication Services `5.42%`, Utilities `5.19%`, Energy `3.91%`, Real Estate `2.62%`, and Telecommunication Services `0.01%`. WisdomTree's presentation risk snapshot as of `2026-03-31` reports since-inception standard deviation `16.71%` and beta `0.98`; official daily NAV history sufficient for maximum drawdown and recovery was not verified.
- Source map: official product `https://www.wisdomtree.com/us/products/equity/dwm`; official factsheet `https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dwm-1059.pdf`; official presentation `https://www.wisdomtree.com/us/media/dwm-presentation`; issuer index `https://www.wisdomtree.com/us/indexes/wtdfa`; S&P official index `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P source URLs are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official identity, NYSE Arca listing, passive equity eligibility, index methodology, distributing treatment, NAV TR basis, separate market price, annual rows, rolling/current fields and as-of dates reconcile.
- Calculation review: PASS — complete-year subset, cumulative returns, CAGRs, benchmark comparisons, year counts and best/worst rankings were recomputed from the stated rows.
- Format and graph review: PASS — Thai-first refreshed performance page, one annual table, required sections, canonical `geography/International` and `geography/developed-markets` tags, and breadcrumb to existing region/index targets are present.
- Planned durable paths/change map: refresh `wiki/analysis/performance/ETF_AMEX_DWM Performance.md`; extend this source batch; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, and append one `log.md` workflow bullet.
- Planned graph/index changes: retain DWM in its existing primary region, `International`; refresh its navigation row and performance-index coverage without changing the region count, and preserve the bidirectional breadcrumb.
- Local pre-save verdict: PASS; `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; no critical or high finding remains.

## DWM research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive international equity identity, current NAV/YTD, official annual NAV total returns, calculations and scheduled-local review passed with country/sector and daily drawdown gaps disclosed.
```

## DTH evidence packet

- Input ticker: `DTH`; canonical identity: `NYSE Arca:DTH`; fund: WisdomTree International High Dividend Fund; CUSIP `97717W802`. WisdomTree identifies DTH as the NYSE Arca-listed fund with inception `2006-06-16`.
- Official classification: `passive-index` equity ETF. WisdomTree says DTH seeks to track the WisdomTree International High Dividend Index, covering dividend-paying companies outside the United States and Canada. The current product page states `Options Available: No`; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified.
- Official identity/facts as of `2026-09-01`: net expense ratio `0.58%`, official NAV `USD 58.397`, total assets `USD 662.804M`. The closing market price was `USD 58.510` as of `2026-08-31`. WisdomTree reports distribution yield `8.35%` and SEC 30-day yield `3.41%` as of `2026-08-31`; these yield fields are not substituted for total return. Portfolio characteristics as of `2026-08-31` were dividend yield `4.36%`, P/E `13.29` and P/B `1.61`.
- Official performance table as of `2026-07-31`: NAV Returns YTD `14.82%`, 1-year annualized `28.98%`, 3-year `19.73%`, 5-year `13.44%`, 10-year `9.26%`, since inception `5.49%`; cumulative since inception NAV return `192.89%`.
- Official calendar NAV-return rows from WisdomTree's presentation as of `2026-03-31`: 2016 `5.10%`, 2017 `20.33%`, 2018 `-12.57%`, 2019 `17.74%`, 2020 `-7.05%`, 2021 `8.62%`, 2022 `-2.12%`, 2023 `15.19%`, 2024 `2.03%`, 2025 `42.41%`.
- Issuer benchmark: `WisdomTree International High Dividend Index`; the product objective and factsheet identify it as the tracked high-dividend international equity index. The common comparison below uses the cached S&P 500 TR convention, not a claim of manager skill.
- Return basis: USD NAV Total Return from WisdomTree's issuer NAV Returns field; DTH is a distributing fund, and market-price return is kept separate.
- Cached common benchmark: S&P 500 Total Return in USD with dividends reinvested, as of `2025-12-31`; rows for 2016-2025 are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations from complete 2016-2025 DTH rows: product `2.1532648311`, cumulative `115.3265%`, rounded-input CAGR `7.9717%`; complete 2021-2025 product `1.7794545933`, cumulative `77.9455%`, CAGR `12.2167%`; `7 / 3` up/down years; best `2025 +42.41%`; least positive `2024 +2.03%`; worst `2018 -12.57%`; least-bad down year `2022 -2.12%`.
- Calculations from the cached S&P rows: 2016-2025 product `3.9832911148`, cumulative `298.3291%`, rounded-input CAGR `14.8218%`; 2021-2025 product `1.9616961801`, cumulative `96.1696%`, CAGR `14.4264%`. DTH's arithmetic CAGR comparison is `-6.8501 pp` for 2016-2025 and `-2.2098 pp` for 2021-2025; these are reference comparisons, not alpha.
- Official portfolio context as of `2026-08-31`: country weights United Kingdom `17.14%`, Japan `12.40%`, France `10.43%`, Spain `8.68%`, Italy `8.53%`, Australia `7.41%`, Hong Kong `5.61%`, Germany `5.29%`, Norway `5.14%` and Switzerland `4.54%`; sector weights Financials `27.15%`, Industrials `14.31%`, Utilities `11.03%`, Energy `9.24%`, Materials `8.14%`, Consumer Staples `7.64%`, Communication Services `6.94%`, Consumer Discretionary `5.45%`, Real Estate `4.85%`, Health Care `3.59%`, Information Technology `1.58%`, Telecom Services `0.06%` and ETF `0.01%`. WisdomTree's June presentation risk snapshot as of `2026-06-30` reports standard deviation `17.60%` and beta `1.01`; official daily NAV history sufficient for maximum drawdown and recovery was not verified.
- Source list: [WisdomTree DTH product page](https://www.wisdomtree.com/us/products/equity/dth) (official product/performance page; identity, current facts, portfolio fields and July 2026 returns); [WisdomTree DTH factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dth-1058.pdf) (official factsheet; identity/listing/distribution disclosure); [WisdomTree DTH presentation](https://www.wisdomtree.com/us/media/dth-presentation) (official presentation; 2016-2025 calendar returns and risk fields); [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) (benchmark definition); cached S&P source URLs and convention are defined in the `check-etf-performance` skill.
- Management benchmark selection reason: not applicable to `passive-index`; the issuer benchmark is retained as the strategy-aligned index, while S&P 500 TR is a common cross-fund reference in USD. Active calculations, management evidence and adviser/team attribution are not applicable.
- Track record: fund inception `2006-06-16`; `long-running-fund`; annual history is complete for 2016-2025 in the reviewed official presentation.
- Candidate chat output: `DTH` is a passive international high-dividend equity ETF. Official July 2026 NAV TR is `14.82%` YTD and `9.26%` annualized over 10 years; rounded-input 2016-2025 CAGR is `7.97%` versus cached S&P 500 TR `14.82%`, while 2021-2025 is `12.22%` versus `14.43%`. The fund is concentrated in financials and several non-U.S. markets; daily-NAV drawdown/recovery remains unverified.
- Planned durable file contents:
  - Performance page: the complete proposed Markdown is the full content of `wiki/analysis/performance/ETF_AMEX_DTH Performance.md` after this write: frontmatter for `NYSE Arca:DTH`, `USD NAV total return`, official as-of dates, bottom line with `9.26%` rolling 10-year NAV TR / `14.82%` YTD / `7.97%` 2016-2025 CAGR / `12.22%` 2021-2025 CAGR, the official 2016-2025 annual table, up/down-year statistics, current country/sector risk fields, the June 2026 standard-deviation/beta snapshot, the daily-NAV gap, and the five source links listed above.
  - Dated source batch: append this complete `## DTH evidence packet` and `## DTH research handoff` section to the existing run-4 Markdown; all prior run-4 sections remain unchanged.
  - Region/index pages: no region page or region-index count change; update the existing International navigation row and append the exact performance-index bullet specified below.
  - `log.md`: append the exact DTH bullet specified below under `## 2026-09-02`.
- Planned durable paths/change map: refresh `wiki/analysis/performance/ETF_AMEX_DTH Performance.md`; extend `raw/imports/ETF_performance_sources_2026-09-02_run-4.md`; update `wiki/analysis/comparisons/International ETF.md` and `wiki/analysis/performance/ETF Performance Index.md`; append one workflow bullet to `log.md`.
- Planned graph/index changes: retain exactly one primary region, `International`, because the underlying exposure is multi-country developed-market equity rather than the listing exchange; preserve `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`, keep `geography/International` and `geography/developed-markets`, refresh the existing DTH row, and do not change the International count.
- Local scheduled pre-save review: PASS. `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; identity/listing, passive eligibility, distribution treatment, NAV/price separation, July current fields, annual rows, calculation outputs, date/currency labels, concentration risk and unresolved daily-NAV drawdown/recovery gap reconcile. No critical or high finding remains.

## DTH research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive international high-dividend identity, current NAV/YTD, official annual NAV total returns, calculations and scheduled-local review passed with country/sector and daily drawdown gaps disclosed.
```

## PIZ evidence packet

- Input ticker: `PIZ`; canonical identity: `Nasdaq:PIZ`; fund: Invesco Dorsey Wright Developed Markets Momentum ETF; CUSIP `46138E875`. The current SEC Summary Prospectus identifies Nasdaq Stock Market LLC as the listing exchange and gives fund inception `2007-12-28`.
- Official classification: `passive-index` equity ETF. Invesco states that the fund generally invests at least `90%` of total assets in the underlying index and uses full replication. The index selects approximately 100 large-cap securities from developed markets excluding the United States using relative-strength characteristics; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified.
- Latest official fund facts from the Invesco Q4 2025 table: underlying holdings `100` as of `2025-12-31`, management fee and total annual fund operating expenses `0.80% / 0.80%` in the February 27, 2026 Summary Prospectus, portfolio turnover `122%` in the latest fiscal year, P/B `5.88`, P/E `24.40` and 30-day SEC yield `0.79%` in the Q4 2025 table. These characteristics are date-specific and are not mixed with a later current quote.
- Official performance table as of `2025-12-31`: ETF NAV average annual total return 1-year `36.34%`, 5-year `9.44%`, 10-year `9.04%`, since inception `5.47%`; market-price return `37.14%`, `9.54%`, `9.12%`, `5.45%`; underlying index return `37.85%`, `10.25%`, `9.81%`, `6.37%`; MSCI EAFE Net benchmark `31.22%`, `8.92%`, `8.18%`, `4.22%`.
- Official complete calendar NAV-return rows from Invesco's Q4 2025 table: 2016 `-7.99%`, 2017 `30.70%`, 2018 `-16.18%`, 2019 `27.33%`, 2020 `17.91%`, 2021 `20.78%`, 2022 `-30.47%`, 2023 `17.88%`, 2024 `16.31%`, 2025 `36.34%`.
- Issuer benchmark: `Dorsey Wright Developed Markets Tech Leaders Index` (the Q4 table also uses the `Technical Leaders` wording). The index return is net of applicable withholding taxes but excludes fund fees and expenses; it is retained as the strategy-aligned benchmark, while the common cross-fund comparison below uses cached S&P 500 TR.
- Return basis: USD ETF NAV Total Return as reported by Invesco; market-price return and underlying-index return are kept separate. Invesco notes that returns reflect applicable fee waivers, if any, and that market returns use the 4 p.m. bid/ask midpoint.
- Cached common benchmark: S&P 500 Total Return in USD with dividends reinvested, as of `2025-12-31`; rows for 2016-2025 are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations from complete 2016-2025 PIZ rows: product `2.3756769308`, cumulative `137.5677%`, rounded-input CAGR `9.0382%`; complete 2021-2025 product `1.5698122986`, cumulative `56.9812%`, CAGR `9.4384%`; `7 / 3` up/down years; best `2025 +36.34%`; least positive `2024 +16.31%`; worst `2022 -30.47%`; least-bad down year `2016 -7.99%`.
- Calculations from the cached S&P rows: 2016-2025 product `3.9832911148`, cumulative `298.3291%`, rounded-input CAGR `14.8218%`; 2021-2025 product `1.9616961801`, cumulative `96.1696%`, CAGR `14.4264%`. PIZ's arithmetic CAGR comparison is `-5.7835 pp` for 2016-2025 and `-4.9881 pp` for 2021-2025; these are reference comparisons, not alpha.
- Risk evidence: the February 27, 2026 prospectus says the fund was managed as diversified as of `2025-10-31`, had significant exposure to Industrials and Financials, and carries momentum, foreign-investment, geographic/industry concentration, currency, ADR/GDR, market-price/NAV and portfolio-turnover risks. Current country/sector weights, official standard deviation, beta and daily NAV history sufficient for maximum drawdown/recovery were not verified.
- Source list: [Invesco PIZ product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-dorsey-wright-developed-markets-momentum-etf.html) (official product page checked `2026-09-02`; current performance module did not expose fields in the reviewed capture); [SEC Summary Prospectus dated February 27, 2026](https://www.sec.gov/Archives/edgar/data/1378872/000119312526079042/d12489d497k.htm) (official primary filing; objective, index construction, fees, replication, turnover, risks and manager continuity); [Invesco Q4 2025 fund performance table](https://www.invesco.com/us-rest/contentdetail?contentId=bbd2fd05f0e21410VgnVCM100000c2f1bf0aRCRD) (official issuer table; performance and calendar rows as of `2025-12-31`); [Nasdaq Dorsey Wright reports](https://dorseywright.nasdaq.com/reports/quilt) (official index-provider context; not used as NAV total return); [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) (common benchmark definition); cached S&P source URLs and convention are defined in the `check-etf-performance` skill.
- Management benchmark selection reason: `passive-index`, so active management benchmark and active calculations are not applicable. The issuer index is the strategy-aligned benchmark; MSCI EAFE Net is the official broad developed-market comparator in the issuer table; cached S&P 500 TR is retained as the common USD reference for the requested cross-fund view.
- Track record: fund inception `2007-12-28`; `long-running-fund`; official annual history is complete for 2016-2025 in the reviewed Q4 2025 table.
- Adviser/team continuity and attribution caveat: Invesco Capital Management LLC is the adviser; the February 27, 2026 prospectus lists Peter Hubbard (since December 2007), Michael Jeanette and Tony Seisser (since February 2015), and Pratik Doshi, CFA (since February 2020). This is a passive index-tracking fund, so annual returns are not evidence of discretionary manager skill.
- Candidate chat output: `PIZ` is a passive developed-market ex-U.S. momentum equity ETF. Official NAV TR is `9.04%` annualized over 10 years as of `2025-12-31`; rounded-input 2016-2025 CAGR is `9.04%` versus cached S&P 500 TR `14.82%`, and 2021-2025 CAGR is `9.44%` versus `14.43%`. The reviewed official product page did not expose current 2026 NAV TR YTD or current NAV/price, so those fields remain an explicit gap; high turnover and momentum/sector/country concentration are the key risks.
- Planned durable file contents:
  - Performance page: complete proposed Markdown is the full content of `wiki/analysis/performance/ETF_NASDAQ_PIZ Performance.md`, reproduced below.

```markdown
---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:PIZ
input_ticker: PIZ
input_alias: PIZ
ticker: PIZ
exchange: Nasdaq
fund: Invesco Dorsey Wright Developed Markets Momentum ETF
tracked_index: Dorsey Wright Developed Markets Tech Leaders Index
benchmark: S&P 500 Total Return
issuer_benchmark: Dorsey Wright Developed Markets Tech Leaders Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: long-running-fund
management_evidence: not applicable
risk_evidence: prospectus-fields
updated: 2026-09-02
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: not disclosed
price_nav_as_of: not disclosed
fund_facts_as_of: 2026-02-27
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-4.md
return_basis: USD NAV total return; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/PIZ
  - geography/International
  - geography/developed-markets
---

# PIZ Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

PIZ เป็น passive developed-market ex-U.S. momentum equity ETF ที่ติดตาม Dorsey
Wright Developed Markets Tech Leaders Index และใช้ full replication. Official NAV
Total Return ล่าสุดที่อ่านได้ครบถ้วนจาก Invesco คือ `9.04%` annualized สำหรับ 10 ปี
ณ `2025-12-31`; current 2026 NAV TR YTD และ current NAV/market price ยัง
`ไม่พบข้อมูลที่ยืนยันได้` จาก official performance module ที่ตรวจครั้งนี้. ช่วง
complete 2016-2025 ให้ CAGR `9.04%` จาก cumulative `137.57%` เทียบ S&P 500 TR
`14.82%`; ช่วง 2021-2025 ให้ CAGR `9.44%` จาก cumulative `56.98%` เทียบ
`14.43%`.

## Performance check

- `entity_key`: `Nasdaq:PIZ`; input ticker: `PIZ`; listing: Nasdaq Stock Market LLC
- CUSIP: `46138E875`; fund inception `2007-12-28`
- Management fee / total annual fund operating expenses: `0.80% / 0.80%` ตาม Summary Prospectus วันที่ `2026-02-27`
- Fund generally invests at least `90%` of total assets in the underlying index and uses full replication; the index selects approximately 100 large-cap companies from developed markets excluding the United States based on relative strength
- Latest official fund facts as of `2025-12-31`: 100 underlying securities; portfolio turnover `122%` in the latest fiscal year; Invesco's official table reports 30-day SEC yield `0.79%`
- Metric: official `ETF - NAV` total return; market-price return and underlying-index return are kept separate. The annual NAV series includes the fund's applicable expenses and distribution effects as reported by Invesco.
- Issuer benchmark: `Dorsey Wright Developed Markets Tech Leaders Index`; the index return is net of applicable withholding taxes but excludes fund fees and expenses
- Official average annual NAV total return as of `2025-12-31`: 1-year `36.34%`, 5-year `9.44%`, 10-year `9.04%`, since inception `5.47%`
- Current 2026 official NAV TR YTD, current NAV and current market price: `not disclosed` in the reviewed official product-page performance capture; no secondary price series is substituted for NAV total return.
- Calendar rows are from Invesco's official Q4 2025 table dated `2025-12-31`; S&P 500 TR uses the cached USD dividend-reinvested convention for 2016-2025.

| Year | PIZ NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | -7.99% | 11.96% |
| 2017 | 30.70% | 21.83% |
| 2018 | -16.18% | -4.38% |
| 2019 | 27.33% | 31.49% |
| 2020 | 17.91% | 18.40% |
| 2021 | 20.78% | 28.71% |
| 2022 | -30.47% | -18.11% |
| 2023 | 17.88% | 26.29% |
| 2024 | 16.31% | 25.02% |
| 2025 | 36.34% | 17.88% |

## Up years / Down years

- Complete 2016-2025 window: `7 / 3` up/down years
- Best complete year: 2025, `+36.34%`
- Least positive: 2024, `+16.31%`
- Worst complete year: 2022, `-30.47%`
- Least-bad down year: 2016, `-7.99%`
- Complete 2016-2025 cumulative return / rounded-input CAGR: `137.57% / 9.04%`
- Complete 2021-2025 window: `4 / 1` up/down years; cumulative return / rounded-input CAGR: `56.98% / 9.44%`
- Current official NAV TR YTD: `ไม่พบข้อมูลที่ยืนยันได้`; no current S&P 500 comparison is asserted.

## Risk read-through

PIZ ใช้ momentum selection และมี turnover สูง: Invesco prospectus ระบุว่า index
คัดหุ้นจาก developed markets นอกสหรัฐฯ ด้วย relative-strength score, มีประมาณ
100 securities และ fund turnover ล่าสุด `122%`. Prospectus ณ `2025-10-31` ระบุว่า
กองทุนมี significant exposure ต่อกลุ่ม Industrials และ Financials; น้ำหนัก
country/sector ปัจจุบันแบบละเอียด รวมถึง official standard deviation, beta และ
daily NAV history สำหรับคำนวณ maximum drawdown/recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`
จากชุด official sources ที่ตรวจ. ความเสี่ยงหลักจึงรวม momentum reversal, industry และ
geographic concentration, foreign-currency/ADR-GDR, mid-cap และ market-price/NAV
divergence; อย่าใช้ผลตอบแทนปี 2025 ที่สูงเป็นหลักฐานว่ากลยุทธ์จะทำได้ซ้ำ.

## Sources

- [Invesco official PIZ product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-dorsey-wright-developed-markets-momentum-etf.html) — official product identity and current performance module checked on `2026-09-02`; the reviewed capture did not expose current performance fields
- [SEC Summary Prospectus dated February 27, 2026](https://www.sec.gov/Archives/edgar/data/1378872/000119312526079042/d12489d497k.htm) — objective, index construction, fees, replication, turnover, risks and management continuity
- [Invesco official Q4 2025 fund performance table](https://www.invesco.com/us-rest/contentdetail?contentId=bbd2fd05f0e21410VgnVCM100000c2f1bf0aRCRD) — NAV/market-price/index/benchmark returns and calendar rows as of `2025-12-31`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references and calculation convention: [[ETF_performance_sources_2026-09-02_run-4]]
```

  - Dated source batch: append this complete `## PIZ evidence packet` and `## PIZ research handoff` section to the existing run-4 Markdown; all prior run-4 sections remain unchanged.
  - International region page: update exactly the PIZ row `| PIZ | Invesco Dorsey Wright Developed Markets Momentum ETF | developed ex-U.S. momentum | 9.04% | 9.44% | ไม่พบข้อมูลที่ยืนยันได้ | [[ETF_NASDAQ_PIZ Performance]] |`.
  - Region index page: change exactly the International count from `68` to `69` and leave all other region counts unchanged.
  - Performance index page: append exactly `- [[ETF_NASDAQ_PIZ Performance]] — PIZ (International; passive developed ex-U.S. momentum equity exposure; official 2016-2025 complete NAV TR cumulative `+137.57%` / rounded-input CAGR `+9.04%`, 2021-2025 CAGR `+9.44%`, official latest rolling 10-year NAV TR `+9.04%` as of 2025-12-31; current 2026 NAV TR YTD/NAV/price not disclosed in the reviewed official capture, with high turnover, momentum, country/sector and daily-NAV gaps disclosed)` under `## 2026-09-02 Queue Coverage Addition`.
  - `log.md`: append the exact bullet below:

    ```text
    - `etf-performance`: Added [[ETF_NASDAQ_PIZ Performance]]; scheduled-inline local pre-save returned PASS, official 2016-2025 complete NAV TR cumulative is `137.57%` / rounded-input CAGR `9.04%`, 2021-2025 CAGR is `9.44%`, and the latest official 10-year NAV TR is `9.04%` as of `2025-12-31`; current 2026 NAV TR YTD/NAV/price remain undisclosed in the reviewed official capture, while high turnover, momentum, country/sector and daily-NAV gaps remain disclosed.
    ```
- Planned durable paths/change map: create `wiki/analysis/performance/ETF_NASDAQ_PIZ Performance.md`; extend `raw/imports/ETF_performance_sources_2026-09-02_run-4.md`; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`; append one workflow bullet to `log.md`.
- Planned graph/index changes: assign exactly one primary region, `International`, because the underlying exposure is developed-market ex-U.S. equity rather than the listing exchange; increment International from `68` to `69`; preserve `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`, add the canonical `geography/International` and `geography/developed-markets` tags, and verify the new wikilink resolves.
- Local scheduled pre-save review: PASS. `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`; identity/listing, passive eligibility, index construction, fee/return labels, annual rows, calculations, benchmark basis, date/currency labels and explicitly undisclosed current fields reconcile. No critical or high finding remains.

## PIZ research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive developed-market momentum identity, Nasdaq listing, official annual NAV total returns, calculations and scheduled-local review passed with current-field, high-turnover, concentration and daily drawdown gaps disclosed.
```
