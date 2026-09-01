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
