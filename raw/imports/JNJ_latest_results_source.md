---
type: source-note
ticker: JNJ
company: Johnson & Johnson
source_kind: latest-results
search_date: 2026-05-19
reporting_scope: Q1 2026 fiscal first quarter ended 2026-03-29 plus FY2025 annual baseline
currency: USD
normalized_output: raw/financials/JNJ_fundamentals.md
entity: "[[JNJ]]"
tags:
  - source/latest-results
  - ticker/JNJ
---

# JNJ - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|
| 1 | SEC Form 10-Q, period ended 2026-03-29 | https://www.sec.gov/Archives/edgar/data/200406/000020040626000087/jnj-20260329.htm | 2026-04-22 | Primary quarterly filing; unaudited USD millions; includes statements, shares, cash flow, balance sheet, segments, debt. |
| 1 | SEC 10-Q filing index | https://www.sec.gov/Archives/edgar/data/200406/000020040626000087/0000200406-26-000087-index.htm | 2026-04-22 | Confirms accession `0000200406-26-000087`. |
| 1 | FY2025 Annual Report / Form 10-K | https://www.jnj.com/download/johnson-johnson-2025-annual-report | 2026 | Annual baseline and FCF reconciliation for FY2025. |
| 2 | Q1 2026 earnings press release | https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-reports-Q1-2026-results-raises-2026-outlook/ | 2026-04-14 | Official IR release; latest results, segment growth, updated FY2026 guidance. |
| 2 | Q1 2026 earnings presentation | https://s203.q4cdn.com/636242992/files/doc_financials/2026/q1/JNJ-Earnings-Presentation-Q1-2026-Final.pdf | 2026-04-14 | Official call deck; capital allocation, cash/debt/FCF, guidance, phasing. |
| 2 | Q1 2026 earnings call transcript | https://s203.q4cdn.com/636242992/files/doc_financials/2026/q1/JNJ-USQ_Transcript_2026-04-14.pdf | 2026-04-14 | IR-hosted LSEG transcript; management commentary, capital allocation, FCF outlook, guidance. |
| 3 | FinanceCharts JNJ price history | https://www.financecharts.com/stocks/JNJ/summary/price | 2026-05-18 current quote page; checked 2026-05-19 Bangkok time | Fresh market-data check for current share price. Lower priority than filings for company facts. |
| 3 | FinanceCharts JNJ overview | https://www.financecharts.com/stocks/JNJ | 2026-05-15 close metrics; checked 2026-05-19 Bangkok time | Cross-check for market cap and valuation context. |

## Reporting Scope

- Company: Johnson & Johnson.
- Ticker / exchange: JNJ, New York Stock Exchange.
- Fiscal period: fiscal first quarter ended March 29, 2026.
- Annual baseline: fiscal year ended December 28, 2025.
- Reporting basis: US GAAP unless explicitly labeled non-GAAP by the company.
- Units: USD millions, except per-share data, percentages, share counts, and market price.

## Currency / Units

- Financial statements: USD millions.
- Guidance: USD billions for sales, dollars per share for adjusted EPS.
- Market data: USD per share and USD billions for calculated market capitalization.

## Extracted Facts

### Identity And Market Data

| Fact | Value | Source |
|---|---:|---|
| Company | Johnson & Johnson | SEC Form 10-Q and J&J IR sources. |
| Ticker / exchange | JNJ / NYSE | SEC Form 10-Q. |
| Current share price | USD 227.54 | FinanceCharts price page, current share price for Monday, 2026-05-18; checked 2026-05-19 Bangkok time. |
| Common shares outstanding | 2,407,216,971 | SEC Form 10-Q: common shares outstanding as of 2026-04-17. |
| Market cap check | USD 547.7B | Calculated: USD 227.54 * 2,407,216,971 shares / 1,000,000,000. |
| Diluted average shares | 2,445.2 million | SEC Form 10-Q, Q1 2026 diluted average shares. |

### Q1 2026 Income Statement

| Metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Sales to customers | 24,062 | 21,893 | SEC Form 10-Q. |
| Gross profit | 15,956 | 14,536 | SEC Form 10-Q. |
| Research and development expense | 3,527 | 3,225 | SEC Form 10-Q. |
| Earnings before provision for taxes | 5,990 | 13,631 | SEC Form 10-Q. |
| Net earnings | 5,235 | 10,999 | SEC Form 10-Q. |
| Diluted EPS | 2.14 | 4.54 | SEC Form 10-Q. |
| Adjusted diluted EPS | 2.70 | not normalized here | J&J Q1 2026 press release; non-GAAP. |

### Q1 2026 Balance Sheet And FCF Inputs

| Metric | 2026-03-29 | 2025-12-28 | Source |
|---|---:|---:|---|
| Cash and cash equivalents | 21,688 | 19,709 | SEC Form 10-Q. |
| Marketable securities | 363 | 393 | SEC Form 10-Q. |
| Cash + marketable securities | 22,051 | 20,102 | Calculated from SEC Form 10-Q. |
| Loans and notes payable | 17,460 | 8,495 | SEC Form 10-Q. |
| Long-term debt | 37,527 | 39,438 | SEC Form 10-Q. |
| Total debt | 54,987 | 47,933 | Calculated: loans and notes payable + long-term debt. |
| Net debt | 32,936 | 27,831 | Calculated: total debt - cash and marketable securities. |
| Total assets | 200,894 | 199,210 | SEC Form 10-Q. |
| Total liabilities | 119,708 | 117,666 | SEC Form 10-Q. |
| Total shareholders' equity | 81,186 | 81,544 | SEC Form 10-Q. |

