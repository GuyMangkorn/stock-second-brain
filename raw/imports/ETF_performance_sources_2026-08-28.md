---
type: source-batch
workflow: check-etf-performance
scope: etf-cagr-top-50
updated: 2026-08-28
window: 2016-2025
return_basis: NAV total return
verification_mode: interactive-local-fallback
reviewer_dispatch: attempted
reviewer_status: source_verifier unavailable after repeated timeout; local checklist completed
---

# ETF Performance Sources — CAGR Top 50 2026-08-28

## Verification record

- `verification_mode: interactive-local-fallback`
- `reviewer_dispatch: attempted`
- `reviewer_status: source_verifier unavailable after repeated timeout; main-agent completed the same pre-save checklist locally before writing`

## Scope and ownership

- This batch is the evidence record for `workflow: check-etf-performance` and the aggregate page [[ETF Performance CAGR Top 50 2016-2025 2026-08-28]].
- Folder inventory: `260` files under `wiki/analysis/performance/`; `255` are ETF owner pages after excluding README/index/regime/redirect artifacts.
- The screen reads only the annual NAV Total Return column from each owner page. It does not substitute market-price return, price return, issuer benchmark return, current YTD, rolling CAGR, or a different currency.
- Counts: `121` eligible; `21` proxy/secondary; `52` partial; `5` continuity-break; `56` no complete comparable window. Reconciliation: `255 = 121 + 21 + 52 + 5 + 56`.

## Metric, window, and calculation

- Common window: complete calendar years `2016` through `2025`, treated as `10.00` years.
- Return basis: `NAV Total Return`, including reinvested distributions and fund expenses where the owner page's definition states them.
- Formula shown to the user: `Cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / 10) - 1`.
- All annual inputs are the displayed owner-page observations; rounded inputs make the derived cumulative return and CAGR approximate. Raw NAV endpoints are generally `not disclosed`.
- The issuer-reported currency is preserved per row. No FX conversion or cross-currency normalization was performed.
- Common `S&P 500 Total Return` cache is not an input to this ranking. No benchmark comparison is used to determine rank.

## Eligibility and exclusion rule

- Eligible means: a current ETF owner page has ten numeric annual observations for 2016–2025 in a NAV/TR-like fund-return column, without a row marked `*` proxy/secondary or `†` inception-year partial, and without an owner-documented in-window fund objective/strategy/implementation break that makes the NAV history non-continuous like-for-like.
- `HEDJ` is retained because its 2025 `‡` row is an official year-end NAV+income calculation reconciled to a secondary observation; it is labelled `official-derived` in this batch and is not treated as a proxy.
- Retained methodology/benchmark caveats include `FYC` (benchmark methodology change 2016-04-08), `IAPD`, `CSKR`, `ISF`, `ISCF`, `EEMA`, and `FNDC`; these are not silently presented as one unchanged benchmark series, but the fund NAV rows remain the ranking input.
- Continuity-break exclusions are `NFTY`, `OPPE`, `CUSS`, `CHIQ`, and `CQQQ`. `CUSS` is excluded because its owner page documents the 2022-06-01 objective/name/benchmark change; `NFTY` documents a Taiwan-to-India index change on 2018-04-17; `OPPE` documents the 2025 transition.
- Complete-table exclusion examples are preserved as: proxy/secondary `DBEU, GREK, IDX, KWEB, OPPJ, RWJ, SCHA, SLYG, SLYV, VIOG`; partial `DGRO, VIGI, VYMI`; continuity-break `NFTY, OPPE, CUSS, CHIQ, CQQQ`; unresolved source-conflict/no-comparable-window `IPOL`. The remaining pages in the bucket counts lack a complete comparable 2016–2025 NAV TR window.

## Full eligible CAGR ledger

The following is the full 121-page ledger used to compute the rank. Each row points to the local owner page and the page's source batch; `not disclosed` is retained when metadata was not verified on the owner page.

