---
type: source-note
ticker: CRWV
company: CoreWeave, Inc.
source_kind: latest-results
search_date: 2026-05-21
reporting_scope: "Q1 2026 quarter ended 2026-03-31; FY2025 annual baseline; FY2026 guidance; fresh market-data check 2026-05-21"
currency: USD
normalized_output: raw/financials/CRWV_fundamentals.md
entity: "[[CRWV]]"
tags:
  - source/latest-results
  - ticker/CRWV
---

# CRWV - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|
| 1 | Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm | 2026-05-15 | Latest official quarterly filing; used for Q1 statements, cash, debt, leases, share count, and cash flow. |
| 1 | FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm | 2026-03-31 | Annual baseline; used for FY2025, FY2024, FY2023 revenue, cash flow, capex, cash, debt, and business/risk context. |
| 2 | Q1 2026 earnings release | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/default.aspx | 2026-05-07 | Official Q1 results release; used for quarterly revenue, backlog, RPO, adjusted EBITDA, capex, cash, debt, and guidance. |
| 2 | Q1 2026 outlook presentation | https://s205.q4cdn.com/133937190/files/doc_financials/2026/q1/CoreWeave-1Q26-Outlook-Presentation.pdf | 2026-05-07 | Official IR presentation; used for Q2/FY2026 guidance and quarterly revenue / adjusted EBITDA trend. |
| 2 | Q1 2026 earnings call transcript | https://s205.q4cdn.com/133937190/files/doc_financials/2026/q1/CoreWeave-Inc-CRWV-US-Q1-2026-Earnings-Call-7-May-2026-5_00-PM-ET.pdf | 2026-05-07 | Company-hosted transcript PDF; used for management commentary on demand, capacity, capex, leverage, and guidance context. |
| 3 | StockAnalysis CRWV quote | https://stockanalysis.com/stocks/crwv/ | 2026-05-21 check | Fresh market-data check: close 2026-05-20 and pre-market 2026-05-21; provider data, not company fact. |
| 3 | StockAnalysis CRWV statistics | https://stockanalysis.com/stocks/crwv/statistics/ | 2026-05-21 check | Provider statistics for enterprise value and total debt cross-check; official filings remain primary. |
| 4 | CoreWeave DDTL 5.0 facility announcement | https://www.businesswire.com/news/home/20260519713510/en/CoreWeave-Closes-%243.1-Billion-Loan-Facility | 2026-05-19 | Post-quarter financing context; not treated as quarter-end debt outstanding without a filing-level draw schedule. |

## Reporting Scope

- Company: CoreWeave, Inc.
- Ticker / Exchange: CRWV / Nasdaq Global Select Market.
- Latest official financial period found: quarter ended 2026-03-31.
- Annual baseline: fiscal years ended 2025-12-31, 2024-12-31, and 2023-12-31 from FY2025 Form 10-K.
- Reporting basis: U.S. GAAP unless explicitly labeled adjusted EBITDA, adjusted operating income, or company-defined capex.

## Currency / Units

- Currency: USD.
- SEC financial tables: USD thousands, converted to USD millions in normalized outputs.
- Earnings release and presentation tables: USD millions unless otherwise stated.
- Per-share market data: USD per Class A common share.
- Market cap and enterprise value: USD billions as labeled by provider.

## Extracted Facts

### Latest Official Results

| Metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Revenue | 2,078 | 982 | Q1 2026 Form 10-Q / earnings release |
| Income / loss from operations | (144) | (270) | Q1 2026 Form 10-Q |
| Net loss | (740) | (315) | Q1 2026 Form 10-Q / earnings release |
| Adjusted operating income | 21 | 163 | Q1 2026 earnings release / outlook presentation |
| Adjusted EBITDA | 1,157 | 606 | Q1 2026 earnings release / outlook presentation |
| Capital expenditures, company-defined | 6,786 | 1,858 | Q1 2026 earnings release |

