---
type: analysis
analysis_type: decision-memo
ticker: MSFT
company: Microsoft Corporation
date: 2026-05-18
currency: USD
decision: WAIT for new capital; HOLD existing core position
source_files:
  - index.md
  - wiki/entities/MSFT.md
  - raw/financials/MSFT_fundamentals.md
  - raw/imports/MSFT_latest_results_source.md
  - raw/imports/MSFT_company_deep_dive_2026-05-17.md
  - wiki/analysis/valuations/MSFT DCF Valuation 2026-05-18.md
tags:
  - analysis/decision-memo
  - ticker/MSFT
---

# MSFT Decision Memo - 2026-05-18

## Decision

**Action: WAIT for new capital; HOLD an existing normal-sized core position.**

Microsoft ยังเป็น high-quality compounder โดย official sources สนับสนุนชัดเจนทั้ง cloud, AI, productivity, developer, security และ enterprise distribution momentum. เหตุผลที่ยังไม่ควร add วันนี้คือ valuation ไม่ใช่ business quality. ที่ราคาตลาดที่เช็กสดล่าสุด หุ้นยังต้องการ free-cash-flow conversion story ที่ดีมาก ในขณะที่ Microsoft กำลังเข้าสู่ช่วง AI buildout ที่ใช้ capital intensity สูงขึ้นมาก

memo นี้ไม่ได้แนะนำให้ trim แบบ blanket เว้นแต่ MSFT จะมีน้ำหนัก oversized ใน portfolio อยู่แล้ว หรือ investor ต้องการลด exposure ต่อ expensive mega-cap AI/platform duration. ถ้า position ยังเป็น normal-sized และ tax/friction costs มีผล การกระทำที่สะอาดกว่าคือ hold แล้วรอทั้งราคาที่ดีกว่านี้ หรือหลักฐานที่ชัดขึ้นว่า AI capex กำลังแปลงเป็น durable free cash flow

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Vault dashboard | `index.md` | ยืนยันว่า MSFT อยู่ใน active coverage และมี source gaps อะไรบ้าง |
| Entity page | `wiki/entities/MSFT.md` | Business model, source map, moat, thesis, risks, catalysts, valuation watch items |
| Normalized financial facts | `raw/financials/MSFT_fundamentals.md` | FY2025 baseline, FY26 Q3 / 9M FY26 financial facts, cash flow, balance sheet |
| Latest results source note | `raw/imports/MSFT_latest_results_source.md` | Local source digest จาก FY26 Q3 official filings, IR tables และ transcript |
| Company deep dive source note | `raw/imports/MSFT_company_deep_dive_2026-05-17.md` | FY2025 annual baseline, segment mix, product/service mix, moat และ AI/capex context |
| DCF valuation memo | `wiki/analysis/valuations/MSFT DCF Valuation 2026-05-18.md` | Source-backed valuation scenarios และ reverse DCF |
| Microsoft FY26 Q3 income statements | https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q3/income-statements | Official quarterly revenue, operating income, net income, EPS |
| Microsoft FY26 Q3 cash flows | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/cash-flows | Official operating cash flow และ capex inputs |
| Microsoft FY26 Q3 earnings transcript | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3 | Management commentary เกี่ยวกับ Azure, AI, RPO, capex และ guidance |
| StockAnalysis MSFT statistics | https://stockanalysis.com/stocks/msft/statistics/ | Fresh market price, valuation ratios, market cap, shares, TTM FCF และ analyst context ที่เช็กเมื่อ 2026-05-18 |

## Facts

### Business And Operating Facts

