---
type: analysis
analysis_type: decision-memo
ticker: GE
company: GE Aerospace
date: 2026-05-21
currency: USD
decision: AVOID-new-capital / WAIT; HOLD only if already owned and position size is intentional
source_files:
  - index.md
  - wiki/entities/GE.md
  - raw/financials/GE_fundamentals.md
  - raw/imports/GE_latest_results_source.md
  - wiki/analysis/valuations/GE DCF Valuation 2026-05-21.md
tags:
  - analysis/decision-memo
  - ticker/GE
---

# GE Decision Memo - 2026-05-21
Entity: [[GE]]

## Action Read

**Action: AVOID-new-capital / WAIT. HOLD only if already owned and position size is intentional.**

GE Aerospace เป็น business คุณภาพสูงขึ้นมากหลัง separation: Q1 2026 orders +87%, adjusted revenue +29%, operating profit +18%, FCF +14%, และ FY2026 guidance ยังชี้ FCF USD 8.0B-8.4B. แต่ราคาที่ USD 300.17 ทำให้ valuation ตึงมาก: TTM FCF yield 2.52%, forward FCF yield แค่ 2.62%, และ forward adjusted P/E ประมาณ 41.4x.

Base DCF ให้ fair value ประมาณ USD 146.40 ต่อ diluted share และ bull case ยังเพียง USD 227.49. ดังนั้นสำหรับ new capital ควร **WAIT** จนกว่าจะได้ราคาที่มี margin of safety หรือ official results พิสูจน์ว่า FCF โตเร็วกว่าที่ guidance ปัจจุบันสะท้อน.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest regular-session close checked | USD 300.17 on 2026-05-20 | Stooq GE quote CSV, fetched 2026-05-21 Asia/Bangkok. |
| Shares outstanding | 1.043337B | GE Q1 2026 Form 10-Q. |
| Market cap | USD 313.18B | 300.17 * 1.043337B. |
| Diluted shares used in DCF | 1.054B | GE Q1 2026 weighted-average diluted shares. |
| Cash, cash equivalents and restricted cash | USD 10.981B | GE Q1 2026 Form 10-Q. |
| Total borrowings | USD 20.277B | GE Q1 2026 Form 10-Q calculation. |
| TTM GE-defined FCF | USD 7.901B | FY2025 FCF 7.694B - Q1 2025 FCF 1.451B + Q1 2026 FCF 1.658B. |
| FY2026 FCF guidance midpoint | USD 8.2B | Midpoint of GE guidance range. |
| TTM FCF yield | 2.52% | 7.901 / 313.18. |
| Market EV / TTM FCF | 40.81x | (313.18 + 20.277 - 10.981) / 7.901. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 orders grew 87% | Demand signal is very strong. | `raw/imports/GE_latest_results_source.md` |
| Q1 2026 adjusted revenue grew 29% | Growth is broad enough for a quality thesis. | `raw/financials/GE_fundamentals.md` |
| CES services revenue grew 39% | Aftermarket engine remains the key compounding driver. | GE Q1 2026 Form 10-Q / source note. |
| Q1 2026 FCF grew 14% | Cash flow supports guidance but does not justify any price. | `raw/financials/GE_fundamentals.md` |
| FY2026 FCF guidance is USD 8.0B-8.4B | Provides a source-backed valuation anchor. | GE Q1 2026 release. |
| Current market cap is about USD 313.18B | Market price embeds very high FCF multiple. | Stooq + GE share count. |
| Run-off insurance liabilities and investment securities are large | Balance-sheet adjustments need care. | GE Q1 2026 Form 10-Q. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 300.17 | Read |
|---|---:|---:|---|
| Bear | USD 94.94 | -68.4% | If growth slows or WACC rises, downside is severe. |
| Base | USD 146.40 | -51.2% | Business quality is not enough to support current price. |
| Bull | USD 227.49 | -24.2% | Even optimistic FCF growth remains below market price. |

