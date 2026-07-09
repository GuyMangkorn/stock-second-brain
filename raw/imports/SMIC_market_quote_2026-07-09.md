---
type: source-note
ticker: SMIC
company: Semiconductor Manufacturing International Corporation
source_kind: market-quote
search_date: 2026-07-09
currency: HKD
entity: "[[SMIC]]"
tags:
  - source/market-quote
  - ticker/SMIC
---

# SMIC - Market Quote 2026-07-09

## Source Map

| Source | URL | Checked | Use |
|---|---|---|---|
| Google Finance `0981:HKG` | https://www.google.com/finance/quote/0981:HKG | 2026-07-09 | Fresh H-share price, displayed market cap, displayed shares outstanding, P/E, EPS, volume, and quote timestamp. |

## Current Price / Market Data Check

| Metric | Value | Source |
|---|---:|---|
| Exchange quote | `0981:HKG` | Google Finance. |
| Price | HKD 84.10 | Google Finance, timestamp 2026-07-09 15:14:56 GMT+8. |
| 1D move | +10.95% / +HKD 8.30 | Google Finance. |
| Open | HKD 77.60 | Google Finance. |
| High | HKD 85.80 | Google Finance. |
| Low | HKD 76.65 | Google Finance. |
| Displayed market cap | HKD 996.95B | Google Finance. |
| Displayed shares outstanding | 5.04B | Google Finance. |
| Volume | 209.88M | Google Finance. |
| Average volume | 152.79M | Google Finance. |
| P/E ratio | 118.83x | Google Finance. |
| EPS | HKD 0.71 | Google Finance. |
| 52-week high | HKD 93.50 | Google Finance. |
| 52-week low | HKD 44.40 | Google Finance. |

## Cross-Checks / Conflicts

| Item | Status | Notes |
|---|---|---|
| Official diluted shares | 8.012731B | Q1 2026 SMIC income statement spreadsheet, diluted shares used in EPS. |
| Market-source shares outstanding | 5.04B | Google Finance display. |
| Implied shares from displayed market cap / price | 11.85B | 996.95B / 84.10. This conflicts with both official diluted shares and Google displayed shares outstanding. |
| Decision use | Use displayed price and market cap, but do not compute precise per-share DCF from conflicted share data. | Dual listing / share-class treatment may explain part of the mismatch, but this pass does not verify the reconciliation. |

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Reconciled total share count across H shares and A shares | ไม่พบข้อมูลที่ยืนยันได้ | Google displayed market cap, Google shares outstanding, and official diluted EPS shares do not reconcile cleanly. |
| Exchange-rate conversion to USD | not needed | P11 stops before a precise DCF, so no HKD/USD conversion is used for fair value. |
| Intraday quote after 2026-07-09 15:14:56 GMT+8 | ไม่พบข้อมูลที่ยืนยันได้ | Refresh before any later action call. |