| Fact | Value | Source |
|---|---:|---|
| Latest verified period in vault | FY26 Q3, quarter ended 2026-03-31 | `wiki/entities/MSFT.md`; `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 revenue | 82,886 million | Microsoft FY26 Q3 income statements; `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 revenue growth | 18.3% YoY | Calculated from 82,886 / 70,066 - 1 |
| FY26 Q3 operating income | 38,398 million | Microsoft FY26 Q3 income statements; `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 operating income growth | 20.0% YoY | Calculated from 38,398 / 32,000 - 1 |
| FY26 Q3 net income | 31,778 million | Microsoft FY26 Q3 income statements; `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 net income growth | 23.1% YoY | Calculated from 31,778 / 25,824 - 1 |
| FY26 Q3 diluted EPS | 4.27 | Microsoft FY26 Q3 income statements; `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 operating margin | 46.33% | `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 Microsoft Cloud revenue | 54,500 million | `raw/imports/MSFT_company_deep_dive_2026-05-17.md` |
| FY26 Q3 Azure and other cloud services growth | 40% YoY | `wiki/entities/MSFT.md`; Microsoft FY26 Q3 transcript |
| FY26 Q3 AI business annual revenue run rate | 37,000 million | `raw/imports/MSFT_company_deep_dive_2026-05-17.md`; Microsoft FY26 Q3 transcript |
| FY26 Q3 commercial RPO | 627,000 million | `raw/imports/MSFT_company_deep_dive_2026-05-17.md`; Microsoft FY26 Q3 transcript |
| Microsoft 365 Copilot paid seats | More than 20 million | `wiki/entities/MSFT.md`; Microsoft FY26 Q3 transcript |

### Cash Flow And Capital Intensity Facts