### Cash Flow / FCF

| Metric | Q1 2026 | Q1 2025 | FY2025 | FY2024 | FY2023 | Source |
|---|---:|---:|---:|---:|---:|---|
| Net cash provided by operating activities | 2,984 | 61 | 3,058 | 2,749 | 1,833 | Q1 2026 Form 10-Q; FY2025 Form 10-K |
| Purchases of property and equipment, including capitalized internal-use software | 7,695 | 1,407 | 10,309 | 8,702 | 2,943 | Q1 2026 Form 10-Q; FY2025 Form 10-K |
| Free cash flow | (4,711) | (1,346) | (7,251) | (5,953) | (1,110) | Calculation: OCF - cash capex |

Calculation:

```text
Q1 2026 FCF = operating cash flow 2,984 - purchases of property and equipment / capitalized software 7,695 = -4,711
TTM FCF = FY2025 FCF -7,251 + Q1 2026 FCF -4,711 - Q1 2025 FCF -1,346 = -10,616
```

### Balance Sheet / Debt

| Metric | 2026-03-31 | 2025-12-31 | Source |
|---|---:|---:|---|
| Cash and cash equivalents | 2,244 | 2,644 | Q1 2026 Form 10-Q |
| Marketable securities | 22 | 24 | Q1 2026 Form 10-Q |
| Cash and marketable securities | 2,266 | 2,668 | Calculation from Q1 2026 Form 10-Q |
| Cash, restricted cash, and marketable securities | 3,342 | 3,602 | Q1 2026 Form 10-Q / earnings release |
| Debt, current | 7,547 | 3,455 | Q1 2026 Form 10-Q |
| Debt, non-current | 17,312 | 14,699 | Q1 2026 Form 10-Q |
| Total debt excluding leases | 24,859 | 18,154 | Calculation from Q1 2026 Form 10-Q |
| Operating lease liabilities | 10,050 | 9,169 | Q1 2026 Form 10-Q |
| Finance lease liabilities | 238 | 85 | Q1 2026 Form 10-Q |
| Total debt-like obligations including leases | 35,147 | 27,408 | Calculation from Q1 2026 Form 10-Q |
| Total assets | 55,573 | 34,064 | Q1 2026 Form 10-Q |
| Total liabilities | 50,814 | 35,461 | Q1 2026 Form 10-Q |
| Stockholders' equity / deficit | 4,759 | (1,397) | Q1 2026 Form 10-Q |

### Shares

| Metric | Value | Source |
|---|---:|---|
| Class A common shares outstanding at 2026-04-30 | 447,573,939 | Q1 2026 Form 10-Q cover page |
| Class B common shares outstanding at 2026-04-30 | 97,996,407 | Q1 2026 Form 10-Q cover page |
| Total shares outstanding at 2026-04-30 | 545,570,346 | Calculation from Q1 2026 Form 10-Q cover page |
| Weighted-average diluted shares, Q1 2026 | 408,799,000 | Q1 2026 Form 10-Q; anti-dilutive due net loss |
| Provider shares outstanding | 545.57M | StockAnalysis quote checked 2026-05-21 |

### Backlog / RPO / Guidance

| Metric | Value | Source |
|---|---:|---|
| Revenue backlog | 99,355 | Q1 2026 earnings release |
| Remaining performance obligations | 98,767 | Q1 2026 earnings release |
| Adjusted EBITDA backlog | 62,983 | Q1 2026 earnings release |
| Q2 2026 revenue guidance | 2,450 to 2,600 | Q1 2026 outlook presentation |
| Q2 2026 adjusted operating income guidance | 30 to 90 | Q1 2026 outlook presentation |
| Q2 2026 capital expenditures guidance | 7,000 to 9,000 | Q1 2026 outlook presentation |
| Q2 2026 interest expense guidance | 650 to 730 | Q1 2026 outlook presentation |
| FY2026 revenue guidance | 12,000 to 13,000 | Q1 2026 outlook presentation |
| FY2026 adjusted operating income guidance | 900 to 1,100 | Q1 2026 outlook presentation |
| FY2026 capital expenditures guidance | 31,000 to 35,000 | Q1 2026 outlook presentation |
| FY2026 exit ARR guidance | 18,000 to 19,000 | Q1 2026 outlook presentation |

