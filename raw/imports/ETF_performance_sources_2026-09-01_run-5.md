---
type: etf-performance-source-batch
workflow: check-etf-performance
run_date: 2026-09-01
run_label: run-5
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---

# ETF Performance Sources — 2026-09-01 — run-5

## EFAX — State Street SPDR MSCI EAFE Fossil Fuel Reserves Free ETF

- `entity_key`: `NYSE Arca:EFAX`; the issuer confirms NYSE Arca ticker `EFAX`, USD trading currency, listing `2016-10-25`, and fund inception `2016-10-24`.
- Management mode: `passive-index`; the fund seeks to track the `MSCI EAFE ex Fossil Fuels Index` using an index-sampling strategy. The underlying exposure is developed-market equity outside the U.S. and Canada, so primary region is `International`.
- Official product source: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-msci-eafe-fossil-fuel-reserves-free-etf-efax — current fund facts as of 2026-08-31; NAV, price, holdings, characteristics, yields, and performance as of 2026-08-28/2026-07-31. NAV `US$56.03`, closing price `US$55.76`, premium/discount `-0.48%`, AUM `US$515.49M`, holdings `641`, P/B `2.43x`, forward P/E `16.76x`, fund distribution yield `3.04%`, and gross expense ratio `0.20%`.
- Official standardized NAV performance as of 2026-07-31: YTD `10.16%`; 1-year `22.15%`; 3-year annualized `15.69%`; 5-year annualized `8.53%`; since-inception annualized `9.29%`. All results assume reinvested dividends and capital gains and are net of fund fees. Market-value returns remain separate.
- Official factsheet: https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-efax.pdf — product information and performance as of 2026-06-30; NAV YTD `8.78%`, 1-year `18.61%`, 3-year annualized `16.37%`, 5-year annualized `8.43%`, and since-inception annualized `9.23%`.
- SEC source: https://www.sec.gov/Archives/edgar/data/1168164/000119312526031207/d72607d497k.htm — January 31, 2026 summary prospectus; fund objective, 0.20% fee, index-sampling strategy, international equity risks, and year-end standardized returns as of 2025-12-31. The annual bar-chart values were not exposed in the reviewed HTML capture, so no annual NAV rows are invented or replaced by a secondary proxy.
- Return basis: USD NAV Total Return with distributions reinvested and fund expenses reflected. A complete 10-year NAV window is not applicable because the verified inception is `2016-10-24`, which is under ten elapsed years at the current 2026-09-01 run date; raw endpoints are also not disclosed.
- S&P 500 common reference: cached `S&P 500 Total Return` USD, dividends reinvested, complete calendar years 2016-2025, reference as of 2025-12-31. Rows: `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`. These are not used to infer EFAX annual rankings.
- Performance calculations: no EFAX calendar cumulative return, CAGR, up/down count, best/worst year, volatility, drawdown, or recovery was calculated because official annual NAV rows and daily NAV endpoints were not disclosed in the reviewed evidence. Issuer-reported period returns are retained with their own as-of date.
- Planned durable path: create `wiki/analysis/performance/ETF_NYSE_ARCA_EFAX Performance.md`; create this source batch. Shared navigation/index files and `log.md` were intentionally not changed because they were already dirty before this card’s claim and must be preserved outside the scoped commit; the performance page retains the required breadcrumb and canonical geography tag.

## Scheduled-inline local review

- Review packet checked canonical exchange/ticker, identity, passive equity eligibility, index and region, NAV TR basis, currency, current and historical as-of dates, official source links, 10-year eligibility, benchmark cache, not-disclosed handling, one annual table, required sections, breadcrumb, and canonical tag.
- Pre-save verdict: `PASS`. No material number lacks a source; no market-price return, unsupported annual proxy, or shorter-period 10-year claim is used. Daily-NAV risk evidence remains explicitly unresolved.

## Item-scoped blocked card

- `DFSB` was separately researched and routed `BLOCKED` with code `unsupported-etf-type`; official Dimensional and SEC materials classify it as the `Dimensional Global Sustainability Fixed Income ETF`, a global sustainability fixed-income fund outside this equity performance workflow. No performance page was planned for DFSB.

### research_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official EFAX performance evidence passed scheduled-local review and the scoped performance page and source batch were written.

