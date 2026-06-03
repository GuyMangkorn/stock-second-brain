---
type: source-note
ticker: VST
company: Vistra Corp.
source_kind: latest-results
search_date: 2026-06-03
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline, FY2026 guidance, and fresh 2026-06-03 market-data check
currency: USD
normalized_output: raw/financials/VST_fundamentals.md
entity: "[[VST]]"
tags:
  - source/latest-results
  - ticker/VST
---

# VST - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|
| 1 | SEC Form 10-Q filing detail | https://www.sec.gov/Archives/edgar/data/1692819/000169281926000014/0001692819-26-000014-index.htm | 2026-05-07 | Primary Q1 2026 filing, accession `0001692819-26-000014`, period ended 2026-03-31. |
| 1 | SEC Form 10-Q document | https://www.sec.gov/Archives/edgar/data/1692819/000169281926000014/vistra-20260331.htm | 2026-05-07 | Primary quarterly statements, segment revenue, cash flow, debt, balance sheet, and shares. |
| 1 | Vistra Q1 2026 earnings release | https://investor.vistracorp.com/2026-05-07-Vistra-Reports-First-Quarter-2026-Results?asPDF=1 | 2026-05-07 | Official results release, Q1 highlights, non-GAAP reconciliation, guidance, liquidity, and share repurchase update. |
| 1 | Vistra Q1 2026 investor presentation | https://filecache.investorroom.com/mr5ir_vistracorp_ir/343/Q1_2026_Results_Presentation_vFINAL.pdf | 2026-05-07 | Official presentation with debt bridge, hedging, strategic priorities, segment adjusted EBITDA, and guidance reconciliation. |
| 1 | Vistra FY2025 Form 10-K / annual report | https://www.sec.gov/Archives/edgar/data/1692819/000169281926000006/vistra-20251231.htm | 2026-02-27 | FY2025 audited annual filing baseline. |
| 1 | Vistra FY2025 results release | https://investor.vistracorp.com/2026-02-26-Vistra-Reports-Fourth-Quarter-and-Full-Year-2025-Results?asPDF=1 | 2026-02-26 | FY2025 revenue, net income, operating cash flow, capex, adjusted EBITDA, and adjusted FCFbG baseline. |
| 2 | StockAnalysis VST transcript index | https://stockanalysis.com/stocks/vst/transcripts/ | checked 2026-06-03 | Third-party transcript / audio discovery surface with links to earnings release, slides, and quarterly report. Official written transcript was not verified. |
| 3 | Vistra IR stock information | https://investor.vistracorp.com/stock-information | checked 2026-06-03 | Company IR quote page, delayed at least 15 minutes; used only as market-data cross-check. |
| 3 | StockAnalysis VST quote / statistics | https://stockanalysis.com/stocks/vst/ and https://stockanalysis.com/stocks/vst/statistics/ | checked 2026-06-03 | Fresh market-data check for intraday price, market cap, shares outstanding, and EV. |

## Reporting Scope

- Latest quarter: Q1 2026, three months ended 2026-03-31.
- Annual baseline: FY2025, year ended 2025-12-31.
- Fiscal year end: December 31.
- Reporting basis: unaudited US GAAP for Q1 2026 statements. `Adjusted EBITDA`, `Ongoing Operations Adjusted EBITDA`, and `Adjusted Free Cash Flow before Growth` / `Adjusted FCFbG` are company-defined non-GAAP measures.
- P1 note scope: source discovery and extracted source facts only. Normalization and entity updates belong to P4.

## Currency / Units

- Currency: USD.
- Units: USD millions unless stated as billions, per-share amounts, share counts, percentages, GWh, TWh, MW, or market quote.
- Local GAAP-style FCF formula for ingest: `FCF = cash provided by operating activities - capital expenditures`, with capex shown as positive spend in local notes.
- `Adjusted FCFbG` is non-GAAP and should not be treated as GAAP `OCF - capex`.

## Extracted Facts

### Company Identity

| Fact | Value | Source |
|---|---:|---|
| Company | Vistra Corp. | SEC Q1 2026 Form 10-Q. |
| Ticker / exchange | VST / NYSE | SEC Q1 2026 Form 10-Q. |
| Headquarters | Irving, Texas | SEC Q1 2026 Form 10-Q / earnings release. |
| Business description | Integrated retail electricity and power generation company in the United States | Vistra Q1 2026 release. |
| Reportable segments | Retail, Texas, East, West, Asset Closure | SEC Q1 2026 Form 10-Q. |

### Q1 2026 Highlights

