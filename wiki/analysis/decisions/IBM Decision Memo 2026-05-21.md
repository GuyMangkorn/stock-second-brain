---
type: analysis
analysis_type: decision-memo
ticker: IBM
company: International Business Machines Corporation
date: 2026-05-21
currency: USD
decision: HOLD / WATCHLIST; selective ADD only with stronger margin of safety
source_files:
  - index.md
  - wiki/entities/IBM.md
  - raw/financials/IBM_fundamentals.md
  - raw/imports/IBM_latest_results_source.md
  - wiki/analysis/valuations/IBM DCF Valuation 2026-05-21.md
tags:
  - analysis/decision-memo
  - ticker/IBM
---

# IBM Decision Memo - 2026-05-21

## Action Read

**Action: HOLD / WATCHLIST. Selective ADD only if price offers more margin of safety or Q2/FY2026 evidence confirms FCF growth and deleveraging.**

IBM มี official-source setup ที่ดีกว่า legacy perception: Q1 2026 revenue โต, Software-led mix ชัดขึ้น, IBM Z cycle แข็งแรง, FCF โต 13%, และ management ยัง guide FY2026 FCF เพิ่มประมาณ USD 1B. แต่ current price ที่ USD 224.88 ให้ base-case DCF upside เพียงประมาณ 6.8% เท่านั้น ยังไม่พอสำหรับ aggressive new money ถ้าต้องการ margin of safety.

สำหรับ existing position ขนาดปกติ: **HOLD** ได้ เพราะ FCF yield และ DCF ไม่ได้บอกว่า overvalued ชัดเจน. สำหรับ new capital: **WATCHLIST / selective ADD** เฉพาะเมื่อราคาอ่อนลงหรือมีหลักฐานเพิ่มว่า Software + AI growth แปลงเป็น FCF และ debt reduction ได้จริง.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest regular-session close checked | USD 224.88 on 2026-05-20 | Stooq IBM quote CSV, fetched 2026-05-21 Asia/Bangkok. |
| Shares outstanding | 939.885M | IBM Q1 2026 Form 10-Q cover page. |
| Market cap | USD 211.36B | 224.88 * 939.885M. |
| Diluted shares used in DCF | 952.1M | IBM Q1 2026 weighted-average diluted shares. |
| Cash + restricted cash + marketable securities | USD 11.828B | IBM Q1 2026 Form 10-Q. |
| Total debt | USD 66.4B | IBM Q1 2026 earnings release. |
| IBM Financing debt included in total debt | USD 12.8B | IBM Q1 2026 earnings release and prepared remarks. |
| TTM IBM-defined FCF | USD 14.992B | FY2025 FCF 14.734B - Q1 2025 FCF 1.962B + Q1 2026 FCF 2.220B. |
| FCF yield | 7.09% | 14.992 / 211.36. |
| Market EV / TTM FCF | 17.74x | (211.36 + 66.40 - 11.828) / 14.992. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 revenue grew 9.46% reported | Growth is real and broad enough for thesis work. | `raw/financials/IBM_fundamentals.md` |
| Software revenue was USD 7.052B, 44.3% of Q1 revenue | IBM is genuinely Software-led by mix. | `raw/financials/IBM_fundamentals.md` |
| Consulting grew only 1% constant currency | Consulting remains the slower part of the portfolio. | IBM prepared remarks / source note. |
| Infrastructure grew 12% constant currency and IBM Z grew 48% | Strong z17 cycle supports near-term growth but may be cyclical. | IBM prepared remarks / source note. |
| Q1 IBM-defined FCF grew 13.15% YoY | Cash conversion is moving in the right direction. | IBM Form 10-Q reconciliation. |
| FY2026 FCF guide implies about USD 15.7B | Management is still confident in FCF growth. | IBM Q1 release and prepared remarks. |
| Total debt is USD 66.4B | Balance sheet is the main valuation constraint. | IBM Q1 release. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 224.88 | Read |
|---|---:|---:|---|
| Bear | USD 152.63 | -32.1% | If growth fades and leverage remains a drag, downside is meaningful. |
| Base | USD 240.27 | +6.8% | Fair-ish, but margin of safety is thin. |
| Bull | USD 367.87 | +63.6% | Requires stronger sustained FCF growth, lower risk premium, and successful Software/AI execution. |

