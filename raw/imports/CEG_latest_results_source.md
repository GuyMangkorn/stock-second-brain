---
type: source-note
ticker: CEG
company: Constellation Energy Corporation
source_kind: latest-results
search_date: 2026-05-31
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline and fresh 2026-05-31 market-data check
currency: USD
normalized_output: raw/financials/CEG_fundamentals.md
entity: "[[CEG]]"
tags:
  - source/latest-results
  - ticker/CEG
---

# CEG - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|
| 1 | SEC Form 10-Q filing detail | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000067/0001868275-26-000067-index.htm | 2026-05-11 | Primary Q1 2026 filing, accession `0001868275-26-000067`, period ended 2026-03-31. |
| 1 | SEC Form 10-Q document | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000067/ceg-20260331.htm | 2026-05-11 | Primary quarterly statements, segment revenue, cash flow, balance sheet, debt, and shares. |
| 1 | Constellation Q1 2026 Form 10-Q PDF | https://investors.constellationenergy.com/static-files/d490ed49-5b20-4619-b6f7-65fcb90c7e99 | 2026-05-11 | IR-hosted official 10-Q PDF used for line-level extraction. |
| 1 | Form 8-K / Q1 2026 release and presentation | https://investors.constellationenergy.com/static-files/9dc0168f-5328-42ce-9d66-2c3abe07bff0 | 2026-05-11 | Official results release, Q1 highlights, guidance, and presentation. |
| 1 | Q1 2026 earnings presentation | https://investors.constellationenergy.com/static-files/e5a93793-71b7-453f-a5d3-6a8acb420282 | 2026-05-11 | Official presentation for Base EPS growth, FCF before growth, capacity, and capital allocation context. |
| 1 | FY2025 Form 10-K / annual report | https://investors.constellationenergy.com/static-files/8d46f4dc-04f9-4916-aa5d-e12bd5c45aa7 | 2026-02-24 | FY2025 annual baseline, cash flow, segment data, adjusted operating earnings, and risk context. |
| 2 | Official Q1 2026 webcast event page | https://investors.constellationenergy.com/events/event-details/q1-2026-constellation-energy-corporation-earnings-conference-call/ | 2026-05-11 | Company-hosted webcast and supporting material links. No official written transcript was verified. |
| 3 | Twelve Data CEG historical quote page | https://twelvedata.com/markets/736051/stock/nasdaq/ceg/historical-data | checked 2026-05-31 | Fresh market-data check: latest regular-market close found was 2026-05-29. |

## Reporting Scope

- Latest quarter: Q1 2026, three months ended 2026-03-31.
- Annual baseline: FY2025, year ended 2025-12-31.
- Fiscal year end: December 31.
- Reporting basis: unaudited US GAAP for Q1 2026 statements. `Adjusted Operating Earnings`, `Base EPS`, and `free cash flow before growth` are company-defined non-GAAP measures.
- P1 note scope: source discovery and extracted source facts only. Normalization and entity updates belong to P4.

## Currency / Units

- Currency: USD.
- Units: USD millions unless stated as billions, per-share data, share counts, percentages, GWh, MW, or MWh.
- Cash-flow formula used for GAAP-style FCF in the ingest handoff: `FCF = operating cash flow - capital expenditures`, with capex shown as positive spend in local notes.

## Extracted Facts

### Q1 2026 Highlights

| Fact | Value | Source |
|---|---:|---|
| Operating revenues | USD 11.122B, up 63.8% YoY | Q1 2026 Form 10-Q / release. |
| GAAP net income attributable to common shareholders | USD 1.590B | Q1 2026 Form 10-Q / release. |
| GAAP EPS | USD 4.49 | Q1 2026 release. |
| Adjusted Operating Earnings | USD 972M | Q1 2026 release; non-GAAP. |
| Adjusted Operating EPS | USD 2.74 | Q1 2026 release; non-GAAP. |
| Operating income | USD 2.332B | Q1 2026 Form 10-Q. |
| Weighted-average diluted shares | 354M | Q1 2026 release. |
| Shares outstanding at 2026-03-31 | 362.359M | Q1 2026 Form 10-Q statement of equity. |
| Cash and cash equivalents | USD 800M | Q1 2026 Form 10-Q balance sheet. |
| Restricted cash and cash equivalents | USD 371M | Q1 2026 Form 10-Q balance sheet. |
| Cash, restricted cash, and cash equivalents | USD 1.171B | Q1 2026 Form 10-Q cash-flow reconciliation. |
| Short-term borrowings | USD 5.102B | Q1 2026 Form 10-Q balance sheet. |
| Long-term debt due within one year | USD 370M | Q1 2026 Form 10-Q balance sheet. |
| Long-term debt | USD 16.994B | Q1 2026 Form 10-Q balance sheet. |
| Total debt used locally | USD 22.466B | Calculation: 5.102 + 0.370 + 16.994. |
| Net debt used locally | USD 21.295B | Calculation: 22.466 - 1.171. |
| Cash from operating activities | USD 425M | Q1 2026 Form 10-Q cash-flow statement. |
| Capital expenditures | USD 1.275B | Q1 2026 Form 10-Q cash-flow statement; capex as positive spend locally. |
| GAAP-style free cash flow | USD (850)M | Calculation: 425 - 1,275. |

