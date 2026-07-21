---
type: source-note
ticker: KO
company: The Coca-Cola Company
source_kind: market-quote
search_date: 2026-06-28
reporting_scope: Market data checked after 2026-06-26 regular-session close
currency: USD
normalized_output: raw/financials/KO_fundamentals.md
entity: "[[KO]]"
tags:
  - source/market-quote
  - ticker/KO
---

# KO - Market Quote 2026-06-28

## Source Map

| Source | URL | Checked | Use |
|---|---|---|---|
| MarketWatch KO quote page | https://www.marketwatch.com/investing/stock/ko | 2026-06-28 Asia/Bangkok | Fresh current price and market cap check for P11/P13. |
| The Coca-Cola Company Q1 2026 Form 10-Q | https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-028802/ko-20260403.htm | 2026-06-28 Asia/Bangkok | Shares outstanding, diluted shares, cash, debt, and balance sheet inputs. |
| The Coca-Cola Company Q1 2026 earnings release | https://investors.coca-colacompany.com/news-events/press-releases/detail/1158/coca-cola-reports-first-quarter-2026-results-and-updates-full-year-guidance | 2026-06-28 Asia/Bangkok | FY2026 FCF guidance used for valuation cross-checks. |

## Reporting Scope

- The current date is 2026-06-28, a Sunday. The fresh market price used is the latest regular-session close available from MarketWatch: 2026-06-26.
- Market data is a current-market input, not a company-disclosed financial-statement fact.

## Currency / Units

- Currency: USD.
- Market cap is USD billions unless stated otherwise.
- Shares are millions unless stated otherwise.

## Extracted Facts

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest regular-session close used | USD 82.63 on 2026-06-26 | MarketWatch KO quote page, checked 2026-06-28 Asia/Bangkok. |
| Market cap displayed by source | USD 355.54B | MarketWatch KO quote page, checked 2026-06-28 Asia/Bangkok. |
| Common shares outstanding | 4,302.482M | KO Q1 2026 Form 10-Q shares outstanding at 2026-04-17. |
| Market cap calculated from filing shares | USD 355.51B | 82.63 * 4,302.482M. |
| Diluted shares used for DCF | 4,314M | KO Q1 2026 Form 10-Q diluted weighted-average shares. |
| Cash and short-term investments | USD 11.083B | KO Q1 2026 Form 10-Q. |
| Total debt used for valuation | USD 43.890B | Loans and notes payable 0.332B + current maturities 4.493B + long-term debt 39.065B. |
| Net debt used for valuation | USD 32.807B | 43.890 - 11.083. |
| FY2026 free cash flow guidance | approximately USD 12.2B | KO Q1 2026 earnings release. |
| Forward FCF yield on market cap | 3.43% | 12.2 / 355.51. |
| Forward EV / guided FCF | 31.83x | (355.51 + 43.89 - 11.083) / 12.2. |
| FY2026 comparable EPS guide implied range | approximately USD 3.24 to USD 3.27 | FY2025 comparable EPS base of USD 3.00 from Q1 2026 release times 8% to 10% comparable currency-neutral EPS growth; actual comparable EPS guidance also includes currency and structural impacts. |
| Price / implied comparable EPS guide | approximately 25.3x to 25.5x | 82.63 / implied USD 3.24 to USD 3.27 range. |

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Intraday quote on 2026-06-28 | not applicable | 2026-06-28 is a Sunday; latest close used instead. |
| Company-disclosed market cap | not disclosed | Market cap is market-data-provider value and a calculation from price * filing shares. |
| Real-time quote feed timestamp beyond MarketWatch page check | ไม่พบข้อมูลที่ยืนยันได้ | Refresh before future action changes. |

## Handoff For Ingest

- Use USD 82.63 close on 2026-06-26 as the fresh price for valuation and decision memo dated 2026-06-28.
- Use MarketWatch displayed market cap USD 355.54B and calculated market cap USD 355.51B as cross-checks.
- Use official filing share counts, cash, and debt for valuation math.
