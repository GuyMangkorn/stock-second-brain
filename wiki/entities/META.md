---
type: entity
ticker: META
company: Meta Platforms, Inc.
market: Nasdaq
currency: USD
period_type: quarterly + annual
reporting_scope: FY2025 annual baseline plus Q1 2026 quarter ended 2026-03-31
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 56311
latest_net_income_usd_m: 26773
source_gap_count: 7
source_gaps:
  - Product-level AI revenue, AI ad-tool revenue, Meta AI revenue, and AI infrastructure ROI are not disclosed.
  - Reality Labs product-level margins, unit volume, and AR glasses economics are not disclosed.
  - Segment-level free cash flow is not disclosed.
  - Full FY2026 actual results are not yet reported.
  - Exact remaining-quarter 2026 capex cadence is not disclosed.
  - FY2023 finance lease principal payments in the extracted table are not verified.
  - Investor-specific position size, tax basis, and required return were not provided.
source_notes:
  - raw/imports/META_latest_results_source.md
  - raw/imports/META_market_quote_2026-06-10.md
normalized_markdown: raw/financials/META_fundamentals.md
normalized_json: raw/financials/META_fundamentals.json
tags:
  - entity/company
  - ticker/META
---

# META - Meta Platforms, Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | META |
| Company | Meta Platforms, Inc. |
| Market | Nasdaq |
| Currency | USD |
| Latest verified period | Q1 2026, quarter ended 2026-03-31 |
| Annual baseline | FY2025, year ended 2025-12-31 |
| Latest quarterly revenue | USD 56,311 million |
| Latest quarterly net income | USD 26,773 million |
| Latest quarterly operating income | USD 22,872 million |
| TTM free cash flow | USD 45,637 million |
| Fresh price check | USD 577.61 on 2026-06-10 12:52 PM ET |
| Normalized file | [[META_fundamentals]] |
| Latest source note | [[META_latest_results_source]] |
| Market quote note | [[META_market_quote_2026-06-10]] |
| Latest valuation memo | [[META DCF Valuation 2026-06-10]] |
| Latest decision memo | [[META Decision Memo 2026-06-10]] |

Meta เป็น global social, messaging, advertising, AI, and immersive-computing platform. Core economics ยังมาจาก Family of Apps advertising เป็นหลัก ขณะที่ Reality Labs และ AI infrastructure เป็นตัวกำหนดว่า future growth จะคุ้มกับ capital intensity ที่สูงขึ้นหรือไม่.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm. FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm. |
| 2 | Earnings release / call materials | Found | Q1 2026 8-K Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1326801/000162828026028364/meta-03312026xexhibit991.htm. |
| 3 | Financial statements / metrics | Found | SEC companyfacts and official earnings release cover Q1 2026 statements, FCF, segment results, guidance, and annual baseline. |
| 4 | News / web context | Not needed | No secondary news was used for durable company facts. Market data from Nasdaq/Yahoo is stored separately as quote context. |

## Business Model

| Business line | Revenue mechanism | Durable driver | Primary official source |
|---|---|---|---|
| Family of Apps advertising | Ads across Facebook, Instagram, Messenger, WhatsApp, and other services | User engagement, ad impressions, ad price, targeting/measurement tools, AI ad optimization | SEC 8-K Exhibit 99.1; FY2025 Form 10-K. |
| Family of Apps other revenue | Payments, business messaging, and other services | Messaging commerce, creator/business tools, platform monetization | SEC 8-K Exhibit 99.1. |
| Reality Labs | Virtual and augmented reality hardware, software, and content | Hardware adoption, content ecosystem, AI/wearable adoption, long-term platform optionality | SEC 8-K Exhibit 99.1; FY2025 Form 10-K. |
| AI infrastructure and models | Mostly enabling capex/opex today rather than separately disclosed revenue | Ad performance, content recommendation, business agents, Meta AI, infrastructure scale | SEC 8-K Exhibit 99.1 guidance and risk language. |

### What Makes The Model Work

- Family of Apps is the profit engine: Q1 2026 FoA revenue was USD 55.909 billion and operating income was USD 26.900 billion.
- Advertising momentum remains strong: Q1 2026 ad impressions increased 19% YoY and average price per ad increased 12% YoY.
- Scale is unusual: Family daily active people averaged 3.56 billion in March 2026.
- Balance sheet remains flexible with USD 81.180 billion of cash, cash equivalents, and marketable securities versus USD 58.748 billion long-term debt.
- The key offset is capital intensity: FY2026 capex including finance lease principal is guided to USD 125-145 billion, up from prior USD 115-135 billion.

## Segments / Revenue Mix

### Q1 2026 Segment Mix

