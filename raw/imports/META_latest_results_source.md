---
type: source-note
ticker: META
company: Meta Platforms, Inc.
source_kind: latest-results
search_date: 2026-06-10
reporting_scope: Q1 2026, quarter ended 2026-03-31
currency: USD
normalized_output: raw/financials/META_fundamentals.md
entity: "[[META]]"
tags:
  - source/latest-results
  - ticker/META
---

# META - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|
| 1 | SEC submissions API | https://data.sec.gov/submissions/CIK0001326801.json | Checked 2026-06-10 | Confirms CIK `0001326801`, ticker `META`, Nasdaq, fiscal year end 12-31, latest 10-Q and earnings 8-K accessions. |
| 1 | SEC Form 10-Q document | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm | 2026-04-30 filing date; signed 2026-04-29 | Q1 2026 Form 10-Q, period of report 2026-03-31, accession `0001628280-26-028526`. |
| 2 | SEC Form 8-K earnings release exhibit 99.1 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028364/meta-03312026xexhibit991.htm | 2026-04-29 | Official Q1 2026 earnings release, financial tables, segment results, FCF reconciliation, guidance, and CFO outlook. |
| 1 | SEC FY2025 Form 10-K document | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm | 2026-01-29 filing date | FY2025 annual baseline and annual cash-flow history. |
| 3 | SEC companyfacts API | https://data.sec.gov/api/xbrl/companyfacts/CIK0001326801.json | Checked 2026-06-10 | Structured XBRL facts used to cross-check annual and quarterly financial fields. |
| 3 | Nasdaq quote API | https://api.nasdaq.com/api/quote/META/info?assetclass=stocks | Checked 2026-06-10 12:52 PM ET | Fresh intraday quote. Market data only, not official company fact. |
| 3 | Nasdaq summary API | https://api.nasdaq.com/api/quote/META/summary?assetclass=stocks | Checked 2026-06-10 | Fresh market capitalization. Market data only, not official company fact. |
| 3 | Yahoo Finance chart API | https://query1.finance.yahoo.com/v8/finance/chart/META?range=1d&interval=1m | Checked 2026-06-10 12:51:30 PM ET | Cross-check quote and intraday OHLC/volume. Market data only. |

## Reporting Scope

- Company: Meta Platforms, Inc.
- Ticker: `META`, Class A common stock on Nasdaq Global Select Market.
- CIK: `0001326801`.
- Fiscal year end: December 31.
- Latest official reporting period found: Q1 2026, quarter ended March 31, 2026.
- Reporting basis: unaudited US GAAP for Q1 2026; FY2025 annual baseline from audited Form 10-K and SEC companyfacts.
- Currency and units: USD millions unless stated otherwise.

## Currency / Units

All financial statement amounts below are USD millions unless stated otherwise. Per-share figures are USD per share. Share counts are stated in millions or billions as labeled. Market capitalization is stated in USD.

## Extracted Facts

### Filing Identity

| Fact | Value | Source |
|---|---:|---|
| SEC CIK | 0001326801 | SEC submissions API. |
| Latest 10-Q accession | 0001628280-26-028526 | SEC submissions API and Form 10-Q. |
| Latest 10-Q filing date | 2026-04-30 | SEC submissions API. |
| Latest 10-Q period of report | 2026-03-31 | SEC submissions API and Form 10-Q. |
| Earnings 8-K accession | 0001628280-26-028364 | SEC submissions API. |
| Earnings release date | 2026-04-29 | SEC 8-K Exhibit 99.1. |
| FY2025 10-K accession | 0001628280-26-003942 | SEC submissions API. |
| FY2025 10-K filing date | 2026-01-29 | SEC submissions API. |

### Q1 2026 Income Statement

| Metric | Q1 2025 | Q1 2026 | YoY Change | Source |
|---|---:|---:|---:|---|
| Revenue | 42,314 | 56,311 | 33% | SEC 8-K Exhibit 99.1 and Q1 2026 Form 10-Q. |
| Costs and expenses | 24,759 | 33,439 | 35% | SEC 8-K Exhibit 99.1. |
| Income from operations | 17,555 | 22,872 | 30% | SEC 8-K Exhibit 99.1 and companyfacts. |
| Operating margin | 41% | 41% | unchanged | SEC 8-K Exhibit 99.1. |
| Provision (benefit) for income taxes | 1,738 | (5,021) | NM | SEC 8-K Exhibit 99.1. |
| Net income | 16,644 | 26,773 | 61% | SEC 8-K Exhibit 99.1 and companyfacts. |
| Diluted EPS | 6.43 | 10.44 | 62% | SEC 8-K Exhibit 99.1. |
| Weighted-average diluted shares | 2,590 | 2,564 | -1.0% | SEC 8-K Exhibit 99.1 and companyfacts. |

