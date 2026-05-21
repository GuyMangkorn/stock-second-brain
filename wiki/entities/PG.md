---
type: entity
ticker: PG
company: The Procter & Gamble Company
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Q3 FY2026 and nine months ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q3 FY2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 21235
latest_net_income_usd_m: 3951
source_gap_count: 7
source_gaps:
  - Full FY2026 actual results are not disclosed.
  - Official company-hosted full earnings call transcript was not verified.
  - Product/category-level profitability below reportable segments is not disclosed.
  - Forward adjusted free cash flow dollar amount is not disclosed.
  - Exact realized FY2026 tariff / commodity impact after Q3 is not disclosed.
  - Market data after 2026-05-20 close was not verified.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/PG_latest_results_source.md
normalized_markdown: raw/financials/PG_fundamentals.md
normalized_json: raw/financials/PG_fundamentals.json
tags:
  - entity/company
  - ticker/PG
---

# PG - The Procter & Gamble Company

## Snapshot

| Item | Value |
|---|---|
| Ticker | PG |
| Company | The Procter & Gamble Company |
| Market | NYSE |
| Currency | USD |
| Latest period | Q3 FY2026, quarter ended 2026-03-31 |
| Reporting scope | Q3 FY2026 / 9M FY2026 plus FY2025 annual baseline |
| Normalized file | `raw/financials/PG_fundamentals.md` |
| Latest price check | USD 142.44 close on 2026-05-20; checked 2026-05-21 Asia/Bangkok |
| Current action read | WAIT / HOLD-existing-quality; avoid new capital without margin of safety |

P&G เป็น consumer staples quality compounder ที่มี brand portfolio ใหญ่, recurring daily-use demand และ capital return discipline สูง. Q3 FY2026 official sources แสดง reported sales +7%, organic sales +3%, YTD FCF โต และ balance sheet ยังรับได้ แต่ current valuation ใช้ FCF yield เพียง 4.53% และ base-case DCF ยังต่ำกว่าราคาตลาด จึงยังไม่ใช่ obvious bargain สำหรับ new money.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q3 FY2026 Form 10-Q for period ended 2026-03-31; FY2025 Annual Report / Form 10-K reviewed. |
| 1 | Official company results | Found | P&G Q3 FY2026 earnings release used for results, segments, guidance, and non-GAAP reconciliation. |
| 2 | Earnings transcript / call material | Partial | Secondary Motley Fool transcript found; official full transcript was not verified. |
| 3 | Financial statements / metrics | Found | Stooq used only for fresh market price; market cap calculated from official common shares. |
| 4 | News / web context | Not used for durable financial facts | Official sources were sufficient for core flow. |

## Business Model

P&G sells branded consumer packaged goods across daily-use categories through global retail, e-commerce, club, pharmacy, distributor, professional, and direct-to-consumer channels. The model depends on brand equity, innovation, retail execution, pricing, productivity, scale procurement, and recurring household consumption.

| Segment | Products / brands | Revenue driver | Source |
|---|---|---|---|
| Beauty | Hair Care, Skin and Personal Care; brands include Head & Shoulders, Pantene, Olay, SK-II | Innovation, brand strength, premiumization, geographic execution | P&G Q3 FY2026 Form 10-Q and FY2025 Annual Report. |
| Grooming | Braun, Gillette, Venus and related shaving / appliances products | Brand loyalty, replenishment, innovation-based pricing | P&G Q3 FY2026 Form 10-Q. |
| Health Care | Oral Care and Personal Health Care; Crest, Oral-B, Vicks, Pepto-Bismol, Metamucil | Daily-use oral care and OTC health demand | P&G Q3 FY2026 Form 10-Q. |
| Fabric & Home Care | Ariel, Downy, Gain, Tide, Cascade, Dawn, Febreze, Mr. Clean, Swiffer | Large global household categories, productivity, pricing, volume | P&G Q3 FY2026 Form 10-Q. |
| Baby, Feminine & Family Care | Pampers, Always, Tampax, Bounty, Charmin, Puffs | Household staples, demographic demand, retail execution | P&G Q3 FY2026 Form 10-Q. |

