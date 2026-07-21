---
type: analysis
analysis_type: earnings-deep-dive
ticker: AAPL
company: Apple Inc.
date: 2026-06-11
currency: USD
latest_period: Q2 FY2026
latest_period_end: 2026-03-28
action_read: WAIT / AVOID new capital; HOLD only with sizing and tax discipline
source_files:
  - raw/imports/AAPL_latest_results_source.md
  - raw/imports/AAPL_market_quote_2026-06-11.md
  - raw/financials/AAPL_fundamentals.md
  - wiki/entities/AAPL.md
  - wiki/analysis/valuations/AAPL DCF Valuation 2026-06-11.md
  - wiki/analysis/valuations/AAPL Bullish Valuation Scenario 2026-06-11.md
  - wiki/analysis/decisions/AAPL Decision Memo 2026-06-11.md
html_artifact: wiki/analysis/earnings/AAPL Earnings Deep Dive 2026-06-11.html
tags:
  - analysis/earnings
  - ticker/AAPL
---

# AAPL Earnings Deep Dive - 2026-06-11
Entity: [[AAPL]]

## PM Bottom Line

**Action read: WAIT / AVOID new capital; HOLD only if existing position size, tax basis, and portfolio role justify it.**

Apple's latest verified earnings are **Q2 FY2026, quarter ended 2026-03-28**. The quarter changed the operating picture positively: revenue growth reaccelerated to **16.6% YoY**, iPhone grew **22% YoY**, Services grew **16% YoY**, operating income grew **21.3% YoY**, and 1H FY2026 FCF reached **USD 78.283B**. This is a high-quality print.

The stock read is different. At the latest checked market close of **USD 291.58 on 2026-06-10**, AAPL trades at about **USD 4.28T market cap**, **33.15x P/FCF**, and **32.67x EV/FCF**. The current price is already close to the vault's **Quality Bull** valuation scenario of about **USD 290/share** and far above the base DCF fair value of about **USD 153/share**. The market is effectively paying for sustained Services/iPhone strength, durable buybacks, and AI/device-cycle optionality before official AI monetization or forward FCF guidance is verified.

## What Changed

| Area | Latest evidence | Investor read | Source |
|---|---:|---|---|
| Revenue growth | Q2 FY2026 net sales USD 111.184B, +16.6% YoY | Growth reaccelerated and was broad enough to matter. | SEC Q2 FY2026 Form 10-Q; `[[AAPL_fundamentals]]` |
| iPhone | USD 56.994B, +22% YoY | Pro mix/product cycle is carrying the quarter; this is the biggest bull datapoint and biggest normalization risk. | SEC Q2 FY2026 Form 10-Q MD&A |
| Services | USD 30.976B, +16% YoY; Services gross margin 76.7% | Services remains the quality layer that can support premium valuation. | SEC Q2 FY2026 Form 10-Q |
| Geography | Greater China USD 20.497B, +28% YoY | China was a positive swing factor, not a drag, in this print. | SEC Q2 FY2026 Form 10-Q |
| Profitability | Gross margin 49.27%, operating margin 32.27% | Margin quality confirmed the revenue beat; this was not only top-line growth. | Calculated from SEC Q2 FY2026 Form 10-Q |
| Cash flow | 1H FY2026 FCF USD 78.283B vs USD 47.876B in 1H FY2025 | Cash flow supports earnings quality, but Q2 standalone OCF/capex was not extracted. | Calculated: OCF - capex in `[[AAPL_fundamentals]]` |
| Capital return | Q2 repurchases USD 11.0B; new USD 100B authorization after quarter-end; dividend raised to USD 0.27 | Buybacks can keep EPS/share compounding, but repurchases at high valuation need scrutiny. | SEC Q2 FY2026 Form 10-Q |
| Risk posture | Component-cost/supply pressure, tariffs, and gross-margin volatility remain explicit risks | The better quarter did not remove the key bear-case mechanisms. | SEC Q2 FY2026 Form 10-Q MD&A / Risk Factors |

## Quality Of Print

**EPS quality screen:** no material below-the-line boost was identified from the verified source set. The effective tax rate was higher YoY, so the EPS growth was not obviously flattered by a lower tax rate. Diluted EPS increased to **USD 2.01** from **USD 1.65**, supported by revenue growth, gross profit expansion, operating income growth, and a lower diluted share count.

The main quality caveat is period granularity: Apple disclosed 1H operating cash flow and capex in the extracted official table, but Q2 standalone OCF and capex were not verified in this pass. Use 1H and TTM FCF for valuation, not an invented Q2 FCF figure.

## What Is Priced In

