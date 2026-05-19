---
type: analysis
analysis_type: decision-memo
ticker: GOOGL
company: Alphabet Inc.
date: 2026-05-18
currency: USD
decision: WAIT / AVOID new capital at current price
source_files:
  - index.md
  - wiki/entities/GOOGL.md
  - raw/financials/GOOGL_fundamentals.md
  - raw/imports/GOOGL_latest_results_source.md
  - wiki/analysis/valuations/GOOGL DCF Valuation 2026-05-18.md
tags:
  - analysis/decision-memo
  - ticker/GOOGL
---

# GOOGL Decision Memo - 2026-05-18

## Action Read

**Action: WAIT / AVOID new capital at current price.**

Alphabet เป็น high-quality business ที่มี Google Cloud revenue เร่งตัว, cloud backlog ขนาดใหญ่ และ Google Services profitability ที่ยังโดดเด่นมาก. ปัญหาหลักคือ price. ที่ fresh market price USD 404.15 หุ้นดูเหมือนต้องการ FCF recovery ที่ aggressive มาก ในขณะที่ official guidance ระบุว่า capex จะยังสูงมากในปี 2026 และจะเพิ่มขึ้นอย่างมีนัยสำคัญอีกครั้งในปี 2027

สำหรับ new position action คือ **WAIT**. สำหรับ existing position action คือ **HOLD only if sizing is normal and the investor is explicitly underwriting a long AI infrastructure payoff**. ถ้า position กลายเป็น oversized หลังหุ้นขึ้นแรง การ **trim** ถือว่าสมเหตุสมผลตาม valuation discipline

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 404.15 | StockAnalysis GOOGL overview, May 18, 2026, 11:16 AM EDT. |
| Market cap | USD 4.90 trillion | StockAnalysis GOOGL overview, checked 2026-05-18. |
| Shares outstanding | 12.12 billion | StockAnalysis GOOGL overview/statistics; official 10-Q shows 12.116 billion at 2026-03-31. |
| TTM revenue | USD 422.50 billion | StockAnalysis GOOGL overview, market-data context. |
| TTM net income | USD 160.21 billion | StockAnalysis GOOGL overview, market-data context. |
| P/E | 30.27x | StockAnalysis GOOGL overview, market-data context. |
| Price target context | USD 427.89 average target | StockAnalysis GOOGL overview; lower-priority market context, not company fact. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | Q1 2026 | `raw/financials/GOOGL_fundamentals.md` |
| Q1 2026 revenue | USD 109.896B | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Q1 2026 revenue growth | 21.79% YoY | Calculated from Q1 2026 and Q1 2025 revenue. |
| Q1 2026 operating income | USD 39.696B | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Q1 2026 operating margin | 36.12% | Calculated from official tables. |
| Q1 2026 net income | USD 62.578B | Alphabet Q1 2026 earnings release and Form 10-Q; includes large equity-security gains. |
| Q1 2026 FCF | USD 10.116B | Alphabet Q1 2026 earnings release FCF reconciliation. |
| TTM FCF | USD 64.429B | Alphabet Q1 2026 earnings release FCF reconciliation. |
| Q1 2026 Google Services revenue | USD 89.637B | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Q1 2026 Google Services operating income | USD 40.589B | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Q1 2026 Google Cloud revenue | USD 20.028B | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Q1 2026 Google Cloud revenue growth | 63% YoY | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Q1 2026 Google Cloud operating income | USD 6.598B | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Revenue backlog | USD 467.6B | Alphabet Q1 2026 Form 10-Q. |
| Google Cloud backlog | USD 462.3B | Alphabet Q1 2026 Form 10-Q. |
| 2026 capex guidance | USD 180B-190B | Alphabet Q1 2026 transcript. |
| 2027 capex direction | Significantly higher than 2026 | Alphabet Q1 2026 transcript; amount not disclosed. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 112.92 per diluted share | ต่ำกว่า fresh market price ประมาณ 72% |
| DCF bull fair value | USD 259.00 per diluted share | ยังต่ำกว่า fresh market price ประมาณ 36% |
| Market cap / TTM FCF | 76.1x | ตลาดกำลังจ่าย multiple สูงมากบน cash flow ในช่วง capex-heavy |
| TTM FCF yield | 1.32% | ต่ำเกินไปสำหรับ ordinary execution risk เว้นแต่ FCF จะ ramp เร็วมาก |
| Reverse DCF | About 44.1% 5-year FCF CAGR required | aggressive มากเมื่อเริ่มจาก TTM FCF USD 64.429B |

valuation บอกว่าตลาด capitalize AI/cloud upside ไปมากแล้ว. Alphabet อาจยัง grow into this price ได้ แต่ margin of safety บางมาก เว้นแต่ FCF จะ accelerate อย่างแรง

## Bull Case