| Rank | Ticker | Entity key | Cumulative NAV TR | CAGR | Years | Source as-of | Performance as-of | Currency | Management mode | Primary geography | Owner page | Source batch | Continuity caveat |
|---:|---|---|---:|---:|---:|---|---|---|---|---|---|---|---|
| 1 | `TDIV` | `Nasdaq:TDIV` | 375.56% | 16.87% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_TDIV Performance.md` | `not disclosed` | none |
| 2 | `VOO` | `NYSE Arca:VOO` | 296.90% | 14.78% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_VOO Performance.md` | `raw/imports/ETF_performance_sources_2026-07-13.md` | none |
| 3 | `DXJ` | `LSE:DXJ` | 268.73% | 13.94% | 10.00 | 2026-06-30 | 2026-06-30 | USD | not disclosed | geography/Japan | `wiki/analysis/performance/ETF_LSE_DXJ Performance.md` | `raw/imports/ETF_performance_sources_2026-07-23.md` | none |
| 4 | `VIG` | `NYSE Arca:VIG` | 242.14% | 13.09% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_VIG Performance.md` | `raw/imports/ETF_performance_sources_2026-07-13.md` | none |
| 5 | `FYC` | `Nasdaq:FYC` | 225.29% | 12.52% | 10.00 | 2026-06-30 | 2026-07-31 | not disclosed | passive-index | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_FYC Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | benchmark methodology changed 2016-04-08; full-year 2016 fund NAV row retained (owner page). |
| 6 | `DLN` | `NYSE Arca:DLN` | 218.23% | 12.27% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_DLN Performance.md` | `not disclosed` | none |
| 7 | `XSMO` | `NYSE Arca:XSMO` | 217.50% | 12.25% | 10.00 | not disclosed | 2025-12-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_XSMO Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 8 | `EWO` | `NYSE Arca:EWO` | 217.16% | 12.23% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Austria | `wiki/analysis/performance/ETF_NYSE_ARCA_EWO Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | tracked-index change 2013-02-12, before the 2016-2025 window; rows retained. |
| 9 | `IJPD` | `LSE:IJPD` | 216.04% | 12.20% | 10.00 | not disclosed | 2026-06-30 | not disclosed | passive-index | geography/Japan | `wiki/analysis/performance/ETF_LSE_IJPD Performance.md` | `raw/imports/ETF_performance_sources_2026-07-23.md` | none |
| 10 | `EWC` | `NYSE Arca:EWC` | 210.78% | 12.01% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Canada | `wiki/analysis/performance/ETF_NYSE_ARCA_EWC Performance.md` | `raw/imports/ETF_performance_sources_2026-07-13.md` | none |
| 11 | `DJD` | `NYSE Arca:DJD` | 207.63% | 11.89% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_DJD Performance.md` | `not disclosed` | none |
| 12 | `DTD` | `NYSE Arca:DTD` | 206.16% | 11.84% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_DTD Performance.md` | `raw/imports/ETF_performance_sources_2026-07-13.md` | none |
| 13 | `PFM` | `Nasdaq:PFM` | 205.96% | 11.83% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_PFM Performance.md` | `not disclosed` | none |
| 14 | `ENFR` | `NYSE Arca:ENFR` | 204.03% | 11.76% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/North-America | `wiki/analysis/performance/ETF_AMEX_ENFR Performance.md` | `not disclosed` | none |
| 15 | `ISAC` | `LSE:ISAC` | 201.54% | 11.67% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/International | `wiki/analysis/performance/ETF_LSE_ISAC Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 16 | `XSVM` | `NYSE Arca:XSVM` | 200.51% | 11.63% | 10.00 | not disclosed | 2025-12-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_XSVM Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 17 | `EWN` | `NYSE Arca:EWN` | 197.74% | 11.53% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Netherlands | `wiki/analysis/performance/ETF_NYSE_ARCA_EWN Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 18 | `VYM` | `NYSE Arca:VYM` | 192.23% | 11.32% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_VYM Performance.md` | `not disclosed` | none |
| 19 | `USSC` | `LSE:USSC` | 191.31% | 11.28% | 10.00 | 2025-12-31 | 2026-07-31 | USD | passive-index | geography/United-States | `wiki/analysis/performance/ETF_LSE_USSC Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 20 | `FYX` | `Nasdaq:FYX` | 183.16% | 10.97% | 10.00 | 2026-06-30 | 2026-06-30 | not disclosed | passive-index | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_FYX Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 21 | `EUFN` | `Nasdaq:EUFN` | 177.80% | 10.76% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Europe | `wiki/analysis/performance/ETF_NASDAQ_EUFN Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 22 | `FESM` | `NYSE Arca:FESM` | 174.39% | 10.62% | 10.00 | 2026-06-30 | 2026-06-30 | USD | active-equity-long-only | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_FESM Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 23 | `EWI` | `NYSE Arca:EWI` | 173.66% | 10.59% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Italy | `wiki/analysis/performance/ETF_NYSE_ARCA_EWI Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 24 | `VB` | `NYSE Arca:VB` | 169.68% | 10.43% | 10.00 | not disclosed | 2026-08-07 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_VB Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 25 | `DVY` | `Nasdaq:DVY` | 168.75% | 10.39% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_DVY Performance.md` | `not disclosed` | none |
| 26 | `ISCG` | `NYSE Arca:ISCG` | 165.20% | 10.24% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_ISCG Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 27 | `EPI` | `NYSE Arca:EPI` | 163.67% | 10.18% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/India | `wiki/analysis/performance/ETF_NYSE_ARCA_EPI Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 28 | `VBR` | `NYSE Arca:VBR` | 162.85% | 10.15% | 10.00 | 2025-12-31 | 2026-06-30 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_VBR Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 29 | `EWP` | `NYSE Arca:EWP` | 162.48% | 10.13% | 10.00 | not disclosed | 2025-12-31 | USD | not disclosed | geography/Spain | `wiki/analysis/performance/ETF_NYSE_ARCA_EWP Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 30 | `DDWM` | `Cboe BZX:DDWM` | 161.81% | 10.10% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_CBOE_DDWM Performance.md` | `not disclosed` | none |
| 31 | `EES` | `NYSE Arca:EES` | 158.70% | 9.97% | 10.00 | not disclosed | 2025-12-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_EES Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 32 | `EPOL` | `NYSE Arca:EPOL` | 154.36% | 9.79% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Poland | `wiki/analysis/performance/ETF_NYSE_ARCA_EPOL Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 33 | `DFAS` | `NYSE Arca:DFAS` | 154.28% | 9.78% | 10.00 | not disclosed | 2025-12-31 | USD | active-equity-long-only | geography/United-States | `wiki/analysis/performance/ETF_CBOE_BZX_DFAS Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 34 | `VIOO` | `NYSE Arca:VIOO` | 153.93% | 9.77% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_VIOO Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 35 | `IJR` | `NYSE Arca:IJR` | 153.87% | 9.76% | 10.00 | not disclosed | 2026-08-13 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_IJR Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 36 | `HEDJ` | `NYSE Arca:HEDJ` | 153.82% | 9.76% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Europe | `wiki/analysis/performance/ETF_NYSE_ARCA_HEDJ Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | 2025 row is official year-end NAV+income calculation reconciled to secondary and marked official-derived (‡). |
| 37 | `IDOG` | `NYSE Arca:IDOG` | 151.71% | 9.67% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_AMEX_IDOG Performance.md` | `not disclosed` | none |
| 38 | `VTWO` | `Nasdaq:VTWO` | 151.67% | 9.67% | 10.00 | 2025-12-31 | 2026-06-30 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_VTWO Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 39 | `VTWG` | `Nasdaq:VTWG` | 150.23% | 9.61% | 10.00 | not disclosed | 2025-12-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_VTWG Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 40 | `IJT` | `Nasdaq:IJT` | 150.04% | 9.60% | 10.00 | not disclosed | 2026-06-30 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_IJT Performance.md` | `raw/imports/ETF_performance_sources_2026-08-15.md` | none |
| 41 | `SDOG` | `NYSE Arca:SDOG` | 149.33% | 9.57% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_SDOG Performance.md` | `not disclosed` | none |
| 42 | `DHS` | `NYSE Arca:DHS` | 149.25% | 9.56% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_DHS Performance.md` | `not disclosed` | none |
| 43 | `IWM` | `NYSE Arca:IWM` | 148.94% | 9.55% | 10.00 | 2025-12-31 | 2026-08-13 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_IWM Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 44 | `IWO` | `NYSE Arca:IWO` | 148.84% | 9.54% | 10.00 | 2025-12-31 | 2026-08-13 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_IWO Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 45 | `VIOV` | `NYSE Arca:VIOV` | 148.69% | 9.54% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_VIOV Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 46 | `DON` | `NYSE Arca:DON` | 148.01% | 9.51% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_DON Performance.md` | `not disclosed` | none |
| 47 | `FSZ` | `Nasdaq:FSZ` | 148.00% | 9.51% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Switzerland | `wiki/analysis/performance/ETF_NASDAQ_FSZ Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | issuer index change predates the 2016-2025 window; rows retained. |
| 48 | `IJS` | `NYSE Arca:IJS` | 146.41% | 9.44% | 10.00 | not disclosed | 2026-06-30 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_IJS Performance.md` | `raw/imports/ETF_performance_sources_2026-08-15.md` | none |
| 49 | `DEM` | `NYSE Arca:DEM` | 145.43% | 9.39% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/Emerging-Markets | `wiki/analysis/performance/ETF_AMEX_DEM Performance.md` | `not disclosed` | none |
| 50 | `IDV` | `Cboe BZX:IDV` | 144.84% | 9.37% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_CBOE_IDV Performance.md` | `not disclosed` | none |
| 51 | `FEP` | `Nasdaq:FEP` | 144.62% | 9.36% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Europe | `wiki/analysis/performance/ETF_NASDAQ_FEP Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 52 | `FEUZ` | `Nasdaq:FEUZ` | 144.62% | 9.36% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Europe | `wiki/analysis/performance/ETF_NASDAQ_FEUZ Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 53 | `EWQ` | `NYSE Arca:EWQ` | 142.69% | 9.27% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/France | `wiki/analysis/performance/ETF_NYSE_ARCA_EWQ Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 54 | `CSKR` | `LSE:CSKR` | 141.88% | 9.23% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/South-Korea | `wiki/analysis/performance/ETF_LSE_CSKR Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | benchmark changed MSCI Korea Index → MSCI Korea 20/35 Index on 2020-02-11; fund NAV rows retained. |
| 55 | `FVD` | `NYSE Arca:FVD` | 141.64% | 9.22% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_FVD Performance.md` | `raw/imports/ETF_performance_sources_2026-07-12.md` | none |
| 56 | `VTWV` | `Nasdaq:VTWV` | 141.46% | 9.22% | 10.00 | not disclosed | 2025-12-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_VTWV Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 57 | `IDP6` | `LSE:IDP6` | 141.31% | 9.21% | 10.00 | 2025-12-31 | 2026-07-30 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_LSE_IDP6 Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 58 | `IMVP` | `NYSE Arca:IMVP` | 140.92% | 9.19% | 10.00 | not disclosed | 2025-12-31 | not disclosed | not disclosed | geography/India | `wiki/analysis/performance/ETF_NYSE_ARCA_IMVP Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 59 | `R2US` | `LSE:R2US` | 140.61% | 9.18% | 10.00 | not disclosed | 2026-07-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_LSE_R2US Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 60 | `FDD` | `NYSE Arca:FDD` | 139.09% | 9.11% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Europe | `wiki/analysis/performance/ETF_AMEX_FDD Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 61 | `DGS` | `NYSE Arca:DGS` | 138.91% | 9.10% | 10.00 | 2026-03-31 | 2026-07-31 | USD | not disclosed | geography/Emerging-Markets | `wiki/analysis/performance/ETF_NYSE_ARCA_DGS Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 62 | `IWN` | `NYSE Arca:IWN` | 138.50% | 9.08% | 10.00 | 2025-12-31 | 2026-08-13 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_IWN Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 63 | `ISX5` | `LSE:ISX5` | 138.31% | 9.07% | 10.00 | not disclosed | 2025-12-31 | EUR | passive-index | geography/Europe | `wiki/analysis/performance/ETF_LSE_ISX5 Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 64 | `EWL` | `NYSE Arca:EWL` | 136.56% | 8.99% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Switzerland | `wiki/analysis/performance/ETF_NYSE_ARCA_EWL Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 65 | `EWY` | `NYSE Arca:EWY` | 135.42% | 8.94% | 10.00 | not disclosed | 2026-06-30 | not disclosed | passive-index | geography/South-Korea | `wiki/analysis/performance/ETF_NYSE_ARCA_EWY Performance.md` | `raw/imports/ETF_performance_sources_2026-07-23.md` | none |
| 66 | `PEY` | `Nasdaq:PEY` | 132.93% | 8.82% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_PEY Performance.md` | `not disclosed` | none |
| 67 | `PID` | `Nasdaq:PID` | 132.73% | 8.81% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_NASDAQ_PID Performance.md` | `not disclosed` | none |
| 68 | `ISF` | `LSE:ISF` | 130.92% | 8.73% | 10.00 | 2025-12-31 | 2026-08-18 | GBP | passive-index | geography/United-Kingdom | `wiki/analysis/performance/ETF_LSE_ISF Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | benchmark changed total-return → net-of-tax total-return on 2019-07-17; fund rows retained. |
| 69 | `VGK` | `NYSE Arca:VGK` | 130.81% | 8.72% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Europe | `wiki/analysis/performance/ETF_NYSE_ARCA_VGK Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 70 | `DAX` | `Nasdaq:DAX` | 130.68% | 8.72% | 10.00 | not disclosed | 2025-12-31 | USD | active-equity-long-only | geography/Germany | `wiki/analysis/performance/ETF_NASDAQ_DAX Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 71 | `CEMU` | `Euronext Amsterdam:CEMU` | 127.84% | 8.58% | 10.00 | not disclosed | 2025-12-31 | EUR | passive-index | geography/Europe | `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_CEMU Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 72 | `ISCF` | `NYSE Arca:ISCF` | 127.24% | 8.55% | 10.00 | 2025-12-31 | 2025-12-31 | USD | passive-index | geography/International | `wiki/analysis/performance/ETF_NYSE_ARCA_ISCF Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | tracking began 2023-03-01; pre-change index and current index are disclosed on owner page; fund rows retained. |
| 73 | `VXUS` | `Nasdaq:VXUS` | 127.03% | 8.54% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_NASDAQ_VXUS Performance.md` | `raw/imports/ETF_performance_sources_2026-07-18.md` | none |
| 74 | `CEMA` | `LSE:CEMA` | 126.95% | 8.54% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Emerging-Markets | `wiki/analysis/performance/ETF_LSE_CEMA Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 75 | `ISCV` | `NYSE Arca:ISCV` | 124.65% | 8.43% | 10.00 | not disclosed | 2026-08-13 | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NYSE_ARCA_ISCV Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 76 | `VDPX` | `LSE:VDPX` | 122.03% | 8.30% | 10.00 | not disclosed | 2026-03-31 | not disclosed | not disclosed | geography/Asia-Pacific | `wiki/analysis/performance/ETF_LSE_VDPX Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 77 | `EEMA` | `Nasdaq:EEMA` | 121.24% | 8.26% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Emerging-Markets | `wiki/analysis/performance/ETF_NASDAQ_EEMA Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | index changed 2018-06-01; fund NAV rows retained with methodology caveat. |
| 78 | `FNDC` | `NYSE Arca:FNDC` | 118.08% | 8.11% | 10.00 | not disclosed | 2026-07-31 | USD | not disclosed | geography/International | `wiki/analysis/performance/ETF_NYSE_ARCA_FNDC Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | benchmark changed 2024-06-21; fund NAV rows retained with methodology caveat. |
| 79 | `VEUR` | `Euronext Amsterdam:VEUR` | 115.91% | 8.00% | 10.00 | not disclosed | 2025-12-31 | EUR | passive-index | geography/Europe | `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_VEUR Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 80 | `DTH` | `NYSE Arca:DTH` | 115.33% | 7.97% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_AMEX_DTH Performance.md` | `not disclosed` | none |
| 81 | `VPL` | `NYSE Arca:VPL` | 114.60% | 7.94% | 10.00 | not disclosed | 2026-05-31 | not disclosed | not disclosed | geography/Asia-Pacific | `wiki/analysis/performance/ETF_NYSE_ARCA_VPL Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 82 | `NORW` | `NYSE Arca:NORW` | 114.25% | 7.92% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Norway | `wiki/analysis/performance/ETF_NYSE_ARCA_NORW Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 83 | `ISEU` | `LSE:ISEU` | 113.94% | 7.90% | 10.00 | not disclosed | 2025-12-31 | EUR | passive-index | geography/Europe | `wiki/analysis/performance/ETF_LSE_ISEU Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 84 | `ENOR` | `Cboe BZX:ENOR` | 113.09% | 7.86% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Norway | `wiki/analysis/performance/ETF_CBOE_BZX_ENOR Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 85 | `DFJ` | `NYSE Arca:DFJ` | 112.38% | 7.82% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/Japan | `wiki/analysis/performance/ETF_AMEX_DFJ Performance.md` | `not disclosed` | none |
| 86 | `DWM` | `NYSE Arca:DWM` | 110.83% | 7.74% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_AMEX_DWM Performance.md` | `not disclosed` | none |
| 87 | `SAUS` | `LSE:SAUS` | 109.27% | 7.66% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Australia | `wiki/analysis/performance/ETF_LSE_SAUS Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 88 | `EWA` | `NYSE Arca:EWA` | 108.31% | 7.61% | 10.00 | not disclosed | 2026-07-16 | not disclosed | not disclosed | geography/Australia | `wiki/analysis/performance/ETF_NYSE_ARCA_EWA Performance.md` | `raw/imports/ETF_performance_sources_2026-07-19.md` | none |
| 89 | `SCHC` | `NYSE Arca:SCHC` | 108.21% | 7.61% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/International | `wiki/analysis/performance/ETF_NYSE_ARCA_SCHC Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 90 | `EIRL` | `NYSE Arca:EIRL` | 107.72% | 7.58% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Ireland | `wiki/analysis/performance/ETF_NYSE_ARCA_EIRL Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 91 | `DES` | `NYSE Arca:DES` | 106.62% | 7.53% | 10.00 | not disclosed | 2026-07-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_AMEX_DES Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 92 | `VSS` | `NYSE Arca:VSS` | 106.58% | 7.53% | 10.00 | not disclosed | 2026-08-11 | not disclosed | not disclosed | geography/International | `wiki/analysis/performance/ETF_NYSE_ARCA_VSS Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 93 | `SMDV` | `Cboe BZX:SMDV` | 106.36% | 7.51% | 10.00 | 2025-12-31 | 2025-12-31 | USD | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_CBOE_BZX_SMDV Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 94 | `SCZ` | `Nasdaq:SCZ` | 104.25% | 7.40% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/International | `wiki/analysis/performance/ETF_NASDAQ_SCZ Performance.md` | `raw/imports/ETF_performance_sources_2026-08-17.md` | none |
| 95 | `EWG` | `NYSE Arca:EWG` | 103.85% | 7.38% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Germany | `wiki/analysis/performance/ETF_NYSE_ARCA_EWG Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 96 | `ASEA` | `NYSE Arca:ASEA` | 102.43% | 7.31% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Southeast-Asia | `wiki/analysis/performance/ETF_NYSE_ARCA_ASEA Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 97 | `FCA` | `Nasdaq:FCA` | 101.92% | 7.28% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/China | `wiki/analysis/performance/ETF_NASDAQ_FCA Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 98 | `DLS` | `NYSE Arca:DLS` | 101.65% | 7.27% | 10.00 | 2026-03-31 | 2026-07-31 | not disclosed | passive-index | geography/International | `wiki/analysis/performance/ETF_NYSE_ARCA_DLS Performance.md` | `raw/imports/ETF_performance_sources_2026-08-16.md` | none |
| 99 | `EWU` | `NYSE Arca:EWU` | 101.02% | 7.23% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/United-Kingdom | `wiki/analysis/performance/ETF_NYSE_ARCA_EWU Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 100 | `EWJ` | `NYSE Arca:EWJ` | 101.00% | 7.23% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Japan | `wiki/analysis/performance/ETF_NYSE_ARCA_EWJ Performance.md` | `raw/imports/ETF_performance_sources_2026-07-18.md` | none |
| 101 | `CPXJ` | `LSE:CPXJ` | 100.75% | 7.22% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Asia-Pacific | `wiki/analysis/performance/ETF_LSE_CPXJ Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 102 | `CJPU` | `LSE:CJPU` | 100.65% | 7.21% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Japan | `wiki/analysis/performance/ETF_LSE_CJPU Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 103 | `IJPU` | `LSE:IJPU` | 98.94% | 7.12% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Japan | `wiki/analysis/performance/ETF_LSE_IJPU Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 104 | `IAPD` | `LSE:IAPD` | 94.63% | 6.89% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Asia-Pacific | `wiki/analysis/performance/ETF_LSE_IAPD Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | benchmark change is disclosed before 2020-06-22; fund NAV rows retained because the rank uses fund NAV TR only. |
| 105 | `EPP` | `NYSE Arca:EPP` | 94.42% | 6.87% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Asia-Pacific | `wiki/analysis/performance/ETF_NYSE_ARCA_EPP Performance.md` | `raw/imports/ETF_performance_sources_2026-07-23.md` | none |
| 106 | `SCJ` | `NYSE Arca:SCJ` | 91.92% | 6.74% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Japan | `wiki/analysis/performance/ETF_NYSE_ARCA_SCJ Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 107 | `FPA` | `Nasdaq:FPA` | 89.03% | 6.57% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Asia-Pacific | `wiki/analysis/performance/ETF_NASDAQ_FPA Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 108 | `CXSE` | `Nasdaq:CXSE` | 82.98% | 6.23% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/China | `wiki/analysis/performance/ETF_NASDAQ_CXSE Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 109 | `AMLP` | `NYSE Arca:AMLP` | 82.29% | 6.19% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/North-America | `wiki/analysis/performance/ETF_AMEX_AMLP Performance.md` | `not disclosed` | none |
| 110 | `FKU` | `Nasdaq:FKU` | 80.82% | 6.10% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/United-Kingdom | `wiki/analysis/performance/ETF_NASDAQ_FKU Performance.md` | `raw/imports/ETF_performance_sources_2026-08-18.md` | none |
| 111 | `EFAV` | `Cboe BZX:EFAV` | 78.42% | 5.96% | 10.00 | not disclosed | 2026-07-16 | USD | not disclosed | geography/International | `wiki/analysis/performance/ETF_CBOE_EFAV Performance.md` | `raw/imports/ETF_performance_sources_2026-07-18.md` | none |
| 112 | `KBWD` | `Nasdaq:KBWD` | 77.77% | 5.92% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_KBWD Performance.md` | `not disclosed` | none |
| 113 | `FJP` | `Nasdaq:FJP` | 76.82% | 5.87% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Japan | `wiki/analysis/performance/ETF_NASDAQ_FJP Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 114 | `EWH` | `NYSE Arca:EWH` | 51.86% | 4.27% | 10.00 | not disclosed | 2026-07-17 | not disclosed | not disclosed | geography/Hong-Kong | `wiki/analysis/performance/ETF_NYSE_ARCA_EWH Performance.md` | `raw/imports/ETF_performance_sources_2026-07-21.md` | none |
| 115 | `VNM` | `Cboe BZX:VNM` | 44.54% | 3.75% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Vietnam | `wiki/analysis/performance/ETF_CBOE_BZX_VNM Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 116 | `FXC` | `LSE:FXC` | 38.28% | 3.29% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/China | `wiki/analysis/performance/ETF_LSE_FXC Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 117 | `TUR` | `Nasdaq:TUR` | 25.33% | 2.28% | 10.00 | not disclosed | 2025-12-31 | USD | passive-index | geography/Turkey | `wiki/analysis/performance/ETF_NASDAQ_TUR Performance.md` | `raw/imports/ETF_performance_sources_2026-08-19.md` | none |
| 118 | `GLIN` | `NYSE Arca:GLIN` | 17.36% | 1.61% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/India | `wiki/analysis/performance/ETF_NYSE_ARCA_GLIN Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 119 | `EIDO` | `NYSE Arca:EIDO` | 11.70% | 1.11% | 10.00 | not disclosed | 2026-06-30 | not disclosed | not disclosed | geography/Indonesia | `wiki/analysis/performance/ETF_NYSE_ARCA_EIDO Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |
| 120 | `KBWY` | `Nasdaq:KBWY` | 10.39% | 0.99% | 10.00 | not disclosed | not disclosed | not disclosed | not disclosed | geography/United-States | `wiki/analysis/performance/ETF_NASDAQ_KBWY Performance.md` | `not disclosed` | none |
| 121 | `PGJ` | `Nasdaq:PGJ` | 3.50% | 0.34% | 10.00 | not disclosed | 2025-12-31 | not disclosed | not disclosed | geography/China | `wiki/analysis/performance/ETF_NASDAQ_PGJ Performance.md` | `raw/imports/ETF_performance_sources_2026-07-24.md` | none |

## Revised Top 50 raw annual observations

The following raw values are the 10 annual NAV TR inputs used for the 50 displayed bars. They are copied from the fund-return column selected on each owner page; benchmark columns are not used.

| Rank | Ticker | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Owner page |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `TDIV` | 19.63% | 21.90% | -3.01% | 33.31% | 17.27% | 29.56% | -22.14% | 36.78% | 24.51% | 25.19% | `wiki/analysis/performance/ETF_NASDAQ_TDIV Performance.md` |
| 2 | `VOO` | 11.93% | 21.78% | -4.42% | 31.46% | 18.35% | 28.66% | -18.15% | 26.25% | 24.98% | 17.84% | `wiki/analysis/performance/ETF_NYSE_ARCA_VOO Performance.md` |
| 3 | `DXJ` | 0.73% | 22.17% | -18.71% | 18.53% | 2.82% | 18.07% | 6.48% | 40.46% | 30.55% | 31.19% | `wiki/analysis/performance/ETF_LSE_DXJ Performance.md` |
| 4 | `VIG` | 11.84% | 22.22% | -2.02% | 29.71% | 15.46% | 23.64% | -9.79% | 14.46% | 17.02% | 14.18% | `wiki/analysis/performance/ETF_AMEX_VIG Performance.md` |
| 5 | `FYC` | 13.92% | 23.19% | -5.60% | 16.80% | 32.08% | 21.75% | -25.75% | 14.15% | 24.05% | 24.34% | `wiki/analysis/performance/ETF_NASDAQ_FYC Performance.md` |
| 6 | `DLN` | 15.37% | 18.21% | -5.77% | 29.03% | 4.55% | 25.60% | -3.79% | 9.93% | 19.55% | 15.59% | `wiki/analysis/performance/ETF_AMEX_DLN Performance.md` |
| 7 | `XSMO` | 7.17% | 23.42% | -2.88% | 28.35% | 21.84% | 19.28% | -15.48% | 21.43% | 17.57% | 9.81% | `wiki/analysis/performance/ETF_NYSE_ARCA_XSMO Performance.md` |
| 8 | `EWO` | 7.10% | 52.50% | -23.20% | 17.70% | -3.20% | 30.74% | -21.67% | 19.88% | 4.58% | 72.85% | `wiki/analysis/performance/ETF_NYSE_ARCA_EWO Performance.md` |
| 9 | `IJPD` | -1.90% | 20.70% | -14.10% | 20.40% | 9.00% | 12.80% | -2.70% | 34.50% | 25.60% | 27.70% | `wiki/analysis/performance/ETF_LSE_IJPD Performance.md` |
| 10 | `EWC` | 24.30% | 16.00% | -17.20% | 27.40% | 5.60% | 26.74% | -12.77% | 14.62% | 12.25% | 36.03% | `wiki/analysis/performance/ETF_NYSE_ARCA_EWC Performance.md` |
| 11 | `DJD` | 16.93% | 21.63% | 0.11% | 22.37% | 0.94% | 22.33% | -0.61% | 9.26% | 13.79% | 15.72% | `wiki/analysis/performance/ETF_AMEX_DJD Performance.md` |
| 12 | `DTD` | +16.59% | +17.25% | -6.35% | +28.28% | +2.57% | +26.14% | -3.81% | +10.44% | +18.75% | +14.22% | `wiki/analysis/performance/ETF_AMEX_DTD Performance.md` |
| 13 | `PFM` | 14.64% | 17.35% | -4.40% | 26.79% | 9.54% | 23.19% | -6.23% | 11.31% | 16.98% | 13.88% | `wiki/analysis/performance/ETF_NASDAQ_PFM Performance.md` |
| 14 | `ENFR` | 41.95% | -0.09% | -18.29% | 21.20% | -24.31% | 39.60% | 18.33% | 15.05% | 42.06% | 5.93% | `wiki/analysis/performance/ETF_AMEX_ENFR Performance.md` |
| 15 | `ISAC` | 7.82% | 23.94% | -9.52% | 26.37% | 15.62% | 18.71% | -18.19% | 22.35% | 17.35% | 22.41% | `wiki/analysis/performance/ETF_LSE_ISAC Performance.md` |
| 16 | `XSVM` | 35.52% | 3.17% | -11.82% | 29.95% | 5.03% | 56.38% | -13.55% | 20.23% | 2.12% | 7.59% | `wiki/analysis/performance/ETF_NYSE_ARCA_XSVM Performance.md` |
| 17 | `EWN` | 3.91% | 33.40% | -14.99% | 31.34% | 24.19% | 22.39% | -24.12% | 21.34% | 2.34% | 34.32% | `wiki/analysis/performance/ETF_NYSE_ARCA_EWN Performance.md` |
| 18 | `VYM` | 16.87% | 16.42% | -5.87% | 24.20% | 1.14% | 26.14% | -0.42% | 6.53% | 17.60% | 15.43% | `wiki/analysis/performance/ETF_AMEX_VYM Performance.md` |
| 19 | `USSC` | 25.83% | 9.37% | -14.31% | 23.80% | 8.46% | 35.40% | -10.23% | 21.18% | 9.67% | 13.89% | `wiki/analysis/performance/ETF_LSE_USSC Performance.md` |
| 20 | `FYX` | 22.72% | 14.45% | -10.26% | 21.04% | 19.23% | 27.48% | -18.39% | 18.12% | 12.20% | 12.90% | `wiki/analysis/performance/ETF_NASDAQ_FYX Performance.md` |
| 21 | `EUFN` | -3.10% | 27.20% | -23.20% | 20.10% | -8.20% | 19.22% | -8.79% | 26.18% | 17.41% | 65.23% | `wiki/analysis/performance/ETF_NASDAQ_EUFN Performance.md` |
| 22 | `FESM` | 22.84% | 7.22% | -13.04% | 23.65% | 18.53% | 20.54% | -18.28% | 21.04% | 16.48% | 17.70% | `wiki/analysis/performance/ETF_NYSE_ARCA_FESM Performance.md` |
| 23 | `EWI` | -9.40% | 28.47% | -17.51% | 27.19% | 2.56% | 13.80% | -14.19% | 30.34% | 10.39% | 55.51% | `wiki/analysis/performance/ETF_NYSE_ARCA_EWI Performance.md` |
| 24 | `VB` | 18.31% | 16.24% | -9.30% | 27.37% | 19.08% | 17.72% | -17.60% | 18.21% | 14.23% | 8.83% | `wiki/analysis/performance/ETF_NYSE_ARCA_VB Performance.md` |
| 25 | `DVY` | 21.50% | 15.00% | -6.30% | 22.70% | -4.90% | 31.63% | 1.92% | 1.09% | 16.19% | 11.64% | `wiki/analysis/performance/ETF_NASDAQ_DVY Performance.md` |
| 26 | `ISCG` | 9.48% | 23.48% | -5.79% | 27.41% | 43.28% | -1.32% | -26.65% | 22.84% | 13.44% | 13.09% | `wiki/analysis/performance/ETF_NYSE_ARCA_ISCG Performance.md` |
| 27 | `EPI` | 2.24% | 39.03% | -10.44% | 1.70% | 18.07% | 28.02% | -5.72% | 26.31% | 11.11% | 1.83% | `wiki/analysis/performance/ETF_NYSE_ARCA_EPI Performance.md` |
| 28 | `VBR` | 24.80% | 11.79% | -12.22% | 22.76% | 5.82% | 28.07% | -9.29% | 16.00% | 12.39% | 9.09% | `wiki/analysis/performance/ETF_NYSE_ARCA_VBR Performance.md` |
| 29 | `EWP` | -2.18% | 26.97% | -15.07% | 10.94% | -3.14% | 0.10% | -5.34% | 29.80% | 6.30% | 77.12% | `wiki/analysis/performance/ETF_NYSE_ARCA_EWP Performance.md` |
| 30 | `DDWM` | 14.18% | 18.52% | -11.05% | 21.03% | -4.20% | 14.33% | -1.27% | 15.44% | 10.65% | 30.10% | `wiki/analysis/performance/ETF_CBOE_DDWM Performance.md` |
| 31 | `EES` | 29.96% | 12.56% | -9.96% | 21.92% | 2.79% | 34.34% | -16.16% | 18.42% | 9.89% | 6.93% | `wiki/analysis/performance/ETF_NYSE_ARCA_EES Performance.md` |
| 32 | `EPOL` | 2.80% | 52.70% | -14.30% | -5.60% | -8.20% | 12.15% | -24.53% | 50.13% | -2.58% | 76.25% | `wiki/analysis/performance/ETF_NYSE_ARCA_EPOL Performance.md` |
| 33 | `DFAS` | 23.99% | 11.87% | -13.12% | 21.89% | 10.36% | 29.70% | -13.80% | 17.53% | 10.35% | 8.18% | `wiki/analysis/performance/ETF_CBOE_BZX_DFAS Performance.md` |
| 34 | `VIOO` | 26.44% | 13.31% | -8.57% | 22.72% | 11.43% | 26.67% | -16.20% | 16.00% | 8.62% | 5.99% | `wiki/analysis/performance/ETF_NYSE_ARCA_VIOO Performance.md` |
| 35 | `IJR` | 26.49% | 13.20% | -8.43% | 22.79% | 11.24% | 26.69% | -16.20% | 16.03% | 8.61% | 5.95% | `wiki/analysis/performance/ETF_NYSE_ARCA_IJR Performance.md` |
| 36 | `HEDJ` | 9.30% | 13.56% | -9.27% | 26.99% | -2.90% | 23.57% | -10.18% | 26.39% | 5.65% | 23.33%‡ | `wiki/analysis/performance/ETF_NYSE_ARCA_HEDJ Performance.md` |
| 37 | `IDOG` | 3.97% | 25.81% | -13.09% | 20.86% | -1.34% | 11.36% | -4.23% | 22.64% | 1.53% | 39.83% | `wiki/analysis/performance/ETF_AMEX_IDOG Performance.md` |
| 38 | `VTWO` | 21.33% | 14.70% | -10.98% | 25.61% | 20.10% | 14.81% | -20.40% | 17.00% | 11.57% | 12.88% | `wiki/analysis/performance/ETF_NASDAQ_VTWO Performance.md` |
| 39 | `VTWG` | 11.40% | 22.13% | -9.31% | 28.59% | 34.70% | 2.82% | -26.35% | 18.73% | 15.17% | 13.07% | `wiki/analysis/performance/ETF_NASDAQ_VTWG Performance.md` |
| 40 | `IJT` | 22.00% | 14.57% | -4.28% | 20.82% | 19.17% | 22.40% | -21.24% | 16.97% | 9.42% | 5.20% | `wiki/analysis/performance/ETF_NASDAQ_IJT Performance.md` |
| 41 | `SDOG` | 22.36% | 12.67% | -11.30% | 24.09% | -0.37% | 24.40% | -0.13% | 4.06% | 14.84% | 11.08% | `wiki/analysis/performance/ETF_AMEX_SDOG Performance.md` |
| 42 | `DHS` | 17.85% | 11.68% | -7.25% | 22.58% | -5.68% | 23.11% | 7.88% | -0.19% | 17.98% | 12.92% | `wiki/analysis/performance/ETF_AMEX_DHS Performance.md` |
| 43 | `IWM` | 21.4% | 14.7% | -11.0% | 25.4% | 19.9% | 14.6% | -20.5% | 16.8% | 11.4% | 12.7% | `wiki/analysis/performance/ETF_NYSE_ARCA_IWM Performance.md` |
| 44 | `IWO` | 11.47% | 22.24% | -9.33% | 28.46% | 34.52% | 2.71% | -26.33% | 18.58% | 15.04% | 12.92% | `wiki/analysis/performance/ETF_NYSE_ARCA_IWO Performance.md` |
| 45 | `VIOV` | 31.07% | 11.50% | -12.77% | 24.40% | 2.70% | 30.74% | -11.19% | 14.75% | 7.45% | 6.66% | `wiki/analysis/performance/ETF_NYSE_ARCA_VIOV Performance.md` |
| 46 | `DON` | 20.30% | 14.86% | -8.27% | 23.42% | -5.40% | 30.19% | -4.76% | 13.98% | 14.12% | 3.91% | `wiki/analysis/performance/ETF_AMEX_DON Performance.md` |
| 47 | `FSZ` | 4.21% | 31.26% | -15.11% | 25.91% | 14.50% | 19.34% | -20.88% | 22.07% | -1.25% | 30.16% | `wiki/analysis/performance/ETF_NASDAQ_FSZ Performance.md` |
| 48 | `IJS` | 31.17% | 11.36% | -12.80% | 24.25% | 2.56% | 30.47% | -11.32% | 14.64% | 7.42% | 6.55% | `wiki/analysis/performance/ETF_NYSE_ARCA_IJS Performance.md` |
| 49 | `DEM` | 22.54% | 24.87% | -7.31% | 19.37% | -5.64% | 11.69% | -10.32% | 20.93% | 5.22% | 20.54% | `wiki/analysis/performance/ETF_AMEX_DEM Performance.md` |
| 50 | `IDV` | 7.70% | 19.60% | -10.50% | 23.10% | -5.40% | 11.97% | -6.75% | 10.75% | 3.97% | 51.69% | `wiki/analysis/performance/ETF_CBOE_IDV Performance.md` |

## Scheduled-inline item records — 2026-08-28

The following item record belongs to the Trello `etf-performance` run. It is
appended to this date's source batch without changing the earlier aggregate
screen's verification record.

### CNYA

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- `entity_key: Cboe BZX:CNYA`; issuer page and factsheet identify the exchange as `Cboe BZX` and the fund as `iShares MSCI China A ETF`.
- `management_mode: passive-index`; official issuer description states that the fund seeks to track an index of Chinese equities trading on the Shanghai or Shenzhen Stock Exchange; official factsheet labels the fund `PASSIVE`.
- `inception: 2016-06-13`; `expense_ratio: 0.60%`; `distribution_frequency: semi-annual`.
- Metric: official `NAV Total Return`, including reinvested dividends/capital gains and fund expenses; currency `USD`.
- Issuer benchmark: `MSCI China A Inclusion Index (Net)` from 2018-04-26 onward; prior index history is `MSCI China A International Index`. The issuer product page shortens the key-facts label to `MSCI China A Inclusion Index`.
- Current snapshot: NAV `USD 36.08` as of `2026-08-27`; closing price `USD 35.83` as of `2026-08-27`; current NAV TR YTD `3.57%` as of `2026-08-26`; holdings `411` as of `2026-08-27`; 3-year standard deviation `19.90%` as of `2026-07-31`; P/E `17.75` and P/B `1.94` as of `2026-08-26`.
- Official calendar NAV TR / issuer benchmark rows, performance as of `2026-06-30`: `2021 2.96% / 3.20%`; `2022 -26.31% / -25.90%`; `2023 -13.51% / -13.47%`; `2024 11.08% / 11.70%`; `2025 25.59% / 26.48%`. 2016–2020 annual rows were not disclosed in the reviewed issuer table; 2016 is marked as a partial inception year and excluded from ranking.
- Official rolling 10-year NAV TR as of `2026-06-30`: `91.51%` cumulative and `6.71%` annualized from `2016-06-30` to `2026-06-30`. Raw endpoint values were not disclosed; normalized review endpoints are `100.00` and `191.51`, with `Years: 10.00`.
- Common benchmark: cached `S&P 500 Total Return` in USD, dividends reinvested, complete calendar years `2016–2025`, as of `2025-12-31`; rows are not used as issuer benchmark or for a new current-YTD claim.
- Calculations from displayed complete rows: CNYA 2021–2025 cumulative `-8.46%`, CAGR `-1.75%`; S&P 500 cumulative `96.17%`, CAGR `14.43%`; CNYA minus S&P CAGR `-16.18 pp`; up/down years `3 / 2`; best `2025 +25.59%`; least positive `2021 +2.96%`; worst `2022 -26.31%`; least bad down year `2023 -13.51%`.
- Source URLs: issuer product/performance page `https://www.ishares.com/us/products/273318/ishares-msci-china-a-etf`; official factsheet `https://www.ishares.com/us/literature/fact-sheet/cnya-ishares-msci-china-a-etf-fund-fact-sheet-en-us.pdf`; summary prospectus `https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-a-etf-7-31.pdf`; cached benchmark source links remain in the skill convention and the pre-existing batch record.
- Gaps/caveats: daily NAV observations sufficient for fund-level max drawdown/recovery were not captured; raw 10-year NAV endpoints and 2016–2020 annual rows are not disclosed; the 2018 issuer benchmark change is retained.