## Segments / Revenue Mix

| Segment | Q3 FY2026 Net Sales | Q3 FY2026 Mix | Reported YoY | Organic Sales Growth | Net Earnings | Source |
|---|---:|---:|---:|---:|---:|---|
| Beauty | USD 3.866B | 18.21% | 11% | 7% | USD 0.579B | P&G Q3 FY2026 earnings release / Form 10-Q. |
| Grooming | USD 1.608B | 7.57% | 7% | 1% | USD 0.331B | P&G Q3 FY2026 earnings release / Form 10-Q. |
| Health Care | USD 3.073B | 14.47% | 7% | 2% | USD 0.579B | P&G Q3 FY2026 earnings release / Form 10-Q. |
| Fabric & Home Care | USD 7.403B | 34.86% | 7% | 3% | USD 1.300B | P&G Q3 FY2026 earnings release / Form 10-Q. |
| Baby, Feminine & Family Care | USD 5.058B | 23.82% | 6% | 3% | USD 0.980B | P&G Q3 FY2026 earnings release / Form 10-Q. |
| Corporate | USD 0.225B | 1.06% | N/A | N/A | USD 0.181B | P&G Q3 FY2026 earnings release / Form 10-Q. |

Fabric & Home Care is the largest segment, while Baby/Feminine/Family and Beauty provide large secondary profit pools. Q3 FY2026 growth was broad, but margin pressure from mix, reinvestment, tariffs, and costs means sales growth did not fully drop through to operating profit.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q3 FY2026 net sales | USD 21.235B | P&G Q3 FY2026 Form 10-Q / earnings release. |
| Q3 FY2026 organic sales growth | 3% | P&G Q3 FY2026 earnings release. |
| Q3 FY2026 gross margin | 49.51% | Calculation: 10.513 / 21.235. |
| Q3 FY2026 operating margin | 21.55% | Calculation: 4.576 / 21.235. |
| Q3 FY2026 diluted EPS / core EPS | USD 1.63 / USD 1.59 | P&G Q3 FY2026 Form 10-Q / earnings release; core EPS is non-GAAP. |
| FY2026 YTD simple FCF | USD 11.039B | Operating cash flow 14.425B - capex 3.386B. |
| TTM simple FCF | USD 15.028B | FY2025 FCF - FY2025 YTD FCF + FY2026 YTD FCF. |
| Cash and equivalents | USD 12.306B | P&G Q3 FY2026 Form 10-Q. |
| Total debt | USD 37.026B | Debt due within one year + long-term debt. |
| FY2026 core EPS guidance | USD 6.83 to USD 7.09 | P&G Q3 FY2026 earnings release. |
| FY2026 cash return guidance | Around USD 10B dividends and approximately USD 5B buybacks | P&G Q3 FY2026 earnings release. |

## Charts

See `raw/financials/PG_fundamentals.md` for source-backed quarterly YoY, YTD, annual, segment mix, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Official release commentary shows a balanced picture: sales and organic growth remained positive, but margin pressure from mix, reinvestment, tariffs, commodities, and other items offset productivity and pricing. Management maintained FY2026 guidance ranges while saying EPS is now expected toward the lower end.

Secondary transcript context suggests management saw volume recovery, positive organic growth in key regions, and market-share stabilization. Because an official company-hosted full transcript was not verified, those transcript details remain lower-priority context rather than primary durable facts.

## Thesis

### Bull Case

P&G คือ high-quality defensive compounder: daily-use categories, global brands, pricing power, productivity muscle, and reliable cash returns. Q3 FY2026 had 7% reported sales growth, 3% organic sales growth, all major segments positive on reported sales, and YTD simple FCF up about 9.8% YoY. Balance sheet leverage is manageable at about 1.64x net debt / TTM FCF, and management still plans around USD 15B of dividends plus repurchases in FY2026.

