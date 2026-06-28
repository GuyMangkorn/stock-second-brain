---
type: entity
ticker: UL
company: Unilever PLC
market: NYSE ADR
currency: EUR
period_type: quarterly trading update + annual
reporting_scope: Q1 2026 trading update and FY2025 annual baseline, continuing operations after Ice Cream demerger
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: null
latest_net_income_usd_m: null
source_gap_count: 6
source_gaps:
  - Q1 2026 full income statement, balance sheet and cash flow were not disclosed in the captured source.
  - Official Q1 2026 transcript / Q&A was not verified.
  - Legal ADR-to-ordinary share ratio source was not independently verified.
  - Capex-only annual line was not extracted; use company-reported FCF instead of inferred capex.
  - Latest balance sheet after 2025-12-31 was not disclosed in the captured source.
  - Product-level profitability below business groups is not disclosed.
source_notes:
  - raw/imports/UL_latest_results_source.md
normalized_markdown: raw/financials/UL_fundamentals.md
normalized_json: raw/financials/UL_fundamentals.json
tags:
  - entity/company
  - ticker/UL
---

# UL - Unilever PLC

## Snapshot

| Item | Value |
|---|---|
| Ticker | UL |
| Company | Unilever PLC |
| Market | NYSE ADR |
| Currency | EUR company financials; USD ADR market data |
| Latest period | Q1 2026 trading update |
| Reporting scope | Q1 2026 trading update plus FY2025 continuing-operations annual baseline |
| Normalized file | `raw/financials/UL_fundamentals.md` |
| Latest price check | USD 60.55 close on 2026-06-26; checked 2026-06-28 Asia/Bangkok |
| Current action read | WATCHLIST / WAIT for better margin of safety |

Unilever เป็น global consumer staples company ที่ขาย Beauty & Wellbeing, Personal Care, Home Care และ Foods ผ่าน brand portfolio ขนาดใหญ่ทั่วโลก. Q1 2026 official update แสดง growth ที่ดีขึ้นแบบ volume-led: USG 3.8%, UVG 2.9%, Power Brands USG 5.0% และ management ยังยืนยัน FY2026 guidance. แต่ valuation ณ USD 60.55 ยังไม่เหลือ margin of safety มากพอใน base-case DCF และ net debt/FCF สูงกว่าที่อยากเห็นสำหรับการ add แบบสบายใจ.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Unilever Annual Report and Accounts 2025 / Form 20-F used for annual baseline, FCF, balance sheet, shares, segment data and capital allocation targets. |
| 2 | Official results / trading update | Found | Unilever Q1 2026 Overview used for latest USG/UVG, turnover, guidance, buyback and management commentary. |
| 2 | Earnings transcript / call material | Not verified | Official Q1 2026 transcript / Q&A was not found in captured sources. |
| 3 | Financial statements / metrics | Partial | StockAnalysis used for fresh ADR price/market cap; XE used for FX. |
| 4 | News / web context | Not used for durable financial facts | Official sources were sufficient for the core flow. |

## Business Model

Unilever monetizes everyday consumer demand through scaled brands, retail distribution, innovation, premiumisation, marketing, emerging-market reach and productivity programs. After Ice Cream demerger, the durable underwriting frame is a sharper, category-led consumer staples portfolio with four continuing business groups.

| Business Group | Role | FY2025 Turnover | Underwriting Read | Source |
|---|---|---:|---|---|
| Beauty & Wellbeing | Beauty, health and wellbeing categories | EUR 12.8B | Higher-growth premiumisation and Power Brands exposure. | Annual Report 2025 |
| Personal Care | Deodorants, skin cleansing, oral/personal care | EUR 13.2B | Largest group by turnover with high UOM. | Annual Report 2025 |
| Home Care | Fabric, home and hygiene products | EUR 11.6B | Lower margin than other groups, but daily-use demand and emerging-market scale. | Annual Report 2025 |
| Foods | Condiments, cooking aids and food brands | EUR 12.9B | Strong margin group, but captured sources note ongoing portfolio changes. | Annual Report 2025 / Q1 2026 Overview |