### EZU

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- `entity_key: Cboe BZX:EZU`; issuer product page identifies the fund as `iShares MSCI Eurozone ETF` on `Cboe BZX`.
- `management_mode: passive-index`; the official issuer description says the fund seeks to track an index of large- and mid-cap developed-country equities using the euro; the prospectus describes an indexing approach and representative sampling.
- `inception: 2000-07-25`; `expense_ratio: 0.50%`; `distribution_frequency: semi-annual`.
- Metric: official `NAV Total Return`, with reinvested distributions and fund expenses reflected in NAV; return currency `USD`.
- Issuer benchmark: `MSCI EMU Index (Net)`; common benchmark remains cached `S&P 500 Total Return` in USD with dividends reinvested.
- Current snapshot: NAV `USD 71.33` as of `2026-08-26`; closing price `USD 71.40` as of `2026-08-26`; current NAV TR YTD `13.57%` as of `2026-08-25`; net assets `USD 10,028,823,430` and holdings `220` as of `2026-08-26`; 3-year standard deviation `14.62%` as of `2026-07-31`; P/E `19.11` and P/B `2.38` as of `2026-08-26`.
- Official calendar NAV TR / issuer benchmark rows, performance as of `2026-06-30`: `2021 13.59% / 13.54%`; `2022 -17.28% / -17.86%`; `2023 22.93% / 22.94%`; `2024 2.58% / 2.64%`; `2025 39.66% / 40.30%`. 2016–2020 annual rows were not disclosed in the reviewed issuer table.
- Official rolling NAV TR as of `2026-06-30`: 10-year annualized `10.91%`; 10-year cumulative `181.78%` from the issuer table. The issuer did not disclose raw rolling endpoint values in the reviewed capture, so no raw-endpoint CAGR was reconstructed.
- Calculations from displayed complete rows: EZU 2021–2025 cumulative `65.48%`, CAGR `10.60%`; issuer benchmark cumulative `65.11%`, CAGR `10.55%`; fund minus issuer benchmark `+0.05 pp` CAGR; S&P 500 cumulative `96.17%`, CAGR `14.43%`; EZU minus S&P `-3.83 pp` CAGR; up/down years `4 / 1`; best `2025 +39.66%`; least positive `2024 +2.58%`; worst `2022 -17.28%`.
- Source URLs: issuer product/performance page `https://www.ishares.com/us/products/239644/EZU`; official factsheet `https://www.ishares.com/us/literature/fact-sheet/ezu-ishares-msci-eurozone-etf-fund-fact-sheet-en-us.pdf`; SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/930667/000119312525336639/d31674d497k.htm`; cached benchmark source links remain in the skill convention and the pre-existing batch record.
- Gaps/caveats: daily NAV observations sufficient for fund-level max drawdown/recovery were not captured; 2016–2020 annual rows are not disclosed; the annual five-row population standard deviation `19.15%` is a calculation from rounded NAV rows and is not substituted for the issuer's 3-year measure; USD share-class returns retain EUR/USD exposure.

### INDA

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- `entity_key: Cboe BZX:INDA`; the canonical iShares product page identifies the fund as `iShares MSCI India ETF` on `Cboe BZX`.
- `management_mode: passive-index`; the official issuer description says the fund seeks to track an index of Indian equities, and the prospectus supports an indexing objective.
- `inception: 2012-02-02`; `expense_ratio: 0.61%`; `distribution_frequency: semi-annual`.
- Metric: official `NAV Total Return`, with reinvested distributions and fund expenses reflected in NAV; return currency `USD`.
- Issuer benchmark: `MSCI India Index (Net)`; common benchmark remains cached `S&P 500 Total Return` in USD with dividends reinvested.
- Current canonical product-page snapshot: NAV `USD 49.56`, closing price `USD 49.75`, net assets `USD 6,613,614,143`, and holdings `167`, all as of `2026-08-26`; current NAV TR YTD is `-8.44%` as of `2026-08-26`; 3-year standard deviation is `14.09%` as of `2026-07-31`; P/E `22.80` and P/B `3.30` as of `2026-08-26`.
- Official rolling NAV TR fields as of `2026-06-30`: 1-year `-11.39%`, 3-year `4.41%`, 5-year `3.64%`, 10-year `7.07%`, and since inception `5.72%`; official 10-year cumulative return is `98.09%` for `2016-06-30` to `2026-06-30`, or `10.00` elapsed years. Raw rolling endpoints were not disclosed; normalized review endpoints are `100.00` and `198.09`.
- Official calendar NAV TR / issuer benchmark rows, performance as of `2026-06-30`: `2021 22.41% / 26.23%`; `2022 -9.38% / -7.95%`; `2023 17.49% / 20.81%`; `2024 8.99% / 11.22%`; `2025 2.47% / 2.62%`. 2016–2020 annual rows were not disclosed in the reviewed issuer table. The issuer table's month-end 2026 YTD NAV TR is `-9.09%` as of `2026-06-30`; current product-page YTD is kept separately.
- Common benchmark: cached `S&P 500 Total Return` in USD, dividends reinvested, complete calendar years `2016–2025`, as of `2025-12-31`; rows are not used as issuer benchmark or for a new current-YTD claim.
- Calculations from displayed complete rows: INDA 2021–2025 cumulative `45.55%`, CAGR `7.80%`; MSCI India Index (Net) cumulative `60.22%`, CAGR `9.89%`; INDA minus issuer benchmark CAGR `-2.09 pp`; S&P 500 cumulative `96.17%`, CAGR `14.43%`; INDA minus S&P CAGR `-6.63 pp`; up/down years `4 / 1`; best `2021 +22.41%`; least positive `2025 +2.47%`; worst `2022 -9.38%`.
- Source conflict: a separate iShares overview endpoint returned `-7.61%` YTD and `165` holdings as of `2026-08-25`; it was not mixed into the snapshot. The canonical `/INDA` product page was selected because it is the direct product endpoint and provides the later `2026-08-26` as-of date with internally consistent current fields.
- Source URLs: issuer product/performance page `https://www.ishares.com/us/products/239659/INDA`; official factsheet `https://www.ishares.com/us/literature/fact-sheet/inda-ishares-msci-india-etf-fund-fact-sheet-en-us.pdf`; summary prospectus `https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-india-etf-8-31.pdf`; S&P 500 definition `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached benchmark source links remain in the skill convention and the pre-existing batch record.
- Gaps/caveats: daily NAV observations sufficient for fund-level max drawdown/recovery were not captured; raw 10-year endpoints and 2016–2020 annual rows are not disclosed; sector breakdown was not disclosed in the reviewed current canonical product-page capture; the separate overview endpoint conflict is preserved above rather than averaged or silently discarded.