| Fact | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Operating revenues | 5,640 | 3,933 | SEC Q1 2026 Form 10-Q / Q1 2026 release. |
| Operating income / loss | 1,499 | (120) | SEC Q1 2026 Form 10-Q / Q1 2026 release. |
| Net income / loss attributable to Vistra | 1,029 | (268) | SEC Q1 2026 Form 10-Q / Q1 2026 release. |
| Net income / loss attributable to Vistra common stock | 980 | (317) | SEC Q1 2026 Form 10-Q / Q1 2026 release. |
| Diluted EPS | 2.87 | (0.93) | SEC Q1 2026 Form 10-Q. |
| Weighted-average diluted shares | 341.857M | 339.800M | SEC Q1 2026 Form 10-Q. |
| Ongoing Operations Adjusted EBITDA | 1,494 | 1,240 | Vistra Q1 2026 release; non-GAAP. |
| Cash provided by operating activities | 1,199 | 599 | SEC Q1 2026 Form 10-Q / Q1 2026 release. |
| Capital expenditures, including nuclear fuel purchases and LTSA prepayments | 883 | 768 | SEC Q1 2026 Form 10-Q / Q1 2026 release; capex shown as positive spend locally. |
| GAAP-style free cash flow | 316 | (169) | Calculation: 1,199 - 883 and 599 - 768. |

### Segment Revenue And Adjusted EBITDA

| Segment / metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Retail operating revenues | 3,689 | 3,168 | SEC Q1 2026 Form 10-Q segment table; includes intersegment sales. |
| Texas operating revenues | 2,987 | 210 | SEC Q1 2026 Form 10-Q segment table; includes intersegment sales. |
| East operating revenues | 2,260 | 1,380 | SEC Q1 2026 Form 10-Q segment table; includes intersegment sales. |
| West operating revenues | 89 | 157 | SEC Q1 2026 Form 10-Q segment table; includes intersegment sales. |
| Asset Closure operating revenues | 6 | 4 | SEC Q1 2026 Form 10-Q segment table. |
| Corporate and Other eliminations | (3,391) | (986) | SEC Q1 2026 Form 10-Q reconciliation. |
| Total consolidated operating revenues | 5,640 | 3,933 | SEC Q1 2026 Form 10-Q. |
| Retail Adjusted EBITDA | 68 | 184 | Vistra Q1 2026 release; non-GAAP. |
| Texas Adjusted EBITDA | 586 | 490 | Vistra Q1 2026 release; non-GAAP. |
| East Adjusted EBITDA | 801 | 514 | Vistra Q1 2026 release; non-GAAP. |
| West Adjusted EBITDA | 56 | 62 | Vistra Q1 2026 release; non-GAAP. |
| Corporate and Other Adjusted EBITDA | (17) | (10) | Vistra Q1 2026 release; non-GAAP. |
| Asset Closure Adjusted EBITDA | (19) | (24) | Vistra Q1 2026 release; non-GAAP. |

### Balance Sheet / Debt / Shares

| Fact | 2026-03-31 | 2025-12-31 | Source |
|---|---:|---:|---|
| Cash and cash equivalents | 634 | 785 | SEC Q1 2026 Form 10-Q. |
| Restricted cash, current and noncurrent | 43 | 37 | SEC Q1 2026 Form 10-Q; 37 + 6 and 31 + 6. |
| Cash, cash equivalents, and restricted cash | 677 | 822 | SEC Q1 2026 Form 10-Q cash-flow statement. |
| Current assets | 9,016 | 9,179 | SEC Q1 2026 Form 10-Q. |
| Total assets | 41,308 | 41,550 | SEC Q1 2026 Form 10-Q. |
| Short-term borrowings | 0 | 1,800 | SEC Q1 2026 Form 10-Q. |
| Long-term debt due currently | 1,899 | 1,201 | SEC Q1 2026 Form 10-Q. |
| Long-term debt, less amounts due currently | 17,264 | 15,842 | SEC Q1 2026 Form 10-Q. |
| Long-term debt including amounts due currently | 19,163 | 17,043 | SEC Q1 2026 Form 10-Q debt note. |
| Accounts receivable financing | 750 | 1,225 | SEC Q1 2026 Form 10-Q debt note / balance sheet. |
| Forward repurchase obligation | 641 | 632 | SEC Q1 2026 Form 10-Q debt note / balance sheet. |
| Total Debt, company debt bridge | 19,262 | not disclosed in source note | Vistra Q1 2026 presentation; includes term loan, notes, revenue bonds, AR financing, forward repurchase obligations, and equipment financing. |
| Net debt before cash margin deposits | 18,628 | not disclosed in source note | Vistra Q1 2026 presentation: total debt 19,262 less cash 634. |
| Net cash margin deposits | 1,059 | not disclosed in source note | Vistra Q1 2026 presentation. |
| Net debt after cash margin deposits | 17,569 | not disclosed in source note | Vistra Q1 2026 presentation. |
| Preferred stock liquidation preference | 2,476 | 2,476 | SEC Q1 2026 Form 10-Q balance sheet. |
| Common shares outstanding | 338.080M | 338.060M | SEC Q1 2026 Form 10-Q balance sheet. |
| Shares outstanding as of 2026-05-01 | approximately 337M | not applicable | Vistra Q1 2026 release. |

