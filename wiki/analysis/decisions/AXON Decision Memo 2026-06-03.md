---
type: analysis
analysis_type: decision-memo
ticker: AXON
company: Axon Enterprise, Inc.
date: 2026-06-03
currency: USD
action_read: WAIT / WATCHLIST-new-capital
source_files:
  - wiki/entities/AXON.md
  - raw/financials/AXON_fundamentals.md
  - raw/imports/AXON_latest_results_source.md
  - wiki/analysis/valuations/AXON DCF Valuation 2026-06-03.md
tags:
  - analysis/decision
  - ticker/AXON
---

# AXON Decision Memo - 2026-06-03
Entity: [[AXON]]

## Action Read

**WAIT / WATCHLIST-new-capital** at the current price.

AXON เป็น quality compounder ที่มี public safety moat, hardware install base, expanding Software and Services, ARR growth, NRR, and a large contracted backlog. แต่ราคาหุ้นยังต้องการ FCF path ที่ aggressive มากเมื่อเทียบกับ official FY2026 FCF guidance ประมาณ USD 450M.

สำหรับ new capital ควรรอ either better price หรือ official evidence ว่า FCF conversion กำลังยกระดับเร็วกว่า model base case. Existing holders can keep it on a high-quality watchlist, but this memo does not support aggressive adding at USD 482.23.

## Current Price / Market Data Check

| Metric | Value | Source |
|---|---:|---|
| Current intraday price | USD 482.23 at 2026-06-03 10:51 AM EDT | StockAnalysis overview. |
| Market cap | USD 38.87B | StockAnalysis overview. |
| Provider shares outstanding | 80.60M | StockAnalysis overview. |
| Previous close | USD 490.12 | StockAnalysis overview. |
| Official cash + short-term investments + marketable securities | USD 736.973M | Q1 2026 Form 10-Q. |
| Official Senior Notes principal | USD 1.750B | Q1 2026 Form 10-Q. |
| FY2026 FCF guidance | approximately USD 450M | Q1 2026 results release / shareholder letter. |
| FY2026 revenue growth guidance | 30% to 32% | Q1 2026 results release / shareholder letter. |

Market-data caveat: price, market cap, EV, and provider shares are not company filing facts. They were freshly checked for P11/P13, but should be refreshed again before any trade.

## Evidence From Vault

- `raw/imports/AXON_latest_results_source.md` records P1 official source discovery from Q1 2026 10-Q, FY2025 10-K, official Q1 release / shareholder letter, company-hosted transcript, and StockAnalysis market-data checks.
- `raw/financials/AXON_fundamentals.md` normalizes Q1 2026 / Q1 2025 financials, FY2025/FY2024/FY2023 annual baseline, segment revenue, ARR, NRR, future contracted bookings, FCF, cash, debt, shares, and FY2026 guidance.
- `wiki/entities/AXON.md` records the business model, segments, thesis, risks, catalysts, valuation watch items, and missing data.
- `wiki/analysis/valuations/AXON DCF Valuation 2026-06-03.md` uses FY2026 FCF guidance as the source-backed scenario anchor.

## Valuation Read

Base-case DCF fair value is approximately **USD 136 per share**, versus USD 482.23 current intraday price. The aggressive scenario reaches about **USD 197 per share**, still materially below the current quote.

This does not mean AXON is a weak company. It means the current price embeds a very long and strong cash-flow runway. Reverse DCF says the current price needs a starting FCF anchor around USD 1.59B under the same base growth shape, roughly 3.5x management's FY2026 FCF guidance. That is possible only if AXON scales FCF quickly and durably, but current official sources do not yet verify that path.

## Bull Case

AXON has several high-quality traits: mission-critical products, public-sector trust, integrated hardware/software workflows, high NRR, ARR growth, and a large future contracted bookings base. Software and Services grew 34.9% YoY in Q1 2026, ARR grew 35% YoY to USD 1.493B, and NRR was 125%. AI products and counter-drone demand add optionality on top of the core TASER/camera/cloud platform.