### SMIN

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- `entity_key: Cboe BZX:SMIN`; the canonical iShares product page identifies the fund as `iShares MSCI India Small-Cap ETF` on `Cboe BZX`.
- `management_mode: passive-index`; the issuer description and summary prospectus state that the fund seeks to track an index composed of small-capitalization Indian equities and uses an indexing approach.
- `inception: 2012-02-08`; `expense_ratio: 0.74%`; `distribution_frequency: semi-annual`.
- Metric: official `NAV Total Return`, with reinvested dividends/distributions and fund expenses reflected in NAV; return currency `USD`.
- Issuer benchmark: `MSCI India Small Cap Index (Net)`; common benchmark remains cached `S&P 500 Total Return` in USD with dividends reinvested.
- Current canonical product-page snapshot: NAV `USD 71.90`, closing price `USD 72.13`, net assets `USD 772,891,256`, shares outstanding `10,750,000`, and holdings `461`, all as of `2026-08-25`; current NAV TR YTD is `2.57%` as of `2026-08-25`; expense ratio `0.74%`; 3-year standard deviation `18.82%` and equity beta `0.46` as of `2026-07-31`; P/E `32.69` and P/B `3.59` as of `2026-08-25`.
- Current sector snapshot as of `2026-08-25`: Industrials `19.70%`, Financials `17.14%`, Health Care `15.14%`, Consumer Discretionary `14.73%`, Materials `11.84%`, Information Technology `8.04%`, Consumer Staples `4.12%`, Real Estate `3.48%`, Utilities `2.37%`, Communication `1.98%`, Energy `1.14%`, and Cash/Derivatives `0.32%`.
- Official rolling NAV TR as of `2026-06-30`: 10-year annualized `9.71%` and 10-year cumulative `152.70%` for `2016-06-30` to `2026-06-30`, or `10.00` elapsed years. Raw rolling endpoints were not disclosed; normalized review endpoints are `100.00` and `252.70`. Other annualized NAV TR fields are 1-year `-7.02%`, 3-year `9.79%`, 5-year `7.42%`, and since inception `9.00%`.
- Official calendar NAV TR / issuer benchmark rows, performance as of `2026-06-30`: `2021 44.69% / 51.13%`; `2022 -13.98% / -13.43%`; `2023 34.80% / 42.63%`; `2024 17.34% / 22.63%`; `2025 -6.82% / -7.92%`. The issuer table's month-end 2026 YTD is `-0.02%` NAV versus `1.08%` benchmark as of `2026-06-30`; current product-page YTD is kept separately.
- Additional complete calendar rows: the official summary prospectus supplies NAV rows for `2015-2024` and the June 2026 factsheet supplies `2025`; the assembled 2015-2025 NAV rows compound to `153.86%` / rounded-input CAGR `8.84%`. The strict common comparison uses the issuer-published 2021-2025 rows.
- Common benchmark: cached `S&P 500 Total Return` in USD, dividends reinvested, complete calendar years `2016–2025`, as of `2025-12-31`; rows are not used as issuer benchmark or for a new current-YTD claim.
- Calculations from displayed complete rows: SMIN 2021-2025 cumulative `83.44%`, CAGR `12.90%`; issuer benchmark cumulative `110.71%`, CAGR `16.07%`; SMIN minus issuer benchmark CAGR `-3.17 pp`; S&P 500 cumulative `96.17%`, CAGR `14.43%`; SMIN minus S&P CAGR `-1.53 pp`; up/down years in 2015-2025 `6 / 5`; best `2017 +61.78%`; least positive `2015 +2.02%`; worst `2018 -25.43%`; least bad down year `2016 -0.42%`.
- Source URLs: issuer product/performance page `https://www.ishares.com/us/products/239660/SMIN`; official factsheet `https://www.ishares.com/us/literature/fact-sheet/smin-ishares-msci-india-small-cap-etf-fund-fact-sheet-en-us.pdf`; summary prospectus `https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-india-small-cap-etf-8-31.pdf`; MSCI India Small Cap Index factsheet `https://www.msci.com/documents/10199/255599/msci-india-small-cap-index.pdf`; S&P 500 definition `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached benchmark source links remain in the skill convention and the pre-existing batch record.
- Gaps/caveats: daily NAV observations sufficient for fund-level max drawdown/recovery were not captured; raw 10-year endpoints are not disclosed; 2015-2024 rows are sourced from the dated prospectus/chart plus the later 2025 factsheet and are kept separate from the current 2026 YTD observation; benchmark-relative differences are tracking comparisons, not alpha.

### SJPA

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- `entity_key: LSE:SJPA`; input alias `IHREF` (OTC) resolves to iShares Core MSCI Japan IMI UCITS ETF, ISIN `IE00B4L5YX21`. Official listings identify `LSE:SJPA` in GBP and the same USD accumulating share class under `LSE:IJPA` in USD; the canonical card mapping remains `LSE:SJPA`.
- `management_mode: passive-index`; the official product page and July 2026 factsheet state that the fund seeks to track an index of Japanese large-, mid- and small-cap companies. Product structure is `physical`, methodology `optimised`, and use of income is `accumulating`.
- `inception: 2009-09-25`; `total_expense_ratio: 0.12%`; `rebalance_frequency: quarterly`; domicile `Ireland`; issuing company `iShares III plc`.
- Metric: official `NAV Total Return` for the USD accumulating share class, with gross income reinvested where applicable; listing currency and return currency are kept separate (`GBP` LSE:SJPA listing, `USD` NAV return).
- Issuer benchmark: `MSCI Japan Investable Market Net Index (USD)`; the issuer states the tracked index changed from `MSCI Japan Index` to the IMI index on `2014-05-30`. Common benchmark remains cached `S&P 500 Total Return` in USD with dividends reinvested.
- Current canonical product-page snapshot: NAV `USD 82.57`, current NAV TR YTD `19.87%`, share-class net assets `USD 8,336,622,614`, fund net assets `USD 8,660,886,597`, shares outstanding `100,963,152`, and holdings `955`, all as of `2026-08-26`; P/B `1.88` and P/E `18.73` as of `2026-08-26`; 3-year standard deviation `14.77%` and beta `0.993` as of `2026-07-31`.
- Current sector snapshot as of `2026-08-26`: Industrials `24.44%`, Financials `17.55%`, Information Technology `16.95%`, Consumer Discretionary `14.86%`, Communication `5.82%`, Health Care `5.26%`, Materials `5.14%`, Consumer Staples `4.61%`, Real Estate `2.88%`, and Utilities `1.18%`.
- The July 2026 official factsheet reports 2016-2025 calendar NAV / benchmark rows: `2016 3.12% / 3.25%`; `2017 25.09% / 25.25%`; `2018 -13.58% / -13.46%`; `2019 19.43% / 19.56%`; `2020 13.03% / 13.10%`; `2021 0.92% / 0.98%`; `2022 -15.88% / -15.78%`; `2023 18.86% / 18.96%`; `2024 7.47% / 7.57%`; `2025 25.36% / 25.45%`. The factsheet's current month-end YTD is `16.99%` NAV versus `17.02%` benchmark as of `2026-07-31`; current product-page YTD is kept separately.
- Calculations from displayed complete rows: 2016-2025 SJPA cumulative `104.57%`, rounded-input CAGR `7.42%`; issuer benchmark cumulative `106.61%`, CAGR `7.53%`; SJPA minus issuer benchmark `-0.11 pp` CAGR. For 2021-2025, SJPA cumulative `35.94%`, CAGR `6.33%`; issuer benchmark cumulative `36.53%`, CAGR `6.42%`; gap `-0.09 pp` CAGR. Cached S&P 500 2016-2025 cumulative `298.33%`, CAGR `14.82%`; SJPA minus S&P `-7.40 pp`; 2021-2025 S&P cumulative `96.17%`, CAGR `14.43%`; gap `-8.09 pp`.
- Calendar-window observations: 2016-2025 up/down years `8 / 2`; best `2017 +25.09%`; least positive `2021 +0.92%`; worst `2022 -15.88%`; least bad down year `2018 -13.58%`.
- Conflict and quality choice: the prior dated source capture `raw/imports/ETF_performance_sources_2026-07-23.md` reported an issuer rolling 10-year `147.80%` cumulative / `9.50%` CAGR for 2016-06-30 to 2026-06-30. The current July factsheet/product capture does not disclose a rolling 10-year numeric field and its official 2016-2025 series compounds to `104.57%` / `7.42%`; the two records cannot be reconciled from the available primary evidence. The current owner page therefore marks rolling 10-year as `not disclosed`, uses the transparent 2016-2025 calendar CAGR with a caveat, and does not silently carry forward the conflicting value.
- Source URLs: official product/performance page `https://www.ishares.com/uk/professionals/en/products/251867/ishares-core-msci-japan-imi-ucits-etf?siteEntryPassthrough=true&switchLocale=y`; official July factsheet `https://www.ishares.com/uk/individual/en/literature/fact-sheet/sjpa-ishares-core-msci-japan-imi-ucits-etf-fund-fact-sheet-en-gb.pdf`; secondary OTC alias identity `https://stockanalysis.com/quote/otc/IHREF/`; S&P 500 definition `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached benchmark source links remain in the skill convention and the pre-existing batch record.
- Gaps/caveats: raw rolling 10-year endpoints and a current reconciled rolling 10-year issuer field are not disclosed in the current capture; the prior `147.80% / 9.50%` record remains a preserved source conflict; daily NAV observations sufficient for fund-level max drawdown/recovery were not captured; GBP listing currency versus USD return basis remains a material comparison caveat.

