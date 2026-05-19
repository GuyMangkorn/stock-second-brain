---
type: analysis
analysis_type: decision-memo
ticker: V
company: Visa Inc.
date: 2026-05-19
currency: USD
decision: WAIT / HOLD existing quality position
source_files:
  - index.md
  - wiki/entities/V.md
  - raw/financials/V_fundamentals.md
  - raw/imports/V_latest_results_source.md
  - wiki/analysis/valuations/V DCF Valuation 2026-05-19.md
tags:
  - analysis/decision-memo
  - ticker/V
---

# V Decision Memo - 2026-05-19

## Action Read

**Action: WAIT for new capital / HOLD existing quality position.**

Visa เป็น business quality สูงมาก และ Q2 FY2026 official results แข็งแรง: revenue growth 17%, operating margin มากกว่า 60%, VAS/CMS โตเร็ว, และ management raised FY2026 adjusted revenue/EPS outlook. แต่ที่ USD 332.64 valuation ยังไม่ให้ margin of safety ชัดเจน. Base-case DCF อยู่ประมาณ USD 233 ต่อ diluted share และ bull case อยู่ใกล้ current price เท่านั้น.

สำหรับ new capital action คือ **WAIT**. สำหรับ existing long-term quality position การ **HOLD** ยังสมเหตุสมผลได้ถ้า position size ไม่เกินกรอบและ investor รับ premium valuation ได้. ไม่ควร upgrade เป็น ADD จนกว่าจะเห็นราคาดีขึ้น, FCF conversion เร่งชัด, หรือ post-exchange share count ลดความไม่แน่นอนลง.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 332.64 | FinanceCharts price page, close for Monday, 2026-05-18; checked 2026-05-19 Bangkok time. |
| Market cap | USD 624.481B | FinanceCharts price page current metrics. |
| Diluted weighted-average Class A shares | 1.916B | SEC 10-Q / earnings release, Q2 FY2026. |
| Implied market cap using diluted shares | USD 637.3B | 332.64 * 1.916B; differs from provider market cap due to multi-class/share-conversion structure. |
| FY2025 FCF yield | 3.45% | USD 21.577B FY2025 FCF / USD 624.481B market cap. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | Q2 FY2026 | `raw/financials/V_fundamentals.md`. |
| Q2 FY2026 net revenue | USD 11.230B | SEC 10-Q / earnings release. |
| Q2 FY2026 net revenue growth | 17.05% YoY | SEC 10-Q / earnings release. |
| Q2 FY2026 operating income | USD 7.234B | SEC 10-Q. |
| Q2 FY2026 net income | USD 6.021B | SEC 10-Q / earnings release. |
| Q2 FY2026 diluted EPS | USD 3.14 | SEC 10-Q. |
| 6M FY2026 FCF | USD 9.027B | SEC 10-Q; OCF less capex. |
| FY2025 FCF | USD 21.577B | FY2025 Form 10-K; OCF less capex. |
| Cash + investment securities | USD 14.221B | SEC 10-Q. |
| Total debt | USD 23.976B | SEC 10-Q debt note. |
| Net debt | USD 9.755B | SEC 10-Q calculation. |
| FY2026 adjusted net revenue guidance | low-double-digit to low-teens growth | Q2 FY2026 transcript. |
| FY2026 adjusted EPS guidance | low-teens growth | Q2 FY2026 transcript. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 233.21 per diluted share | ต่ำกว่า current price ประมาณ 30% |
| DCF bull fair value | USD 336.91 per diluted share | ใกล้ current price แต่ต้องใช้ assumptions ที่ favorable |
| Market cap / FY2025 FCF | 28.9x | premium multiple |
| FY2025 FCF yield | 3.45% | quality สูง แต่ยังไม่ถูกชัด |
| Base terminal value share of EV | 76.7% | assumption-heavy but not above warning zone |

