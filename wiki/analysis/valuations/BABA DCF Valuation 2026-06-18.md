---
type: analysis
analysis_type: dcf-valuation
ticker: BABA
company: Alibaba Group Holding Limited
date: 2026-06-18
currency: USD
fair_value_base_per_ads: 88
fair_value_range_per_ads: 75-110
source_files:
  - wiki/entities/BABA.md
  - raw/financials/BABA_fundamentals.md
  - raw/imports/BABA_latest_results_source.md
  - wiki/analysis/decisions/BABA Decision Memo 2026-06-11.md
tags:
  - analysis/valuation
  - ticker/BABA
---

# BABA DCF Valuation - 2026-06-18

## Bottom Line

**Base-case fair value: about USD 88 per ADS. Practical fair value range: USD 75-110 per ADS. Bull recovery case: about USD 129 per ADS.**

ราคาล่าสุดที่ verify ได้คือ **USD 107.44 close on 2026-06-17**, หรือ **44.24% below 52-week high**. จาก scenario DCF นี้ BABA ไม่ได้แพงแบบ obvious แต่ก็ไม่ใช่ obvious bargain แล้วถ้าใช้ conservative FCF recovery path. ที่ USD 107.44 หุ้นอยู่ใกล้ปลายบนของ base range และต้องการหลักฐานเพิ่มว่า FY2026 เป็น trough FCF year จริง.

ผมจะตีความ valuation แบบนี้:

| Zone | Price / ADS | Read |
|---|---:|---|
| Attractive starter | Below USD 85 | Margin of safety เริ่มน่าสนใจถ้ายังเชื่อว่า Cloud/AI และ China commerce profit จะฟื้น. |
| Fair / watch closely | USD 85-110 | ต้องใช้ staged entry และรอ FCF evidence; current price อยู่ใน zone นี้. |
| Recovery priced | Above USD 110 | ต้องการ bull case ที่ชัดขึ้น เช่น Cloud margin expansion และ quick-commerce losses peak. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Alibaba FY2026 official results release | https://data.alibabagroup.com/ecms-files/1532295521/5b1cb883-8d00-4237-a148-6631cc12a5d2/Alibaba%20Group%20Announces%20March%20Quarter%202026%20and%20Fiscal%20Year%202026%20Results.pdf | Revenue, FCF, capex, adjusted EBITA, cash, debt, ADS ratio, diluted EPS. |
| Alibaba IR quarterly results page | https://www.alibabagroup.com/en-US/ir-financial-reports-quarterly-results | Official source discovery for March quarter 2026 and FY2026 results. |
| MarketWatch BABA market-data article | https://www.marketwatch.com/data-news/alibaba-group-holding-ltd-adr-outperforms-competitors-despite-losses-on-the-day-a58e2c90-e4a7aa3930d7 | Latest verified close and drawdown context. |
| `raw/financials/BABA_fundamentals.md` | Local normalized facts | Verified financial facts and prior market valuation context. |
| `wiki/entities/BABA.md` | Local entity page | Thesis, risks, catalysts, source gaps. |

## Input Table

| Input | Value | Source / calculation |
|---|---:|---|
| Current price | USD 107.44 on 2026-06-17 close | MarketWatch article checked 2026-06-18. |
| 52-week high drawdown | 44.24% below USD 192.67 | MarketWatch article. |
| FY2026 revenue | RMB 1,023.670B / USD 148.401B | Official results release. |
| FY2026 operating cash flow | RMB 76.213B / USD 11.049B | Official results release. |
| FY2026 free cash flow | RMB (46.609B) / USD (6.757B) | Official results release. |
| FY2025 free cash flow | RMB 73.870B | Official results release. |
| FY2026 capex | RMB 126.063B | Official results release. |
| FY2026 adjusted EBITA | RMB 76.416B / USD 11.078B | Official results release. |
| Cash and other liquid investments | RMB 520.824B / USD 75.504B | Official results release. |
| Interest-bearing debt | RMB 259.996B / USD 37.692B | Sum of current bank borrowings, non-current bank borrowings, senior notes, convertible notes, and exchangeable bonds from official results release. |
| Net liquid investments less debt | USD 37.812B | USD 75.504B - USD 37.692B. |
| Diluted ADS equivalent | 2.407B ADS | RMB 105.904B net income attributable to ordinary shareholders / RMB 44.00 diluted EPS per ADS. |
| Current market cap | USD 258.598B | USD 107.44 * 2.407B ADS. |
| Current enterprise value | USD 220.786B | Market cap - net liquid investments less debt. |
| Current P / FY2026 non-GAAP net income | 29.4x | USD 258.598B / USD 8.794B. |
| Current EV / FY2026 adjusted EBITA | 19.9x | USD 220.786B / USD 11.078B. |
| Current EV / FY2026 revenue | 1.5x | USD 220.786B / USD 148.401B. |

## Base Case Assumptions

