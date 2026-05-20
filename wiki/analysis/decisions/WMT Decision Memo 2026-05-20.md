---
type: analysis
analysis_type: decision-memo
ticker: WMT
company: Walmart Inc.
date: 2026-05-20
currency: USD
decision: AVOID new capital / WAIT for valuation reset or post-Q1 FY2027 update
source_files:
  - index.md
  - wiki/entities/WMT.md
  - raw/financials/WMT_fundamentals.md
  - raw/imports/WMT_latest_results_source.md
  - wiki/analysis/valuations/WMT DCF Valuation 2026-05-20.md
tags:
  - analysis/decision-memo
  - ticker/WMT
---

# WMT Decision Memo - 2026-05-20

## Action Read

**Action: AVOID new capital / WAIT. Existing holders can HOLD only if they explicitly accept premium valuation risk and plan to refresh after FY2027 Q1 results.**

WMT เป็น high-quality defensive scale retailer แต่ราคาปัจจุบันไม่ให้ margin of safety. Fresh quote อยู่ที่ USD 132.57 และ implied market cap ประมาณ USD 1.057T. เทียบกับ FY2026 FCF USD 14.923B, FCF yield อยู่แค่ประมาณ 1.4%. DCF base case ที่ใช้ source-backed FCF, cash, debt, diluted shares, and guidance context ให้ fair value ประมาณ USD 37.41 ต่อ diluted share.

เนื่องจาก FY2027 Q1 results จะออก 2026-05-21 หลัง source check นี้, action read ที่ปลอดภัยคือรอข้อมูลใหม่และไม่ไล่ซื้อก่อน catalyst ที่ใกล้มาก. ถ้าหลัง Q1 มีหลักฐานว่า FCF per share เร่งจริงและ guidance ดีขึ้นมาก ค่อย revisit.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh WMT quote | USD 132.57 | Stooq CSV, WMT.US, 2026-05-20 17:29:38. |
| Intraday open / high / low | USD 132.905 / 133.65 / 130.885 | Stooq CSV, checked 2026-05-20. |
| Quote volume | 4,517,090 | Stooq CSV. |
| Common shares outstanding | 7.972402501B | FY2026 Form 10-K, as of 2026-03-11. |
| Implied market cap | USD 1.057T | 132.57 * 7.972402501B. |
| Diluted weighted-average shares | 8.022B | Q4 FY26 earnings release, FY2026. |
| FY2026 FCF yield on implied market cap | 1.41% | 14.923 / 1,056.901. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest official period | FY2026 ended 2026-01-31 | `raw/financials/WMT_fundamentals.md`. |
| FY2026 total revenues | USD 713.163B | FY2026 Form 10-K. |
| FY2026 revenue growth | 4.7% | FY2026 Form 10-K / calculation. |
| FY2026 operating income | USD 29.825B | FY2026 Form 10-K. |
| FY2026 consolidated net income | USD 22.270B | FY2026 Form 10-K. |
| FY2026 operating cash flow | USD 41.565B | FY2026 Form 10-K. |
| FY2026 capex spend | USD 26.642B | FY2026 Form 10-K. |
| FY2026 free cash flow | USD 14.923B | FY2026 Form 10-K reconciliation. |
| Cash and cash equivalents | USD 10.727B | Q4 FY26 earnings release. |
| Total debt and finance lease obligations | USD 51.523B | Calculation from Q4 FY26 earnings release. |
| FY2027 net sales guidance | +3.5% to +4.5% constant currency | Q4 FY26 earnings release. |
| FY2027 adjusted operating income guidance | +6.0% to +8.0% constant currency | Q4 FY26 earnings release; non-GAAP. |
| FY2027 adjusted EPS guidance | USD 2.75 to USD 2.85 | Q4 FY26 earnings release; non-GAAP. |
| FY2027 capex guidance | approximately 3.5% of net sales | Q4 FY26 earnings release. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 37.41 per diluted share | Far below current price. |
| DCF bull fair value | USD 59.65 per diluted share | Still far below current price. |
| FY2026 FCF yield on implied market cap | 1.41% | Too low for a fresh add without exceptional FCF acceleration evidence. |
| Forward adjusted P/E | about 47.35x | Premium multiple on non-GAAP FY2027 EPS guide midpoint. |
| Net debt and finance leases / FY2026 FCF | 2.73x | Manageable, but valuation leaves little room for capex/FCF disappointment. |

