---
type: valuation
ticker: NVDA
company: NVIDIA Corporation
valuation_date: 2026-06-26
price_check: 2026-06-25 12:43 PM EDT
currency: USD
tags:
  - analysis/valuation
  - ticker/NVDA
---

# NVDA DCF Valuation - 2026-06-26
Entity: [[NVDA]]

## Bottom Line

Base-case DCF ให้ fair value ประมาณ USD 117.96 ต่อ share เทียบกับราคาเช็คสด USD 195.03. นี่ไม่ใช่การบอกว่า NVDA เป็นธุรกิจแย่; ตรงกันข้าม official results แข็งมาก. ประเด็นคือ current price ต้องการ growth runway และ margin durability ที่สูงกว่า conservative DCF assumptions ชุดนี้มาก.

Action implication สำหรับ P13: `WAIT / HOLD-existing-quality-position`, ไม่ใช่ add new capital แบบเต็มขนาด เว้นแต่ investor ตั้งใจรับ valuation risk ของ AI infrastructure leader ที่ตลาด price-in ไปมากแล้ว.

## Source Map

| Source | URL / Path | Used For |
|---|---|---|
| NVIDIA Q1 FY2027 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm | Latest filing period, debt, balance-sheet validation. |
| NVIDIA FY2026 Form 10-K | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm | Annual FCF history and revenue mix. |
| NVIDIA Q1 FY2027 press release | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx | Q1 FY2027 FCF, cash flow, balance sheet, guidance. |
| StockAnalysis NVDA quote | https://stockanalysis.com/stocks/nvda/ | Current price, market cap, shares outstanding. |
| Local normalized facts | `raw/financials/NVDA_fundamentals.md` | Normalized financial base. |

## Input Table

| Input | Value | Source / Calculation |
|---|---:|---|
| Current price | USD 195.03 | StockAnalysis, 2026-06-25 12:43 PM EDT |
| Market cap | USD 4.72T | StockAnalysis, 2026-06-25 12:43 PM EDT |
| Shares outstanding | 24.221B | StockAnalysis showed 24.22B; model uses 24.221B for calculation precision |
| FY2026 FCF | USD 96.575B | FY2026 OCF 102.718B - capex/intangible purchases 6.042B - principal payments 0.101B |
| Q1 FY2027 FCF | USD 48.554B | NVIDIA Q1 FY2027 reconciliation |
| Q1 FY2026 FCF | USD 26.135B | NVIDIA Q1 FY2027 reconciliation |
| TTM FCF | USD 118.994B | FY2026 FCF 96.575B - Q1 FY2026 FCF 26.135B + Q1 FY2027 FCF 48.554B |
| Cash + marketable debt securities | USD 50.335B | Cash 13.237B + marketable debt securities 37.098B |
| Total debt | USD 8.470B | Short-term debt 1.000B + long-term debt 7.470B |
| Marketable equity securities | USD 30.237B | Excluded from base net cash because fair value can fluctuate |
| Q2 FY2027 revenue guidance | USD 91.0B +/- 2% | NVIDIA Q1 FY2027 press release |

## Base Case Assumptions

| Assumption | Base Case | Rationale |
|---|---:|---|
| Starting FCF | USD 118.994B | Latest TTM calculated from official FCF reconciliation. |
| Year 1 FCF growth | 28% | Reflects Q2 guide strength but fades from extreme recent growth. |
| Year 2 FCF growth | 20% | Assumes AI factory buildout remains strong. |
| Year 3 FCF growth | 14% | Fade toward large-cap maturity. |
| Year 4 FCF growth | 10% | Continued platform growth but slower base effect. |
| Year 5 FCF growth | 6% | Approaches mature compounder stage. |
| WACC | 10.0% | Information Technology range 8%-12%, adjusted for AI cycle volatility and offset by net cash / market leadership. |
| Terminal growth | 2.5% | Mature developed-market compounder terminal range. |

## FCF Projection

| Year | FCF | Discounted FCF |
|---:|---:|---:|
| 1 | 152.312 | 138.466 |
| 2 | 182.775 | 151.054 |
| 3 | 208.363 | 156.546 |
| 4 | 229.200 | 156.546 |
| 5 | 242.952 | 150.854 |

Units: USD billions.

## Valuation Summary

| Item | Value |
|---|---:|
| PV of explicit FCF | USD 753.466B |
| PV of terminal value | USD 2,061.669B |
| Enterprise value | USD 2,815.134B |
| Add cash + marketable debt securities | USD 50.335B |
| Less total debt | USD 8.470B |
| Equity value | USD 2,856.999B |
| Shares outstanding | 24.221B |
| Base DCF fair value / share | USD 117.96 |
| Current price | USD 195.03 |
| Implied upside/downside | -39.5% |
| Terminal value share of EV | 73.2% |

## Sensitivity Matrix

Fair value per share, USD.

| Terminal Growth / WACC | 9.0% | 10.0% | 11.0% |
|---|---:|---:|---:|
| 2.0% | 128.71 | 112.25 | 99.46 |
| 2.5% | 136.52 | 117.96 | 103.78 |
| 3.0% | 145.63 | 124.48 | 108.64 |

## Sanity Checks

- Current TTM FCF yield using StockAnalysis market cap: `118.994 / 4,720 = 2.5%`.
- Current price implies a premium to this conservative DCF even after very strong FCF growth assumptions.
- Terminal value is 73.2% of EV in the base case, which is within but still meaningfully assumption-sensitive.
- Q1 FY2027 net income margin includes large other income from equity securities; DCF should anchor on FCF, not GAAP net income alone.
- If marketable equity securities are added to excess cash, fair value rises by about USD 1.25/share, not enough to change the decision.

## What Would Change The Valuation

- Q2 FY2027 results beat the USD 91.0B +/- 2% revenue guide while maintaining around 75% gross margin and high FCF conversion.
- Management gives clearer durable demand signals beyond near-term AI factory capex.
- Evidence that custom silicon / competition is not compressing pricing or attach rates.
- Updated full-year FCF run-rate supports materially higher starting FCF than USD 118.994B.
- Price falls enough to offer margin of safety against a conservative DCF, or reverse DCF assumptions become easier to underwrite.

## Missing / Unverified Data

- Full earnings call transcript / Q&A not ingested.
- No source-backed peer multiple set was created.
- Named customer demand and backlog are not disclosed.
- Current market quote is intraday and should be refreshed before trade execution.

## Entity Update

Updated `wiki/entities/NVDA.md` with valuation watch items and linked this memo.
