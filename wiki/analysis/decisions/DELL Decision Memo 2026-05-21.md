---
type: decision-memo
ticker: DELL
company: Dell Technologies Inc.
date: 2026-05-21
action_read: "WAIT / AVOID-new-capital"
price_checked: "2026-05-21"
tags:
  - analysis/decision
  - ticker/DELL
---

# DELL Decision Memo - 2026-05-21
Entity: [[DELL]]

## Action Read

**WAIT / AVOID-new-capital at current price.**

DELL มี AI infrastructure momentum ที่แรงมาก แต่ราคาปัจจุบัน already prices in a lot. Base-case DCF fair value is about USD 209/share versus USD 242.93 close, implying roughly 14% downside. Until FY2027 Q1 confirms cash conversion and margin protection, the source-backed decision is to wait rather than add new capital.

## Current Price / Market Data Check

| Metric | Value | Source / Timestamp |
|---|---:|---|
| Close price | USD 242.93 | StockAnalysis, at close 2026-05-20 4:00 PM EDT; checked 2026-05-21 |
| Pre-market price | USD 242.39 | StockAnalysis, 2026-05-21 6:52 AM EDT |
| Market cap | USD 157.80B | StockAnalysis provider value |
| Shares out | 649.57M | StockAnalysis provider value |
| FY2026 weighted-average diluted shares | 684M | FY2026 Form 10-K |
| PE ratio | 27.99x | StockAnalysis provider value |
| Forward PE | 18.73x | StockAnalysis provider value |
| Next earnings | 2026-05-28 | Dell IR upcoming events / StockAnalysis |

## Evidence From Vault

- `raw/imports/DELL_latest_results_source.md` created as P1 source note only.
- `raw/financials/DELL_fundamentals.md` normalizes FY2026 annual results, FY2027 guidance, FCF, cash, debt, shares, and market data.
- `wiki/entities/DELL.md` captures thesis, risks, catalysts, valuation watch items, and missing data.
- `wiki/analysis/valuations/DELL DCF Valuation 2026-05-21.md` provides DCF range and debt-treatment sensitivity.

Key source-backed facts:

| Fact | Value |
|---|---:|
| FY2026 revenue | USD 113.538B |
| FY2026 operating income | USD 8.149B |
| FY2026 net income attributable | USD 5.936B |
| FY2026 FCF | USD 8.555B |
| Cash and equivalents | USD 11.528B |
| Core debt principal | USD 17.018B |
| Total debt principal | USD 31.763B |
| FY2027 revenue guidance midpoint | USD 140.0B |
| FY2027 AI server revenue guidance | Roughly USD 50.0B |
| FY2027 GAAP diluted EPS guidance midpoint | USD 11.52 |
| FY2027 non-GAAP diluted EPS guidance midpoint | USD 12.90 |

## Valuation Read

Base-case DCF using FY2026 FCF, 10.0% WACC, 2.5% terminal growth, FY2026 weighted-average diluted shares, and core debt bridge gives fair value around **USD 209/share**. That is not enough margin of safety against the fresh checked close price.

The bull case can work if AI server growth converts into stronger FCF and attach revenue, but the current market price is already close to the 9.0% WACC / 2.5% terminal growth sensitivity case. นั่นแปลว่าหุ้นต้อง execute well, not merely execute okay.

## Bull Case

- FY2027 guidance implies a step-change year: revenue midpoint USD 140B and AI server revenue roughly USD 50B.
- Ending AI backlog of USD 43B gives visibility into near-term shipments.
- Dell's scale, supply chain, deployment capability, DFS financing, and service attach can help win large AI deployments.
- Pricing actions and shorter quote validity may protect margins in a component inflation cycle.
- Buybacks and dividend increases can support per-share compounding if FCF stays high.

## Bear Case

- AI server revenue may be lower-margin hardware revenue, so revenue growth may not equal FCF growth.
- FY2027 FCF guidance is not disclosed; the DCF depends on assumed conversion from FY2026 FCF.
- Component cost inflation and supply constraints can pressure gross margin and working capital.
- Customer concentration and product-level AI profitability are not disclosed.
- The stock is already at about 18.4x FY2026 FCF and around 28x trailing EPS on provider data.
- DFS financing debt complicates leverage and valuation interpretation.

## Key Assumptions

- FY2026 FCF is a valid base, not an exceptional one-off peak.
- FY2027 revenue/EPS guidance translates into at least moderate FCF growth.
- Core debt is the cleaner equity-bridge debt measure for operating DCF, with total debt shown as sensitivity.
- 10.0% WACC appropriately captures Information Technology sector risk, hardware cyclicality, leverage, and AI component-cost uncertainty.
- Terminal growth of 2.5% is reasonable for a mature developed-market infrastructure hardware company.

## What Would Change The Decision

- Upgrade toward WATCHLIST / ADD only if FY2027 Q1 confirms strong FCF conversion, stable/improving gross margin, and continued AI backlog/orders without excessive working-capital absorption.
- Upgrade if price falls below base-case fair value with no source-backed deterioration in FCF or guidance.
- Downgrade further if Q1 shows revenue growth without cash conversion, gross margin pressure, or inventory / receivables build tied to AI shipments.
- Re-run P11 if management gives FY2027 FCF guidance or more granular AI margin / attach economics.

## Missing / Unverified Data

- FY2027 Q1 actual results are not available as of 2026-05-21.
- FY2027 free cash flow guidance is not disclosed.
- Product-level and customer-level AI server profitability is not disclosed.
- Segment-level FCF is not disclosed.
- AI server order/backlog split by enterprise, neocloud, and sovereign customers is not disclosed.
- DFS debt valuation treatment requires explicit judgment.
- Investor-specific cost basis, position size, tax status, and required return were not provided.

## Source Map

| Source | URL / Path |
|---|---|
| DELL latest results source note | `raw/imports/DELL_latest_results_source.md` |
| DELL fundamentals | `raw/financials/DELL_fundamentals.md` |
| DELL entity page | `wiki/entities/DELL.md` |
| DELL DCF valuation | `wiki/analysis/valuations/DELL DCF Valuation 2026-05-21.md` |
| FY2026 Form 10-K | https://investors.delltechnologies.com/node/19326/html |
| FY2026 Q4 / full-year results release | https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3 |
| Q4 FY2026 transcript | https://investors.delltechnologies.com/static-files/9e5d4126-0f17-4ceb-b26c-a2563b8bcbc9 |
| StockAnalysis quote | https://stockanalysis.com/stocks/dell/ |