valuation read ไม่ได้บอกว่า Walmart เป็นธุรกิจอ่อนแอ. มันบอกว่าราคาตลาด embed ความมั่นใจสูงมากว่า higher-margin digital/advertising/membership engines จะเปลี่ยน FCF trajectory. ก่อน FY2027 Q1 actuals ที่จะออกวันถัดไป, การไล่ซื้อไม่มี edge จาก source-backed data.

## Bull Case

- Walmart มี defensive traffic จาก grocery/value proposition และ scale ที่คู่แข่งเลียนแบบยาก.
- FY2027 guidance ชี้ net sales +3.5% to +4.5% constant currency และ adjusted operating income +6.0% to +8.0%, แปลว่า management คาด profit growth เร็วกว่ายอดขาย.
- eCommerce, advertising, membership, marketplace, VIZIO, data services, automation, and AI commerce อาจช่วย lift margin over time.
- Q4 management commentary ชี้ว่า global eCommerce +24%, Walmart U.S. eCommerce +27%, advertising +37% globally, Walmart Connect U.S. +41%, and membership income +15%+.
- New USD 30B share repurchase authorization supports per-share capital return if valuation and cash flow allow.

## Bear Case

- Current valuation is extreme on source-backed FCF: FY2026 FCF yield is about 1.4%.
- FY2027 adjusted EPS guidance midpoint of USD 2.80 implies roughly 47x forward adjusted P/E at USD 132.57.
- FY2027 capex is guided at approximately 3.5% of net sales, so FCF conversion may remain pressured.
- Product-level profitability for ads, membership, marketplace, VIZIO, and data services is not disclosed, so the key premium-valuation driver is only partially source-backed.
- FY2027 Q1 actual results were not yet available, and the release is imminent on 2026-05-21.
- Tariffs, labor costs, claims expense, price investments, and mix shifts can compress margin in a low-margin retail model.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term investor who still requires margin of safety. |
| Position status | Unknown; action focuses on new capital. |
| FCF anchor | FY2026 FCF of USD 14.923B from official reconciliation. |
| Valuation framework | Consumer Staples / defensive retailer DCF, 7.5% base WACC, 2.5% terminal growth. |
| Debt treatment | Includes short-term borrowings, current and long-term debt, and finance lease obligations. |
| Next catalyst | FY2027 Q1 earnings on 2026-05-21. |

## What Would Change The Decision

- Upgrade toward watchlist/add only if FY2027 Q1/YTD FCF conversion materially improves and guidance stays strong.
- Upgrade if the share price resets enough to create a reasonable FCF yield and DCF margin of safety.
- Upgrade if Walmart discloses hard profitability proof for advertising, membership, marketplace, VIZIO, and data services.
- Stay avoid/wait if FY2027 capex remains high and FCF growth does not accelerate.
- Downgrade further if Q1 FY2027 shows margin pressure, weaker guidance, or cash-flow deterioration.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| FY2027 Q1 actual results | not yet available | Official event was scheduled for 2026-05-21, after this source check. |
| FY2027 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses FY2026 FCF anchor rather than invented FCF guidance. |
| Forward GAAP EPS / net income guidance | not provided | Limits GAAP valuation cross-check. |
| Product-level profitability by higher-margin growth engines | not disclosed | The premium valuation depends heavily on these engines scaling profitably. |
| Segment-level FCF | not disclosed | Limits granular FCF quality analysis. |
| Exact end-of-day U.S. market data after 2026-05-20 close | partially verified | Refresh before any future action change. |
| Investor-specific tax basis, position size, and required return | not provided | Needed for personalized hold/trim/add sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/WMT_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/financials/WMT_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios, guidance, market data. |
| `wiki/entities/WMT.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/WMT DCF Valuation 2026-05-20.md` | Local valuation memo | P11 DCF and sensitivity. |
| FY2026 Form 10-K | https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000055/0000104169-26-000055.pdf | Official annual facts. |
| Q4 FY26 earnings release | https://corporate.walmart.com/content/dam/corporate/documents/newsroom/2026/02/19/walmart-releases-q4-fy26-earnings/q4-fy26-earnings-release.pdf | FY2027 guidance, balance sheet, cash flow, EPS, shares. |
| Q4 FY26 earnings transcript | https://corporate.walmart.com/content/dam/corporate/documents/newsroom/2026/02/19/walmart-releases-q4-fy26-earnings/q4-fy26-earnings-call-transcript.pdf | Management commentary. |
| Stooq quote CSV | https://stooq.com/q/l/?s=wmt.us&f=sd2t2ohlcv&h&e=csv | Fresh market-data check. |