## IIXFF → LSE:IDFF — iShares MSCI AC Far East ex-Japan UCITS ETF

- `entity_key`: `LSE:IDFF`; card input `IIXFF` is retained as the raw alias, while the official issuer page and factsheet identify the USD London Stock Exchange line as `IDFF` for share class ISIN `IE00B0M63730`. Other listing lines include GBP `IFFF` on LSE and USD `IFFF` on SIX; the USD LSE line is the canonical display line for this card.
- Management mode: `passive-index`; physical replicated equity ETF; fund/share-class launch `2005-10-28`; primary underlying exposure is East Asia excluding Japan and India, so primary region is `Asia ex Japan`.
- Official product source: https://www.ishares.com/uk/individual/en/products/251848/ishares-msci-ac-far-east-exjapan-ucits-etf — current NAV `US$96.75` as of 2026-08-27; NAV Total Return YTD `32.28%` as of 2026-08-26; holdings `423`, P/E `21.68x`, P/B `2.68x`, and 12-month trailing distribution yield `1.05%` as of 2026-08-28; 3-year beta `0.998` as of 2026-07-31; expense ratio `0.74%`; benchmark `MSCI All Country World Far East Ex Japan USD Index (USD)`.
- Official factsheet: https://www.ishares.com/uk/individual/en/literature/fact-sheet/ifff-ishares-msci-ac-far-east-ex-japan-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y — USD distributing share class; performance/as-of 2026-06-30; official calendar NAV rows are `2016 5.50%`, `2017 41.19%`, `2018 -15.68%`, `2019 18.66%`, `2020 25.08%`, `2021 -8.92%`, `2022 -21.94%`, `2023 2.30%`, `2024 11.66%`, and `2025 39.91%`; benchmark rows are `6.21%, 42.16%, -15.14%, 19.45%, 26.04%, -8.42%, -21.57%, 3.00%, 12.42%, 40.69%`.
- Return basis: USD NAV Total Return with gross income reinvested where applicable; market price is not mixed. The issuer factsheet also reports 5-year annualized `4.94%` and since-inception annualized `8.20%` as of 2026-06-30; these are retained as separate official fields, not substituted for the calendar CAGR.
- Cached S&P 500 common reference: complete 2016-2025 USD Total Return calendar rows as of 2025-12-31: `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`.
- Calculations: IDFF 2016-2025 product `2.1181309`, cumulative `111.81%`, normalized endpoints `100.00 → 211.81`, rounded-input 10-year calendar CAGR `7.79%†`; 2021-2025 product `1.1362492`, cumulative `13.62%`, CAGR `2.59%`; S&P 500 cumulative `298.33%` / CAGR `14.82%`; S&P 2021-2025 cumulative `96.17%` / CAGR `14.43%`; population annual-return standard deviation `20.71%` for 2016-2025 and `20.92%` for 2021-2025.
- Calendar ranking: `7 / 3` positive/negative years; best `2017 +41.19%`; least positive `2023 +2.30%`; worst `2022 -21.94%`; least bad down year `2021 -8.92%`. No partial year is ranked.
- Risk evidence: official 3-year standard deviation `21.47%` and beta `0.998` are as of 2026-07-31; daily NAV observations sufficient for maximum drawdown/recovery and compatible risk-adjusted metrics were not verified. No market-price proxy is substituted.
- Planned durable paths: create `wiki/analysis/performance/ETF_LSE_IDFF Performance.md`; update this shared source batch. Shared region/index/log files are not changed because they were dirty before the retained lease and must remain outside the scoped commit; the performance page carries the Asia ex Japan breadcrumb and canonical geography tag.

## IIXFF scheduled-inline local review

- Review packet checked raw-alias-to-USD-line reconciliation, exchange/display key, fund identity, passive physical equity eligibility, return basis/currency, official annual rows, cached S&P basis/window, calculations, as-of dates, distribution treatment, risk gaps, one-region assignment, required sections, breadcrumb, and source links.
- Pre-save verdict: `PASS`. The 10-year label is limited to ten complete official calendar years and is marked `†` for rounded-input approximation; no current S&P YTD or daily drawdown is inferred.

### research_handoff — IIXFF

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official IIXFF-to-IDFF performance evidence passed scheduled-local review and the scoped page and source batch were written.