This is a scenario DCF, not a company-disclosed value. FY2026 FCF was negative, so the model is anchored on a recovery path rather than on trailing FCF.

| Assumption | Base case | Rationale |
|---|---:|---|
| WACC | 10.5% | Information Technology / Consumer Discretionary platform, plus China / ADR / regulatory risk and volatile FCF, partly offset by net liquid balance sheet and market leadership. |
| Terminal growth | 2.5% | Mature platform terminal range after explicit recovery period. |
| Year 1 FCF | RMB 20B | Assumes FY2026 was trough but investment intensity remains high. |
| Year 5 FCF | RMB 120B | Below FY2025 OCF and above FY2025 FCF, requiring quick-commerce losses to narrow and Cloud scale to contribute cash. |
| Net cash adjustment | USD 37.812B | Uses company-defined liquid investments less interest-bearing debt. |
| Share count | 2.407B ADS equivalent | Derived from official FY2026 diluted EPS per ADS. |

## FCF Projection

| Year | FCF assumption | USD equivalent | Notes |
|---|---:|---:|---|
| Year 1 | RMB 20B | USD 2.9B | Partial recovery from FY2026 outflow. |
| Year 2 | RMB 55B | USD 8.0B | Quick-commerce / AI app investment drag begins to narrow. |
| Year 3 | RMB 85B | USD 12.3B | Cloud scale and China commerce profit stabilization start to matter. |
| Year 4 | RMB 105B | USD 15.2B | Better operating leverage, still below aggressive recovery. |
| Year 5 | RMB 120B | USD 17.4B | Normalized recovery case, not a confirmed run-rate. |

## Valuation Summary

| Scenario | FCF path logic | WACC | Terminal growth | Fair value / ADS | Read |
|---|---|---:|---:|---:|---|
| Bear | FCF recovery is slow; Year 5 FCF only RMB 70B | 10.5% | 2.5% | USD 54 | Price still too high if cash conversion does not return. |
| Low base | Year 5 FCF reaches RMB 100B | 10.5% | 2.5% | USD 74 | Downside case inside a modest recovery. |
| Base | Year 5 FCF reaches RMB 120B | 10.5% | 2.5% | USD 88 | My central fair value. |
| High base | Year 5 FCF reaches RMB 150B | 10.5% | 2.5% | USD 106 | Roughly where the current market price sits. |
| Bull | Year 5 FCF reaches RMB 185B | 10.5% | 2.5% | USD 129 | Requires strong Cloud/AI monetization plus China commerce margin recovery. |

## Sensitivity Matrix

Base FCF path: RMB 20B, RMB 55B, RMB 85B, RMB 105B, RMB 120B.

| WACC / terminal growth | 2.0% | 2.5% | 3.0% |
|---|---:|---:|---:|
| 9.5% | USD 94.9 | USD 99.7 | USD 105.2 |
| 10.5% | USD 84.6 | USD 88.1 | USD 92.2 |
| 11.5% | USD 76.5 | USD 79.2 | USD 82.3 |

## Sanity Checks

- Base-case DCF enterprise value is USD 174.352B, implying about **10.0x Year 5 FCF**. That is not aggressive, but it depends on FCF recovering from negative FY2026 levels.
- Terminal value is about **77.6% of DCF enterprise value**, acceptable for a recovery DCF but still assumption-sensitive.
- Current EV / FY2026 adjusted EBITA is about **19.9x**, so the market is already paying for some recovery despite the headline drawdown.
- Current EV / FY2026 revenue is only about **1.5x**, which looks cheap, but revenue quality is mixed because quick commerce and All others dilute margins.
- The dividend yield is about **1.0%** using the USD 1.05 per ADS annual dividend, so capital return is not enough by itself to anchor downside.

## What Would Change The Valuation

- Raise fair value if the next official quarter shows positive FCF or a much smaller outflow while Cloud revenue stays above 30% YoY.
- Raise fair value if China E-commerce adjusted EBITA stabilizes and quick-commerce unit economics improve without larger subsidies.
- Raise fair value if management gives clearer AI/cloud capex payback or AI-related product margin disclosure.
- Lower fair value if FY2027 capex intensity rises again without FCF improvement.
- Lower fair value if Cloud growth slows before margin expansion appears.

## Missing / Unverified Data

| Item | Status | Handling |
|---|---|---|
| Full FY2026 Form 20-F | ไม่พบข้อมูลที่ยืนยันได้ in this pass | Use official FY2026 results release. |
| Official earnings call transcript | ไม่พบข้อมูลที่ยืนยันได้ in this pass | Use release commentary only. |
| Segment-level FCF | Not disclosed | Model consolidated FCF only. |
| AI/cloud capex payback | Not disclosed | Treat as key valuation variable. |
| Quick-commerce subsidy cadence | Not disclosed | Do not infer precise margin recovery timing. |

## Entity Update

Updated `wiki/entities/BABA.md` with the 2026-06-18 valuation memo link and current fair value read.
