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

### ENZL

- workflow: check-etf-performance
- execution_profile: scheduled-inline
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design
- entity_key: NASDAQ:ENZL; official issuer page identifies iShares MSCI New Zealand ETF on NASDAQ.
- management_mode: passive-index; the official issuer objective and summary prospectus describe an index-tracking equity fund.
- inception: 2010-09-01; expense_ratio: 0.50%; distribution_frequency: semi-annual; asset_class: Equity.
- metric: official NAV Total Return, including reinvested distributions and fund expenses; return_currency: USD.
- issuer_benchmark: MSCI New Zealand All Cap Top 25 Capped Index (Net); the issuer states that the benchmark changed from MSCI New Zealand IMI 25/50 Index (Net) on 2024-09-03. Common benchmark is cached S&P 500 Total Return in USD with dividends reinvested.
- current_snapshot: NAV USD 48.36 and closing price USD 48.56 as of 2026-08-27; current NAV TR YTD 8.69% as of 2026-08-26; holdings 26 as of 2026-08-27; 3-year standard deviation 15.88% and beta 0.83 as of 2026-07-31; P/E 23.80 and P/B 1.55 as of 2026-08-26.
- official_rolling: 2016-06-30 to 2026-06-30 cumulative 38.78% and annualized 3.33%, based on the issuer standardized performance table; raw endpoint NAV values were not disclosed, so review normalization is 100.00 to 138.78 over 10.00 years.
- official_annual_rows: 2021 -10.86% / benchmark -10.39%; 2022 -16.63% / -16.49%; 2023 3.53% / 4.47%; 2024 -4.55% / -4.01%; 2025 1.68% / 1.85%, performance as of 2026-06-30. 2016-2020 annual rows were not disclosed in the reviewed current issuer table.
- common_window_calculation: 2021-2025 cumulative -25.33%, CAGR -5.67%, up/down 2/3; best 2023 +3.53%; least positive 2025 +1.68%; worst 2022 -16.63%; least bad down year 2024 -4.55%. Cached S&P 500 2021-2025 CAGR is 14.43%, so the arithmetic CAGR difference is -20.10 percentage points and is not called alpha.
- source_urls: issuer product/performance page https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239672&seoSlug=ishares-msci-new-zealand-capped-etf; factsheet https://www.ishares.com/us/literature/fact-sheet/enzl-ishares-msci-new-zealand-etf-fund-fact-sheet-en-us.pdf; summary prospectus https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-new-zealand-capped-etf-8-31.pdf; annual report https://www.blackrock.com/us/individual/literature/annual-report/ar-enzl-en.pdf; S&P definition https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- gaps: daily NAV observations sufficient for fund-level max drawdown and recovery were not captured; raw rolling endpoints and exact June-to-June S&P 500 TR were not disclosed in the reviewed evidence; benchmark splice remains a comparability caveat. Current sector snapshot is Health Care 31.75%, Industrials 22.84%, Financials 12.99%, Real Estate 12.17%, and Utilities 11.89% as of 2026-08-26.

### INDY

- workflow: check-etf-performance
- execution_profile: scheduled-inline
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design
- entity_key: NASDAQ:INDY; official issuer page identifies iShares India 50 ETF on NASDAQ.
- management_mode: passive-index; the official issuer objective and summary prospectus describe an index-tracking equity fund tracking the Nifty 50 Index.
- inception: 2009-11-18; expense_ratio: 0.65%; distribution_frequency: semi-annual; asset_class: Equity.
- metric: official NAV Total Return, including reinvested distributions and fund expenses; return_currency: USD.
- issuer_benchmark: Nifty 50 Index; common benchmark is cached S&P 500 Total Return in USD with dividends reinvested.
- current_snapshot: NAV USD 43.57 and closing price USD 43.58 as of 2026-08-27; current NAV TR YTD -11.36% as of 2026-08-26; holdings 50 as of 2026-08-27; 3-year standard deviation 13.32% and beta 0.37 as of 2026-07-31; P/E 21.64 and P/B 3.03 as of 2026-08-27.
- official_rolling: 2016-06-30 to 2026-06-30 cumulative 90.75% and annualized 6.67%, based on the issuer standardized performance table; raw endpoint NAV values were not disclosed, so review normalization is 100.00 to 190.75 over 10.00 years.
- official_annual_rows: 2021 19.28%; 2022 -7.86%; 2023 17.05%; 2024 4.02%; 2025 4.42%, performance as of 2026-06-30. The additional 2020 row is 10.67% from the dated BlackRock factsheet; 2016-2019 annual rows are not disclosed in the reviewed current capture.
- common_window_calculation: 2021-2025 cumulative 39.73%, CAGR 6.92%, up/down 4/1; best 2021 +19.28%; least positive 2024 +4.02%; worst and only down year 2022 -7.86%. Cached S&P 500 2021-2025 CAGR is 14.43%, so the arithmetic CAGR difference is -7.51 percentage points and is not called alpha. The 2020-2025 six-row series compounds to 54.64% / 7.54% CAGR with 5/1 up/down years.
- current_month_end: issuer standardized YTD -11.49% as of 2026-06-30; kept separate from current product-page YTD -11.36% as of 2026-08-26.
- source_quality_choice: canonical INDY direct product page was selected over a separate overview endpoint that showed YTD -7.61% and holdings 165 as of 2026-08-25. The conflict is preserved and not averaged.
- source_urls: issuer product/performance page https://www.ishares.com/us/products/239758/ishares-india-50-etf; factsheet https://www.ishares.com/us/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-us.pdf; summary prospectus https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-india-50-etf-3-31.pdf; 2020 factsheet https://www.blackrock.com/americas-offshore/en/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-lm.pdf; S&P definition https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- gaps: daily NAV observations sufficient for fund-level max drawdown and recovery were not captured; raw rolling endpoints and 2016-2019 annual rows are not disclosed; the separate overview endpoint conflict is retained above. Current sector snapshot is Financials 36.04%, Consumer Discretionary 11.95%, Energy 9.48%, Industrials 8.60%, and Information Technology 8.13% as of 2026-08-27.