ถ้า organic sales อยู่ใกล้ upper half ของ guidance, margin pressure eases, และ FCF conversion stays high, PG deserves a premium versus average consumer staples names.

### Bear Case

Current valuation already prices in a lot of quality. At USD 142.44, PG trades at about 23.7x EV / TTM simple FCF and only about 4.53% FCF yield. Base-case DCF is around USD 133 per diluted share, below the current price. Guidance also says EPS is likely toward the lower end because tariff, commodity, tax/interest, and reinvestment pressure remain meaningful.

สำหรับ new capital, quality alone is not enough if margin of safety is thin.

### Key Debate

คำถามหลักคือ market ควรจ่าย premium multiple แค่ไหนให้ P&G ในช่วงที่ organic growth เป็น low-single-digit และ margin ถูกกดดัน. Business quality is high, but the stock needs either a lower entry price, stronger organic growth/margin evidence, or a lower required return to justify adding aggressively.

## Risks

- Tariffs and commodity costs can keep gross margin under pressure.
- Reinvestment in innovation and demand creation may limit near-term operating leverage.
- Organic growth guidance is broad, from in-line to +4%, and actual EPS is expected toward the lower end.
- Premium valuation leaves less room for execution error.
- Brand/category-level profitability is not disclosed, limiting granular underwriting.
- FX and emerging-market volatility can affect reported sales and margins.
- Current market data uses latest available 2026-05-20 close; refresh before any future action change.

## Catalysts

- FY2026 Q4 / full-year results confirming stronger organic sales and margin stabilization.
- Evidence that tariff/commodity headwinds are offset by productivity and pricing.
- Higher adjusted free cash flow productivity and continued buyback execution.
- Segment-level organic acceleration, especially Beauty and Fabric & Home Care.
- Any updated FY2027 guidance that suggests re-acceleration or lower cost headwinds.
- Price pullback that creates a clearer FCF yield and DCF margin of safety.

## Valuation Watch Items

- Current DCF memo: [[PG DCF Valuation 2026-05-21]].
- Base-case fair value is about USD 133.34 per diluted share versus USD 142.44 latest close, implying roughly 6.4% downside.
- Bear case is about USD 85.00 and bull case about USD 179.70; wide range reflects WACC / terminal-growth sensitivity for a mature premium compounder.
- Current price does not provide an obvious margin of safety for new capital; existing holders can justify HOLD if they value PG's defensive quality and tax/portfolio context.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[PG_latest_results_source]] | Latest results source note |
| [[PG_fundamentals]] | Normalized financial facts |
| [[PG DCF Valuation 2026-05-21]] | DCF valuation |
| [[PG Decision Memo 2026-05-21]] | Decision memo |

## Follow-Up

- Refresh after FY2026 Q4 / full-year results with organic sales, gross margin, operating margin, FCF, cash, debt, shares, and FY2027 guidance.
- Verify whether tariff / commodity headwinds ease or persist into FY2027.
- Look for an official full transcript or management commentary pack if P&G publishes one.
- Track adjusted free cash flow productivity versus the 85%-90% guidance range.
- Refresh price before changing the WAIT / HOLD-existing-quality action read.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Full FY2026 actual results | not disclosed | Q3 FY2026 / nine-month data is latest official period found. |
| Official company-hosted full earnings call transcript | ไม่พบข้อมูลที่ยืนยันได้ | Secondary transcript context was found, but no official full transcript was verified. |
| Product/category-level profitability below reportable segments | not disclosed | Segment sales and earnings are disclosed; brand/category profitability is not. |
| Forward adjusted free cash flow dollar amount | not disclosed | P&G discloses productivity guidance, not a reconciled FY2026 FCF dollar amount. |
| Exact realized FY2026 tariff / commodity impact after Q3 | not disclosed | Final impact requires FY2026 actual results. |
| Market data after 2026-05-20 close | ไม่พบข้อมูลที่ยืนยันได้ | Latest available Stooq close at check time was 2026-05-20. |
| Investor-specific tax basis, position size, tax status, and required return | not provided | Needed for personalized sizing. |
