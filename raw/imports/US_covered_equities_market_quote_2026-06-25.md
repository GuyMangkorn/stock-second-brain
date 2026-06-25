---
type: source-note
ticker: MULTI
company: US-listed covered equities
source_kind: market_quote
search_date: 2026-06-25
reporting_scope: Nasdaq quote API real-time / intraday market-data check
currency: USD
normalized_output: wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-06-25.md
entity: MULTI
tags:
  - market-data
  - decision-refresh
---

# US Covered Equities - Nasdaq Market Quote Check

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Nasdaq quote API | `https://api.nasdaq.com/api/quote/{TICKER}/info?assetclass=stocks` | Fresh price, exchange, timestamp, market status, 52-week range. |
| Local decision memos | `wiki/analysis/decisions/` | Prior action read and valuation anchors. |

## Reporting Scope

Quotes were fetched on 2026-06-25 from the Nasdaq quote API. The API reported
`marketStatus: Open` and `isRealTime: true` for the captured rows. Market data
is not a company filing fact and should be refreshed again before any trade.

## Currency / Units

- Currency: USD
- Quote timestamp: 2026-06-25, approximately 12:47-12:48 PM ET
- Price field: `lastSalePrice`

## Extracted Facts

| Ticker | Company / Security | Exchange | Last Sale Price | Net Change | % Change | Quote Timestamp | 52 Week Range |
|---|---|---|---:|---:|---:|---|---|
| AAPL | Apple Inc. Common Stock | NASDAQ-GS | 274.665 | -18.415 | -6.28% | Jun 25, 2026 12:47 PM ET | 199.26 - 317.40 |
| ABT | Abbott Laboratories Common Stock | NYSE | 93.325 | +2.835 | +3.13% | Jun 25, 2026 12:47 PM ET | 81.97 - 138.84 |
| AMAT | Applied Materials, Inc. Common Stock | NASDAQ-GS | 646.95 | +57.98 | +9.84% | Jun 25, 2026 12:47 PM ET | 154.46 - 641.18 |
| ATLX | Atlas Lithium Corporation Common Stock | NASDAQ-CM | 3.475 | -0.105 | -2.93% | Jun 25, 2026 12:48 PM ET | 3.32 - 8.25 |
| AXON | Axon Enterprise, Inc. Common Stock | NASDAQ-GS | 448.965 | -7.765 | -1.70% | Jun 25, 2026 12:47 PM ET | 339.01 - 885.92 |
| BABA | Alibaba Group Holding Limited ADS | NYSE | 95.46 | -4.34 | -4.35% | Jun 25, 2026 12:48 PM ET | 99.10 - 192.67 |
| CEG | Constellation Energy Corporation Common Stock | NASDAQ-GS | 270.68 | +2.71 | +1.01% | Jun 25, 2026 12:47 PM ET | 240.51 - 412.70 |
| COST | Costco Wholesale Corporation Common Stock | NASDAQ-GS | 942.25 | -18.84 | -1.96% | Jun 25, 2026 12:47 PM ET | 844.06 - 1,096.50 |
| CRWD | CrowdStrike Holdings, Inc. Class A Common Stock | NASDAQ-GS | 672.71 | -0.31 | -0.05% | Jun 25, 2026 12:47 PM ET | 342.72 - 785.66 |
| CRWV | CoreWeave, Inc. Class A Common Stock | NASDAQ-GS | 100.34 | -0.54 | -0.54% | Jun 25, 2026 12:47 PM ET | 63.80 - 180.25 |
| CSCO | Cisco Systems, Inc. Common Stock (DE) | NASDAQ-GS | 118.725 | -1.005 | -0.84% | Jun 25, 2026 12:47 PM ET | 65.75 - 130.37 |
| DELL | Dell Technologies Inc. Class C Common Stock | NYSE | 408.19 | -25.87 | -5.96% | Jun 25, 2026 12:47 PM ET | 110.22 - 469.47 |
| EW | Edwards Lifesciences Corporation Common Stock | NYSE | 90.34 | +0.68 | +0.76% | Jun 25, 2026 12:47 PM ET | 72.30 - 90.99 |
| GE | GE Aerospace Common Stock | NYSE | 373.605 | +7.725 | +2.11% | Jun 25, 2026 12:47 PM ET | 243.34 - 369.25 |
| GEV | GE Vernova Inc. Common Stock | NYSE | 1,092.17 | +34.52 | +3.26% | Jun 25, 2026 12:47 PM ET | 482.20 - 1,181.95 |
| GOOGL | Alphabet Inc. Class A Common Stock | NASDAQ-GS | 341.045 | -4.245 | -1.23% | Jun 25, 2026 12:47 PM ET | 167.55 - 408.61 |
| IBM | International Business Machines Corporation Common Stock | NYSE | 260.24 | -2.72 | -1.03% | Jun 25, 2026 12:47 PM ET | 212.34 - 332.46 |
| JNJ | Johnson & Johnson Common Stock | NYSE | 244.10 | +3.10 | +1.29% | Jun 25, 2026 12:48 PM ET | 150.73 - 251.71 |
| MCD | McDonald's Corporation Common Stock | NYSE | 266.15 | -7.73 | -2.82% | Jun 25, 2026 12:48 PM ET | 270.08 - 341.75 |
| MDT | Medtronic plc. Ordinary Shares | NYSE | 81.35 | +1.22 | +1.52% | Jun 25, 2026 12:48 PM ET | 73.31 - 106.33 |
| META | Meta Platforms, Inc. Class A Common Stock | NASDAQ-GS | 546.92 | -10.75 | -1.93% | Jun 25, 2026 12:48 PM ET | 520.26 - 796.25 |
| MSFT | Microsoft Corporation Common Stock | NASDAQ-GS | 351.7651 | -13.6949 | -3.75% | Jun 25, 2026 12:48 PM ET | 356.28 - 555.45 |
| PG | Procter & Gamble Company Common Stock | NYSE | 149.20 | -2.84 | -1.87% | Jun 25, 2026 12:48 PM ET | 137.62 - 167.25 |
| SHOP | Shopify Inc. Class A Subordinate Voting Shares | NASDAQ-GS | 114.78 | +0.61 | +0.53% | Jun 25, 2026 12:48 PM ET | 94.00 - 182.19 |
| UNH | UnitedHealth Group Incorporated Common Stock (DE) | NYSE | 416.17 | +10.37 | +2.56% | Jun 25, 2026 12:48 PM ET | 234.60 - 415.98 |
| V | Visa Inc. | NYSE | 335.245 | +3.015 | +0.91% | Jun 25, 2026 12:48 PM ET | 293.89 - 359.66 |
| VST | Vistra Corp. Common Stock | NYSE | 167.865 | +4.995 | +3.07% | Jun 25, 2026 12:48 PM ET | 132.66 - 219.82 |
| VZ | Verizon Communications Inc. Common Stock | NYSE | 45.945 | +0.265 | +0.58% | Jun 25, 2026 12:48 PM ET | 10.60 - 51.68 |
| WMT | Walmart Inc. Common Stock | NASDAQ-GS | 115.83 | -3.17 | -2.66% | Jun 25, 2026 12:48 PM ET | 94.23 - 135.16 |

## Missing / Unverified Data

- Market cap and shares were not refreshed in this batch source note.
- Quote provider data can differ from official exchange close and should be
  refreshed before trade execution.
- This note does not update company fundamentals or new quarterly filings.

## Handoff For Ingest

Use this note as the market-data input for the 2026-06-25 covered-equities
decision refresh. Do not ingest these prices as durable company financial facts.
