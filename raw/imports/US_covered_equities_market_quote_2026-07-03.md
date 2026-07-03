---
type: source-note
source_kind: market-quote
date: 2026-07-03
scope: covered equities previously researched in vault
source: Nasdaq quote API
fetched_at: 2026-07-03 Asia/Bangkok
tags:
  - source/market-quote
  - covered-equities
---

# US Covered Equities Market Quote - 2026-07-03

## Source Context

Quotes were fetched from Nasdaq quote API on 2026-07-03 Asia/Bangkok using:

```text
https://api.nasdaq.com/api/quote/{TICKER}/info?assetclass=stocks
```

Nasdaq reported `marketStatus: Closed`, `isRealTime: false`, and
`lastTradeTimestamp: Jul 1, 2026` for the fetched quotes. Treat these as the
latest available closed-market quotes from this source, not live intraday
prices.

## Quote Table

| Ticker | Company | Last Sale Price | Net Change | Percentage Change | Last Trade Timestamp | Volume | Market Status |
|---|---|---:|---:|---:|---|---:|---|
| AAPL | Apple Inc. Common Stock | USD 308.63 | +14.25 | +4.84% | Jul 1, 2026 | 75,400,911 | Closed |
| ABT | Abbott Laboratories Common Stock | USD 95.40 | +3.22 | +3.49% | Jul 1, 2026 | 10,644,585 | Closed |
| AMAT | Applied Materials, Inc. Common Stock | USD 603.04 | -47.87 | -7.35% | Jul 1, 2026 | 15,096,172 | Closed |
| ATLX | Atlas Lithium Corporation Common Stock | USD 3.64 | -0.13 | -3.45% | Jul 1, 2026 | 413,115 | Closed |
| AXON | Axon Enterprise, Inc. Common Stock | USD 597.04 | +3.08 | +0.52% | Jul 1, 2026 | 1,062,209 | Closed |
| BABA | Alibaba Group Holding Limited American Depositary Shares each representing eight Ordinary share | USD 96.14 | -1.85 | -1.89% | Jul 1, 2026 | 11,764,196 | Closed |
| CEG | Constellation Energy Corporation Common Stock | USD 239.25 | +2.75 | +1.16% | Jul 1, 2026 | 4,271,001 | Closed |
| COST | Costco Wholesale Corporation Common Stock | USD 951.67 | +27.00 | +2.92% | Jul 1, 2026 | 2,787,694 | Closed |
| CRWD | CrowdStrike Holdings, Inc. Class A Common Stock | USD 193.98 | +0.795 | +0.41% | Jul 1, 2026 | 10,432,190 | Closed |
| CRWV | CoreWeave, Inc. Class A Common Stock | USD 81.745 | -3.94 | -4.60% | Jul 1, 2026 | 32,788,121 | Closed |
| CSCO | Cisco Systems, Inc. Common Stock (DE) | USD 112.69 | -4.32 | -3.69% | Jul 1, 2026 | 24,254,889 | Closed |
| DELL | Dell Technologies Inc. Class C Common Stock | USD 394.32 | -30.93 | -7.27% | Jul 1, 2026 | 6,618,458 | Closed |
| EW | Edwards Lifesciences Corporation Common Stock | USD 94.37 | +2.38 | +2.59% | Jul 1, 2026 | 3,206,400 | Closed |
| GE | GE Aerospace Common Stock | USD 377.52 | +2.58 | +0.69% | Jul 1, 2026 | 3,275,349 | Closed |
| GEV | GE Vernova Inc. Common Stock | USD 1,113.11 | -21.24 | -1.87% | Jul 1, 2026 | 2,363,031 | Closed |
| GOOGL | Alphabet Inc. Class A Common Stock | USD 359.91 | -1.30 | -0.36% | Jul 1, 2026 | 25,999,437 | Closed |
| IBM | International Business Machines Corporation Common Stock | USD 289.52 | +3.27 | +1.14% | Jul 1, 2026 | 5,950,179 | Closed |
| JNJ | Johnson & Johnson Common Stock | USD 263.04 | +9.06 | +3.57% | Jul 1, 2026 | 8,000,765 | Closed |
| KO | Coca-Cola Company (The) Common Stock | USD 84.14 | +2.85 | +3.51% | Jul 1, 2026 | 18,320,588 | Closed |
| MCD | McDonald's Corporation Common Stock | USD 280.63 | +11.20 | +4.16% | Jul 1, 2026 | 6,875,869 | Closed |
| MDT | Medtronic plc. Ordinary Shares | USD 83.19 | +3.99 | +5.04% | Jul 1, 2026 | 9,723,082 | Closed |
| META | Meta Platforms, Inc. Class A Common Stock | USD 582.90 | -30.01 | -4.90% | Jul 1, 2026 | 21,751,182 | Closed |
| MSFT | Microsoft Corporation Common Stock | USD 390.49 | +6.21 | +1.62% | Jul 1, 2026 | 42,194,622 | Closed |
| NVDA | NVIDIA Corporation Common Stock | USD 194.83 | -2.75 | -1.39% | Jul 1, 2026 | 142,387,459 | Closed |
| PG | Procter & Gamble Company (The) Common Stock | USD 151.41 | +3.98 | +2.70% | Jul 1, 2026 | 9,256,707 | Closed |
| SHOP | Shopify Inc. Class A Subordinate Voting Shares | USD 119.46 | -2.17 | -1.78% | Jul 1, 2026 | 6,761,737 | Closed |
| UL | Unilever PLC American Depositary Shares (each representing One Ordinary Share) | USD 62.48 | +1.59 | +2.61% | Jul 1, 2026 | 3,240,648 | Closed |
| UNH | UnitedHealth Group Incorporated Common Stock (DE) | USD 425.36 | -1.18 | -0.28% | Jul 1, 2026 | 3,931,603 | Closed |
| V | Visa Inc. | USD 362.13 | +11.05 | +3.15% | Jul 1, 2026 | 9,817,202 | Closed |
| VST | Vistra Corp. Common Stock | USD 151.05 | -2.11 | -1.38% | Jul 1, 2026 | 4,255,902 | Closed |
| VZ | Verizon Communications Inc. Common Stock | USD 42.56 | +0.57 | +1.36% | Jul 1, 2026 | 59,060,866 | Closed |
| WMT | Walmart Inc. Common Stock | USD 111.84 | +3.02 | +2.78% | Jul 1, 2026 | 29,526,256 | Closed |

## Source Caveats

- This is a market-price refresh only. It does not update company filings,
  earnings transcripts, financial statements, market cap, enterprise value,
  shares, or valuation multiples for each ticker.
- Nasdaq returned latest available closed-market quote data, not real-time
  intraday prices.
- Decision work using this note should compare the quotes against the latest
  source-backed valuation and decision memos already in the vault.
