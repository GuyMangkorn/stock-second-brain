---
type: analysis
analysis_type: decision-memo
ticker: IBM
company: International Business Machines Corporation
date: 2026-06-18
currency: USD
decision: WAIT / HOLD-existing; price drop improves risk/reward but still lacks clear base-case margin of safety
source_files:
  - wiki/entities/IBM.md
  - raw/financials/IBM_fundamentals.md
  - raw/imports/IBM_latest_results_source.md
  - raw/imports/IBM_market_quote_2026-06-18.md
  - wiki/analysis/valuations/IBM DCF Valuation 2026-06-10.md
tags:
  - analysis/decision-memo
  - ticker/IBM
---

# IBM Decision Memo - 2026-06-18

## Action Read

**Action: WAIT / HOLD-existing. IBM ลงมาแรงจาก 52-week high แล้ว risk/reward ดีขึ้น แต่ยังไม่ใช่ obvious ADD เพราะราคาล่าสุด USD 262.35 ยังสูงกว่า base-case DCF fair value USD 240.27 ประมาณ 9.2%.**

ถ้ามี position อยู่แล้วขนาดปกติ ผมยังให้ถือรอดู Q2 2026 proof ได้ เพราะ Q1 2026 official sources ยัง support Software-led growth, FCF growth, guidance, และ dividend. แต่ถ้าเป็น new money ผมยังไม่อยากไล่ซื้อหลังราคายังอยู่เหนือ base value; โซนที่น่าสนใจขึ้นคือใกล้ base DCF หรือเมื่อ Q2 พิสูจน์ว่า Software / FCF / debt trajectory ดีกว่าที่ model base case ใส่ไว้.

สั้นๆ: price drop นี้เป็น **watchlist upgrade** มากกว่า buy signal ทันที.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest close used | USD 262.35 | MarketWatch, 2026-06-17 close; checked 2026-06-18 Asia/Bangkok. |
| One-day move | -3.12% | MarketWatch. |
| 52-week high | USD 332.46 on 2026-06-02 | MarketWatch. |
| Drawdown from 52-week high | -21.09% | MarketWatch / calculation. |
| Price move since 2026-06-10 memo | -5.45% | 262.35 / 277.49 - 1. |
| Price move since 2026-05-20 close | +16.66% | 262.35 / 224.88 - 1. |
| Shares outstanding | 939.885M | IBM Q1 2026 Form 10-Q cover page. |
| Market cap | USD 246.58B | 262.35 * 939.885M. |
| Cash + restricted cash + marketable securities | USD 11.828B | IBM Q1 2026 Form 10-Q. |
| Total debt | USD 66.4B | IBM Q1 2026 earnings release. |
| TTM IBM-defined FCF | USD 14.992B | FY2025 FCF 14.734B - Q1 2025 FCF 1.962B + Q1 2026 FCF 2.220B. |
| Market FCF yield | 6.08% | 14.992 / 246.58. |
| Market EV / TTM FCF | 20.09x | (246.58 + 66.40 - 11.828) / 14.992. |
| FY2026 guided FCF yield | about 6.38% | About USD 15.734B FCF / USD 246.58B market cap. |
| Annualized dividend yield | about 2.58% | USD 1.69 quarterly dividend * 4 / 262.35. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 revenue grew 9.46% reported | Growth is real, not only narrative. | `raw/financials/IBM_fundamentals.md` |
| Software revenue was USD 7.052B, 44.3% of Q1 revenue | IBM is increasingly Software-led. | `raw/financials/IBM_fundamentals.md` |
| Software constant-currency growth was 8%; FY2026 Software guide was 10%+ | Core thesis needs this durability to continue. | IBM Q1 2026 release / prepared remarks. |
| Consulting constant-currency growth was only 1% | Still the slowest major segment and a key execution question. | IBM prepared remarks / source note. |
| Q1 IBM-defined FCF grew 13.15% YoY | Cash conversion supports the bull case. | IBM Form 10-Q reconciliation. |
| FY2026 FCF guide implies about USD 15.7B | Current market cap gives about 6.4% guided FCF yield. | IBM Q1 release / prepared remarks and calculation. |
| Total debt is USD 66.4B | Leverage remains the main valuation brake. | IBM Q1 release. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 262.35 | Read |
|---|---:|---:|---|
| Bear | USD 152.63 | -41.8% | If growth fades and leverage remains a drag, downside is still large. |
| Base | USD 240.27 | -8.4% | Price is closer to fair value but not below base case. |
| Bull | USD 367.87 | +40.2% | Requires stronger sustained FCF growth, lower risk premium, and successful Software / AI execution. |

The pullback improves the setup because FCF yield has moved from 5.75% in the 2026-06-10 memo to about 6.08%. But the market is still paying roughly 20.1x EV / TTM FCF while official company facts have not changed since Q1 2026. That means the stock is cheaper than the spike, not necessarily cheap.

## Why The Stock Fell