### MCHI

- workflow: check-etf-performance
- execution_profile: scheduled-inline
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design
- entity_key: NASDAQ:MCHI; official issuer page identifies iShares MSCI China ETF on NASDAQ.
- management_mode: passive-index; the official issuer objective and summary prospectus describe an index-tracking equity fund tracking the MSCI China Index.
- inception: 2011-03-29; expense_ratio: 0.59%; distribution_frequency: semi-annual; asset_class: Equity.
- metric: official NAV Total Return, including reinvested distributions and fund expenses; return_currency: USD.
- issuer_benchmark: MSCI China Index (Net); common benchmark is cached S&P 500 Total Return in USD with dividends reinvested.
- current_snapshot: NAV USD 55.02 and closing price USD 54.90 as of 2026-08-27; current NAV TR YTD -7.93% as of 2026-08-26; holdings 575 as of 2026-08-27; 3-year standard deviation 21.63% and beta 0.36 as of 2026-07-31; P/E 13.68 and P/B 1.66 as of 2026-08-26.
- official_rolling: 2016-06-30 to 2026-06-30 cumulative 45.52% and annualized 3.82%, based on the issuer standardized performance table; raw endpoint NAV values were not disclosed, so review normalization is 100.00 to 145.52 over 10.00 years.
- official_annual_rows: 2021 -22.38% / benchmark -21.72%; 2022 -22.53% / -21.93%; 2023 -11.07% / -11.20%; 2024 18.06% / 19.42%; 2025 31.07% / 31.17%, performance as of 2026-06-30. 2016-2020 annual rows were not disclosed in the reviewed current issuer table.
- common_window_calculation: 2021-2025 cumulative -17.25%, CAGR -3.72%, up/down 2/3; best 2025 +31.07%; least positive 2024 +18.06%; worst 2022 -22.53%; least bad down year 2023 -11.07%. Cached S&P 500 2021-2025 CAGR is 14.43%, so the arithmetic CAGR difference is -18.14 percentage points and is not called alpha.
- current_month_end: issuer standardized YTD -14.65% as of 2026-06-30; kept separate from current product-page YTD -7.93% as of 2026-08-26.
- source_urls: issuer product/performance page https://www.ishares.com/us/products/239619/ishares-msci-china-etf; factsheet https://www.ishares.com/us/literature/fact-sheet/mchi-ishares-msci-china-etf-fund-fact-sheet-en-us.pdf; summary prospectus https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-etf-8-31.pdf; annual financial statements https://www.ishares.com/us/literature/annual-financial-statements/afs-ishares-trust-msci-country-etfs-book1-08-31-en.pdf; S&P definition https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- gaps: daily NAV observations sufficient for fund-level max drawdown and recovery were not captured; raw rolling endpoints and 2016-2020 annual rows are not disclosed. Current sector snapshot is Consumer Discretionary 24.12%, Financials 19.78%, Communication 17.80%, Information Technology 10.91%, and Health Care 5.86% as of 2026-08-26. Index futures use may offset cash/receivables but is not strategy-defining.

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

### BSVO

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Evidence identity: official Bridgeway product page identifies `EA Bridgeway Omni Small-Cap Value ETF`, ticker `BSVO`, exchange `Nasdaq`, and `Fund Type: Active`; the SEC annual report identifies the same Nasdaq-listed fund.
- `management_mode: active-equity-long-only`; the official objective is long-term total return primarily through capital appreciation from a broad and diverse group of U.S. small-cap value stocks.
- `active_process: systematic-active`; official materials describe a statistical and evidence-based process using market and financial data, value measures, market-cap weighting and risk constraints. The product page also uses “passive, asset-class investing” to describe implementation, but no specific index is tracked.
- `management_benchmark: Russell 2000 Value Total Return Index`; the official annual report identifies this benchmark as the measure of the Fund’s investment strategy and universe.
- `track_record: established`; the official table includes predecessor mutual-fund history from 2010-12-31, while live ETF listing began 2023-03-10 and the March 2023 reorganization must remain disclosed.
- `management_evidence: positive return-only`; official fiscal-year benchmark comparisons as of `2025-06-30` are mixed by horizon: 1-year `1.39%` versus `5.54%` (`-4.15 pp`), 5-year annualized `17.45%` versus `12.47%` (`+4.98 pp`), and 10-year annualized `7.14%` versus `6.72%` (`+0.42 pp`). These are return comparisons, not alpha.
- `risk_evidence: not-verified`; compatible daily NAV observations sufficient for reproducible maximum drawdown and recovery were not captured.
- Return definition: official `NAV Total Return`, USD, with the issuer’s published return convention; current periods under one year are cumulative and multi-year periods are annualized. The common `S&P 500 Total Return` reference is USD with dividends reinvested, but no synchronized current comparison was calculated.
- Current official month-end fields as of `2026-07-31`: NAV YTD `25.66%`, rolling 1-year `44.04%`, rolling 3-year annualized `16.32%`, rolling 5-year annualized `11.89%`, rolling 10-year annualized `11.04%`, and since predecessor inception annualized `10.45%`.
- Current product-page snapshot as of `2026-08-28`: NAV `US$29.50`, market price `US$29.51`, premium/discount `+0.03%`, AUM `US$2,445.82 million`, bid/ask spread `0.07%`, and current expense ratio `0.45%`.
- Source conflict: the reviewed 2024 SEC summary prospectus reports `0.47%` total annual fund operating expenses; the older value is retained with its source date and is not averaged with the current product-page value.
- Calendar-year evidence: no complete annual calendar-row table was disclosed in the reviewed current product-page and SEC source set, so best/worst year, up/down count, calendar CAGR and annual hit rate are `ไม่พบข้อมูลที่ยืนยันได้` and are not inferred from rolling figures.
- Current-to-benchmark reconciliation: current `2026-07-31` fund fields and `2025-06-30` benchmark snapshot have different as-of dates; no excess return was calculated for the current fields. The S&P 500 common reference is not substituted for the strategy-aligned Russell 2000 Value benchmark.
- Source URLs: product page `https://bridgewayetfs.com/bsvo/`; SEC summary prospectus `https://www.sec.gov/Archives/edgar/data/1592900/000159290024002170/eabridgewayomnismall-capva.htm`; SEC annual shareholder report `https://www.sec.gov/Archives/edgar/data/1592900/000159290025002595/ck0001592900-20250630.htm`; SEC SAI `https://www.sec.gov/Archives/edgar/data/1592900/000159290025001783/bridgewaysaibbluandbsvo.htm`.
- Pre-save checklist: PASS. Identity/exchange, active classification, NAV/TR basis, USD currency, distributions/expense caveat, current and fiscal as-of dates, predecessor-history caveat, benchmark alignment, displayed-value arithmetic, source links, unresolved gaps, and graph links were checked locally before writing.
- Proposed durable contents: update `wiki/analysis/performance/ETF_NASDAQ_BSVO Performance.md` with the exact classification values `active-equity-long-only`, `systematic-active`, `established`, `positive return-only`, and `not-verified`; refresh the current product snapshot to 2026-08-28; point `source_batch` to this file; retain the 2026-07-31 NAV table, 2025-06-30 Russell 2000 Value comparison, source URLs and disclosed gaps; append one `etf-performance` bullet to `log.md`. No region/index navigation change is proposed because the USA primary-region links and coverage remain unchanged.
- Proposed log entry: `- etf-performance: Refreshed [[ETF_NASDAQ_BSVO Performance]] and extended [[ETF_performance_sources_2026-08-28]]. Scheduled-inline local pre-save returned PASS; official rolling 10-year NAV TR is 11.04% as of 2026-07-31, current official NAV TR YTD is 25.66% as of 2026-07-31, and 2025-06-30 Russell 2000 Value evidence is mixed (-4.15 pp / +4.98 pp / +0.42 pp across 1Y/5Y/10Y); BSVO remains an active systematic long-only U.S. small-cap value ETF with predecessor history and daily NAV drawdown/recovery gaps disclosed.`
- `pre_save_result: PASS`

