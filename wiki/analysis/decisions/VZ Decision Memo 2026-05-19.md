---
type: analysis
analysis_type: decision-memo
ticker: VZ
company: Verizon Communications Inc.
date: 2026-05-19
currency: USD
decision: WAIT / WATCHLIST for new capital; HOLD income position only with leverage risk tolerance
source_files:
  - index.md
  - wiki/entities/VZ.md
  - raw/financials/VZ_fundamentals.md
  - raw/imports/VZ_latest_results_source.md
  - wiki/analysis/valuations/VZ DCF Valuation 2026-05-19.md
tags:
  - analysis/decision-memo
  - ticker/VZ
---

# VZ Decision Memo - 2026-05-19

## Action Read

**Action: WAIT / WATCHLIST for new capital. HOLD existing income-oriented position only if leverage risk and position size are acceptable.**

VZ มี dividend/FCF appeal ชัด: FY2026 FCF guidance อยู่ที่ USD 21.5B or more, market cap ประมาณ USD 195.74B, ทำให้ equity FCF yield ดูสูง. แต่เมื่อมองแบบ enterprise value และหัก total debt ตาม DCF discipline, base fair value อยู่ประมาณ USD 34.96 ต่อ diluted share เทียบกับ fresh close price USD 46.88.

ดังนั้น new capital ไม่ควรเร่ง add ที่ราคานี้. สำหรับคนถือเพื่อ income อยู่แล้ว การ hold อาจยังสมเหตุสมผลถ้า position size ไม่ใหญ่และยอมรับ debt/integration risk ได้. ถ้าต้องการ margin of safety จริง ควรรอราคาถอย, FCF actual ดีกว่า guide, หรือ debt paydown ชัดกว่าเดิม.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 46.88 close on 2026-05-18 | MarketBeat, checked 2026-05-19 Bangkok time. |
| Extended-hours quote | USD 46.79 as of 04:35 AM Eastern on 2026-05-19 | MarketBeat. |
| Market cap | USD 195.74B | MarketBeat key stats. |
| Common shares outstanding | 4,175,558,910 | SEC 10-Q, 2026-03-31. |
| Diluted weighted-average shares | 4.210B | SEC 10-Q, Q1 2026. |
| FY2026 guided FCF yield | 10.98% | USD 21.5B FCF guidance floor / USD 195.74B market cap. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | Q1 2026 | `raw/financials/VZ_fundamentals.md`. |
| Q1 2026 operating revenue | USD 34.440B | SEC 10-Q. |
| Q1 2026 revenue growth | 2.85% YoY | SEC 10-Q. |
| Q1 2026 operating income | USD 8.242B | SEC 10-Q. |
| Q1 2026 net income | USD 5.146B | SEC 10-Q. |
| Q1 2026 diluted EPS | USD 1.20 | SEC 10-Q. |
| Q1 2026 FCF | USD 3.783B | SEC 10-Q reconciliation. |
| Cash and cash equivalents | USD 8.366B | SEC 10-Q. |
| Total debt | USD 172.460B | SEC 10-Q balance sheet calculation. |
| Net debt | USD 164.094B | Calculation from SEC 10-Q. |
| FY2026 FCF guidance | USD 21.5B or more | Verizon Q1 2026 earnings release. |
| FY2026 adjusted EPS guidance | USD 4.95 to USD 4.99 | Verizon Q1 2026 earnings release. |
| FY2026 mobility and broadband service revenue guidance | 2.0% to 3.0%, approximately USD 93B | Verizon Q1 2026 earnings release. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 34.96 per diluted share | ต่ำกว่า current price ประมาณ 25% |
| DCF bull fair value | USD 47.29 per diluted share | ใกล้ current price แต่ margin of safety แทบไม่มี |
| FY2026 guided FCF yield on market cap | 10.98% | น่าสนใจเชิง income แต่ต้องระวัง leverage |
| Market EV / FY2026 guided FCF | 16.7x | valuation ดูแพงขึ้นเมื่อรวม net debt |
| Net debt / FY2026 guided FCF | 7.63x | balance sheet เป็น risk หลัก |

valuation บอกว่า VZ ไม่ใช่ stock ที่ไร้คุณค่า. แต่ upside จาก dividend/FCF ต้องชั่งกับ debt load, integration risk, และ growth ที่ไม่สูง. ราคาปัจจุบันยังไม่ชดเชยความเสี่ยงมากพอสำหรับ new capital ที่ต้องการ margin of safety.