Base case does not justify an aggressive add because expected upside is modest and source gaps are material. The stock can still be worth holding because FCF yield is reasonable, guidance supports FCF growth, and the business mix is improving.

## Bull Case

- Software-led mix is now large enough to change IBM's long-term quality profile.
- Red Hat/OpenShift, Data, Automation, Transaction Processing, and watsonx can create recurring enterprise AI/hybrid-cloud demand.
- FY2026 FCF guidance of about USD 15.7B implies a current FCF yield above 7%.
- IBM Z / z17 cycle is strong and mission-critical workloads are sticky.
- Productivity savings and margin expansion can offset acquisition dilution from Confluent.
- If debt declines, equity value can rise even without heroic growth assumptions.

## Bear Case

- Total debt of USD 66.4B is material, especially after Confluent.
- IBM Financing makes simple EV and FCF interpretation less clean.
- Consulting growth is still slow; GenAI backlog penetration must convert into actual revenue.
- Product-level AI revenue and margins are not disclosed, so AI economics are hard to underwrite.
- Infrastructure strength may be partly cyclical from z17 rather than recurring long-term growth.
- Base DCF upside is only 6.8%, so current price does not give much room for execution error.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | IBM-defined FCF | IBM explicitly adjusts for Financing receivables; using simple GAAP OCF minus capex would distort comparability. |
| Debt treatment | Total debt in base DCF | Conservative; excluding IBM Financing debt would raise valuation but requires judgment. |
| Required margin of safety | More than low single-digit upside for new money | IBM has leverage and execution risk; small DCF upside is not enough for high-conviction add. |
| Investor profile | Long-term investor, normal-sized position | Without position size and tax basis, memo avoids individualized trim/add sizing. |
| AI economics | Positive but not directly modeled | Product-level AI revenue/margins are not disclosed. |

## What Would Change The Decision

- Upgrade toward ADD if Q2/FY2026 data confirms FCF tracking toward USD 15.7B+, Software growth stays 10%+, Consulting accelerates, and debt starts declining.
- Upgrade toward ADD if price falls meaningfully below base fair value without thesis deterioration.
- Downgrade toward WAIT / TRIM if FCF guide is cut, debt remains elevated, Consulting growth stalls, or AI/Software growth proves mostly acquisition-driven.
- Re-run DCF after any official disclosure of AI book-of-business, product-level AI economics, or post-Confluent debt reduction.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year FCF and debt trajectory. |
| Product-level AI revenue and AI margins | not disclosed | Cannot directly underwrite AI unit economics. |
| Exact Q1 2026 generative AI book of business value | ไม่พบข้อมูลที่ยืนยันได้ | AI pipeline expansion is not fully quantified. |
| Segment-level FCF | not disclosed | Cannot prove which segment drives cash conversion. |
| Full detailed balance sheet normalization | not completed | Current decision has required cash/debt/shares, but broader balance-sheet line review is still a follow-up. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/IBM.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/IBM_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, market data, cash, debt, FCF, guidance. |
| Latest results source note | `raw/imports/IBM_latest_results_source.md` | Source map and extracted facts. |
| DCF valuation memo | `wiki/analysis/valuations/IBM DCF Valuation 2026-05-21.md` | Source-backed DCF scenarios and sensitivity. |
| IBM Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/51143/000005114326000038/ibm-20260331.htm | Primary filing source. |
| IBM Q1 2026 earnings release | https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS | Official results and guidance. |
| IBM 1Q26 prepared remarks | https://www.ibm.com/downloads/documents/us-en/15db805fff4249f1 | Official management commentary. |
| Stooq IBM quote CSV | https://stooq.com/q/l/?s=ibm.us&f=sd2t2ohlcv&h&e=csv | Fresh market price. |