### FY2025 Annual Baseline

| Fact | FY2025 | FY2024 | Source |
|---|---:|---:|---|
| Operating revenues | 17,738 | 17,224 | FY2025 results release / 10-K. |
| Operating income | 1,906 | 4,081 | FY2025 results release / 10-K. |
| Net income | 944 | 2,812 | FY2025 results release / 10-K. |
| Net income attributable to Vistra common stock | 752 | 2,467 | FY2025 results release / 10-K. |
| Cash provided by operating activities | 4,070 | 4,563 | FY2025 results release / 10-K. |
| Capital expenditures, including nuclear fuel purchases and LTSA prepayments | 2,752 | 2,078 | FY2025 results release / 10-K; capex shown as positive spend locally. |
| GAAP-style free cash flow | 1,318 | 2,485 | Calculation: OCF - capex. |
| Ongoing Operations Adjusted EBITDA | 5,912 | not normalized in this source note | Vistra Q1 2026 presentation / FY2025 release; non-GAAP. |
| Adjusted free cash flow before growth | 3,501 | not normalized in this source note | Vistra Q1 2026 presentation; consolidated non-GAAP. |
| Ongoing Operations Adjusted FCFbG | 3,592 | not normalized in this source note | Vistra Q1 2026 presentation; non-GAAP. |

### Guidance / Strategic Commentary

| Item | Value | Source |
|---|---:|---|
| FY2026 Ongoing Operations Adjusted EBITDA guidance | USD 6.8B-7.6B | Vistra Q1 2026 release / presentation; non-GAAP. |
| FY2026 Ongoing Operations Adjusted FCFbG guidance | USD 3.925B-4.725B | Vistra Q1 2026 release / presentation; non-GAAP. |
| FY2026 consolidated Adjusted EBITDA guidance | USD 6.720B-7.520B | Vistra Q1 2026 release reconciliation; non-GAAP. |
| FY2026 consolidated Adjusted FCFbG guidance | USD 3.760B-4.560B | Vistra Q1 2026 release reconciliation; non-GAAP. |
| 2027 Ongoing Operations Adjusted EBITDA midpoint opportunity | USD 7.4B-7.8B | Vistra Q1 2026 release; not guidance and no GAAP reconciliation provided. |
| Expected generation hedged as of 2026-05-01 | approximately 98% for 2026, 89% for 2027, 65% for 2028 | Vistra Q1 2026 release. |
| Pending acquisition / PPA exclusions | 2026 guidance excludes potential benefits from Cogentrix and Meta PPAs | Vistra Q1 2026 release. |
| Share repurchases since November 2021 | approximately USD 6.3B | Vistra Q1 2026 release. |
| Remaining share repurchase authorization | approximately USD 1.5B, expected to complete by year-end 2027 | Vistra Q1 2026 release. |
| Available liquidity | approximately USD 4.173B | Vistra Q1 2026 release. |
| Corporate issuer credit rating | Investment Grade at second major credit rating agency | Vistra Q1 2026 release. |

### Fresh Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Fresh intraday price checked | USD 155.37 at 2026-06-03 12:00 PM EDT, market open | StockAnalysis VST statistics page, checked 2026-06-03. |
| Market cap | USD 52.39B | StockAnalysis VST statistics page, checked 2026-06-03. |
| Shares outstanding | 337.18M | StockAnalysis VST statistics page, checked 2026-06-03; cross-check with Vistra release approximately 337M as of 2026-05-01. |
| Enterprise value | USD 72.53B | StockAnalysis VST statistics page, checked 2026-06-03. |
| IR quote cross-check | USD 155.78, market cap USD 52.5B | Vistra IR stock information page; delayed at least 15 minutes. |
| Local market cap cross-check | USD 52.388B | Calculation: 155.37 * 337.18M shares. |
| Local EV bridge for common equity DCF | USD 73.492B | Market cap 52.388 + net debt before cash margin deposits 18.628 + preferred stock liquidation preference 2.476. |
| TTM GAAP-style FCF | USD 1.803B | Calculation: FY2025 FCF 1.318B - Q1 2025 FCF (0.169B) + Q1 2026 FCF 0.316B. |
| FY2026 consolidated Adjusted FCFbG midpoint | USD 4.160B | Calculation: (3.760 + 4.560) / 2; non-GAAP guidance. |

## Transcript / Commentary