### Segment Revenue And Operating Data

| Segment / metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Mid-Atlantic operating revenues | 1,847 | 1,665 | Q1 2026 Form 10-Q. |
| Midwest operating revenues | 1,732 | 1,404 | Q1 2026 Form 10-Q. |
| New York operating revenues | 569 | 562 | Q1 2026 Form 10-Q. |
| ERCOT operating revenues | 370 | 398 | Q1 2026 Form 10-Q. |
| Other Power Regions operating revenues | 1,487 | 1,556 | Q1 2026 Form 10-Q. |
| Calpine operating revenues | 2,395 | not applicable | Q1 2026 Form 10-Q; Calpine acquired in January 2026. |
| Total reportable segment revenues | 8,400 | 5,585 | Q1 2026 Form 10-Q. |
| Other operating revenues | 1,407 | 1,490 | Q1 2026 Form 10-Q. |
| Unrealized gains / losses | 1,315 | (287) | Q1 2026 Form 10-Q. |
| Total operating revenues | 11,122 | 6,788 | Q1 2026 Form 10-Q. |
| Nuclear generation | 44,666 GWh | 45,582 GWh | Q1 2026 release. |
| Nuclear capacity factor | 92.3% | 94.1% | Q1 2026 release; excludes Salem and STP. |
| Planned refueling outage days | 99 | 88 | Q1 2026 release. |
| Non-refueling outage days | 0 | 0 | Q1 2026 release. |
| Natural gas, oil, and pumped-storage hydro EFOF | 4.5% | not disclosed | Q1 2026 release; new key metric after Calpine. |
| Renewable energy capture | 96.7% | 96.2% | Q1 2026 release. |

### FY2025 Annual Baseline

| Fact | Value | Source |
|---|---:|---|
| FY2025 operating revenues | USD 25.533B | FY2025 Form 10-K. |
| FY2025 operating income | USD 3.086B | FY2025 Form 10-K. |
| FY2025 GAAP net income attributable to common shareholders | USD 2.319B | FY2025 Form 10-K. |
| FY2025 GAAP diluted EPS | USD 7.40 | FY2025 Form 10-K. |
| FY2025 Adjusted Operating Earnings | USD 2.944B | FY2025 Form 10-K; non-GAAP. |
| FY2025 Adjusted Operating EPS | USD 9.39 | FY2025 Form 10-K; non-GAAP. |
| FY2025 operating cash flow | USD 4.237B | FY2025 Form 10-K. |
| FY2025 capital expenditures | USD 2.949B | FY2025 Form 10-K; capex as positive spend locally. |
| FY2025 GAAP-style free cash flow | USD 1.288B | Calculation: 4.237 - 2.949. |
| FY2025 diluted shares | 314M | FY2025 Form 10-K. |

## Transcript / Commentary

- Official written transcript / Q&A was not verified. The official webcast page was found, and the official 8-K / presentation were used for management commentary.
- Management affirmed full-year 2026 Adjusted Operating Earnings guidance of USD 11.00-12.00 per share.
- Presentation states full-year 2026 guidance is based on expected average diluted common shares outstanding of 361M.
- Presentation frames Constellation as a larger post-Calpine fleet with about 55 GW of capacity across nuclear, natural gas, oil, geothermal, hydro, wind, and solar.
- Management highlighted `20%+` Base EPS growth through 2029, long-term rolling three-year Base EPS growth target of `10%+`, an increased share buyback authorization to USD 5.0B, and USD 3.9B of growth capital projects.
- Presentation gives expected free cash flow before growth of USD 8.4B across 2026-2027 and USD 11.5B-13.0B across 2028-2029. This is non-GAAP and not the same as GAAP `OCF - capex`.

## Financial Tables

### Income Statement Summary

| Metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Operating revenues | 11,122 | 6,788 | Q1 2026 Form 10-Q. |
| Purchased power and fuel | 6,352 | 4,384 | Q1 2026 release. |
| Operating and maintenance | 1,780 | 1,545 | Q1 2026 release. |
| Depreciation and amortization | 443 | 248 | Q1 2026 release. |
| Taxes other than income taxes | 229 | 160 | Q1 2026 release. |
| Total operating expenses | 8,804 | 6,337 | Q1 2026 release. |
| Operating income | 2,332 | 451 | Q1 2026 release. |
| Interest expense, net | 253 | 146 | Q1 2026 release. |
| Net income attributable to common shareholders | 1,590 | 118 | Q1 2026 release / Form 10-Q. |
| GAAP EPS | 4.49 | 0.38 | Q1 2026 release. |
| Adjusted Operating Earnings | 972 | 673 | Q1 2026 release; non-GAAP. |
| Adjusted Operating EPS | 2.74 | 2.14 | Q1 2026 release; non-GAAP. |
| Weighted-average diluted shares | 354 | 314 | Q1 2026 release. |

### Cash Flow Reconciliation

