---
type: source-note
ticker: AAPL
company: Apple Inc.
source_kind: market-quote
search_date: 2026-06-11
reporting_scope: market data checked 2026-06-10 EDT
currency: USD
entity: "[[AAPL]]"
tags:
  - source/market-data
  - ticker/AAPL
---

# AAPL - Market Quote Source - 2026-06-11

## Source Map

| Source | URL | Checked At | Use |
|---|---|---|---|
| StockAnalysis AAPL statistics | https://stockanalysis.com/stocks/aapl/statistics/ | 2026-06-10 1:01 PM EDT, market open | Fresh price, market cap, shares, valuation ratios, cash/debt cross-check. |
| StockAnalysis AAPL overview | https://stockanalysis.com/stocks/aapl/ | 2026-06-10 11:36 AM EDT, market open | Intraday quote and market-data cross-check. |
| StockAnalysis AAPL financials | https://stockanalysis.com/stocks/aapl/financials/ | Last checked by provider 2026-06-09 | TTM standardized financial cross-check. |
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm | Filed 2026-05-01 | Official share count, cash, marketable securities, and debt inputs. |

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 292.15 | StockAnalysis statistics page, 2026-06-10 1:01 PM EDT, market open. |
| Market capitalization | USD 4.29T | StockAnalysis statistics page, checked 2026-06-10. |
| Enterprise value | USD 4.21T | StockAnalysis statistics page, checked 2026-06-10. |
| Shares outstanding | 14.69B | StockAnalysis statistics page, checked 2026-06-10. |
| Shares issued and outstanding | 14.687356B | SEC Q2 FY2026 Form 10-Q cover page, as of 2026-04-17. |
| Weighted-average diluted shares | 14.768115B | SEC Q2 FY2026 Form 10-Q, six months ended 2026-03-28. |
| TTM revenue | USD 451.44B | StockAnalysis statistics page. |
| TTM net income | USD 122.58B | StockAnalysis statistics page. |
| TTM operating cash flow | USD 140.22B | StockAnalysis statistics page; matches source-backed calculation in `[[AAPL_latest_results_source]]`. |
| TTM capex | USD (11.05B) | StockAnalysis statistics page; matches source-backed calculation in `[[AAPL_latest_results_source]]`. |
| TTM FCF | USD 129.17B | StockAnalysis statistics page; source-backed calculation is USD 129.174B. |
| Cash and marketable securities | USD 146.60B | StockAnalysis statistics page; SEC source-backed value is USD 146.595B. |
| Total debt | USD 84.71B | StockAnalysis statistics page; SEC source-backed value is USD 84.711B. |
| Net cash | USD 61.88B | StockAnalysis statistics page; calculated from SEC inputs as USD 61.884B. |
| P/FCF | 33.04x | StockAnalysis statistics page. |
| EV/FCF | 32.56x | StockAnalysis statistics page. |
| FCF yield | 3.03% | StockAnalysis statistics page. |
| Analyst average price target | USD 311.55 | StockAnalysis statistics page; secondary market context only. |

## Additional Fresh Check For Bullish Scenario

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 292.38 | StockAnalysis overview page, 2026-06-10 1:08 PM EDT, market open. |
| Market capitalization | USD 4.29T | StockAnalysis overview page, checked 2026-06-10. |
| Shares outstanding | 14.69B | StockAnalysis overview page, checked 2026-06-10. |
| Analyst average price target | USD 311.55 | StockAnalysis overview page; secondary market context only. |

## Missing / Unverified Data

| Item | Status | Handling |
|---|---|---|
| Official company-provided current market cap | Not a company filing item | Use market-data provider and label as market data. |
| Real-time exchange feed direct from Nasdaq | Not used in this pass | StockAnalysis quote is treated as fresh market-data context, not official company fact. |
| Investor position size and cost basis | Not provided | Decision memo separates new-capital action from existing-position action. |