| Segment | Q1 2026 Revenue | Share of Q1 2026 Revenue | Q1 2026 Operating Income (Loss) | Source |
|---|---:|---:|---:|---|
| Family of Apps | 55,909 | 99.29% | 26,900 | SEC 8-K Exhibit 99.1. |
| Reality Labs | 402 | 0.71% | (4,028) | SEC 8-K Exhibit 99.1. |
| Total | 56,311 | 100.00% | 22,872 | SEC 8-K Exhibit 99.1. |

### Revenue Mix Read

Meta เป็น business ที่กำไรแทบทั้งหมดมาจาก FoA ads. Reality Labs revenue ยังเล็กมากและขาดทุนมากกว่า revenue หลายเท่า ดังนั้น investment debate ไม่ใช่แค่ revenue growth แต่เป็นคำถามว่า AI/data-center capex และ Reality Labs spend จะสร้าง FCF หลัง reinvestment ได้มากพอหรือไม่.

## Financial Facts

### Latest Quarterly Facts

| Metric | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Revenue | 56,311 | 42,314 | SEC 8-K Exhibit 99.1 and Form 10-Q. |
| Operating income | 22,872 | 17,555 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Operating margin | 40.62% | 41.49% | Calculated from official tables. |
| Net income | 26,773 | 16,644 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Diluted EPS | 10.44 | 6.43 | SEC 8-K Exhibit 99.1. |
| Net cash from operations | 32,226 | 24,026 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Purchases of property and equipment | (18,997) | (12,941) | SEC 8-K Exhibit 99.1 and companyfacts. |
| Principal payments on finance leases | (843) | (751) | SEC 8-K Exhibit 99.1 and companyfacts. |
| Free cash flow | 12,386 | 10,334 | SEC 8-K Exhibit 99.1 company non-GAAP reconciliation. |

### Balance Sheet Facts

| Metric | 2026-03-31 | Source |
|---|---:|---|
| Cash and cash equivalents | 23,426 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Marketable securities | 57,754 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Cash, cash equivalents, and marketable securities | 81,180 | SEC 8-K Exhibit 99.1. |
| Long-term debt | 58,748 | SEC 8-K Exhibit 99.1 and companyfacts. |
| Total liabilities | 151,569 | SEC 8-K Exhibit 99.1. |
| Total stockholders' equity | 243,681 | SEC 8-K Exhibit 99.1. |
| Class A + Class B shares outstanding | 2.538 billion | SEC Form 10-Q cover facts as of 2026-04-24; calculated. |

### Key Ratios

| Ratio | Period / date | Value | Formula |
|---|---|---:|---|
| Revenue growth | Q1 2026 YoY | 33.08% | 56,311 / 42,314 - 1 |
| Operating margin | Q1 2026 | 40.62% | 22,872 / 56,311 |
| Net profit margin | Q1 2026 | 47.55% | 26,773 / 56,311; includes tax benefit |
| FCF margin | Q1 2026 | 22.00% | 12,386 / 56,311 |
| Current ratio | 2026-03-31 | 2.35x | 109,765 / 46,753 |
| Liabilities / equity | 2026-03-31 | 0.62x | 151,569 / 243,681 |
| Family of Apps operating margin | Q1 2026 | 48.11% | 26,900 / 55,909 |

## Charts

Charts use only verified values from `raw/financials/META_fundamentals.md`.

### Quarterly YoY Comparison

```chart
type: bar
labels: ["Q1 2025", "Q1 2026"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [42314, 56311]
  - title: Operating Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [17555, 22872]
  - title: Free Cash Flow
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [10334, 12386]
```

### Segment Revenue

```chart
type: bar
labels: ["Family of Apps", "Reality Labs"]
series:
  - title: Q1 2026 Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [55909, 402]
  - title: Q1 2025 Revenue
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [41902, 412]
```

### Cash Flow And Capex

```chart
type: bar
labels: ["Q1 2025", "Q1 2026", "TTM Q1 2026"]
series:
  - title: Operating Cash Flow
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [24026, 32226, 124000]
  - title: Capex + Finance Lease Principal
    backgroundColor: rgba(244, 63, 94, 0.64)
    borderColor: rgba(251, 113, 133, 1)
    data: [13692, 19840, 78363]
  - title: Free Cash Flow
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [10334, 12386, 45637]
```

## Transcript / Management Commentary