## Segments / Revenue Mix

| Business Group | FY2025 Turnover | FY2025 Revenue Mix | FY2025 USG | FY2025 Operating Margin | FY2025 UOM | Source |
|---|---:|---:|---:|---:|---:|---|
| Beauty & Wellbeing | EUR 12.8B | 25.35% | 4.3% | 16.2% | 19.2% | Annual Report 2025. |
| Personal Care | EUR 13.2B | 26.14% | 4.7% | 20.5% | 22.6% | Annual Report 2025. |
| Home Care | EUR 11.6B | 22.97% | 2.6% | 13.1% | 14.9% | Annual Report 2025. |
| Foods | EUR 12.9B | 25.54% | 2.5% | 21.3% | 22.6% | Annual Report 2025. |

Portfolio quality is not uniform. Personal Care and Foods carry stronger FY2025 UOM, Beauty & Wellbeing has more premiumisation/growth appeal, and Home Care is more margin-sensitive. Q1 2026 improvement being volume-led matters because it is healthier than pure price-led growth.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q1 2026 turnover | EUR 12.6B | Unilever Q1 2026 Overview. |
| Q1 2026 USG / UVG | 3.8% / 2.9% | Unilever Q1 2026 Overview. |
| Q1 2026 Power Brands USG / UVG | 5.0% / 4.0% | Unilever Q1 2026 Overview. |
| FY2025 turnover | EUR 50.5B | Annual Report 2025 continuing operations summary. |
| FY2025 underlying operating margin | 20.0% | Annual Report 2025. |
| FY2025 FCF | EUR 5.921B | Annual Report 2025. |
| Cash and equivalents | EUR 3.941B | Annual Report 2025. |
| Total financial liabilities | EUR 28.278B | Annual Report 2025. |
| Net debt | EUR 23.076B | Annual Report 2025. |
| Diluted average shares | 2,195.3M | Annual Report 2025. |
| FY2026 guidance | USG bottom end of 4%-6%; volume growth at least 2%; modest margin improvement | Unilever Q1 2026 Overview FAQ. |

## Charts

See `raw/financials/UL_fundamentals.md` for source-backed annual trend, business group mix and balance-sheet chart blocks. No Q1 income-statement/cash-flow chart was created because the captured Q1 source is a trading update, not a full financial statement.

## Transcript / Management Commentary

Q1 2026 CEO commentary frames the quarter as volume-led growth with Power Brands, emerging markets, India and Latin America as positive contributors. Management also highlighted confidence in FY2026 guidance and announced a EUR 1.5B buyback expected to complete by 2026-07-06.

Annual Report 2025 strategy highlights focus on the Growth Action Plan, `Desire at Scale`, stronger category focus, premiumisation, AI/digital productivity, cash conversion and disciplined capital allocation.

Official Q1 2026 transcript / Q&A was not verified, so the entity page does not treat Q&A detail as durable fact.

## Thesis

### Bull Case

Unilever is a credible defensive compounder if management can turn the post-Ice-Cream portfolio into steadier mid-single-digit USG, positive volume, and modest margin expansion. Q1 2026 is encouraging because growth was volume-led, Power Brands grew faster than the company, emerging markets remained strong, and FY2026 guidance stayed intact. FY2025 UOM at 20.0%, company-reported FCF of EUR 5.921B, and about 100% cash-conversion ambition support the quality case.

### Bear Case

The setup is not an obvious bargain. FY2025 FCF declined versus FY2024, total financial liabilities / FY2025 FCF is about 4.78x, and base-case DCF gives fair value below the USD 60.55 ADR price. Q1 2026 captured source does not include full statements, so cash/debt/FCF inputs remain anchored to FY2025 until the next full filing. The business also has portfolio-change complexity after Ice Cream demerger and Foods transaction context in Q1 materials.