## Bull Case

- FY2026 FCF guidance มากกว่า USD 21.5B ทำให้ equity FCF yield ดูสูงเมื่อเทียบ market cap.
- Dividend coverage จาก FCF ยังดูได้ ถ้าใช้ FY2025 dividends paid เทียบ FY2026 FCF guidance floor.
- Q1 2026 มี positive postpaid phone net additions ครั้งแรกใน Q1 ตั้งแต่ 2013.
- Churn ดีขึ้น และ management ระบุว่า March Consumer postpaid phone churn ต่ำกว่า 85 bps.
- Frontier เพิ่ม fiber footprint และ management ตั้งเป้า run-rate operating cost synergies มากกว่า USD 1B ภายใน 2028.
- ถ้า debt paydown เร็วและ FCF actual สูงกว่า guide, equity value อาจ rerate ได้.

## Bear Case

- Total debt Q1 2026 ประมาณ USD 172.5B และ net debt จาก total debt minus cash ประมาณ USD 164.1B.
- Interest expense เพิ่ม 18.9% YoY ใน Q1 2026.
- Telecom growth ต่ำและต้องใช้ capex recurring สูง.
- Frontier integration ทำให้ comparability ยากขึ้นและยังต้องพิสูจน์ synergy.
- Competition จาก wireless peers, cable MVNO, fiber, FWA และ broadband alternatives อาจกด pricing/promo intensity.
- DCF base case ต่ำกว่า market price ชัดเจนเมื่อ subtract total debt.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term investor ที่สนใจ income แต่ยังต้องการ margin of safety |
| Position status | Unknown; action จึงแยก new capital จาก existing income position |
| FCF anchor | FY2026 company guidance floor of USD 21.5B |
| Valuation framework | Communication Services DCF, 9.0% base WACC, 2.0% terminal growth |
| Balance sheet treatment | Use total debt minus cash, not only net unsecured debt, for conservative equity value |

## What Would Change The Decision

- Upgrade toward add ถ้า price ลดลงใกล้หรือต่ำกว่า base DCF fair value โดย FCF guide ยัง intact.
- Upgrade ถ้า debt paydown เร็วกว่าแผนและ WACC risk ลดลง.
- Upgrade ถ้า Q2/Q3 results ยืนยันว่า FCF conversion, churn, and net adds ดีขึ้นโดยไม่ต้องเพิ่ม promotion.
- Downgrade toward trim/avoid ถ้า FCF guide ถูกลด, debt remains elevated, or Frontier integration drags margins/capex.
- Downgrade ถ้า dividend coverage แคบลงจนต้องเลือกระหว่าง dividend กับ debt reduction.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Product-level profitability by wireless, FWA, fiber, IoT, security, and enterprise services | not disclosed | Limits valuation by growth engine. |
| Frontier standalone post-close financial contribution in Q1 2026 | not fully isolated | Limits clean pro forma trend analysis. |
| Exact normalized recurring FCF after Frontier integration and debt paydown | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses company FCF guidance floor rather than an invented run-rate. |
| Investor-specific tax basis, dividend income need, and position size | not provided | Makes a universal trim/hold sizing recommendation inappropriate. |
| Intrayear market price after regular market open on 2026-05-19 | ไม่พบข้อมูลที่ยืนยันได้ | Decision uses 2026-05-18 close plus 2026-05-19 extended-hours check. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/VZ_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/financials/VZ_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios. |
| `wiki/entities/VZ.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/VZ DCF Valuation 2026-05-19.md` | Local valuation memo | P11 DCF and valuation sensitivity. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/732712/000073271226000023/vz-20260331.htm | Official quarterly facts. |
| Verizon FY2025 Form 10-K | https://www.verizon.com/about/sites/default/files/2025-Annual-Report-on-Form-10k.pdf | FY2025 annual baseline and FCF. |
| Verizon Q1 2026 earnings release | https://www.verizon.com/about/news/feed/verizons-transformation-actions-deliver-growth-profitability-1q26-company-raises-adjusted-eps | FY2026 guidance and highlights. |
| Q1 2026 earnings transcript | https://www.verizon.com/about/file/77847/download?token=DCOVBtyf | Management commentary. |
| MarketBeat VZ stock page | https://www.marketbeat.com/stocks/NYSE/VZ/ | Fresh price and market-data check. |