If the company converts hardware deployments into more recurring software and AI workflows, AXON can compound revenue and FCF for longer than a normal industrial company.

## Bear Case

Valuation is the main bear case. Q1 2026 FCF was USD -54.642M, FY2025 simple FCF was USD 75.081M, and FY2026 FCF guidance is approximately USD 450M. At the freshly checked market price, EV / FY2026 FCF guidance is about 88.6x using official cash/debt inputs.

Net income also needs careful reading because Q1 includes strategic investment gains. Guidance is framed around Adjusted EBITDA rather than GAAP net income, and management does not provide a GAAP reconciliation because relevant items are hard to forecast. Stock-based compensation guidance of USD 590M to USD 620M is material.

## Key Assumptions

- FY2026 FCF guidance of approximately USD 450M is the best source-backed forward FCF anchor.
- Q1 2026 negative FCF is not annualized because management described full-year FCF as positive and Q1 as seasonally affected.
- 10.5% WACC is appropriate for a high-growth mixed hardware/software public safety platform with valuation, hardware margin, and regulatory risk.
- Terminal growth of 2.5% is appropriate after explicit high-growth fade.
- Provider shares outstanding of 80.60M are used for P11 per-share output, cross-checked against Q1 filing common shares outstanding of 80.572M.

## What Would Change The Decision

- Price falls enough to bring EV / FY2026 FCF guidance closer to a reasonable quality-growth entry range.
- Management raises FY2026 FCF guidance materially above USD 450M or reports Q2/Q3 FCF conversion well ahead of the annual plan.
- Software and Services mix expands with stable gross margin and clearer AI monetization.
- Product-level disclosure supports high-margin growth in AI and counter-drone rather than low-margin hardware expansion.
- Stock-based compensation and dilution trend lower without slowing innovation.

## Missing / Unverified Data

- FY2026 full-year actual results are not disclosed.
- FY2026 GAAP net income guidance and GAAP-to-Adjusted EBITDA reconciliation are not provided because management says the relevant items are not reasonably estimable.
- Product-level profitability for AI products, counter-drone, TASER, cameras, Fusus, Carbyne, Prepared, and other modules is not disclosed.
- Segment-level FCF is not disclosed.
- Normalized recurring FCF is uncertain because Q1 2026 FCF was negative while management still guides to approximately USD 450M full-year FCF.
- Exact timing, cancellation risk, and margin conversion for future contracted bookings are not fully disclosed.
- Provider market data is not an official company filing fact and may vary by timestamp.
- Investor-specific cost basis, position size, tax status, and required return were not provided.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Source note | `raw/imports/AXON_latest_results_source.md` | P1 source discovery and raw extraction. |
| Normalized financials | `raw/financials/AXON_fundamentals.md` | P4 normalized facts and ratios. |
| Entity page | `wiki/entities/AXON.md` | P6 thesis, risks, catalysts, and source gaps. |
| DCF memo | `wiki/analysis/valuations/AXON DCF Valuation 2026-06-03.md` | P11 valuation. |
| Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1069183/000162828026031542/axon-20260331.htm | Official quarterly filing facts. |
| FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1069183/000162828026011360/axon-20251231.htm | Official annual baseline. |
| Q1 2026 results release / shareholder letter | https://www.sec.gov/Archives/edgar/data/1069183/000162828026031285/axon-20260506xex991.htm | Latest official results and FY2026 guidance. |
| Q1 2026 transcript PDF | https://investor.axon.com/image/Axon_Q1_2026_Earnings_Call_Transcript.pdf | Management commentary and Q&A. |
| StockAnalysis overview / statistics | https://stockanalysis.com/stocks/axon/ and https://stockanalysis.com/stocks/axon/statistics/ | Fresh market data checked 2026-06-03. |
