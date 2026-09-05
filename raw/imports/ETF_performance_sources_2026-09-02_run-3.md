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

# ETF Performance Sources — 2026-09-02 Run 3

This dated batch records source-backed evidence and the scheduled-inline
pre-save review for the `research-queue-manager` run. Each card was processed
sequentially under one retained project lease; unsupported bond cards were
blocked without durable ETF-performance output.

## ISCF evidence packet

- Input ticker and canonical identity: `ISCF`; `NYSE Arca:ISCF`; fund: iShares International Small-Cap Equity Factor ETF; fund launch date `2015-04-28`.
- Official classification: `passive-index`; international developed-markets small-cap equity ETF using value, quality, momentum, and low-volatility factors. The official product page identifies `NYSE Arca`, asset class `Equity`, and current benchmark `STOXX International Small-Cap Equity Factor Index (USD) (Net)`.
- Official current product-page observations reviewed 28 Aug 2026: NAV `USD 45.92`, closing price `USD 46.01`, net assets `USD 684,261,985`, holdings `1,161`, and NAV Total Return YTD `12.99%`; 30-day SEC yield `2.68%` and 12-month trailing yield `3.64%` were as of 31 Jul 2026. Expense ratio is `0.24%`.
- Official risk fields reviewed on the same iShares page: 3-year standard deviation `14.21%` and beta `0.73`, both as of 31 Jul 2026. Official daily NAV observations sufficient to calculate maximum drawdown and recovery were not verified.
- Official annual NAV Total Return rows retained from the prior verified official source set: 2016 `0.01%`, 2017 `36.24%`, 2018 `-18.18%`, 2019 `25.94%`, 2020 `7.89%`, 2021 `13.22%`, 2022 `-15.06%`, 2023 `11.52%`, 2024 `4.33%`, and 2025 `34.07%`. The 2016-2024 rows are from the official summary prospectus; the 2025 row and overlapping 2021-2025 rows are from the official June 2026 factsheet/product performance table.
- Return basis: USD `NAV Total Return` with dividends and capital gains reinvested and fund expenses deducted; market-price return is kept separate. Common comparison benchmark is cached `S&P 500 Total Return` in USD with dividends reinvested, complete calendar years 2016-2025, as of 31 Dec 2025.
- Issuer benchmark metadata: `STOXX International Small-Cap Equity Factor Index (Net)` from 1 Mar 2023; historical index data before 1 Mar 2023 is for the `MSCI World ex USA Small Cap Diversified Multiple-Factor Index (Net)`. This splice is disclosed and not treated as one unchanged benchmark series.
- Calculations from the retained rounded official annual rows: 2016-2025 product `2.2723823333`, cumulative `127.24%`, rounded-input CAGR `8.55%`; 2021-2025 product `1.5001303055`, cumulative `50.01%`, CAGR `8.45%`; population standard deviation `16.27%`; `8 / 2` up/down years. Best `2017 +36.24%`; least positive `2016 +0.01%`; worst `2018 -18.18%`; least-bad down year `2022 -15.06%`.
- Calculation reconciliation note: the current iShares web capture exposes the overlapping 2021-2025 rows and refreshed current fields but not a replacement 2016-2020 table. The durable page preserves the previously verified full-window calculation and updates only the newly verified current fields; no new 2016-2020 values are inferred from the current page.
- S&P 500 cached comparison: 2016-2025 cumulative `298.33%` / rounded-input CAGR `14.82%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`. These are common-reference comparisons, not alpha, and no synchronized 2026 S&P YTD is claimed.
- Source map: official product page `https://www.ishares.com/us/products/272823/ishares-international-small-cap-equity-factor-etf`; official factsheet `https://www.ishares.com/us/literature/fact-sheet/iscf-ishares-international-small-cap-equity-factor-etf-fund-fact-sheet-en-us.pdf` dated 30 Jun 2026; official summary prospectus `https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-edge-msci-multifactor-intl-small-cap-etf-7-31.pdf`; cached S&P references and index definition are defined in the `check-etf-performance` skill.
- Source integrity review: PASS — official identity, exchange, passive equity eligibility, fee, NAV/market-price separation, current YTD, benchmark splice, and visible as-of dates reconcile; the current page does not replace the previously verified 2016-2020 rows.
- Calculation review: PASS — retained 2016-2025 and 2021-2025 calculations, current YTD, up/down counts, and best/worst subsets were recomputed; the current capture's incomplete historical presentation was not used to overwrite the prior full-window calculation.
- Format and graph review: PASS — Thai-first narrative, one annual table, required sections, canonical `geography/International` and legacy `geography/international-ex-US` tags, and breadcrumb targets resolve to existing files. `International ETF.md`, `ETF Performance Index.md`, and `log.md` were included because their existing ISCF snapshots were refreshed.
- Planned durable paths/change map: update `wiki/analysis/performance/ETF_NYSE_ARCA_ISCF Performance.md`; create this source batch; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, and `log.md`.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## ISCF research handoff

```text
status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive ISCF identity, refreshed current NAV/YTD, retained verified annual calculations, benchmark splice, graph updates and scheduled-local review passed with daily drawdown and current historical-row presentation gaps disclosed.
```