- Official written transcript / full Q&A was not verified. The company hosted a webcast and official slides; StockAnalysis lists a Q1 2026 transcript as a third-party transcript discovery surface.
- Management commentary in the official release emphasized Q1 execution, a diversified generation portfolio, load growth across primary markets, disciplined capital allocation, and preparation for summer demand.
- The release says 2026 guidance excludes potential benefits from Cogentrix and Meta PPAs, with some Meta contribution expected to begin in 2027.
- Use the webcast / third-party transcript only for context unless an official written transcript becomes available.

## Financial Tables

### Income Statement Summary

| Metric | Q1 2026 | Q1 2025 | FY2025 | Source |
|---|---:|---:|---:|---|
| Operating revenues | 5,640 | 3,933 | 17,738 | SEC Q1 2026 Form 10-Q / FY2025 release. |
| Operating income / loss | 1,499 | (120) | 1,906 | SEC Q1 2026 Form 10-Q / FY2025 release. |
| Net income / loss attributable to Vistra | 1,029 | (268) | 944 | SEC Q1 2026 Form 10-Q / FY2025 release. |
| Net income / loss attributable to Vistra common stock | 980 | (317) | 752 | SEC Q1 2026 Form 10-Q / FY2025 release. |
| Diluted EPS | 2.87 | (0.93) | not normalized | SEC Q1 2026 Form 10-Q. |
| Ongoing Operations Adjusted EBITDA | 1,494 | 1,240 | 5,912 | Vistra Q1 2026 release / presentation; non-GAAP. |

### Cash Flow Reconciliation

| Metric | Q1 2026 | Q1 2025 | FY2025 | Source |
|---|---:|---:|---:|---|
| Cash provided by operating activities | 1,199 | 599 | 4,070 | SEC Q1 2026 Form 10-Q / FY2025 release. |
| Capital expenditures, including nuclear fuel purchases and LTSA prepayments | 883 | 768 | 2,752 | SEC Q1 2026 Form 10-Q / FY2025 release; capex shown as positive spend. |
| GAAP-style free cash flow | 316 | (169) | 1,318 | Calculation: operating cash flow - capex. |
| TTM GAAP-style free cash flow | 1,803 | not applicable | not applicable | Calculation: FY2025 FCF 1,318 - Q1 2025 FCF (169) + Q1 2026 FCF 316. |
| FY2026 consolidated Adjusted FCFbG guidance | 3,760-4,560 | not applicable | not applicable | Vistra Q1 2026 release; non-GAAP. |
| FY2026 Ongoing Operations Adjusted FCFbG guidance | 3,925-4,725 | not applicable | not applicable | Vistra Q1 2026 release; non-GAAP. |

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Full FY2026 actual results | not disclosed | Q1 2026 is the latest official period found. |
| Official written Q1 2026 call transcript / full Q&A | not verified | Company webcast and slides are available; written transcript source is third-party. |
| GAAP reconciliation for 2027 Adjusted EBITDA midpoint opportunity | not provided | Company states it cannot provide quantitative reconciliation without unreasonable effort. |
| Post-close Cogentrix actual contribution | not disclosed | Transaction was still pending in Q1 2026 source set. |
| Meta PPA contribution economics | partially disclosed | Company says guidance excludes benefits and part may begin contributing in 2027, but contract-level economics were not disclosed. |
| Segment-level FCF | not disclosed | Segment revenue and Adjusted EBITDA are available, but segment FCF is not. |
| Required growth capex versus maintenance capex split | partially disclosed | `Adjusted FCFbG` is before growth and non-GAAP; full owner-earnings bridge remains judgment-heavy. |
| Exact current price after market close on 2026-06-03 | not available during market-open check | Market data was checked intraday at 12:00 PM EDT; recheck before any trade. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Needed for personalized sizing. |

## Handoff For Ingest

- Normalize Q1 2026 results from the SEC Form 10-Q and official Q1 2026 release.
- Use FY2025 release / 10-K as annual baseline for revenue, net income, operating cash flow, capex, GAAP-style FCF, Adjusted EBITDA, and Adjusted FCFbG.
- Keep `Adjusted EBITDA`, `Ongoing Operations Adjusted EBITDA`, and `Adjusted FCFbG` separate from GAAP metrics.
- Use GAAP-style `OCF - capex` for normalized FCF and label company `Adjusted FCFbG` as non-GAAP guidance.
- For P11, use current price USD 155.37 checked 2026-06-03 12:00 PM EDT, market cap USD 52.39B, StockAnalysis shares 337.18M, company net debt before cash margin deposits USD 18.628B, preferred stock USD 2.476B, TTM GAAP-style FCF USD 1.803B, and FY2026 consolidated Adjusted FCFbG midpoint USD 4.160B.
- Do not infer segment-level FCF, Cogentrix contribution, Meta PPA economics, or post-2026 actual results.