### AAXJ

- workflow: check-etf-performance
- execution_profile: scheduled-inline
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design
- entity_key: NASDAQ:AAXJ; official issuer page identifies iShares MSCI All Country Asia ex Japan ETF on NASDAQ.
- management_mode: passive-index; the official issuer objective and summary prospectus describe an index-tracking equity fund investing across developed and emerging Asia ex Japan.
- inception: 2008-08-13; expense_ratio: 0.72%; distribution_frequency: semi-annual.
- metric: official NAV Total Return, including reinvested distributions and fund expenses; return_currency: USD.
- issuer_benchmark: MSCI AC Asia ex Japan Index (Net); common benchmark is cached S&P 500 Total Return in USD with dividends reinvested.
- current_snapshot: NAV USD 116.34 as of 2026-08-25; closing price USD 114.34 as of 2026-08-24; current NAV TR YTD 22.87% as of 2026-08-24; holdings 941 as of 2026-08-24; 3-year standard deviation 17.20% and beta 0.88 as of 2026-07-31; P/E 21.73 and P/B 2.74 as of 2026-08-24.
- official_rolling: 2016-06-30 to 2026-06-30 cumulative 164.36% and annualized 10.21%, based on the issuer standardized performance table; raw endpoint NAV values were not disclosed, so review normalization is 100.00 to 264.36 over 10.00 years.
- official_annual_rows: 2021 -5.89%; 2022 -20.18%; 2023 4.94%; 2024 10.48%; 2025 32.09%, performance as of 2026-06-30. 2016-2020 annual rows were not disclosed in the reviewed current issuer table.
- common_window_calculation: 2021-2025 cumulative 15.04%, CAGR 2.84%, up/down 3/2; best 2025 +32.09%; least positive 2023 +4.94%; worst 2022 -20.18%; least bad down year 2021 -5.89%. Cached S&P 500 2021-2025 CAGR is 14.43%, so the arithmetic CAGR difference is -11.59 percentage points and is not called alpha.
- source_urls: issuer product/performance page https://www.ishares.com/us/products/239601/ishares-msci-all-country-asia-ex-japan-etf; factsheet https://www.ishares.com/us/literature/fact-sheet/aaxj-ishares-msci-all-country-asia-ex-japan-etf-fund-fact-sheet-en-us.pdf; summary prospectus https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-all-country-asia-ex-japan-etf-7-31.pdf; S&P definition https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- gaps: daily NAV observations sufficient for fund-level max drawdown and recovery were not captured; raw rolling endpoints and exact June-to-June S&P 500 TR were not disclosed in the reviewed evidence. Exposure snapshot is Taiwan 30.17%, China 23.12%, Korea South 23.08%, India 12.72%, and Information Technology 45.88% as of 2026-08-24.

