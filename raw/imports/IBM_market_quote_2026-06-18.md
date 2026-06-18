---
type: source-note
ticker: IBM
company: International Business Machines Corporation
source_kind: market_quote
search_date: 2026-06-18
reporting_scope: latest market quote and price-drop context for decision refresh
currency: USD
normalized_output: wiki/analysis/decisions/IBM Decision Memo 2026-06-18.md
entity: "[[IBM]]"
tags:
  - source/market-quote
  - ticker/IBM
---

# IBM - Market Quote Source - 2026-06-18

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| MarketWatch IBM daily market-data article | https://www.marketwatch.com/data-news/international-business-machines-corp-stock-outperforms-competitors-despite-losses-on-the-day-dfde7ca3-d1796dbb0803 | Latest close, daily move, 52-week high distance, volume, and market comparison for 2026-06-17. |
| Investopedia IBM record-high / Barclays context | https://www.investopedia.com/ibm-stock-just-reached-a-new-record-high-why-barclays-says-it-is-following-the-nvidia-playbook-11987791 | Secondary context for the early-June rally and analyst / AI / quantum narrative. |
| Axios IBM meme-stock context | https://www.axios.com/2026/06/02/ibm-meme-stock-trump | Secondary market-chatter context for speculative early-June price action. |
| IBM Q1 2026 earnings release | https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS | Existing official source for Q1 2026 financial facts, guidance, debt, cash, FCF, and quarterly dividend. |
| IBM Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/51143/000005114326000038/ibm-20260331.htm | Existing official source for share count and financial statement details. |
| Prior normalized facts | raw/financials/IBM_fundamentals.md | Source-backed operating and balance-sheet inputs used in the decision refresh. |
| Prior DCF memo | wiki/analysis/valuations/IBM DCF Valuation 2026-06-10.md | Source-backed DCF scenarios and fair value ranges used for current valuation read. |

## Reporting Scope

- Market quote checked on 2026-06-18 Asia/Bangkok.
- Latest close found: 2026-06-17 regular-session close.
- This note updates market context only. It does not replace official IBM filings, earnings release, or normalized Q1 2026 financial facts.
- Secondary news / market-chatter sources are used only to explain price action context, not as durable company financial facts.

## Currency / Units

- Currency: USD.
- Stock price: USD per common share.
- Volume: shares.
- Financial calculations use USD billions unless noted.

## Extracted Facts

| Field | Value | Source |
|---|---:|---|
| Symbol | IBM | MarketWatch IBM daily market-data article. |
| Latest regular-session close | USD 262.35 | MarketWatch, 2026-06-17 close. |
| Daily move | -3.12% | MarketWatch, 2026-06-17. |
| S&P 500 daily move | -1.21% | MarketWatch, 2026-06-17. |
| Dow Jones Industrial Average daily move | -0.98% | MarketWatch, 2026-06-17. |
| 52-week high | USD 332.46 | MarketWatch; high reached 2026-06-02. |
| Distance from 52-week high | -21.09% | MarketWatch. |
| Trading volume | 5.5M | MarketWatch, 2026-06-17. |
| 50-day average volume | 8.8M | MarketWatch, 2026-06-17. |

## Price Action Context

| Context | Read | Source |
|---|---|---|
| Early-June spike | IBM reached a record-high area after a strong AI / software / quantum narrative and Barclays initiated coverage with an overweight rating and USD 350 target. | Investopedia. |
| Speculative momentum | Some early-June price action was described as retail / meme-stock driven around quantum enthusiasm and viral political-video chatter. | Axios. |
| Latest decline | 2026-06-17 decline occurred during a broad market selloff, but IBM still closed about 21.1% below its 52-week high. | MarketWatch. |
| Operating fundamentals | No new official quarterly IBM result after Q1 2026 was verified in this refresh. | Existing IBM source note and official source set. |

## Calculations Used In Refresh

| Metric | Value | Formula / Source |
|---|---:|---|
| Shares outstanding used for market cap | 939.88528M | IBM Q1 2026 Form 10-Q cover page, carried from `raw/financials/IBM_fundamentals.md`. |
| Diluted shares used for DCF | 952.1M | IBM Q1 2026 weighted-average diluted shares, carried from `raw/financials/IBM_fundamentals.md`. |
| Market capitalization | USD 246.58B | 262.35 * 939.88528M. |
| Implied market cap using diluted shares | USD 249.79B | 262.35 * 952.1M. |
| Price move since 2026-06-10 quote | -5.45% | 262.35 / 277.49 - 1. |
| Price move since 2026-05-20 close | +16.66% | 262.35 / 224.88 - 1. |
| Price move from 52-week high | -21.09% | 262.35 / 332.46 - 1. |
| TTM IBM-defined FCF | USD 14.992B | FY2025 FCF 14.734B - Q1 2025 FCF 1.962B + Q1 2026 FCF 2.220B. |
| Market FCF yield | 6.08% | 14.992 / 246.58. |
| Market EV / TTM FCF | 20.09x | (246.58 + 66.40 - 11.828) / 14.992. |
| FY2026 guided FCF yield | about 6.38% | 15.734 / 246.58, using FY2025 FCF plus about USD 1B guidance. |
| Annualized dividend yield | about 2.58% | 1.69 * 4 / 262.35; dividend from IBM Q1 2026 earnings release. |
| Base DCF downside | -8.42% | 240.27 / 262.35 - 1. |

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Intraday real-time quote on 2026-06-18 | not disclosed | This refresh uses the latest regular-session close found, 2026-06-17. |
| Any new IBM operating results after Q1 2026 | ไม่พบข้อมูลที่ยืนยันได้ | No newer official quarterly result was used in this refresh. |
| Product-level AI / quantum revenue and margins | not disclosed | Secondary price-action context cannot replace official segment economics. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Needed for personalized add / trim sizing. |

## Handoff For Ingest

- Use the quote only for `Current Price / Market Data Check` in decision memos.
- Do not overwrite Q1 2026 financial facts with market-data values.
- Refresh again after Q2 2026 official results or before any trading decision.
