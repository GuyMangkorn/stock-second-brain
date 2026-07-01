---
type: etf_top10_holdings_source_status
created: 2026-07-01
universe_source: wiki/analysis/comparisons/Dividend ETF Full Universe Triage 2026-06-28.md
custom-width: 90
---

# ETF Top 10 Holdings Sources 2026-07-01

## Scope

Initial source-status note for the updated ETF grouping goal: group ETFs by verified Top 10 holdings where available, otherwise mark holdings as not found / pending and use ETF description fallback grouping.

## Official Source Patterns Tested

- BlackRock/iShares new product page embeds `productDataContext`; holdings are fetched through `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data` with `component=holdings.all`, `portfolioId`, `locale`, and `targetSite`.
- iShares old CSV endpoint returned HTML for DGRO, so it was not used as source evidence.
- iShares product screener JSON returned HTTP 500 during this run, so it was not usable for productId discovery.
- Vanguard VIG official page exposes `fundProfileData`, but the holdings endpoint was not fully resolved in this batch.

## Verified Holdings Extracted

### AMEX:DGRO

- Source: BlackRock/iShares official product-data API, portfolioId 264623
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=en_US&portfolioId=264623&targetSite=us-ishares&userType=individual&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `JNJ` | JOHNSON & JOHNSON | 3.12% |
| 2 | `ABBV` | ABBVIE INC | 3.05% |
| 3 | `JPM` | JPMORGAN CHASE & CO | 3.03% |
| 4 | `AAPL` | APPLE INC | 2.76% |
| 5 | `MSFT` | MICROSOFT CORP | 2.67% |
| 6 | `XOM` | EXXON MOBIL CORP | 2.60% |
| 7 | `AVGO` | BROADCOM INC | 2.55% |
| 8 | `HD` | HOME DEPOT INC | 2.33% |
| 9 | `PG` | PROCTER & GAMBLE | 2.26% |
| 10 | `PM` | PHILIP MORRIS INTERNATIONAL INC | 2.08% |

### CBOE:IDV

- Source: BlackRock/iShares official product-data API, portfolioId 239499
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=en_US&portfolioId=239499&targetSite=us-ishares&userType=individual&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `TTE` | TOTALENERGIES | 4.35% |
| 2 | `BATS` | BRITISH AMERICAN TOBACCO | 4.08% |
| 3 | `ENEL` | ENEL | 3.25% |
| 4 | `RIO` | RIO TINTO PLC | 2.79% |
| 5 | `ENI` | ENI | 2.59% |
| 6 | `TEF` | TELEFONICA SA | 2.20% |
| 7 | `MBG` | MERCEDES-BENZ GROUP N AG | 2.14% |
| 8 | `ZURN` | ZURICH INSURANCE GROUP AG | 2.09% |
| 9 | `INGA` | ING GROEP NV | 1.92% |
| 10 | `REP` | REPSOL SA | 1.89% |

## Failed / Rejected Lookup

- `NASDAQ:DVY`: candidate iShares `portfolioId=239464` was rejected because official API returned `iShares Intermediate Government/Credit Bond ETF` / `GVI`, not `iShares Select Dividend ETF` / `DVY`. Marked `official_lookup_failed` until correct official productId/source is found.

## Next Extraction Queue

- Resolve official issuer holdings endpoints for Vanguard, State Street SPDR, WisdomTree, ProShares, Invesco, Fidelity, First Trust, VanEck, ALPS, Global X, and regional exchanges.
- For every ETF, set one of: `official_holdings_found`, `official_lookup_failed`, or `source_not_available_after_check`; do not infer Top 10 holdings from fund name.