| Topic | Commentary | Investment read |
|---|---|---|
| Q2 2026 revenue guidance | Meta expects Q2 2026 revenue of USD 58-61B. | Revenue momentum remains strong after Q1. |
| FY2026 expenses guidance | Total expenses expected at USD 162-169B. | Scale benefits are being reinvested into AI, infrastructure, and product bets. |
| FY2026 capex guidance | Capex including finance lease principal expected at USD 125-145B, increased from USD 115-135B. | The biggest valuation debate is whether this capex earns high returns. |
| Capex driver | Higher component pricing and additional data center costs. | Near-term FCF pressure may persist even with strong revenue growth. |
| Legal/regulatory matters | Meta flags EU/U.S. headwinds, youth-related scrutiny, and trials that may result in material loss. | Regulatory risk remains part of the bear case. |

## Thesis

### Bull Case

- FoA advertising is compounding quickly: Q1 2026 revenue increased 33% YoY.
- FoA operating income of USD 26.900B in Q1 2026 funds AI and Reality Labs investment.
- Ad impressions and average price per ad both grew double digits, which suggests AI/relevance improvements are helping monetization.
- Balance sheet still has net cash when cash and marketable securities are compared with long-term debt.
- If AI infrastructure lifts ad conversion, business messaging, agents, and recommendation quality, Meta can grow into heavy capex.

### Bear Case

- FY2026 capex guidance of USD 125-145B is far above FY2025 capex spend and compresses FCF.
- Reality Labs remains a large drag: Q1 2026 operating loss was USD 4.028B on only USD 402M revenue.
- Q1 2026 net income includes USD 8.03B tax benefit, so headline EPS overstates recurring after-tax earnings.
- AI product-level revenue and ROI are not disclosed, making it hard to underwrite payback directly.
- Legal and regulatory issues could create material losses or product restrictions.

### Key Debate

Can Meta convert a very large AI/data-center investment cycle into higher ad ROI, new product monetization, and durable FCF growth quickly enough to justify a premium multiple?

## Risks

- Capex and depreciation outpace revenue growth.
- Reality Labs losses remain structurally high without visible monetization.
- AI ad tools improve revenue but not enough to offset infrastructure cost.
- Platform/regulatory restrictions reduce ad targeting, messaging monetization, or user engagement.
- Youth safety, privacy, antitrust, and content moderation matters produce material costs or operating limits.
- Current valuation assumes a successful FCF recovery after the capex step-up.

## Catalysts

- Q2 2026 revenue prints above guidance or with improving operating leverage.
- Evidence that TTM FCF stabilizes despite high AI infrastructure spend.
- Management narrows capex guidance or provides stronger ROI commentary.
- Reality Labs losses narrow or hardware/wearables revenue inflects.
- Disclosure of AI ad-tool adoption, business messaging revenue, or Meta AI monetization.
- Regulatory outcomes become clearer and less costly than feared.

## Valuation Watch Items

- Fresh price check: USD 577.61 on 2026-06-10 12:52 PM ET.
- Base DCF fair value from `[[META DCF Valuation 2026-06-10]]`: about USD 529 per diluted share.
- Base-case upside/downside vs fresh price: about (8)%.
- TTM FCF yield on Nasdaq market cap: about 3.1%.
- Reverse DCF at 9.0% WACC / 2.5% terminal growth requires about 19.8% 5-year FCF CAGR from TTM Q1 2026 FCF.
- Watch whether FY2026 capex guidance moves again; this is the main variable in FCF conversion.

## Reports / Source Notes

- [[META_latest_results_source]]
- [[META_market_quote_2026-06-10]]
- [[META_fundamentals]]
- [[META DCF Valuation 2026-06-10]]
- [[META Decision Memo 2026-06-10]]

## Follow-Up

- Refresh after Q2 2026 results and compare actual revenue against USD 58-61B guidance.
- Track whether FY2026 capex guidance remains USD 125-145B or rises again.
- Look for official disclosure on AI ad tools, business messaging, Meta AI, and Reality Labs economics.
- Re-run valuation if TTM FCF moves materially above or below the base path.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Product-level AI revenue, AI ad-tool revenue, Meta AI revenue, and AI infrastructure ROI | Not disclosed | Cannot directly underwrite AI payback. |
| Reality Labs product-level margins and unit economics | Not disclosed | Cannot separate hardware scale from operating loss drag. |
| Segment-level free cash flow | Not disclosed | FoA cash generation and Reality Labs cash burn cannot be isolated. |
| Full FY2026 actual results | Not yet reported | Q1 2026 and TTM are the freshest verified cash-flow facts. |
| Exact remaining-quarter 2026 capex cadence | Not disclosed | Important for near-term FCF. |
| FY2023 company-method FCF | ไม่พบข้อมูลที่ยืนยันได้ | Missing FY2023 finance lease principal payment in extracted table. |
| Investor-specific tax basis and position size | Not provided | Existing-position action depends on sizing and tax context. |