มุมมองที่ source-backed ที่สุดคือราคาไม่ได้ลงเพราะ official IBM result ใหม่แย่ลง แต่เป็นการ unwind ของ early-June rally ที่ผสม AI / quantum / analyst enthusiasm และ speculative market-chatter. MarketWatch also showed the latest drop happened during a broad weak market day. ดังนั้นอย่าอ่าน price drop นี้เป็น fundamental deterioration โดยตรง และอย่าอ่านเป็น bargain โดยอัตโนมัติ.

The key distinction:

- **Fundamentals:** Q1 2026 remained solid: growth, FCF, guidance, Software mix.
- **Price:** Early-June valuation may have run ahead of proof after the stock reached a 52-week high.
- **Decision:** Better entry than USD 277.49, but still above base DCF.

## Bull Case

- IBM has shifted toward a Software-led hybrid-cloud and enterprise AI platform with Red Hat, OpenShift, Automation, Data, Transaction Processing, and watsonx.
- FY2026 FCF guidance of about USD 15.7B supports a mid-single-digit FCF yield and dividend coverage.
- IBM Z / z17 cycle and mission-critical workloads support near-term Infrastructure growth.
- Enterprise AI demand may favor IBM because regulated customers care about governance, data control, security, and hybrid deployment.
- Debt reduction after Confluent would lift equity value and could support a lower risk premium.

## Bear Case

- Latest price is still above base DCF fair value, so margin of safety remains thin for new capital.
- Total debt of USD 66.4B is material and Financing debt treatment requires judgment.
- Consulting growth remains slow; GenAI backlog must convert into revenue and FCF.
- Product-level AI / quantum revenue and margins are not disclosed, so market enthusiasm is hard to underwrite precisely.
- Infrastructure strength may be partly cyclical from z17 rather than recurring long-term growth.
- The early-June move had speculative / sentiment components, so volatility can remain high even if operating facts are stable.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | IBM-defined FCF | IBM adjusts for Financing receivables; simple GAAP OCF minus capex is less comparable. |
| Debt treatment | Total debt in base DCF | Conservative; excluding IBM Financing debt would raise value but requires judgment. |
| Current price | USD 262.35 | Latest regular-session close found for 2026-06-17. |
| Required margin of safety | Prefer price at or below base DCF for new money | Current price still fails that test. |
| Investor profile | Long-term investor, normal-sized position | Without position size and tax basis, memo avoids individualized sizing. |
| AI / quantum economics | Positive optionality but not directly modeled | Product-level revenue and margins are not disclosed. |

## What Would Change The Decision

- Upgrade toward ADD if price falls near or below the base DCF range without thesis deterioration.
- Upgrade toward ADD if Q2 2026 confirms FCF above trajectory, Software remains 10%+, Consulting accelerates, and total debt starts falling.
- Keep HOLD if IBM executes but price remains above base fair value; dividend and FCF quality can still justify holding a normal-sized position.
- Downgrade toward TRIM if position size is large and Q2 does not confirm the stronger expectations embedded in price.
- Downgrade if FCF guide is cut, debt rises further, Consulting stays weak, or AI / Software growth proves mostly acquisition-driven.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year FCF and debt trajectory. |
| Q2 2026 results | not disclosed | Current decision still relies on Q1 2026 official facts. |
| Product-level AI revenue and AI margins | not disclosed | Cannot directly underwrite AI unit economics. |
| Product-level quantum revenue and margins | not disclosed | Quantum remains optionality, not a modeled cash-flow base. |
| Segment-level FCF | not disclosed | Cannot prove which segment drives cash conversion. |
| Intraday 2026-06-18 real-time quote | not disclosed | Latest close used was 2026-06-17. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/IBM.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/IBM_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, cash, debt, FCF, shares, guidance. |
| Latest results source note | `raw/imports/IBM_latest_results_source.md` | Official-source map and extracted facts. |
| Market quote source note | `raw/imports/IBM_market_quote_2026-06-18.md` | Fresh price and current market calculations. |
| DCF valuation memo | `wiki/analysis/valuations/IBM DCF Valuation 2026-06-10.md` | Source-backed DCF scenarios and sensitivity. |
| IBM Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/51143/000005114326000038/ibm-20260331.htm | Primary filing source. |
| IBM Q1 2026 earnings release | https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS | Official results, guidance, debt/cash, dividend. |
| IBM 1Q26 prepared remarks | https://www.ibm.com/downloads/documents/us-en/15db805fff4249f1 | Official management commentary. |
| MarketWatch IBM daily market-data article | https://www.marketwatch.com/data-news/international-business-machines-corp-stock-outperforms-competitors-despite-losses-on-the-day-dfde7ca3-d1796dbb0803 | 2026-06-17 close, drawdown, volume, market comparison. |
| Investopedia IBM record-high / Barclays context | https://www.investopedia.com/ibm-stock-just-reached-a-new-record-high-why-barclays-says-it-is-following-the-nvidia-playbook-11987791 | Secondary price-action context. |
| Axios IBM meme-stock context | https://www.axios.com/2026/06/02/ibm-meme-stock-trump | Secondary market-chatter context. |

## Entity Update

Updated `wiki/entities/IBM.md` with the 2026-06-18 market quote and decision memo. Core action read remains `WAIT / HOLD-existing`, but watchlist priority improves because the price is much closer to base fair value than at the 2026-06-10 refresh.
