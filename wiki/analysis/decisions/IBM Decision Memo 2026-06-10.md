---
type: analysis
analysis_type: decision-memo
ticker: IBM
company: International Business Machines Corporation
date: 2026-06-10
currency: USD
decision: WAIT / HOLD-existing-only; do not add at current price without stronger FCF/debt proof
source_files:
  - index.md
  - wiki/entities/IBM.md
  - raw/financials/IBM_fundamentals.md
  - raw/imports/IBM_latest_results_source.md
  - raw/imports/IBM_market_quote_2026-06-10.md
  - wiki/analysis/valuations/IBM DCF Valuation 2026-06-10.md
tags:
  - analysis/decision-memo
  - ticker/IBM
---

# IBM Decision Memo - 2026-06-10

## Action Read

**Action: WAIT for new capital / HOLD existing normal-sized position. Avoid adding at USD 277.49 unless the investor has a specific strategic reason or a lower required return.**

IBM ยังเป็น story ที่ดีขึ้น: Software-led mix, Red Hat/OpenShift, Data/Automation, z17 cycle, enterprise AI/hybrid-cloud demand, FCF guidance และ dividend discipline ยัง support คุณภาพธุรกิจ. แต่ราคาขึ้นมามากจาก DCF refresh เดิม: latest quote USD 277.49 เทียบกับ USD 224.88 ใน memo วันที่ 2026-05-21 หรือเพิ่มประมาณ 23.4%.

ที่ราคานี้ base-case DCF fair value USD 240.27 ให้ downside ประมาณ 13.4%. ดังนั้นมุมมองเปลี่ยนจาก `HOLD / WATCHLIST` เป็น **WAIT / HOLD-existing-only**. ถ้ามี position อยู่ขนาดปกติยังถือรอดู Q2 ได้ แต่ถ้าเป็น new money ผมยังไม่ไล่ราคา.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest quote used | USD 277.49 | Alpha Vantage `GLOBAL_QUOTE`, latest trading day 2026-06-09; fetched 2026-06-10 Asia/Bangkok. |
| Prior DCF price | USD 224.88 | Prior DCF memo checked 2026-05-21 using 2026-05-20 close. |
| Price move since prior DCF | +23.4% | 277.49 / 224.88 - 1. |
| Shares outstanding | 939.885M | IBM Q1 2026 Form 10-Q cover page. |
| Market cap | USD 260.81B | 277.49 * 939.885M. |
| Diluted shares used in DCF | 952.1M | IBM Q1 2026 weighted-average diluted shares. |
| Cash + restricted cash + marketable securities | USD 11.828B | IBM Q1 2026 Form 10-Q. |
| Total debt | USD 66.4B | IBM Q1 2026 earnings release. |
| IBM Financing debt included in total debt | USD 12.8B | IBM Q1 2026 earnings release and prepared remarks. |
| TTM IBM-defined FCF | USD 14.992B | FY2025 FCF 14.734B - Q1 2025 FCF 1.962B + Q1 2026 FCF 2.220B. |
| FCF yield | 5.75% | 14.992 / 260.81. |
| Market EV / TTM FCF | 21.04x | (260.81 + 66.40 - 11.828) / 14.992. |
| FY2026 guided FCF yield | about 6.03% | About USD 15.7B FCF guidance / USD 260.81B market cap. |
| Annualized dividend yield | about 2.44% | USD 1.69 quarterly dividend * 4 / 277.49. |

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

| Scenario | Fair Value / Share | Upside / Downside vs USD 277.49 | Read |
|---|---:|---:|---|
| Bear | USD 152.63 | -45.0% | If growth fades and leverage remains a drag, downside is large. |
| Base | USD 240.27 | -13.4% | Current price is above source-backed base value. |
| Bull | USD 367.87 | +32.6% | Requires stronger sustained FCF growth, lower risk premium, and successful Software/AI execution. |