### ECNS

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Evidence identity: the official iShares product page identifies `iShares MSCI China Small-Cap ETF`, ticker `ECNS`, `NYSE Arca`, inception `2010-09-28`, asset class Equity, semi-annual distributions, and `266` holdings as of `2026-08-27`; latest official NAV is `$29.61` and closing market price is `$29.36` as of `2026-08-27`.
- `management_mode: passive-index`; the current official prospectus states that ECNS seeks to track the investment results of the `MSCI China Small Cap Index`, composed of small-capitalization Chinese equities available to international investors. The reviewed strategy is passive and not derivative-heavy.
- `tracked_index: MSCI China Small Cap Index (Net)`; `benchmark: S&P 500 Total Return` is only a common USD reference with dividends reinvested. Return basis is official `NAV Total Return` in `USD`, including reinvested distributions and after fund expenses; expense ratio is `0.59%`.
- Current official fields: NAV Total Return YTD `-9.18%` as of `2026-08-26`; 30-day SEC yield `3.57%` and 12-month trailing yield `6.57%` as of `2026-07-31`; P/E `11.66`, P/B `0.90`, net assets `$66,617,297`, premium/discount `-0.84%`, and `266` holdings as of `2026-08-27`; 1-day NAV change was `+$0.07 (+0.25%)` as of `2026-08-27`.
- Official risk snapshot: 3-year standard deviation `26.02%` and beta `0.51` as of `2026-07-31`; sector exposure as of `2026-08-27` was Health Care `22.79%`, Industrials `14.44%`, Information Technology `11.42%`, Consumer Discretionary `11.23%`, Materials `9.78%`, Real Estate `8.35%`, Communication `8.29%`, Consumer Staples `5.20%`, Financials `4.26%`, Utilities `2.06%`, Energy `1.72%`, and cash/derivatives `0.46%`.
- Official complete calendar NAV TR rows from the current factsheet/product page, through `2025-12-31`: `2021 3.10%`, `2022 -24.77%`, `2023 -23.28%`, `2024 6.94%`, `2025 36.42%`; no `*` or `†` markers. The corresponding official MSCI index rows are `-6.29%`, `-24.80%`, `-24.86%`, `6.75%`, and `35.27%`.
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`; NAV TR CAGR `1.05%`. Raw NAV endpoints and issuer cumulative return were not disclosed, so normalized endpoint and cumulative-return calculations are not asserted.
- Calculations from displayed rows: ECNS 2021-2025 cumulative `-13.19%`, CAGR `-2.79%`, up/down years `3 / 2`, best `2025 +36.42%`, least positive `2021 +3.10%`, worst `2022 -24.77%`, and least bad down year `2023 -23.28%`. Tracked-index cumulative/CAGR are `-23.54%` / `-5.23%`; arithmetic fund-minus-index CAGR gap is `+2.44 pp` and is not called alpha. Cached S&P 500 TR for complete calendar years `2016-2025` is cumulative `96.17%`, CAGR `14.43%`, giving an arithmetic ECNS gap of `-17.22 pp`; this is only a common reference comparison.
- Daily NAV TR observations sufficient for reproducible maximum drawdown and recovery were not captured: `ไม่พบข้อมูลที่ยืนยันได้`; no 52-week price drawdown or secondary price proxy is substituted for NAV TR. Key gaps/risks retained are China single-country and small-cap exposure, domestic demand/property, policy/geopolitical, FX, liquidity, systematic-fair-value and sector-concentration sensitivity.
- Source URLs: product `https://www.ishares.com/us/products/239620/ishares-msci-china-etf`; factsheet `https://www.ishares.com/us/literature/fact-sheet/ecns-ishares-msci-china-small-cap-etf-fund-fact-sheet-en-us.pdf`; prospectus `https://www.ishares.com/us/literature/prospectus/p-ishares-trust-emerging-8-31.pdf`; common-reference S&P page `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`. The S&P 500 2016-2025 rows reuse the vault cache convention without a new search, with USD total-return basis, window `2016-2025`, and reference as-of `2025-12-31`.
- Complete local pre-save checklist: PASS. Identity/exchange/fund/inception, passive eligibility, tracked index, return basis/currency, fee and distribution treatment, current and rolling as-of dates, annual rows and markers, S&P cache window, calculations, source links, unresolved gaps, Thai-first durable sections, canonical path, China region assignment and graph links were checked before writing.
- Proposed durable contents: rewrite `wiki/analysis/performance/ETF_NYSE_ARCA_ECNS Performance.md` with refreshed frontmatter and sections `Bottom line`, `Performance check`, `Up years / Down years`, `Risk read-through`, and `Sources`; update the current ECNS rows in `wiki/analysis/comparisons/China ETF.md` and `wiki/analysis/performance/ETF Performance Index.md` to current YTD `-9.18%`; append one `etf-performance` bullet to `log.md`; retain the breadcrumb `[[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]`.
- Proposed log entry: `- etf-performance: Refreshed [[ETF_NYSE_ARCA_ECNS Performance]], [[China ETF]], [[ETF Performance Index]], and extended [[ETF_performance_sources_2026-08-28]]. Scheduled-inline local pre-save returned PASS; official rolling 10-year NAV TR is 1.05% as of 2026-06-30, 2021-2025 CAGR is -2.79%, and current official NAV TR YTD is -9.18% as of 2026-08-26; ECNS remains a passive China small-cap ETF with high volatility, domestic-demand/property/liquidity/FX sensitivity and daily NAV drawdown/recovery gap disclosed.`
- `pre_save_result: PASS`