### Key Debate

คำถามหลักคือ market ควรจ่าย premium multiple ให้ UL แค่ไหนเมื่อ growth quality ดีขึ้น แต่ leverage/FCF and portfolio-transition risk ยังต้องพิสูจน์ต่อ. ถ้า management ทำให้ volume-led growth ต่อเนื่องและ margin ค่อย ๆ ขยายได้ valuation อาจรับได้; ถ้า FCF ยังอ่อนหรือ growth กลับไปช้า stock มี downside จาก multiple compression.

## Risks

- Q1 2026 source is a trading update; no full quarterly cash flow or balance sheet was captured.
- Net debt and financial liabilities are meaningful relative to FY2025 FCF.
- Portfolio transition after Ice Cream demerger can reduce historical comparability.
- Foods transaction references in Q1 source need deeper pro forma analysis before treating future mix as stable.
- Emerging-market exposure can create FX, pricing, volume and political risk.
- Premium valuation depends on sustained volume growth and margin improvement.
- Legal ADR ratio was not independently sourced; valuation uses market shares and official ordinary shares as a practical cross-check.

## Catalysts

- Next full filing confirming Q1/H1 2026 cash flow, cash, debt and share count.
- Evidence that FY2026 USG lands above the bottom of guidance, with volume growth at least 2%.
- Continued Power Brands outperformance and emerging-market volume momentum.
- Modest UOM improvement in 2026 without sacrificing volume.
- Buyback completion and disciplined capital allocation after portfolio changes.
- Price pullback that lifts FCF yield and creates clearer margin of safety.

## Valuation Watch Items

- Current DCF memo: [[UL DCF Valuation 2026-06-28]].
- Base-case fair value is about USD 53.28 per ADR versus USD 60.55 close, implying roughly 12.0% downside.
- Bear case is about USD 30.13 and bull case about USD 73.28; wide range reflects WACC and terminal-growth sensitivity.
- Market FCF yield is about 5.13% using FY2025 FCF converted to USD and StockAnalysis market cap.
- Decision read is `WATCHLIST / WAIT`, not `ADD`, because base valuation is below market and source gaps remain around Q1 full statements and ADR mechanics.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[UL_latest_results_source]] | Latest results source note |
| [[UL_fundamentals]] | Normalized financial facts |
| [[UL DCF Valuation 2026-06-28]] | DCF valuation |
| [[UL Decision Memo 2026-06-28]] | Decision memo |

## Follow-Up

- Refresh after the next full filing with Q1/H1 2026 cash flow, balance sheet, cash, debt, shares and FCF.
- Verify legal ADR-to-ordinary share ratio from depositary or company source.
- Track whether FY2026 USG stays at least at the bottom of 4%-6% and whether volume remains at least 2%.
- Watch UOM improvement versus FY2025's 20.0%.
- Re-run valuation if price falls materially, FY2026 FCF improves, or pro forma portfolio mix changes after Foods transaction detail becomes clearer.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Q1 2026 full income statement, balance sheet and cash flow | not disclosed in captured source | P11 uses FY2025 financial statement inputs until next full filing. |
| Official Q1 2026 transcript / Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Only official overview and CEO commentary captured. |
| Legal ADR-to-ordinary share ratio source | ไม่พบข้อมูลที่ยืนยันได้ | StockAnalysis shares out and official ordinary shares are close, but ratio itself was not independently sourced. |
| Capex-only annual line | ไม่พบข้อมูลที่ยืนยันได้ in extracted table | Company-reported FCF is used; no inferred capex chart. |
| Latest balance sheet after 2025-12-31 | not disclosed in captured source | Refresh with next filing before action changes. |
| Product-level profitability below business groups | not disclosed | Business group margins are available, but brand economics are not. |
