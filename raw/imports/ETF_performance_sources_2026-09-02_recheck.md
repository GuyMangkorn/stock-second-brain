---
type: etf-performance-source-batch
workflow: check-etf-performance
batch_date: 2026-09-02
run_label: recheck-1
execution_profile: interactive-delegated
verification_mode: interactive-local-fallback
reviewer_dispatch: unavailable-after-usage-limit
reviewer_fallback_reason: project-scoped source_verifier exhausted its usage limit before returning a verdict; the main agent completed the same source, calculation, freshness, taxonomy, and graph checklist locally
pre_save_review: PASS
---

# ETF Performance Sources — 2026-09-02 — correction recheck

ขอบเขตของ batch นี้คือการตรวจซ้ำและแก้ canonical records ของ `Cboe BZX:NUDM`,
`NYSE Arca:FNDF` และ `Cboe BZX:DFIS` ก่อนนำไปใช้เป็น research context ของ
paper portfolio. ตัวเลข performance เป็น USD NAV Total Return เว้นแต่จะระบุเป็น
อย่างอื่น. S&P 500 Total Return เป็นเพียง common reference benchmark; DFIS
benchmark-relative arithmetic ไม่ถูกเรียกว่า alpha.

## NUDM — Nuveen ESG International Developed Markets Equity ETF