Valuation read คือ GE น่าจะเป็น great company at a stretched price. การซื้อวันนี้ต้องเชื่อว่า FCF growth จะสูงกว่า scenario ปกติอย่างมาก หรือ market จะยอมให้ premium multiple สูงต่อเนื่องนานมาก.

## Bull Case

- GE Aerospace เป็น pure-play leader ใน commercial engines, defense propulsion, services, and MRO.
- Installed base และ long-term service agreements ทำให้ aftermarket economics มี durability.
- CES services growth, spare parts, shop visits, and MRO network expansion can compound revenue and margin.
- FY2026 guidance still points to FCF growth and >100% FCF conversion.
- Buybacks can reduce share count if management executes capital allocation well.
- Supply chain improvements could unlock more output and backlog conversion.

## Bear Case

- Current price implies only 2.52% TTM FCF yield and about 41.4x forward adjusted EPS.
- Supply chain delinquency and material availability remain constraints.
- Install engine mix and growth investments can pressure margin.
- Airlines may delay activity if fuel costs, geopolitics, or macro pressure worsen.
- Program-level profitability is not disclosed, so LEAP/GE9X/defense economics cannot be fully underwritten.
- Investment securities and insurance liabilities make simple excess-cash adjustments unsafe.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | GE-defined non-GAAP FCF | Matches company guidance and official reconciliations. |
| Starting FCF for base DCF | FY2026 guidance midpoint of USD 8.2B | More relevant than stale annual FCF alone, but still source-backed. |
| Debt treatment | Total borrowings minus cash/restricted cash | Conservative and avoids unsupported investment-securities adjustment. |
| Required margin of safety | High for new capital at premium multiple | Business is strong, but valuation risk is the main issue. |
| Investor profile | Long-term investor, normal-sized position | No position size, tax basis, or required return was provided. |

## What Would Change The Decision

- Upgrade toward WATCHLIST / selective ADD if price falls enough to lift forward FCF yield materially.
- Upgrade if FY2026 FCF tracks above USD 8.4B while CES margin and supply-chain execution improve.
- Keep WAIT if price remains near current levels and FCF stays only within guidance.
- Downgrade toward TRIM for existing oversized positions if price rises further without a commensurate FCF guide raise.
- Re-run DCF after Q2 2026 results and any disclosure that clarifies insurance/investment securities treatment.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year FCF and margin confirmation. |
| Forward GAAP reconciliation for non-GAAP guidance | not disclosed | Limits GAAP-to-FCF bridge. |
| Segment-level FCF | not disclosed | Cannot prove which segment drives cash conversion. |
| Program-level profitability | not disclosed | LEAP, GE9X, defense, and aftermarket economics cannot be modeled directly. |
| Customer concentration and airline credit exposure | not disclosed | Important because aftermarket cash flows depend on customer health. |
| Excess cash / insurance investment normalization | judgment required | Prevents confident use of all investment securities as excess cash. |
| Market quote after 2026-05-20 close | ไม่พบข้อมูลที่ยืนยันได้ | Refresh before future action changes. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/GE.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/GE_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, market data, cash, debt, FCF, guidance. |
| Latest results source note | `raw/imports/GE_latest_results_source.md` | Source map and extracted facts. |
| DCF valuation memo | `wiki/analysis/valuations/GE DCF Valuation 2026-05-21.md` | Source-backed DCF scenarios and sensitivity. |
| GE Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/40545/000004054526000027/ge-20260331.htm | Primary filing source. |
| GE Q1 2026 earnings release | https://www.sec.gov/Archives/edgar/data/40545/000004054526000026/ge1q2026earningsrelease.htm | Official results and guidance. |
| GE Q1 2026 earnings call transcript | https://www.geaerospace.com/sites/default/files/geaerospace_webcast_transcript_04212026.pdf | Management commentary. |
| GE FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm | FY2025 annual baseline. |
| Stooq GE quote CSV | https://stooq.com/q/l/?s=ge.us&f=sd2t2ohlcv&h&e=csv | Fresh market price. |