The market is now paying for more of the bull case. That does not make IBM a bad company, but it reduces the margin of safety. At current price, the thesis needs Q2 confirmation: Software durability, Consulting conversion, post-Confluent integration, FCF tracking, and debt reduction.

## Bull Case

- IBM has shifted from legacy services perception toward a Software-led hybrid cloud and AI platform.
- Red Hat/OpenShift, Data, Automation, Transaction Processing, and watsonx can create recurring enterprise AI demand.
- FY2026 FCF guidance of about USD 15.7B still supports a roughly 6% guided FCF yield at current price.
- IBM Z / z17 cycle is strong and mission-critical workloads are sticky.
- Confluent can improve IBM's real-time data layer for enterprise AI and agent workloads.
- Debt reduction would directly lift equity value and improve the risk premium.

## Bear Case

- Price already moved 23.4% from the prior DCF price, while official financial inputs are still Q1 2026.
- Base DCF now shows 13.4% downside, so new money has weak margin of safety.
- Total debt of USD 66.4B remains material after Confluent.
- Consulting growth is still slow; GenAI backlog must convert into revenue and FCF.
- Product-level AI revenue and margins are not disclosed, so AI economics are hard to underwrite.
- Infrastructure strength may be partly cyclical from z17 rather than recurring long-term growth.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | IBM-defined FCF | IBM explicitly adjusts for Financing receivables; using simple GAAP OCF minus capex would distort comparability. |
| Debt treatment | Total debt in base DCF | Conservative; excluding IBM Financing debt would raise valuation but requires judgment. |
| Current price | USD 277.49 | Latest quote source returned 2026-06-09 trading day. |
| Required margin of safety | Positive base-case upside for new money | Current price fails this test. |
| Investor profile | Long-term investor, normal-sized position | Without position size and tax basis, memo avoids individualized trim/add sizing. |
| AI economics | Positive but not directly modeled | Product-level AI revenue/margins are not disclosed. |

## What Would Change The Decision

- Upgrade toward ADD if Q2/FY2026 results show FCF above trajectory, Software remains 10%+, Consulting accelerates, and debt starts falling.
- Upgrade toward ADD if price falls back near or below the base DCF range without thesis deterioration.
- Keep HOLD if IBM executes but price remains high; dividend and FCF quality may still justify holding an existing normal-sized position.
- Downgrade toward TRIM if position size is large and Q2 does not confirm the stronger expectations now embedded in price.
- Downgrade if FCF guide is cut, debt rises further, Consulting stays weak, or AI/Software growth proves mostly acquisition-driven.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year FCF and debt trajectory. |
| Q2 2026 results | not disclosed | Current price has moved before the next official quarterly proof point. |
| Product-level AI revenue and AI margins | not disclosed | Cannot directly underwrite AI unit economics. |
| Exact Q1 2026 generative AI book of business value | ไม่พบข้อมูลที่ยืนยันได้ | AI pipeline expansion is not fully quantified. |
| Segment-level FCF | not disclosed | Cannot prove which segment drives cash conversion. |
| Intraday 2026-06-10 real-time quote | not disclosed | Market quote source returned 2026-06-09 latest trading day. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/IBM.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/IBM_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, cash, debt, FCF, shares, guidance. |
| Latest results source note | `raw/imports/IBM_latest_results_source.md` | Official-source map and extracted facts. |
| Market quote source note | `raw/imports/IBM_market_quote_2026-06-10.md` | Fresh price and current market calculations. |
| DCF valuation memo | `wiki/analysis/valuations/IBM DCF Valuation 2026-06-10.md` | Source-backed DCF scenarios and sensitivity. |
| IBM Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/51143/000005114326000038/ibm-20260331.htm | Primary filing source. |
| IBM Q1 2026 earnings release | https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS | Official results, guidance, debt/cash, dividend. |
| IBM 1Q26 prepared remarks | https://www.ibm.com/downloads/documents/us-en/15db805fff4249f1 | Official management commentary. |
| Alpha Vantage `GLOBAL_QUOTE` | https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo | Market quote checked 2026-06-10 Asia/Bangkok. |