- `entity_key`: `Cboe BZX:NUDM`; official SEC listing exchange is Cboe BZX Exchange, Inc.; inception `2017-06-06`; supported `passive-index` equity ETF.
- Official sources: [Nuveen product page](https://www.nuveen.com/en-us/exchange-traded-funds/nudm-nuveen-esg-international-developed-markets-equity-etf), [Nuveen factsheet](https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?download=1&uniqueId=02852fbf-974a-433c-9b45-56a6a1289a83), [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1635073/000119312526080207/d40382d497k.htm), [MSCI index page](https://www.msci.com/indexes/index/713162/nuveen-esg-international-developed-markets-equity-index), and [MSCI index factsheet](https://www.msci.com/documents/1296102/5161905/tiaa_esg_international_developed_markets_equity_index_usd_net.pdf/c086131e-2b0a-52de-ffec-ad056865129f).
- The dated Nuveen factsheet is as of `2026-06-30` and reports NAV TR calendar rows `2018 -14.63%`, `2019 24.28%`, `2020 10.74%`, `2021 10.21%`, `2022 -15.08%`, `2023 17.89%`, `2024 5.55%`, `2025 29.35%`, plus 2026 YTD `10.10%`. Its index rows are `-14.47%`, `24.66%`, `11.14%`, `10.52%`, `-14.94%`, `18.19%`, `5.80%`, `29.87%`, and `10.26%` YTD.
- Fund facts as of `2026-06-30`: expense ratio `0.27%`, SEC 30-day yield `2.33%`, annual distributions, net assets `US$698.26M`, `76` positions, weighted average market cap `US$126.09B`, forward P/E `17.39x`. Current price/NAV was not disclosed in the reviewed official evidence and remains `not disclosed`.
- Calculations from the eight rounded official annual rows: product `1.7698793878`, cumulative `76.99%`, normalized calculation `100.00 at 2017-12-31 → 176.99 at 2025-12-31`, rounded-input CAGR `7.40%`; 2021-2025 product `1.5063734`, cumulative `50.64%`, CAGR `8.54%`; annual up/down `6 / 2`; best `2025 +29.35%`; worst `2022 -15.08%`; annual-row population standard deviation `15.33%` (2018-2025) and `14.73%` (2021-2025).
- Common S&P 500 TR reference uses the cached 2025-12-31 USD convention: 2018-2025 cumulative/CAGR `192.03%`/`14.33%`; 2021-2025 `96.17%`/`14.43%`. It is not the issuer benchmark.
- The factsheet states that Teachers Advisors, LLC merged into Nuveen Asset Management, LLC effective `2026-08-01`, without investment-strategy or portfolio-management change, and that Nuveen Asset Management became sub-adviser. Product-page and dated-factsheet adviser/sub-adviser wording is retained as a wording conflict; the dated factsheet is the as-of source selected here.
- Risk gap: compatible daily NAV history for maximum drawdown, recovery duration, downside capture, and risk-adjusted evidence was not verified; no proxy is substituted.

## FNDF — Schwab Fundamental International Equity ETF

- `entity_key`: `NYSE Arca:FNDF`; official Schwab identity, exchange and inception `2013-08-15`; supported `passive-index` equity ETF.
- Official sources: [Schwab product page](https://www.schwabassetmanagement.com/products/fndf) and [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1454889/000088454626000305/c497k.htm).
- Official annual NAV TR rows as of 12/31 are `2016 7.70%`, `2017 23.81%`, `2018 -14.19%`, `2019 18.41%`, `2020 4.02%`, `2021 14.52%`, `2022 -7.77%`, `2023 20.34%`, `2024 2.6504872%`, and `2025 40.733244%`. Product cumulative is `158.78%`; rounded-row calendar CAGR is `9.97%`; official SEC 10-year average annual NAV TR is `9.98%`; 2021-2025 cumulative/CAGR is `83.62%`/`12.92%`.
- Current official standardized performance through `2026-07-31`: NAV TR YTD `20.44%`; issuer rolling 10-year NAV TR `11.73%`; expense ratio `0.25%`, turnover `12.46%`, beta `1.00`, and 3-year standard deviation `13.99%`.
- Current official snapshot as of `2026-08-31`: NAV `US$55.66`, bid/ask midpoint `US$55.53`, premium/discount `-0.17%`, net assets `US$26,178,552,634.28`, and `906` holdings. The current product page also shows a 30-day median bid/ask spread of `0.02%` for the displayed 2026-08-01–2026-08-31 window.
- SEC strategy evidence: the fund normally invests at least 90% of net assets in index stocks or depositary receipts, does not hedge foreign-currency exposure, and may use forward contracts for securities awaiting settlement. The current tracked index is `RAFI Fundamental High Liquidity Developed ex US Large Index (Net)`; the benchmark changed from Russell RAFI effective `2024-06-21`.
- Calculations from the official annual rows: product `2.5878305058`, cumulative `158.78%`, normalized endpoints `100.00 → 258.78`, rounded-input 10-year CAGR `9.97%`; S&P 500 cached 2016-2025 cumulative/CAGR `298.33%`/`14.82%`; 2021-2025 S&P cumulative/CAGR `96.17%`/`14.43%`; annual up/down `8 / 2`; best `2025 +40.73%`; worst `2018 -14.19%`.
- Cached S&P 500 TR source URLs: [2016-2019 reference PDF](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022 commentary](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 commentary](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025 commentary](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/), and [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/).
- Risk gap: compatible official daily NAV history for maximum drawdown, recovery duration, downside capture, and risk-adjusted evidence was not verified; no market-price proxy is substituted for those metrics.

## DFIS — Dimensional International Small Cap ETF

- `entity_key`: `Cboe BZX:DFIS`; [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000070/c497k.htm) identifies the ticker and Cboe BZX exchange; inception `2022-03-23`, listing `2022-03-24`; supported `active-equity-long-only`, `systematic-active` equity ETF.
- Official sources: [Dimensional fund page](https://www.dimensional.com/us-en/funds/dfis/international-small-cap-etf), [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000070/c497k.htm), and [Cboe listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/DFIS/). SEC describes an actively managed fund that does not seek to replicate a specific index and uses an integrated research, portfolio-design, portfolio-management and trading process.
- Current 2026 prospectus fees are management fee `0.35%`, other expenses `0.04%`, total annual fund operating expenses `0.39%`. The strategy-aligned management benchmark is `MSCI World ex USA Small Cap Index (net dividends)`, identified in the official performance table as a similar-universe comparison; S&P 500 remains common reference only.
- Official complete post-launch calendar rows: 2023 fund/benchmark `15.04%`/`12.62%`; 2024 `3.79%`/`2.76%`; 2025 `37.49%`/`34.07%`. The 2022 inception year is partial and excluded.
- Official standardized NAV TR fields as of `2026-07-31`: 3M `1.96%`, 1Y `23.26%`, 3Y annualized `17.39%`, and since inception `11.04%`. Official current snapshot as of `2026-08-31`: NAV `US$37.61`, market price `US$37.53`, premium/discount `-0.22%`. Current YTD `10.30%*` as of `2026-07-31` is a secondary AAII NAV total-return field and is marked with `*`.
- Calculations from official 2023-2025 rows: fund product `1.6416308200`, cumulative `64.16%`, rounded-input CAGR `17.97%`, population standard deviation `14.01%`; management benchmark product `1.5515694790`, cumulative `55.16%`, CAGR `15.77%`; S&P 500 cumulative/CAGR `86.12%`/`23.01%`. Annual active differences are `+2.42pp`, `+1.03pp`, and `+3.42pp`; Excess CAGR `+2.20pp`, hit rate `3/3`, relative wealth `+5.80%`. These are provisional benchmark-relative return observations, not alpha.
- Active track-record fields: `track_record: provisional`, `management_evidence: positive return evidence`, `risk_evidence: not-verified`; no complete down year in the three official rows (`3 / 0` up/down). Secondary AAII evidence as of `2026-07-31` reports `3,461` holdings, `9.0%` turnover and `10.30%` NAV YTD; these are not substituted for the official price/NAV snapshot.
- Risk gap: compatible daily NAV history for maximum drawdown, recovery duration, downside capture, and risk-adjusted evidence was not verified.

## Local pre-save verification

- Identity/exchange: PASS — NUDM `Cboe BZX`, FNDF `NYSE Arca`, DFIS `Cboe BZX`; no OTC alias is used as the canonical key.
- Eligibility/taxonomy: PASS — all three are equity ETFs and classified as supported passive-index or active-equity-long-only; no bond, commodity, currency, multi-asset, leveraged, inverse, defined-outcome, covered-call, option-income, single-stock-option or derivative-heavy fund is included.
- Return basis/periods: PASS — NAV Total Return, USD, reinvested distributions where the official source states it; partial inception years excluded; current DFIS YTD is explicitly secondary and marked `*`.
- Calculations: PASS — products, cumulative returns, CAGRs, up/down counts, benchmark comparisons, and DFIS active differences were recomputed from the stated rows; FNDF official SEC `9.98%` is kept separate from the `9.97%` rounded-row calculation.
- Freshness: PASS for the durable claims — issuer/SEC evidence dates are recorded separately for performance, fund facts, price/NAV, holdings and methodology; no 2026-09-02 live price is backfilled into an earlier as-of field.
- Risks/gaps: PASS — no unsupported daily maximum drawdown, recovery, downside capture, or risk-adjusted metric is claimed; NUDM price/NAV and DFIS official current YTD gaps remain visible.
- Graph/ownership: PASS — each page has the breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`, canonical `geography/International` tag, one canonical page, and resolved performance links; `International ETF.md` has `65` unique performance links after adding NUDM.
- Correction scope: PASS — the stale DFIS duplicate `ETF_CBOE_DFIS Performance.md` is removed; the prior mixed run-3 DFIS handoff is superseded by this scoped batch; NUDM/FNDF pages point to this recheck.

## Durable output map

- Updated: `wiki/analysis/performance/ETF_CBOE_BZX_NUDM Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_FNDF Performance.md`, `wiki/analysis/performance/ETF_CBOE_BZX_DFIS Performance.md`.
- Updated navigation: `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`.
- Created: this scoped recheck batch.
- Historical batches: `raw/imports/ETF_performance_sources_2026-09-01_run-5.md` and `raw/imports/ETF_performance_sources_2026-09-01.md` remain historical source captures; their supersession notes point to this recheck. The mixed DFIS block in `run-3` is replaced by a correction notice so the wrong canonical key is not left active.
- `log.md` receives one dated `etf-performance` correction bullet. No portfolio ledger event is created by this research-only correction.

## Verdict

`PASS` — local fallback review completed after the project-scoped reviewer became unavailable. Durable writes are permitted for the scoped files above, with the disclosed source gaps and correction history preserved.
