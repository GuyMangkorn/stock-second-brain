---
type: source-note
ticker: JNJ
company: Johnson & Johnson
source_kind: market-quote
search_date: 2026-07-09
reporting_scope: latest available market quote and pre-Q2 2026 earnings setup
currency: USD
normalized_output:
entity: "[[JNJ]]"
tags:
  - source/market-quote
  - ticker/JNJ
---

# JNJ - Market Quote 2026-07-09

## Source Map

| Priority | Source | URL / Path | Date / Timestamp | Notes |
|---:|---|---|---|---|
| 1 | Existing JNJ normalized facts | raw/financials/JNJ_fundamentals.md | Q1 2026, fiscal quarter ended 2026-03-29 | Official-source financial anchor for FCF, guidance, cash, debt, and shares. |
| 1 | SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/200406/000020040626000087/jnj-20260329.htm | filed 2026-04-22 | Common shares outstanding and Q1 financial statements. |
| 2 | J&J Q1 2026 results press release | https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-reports-Q1-2026-results-raises-2026-outlook/ | 2026-04-14 | Latest official quarterly result and FY2026 guidance available in this refresh. |
| 3 | MarketWatch peer-market note mentioning JNJ | https://www.marketwatch.com/data-news/biogen-inc-stock-underperforms-wednesday-when-compared-to-competitors-1093f1d3-1cbded96d28d | 2026-07-08 / published 2026-07-09 | Reports JNJ fell 1.44% to close at USD 263.40 on Wednesday, 2026-07-08. Market data is lower priority than company filings. |
| 4 | Investor's Business Daily earnings setup | https://www.investors.com/research/ibd-stock-of-the-day/johnson-johnson-stock-q2-2026-earnings-due/ | 2026-07-07 | Secondary context: Q2 2026 earnings due 2026-07-15 and stock in a technical buy zone. Not used as a durable company financial fact. |

## Reporting Scope

- Scope: market-data refresh and pre-Q2 2026 decision check.
- Latest official results verified in the vault: Q1 2026.
- Q2 2026 actual results: `ไม่พบข้อมูลที่ยืนยันได้` as of 2026-07-09 in this check.
- Secondary market context says Q2 2026 earnings are due 2026-07-15; this is not an official company filing fact in the captured source set.

## Currency / Units

- Market price: USD per share.
- Shares: actual common shares outstanding from SEC Form 10-Q.
- Market cap: USD billions, calculated.
- FCF outlook: USD billions from existing official-source JNJ facts.

## Extracted Facts

| Fact | Value | Source |
|---|---:|---|
| Latest checked share price | USD 263.40 | MarketWatch peer-market note, close on 2026-07-08. |
| Prior vault price check | USD 228.92 | `wiki/analysis/decisions/JNJ Decision Memo 2026-05-19.md`. |
| Price change since prior vault check | +15.1% | Calculated: 263.40 / 228.92 - 1. |
| Common shares outstanding | 2,407,216,971 | SEC Form 10-Q, as of 2026-04-17. |
| Market cap at USD 263.40 | USD 634.1B | Calculated: 263.40 * 2,407,216,971 / 1,000,000,000. |
| FY2026 FCF outlook | approximately USD 21.0B | Existing official-source JNJ facts from Q1 2026 transcript / `JNJ_fundamentals`. |
| Market cap / FY2026 FCF outlook | 30.2x | Calculated: 634.1 / 21.0. |
| FY2026 FCF yield | 3.31% | Calculated: 21.0 / 634.1. |
| FY2026 adjusted EPS guidance midpoint | USD 11.55 | J&J Q1 2026 press release / presentation in existing source note. |
| Forward adjusted P/E on guidance midpoint | 22.8x | Calculated: 263.40 / 11.55. |
| Annual dividend rate | USD 5.36 | Existing official-source JNJ facts from Q1 2026 transcript / presentation. |
| Dividend yield at USD 263.40 | 2.03% | Calculated: 5.36 / 263.40. |
| Prior base DCF fair value | USD 150.38/share | `wiki/analysis/valuations/JNJ DCF Valuation 2026-05-19.md`. |
| Gap to prior base DCF fair value | -42.9% | Calculated: 150.38 / 263.40 - 1. |

## Decision Context

ราคาหุ้นที่สูงขึ้นทำให้ quality case ไม่ได้หายไป แต่ margin of safety แย่ลงชัดเจน. ก่อน Q2 2026 results สิ่งที่ควรรอคือ cash-flow conversion, net debt, STELARA headwind, MedTech margin/tariff impact, and any FY2026 guidance revision. หากงบ Q2 ไม่ยก FY2026 FCF outlook สูงกว่าเดิมอย่างมีนัยสำคัญ ราคา USD 263.40 ยังดู demanding เมื่อเทียบกับ FCF outlook ประมาณ USD 21B.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Q2 2026 official results | ไม่พบข้อมูลที่ยืนยันได้ | Secondary source says earnings due 2026-07-15, after this 2026-07-09 check. |
| Official company-hosted July 2026 market quote | ไม่พบข้อมูลที่ยืนยันได้ | J&J IR stock quote page did not expose quote values in captured text. |
| Updated shares after 2026-04-17 | ไม่พบข้อมูลที่ยืนยันได้ | This refresh uses latest SEC verified common shares outstanding from Q1 Form 10-Q. |
| Updated FY2026 FCF guidance after Q1 | ไม่พบข้อมูลที่ยืนยันได้ | No newer official earnings release was captured before Q2 results. |

## Handoff For Analysis

Use this quote note to refresh `wiki/analysis/decisions/JNJ Decision Memo 2026-07-09.md` and `wiki/entities/JNJ.md`. Do not update `raw/financials/JNJ_fundamentals.md` unless new official financial statements or guidance are ingested.