### Cash Flow

| Metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Net cash flows from operating activities | 2,514 | 4,174 | SEC Form 10-Q. |
| Additions to property, plant and equipment | (1,049) | (795) | SEC Form 10-Q. |
| Free cash flow | 1,465 | 3,379 | Calculated: operating cash flow - capex spend. |

### Annual FCF Baseline And Outlook

| Metric | FY2025 | FY2024 | Source |
|---|---:|---:|---|
| Operating cash flow | 24,530 | 24,266 | FY2025 Annual Report. |
| Capex spend | 4,832 | 4,424 | FY2025 Annual Report. |
| Free cash flow | 19,698 | 19,842 | Calculated: operating cash flow - capex spend. |
| FY2026 FCF outlook | approximately 21,000 | n/a | Q1 2026 earnings call transcript; CFO commentary. |

### Segment And Geographic Results

| Segment / geography | Q1 2026 sales | Q1 2025 sales | YoY change | Source |
|---|---:|---:|---:|---|
| Innovative Medicine | 15,426 | 13,873 | 11.2% reported | SEC Form 10-Q / press release. |
| MedTech | 8,636 | 8,020 | 7.7% reported | SEC Form 10-Q / press release. |
| Worldwide | 24,062 | 21,893 | 9.9% reported | SEC Form 10-Q / press release. |
| United States | 13,330 | 12,305 | 8.3% | SEC Form 10-Q. |
| International | 10,732 | 9,588 | 11.9% | SEC Form 10-Q. |

### Guidance

| Guidance item | April 2026 guidance | Source |
|---|---:|---|
| Adjusted operational sales growth | 5.6% to 6.6%; midpoint 6.1% | J&J Q1 2026 press release / presentation. |
| Operational sales | USD 99.7B to USD 100.7B; midpoint USD 100.2B | J&J Q1 2026 press release / presentation. |
| Estimated reported sales | USD 100.3B to USD 101.3B; midpoint USD 100.8B | J&J Q1 2026 press release / presentation. |
| Adjusted operational diluted EPS | USD 11.30 to USD 11.50; midpoint USD 11.40 | J&J Q1 2026 press release / presentation. |
| Adjusted diluted EPS | USD 11.45 to USD 11.65; midpoint USD 11.55 | J&J Q1 2026 press release / presentation. |
| Adjusted pretax operating margin | improve by at least 50 bps | Q1 2026 earnings call transcript / presentation. |
| Net interest expense / income | USD 300M to USD 400M | Q1 2026 presentation. |
| Effective tax rate | 17.5% to 18.5% | Q1 2026 presentation. |

## Transcript / Commentary

- CEO Joaquin Duato framed 2026 as a year of accelerated growth and impact, supported by Q1 operational sales growth of 6.4% and raised guidance.
- Management highlighted six key businesses: Oncology, Immunology, Neuroscience, Cardiovascular, Surgery, and Vision.
- Q1 worldwide sales were USD 24.1B; operational growth was 6.4%. Management said STELARA was an approximate 540 bps headwind and that J&J grew double digits excluding STELARA.
- Innovative Medicine operational sales grew 7.4%; growth drivers included DARZALEX, CARVYKTI, ERLEADA, RYBREVANT/LAZCLUZE, TREMFYA, and SPRAVATO, offset partly by STELARA and IMBRUVICA pressure.
- MedTech operational sales grew 4.6%; growth drivers included electrophysiology, Abiomed, Shockwave, and trauma.
- CFO Joseph Wolk stated Q1 cash and marketable securities were approximately USD 22B, debt approximately USD 55B, net debt approximately USD 33B, Q1 FCF approximately USD 1.5B, and full-year FCF outlook approximately USD 21B.
- The board authorized a 3.1% dividend increase to an annual rate of USD 5.36 per share, described as the 64th consecutive year of dividend growth.
- The company expects heavier investment in the first half of 2026 and higher EPS growth in the second half.

## Financial Tables

See extracted tables above. P4 should normalize:

- Q1 2026 / Q1 2025 income statement and cash flow.
- March 29, 2026 / December 28, 2025 balance sheet inputs.
- Segment revenue and segment income before tax.
- FY2025 annual FCF baseline.
- Current market price / market cap as lower-priority market data, clearly separated from company facts.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Product-level revenue for several specific launch assets such as ICOTYDE and IMAAVY | not disclosed | Transcript says IMAAVY sales are not disclosed yet. |
| Product-level profitability by brand | not disclosed | Segment income is disclosed, but brand margins are not. |
| GAAP forward guidance | not provided | Company says it does not provide forward-looking GAAP financial measures because certain items cannot be predicted with reasonable certainty. |
| FY2026 full-year actual results | ไม่พบข้อมูลที่ยืนยันได้ | Only Q1 2026 actuals and FY2026 guidance are available. |
| Long-run FCF growth by segment | ไม่พบข้อมูลที่ยืนยันได้ | DCF must use explicit scenario assumptions. |

## Handoff For Ingest

Normalize only verified fields from the tables above into `raw/financials/JNJ_fundamentals.md` and `raw/financials/JNJ_fundamentals.json`.

Then create `wiki/entities/JNJ.md` with the standard entity sections. Keep facts, calculations, and judgment separated. Use `ไม่พบข้อมูลที่ยืนยันได้` or `not disclosed` for missing items. Update `log.md` after each durable output step.