Q1 2026 includes an USD 8.03 billion income tax benefit. Meta says excluding this benefit, diluted EPS would have been USD 3.13 lower.

### Q1 2026 Operating Metrics And Cash Flow

| Metric | Q1 2025 | Q1 2026 | Source |
|---|---:|---:|---|
| Family daily active people | not in extracted table | 3.56 billion average for March 2026 | SEC 8-K Exhibit 99.1. |
| Ad impressions delivered across Family of Apps | not disclosed as absolute value | +19% YoY | SEC 8-K Exhibit 99.1. |
| Average price per ad | not disclosed as absolute value | +12% YoY | SEC 8-K Exhibit 99.1. |
| Net cash provided by operating activities | 24,026 | 32,226 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Purchases of property and equipment | (12,941) | (18,997) | SEC 8-K Exhibit 99.1 and companyfacts. |
| Principal payments on finance leases | (751) | (843) | SEC 8-K Exhibit 99.1 and companyfacts. |
| Free cash flow | 10,334 | 12,386 | SEC 8-K Exhibit 99.1 company non-GAAP reconciliation. |
| Capital expenditures including principal payments on finance leases | not in extracted table | 19,840 | SEC 8-K Exhibit 99.1. |
| Headcount | not in extracted table | 77,986 | SEC 8-K Exhibit 99.1. |

### Balance Sheet Snapshot

| Metric | 2025-12-31 | 2026-03-31 | Source |
|---|---:|---:|---|
| Cash and cash equivalents | 35,873 | 23,426 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Marketable securities | 45,719 | 57,754 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Cash, cash equivalents, and marketable securities | 81,592 | 81,180 | SEC 8-K Exhibit 99.1. |
| Accounts receivable, net | 19,769 | 17,470 | SEC 8-K Exhibit 99.1. |
| Total current assets | 108,722 | 109,765 | SEC 8-K Exhibit 99.1. |
| Property and equipment, net | 176,400 | 194,776 | SEC 8-K Exhibit 99.1. |
| Total assets | 366,021 | 395,250 | SEC 8-K Exhibit 99.1. |
| Total current liabilities | 41,836 | 46,753 | SEC 8-K Exhibit 99.1. |
| Operating lease liabilities, non-current | 22,940 | 25,607 | SEC 8-K Exhibit 99.1. |
| Long-term debt | 58,744 | 58,748 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Total liabilities | 148,778 | 151,569 | SEC 8-K Exhibit 99.1. |
| Total stockholders' equity | 217,243 | 243,681 | SEC 8-K Exhibit 99.1. |

### Q1 2026 Segment Results

| Segment / line | Q1 2025 Revenue | Q1 2026 Revenue | Q1 2025 Operating Income (Loss) | Q1 2026 Operating Income (Loss) | Source |
|---|---:|---:|---:|---:|---|
| Advertising | 41,392 | 55,024 | not applicable | not applicable | SEC 8-K Exhibit 99.1. |
| Other revenue | 510 | 885 | not applicable | not applicable | SEC 8-K Exhibit 99.1. |
| Family of Apps | 41,902 | 55,909 | 21,765 | 26,900 | SEC 8-K Exhibit 99.1. |
| Reality Labs | 412 | 402 | (4,210) | (4,028) | SEC 8-K Exhibit 99.1. |
| Total | 42,314 | 56,311 | 17,555 | 22,872 | SEC 8-K Exhibit 99.1. |

### FY2025 Annual Baseline