valuation ไม่ได้บอกว่า Visa เป็นธุรกิจอ่อนแอ. ตรงข้าม source-backed facts ยืนยันว่า business economics แข็งแรงมาก. แต่ current price ต้องการการเติบโตต่อเนื่อง, buybacks ที่ value-accretive, และความเสี่ยง regulatory/litigation ที่ไม่แย่ลง.

## Bull Case

- Q2 FY2026 net revenue โต 17% และ operating income โต 33% YoY.
- Operating margin 64.4% สะท้อน network economics ที่หาได้ยาก.
- VAS revenue โต 27% constant dollar และมี distribution advantage จาก transaction/card/account data.
- CMS revenue โต 24% constant dollar และ Visa Direct transactions โต 23% YoY.
- Management raised full-year adjusted revenue และ EPS guide.
- Buyback capacity ประมาณ USD 33B หลัง April authorization สามารถ support per-share growth ได้.

## Bear Case

- Current valuation ประมาณ 28.9x FY2025 FCF และ FCF yield เพียง 3.45%.
- 6M FY2026 FCF ลดลง 4.2% YoY แม้ earnings โตดี จึงต้อง monitor cash conversion.
- Regulatory scrutiny, interchange litigation, fee pressure และ network competition เป็น long-lived risks.
- Cross-border travel และ volatility ช่วย/กดรายได้ได้เป็นรอบ และ Middle East conflict เป็น near-term uncertainty.
- Product-level economics ของ agentic commerce, stablecoin settlement, Visa Direct และ VAS ไม่ได้ disclosed.
- Post-exchange-offer diluted share count ยังไม่เป็น single clean number ใน checked sources.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term investor ที่ต้องการ quality compounding แต่ยังสนใจ margin of safety |
| Position status | Unknown; action จึงแยก new capital จาก existing position |
| FCF anchor | FY2025 FCF USD 21.577B; not company forward FCF guidance |
| Valuation framework | Mature high-quality payments network DCF with 8.5% base WACC and 2.5% terminal growth |
| Quality vs price | ยอมรับ business quality แต่ wait เพราะ valuation ต้องการ assumptions ที่ดีมาก |

## What Would Change The Decision

- Upgrade toward add ถ้า price ลดลงจน FCF yield สูงขึ้นชัด โดย official growth/FCF ยัง intact.
- Upgrade ถ้า FY2026 FCF conversion เร่งจน support value above current price without aggressive assumptions.
- Upgrade ถ้า Visa discloses cleaner post-exchange diluted share count and buybacks reduce per-share denominator materially.
- Upgrade ถ้า VAS/CMS growth remains above company average while margins stay strong.
- Downgrade toward trim ถ้า regulatory/litigation risk escalates, FCF conversion weakens, or guidance upgrades are not backed by cash flow.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Forward free cash flow guidance | not disclosed | DCF forecast uses assumptions, not company FCF guidance. |
| Post-exchange-offer fully diluted share count | ไม่พบข้อมูลที่ยืนยันได้ | Affects exact per-share valuation and buyback math. |
| Segment profit by growth engine | not disclosed | Limits VAS/CMS separate valuation. |
| Product-level economics for agentic commerce, stablecoin settlement, and Visa Direct | not disclosed | Limits underwriting of new growth engines. |
| Investor-specific cost basis and position size | not provided | Makes universal trim/hold sizing recommendation inappropriate. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/V_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/financials/V_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios. |
| `wiki/entities/V.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/V DCF Valuation 2026-05-19.md` | Local valuation memo | P11 DCF and valuation sensitivity. |
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1403161/000140316126000079/v-20260331.htm | Official quarterly facts. |
| FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm | FY2025 annual baseline and FCF. |
| Visa Q2 FY2026 transcript | https://s1.q4cdn.com/050606653/files/doc_financials/2026/q2/CORRECTED-TRANSCRIPT_-Visa-Inc-V-US-Q2-2026-Earnings-Call-28-April-2026-5_00-PM-ET-4.pdf | Management commentary and guidance. |
| FinanceCharts V price page | https://www.financecharts.com/stocks/V/summary/price | Fresh price and market-data check. |