- Google Services ยังเป็น profit pool ที่ยอดเยี่ยม โดย Q1 2026 operating income อยู่ที่ USD 40.589B
- Search และ Gemini-related surfaces อาจช่วยปกป้องหรือขยาย engagement และ management ระบุว่า AI Overviews, AI Mode และ Gemini กำลังช่วยหนุน usage
- Google Cloud scale เร็วมาก: Q1 2026 revenue เพิ่ม 63% YoY และ operating income ถึง USD 6.598B
- Cloud backlog USD 462.3B เป็น forward demand signal ที่จับต้องได้
- Alphabet มี balance sheet แข็งแรง พร้อม cash and marketable securities USD 126.840B
- Vertical integration ตั้งแต่ models, TPU infrastructure, Search, YouTube, Android, Workspace, Cloud และ Gemini อาจสร้าง durable AI economics ได้

## Bear Case

- capex สูงมาก: Q1 2026 capex อยู่ที่ USD 35.674B และ 2026 guidance อยู่ที่ USD 180B-190B
- management คาดว่า 2027 capex จะเพิ่มขึ้นอย่างมีนัยสำคัญ ดังนั้น FCF pressure ไม่ใช่ประเด็นปีเดียว
- Q1 2026 FCF ลดลงเหลือ USD 10.116B แม้ revenue และ operating income growth แข็งแรง
- Q1 2026 net income ได้แรงหนุนจาก after-tax equity-security gains USD 28.7B
- TPU hardware sales และ AI infrastructure contracts อาจเพิ่ม revenue แต่ไม่จำเป็นต้องแปลเป็น high-margin FCF
- regulatory, antitrust, privacy และ AI search disruption risks ยังเป็นความเสี่ยงจริง
- ที่ USD 404.15 แม้ bull DCF case ก็ยังต่ำกว่า market price

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term investor ที่ focus risk-adjusted compounding ไม่ใช่ short-term momentum |
| Position status | ยังไม่รู้; action จึงแยก new capital ออกจาก existing position sizing |
| Valuation discipline | fresh price ต้องเทียบกับ source-backed FCF ไม่ใช่แค่ revenue growth หรือ analyst targets |
| AI economics | demand เป็นของจริง แต่ product-level AI margins และ TPU hardware economics ยังไม่ disclosed |
| FCF recovery | เป็นไปได้ แต่ยัง verify ได้ไม่แข็งแรงพอที่จะ justify การ add ที่ current price |

## What Would Change The Decision

- upgrade toward add ถ้า price ลดลงอย่างมีนัยสำคัญ ขณะที่ official sources ยังแสดง cloud backlog conversion ที่แข็งแรงและ Google Services profitability ที่ stable
- upgrade ถ้า FCF เพิ่มขึ้นแม้ capex ยังสูง โดยเฉพาะถ้า TTM FCF เริ่มขยับเข้าใกล้ DCF bull path
- upgrade ถ้า management quantify 2027 capex แล้วออกมาเบากว่า qualitative warning ปัจจุบัน
- upgrade ถ้า Alphabet disclose AI product หรือ TPU economics ที่ support ROIC แข็งแรง
- downgrade toward trim ถ้า capex เพิ่มอีกโดยไม่มี FCF recovery, Google Cloud margin อ่อนลง, backlog quality แย่ลง หรือ Search monetization เริ่มเห็น AI-driven pressure

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Product-level AI revenue and margin for AI Overviews, Gemini, Vertex AI, TPU sales, and AI infrastructure | Not disclosed | ยัง underwrite AI economics โดยตรงไม่ได้ |
| Exact TPU hardware sales economics and customer concentration | Not disclosed | สำคัญต่อการประเมินว่า backlog เป็น high-quality FCF หรือเป็น lower-margin hardware/infrastructure revenue |
| Quantified 2027 capex | Not disclosed | เป็น input สำคัญของ FCF recovery |
| FY2026 full-year results | ไม่พบข้อมูลที่ยืนยันได้ | Q1 และ TTM data คือ cash-flow facts ที่สดและ verify ได้ที่สุด |
| Investor-specific tax basis and position size | Not provided | ทำให้ให้ universal hold/trim answer สำหรับ existing holders ไม่ได้ |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/GOOGL_latest_results_source.md` | Local source note | P1 official-source discovery และ extraction |
| `raw/financials/GOOGL_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios |
| `wiki/entities/GOOGL.md` | Local entity page | P6 business model, thesis, risks, catalysts |
| `wiki/analysis/valuations/GOOGL DCF Valuation 2026-05-18.md` | Local valuation memo | P11 DCF และ valuation sensitivity |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm | Official quarterly facts |
| Alphabet Q1 2026 earnings release | https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/2026q1-alphabet-earnings-release.pdf | Financial tables และ FCF |
| Alphabet Q1 2026 transcript | https://s206.q4cdn.com/479360582/files/doc_events/2026/Apr/29/2026_Q1_Earnings_Transcript.pdf | Capex guidance และ management commentary |
| StockAnalysis GOOGL overview | https://stockanalysis.com/stocks/googl/ | Fresh price และ market data checked 2026-05-18 |