### DVYA

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Evidence identity: the official iShares product page identifies `iShares Asia/Pacific Dividend ETF`, ticker `DVYA`, `NYSE Arca`, inception `2012-02-23`, asset class Equity, quarterly distributions, and `50` holdings as of `2026-08-26`; latest official NAV is `$52.14` and closing market price is `$52.11` as of `2026-08-26`.
- `management_mode: passive-index`; the official summary prospectus states that DVYA uses an indexing approach to seek results corresponding to the `Dow Jones Asia/Pacific Select Dividend 50 Index (Net)`, a 50-stock developed Asia-Pacific high-dividend index. Futures/options/swaps/cash may be used for implementation within the disclosed limits; the reviewed strategy is not derivative-heavy.
- `tracked_index: Dow Jones Asia/Pacific Select Dividend 50 Index (Net)`; `benchmark: S&P 500 Total Return` is only a common USD reference with dividends reinvested. Return basis is official `NAV Total Return` in `USD`, including reinvested distributions and after fund expenses; expense ratio is `0.49%`.
- Current official fields: NAV Total Return YTD `21.45%` as of `2026-08-25`; 30-day SEC yield `4.55%` and 12-month trailing yield `4.37%` as of `2026-07-31`; P/E `16.12`, P/B `1.14`, net assets `$73,002,539`, and premium/discount `-0.07%` as of `2026-08-26`.
- Official risk/exposure snapshot: 3-year standard deviation `13.97%` and beta `0.51` as of `2026-07-31`; country exposure Australia `42.15%`, Hong Kong `24.39%`, Singapore `19.07%`, Japan `8.88%`, New Zealand `3.95%`, other `0.90%`, and cash/derivatives `0.66%`; largest sectors Financials `32.85%` and Materials `16.13%`, all as of `2026-08-26`.
- Official complete calendar NAV TR rows from the current product page/factsheet, through `2025-12-31`: `2021 4.23%`, `2022 -2.12%`, `2023 13.96%`, `2024 5.99%`, `2025 30.16%`; no `*` or `†` markers. The issuer notes that the underlying index changed from the Dow Jones Asia/Pacific Select Dividend 30 Index to the Select Dividend 50 Index on `2020-06-22`.
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`, NAV TR CAGR `6.90%`, official cumulative return `94.89%`; normalized endpoints are `100.00` and `194.89` over `10.00` years. Formula: `(End TR / Start TR)^(1 / Years) - 1`; raw daily NAV TR endpoints were not disclosed.
- Calculations from displayed rows: 2021-2025 cumulative `60.39%`, CAGR `9.91%`, up/down years `4 / 1`, best `2025 +30.16%`, least positive `2024 +5.99%`, worst `2022 -2.12%`. Cached S&P 500 TR for complete calendar years `2016-2025` is cumulative `96.17%`, CAGR `14.43%`, with arithmetic CAGR gap `-4.52 pp`; this is not called alpha. Average of the latest four official distributions captured is `$0.559817` and is not used as a return substitute.
- Daily NAV TR observations sufficient for reproducible maximum drawdown and recovery were not captured: `ไม่พบข้อมูลที่ยืนยันได้`; no secondary price proxy is mixed into NAV TR analysis. Key risks/gaps retained: Australia/Hong Kong/Singapore and financials/materials concentration, FX, commodity/materials, country/policy and liquidity sensitivity; current daily drawdown/recovery remains unresolved.
- Source URLs: product `https://www.ishares.com/us/products/239443/ishares-asiapacific-dividend-etf`; factsheet `https://www.ishares.com/us/literature/fact-sheet/dvya-ishares-asia-pacific-dividend-etf-fund-fact-sheet-en-us.pdf`; summary prospectus `https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-asia-pacific-dividend-etf-4-30.pdf`; common-reference S&P page `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`. The S&P 500 2016-2025 rows reuse the vault cache convention without a new search, with USD total-return basis, window `2016-2025`, and reference as-of `2025-12-31`.
- Complete local pre-save checklist: PASS. Identity/exchange/fund/inception, passive eligibility, tracked index, return basis/currency, fee and distribution treatment, current and rolling as-of dates, annual rows and markers, index-change note, S&P cache window, calculations, source links, unresolved gaps, Thai-first durable sections, canonical path, region assignment and graph links were checked before writing.
- Proposed durable contents: rewrite `wiki/analysis/performance/ETF_NYSE_ARCA_DVYA Performance.md` with the refreshed frontmatter and sections `Bottom line`, `Performance check`, `Up years / Down years`, `Risk read-through`, and `Sources`; update the current DVYA row in `wiki/analysis/comparisons/Asia-Pacific ETF.md` and `wiki/analysis/performance/ETF Performance Index.md` to current YTD `21.45%`; append one `etf-performance` bullet to `log.md`; retain the shared source-batch link and breadcrumb `[[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]`.
- Proposed log entry: `- etf-performance: Refreshed [[ETF_NYSE_ARCA_DVYA Performance]], [[Asia-Pacific ETF]], [[ETF Performance Index]], and extended [[ETF_performance_sources_2026-08-28]]. Scheduled-inline local pre-save returned PASS; official rolling 10-year NAV TR is 6.90% as of 2026-06-30, 2021-2025 CAGR is 9.91%, and current official NAV TR YTD is 21.45% as of 2026-08-25; DVYA remains a passive developed Asia-Pacific dividend ETF with FX/commodity/financials concentration and daily NAV drawdown/recovery gap disclosed.`
- `pre_save_result: PASS`