| Metric | FY2023 | FY2024 | FY2025 | Source |
|---|---:|---:|---:|---|
| Revenue | 134,902 | 164,501 | 200,966 | SEC companyfacts / FY2025 Form 10-K accession `0001628280-26-003942`. |
| Operating income | 46,751 | 69,380 | 83,276 | SEC companyfacts / FY2025 Form 10-K. |
| Net income | 39,098 | 62,360 | 60,458 | SEC companyfacts / FY2025 Form 10-K. |
| Net cash provided by operating activities | 71,113 | 91,328 | 115,800 | SEC companyfacts / FY2025 Form 10-K. |
| Purchases of property and equipment | (27,045) | (37,256) | (69,691) | SEC companyfacts / FY2025 Form 10-K. |
| Principal payments on finance leases | ไม่พบข้อมูลที่ยืนยันได้ใน P1 table | (1,969) | (2,524) | SEC companyfacts. |
| Free cash flow using company method | ไม่พบข้อมูลที่ยืนยันได้ | 52,103 | 43,585 | Calculated: OCF - capex spend - finance lease principal. |

## Transcript / Commentary

| Topic | Extracted fact / commentary | Source |
|---|---|---|
| Q2 2026 revenue guidance | Meta expects Q2 2026 total revenue of USD 58-61 billion. | SEC 8-K Exhibit 99.1 CFO Outlook Commentary. |
| FX assumption | Guidance assumes foreign currency is approximately a 2% tailwind to YoY total revenue growth. | SEC 8-K Exhibit 99.1. |
| FY2026 expenses guidance | Full-year 2026 total expenses expected at USD 162-169 billion, unchanged from prior outlook. | SEC 8-K Exhibit 99.1. |
| FY2026 operating income direction | Meta expects 2026 operating income above 2025 operating income. | SEC 8-K Exhibit 99.1. |
| FY2026 capex guidance | Capital expenditures including principal payments on finance leases expected at USD 125-145 billion, up from prior USD 115-135 billion. | SEC 8-K Exhibit 99.1. |
| Capex driver | Higher component pricing and additional data center costs to support future-year capacity. | SEC 8-K Exhibit 99.1. |
| Tax rate | Remaining 2026 quarters expected tax rate of 13%-16% absent tax landscape changes. | SEC 8-K Exhibit 99.1. |
| Legal/regulatory caution | Meta continues to monitor EU and U.S. matters, youth-related scrutiny, and trials that may result in a material loss. | SEC 8-K Exhibit 99.1. |

## Financial Tables

The tables above are the P4 ingest handoff tables. Normalize only verified source fields and keep market data separate from company-filed financial facts.

## Missing / Unverified Data

| Data item | Status | Handling |
|---|---|---|
| Product-level AI revenue, AI ad-tool revenue, Meta AI revenue, and AI infrastructure ROI | Not disclosed | Treat as thesis variable, not a financial fact. |
| Reality Labs product-level gross margin, AR glasses economics, and unit volume | Not disclosed | Do not infer unit economics from segment revenue/loss alone. |
| Segment-level free cash flow | Not disclosed | Use consolidated FCF only. |
| Full FY2026 actual results | Not yet reported | Use Q1 2026, TTM, and guidance only. |
| Exact remaining-quarter 2026 capex cadence | Not disclosed | Use full-year guidance range only. |
| Official company-provided current market cap | Not a company filing item | Use market-data source note with check timestamp. |
| Investor-specific position size, tax basis, and required return | Not provided | Decision memo should separate new-capital action from existing-position sizing. |

## Handoff For Ingest

Normalize only verified source fields:

- Company identity: Meta Platforms, Inc.; ticker `META`; Nasdaq; USD; fiscal year end December 31.
- Latest period: Q1 2026, quarter ended March 31, 2026.
- Core quarterly income statement: revenue, costs and expenses, income from operations, operating margin, tax provision/benefit, net income, diluted EPS, diluted shares.
- Cash flow: Q1 2026 and Q1 2025 OCF, capex spend, finance lease principal payments, FCF; annual FY2023-FY2025 OCF/capex where available.
- Balance sheet: cash, marketable securities, cash + marketable securities, current assets, PPE, total assets, current liabilities, operating leases, long-term debt, total liabilities, equity.
- Segment results: Family of Apps and Reality Labs revenue and operating income/loss, advertising revenue and other revenue.
- Management commentary: Q2 revenue guidance, FY2026 expense guidance, FY2026 capex guidance, tax rate range, legal/regulatory caveats.
- Market data for valuation: use `raw/imports/META_market_quote_2026-06-10.md`; label as market data, not company fact.
