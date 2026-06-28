---
type: source-note
ticker: MULTI
company: US-listed covered equities
source_kind: market_quote
search_date: 2026-06-28
reporting_scope: Nasdaq quote API closed-market latest quote check
currency: USD
normalized_output: wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-06-28.md
entity: MULTI
tags:
  - market-data
  - decision-refresh
---

# US Covered Equities - Nasdaq Market Quote Check

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Nasdaq quote API | `https://api.nasdaq.com/api/quote/{TICKER}/info?assetclass=stocks` | Latest available price, exchange, timestamp, market status, volume, and 52-week range. |
| Local decision memos | `wiki/analysis/decisions/` | Prior action read and valuation anchors. |
| Local valuation memos | `wiki/analysis/valuations/` | Base/bull DCF or valuation-stop context. |

## Reporting Scope

Quotes were fetched on 2026-06-28 Asia/Bangkok. Because U.S. markets were
closed, Nasdaq reported `marketStatus: Closed`, `isRealTime: false`, and
`lastTradeTimestamp: Jun 25, 2026` for the captured rows. Market data is not a
company filing fact and should be refreshed again before any trade.

## Currency / Units

- Currency: USD
- Price field: `primaryData.lastSalePrice`
- Quote timestamp reported by Nasdaq: Jun 25, 2026

## Extracted Facts

| Ticker | Company / Security | Exchange | Last Sale Price | Net Change | % Change | Volume | Market Status | 52 Week Range |
|---|---|---|---:|---:|---:|---:|---|---|
| AAPL | Apple Inc. Common Stock | NASDAQ-GS | 283.78 | +8.63 | +3.14% | 261,775,692 | Closed | 199.26 - 317.40 |
| ABT | Abbott Laboratories Common Stock | NYSE | 94.12 | +0.88 | +0.94% | 16,465,119 | Closed | 81.97 - 137.54 |
| AMAT | Applied Materials, Inc. Common Stock | NASDAQ-GS | 626.84 | -41.16 | -6.16% | 28,138,630 | Closed | 154.46 - 669.22 |
| ATLX | Atlas Lithium Corporation Common Stock | NASDAQ-CM | 3.68 | +0.15 | +4.25% | 387,776 | Closed | 3.32 - 8.25 |
| AXON | Axon Enterprise, Inc. Common Stock | NASDAQ-GS | 464.83 | +20.10 | +4.52% | 1,504,205 | Closed | 339.01 - 885.92 |
| BABA | Alibaba Group Holding Limited ADS | NYSE | 94.81 | -0.26 | -0.27% | 18,307,577 | Closed | 94.71 - 192.67 |
| CEG | Constellation Energy Corporation Common Stock | NASDAQ-GS | 264.02 | -4.67 | -1.74% | 3,922,210 | Closed | 240.51 - 412.70 |
| COST | Costco Wholesale Corporation Common Stock | NASDAQ-GS | 952.54 | +10.30 | +1.09% | 8,239,265 | Closed | 844.06 - 1,096.50 |
| CRWD | CrowdStrike Holdings, Inc. Class A Common Stock | NASDAQ-GS | 701.09 | +22.44 | +3.31% | 3,332,277 | Closed | 342.72 - 785.66 |
| CRWV | CoreWeave, Inc. Class A Common Stock | NASDAQ-GS | 96.58 | -2.18 | -2.21% | 47,706,038 | Closed | 63.80 - 173.35 |
| CSCO | Cisco Systems, Inc. Common Stock (DE) | NASDAQ-GS | 113.77 | -5.20 | -4.37% | 51,641,398 | Closed | 65.75 - 130.37 |
| DELL | Dell Technologies Inc. Class C Common Stock | NYSE | 399.49 | -9.96 | -2.43% | 10,833,002 | Closed | 110.22 - 469.47 |
| EW | Edwards Lifesciences Corporation Common Stock | NYSE | 90.78 | +1.06 | +1.18% | 14,421,063 | Closed | 72.30 - 91.65 |
| GE | GE Aerospace Common Stock | NYSE | 369.00 | -2.36 | -0.64% | 8,361,170 | Closed | 243.34 - 379.67 |
| GEV | GE Vernova Inc. Common Stock | NYSE | 1,045.17 | -40.30 | -3.71% | 3,654,230 | Closed | 482.20 - 1,181.95 |
| GOOGL | Alphabet Inc. Class A Common Stock | NASDAQ-GS | 337.39 | -6.32 | -1.84% | 114,706,469 | Closed | 169.94 - 408.61 |
| IBM | International Business Machines Corporation Common Stock | NYSE | 271.63 | +13.36 | +5.17% | 9,719,945 | Closed | 212.34 - 332.46 |
| JNJ | Johnson & Johnson Common Stock | NYSE | 254.66 | +9.78 | +3.99% | 16,316,791 | Closed | 151.01 - 251.71 |
| MCD | McDonald's Corporation Common Stock | NYSE | 269.76 | +5.22 | +1.97% | 7,422,847 | Closed | 264.53 - 341.75 |
| MDT | Medtronic plc. Ordinary Shares | NYSE | 80.98 | +0.46 | +0.57% | 12,401,090 | Closed | 73.31 - 106.33 |
| META | Meta Platforms, Inc. Class A Common Stock | NASDAQ-GS | 550.25 | +7.38 | +1.36% | 18,868,168 | Closed | 520.26 - 796.25 |
| MSFT | Microsoft Corporation Common Stock | NASDAQ-GS | 372.97 | +20.14 | +5.71% | 186,201,829 | Closed | 349.20 - 555.45 |
| NVDA | NVIDIA Corporation Common Stock | NASDAQ-GS | 192.53 | -3.21 | -1.64% | 179,306,787 | Closed | 151.49 - 236.54 |
| PG | Procter & Gamble Company Common Stock | NYSE | 149.02 | +0.52 | +0.35% | 16,724,562 | Closed | 137.62 - 167.25 |
| SHOP | Shopify Inc. Class A Subordinate Voting Shares | NASDAQ-GS | 116.86 | +5.24 | +4.69% | 9,946,424 | Closed | 94.00 - 182.19 |
| UNH | UnitedHealth Group Incorporated Common Stock (DE) | NYSE | 427.89 | +12.36 | +2.97% | 10,588,255 | Closed | 234.60 - 417.58 |
| V | Visa Inc. | NYSE | 336.23 | +5.71 | +1.73% | 16,717,400 | Closed | 293.89 - 359.66 |
| VST | Vistra Corp. Common Stock | NYSE | 163.49 | -4.28 | -2.55% | 5,487,413 | Closed | 132.66 - 219.82 |
| VZ | Verizon Communications Inc. Common Stock | NYSE | 46.54 | +0.47 | +1.02% | 38,132,777 | Closed | 10.60 - 51.68 |
| WMT | Walmart Inc. Common Stock | NASDAQ-GS | 115.69 | -0.09 | -0.08% | 36,635,993 | Closed | 94.23 - 135.16 |

## Missing / Unverified Data

- Market cap, shares, enterprise value, and valuation multiples were not
  refreshed in this batch source note.
- Nasdaq reported the latest available closed-market quote rather than a live
  intraday quote.
- This note does not update company fundamentals or new quarterly filings.

## Handoff For Decision Refresh

Use this note as the market-data input for the 2026-06-28 covered-equities
decision refresh. Do not ingest these prices as durable company financial facts.