### ASHR

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Evidence identity: the official DWS Q2 2026 factsheet identifies `Xtrackers Harvest CSI 300 China A-Shares ETF`, ticker `ASHR`, NYSE listing, inception `2013-11-05`, `288` holdings and net assets `$1,644,586,990.45`, all as of `2026-06-30`.
- `management_mode: passive-index`; the October 1, 2025 official prospectus states that the fund uses a passive/indexing approach to seek results corresponding to the `CSI 300 Index`, with at least 80% exposure to index components or qualifying exposure instruments. Derivatives are permitted for implementation and risk management; the reviewed strategy is not derivative-heavy.
- `tracked_index: CSI 300 Index`; the official factsheet defines it as 300 large- and mid-cap China A-share stocks listed on Shenzhen or Shanghai. `benchmark: S&P 500 Total Return` remains only a common USD reference with dividends reinvested.
- `expense_ratio: 0.65%` gross and net, per the Q2 2026 factsheet and October 2025 prospectus. Return basis is official NAV Total Return in USD; issuer index returns are gross of fees.
- Official Q2 2026 NAV TR fields as of `2026-06-30`: 3-month `13.88%`, 1-year `35.88%`, 3-year annualized `13.23%`, 5-year annualized `-0.51%`, 10-year annualized `5.84%`, and since ETF inception `6.30%`.
- Official Q2 2026 CSI 300 Index comparison as of `2026-06-30`: 3-month `14.68%`, 1-year `36.47%`, 3-year annualized `14.21%`, 5-year annualized `0.30%`, 10-year annualized `6.65%`, and since ETF inception `7.24%`. Fund-minus-index differences are `-0.80 pp`, `-0.59 pp`, `-0.98 pp`, `-0.81 pp`, `-0.81 pp`, and `-0.94 pp`, respectively; these are tracking/fee comparisons, not alpha.
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`, exactly `10.00` elapsed years, NAV TR CAGR `5.84%`. Raw NAV endpoints and issuer cumulative return were not disclosed; review normalization is `100.00 × (1 + 5.84%)^10.00 = approximately 176.40`, with calculated cumulative return approximately `76.40%`.
- Official calendar NAV TR rows from the October 2025 prospectus, performance through `2024-12-31`: `2016 -15.06%`, `2017 31.81%`, `2018 -28.05%`, `2019 35.57%`, `2020 37.42%`, `2021 -2.17%`, `2022 -26.98%`, `2023 -13.07%`, and `2024 12.55%`. The current Q2 2026 factsheet did not disclose a 2025 calendar NAV row or current YTD field.
- Calculations from displayed complete rows: 2016-2024 cumulative `4.89%`, CAGR `0.53%` over `9.00` years, up/down years `4 / 5`, best `2020 +37.42%`, least positive `2024 +12.55%`, worst `2018 -28.05%`, and least bad down year `2021 -2.17%`. The 2021-2024 subset compounds to `-30.11%`, CAGR `-8.57%`; cached S&P 500 TR for the same 2021-2024 rows is `66.41%`, CAGR `13.58%`, so the arithmetic difference is approximately `-22.15 pp` and is not called alpha.
- Current YTD: `ไม่พบข้อมูลที่ยืนยันได้`; the reviewed current official factsheet presents a 3-month period ending 2026-06-30 but does not label a year-to-date return, and no later official current performance field was captured.
- Risk and gaps: China single-country/A-share, Stock Connect/QFI, government restrictions, currency, liquidity, policy/geopolitical and sector-concentration risks remain relevant. Daily NAV observations sufficient for reproducible maximum drawdown and recovery were not captured. The 2025 calendar row, current YTD, raw 10-year endpoints and current NAV/market-price snapshot remain not disclosed in the reviewed evidence.
- Source URLs: Q2 2026 factsheet `https://etf.dws.com/download/asset/e73aaa93-92c6-4a51-9233-38ccb329e09b`; October 1, 2025 prospectus `https://etf.dws.com/download/asset/ce51b065-fc18-496f-9b88-8996a37d16b3`; S&P 500 reference `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P 500 2016-2025 rows were reused under the vault convention without a new search.
- Pre-save checklist: PASS. Identity/exchange, passive classification, tracked index, NAV/TR basis, USD currency, fee treatment, distribution inclusion, current rolling as-of date, 10-year endpoint convention, annual-row completeness, S&P cache window, calculation labels, source links, unresolved gaps, and graph links were checked locally before writing.
- Proposed durable contents: update `wiki/analysis/performance/ETF_NYSE_ARCA_ASHR Performance.md` with `management_mode: passive-index`, `updated: 2026-08-28`, `source_batch: raw/imports/ETF_performance_sources_2026-08-28.md`, `return_currency: USD`, refreshed Q2 2026 rolling fields, official CSI 300 comparison, and retained 2016-2024 calendar evidence/gaps; append one `etf-performance` bullet to `log.md`. No region/index navigation change is proposed because ASHR remains the China primary-region page and its coverage classification is unchanged.
- Proposed log entry: `- etf-performance: Refreshed [[ETF_NYSE_ARCA_ASHR Performance]] and extended [[ETF_performance_sources_2026-08-28]]. Scheduled-inline local pre-save returned PASS; official rolling 10-year NAV TR is 5.84% and 1-year NAV TR is 35.88% as of 2026-06-30, while current YTD remains not disclosed; ASHR remains a passive CSI 300 China A-share ETF with tracking/fee differences, China access risks, and daily NAV drawdown/recovery gaps disclosed.`
- `pre_save_result: PASS`