| Metric | Q1 2026 | Q1 2025 | FY2025 | Source |
|---|---:|---:|---:|---|
| Cash from operating activities | 425 | 107 | 4,237 | Q1 2026 Form 10-Q / FY2025 Form 10-K. |
| Capital expenditures | 1,275 | 806 | 2,949 | Q1 2026 Form 10-Q / FY2025 Form 10-K; capex shown as positive spend. |
| GAAP-style free cash flow | (850) | (699) | 1,288 | Calculation: operating cash flow - capex. |
| TTM GAAP-style free cash flow | 1,137 | not applicable | not applicable | Calculation: FY2025 FCF 1,288 - Q1 2025 FCF (699) + Q1 2026 FCF (850). |
| Free cash flow before growth | 8.4B across 2026-2027 | not applicable | not applicable | Company presentation; non-GAAP. |
| Free cash flow before growth | 11.5B-13.0B across 2028-2029 | not applicable | not applicable | Company presentation; non-GAAP. |

### Balance Sheet Snapshot

| Metric | 2026-03-31 | 2025-12-31 | Source |
|---|---:|---:|---|
| Cash and cash equivalents | 800 | 3,641 | Q1 2026 Form 10-Q. |
| Restricted cash and cash equivalents | 371 | 107 | Q1 2026 Form 10-Q. |
| Cash, restricted cash, and cash equivalents | 1,171 | 3,748 | Q1 2026 Form 10-Q cash-flow reconciliation. |
| Current assets | 18,009 | 12,119 | Q1 2026 Form 10-Q. |
| Total assets | 96,911 | 57,249 | Q1 2026 Form 10-Q. |
| Short-term borrowings | 5,102 | 1,650 | Q1 2026 Form 10-Q. |
| Long-term debt due within one year | 370 | 92 | Q1 2026 Form 10-Q. |
| Long-term debt | 16,994 | 7,250 | Q1 2026 Form 10-Q. |
| Total debt used locally | 22,466 | 8,992 | Calculation from Q1 2026 Form 10-Q balance sheet. |
| Total liabilities | 63,091 | 42,396 | Q1 2026 Form 10-Q. |
| Total equity | 33,820 | 14,853 | Q1 2026 Form 10-Q. |
| Shares outstanding | 362.359M | 312.355M | Q1 2026 Form 10-Q statement of equity. |

### Guidance / Market Data

| Metric | Value | Source / Calculation |
|---|---:|---|
| FY2026 Adjusted Operating EPS guidance | USD 11.00-12.00 | Q1 2026 release / presentation; non-GAAP. |
| FY2026 expected average diluted shares | 361M | Q1 2026 presentation. |
| Base EPS growth target through 2029 | 20%+ | Q1 2026 presentation; non-GAAP. |
| Long-term rolling three-year Base EPS growth target | 10%+ | Q1 2026 presentation; non-GAAP. |
| FCF before growth, 2026-2027 | USD 8.4B aggregate | Q1 2026 presentation; non-GAAP. |
| FCF before growth, 2028-2029 | USD 11.5B-13.0B aggregate | Q1 2026 presentation; non-GAAP. |
| Latest market close checked | USD 287.75 on 2026-05-29, 3:59 PM EDT | Twelve Data historical quote page, checked 2026-05-31. |
| Market cap cross-check | USD 104.27B | Calculation: USD 287.75 * 362.359M shares outstanding. |
| Market EV cross-check | USD 125.56B | Market cap + net debt 21.295B. |

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Full FY2026 actual results | not disclosed | Q1 2026 is the latest official period found. |
| Official written Q1 2026 earnings call transcript / full Q&A | not verified | Company webcast was found, but no official text transcript was verified. |
| GAAP reconciliation for forward `Base EPS` and `free cash flow before growth` | not fully disclosed | Forward non-GAAP guide should not be treated as GAAP FCF. |
| Segment-level operating income and FCF | not disclosed | Segment table discloses revenues / RNF style context, not segment-level FCF. |
| Durable post-Calpine run-rate FCF after growth capex | partially disclosed | FCF before growth is disclosed as an aggregate non-GAAP guide, while GAAP-style TTM FCF is much lower. |
| Product/customer-level profitability for data-center, powered-land, nuclear, and gas contracts | not disclosed | Important for underwriting premium demand narrative. |
| Exact future regulatory outcomes for PJM, ERCOT, nuclear PTC, co-location, and large-load contracting | not knowable | Material to long-term value and contracting economics. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Needed for personalized add/trim sizing. |

## Handoff For Ingest

- Normalize Q1 2026 financial facts from the official Form 10-Q and Q1 2026 release.
- Use FY2025 Form 10-K as annual baseline for revenue, net income, adjusted operating earnings, OCF, capex, FCF, shares, and segment context.
- Use GAAP-style `OCF - capex` FCF in normalized facts and separately label company `free cash flow before growth` as non-GAAP guidance.
- For P11, do not treat FCF before growth as equivalent to GAAP FCF. Use it as a scenario valuation anchor, and show GAAP TTM FCF as a sanity check.
- Use Twelve Data only for fresh market-data check; use SEC / official filing share count for company facts.