### Fresh Market-Data Check

| Metric | Value | Timestamp / Basis | Source |
|---|---:|---|---|
| Close price | 101.28 | At close 2026-05-20 4:00 PM EDT | StockAnalysis quote checked 2026-05-21 |
| Pre-market price | 105.95 | 2026-05-21 8:15 AM EDT | StockAnalysis quote checked 2026-05-21 |
| Market cap | 55.26B | Provider value on quote page | StockAnalysis quote checked 2026-05-21 |
| Enterprise value | 88.14B | Provider value on statistics page | StockAnalysis checked 2026-05-21 |
| Shares out | 545.57M | Provider value on quote page | StockAnalysis quote checked 2026-05-21 |
| TTM revenue | 6.23B | Provider value; reconciles to SEC-based TTM calculation | StockAnalysis checked 2026-05-21 |
| TTM FCF | (10.62B) | Provider value; reconciles to SEC-based TTM calculation | StockAnalysis checked 2026-05-21 |
| EV / TTM revenue | 14.15x | Provider value; EV 88.14B / TTM revenue 6.23B | StockAnalysis checked 2026-05-21 |

## Transcript / Commentary

- Management framed demand as constrained by available capacity rather than lack of customers. The call emphasized expansion of the platform and very large backlog.
- Management said full-year 2026 revenue guidance is USD 12B to USD 13B, with exit ARR guidance of USD 18B to USD 19B.
- The call and outlook materials point to very high capex intensity, with FY2026 capex guidance of USD 31B to USD 35B and Q2 capex guidance of USD 7B to USD 9B.
- Management discussed leverage and financing flexibility, but no source-backed FY2026 FCF guidance was found in the official materials.

## Financial Tables

The extracted facts above are the handoff tables for P4 normalization. All normalized financial-statement figures should use USD millions, converted from SEC USD thousands when needed.

## Missing / Unverified Data

- FY2026 full-year actual results are not available as of the 2026-05-21 source check.
- FY2026 free cash flow guidance is not disclosed.
- A source-backed positive normalized FCF base is not available; FY2025, Q1 2026, and TTM FCF are all negative by `OCF - cash capex`.
- Revenue by product line, customer type, or individual major customer is not fully disclosed.
- Segment-level operating income and segment-level FCF are not disclosed.
- Post-quarter DDTL 5.0 draw amounts and exact pro forma debt outstanding are not verified in a filing-level balance sheet.
- GAAP net income or EPS guidance for FY2026 was not verified.
- Current market quote is provider-sourced and pre-market on 2026-05-21, not a company filing and not a post-2026-05-21 close.
- Investor-specific cost basis, position size, tax status, and required return were not provided.

## Handoff For Ingest

- Normalize Q1 2026 and Q1 2025 quarterly financials from the Q1 2026 Form 10-Q and official earnings release.
- Normalize FY2025, FY2024, and FY2023 annual cash flow and revenue baseline from the FY2025 Form 10-K.
- Use Q1 2026 FCF = OCF 2,984 - cash capex 7,695 = -4,711.
- Use TTM FCF = FY2025 FCF -7,251 + Q1 2026 FCF -4,711 - Q1 2025 FCF -1,346 = -10,616.
- Use cash and marketable securities 2,266, total debt excluding leases 24,859, total debt-like obligations including leases 35,147, and total shares outstanding 545.570346M.
- Record source gaps rather than inferring FY2026 FCF guidance, positive normalized FCF, product-level profitability, or pro forma debt after post-quarter financing.
