---
type: source-note
ticker: IBM
company: International Business Machines Corporation
source_kind: market_quote
search_date: 2026-06-10
reporting_scope: latest market quote for valuation refresh
currency: USD
normalized_output: wiki/analysis/decisions/IBM Decision Memo 2026-06-10.md
entity: "[[IBM]]"
tags:
  - source/market-quote
  - ticker/IBM
---

# IBM - Market Quote Source - 2026-06-10

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Alpha Vantage `GLOBAL_QUOTE` demo endpoint | https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo | Latest market quote used for current valuation and decision refresh. |
| IBM Q1 2026 earnings release | https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS | Existing official source for Q1 2026 financial facts, guidance, debt, cash, FCF, and quarterly dividend. |
| IBM Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/51143/000005114326000038/ibm-20260331.htm | Existing official source for share count and financial statement details. |
| Prior normalized facts | raw/financials/IBM_fundamentals.md | Source-backed operating and balance-sheet inputs used in the valuation refresh. |

## Reporting Scope

- Market quote checked on 2026-06-10 Asia/Bangkok.
- Latest trading day returned by source: 2026-06-09.
- This note updates market context only. It does not replace official IBM filings, earnings release, or normalized Q1 2026 financial facts.

## Currency / Units

- Currency: USD.
- Stock price: USD per common share.
- Volume: shares.

## Extracted Facts

| Field | Value | Source |
|---|---:|---|
| Symbol | IBM | Alpha Vantage `GLOBAL_QUOTE` response. |
| Latest trading day | 2026-06-09 | Alpha Vantage `GLOBAL_QUOTE` response. |
| Open | USD 281.1350 | Alpha Vantage `GLOBAL_QUOTE` response. |
| High | USD 283.5900 | Alpha Vantage `GLOBAL_QUOTE` response. |
| Low | USD 271.2900 | Alpha Vantage `GLOBAL_QUOTE` response. |
| Price / latest close | USD 277.4900 | Alpha Vantage `GLOBAL_QUOTE` response. |
| Volume | 9,007,918 | Alpha Vantage `GLOBAL_QUOTE` response. |
| Previous close | USD 280.8200 | Alpha Vantage `GLOBAL_QUOTE` response. |
| Change | USD -3.3300 | Alpha Vantage `GLOBAL_QUOTE` response. |
| Change percent | -1.1858% | Alpha Vantage `GLOBAL_QUOTE` response. |

## Calculations Used In Refresh

| Metric | Value | Formula / Source |
|---|---:|---|
| Shares outstanding used for market cap | 939.88528M | IBM Q1 2026 Form 10-Q cover page, carried from `raw/financials/IBM_fundamentals.md`. |
| Diluted shares used for DCF | 952.1M | IBM Q1 2026 weighted-average diluted shares, carried from `raw/financials/IBM_fundamentals.md`. |
| Market capitalization | USD 260.81B | 277.49 * 939.88528M. |
| Implied market cap using diluted shares | USD 264.20B | 277.49 * 952.1M. |
| TTM IBM-defined FCF | USD 14.992B | FY2025 FCF 14.734B - Q1 2025 FCF 1.962B + Q1 2026 FCF 2.220B. |
| Market FCF yield | 5.75% | 14.992 / 260.81. |
| Market EV / TTM FCF | 21.04x | (260.81 + 66.40 - 11.828) / 14.992. |
| FY2026 guided FCF yield | about 6.03% | 15.734 / 260.81, using FY2025 FCF plus about USD 1B guidance. |
| Annualized dividend yield | about 2.44% | 1.69 * 4 / 277.49; dividend from IBM Q1 2026 earnings release. |

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Intraday real-time quote after 2026-06-09 close | not disclosed | The source returned latest trading day 2026-06-09, not a real-time intraday quote for 2026-06-10. |
| Official exchange quote snapshot | not disclosed | This pass used Alpha Vantage after Stooq returned an endpoint error and Yahoo Finance returned rate limiting. |
| Any new IBM operating results after Q1 2026 | ไม่พบข้อมูลที่ยืนยันได้ | No newer official quarterly result was used in this refresh. |

## Handoff For Ingest

- Use the quote only for `Current Price / Market Data Check` in decision and valuation memos.
- Do not overwrite Q1 2026 financial facts with market-data values.
- Refresh again after Q2 2026 official results or before any trading decision.