| Market / valuation item | Latest read | Interpretation | Source |
|---|---:|---|---|
| Latest checked close | USD 291.58 on 2026-06-10 | Price is essentially at the prior Quality Bull DCF scenario. | StockAnalysis overview, checked 2026-06-11 Bangkok |
| Market cap | USD 4.28T | Mega-cap quality premium is fully visible. | StockAnalysis statistics |
| P/FCF | 33.15x | Requires strong FCF per-share compounding from a USD 129.174B TTM FCF base. | StockAnalysis statistics / `[[AAPL_fundamentals]]` |
| EV/FCF | 32.67x | Enterprise valuation already embeds durable margin and growth. | StockAnalysis statistics |
| FCF yield | 3.02% | Thin margin of safety unless growth and buybacks persist. | StockAnalysis statistics |
| Base DCF | About USD 153/share | Base case says the stock is expensive. | `[[AAPL DCF Valuation 2026-06-11]]` |
| Quality Bull DCF | About USD 290/share | Current price requires bullish but not impossible assumptions. | `[[AAPL Bullish Valuation Scenario 2026-06-11]]` |
| Aggressive Bull DCF | About USD 430/share | Upside exists only if FCF growth and terminal valuation stay very strong. | `[[AAPL Bullish Valuation Scenario 2026-06-11]]` |
| Reverse DCF | About 20.5% 5-year FCF CAGR at 9.0% WACC / 2.5% terminal growth | This is the key underwriting problem for new money. | `[[AAPL DCF Valuation 2026-06-11]]` |

**PM judgment:** ตลาดน่าจะ price in แล้วว่า Q2 strength ไม่ใช่ one-off, Services จะโต double digit, iPhone/AI device cycle จะช่วย upgrade demand, และ buybacks จะลด share count ต่อเนื่อง. สิ่งที่ยังไม่ price in ดีพอสำหรับ bear case คือ margin pressure จาก components/tariffs, China normalization, และความเสี่ยงว่า AI optionality อาจยังไม่แปลงเป็น disclosed revenue หรือ FCF.

## What Should An Investor Watch Next

| Watch item | Why it matters | Falsifier / next check |
|---|---|---|
| FY2026 Q3 results, estimated 2026-07-30 after market close | Hard next earnings catalyst. | If Q3 revenue/services/margin decelerate sharply, Q2 looks more cyclical. |
| iPhone durability and Pro mix | iPhone was 51.3% of Q2 revenue and the biggest growth driver. | Growth normalizes to low single digits without offsetting Services acceleration. |
| Services revenue and Services gross margin | This is the valuation-quality bridge. | Services growth falls below double digit or margin compresses materially. |
| Gross margin vs components/tariffs | Apple explicitly flagged component and tariff risks. | Gross margin fails to hold despite strong mix; pricing actions hurt demand. |
| Greater China | Q2 China was +28% YoY and helped the print. | China growth reverses or regulatory / competitive pressure rises. |
| FCF conversion | Valuation depends on FCF, not only EPS. | 2H FCF fails to confirm 1H strength or capex/intangible/infrastructure needs rise. |
| Buyback pace and average repurchase price | Buybacks support EPS but can destroy value if done too expensively. | Repurchases remain aggressive while FCF growth slows and valuation stays stretched. |
| AI / Apple Intelligence monetization | Current multiple likely includes some AI/device-cycle option value. | No official adoption, revenue, Services attach, or upgrade-cycle evidence by late FY2026. |
| Regulatory risk around Services | Services carries very high gross margin. | App Store/payment/advertising economics face adverse rule changes. |

## Thesis Change

The earnings print improves confidence in Apple's operating durability but does **not** improve the new-capital action read at current valuation. The company thesis is stronger after Q2 FY2026; the stock thesis remains valuation-constrained.

## Source Limitations

- Official SEC Form 10-Q was verified and is the primary source for financial facts.
- Official Apple newsroom / IR earnings release and official call transcript were not verified in this pass, so this memo does not use management call quotes or Q&A tone.
- Official forward revenue, EPS, gross margin, capex, FCF guidance, and AI-specific monetization were not disclosed in the verified source set.
- Market data is from StockAnalysis and is labeled as market data, not company-filed fact.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm | Latest official quarterly filing, financial statements, MD&A, risks, capital return. |
| StockAnalysis overview | https://stockanalysis.com/stocks/aapl/ | Latest checked close, market cap, shares, next estimated earnings date, analyst context. |
| StockAnalysis statistics | https://stockanalysis.com/stocks/aapl/statistics/ | Valuation ratios, P/FCF, EV/FCF, TTM FCF cross-check, data timestamp. |
| Latest source note | `raw/imports/AAPL_latest_results_source.md` | Local source extraction. |
| Market quote note | `raw/imports/AAPL_market_quote_2026-06-11.md` | Fresh market quote and valuation context. |
| Normalized facts | `raw/financials/AAPL_fundamentals.md` | Financial tables, ratios, charts, FCF calculations. |
| Entity page | `wiki/entities/AAPL.md` | Durable thesis, risks, catalysts, valuation watch items. |
| Base DCF | `wiki/analysis/valuations/AAPL DCF Valuation 2026-06-11.md` | Base/bear/bull fair value and reverse DCF. |
| Bullish scenario | `wiki/analysis/valuations/AAPL Bullish Valuation Scenario 2026-06-11.md` | Quality Bull and Aggressive Bull valuation cases. |