### ASHS

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Evidence identity: the official DWS Q1 2026 factsheet identifies `Xtrackers Harvest CSI 500 China A-Shares Small Cap ETF`, ticker `ASHS`, NYSE listing, inception `2014-05-20`, `497` holdings and net assets `$38,263,257`, all as of `2026-03-31`.
- `management_mode: passive-index`; the October 1, 2025 official prospectus states that the fund uses a passive/indexing approach to seek results corresponding to the `CSI 500 Index`, an index of 500 predominantly small-cap China A-share companies. The fund may use Stock Connect, QFI and permitted derivatives for implementation; the reviewed strategy is not derivative-heavy.
- `tracked_index: CSI 500 Index`; the official Q1 factsheet identifies CSI as provider and 500 constituents. `benchmark: S&P 500 Total Return` remains only a common USD reference with dividends reinvested.
- `expense_ratio: 0.65%` gross and net, per the Q1 2026 factsheet and October 2025 prospectus. Return basis is official NAV Total Return in USD; issuer index returns are gross of fees.
- Latest official NAV TR fields located, as of `2026-03-31`: 3-month `3.36%`, 1-year `38.14%`, 3-year annualized `7.16%`, 5-year annualized `3.79%`, 10-year annualized `1.96%`, and since ETF inception `5.23%`. No newer official current YTD field was captured by `2026-08-28`.
- Official CSI 500 Index comparison as of `2026-03-31`: 3-month `3.29%`, 1-year `38.41%`, 3-year annualized `7.80%`, 5-year annualized `4.54%`, 10-year annualized `2.74%`, and since ETF inception `6.53%`. Fund-minus-index differences are `+0.07 pp`, `-0.27 pp`, `-0.64 pp`, `-0.75 pp`, `-0.78 pp`, and `-1.30 pp`, respectively; these are tracking/fee comparisons, not alpha.
- Official rolling 10-year window: `2016-03-31` to `2026-03-31`, exactly `10.00` elapsed years, NAV TR CAGR `1.96%`. Raw NAV endpoints and issuer cumulative return were not disclosed; review calculation is `100.00 × (1 + 1.96%)^10.00 = approximately 121.42`, or approximately `21.42%` cumulative.
- Annual-year evidence: the reviewed Q1 2026 factsheet provides standardized rolling periods but no readable complete annual NAV/index rows for `2016-2025`; the 2025 annual report provides a growth-of-$10,000 chart rather than a complete annual return table. No chart-derived proxy or third-party annual series is substituted, so calendar CAGR, up/down count, best/worst year and exact 2021-2025 spread remain `ไม่พบข้อมูลที่ยืนยันได้`.
- Current YTD: latest official reported value is `3.36%` as of `2026-03-31`; the reviewed source set did not provide a Q2 2026 factsheet or a `2026-06-30` YTD field, so no newer value is inferred.
- Risk and gaps: China A-share/small-cap, Stock Connect/QFI, government restrictions, currency, custody/tax, liquidity, policy/geopolitical and sector-concentration risks remain relevant. Daily NAV observations sufficient for reproducible maximum drawdown and recovery were not captured. Current NAV/market-price snapshot, Q2 2026 YTD and complete annual return rows remain not disclosed in the reviewed evidence.
- Source URLs: Q1 2026 factsheet `https://etf.dws.com/download/asset/1bfed1b5-c933-4199-bdcc-30b0ed651740`; October 1, 2025 summary prospectus `https://etf.dws.com/download/asset/7a928aa7-d2cc-490b-a3de-fb6144afc0cb`; October 1, 2025 combined prospectus `https://etf.dws.com/download/asset/ce51b065-fc18-496f-9b88-8996a37d16b3`; annual shareholder report `https://etf.dws.com/download/asset/cd4f449d-b77e-49df-8486-46f48efe43cc`; S&P 500 reference `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P 500 2016-2025 rows were reused under the vault convention without a new search.
- Pre-save checklist: PASS. Identity/exchange, passive classification, tracked index, NAV/TR basis, USD currency, fee treatment, distribution inclusion, latest-source date, 10-year endpoint convention, annual-row gap, S&P cache window, calculation labels, source links, unresolved gaps, and graph links were checked locally before writing.
- Proposed durable contents: update `wiki/analysis/performance/ETF_NYSE_ARCA_ASHS Performance.md` with `management_mode: passive-index`, `updated: 2026-08-28`, `source_batch: raw/imports/ETF_performance_sources_2026-08-28.md`, `return_currency: USD`, the latest Q1 2026 rolling fields and CSI 500 comparison, and retained annual-row/YTD gaps; append one `etf-performance` bullet to `log.md`. No region/index navigation change is proposed because ASHS remains the China primary-region page and its coverage classification is unchanged.
- Proposed log entry: `- etf-performance: Refreshed [[ETF_NYSE_ARCA_ASHS Performance]] and extended [[ETF_performance_sources_2026-08-28]]. Scheduled-inline local pre-save returned PASS; latest official rolling 10-year NAV TR is 1.96% and 1-year NAV TR is 38.14% as of 2026-03-31, while current YTD remains 3.36% only at that date; ASHS remains a passive CSI 500 China A-share small-cap ETF with current-source and daily NAV drawdown/recovery gaps disclosed.`
- `pre_save_result: PASS`

### CNXT

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Evidence identity: the official VanEck factsheet identifies `VanEck ChiNext Innovators ETF`, ticker `CNXT`, exchange `NYSE Arca`, index ticker `SZ988107`, inception `2014-07-23`, currency `USD`, `99` holdings and total net assets `$102.75 million`, as of `2026-07-31`.
- `management_mode: passive-index`; the official objective is to replicate as closely as possible, before fees and expenses, the price and yield performance of the `ChiNext Index`, which covers the 100 largest and most liquid stocks listed and trading on the Shenzhen ChiNext Market.
- `tracked_index: ChiNext Index (SZ988107)`; `benchmark: S&P 500 Total Return` is only a common USD reference with dividends reinvested. The issuer’s factsheet distinguishes NAV, market-price and index returns; only NAV TR is the fund performance basis.
- Fee evidence as of the current factsheet: management fee `0.50%`, other expenses `0.50%`, gross expense ratio `1.00%`, fee waiver/reimbursement `-0.35%`, net expense ratio `0.65%`, with contractual cap through `2027-05-01`.
- Latest official month-end NAV TR fields as of `2026-07-31`: 1-month `-23.56%`, 3-month `-8.60%`, YTD `8.45%`, 1-year `55.19%`, 3-year annualized `18.06%`, 5-year annualized `-0.09%`, 10-year annualized `4.80%`, and since ETF inception `6.52%`.
- Latest official month-end ChiNext Index comparison as of `2026-07-31`: 1-month `-22.49%`, 3-month `-7.53%`, YTD `8.78%`, 1-year `54.54%`, 3-year annualized `17.93%`, 5-year annualized `-0.01%`, 10-year annualized `6.17%`, and since ETF inception `8.19%`. Fund-minus-index differences are `-1.07 pp`, `-1.07 pp`, `-0.33 pp`, `+0.65 pp`, `+0.13 pp`, `-0.08 pp`, `-1.37 pp`, and `-1.67 pp`; these are tracking/fee comparisons, not alpha.
- Official rolling 10-year window: `2016-07-31` to `2026-07-31`, exactly `10.00` elapsed years, NAV TR CAGR `4.80%`. Raw NAV endpoints and issuer cumulative return were not disclosed; review calculation is `100.00 × (1 + 4.80%)^10.00 = approximately 159.81`, or approximately `59.81%` cumulative.
- Period reconciliation: the prior quarter-end factsheet field was 10-year NAV TR `7.37%` as of `2026-06-30`; it is retained only as a dated prior observation and is not mixed with the newer `2026-07-31` month-end field. The current factsheet also reports 2026-06-30 quarter-end YTD NAV TR `41.88%`, separately from the current 2026-07-31 YTD `8.45%`.
- Calendar-year evidence: the reviewed current official factsheet does not disclose complete annual NAV/index rows for `2016-2025`, so calendar CAGR, up/down count, best/worst year and exact 2021-2025 spread remain `ไม่พบข้อมูลที่ยืนยันได้`. Cached S&P 500 2016-2025 rows are retained only as a common reference and not used to fill CNXT gaps.
- Price and risk snapshot: the current factsheet does not disclose a 2026-07-31 NAV quote; the prior official capture recorded latest NAV `US$51.14` on `2026-07-22`. Current holdings/sector data are Information Technology `48.2%`, Industrials `29.6%`, Financials `6.2%`, Health Care `5.8%`, Materials `5.3%`, and Other/Cash `0.2%`, as of 2026-07-31. China A-share, ChiNext concentration, technology/industrials, Stock Connect, PRC tax, foreign currency, liquidity, index-tracking and high-turnover risks remain relevant; daily NAV drawdown/recovery is not verified.
- Methodology continuity caveat: VanEck states that pre-market-close data before `2021-12-10` reflected the `SME-ChiNext 100 Index (CNI6109)` and after that date reflects `ChiNext Index (SZ988107)`. The 10-year figure therefore crosses an index/methodology change.
- Source-quality choice: the official VanEck product page timed out during the current fetch, so the current factsheet was used as the authoritative source for current performance, holdings, fee and risk fields; no third-party substitute was used.
- Source URLs: official product page `https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt/`; official factsheet `https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt-fact-sheet.pdf/`; S&P 500 reference `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P 500 2016-2025 rows were reused under the vault convention without a new search.
- Pre-save checklist: PASS. Identity/exchange, passive classification, tracked index, NAV/TR basis, USD currency, fee waiver, distribution/fee treatment, latest month-end and prior quarter-end separation, 10-year window, methodology break, S&P cache window, calculation labels, source links, unresolved gaps, and graph links were checked locally before writing.
- Proposed durable contents: update `wiki/analysis/performance/ETF_NYSE_ARCA_CNXT Performance.md` with `management_mode: passive-index`, `updated: 2026-08-28`, current `2026-07-31` NAV/benchmark fields, normalized 10-year calculation, latest holdings/sector snapshot, source batch link and disclosed gaps; update the current CNXT rows in `wiki/analysis/comparisons/China ETF.md` and `wiki/analysis/performance/ETF Performance Index.md` from `7.37% / 16.05%` to `4.80% / 8.45%`; append one `etf-performance` bullet to `log.md`. No region file is created because `China ETF` already exists.
- Proposed log entry: `- etf-performance: Refreshed [[ETF_NYSE_ARCA_CNXT Performance]], [[China ETF]] and [[ETF Performance Index]], and extended [[ETF_performance_sources_2026-08-28]]. Scheduled-inline local pre-save returned PASS; latest official rolling 10-year NAV TR is 4.80% and current NAV TR YTD is 8.45% as of 2026-07-31; CNXT remains a passive ChiNext China A-share ETF with the 2021-12-10 methodology break, concentrated sector exposure and daily NAV drawdown/recovery gap disclosed.`
- `pre_save_result: PASS`

