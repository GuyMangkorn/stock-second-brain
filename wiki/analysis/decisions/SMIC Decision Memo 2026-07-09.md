---
type: analysis
analysis_type: decision-memo
ticker: SMIC
company: Semiconductor Manufacturing International Corporation
date: 2026-07-09
currency: USD / CNY / HKD
source_files:
  - wiki/entities/SMIC.md
  - raw/financials/SMIC_fundamentals.md
  - raw/imports/SMIC_latest_results_source.md
  - raw/imports/SMIC_market_quote_2026-07-09.md
  - wiki/analysis/valuations/SMIC DCF Valuation 2026-07-09.md
tags:
  - analysis/decision
  - ticker/SMIC
---

# SMIC Decision Memo - 2026-07-09
Entity: [[SMIC]]

## Action Read

**WATCHLIST / WAIT.** SMIC has improving near-term official guidance and strategic China localization exposure, but the current decision is not strong enough for new capital under source-integrity rules. The blocking issues are negative FCF after capex, missing FY2026 FCF / capex guidance, and unresolved market-cap/share-count reconciliation.

This is not an `avoid forever` call. It is a `wait for cash-flow and valuation clarity` call.

## Current Price / Market Data Check

| Metric | Value | Source |
|---|---:|---|
| Fresh H-share price | HKD 84.10 | Google Finance `0981:HKG`, timestamp 2026-07-09 15:14:56 GMT+8. |
| Displayed market cap | HKD 996.95B | Google Finance. |
| Displayed shares outstanding | 5.04B | Google Finance. |
| Official diluted shares used in EPS | 8.012731B | SMIC Q1 2026 income statement spreadsheet. |
| Implied shares from displayed market cap / price | 11.85B | 996.95B / 84.10. |
| Market-source P/E | 118.83x | Google Finance. |

Market-data caveat: displayed shares, official diluted shares, and implied shares from market cap / price conflict. This memo uses the quote and displayed market cap as fresh market context, but does not infer a precise fair value per share.

## Evidence From Vault

| Evidence | Read |
|---|---|
| Q1 2026 revenue USD 2.5055B, +11.49% YoY and +0.67% QoQ | Growth is positive but not explosive in Q1 itself. |
| Q2 2026 guidance calls for revenue +14% to +16% QoQ | Near-term demand / order momentum improved materially. |
| Q1 2026 gross margin 20.1%; Q2 guide 20% to 22% | Margin guide is stable to slightly better versus Q1. |
| Q1 2026 simple FCF USD -0.627B | Cash conversion remains weak after capex. |
| FY2025 simple FCF RMB -39.870B | Heavy reinvestment is not a one-quarter artifact. |
| Cash USD 7.279B vs debt-like obligations USD 14.512B | Balance sheet can support expansion, but not from a net-cash position on this definition. |

## Valuation Read

P11 stopped before a point-estimate DCF. A precise target price would require unsupported assumptions about future FCF, full-year capex, WACC, and share count.

The practical valuation read is:

- Strategic optionality is real, but current market data show a high headline P/E of 118.83x.
- Official cash-flow evidence is not yet enough to underwrite a DCF.
- The stock needs either a much clearer FCF inflection or a lower entry price to create a margin of safety.

## Bull Case

SMIC เป็น strategic foundry platform ที่ได้ประโยชน์จาก China semiconductor localization. Q2 2026 guidance +14% to +16% QoQ revenue และ gross margin 20%-22% บอกว่า order momentum ดีขึ้น. ถ้า utilization สูงขึ้นพร้อม margin คงตัว และ capex intensity เริ่มลดลงในปีถัดไป FCF อาจ inflect ได้แรงกว่าที่ trailing data แสดงอยู่.

## Bear Case

รายได้และ margin ยังไม่พอชดเชย capex. Q1 2026 simple FCF ติดลบ USD 627M และ FY2025 annual simple FCF ติดลบ RMB 39.87B. Debt-like obligations เพิ่มขึ้น และ market quote ปัจจุบันดู demanding จาก P/E 118.83x. ถ้า expansion cycle ยืดเยื้อหรือ utilization ลดลง valuation จะรับแรงกดดันเร็ว.

## Key Assumptions

- Q2 2026 guidance is treated as official forward-looking guidance, not realized fact.
- FCF remains the key underwriting gap until official guidance or realized results prove otherwise.
- Market cap and shares are treated cautiously because fresh market-data source values conflict with official diluted EPS shares.
- No personalized portfolio sizing is provided.

## What Would Change The Decision

- SMIC reports positive FCF after capex for multiple quarters.
- Official FY2026 capex and FCF guidance becomes available.
- Share-count / market-cap reconciliation is resolved.
- Q2 2026 meets or beats revenue and gross-margin guidance without a further balance-sheet stretch.
- Price falls enough to reduce dependence on strategic optionality.

## Missing / Unverified Data

| Item | Status | Decision impact |
|---|---|---|
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Prevents DCF-derived fair value and upside/downside. |
| FY2026 capex guidance | ไม่พบข้อมูลที่ยืนยันได้ | Prevents cash-flow normalization. |
| Reconciled share count / market cap | ไม่พบข้อมูลที่ยืนยันได้ | Blocks clean per-share valuation. |
| Official Q1 2026 transcript text | ไม่พบข้อมูลที่ยืนยันได้ | Limits Q&A-level confidence. |
| Node-level profitability | not disclosed | Limits ability to underwrite advanced-node economics. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| SMIC latest results source note | `raw/imports/SMIC_latest_results_source.md` | Official source map and P1 raw extraction. |
| SMIC normalized fundamentals | `raw/financials/SMIC_fundamentals.md` | P4 normalized statement facts and ratios. |
| SMIC entity page | `wiki/entities/SMIC.md` | P6 thesis, risks, catalysts, missing data. |
| SMIC market quote | `raw/imports/SMIC_market_quote_2026-07-09.md` | Fresh price, market cap, market-data conflict. |
| SMIC valuation-gap memo | `wiki/analysis/valuations/SMIC DCF Valuation 2026-07-09.md` | P11 stop rationale. |
