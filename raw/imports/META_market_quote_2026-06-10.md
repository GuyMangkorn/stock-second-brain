---
type: source-note
ticker: META
company: Meta Platforms, Inc.
source_kind: market-quote
search_date: 2026-06-10
reporting_scope: market data checked 2026-06-10
currency: USD
entity: "[[META]]"
tags:
  - source/market-quote
  - ticker/META
---

# META - Market Quote 2026-06-10

## Source Map

| Source | URL / Path | Checked | Notes |
|---|---|---|---|
| Nasdaq quote API | https://api.nasdaq.com/api/quote/META/info?assetclass=stocks | 2026-06-10 12:52 PM ET | Intraday quote, market open, NasdaqGS. |
| Nasdaq summary API | https://api.nasdaq.com/api/quote/META/summary?assetclass=stocks | 2026-06-10 | Market capitalization and trading summary. |
| Yahoo Finance chart API | https://query1.finance.yahoo.com/v8/finance/chart/META?range=1d&interval=1m | 2026-06-10 12:51:30 PM ET | Cross-check quote and intraday OHLC/volume. |
| SEC Form 10-Q cover facts | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm | 2026-06-10 | Class A/B shares outstanding as of 2026-04-24. |

## Market Data

| Item | Value | Source |
|---|---:|---|
| Last sale price | USD 577.61 | Nasdaq quote API, Jun 10, 2026 12:52 PM ET. |
| Net change | USD (6.98) | Nasdaq quote API. |
| Percentage change | (1.19)% | Nasdaq quote API. |
| Market status | Open | Nasdaq quote API. |
| Day range | USD 575.02 - USD 591.30 | Nasdaq quote and summary APIs. |
| Previous close | USD 584.59 | Nasdaq summary API. |
| Market capitalization | USD 1,466,244,068,856 | Nasdaq summary API. |
| Class A shares outstanding | 2,196,045,588 | SEC Q1 2026 Form 10-Q cover fact, as of 2026-04-24. |
| Class B shares outstanding | 342,377,716 | SEC Q1 2026 Form 10-Q cover fact, as of 2026-04-24. |
| Total Class A + Class B shares outstanding | 2,538,423,304 | Calculated from SEC cover facts. |
| Weighted-average diluted shares | 2,564 million | SEC Q1 2026 Form 10-Q / Exhibit 99.1, Q1 2026. |
| Yahoo regularMarketPrice cross-check | USD 576.91 | Yahoo Finance chart API, regularMarketTime 2026-06-10 12:51:30 PM ET. |

## Calculation Checks

| Calculation | Result | Notes |
|---|---:|---|
| Nasdaq market cap / Nasdaq last sale price | 2.538 billion shares | USD 1.466244T / USD 577.61; consistent with SEC total Class A+B shares outstanding. |
| Nasdaq market cap / SEC total shares outstanding | USD 577.62 per share | Cross-checks Nasdaq market cap against SEC share count. |

## Missing / Unverified Data

| Item | Status | Handling |
|---|---|---|
| End-of-day closing price for 2026-06-10 | Not available during intraday check | Use timestamped intraday quote only. |
| Market cap from company filing | Not a company filing item | Use Nasdaq market-data source and keep separate from official financial facts. |
| Float-adjusted market cap | ไม่พบข้อมูลที่ยืนยันได้ | Do not use for valuation. |