### DBJP

- `workflow: check-etf-performance`
- `execution_profile: scheduled-inline`
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Evidence identity: the official DWS Q2 2026 factsheet identifies `Xtrackers MSCI Japan Hedged Equity ETF`, ticker `DBJP`, NYSE Arca, tracked index `MSCI Japan US Dollar Hedged Index`, inception `2011-06-08`, `169` holdings and net assets `$670,068,018.42`, all as of `2026-06-30`.
- `management_mode: passive-index`; the October 1, 2025 official summary prospectus states that the fund uses a passive/indexing approach to seek results corresponding to the MSCI Japan US Dollar Hedged Index. The fund uses full replication where practicable and may use sampling, forward contracts/NDFs, futures and options for non-speculative tracking and JPY hedging; the reviewed strategy is not derivative-heavy.
- `tracked_index: MSCI Japan US Dollar Hedged Index`; the factsheet describes exposure to Japanese equities while mitigating USD/JPY fluctuations. `benchmark: S&P 500 Total Return` remains only a common USD reference with dividends reinvested.
- `expense_ratio: 0.45%` gross and net as of `2026-06-30`; the prospectus reports portfolio turnover of `17%`. Return basis is official NAV Total Return in USD, including reinvested distributions and fund expenses.
- Official Q2 2026 NAV TR fields as of `2026-06-30`: 3-month `17.29%`, 1-year `49.40%`, 3-year annualized `28.05%`, 5-year annualized `21.88%`, 10-year annualized `17.28%`, and since ETF inception `14.22%`.
- Official Q2 2026 MSCI Japan US Dollar Hedged Index comparison as of `2026-06-30`: 3-month `17.56%`, 1-year `50.24%`, 3-year annualized `28.70%`, 5-year annualized `22.49%`, 10-year annualized `17.89%`, and since ETF inception `14.87%`. Fund-minus-index differences are `-0.27 pp`, `-0.84 pp`, `-0.65 pp`, `-0.61 pp`, `-0.61 pp`, and `-0.65 pp`, respectively; these are tracking/fee/hedging comparisons, not manager alpha.
- For context, the same factsheet's unhedged MSCI Japan Index reference returned `14.21%`, `29.11%`, `18.49%`, `9.49%`, `9.84%` and `8.10%` for the six windows above; this is context for the currency-hedge outcome, not the fund benchmark.
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`, exactly `10.00` elapsed years, NAV TR CAGR `17.28%`. Raw NAV endpoints and issuer cumulative return were not disclosed; review normalization is `100.00 × (1 + 17.28%)^10.00 = approximately 492.31`, or approximately `392.31%` cumulative.
- Official calendar NAV TR rows from the October 1, 2025 prospectus, used for `2016-2024`: `2016 -2.00%`, `2017 20.83%`, `2018 -14.03%`, `2019 20.78%`, `2020 9.49%`, `2021 12.89%`, `2022 -2.54%`, `2023 34.97%`, and `2024 26.05%`. The current Q2 2026 factsheet did not disclose a 2025 calendar NAV row or current YTD field.
- Calculations from displayed complete rows: 2016-2024 cumulative `51.99%`, CAGR `10.81%` over `9.00` years, up/down years `6 / 3`, best `2023 +34.97%`, least positive `2020 +9.49%`, worst `2018 -14.03%`, and least bad down year `2022 -2.54%`. This calendar-row CAGR is not the same measurement as the official rolling 10-year CAGR.
- Current YTD: `ไม่พบข้อมูลที่ยืนยันได้`; the latest official factsheet presents quarter-end and rolling fields through `2026-06-30` but does not label a year-to-date return, and no newer official performance field was captured.
- Risk and gaps: Japan single-country/sector, equity-market, currency, forward-hedging, hedge-cost/basis-risk, derivatives, liquidity and tracking-error risks remain relevant. The factsheet reports beta `0.89` and the expense ratio above. Daily NAV observations sufficient for reproducible maximum drawdown and recovery were not captured; current NAV/market-price snapshot and current YTD remain not disclosed in the reviewed evidence.
- Source URLs: Q2 2026 factsheet `https://www.dws.com/US/EN/resources/Xtrackers-MSCI-Japan-Hedged-Equity-ETF/DBJP_fact-sheet.pdf`; summary prospectus `https://etf.dws.com/en-us/AssetDownload/Index/c7bca405-12a0-486d-8a66-5d3558c23fa0/DBJP-SUM.pdf`; dividend schedule `https://etf.dws.com/en-us/AssetDownload/Index/6b4403da-1256-4e11-8e8a-14254534db91/Dividend-Schedule.pdf`; currency-hedged ETF explanation `https://etf.dws.com/en-us/etf-knowledge/focus-topics-etf-investment-strategies/currency-hedged-etfs-mitigating-currency-risks-from-international-equities/`; S&P 500 reference `https://www.spglobal.com/spdji/en/indices/equity/sp-500/`; cached S&P 500 2016-2025 rows were reused under the vault convention without a new search.
- Pre-save checklist: PASS. Identity/exchange, passive classification, tracked index, NAV/TR basis, USD currency, fee and distribution treatment, rolling-period as-of date, hedge/index comparison, 10-year endpoint convention, annual-row completeness, S&P cache window, calculation labels, source links, unresolved gaps, and graph links were checked locally before writing.
- Proposed durable contents: update `wiki/analysis/performance/ETF_NYSE_ARCA_DBJP Performance.md` with `management_mode: passive-index`, `updated: 2026-08-28`, `source_batch: raw/imports/ETF_performance_sources_2026-08-28.md`, `return_currency: USD`, the Q2 2026 rolling fields and MSCI Japan USD Hedged Index comparison, updated holdings/net assets and disclosed hedge risks, while retaining the 2016-2024 calendar evidence and current-YTD gap; append one `etf-performance` bullet to `log.md`. No region/index navigation change is proposed because DBJP remains in the Japan primary region and its current 10-year/YTD summary values are unchanged.
- Proposed log entry: `- etf-performance: Refreshed [[ETF_NYSE_ARCA_DBJP Performance]] and extended [[ETF_performance_sources_2026-08-28]]. Scheduled-inline local pre-save returned PASS; official rolling 10-year NAV TR is 17.28% and 1-year NAV TR is 49.40% as of 2026-06-30, while current YTD remains not disclosed; DBJP remains a passive USD/JPY-hedged Japan ETF with official tracking/hedging risks and daily NAV drawdown/recovery gaps disclosed.`
- `pre_save_result: PASS`