### AIA

- workflow: check-etf-performance
- execution_profile: scheduled-inline
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design
- entity_key: NASDAQ:AIA; official issuer page identifies iShares Asia 50 ETF on NASDAQ.
- management_mode: passive-index; the official issuer objective and prospectus describe an indexing approach tracking the S&P Asia 50 Capped Index.
- inception: 2007-11-13; expense_ratio: 0.50%; distribution_frequency: semi-annual; asset_class: Equity.
- metric: official NAV Total Return, including reinvested distributions and fund expenses; return_currency: USD.
- issuer_benchmark: S&P Asia 50 Capped Index (Net); common benchmark is cached S&P 500 Total Return in USD with dividends reinvested.
- current_snapshot: NAV USD 139.82 and closing price USD 139.38 as of 2026-08-27; current NAV TR YTD 43.01% as of 2026-08-26; holdings 53 as of 2026-08-27; 3-year standard deviation 21.43% and beta 1.05 as of 2026-07-31; P/E 21.44 and P/B 2.75 as of 2026-08-27.
- official_rolling: 2016-06-30 to 2026-06-30 cumulative 298.99% and annualized 14.84%, based on the issuer standardized performance table; raw endpoint NAV values were not disclosed, so review normalization is 100.00 to 398.99 over 10.00 years.
- official_annual_rows: 2021 -10.75%; 2022 -24.07%; 2023 4.84%; 2024 20.42%; 2025 47.01%, performance as of 2026-06-30.
- common_window_calculation: 2021-2025 cumulative 25.77%, CAGR 4.69%, up/down 3/2; best 2025 +47.01%; least positive 2023 +4.84%; worst 2022 -24.07%; least bad down year 2021 -10.75%. Cached S&P 500 2021-2025 CAGR is 14.43%, so the arithmetic CAGR difference is -9.73 percentage points and is not called alpha.
- source_urls: issuer product/performance page https://www.ishares.com/us/products/239730/ishares-asia-50-etf; factsheet https://www.ishares.com/us/literature/fact-sheet/aia-ishares-asia-50-etf-fund-fact-sheet-en-us.pdf; prospectus https://www.ishares.com/us/literature/prospectus/p-ishares-asia-50-etf-3-31.pdf; S&P definition https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- gaps: daily NAV observations sufficient for fund-level max drawdown and recovery were not captured; raw rolling endpoints and exact June-to-June S&P 500 TR were not disclosed in the reviewed evidence. Exposure snapshot is Taiwan 37.10%, Korea South 27.44%, China 24.65%, Singapore 5.82%, Hong Kong 4.77%, and Information Technology 57.06% as of 2026-08-27.