| Fact | Value | Source |
|---|---:|---|
| FY26 Q3 operating cash flow | 46,679 million | Microsoft FY26 Q3 cash flows; `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 capex spend | 30,876 million | Microsoft FY26 Q3 cash flows; `raw/financials/MSFT_fundamentals.md` |
| FY26 Q3 free cash flow | 15,803 million | Calculated: 46,679 - 30,876 |
| FY26 Q3 free cash flow change | -22.1% YoY | Calculated from 15,803 / 20,299 - 1 |
| 9M FY26 operating cash flow | 127,494 million | Microsoft FY26 Q3 cash flows; `raw/financials/MSFT_fundamentals.md` |
| 9M FY26 capex spend | 80,146 million | Microsoft FY26 Q3 cash flows; `raw/financials/MSFT_fundamentals.md` |
| 9M FY26 free cash flow | 47,348 million | Calculated: 127,494 - 80,146 |
| 9M FY26 free cash flow change | 2.8% YoY | Calculated from 47,348 / 46,043 - 1 |
| Calendar 2026 capex expectation | Roughly 190,000 million | Microsoft FY26 Q3 transcript; `raw/imports/MSFT_company_deep_dive_2026-05-17.md` |
| FY26 Q4 capex guidance | More than 40,000 million | Microsoft FY26 Q3 transcript; `wiki/analysis/valuations/MSFT DCF Valuation 2026-05-18.md` |

### Fresh Market And Valuation Facts

| Fact | Value | Source |
|---|---:|---|
| Latest regular-session close checked | 421.92 on 2026-05-15, 4:00 PM EDT | StockAnalysis MSFT statistics, checked 2026-05-18 15:34 Asia/Bangkok |
| Premarket quote checked | 420.19 on 2026-05-18, 4:01 AM EDT | StockAnalysis MSFT statistics, checked 2026-05-18 15:34 Asia/Bangkok |
| Market capitalization | 3.13 trillion | StockAnalysis MSFT statistics |
| Shares outstanding | 7.43 billion | StockAnalysis MSFT statistics; Microsoft balance sheet also shows 7.429 billion shares outstanding at 2026-03-31 |
| Trailing P/E | 25.13x | StockAnalysis MSFT statistics |
| Forward P/E | 22.77x | StockAnalysis MSFT statistics |
| Price / FCF | 42.98x | StockAnalysis MSFT statistics |
| EV / FCF | 43.63x | StockAnalysis MSFT statistics |
| TTM free cash flow | 72.92 billion | StockAnalysis MSFT statistics; consistent with DCF memo TTM FCF of 72.916 billion |
| FCF yield | 2.33% | StockAnalysis MSFT statistics |
| Average analyst price target | 560.63 | StockAnalysis MSFT statistics; lower-priority market context, not a durable company fact |

## Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| Investor profile | Long-term investor ที่มองหา risk-adjusted compounding ไม่ใช่ short-term trading | action read จึงให้ความสำคัญกับ durable business quality และ valuation discipline |
| Existing position size | ถือว่าเป็น normal-sized core position เว้นแต่ระบุเป็นอย่างอื่น | ถ้า position oversized การ trim จะน่าสนใจขึ้น |
| Tax/friction | ยังไม่รู้ tax และ transaction costs | เมื่อไม่มี personal tax facts memo นี้จึงหลีกเลี่ยงการแนะนำ blanket trim |
| Required margin of safety | New money ควรต้องได้ราคาที่ใกล้ intrinsic value มากขึ้น หรือเห็น FCF conversion ชัดเจนขึ้นมาก | MSFT มีคุณภาพสูง แต่ current FCF yield ต่ำ ขณะที่ capex intensity กำลังสูงขึ้น |
| Valuation framework | DCF และ FCF yield สำคัญกว่า analyst targets | analyst targets อาจสะท้อน market sentiment และ forward EPS optimism; cash-flow conversion คือ key debate |
| AI economics | AI demand เป็นของจริง แต่ product-level AI margins และ OpenAI-specific economics ยังไม่ disclosed | upside case มีอยู่ แต่ยัง underwrite จาก official sources ได้ไม่เต็มที่ |

## Calculations

| Calculation | Result | Read |
|---|---:|---|
| FY26 Q3 revenue growth | 18.3% | top-line momentum ยังแข็งแรง |
| FY26 Q3 operating income growth | 20.0% | ยังเห็น operating leverage แม้ AI spend สูงขึ้น |
| FY26 Q3 net income growth | 23.1% | earnings growth ยังแข็งแรง |
| FY26 Q3 capex growth | 84.4% | capex โตเร็วกว่ารายได้และ operating income มาก |
| FY26 Q3 FCF growth | -22.1% | cash conversion คือสัญญาณลบหลัก |
| 9M FY26 capex growth | 68.8% | capital intensity ไม่ใช่ปัญหาแค่ไตรมาสเดียว |
| 9M FY26 FCF growth | 2.8% | operating cash flow growth ส่วนใหญ่ถูก capex ดูดซับ |
| DCF base fair value vs 421.92 close | 205.70, or -51.2% | DCF ใน vault บอกว่า base case ต่ำกว่าราคาตลาดมาก |
| DCF bull fair value vs 421.92 close | 309.10, or -26.7% | แม้ bull case ก็ยังต่ำกว่า latest close ภายใต้ mature-company terminal assumptions |
| Market-implied FCF yield | 2.33% | investor กำลังจ่ายเพื่อ runway ของ future FCF growth ที่ยาวมาก |
| Market EV / TTM FCF | 43.63x | multiple ค่อนข้าง demanding ในช่วงที่ AI capex ยังสูง |
| Reverse DCF from vault | About 25.1% 5-year FCF CAGR required | current price ต้องการ FCF path ที่แข็งแรงกว่า base case มาก |

## Judgment

### Why Not Add Now

- company quality ไม่ใช่ประเด็นลบหลัก. Official sources แสดง revenue, operating income, net income, Azure growth, Microsoft Cloud growth, AI ARR, RPO และ Copilot adoption ที่แข็งแรง
- stock price สะท้อน future FCF conversion ไปมากแล้ว. ที่ประมาณ 43x FCF และ 2.33% FCF yield ตลาดกำลัง underwrite ว่า AI monetization cycle จะสำเร็จ
- cash-flow signal อ่อนกว่า income statement signal. FY26 Q3 revenue โต 18.3% และ operating income โต 20.0% แต่ Q3 FCF ลดลง 22.1% เพราะ capex เพิ่มแรง
- DCF ใน vault มีช่องว่างกว้างระหว่าง intrinsic value กับ market price. Base fair value ประมาณ USD 205.70 และ bull fair value ประมาณ USD 309.10 เทียบกับ latest close ที่ USD 421.92

### Why Not Blanket Trim

- Microsoft ยังเป็นหนึ่งในธุรกิจคุณภาพสูงสุดใน vault: enterprise distribution แข็งแรง, operating margins สูง, growth engines กระจายตัว, balance sheet ลึก และมี reported AI demand
- forced trim อาจเร็วเกินไปถ้า AI capex convert เร็วกว่าที่ DCF assume โดยเฉพาะถ้า Azure capacity constraints คลี่คลาย และ Copilot/GitHub/Dynamics monetization scale ได้
- analyst context ยังเป็นบวก โดย StockAnalysis แสดง strong-buy consensus และ average target สูงกว่าราคาตลาด แม้นี่เป็น lower-priority context และไม่ใช่ตัวแทนของ source-backed valuation work

### What To Do

| Situation | Action | Rationale |
|---|---|---|
| No position / considering new capital | WAIT | ราคายังไม่ให้ cash-flow margin of safety เพียงพอวันนี้ |
| Existing normal-sized position | HOLD | business quality และ AI/cloud momentum ยังพอรองรับการถือ แต่ valuation ไม่สนับสนุนให้ add |
| Existing oversized position | TRIM selectively | ลด concentration risk ถ้า MSFT ใหญ่เกินไป หรือ portfolio มี AI infrastructure/platform exposure หนักอยู่แล้ว |
| Price falls near DCF bull value without thesis deterioration | Reassess for ADD | แถว low USD 300s valuation debate จะสมดุลขึ้น โดยยังต้องอัปเดต FCF และ capex data |
| FCF conversion improves materially while price stays flat | Reassess for ADD | หุ้นอาจน่าสนใจขึ้นได้จาก cash flow ที่ดีขึ้น ไม่จำเป็นต้องมาจากราคาที่ลดลงเท่านั้น |

## Decision Triggers

### Upgrade Toward Add

- FY26 Q4 / FY2026 full-year cash flow แสดงว่า operating cash flow growth absorb capex ได้ดีกว่าคาด
- Microsoft Cloud gross margin ทรงตัวหรือดีขึ้น แม้ AI infrastructure growth สูง
- Azure growth อยู่ใกล้หรือสูงกว่า management's high-30s constant-currency guide พร้อมกับ capacity constraints ที่คลี่คลาย
- Microsoft disclose AI monetization economics ที่แข็งแรงขึ้น เช่น Copilot, GitHub Copilot, Security Copilot, Dynamics agents หรือ Azure AI usage economics
- price ลดลงเข้าใกล้ DCF bull-case range โดยเฉพาะถ้า decline ไม่ได้มาพร้อม thesis damage

### Downgrade Toward Trim

- capex, finance leases, depreciation หรือ component pricing ยังเพิ่มต่อโดยไม่มี FCF recovery ที่ชัด
- Microsoft Cloud gross margin compress ต่อและต่ำกว่า guidance
- RPO quality อ่อนลง, recognition ช้าลง หรือ OpenAI-related concentration กลายเป็น unresolved risk ที่ใหญ่ขึ้น
- Azure growth decelerate แม้มี capacity investment หนัก
- position ใหญ่เกิน portfolio risk limits

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Product-level revenue and margins for Microsoft 365 Copilot, GitHub Copilot, Security Copilot, and other AI products | Not disclosed | ยัง underwrite AI unit economics โดยตรงไม่ได้ |
| OpenAI-specific Azure revenue, capacity allocation, margins, and contract economics | Not disclosed with enough granularity | concentration และ profitability risk ยัง quantify ได้ยาก |
| Full FY2026 annual results | ไม่พบข้อมูลที่ยืนยันได้ | FY2026 ยังไม่ครบปี ณ FY26 Q3 |
| Exact FY26 Q4 cash paid for property and equipment | Not yet reported | ต้องใช้ตรวจว่า capex ยัง suppress FCF ต่อหรือไม่ |
| Investor-specific tax basis, position size, and risk limits | Not provided | ทำให้ไม่สามารถให้ universal trim/hold recommendation ได้ |

## Bottom Line

MSFT เป็น **hold-quality business** แต่เป็น **wait-price stock** ณ วันนี้. สำหรับ new money decision คือ **WAIT**. สำหรับ existing normal-sized long-term position decision คือ **HOLD**. ควร trim เฉพาะเมื่อ portfolio sizing หรือ risk exposure ต้องการ ไม่ใช่เพราะ company fundamentals เพียงอย่างเดียว
