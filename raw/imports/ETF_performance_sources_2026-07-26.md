---
type: source-batch
date: 2026-07-26
scope: etf-performance-coverage-audit
source_kind: official-issuer-plus-local-vault-reconciliation
tags:
  - source/etf-performance
  - audit/10-year-nav-tr
---

# ETF Performance Sources - 2026-07-26

## Audit scope

- Audit date: `2026-07-26`
- Canonical performance pages reviewed: `143`
- Status result: `106 EXPANDED_TO_10Y`, `37 ACCEPTED_SHORT_HISTORY`, `0 ADDITIONAL_HISTORY_FOUND`, `0 UNRESOLVED_10Y_TR`, `0 UNSUPPORTED_ETF_TYPE`
- Existing per-ETF source batches remain the primary source map for unchanged pages. This batch records the final coverage reconciliation and the fresh source checks that changed two current snapshots.
- No unsupported or identity-unresolved performance page was created. Unsupported input records remain in prior dated source batches.

## Fresh official source map

| Entity | Official source | Return basis / role | Verified observation |
|---|---|---|---|
| `NYSE Arca:FLAU` | [Franklin FLAU product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26365/SINGLCLASS/franklin-ftse-australia-etf/FLAU) | passive FTSE Australia exposure; NAV return includes reinvested distributions and fund expenses | Inception `2017-11-02`; NYSE Arca; 10-year field `—`; NAV TR YTD `9.50%` as of `2026-07-17`; since-inception NAV annualized `7.53%` as of `2026-06-30`; expense ratio `0.09%` |
| `NYSE Arca:FLAU` | [Franklin FLAU factsheet](https://www.franklintempleton.com/forms-literature/download/FLAU-FF) | official annual NAV TR and return-definition cross-check | Complete annual rows `2018-2025`; 2017 partial/inception year; factsheet capture as of `2026-03-31`; no official 10-year NAV TR |
| `NYSE Arca:FLCA` | [Franklin FLCA product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26364/SINGLCLASS/franklin-ftse-canada-etf/FLCA) | passive FTSE Canada exposure; NAV return includes reinvested distributions and fund expenses | Inception `2017-11-02`; NYSE Arca; 10-year field `—`; NAV TR YTD `8.17%` as of `2026-07-06`; expense ratio `0.09%` |
| `NYSE Arca:FLCA` | [Franklin FLCA factsheet](https://www.franklintempleton.com/forms-literature/download/FLCA-FF) | official annual NAV TR and return-definition cross-check | Complete annual rows `2018-2025`; 2017 partial/inception year; factsheet capture as of `2026-03-31`; no official 10-year NAV TR |
| `NYSE Arca:EPHE` | [iShares EPHE product page](https://www.ishares.com/us/products/239675/ishares-msci-philippines-etf) | identity, exchange, benchmark, NAV TR, current YTD and 10-year performance | Inception `2010-09-28`; NYSE Arca; rolling 10Y `2016-06-30` to `2026-06-30`; cumulative `-28.05%`; CAGR `-3.24%`; NAV TR YTD `2.76%` as of `2026-07-23` |
| `NYSE Arca:EPHE` | [iShares EPHE data page](https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239675&seoSlug=ishares-msci-philippines-etf) | current NAV/YTD cross-check | NAV `25.11` and NAV TR YTD `2.76%` as of `2026-07-23`; annual rows 2016-2020 remain not disclosed |
| `NYSE Arca:EPHE` | [EPHE factsheet](https://www.ishares.com/us/literature/fact-sheet/ephe-ishares-msci-philippines-etf-fund-fact-sheet-en-us.pdf) | annual NAV TR and index-change cross-check | 2021-2025 official rows; current index tracking from `2020-12-01`; 2016-2020 annual rows not disclosed |
| `NASDAQ:AAXJ` | [iShares AAXJ product page](https://www.ishares.com/us/products/239601/ishares-msci-all-country-asia-ex-japan-etf) | identity, exchange, benchmark, NAV TR, current YTD and 10-year performance | Inception `2008-08-13`; NASDAQ; rolling 10Y cumulative `164.36%` / CAGR `10.21%` for `2016-06-30` to `2026-06-30`; NAV TR YTD `21.30%` as of `2026-07-22` |
| `NASDAQ:AAXJ` | [AAXJ factsheet](https://www.ishares.com/us/literature/fact-sheet/aaxj-ishares-msci-all-country-asia-ex-japan-etf-fund-fact-sheet-en-us.pdf) | official fund identity, NAV return definition, annual rows and benchmark cross-check | Fund is passive/index-tracking equity; expense ratio `0.72%`; raw rolling endpoints not disclosed; 2021-2025 annual rows retained |

## Calculation convention

- Fund age: `(2026-07-26 - inception_date) / 365.25`.
- Ten-year qualification: official endpoints with at least `10.00` elapsed years or exactly ten consecutive complete calendar-year NAV TR observations.
- Rolling CAGR: `(End TR / Start TR)^(1 / Years) - 1`.
- Short-history pages are not relabeled as 10-year; no dividend-adjusted proxy is counted as official NAV TR.
- S&P 500 Total Return comparisons use the cached 2016-2025 USD, dividends-reinvested convention when the page window is eligible; current YTD observations stay separate by as-of date.

## Remaining gaps

- Short-history group: `Cboe BZX:BBJP, Cboe BZX:BBAX, Euronext Amsterdam:ICHN, LSE:DXJA, LSE:FLXI, LSE:KWEB, LSE:VAPU, LSE:VJPU, NASDAQ:CNQQ, NASDAQ:EWJV, Nasdaq:IND, Nasdaq:INDH, Nasdaq:INDQ, Nasdaq:SMHC, NASDAQ:TCHI, Nasdaq:WDAF, NYSE Arca:DGIN, NYSE Arca:FLAU, NYSE Arca:FLAX, NYSE Arca:FLCA, NYSE Arca:FLCH, NYSE Arca:FLIN, NYSE Arca:FLJH, NYSE Arca:FLJP, NYSE Arca:FLKR, NYSE Arca:FLTW, NYSE Arca:INQQ, NYSE Arca:KCAI, NYSE Arca:KDEF, NYSE Arca:KGRN, NYSE Arca:KMCA, NYSE Arca:KSTR, NYSE Arca:KTEC, NYSE Arca:KURE, NYSE Arca:VNAM, NYSE:KPHO, XETRA:VJPA`; each page states the verified inception/available window and does not invent missing years.
- Older-fund unresolved group: none.
- Unsupported/identity-unresolved group: none.

## Reviewer record

- Independent pre-save reviewer: PASS; source batch cleared for durable write.
 - The main agent remained the sole durable-file writer.