## Active-management classification

- `FESM`: owner page classification `active-equity-long-only`; it is ranked on raw NAV TR CAGR only.
- `DFAS`: owner page classification `active-equity-long-only`; it is ranked on raw NAV TR CAGR only.
- For both active rows: `active_process` is `systematic-active`; `management_benchmark` is the official `Russell 2000`; `track_record` is `provisional` because predecessor history is included; `management_evidence` is `insufficient` for this aggregate and `risk_evidence` is `not-verified`.
- The aggregate records the official strategy-aligned benchmark as classification context but intentionally does not calculate excess CAGR, hit rate, or risk-adjusted evidence. It therefore makes no claim of manager skill and does not call arithmetic return differences `alpha`.

## Unresolved gaps and source ownership

- Some older owner pages do not expose an explicit annual-row as-of date or return currency; those cells remain `not disclosed` in the ledger.
- Annual inputs are rounded to the precision shown by the issuer/page. Calculations are reproducible from the displayed rows but may differ slightly from an issuer's raw-endpoint calculation.
- Current YTD, rolling endpoints, market price, distributions, drawdown, and recovery were deliberately excluded from the common-window rank.
- Numeric source of truth remains each linked owner page under `wiki/analysis/performance/`; this dated batch records the selected column, raw Top 50 inputs, calculations, caveats, and gaps.
