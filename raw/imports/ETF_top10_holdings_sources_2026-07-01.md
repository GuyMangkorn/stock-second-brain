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


## Additional Verified Holdings Extracted - Batch 2026-07-01B
### Source Patterns Added
- State Street/SPDR official fund pages expose `Fund Top Holdings` tables directly in HTML; parsed `SPYD`, `SDY`, and `WDIV`.
- ProShares official fund pages expose holdings tables directly in HTML; parsed `NOBL`, `REGL`, `SMDV`, and `TDV`.
- Vanguard official `vmf` portfolio-holding endpoint worked for U.S.-listed Vanguard ETFs: `https://investor.vanguard.com/vmf/api/{ticker}/portfolio-holding/stock.json?asOfType=daily`; parsed `VIG`, `VYM`, `VIGI`, and `VYMI`.
- WisdomTree official product pages returned Cloudflare challenge content in this environment, and guessed holdings CSV paths did not return usable holdings files; WisdomTree ETFs remain `pending_source_check` rather than inferred.
### AMEX:SPYD
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/us/en/intermediary/etfs/spdr-portfolio-sp-500-high-dividend-etf-spyd`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | IRON MOUNTAIN INC | 1.61% |
| 2 | `not disclosed` | FRANKLIN RESOURCES INC | 1.56% |
| 3 | `not disclosed` | CVS HEALTH CORP | 1.52% |
| 4 | `not disclosed` | HOST HOTELS + RESORTS INC | 1.52% |
| 5 | `not disclosed` | EDISON INTERNATIONAL | 1.47% |
| 6 | `not disclosed` | TARGET CORP | 1.47% |
| 7 | `not disclosed` | APA CORP | 1.47% |
| 8 | `not disclosed` | VIATRIS INC | 1.45% |
| 9 | `not disclosed` | KIMCO REALTY CORP | 1.45% |
| 10 | `not disclosed` | SIMON PROPERTY GROUP INC | 1.44% |

### AMEX:SDY
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/us/en/intermediary/etfs/spdr-sp-dividend-etf-sdy`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | VERIZON COMMUNICATIONS INC | 2.15% |
| 2 | `not disclosed` | REALTY INCOME CORP | 2.14% |
| 3 | `not disclosed` | KENVUE INC | 1.76% |
| 4 | `not disclosed` | KIMBERLY CLARK CORP | 1.75% |
| 5 | `not disclosed` | ABBVIE INC | 1.62% |
| 6 | `not disclosed` | QUALCOMM INC | 1.57% |
| 7 | `not disclosed` | TEXAS INSTRUMENTS INC | 1.56% |
| 8 | `not disclosed` | TARGET CORP | 1.55% |
| 9 | `not disclosed` | AUTOMATIC DATA PROCESSING | 1.54% |
| 10 | `not disclosed` | EDISON INTERNATIONAL | 1.45% |

### AMEX:WDIV
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/us/en/intermediary/etfs/spdr-sp-global-dividend-etf-wdiv`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | LENOVO GROUP LTD | 2.24% |
| 2 | `not disclosed` | LEGAL + GENERAL GROUP PLC | 1.79% |
| 3 | `not disclosed` | ALTRIA GROUP INC | 1.74% |
| 4 | `not disclosed` | HIGHWOODS PROPERTIES INC | 1.74% |
| 5 | `not disclosed` | GETTY REALTY CORP | 1.61% |
| 6 | `not disclosed` | NORTHWEST BANCSHARES INC | 1.57% |
| 7 | `not disclosed` | APA GROUP | 1.50% |
| 8 | `not disclosed` | VERIZON COMMUNICATIONS INC | 1.47% |
| 9 | `not disclosed` | TELUS CORP | 1.47% |
| 10 | `not disclosed` | VANGUARD INTERNATIONAL SEMI | 1.45% |

### CBOE:NOBL
- Source: ProShares official fund page HTML
- URL: `https://www.proshares.com/our-etfs/strategic/nobl`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `CAT` | CATERPILLAR INC | 1.86% |
| 2 | `WST` | WEST PHARMACEUTICAL SERVICES | 1.82% |
| 3 | `SWK` | STANLEY BLACK & DECKER INC | 1.72% |
| 4 | `ABBV` | ABBVIE INC | 1.71% |
| 5 | `BEN` | FRANKLIN RESOURCES INC | 1.70% |
| 6 | `SJM` | JM SMUCKER CO/THE | 1.64% |
| 7 | `HRL` | HORMEL FOODS CORP | 1.63% |
| 8 | `GWW` | WW GRAINGER INC | 1.62% |
| 9 | `CAH` | CARDINAL HEALTH INC | 1.61% |
| 10 | `ESS` | ESSEX PROPERTY TRUST INC | 1.61% |

### CBOE:REGL
- Source: ProShares official fund page HTML
- URL: `https://www.proshares.com/our-etfs/strategic/regl`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `CHE` | CHEMED CORP | 1.88% |
| 2 | `CBT` | CABOT CORP | 1.80% |
| 3 | `THG` | HANOVER INSURANCE GROUP INC/ | 1.78% |
| 4 | `UMBF` | UMB FINANCIAL CORP | 1.75% |
| 5 | `AIT` | APPLIED INDUSTRIAL TECH INC | 1.73% |
| 6 | `LFUS` | LITTELFUSE INC | 1.73% |
| 7 | `R` | RYDER SYSTEM INC | 1.72% |
| 8 | `CBSH` | COMMERCE BANCSHARES INC | 1.72% |
| 9 | `SLGN` | SILGAN HOLDINGS INC | 1.72% |
| 10 | `UNM` | UNUM GROUP | 1.71% |

### CBOE:SMDV
- Source: ProShares official fund page HTML
- URL: `https://www.proshares.com/our-etfs/strategic/smdv`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `HNI` | HNI CORP | 1.17% |
| 2 | `MTRN` | MATERION CORP | 1.16% |
| 3 | `GOLF` | ACUSHNET HOLDINGS CORP | 1.14% |
| 4 | `SXI` | STANDEX INTERNATIONAL CORP | 1.13% |
| 5 | `APOG` | APOGEE ENTERPRISES INC | 1.10% |
| 6 | `BMI` | BADGER METER INC | 1.09% |
| 7 | `NPO` | ENPRO INC | 1.08% |
| 8 | `GRC` | GORMAN-RUPP CO | 1.06% |
| 9 | `KWR` | QUAKER CHEMICAL CORPORATION | 1.06% |
| 10 | `AGM` | FEDERAL AGRIC MTG CORP-CL C | 1.05% |

### CBOE:TDV
- Source: ProShares official fund page HTML
- URL: `https://www.proshares.com/our-etfs/strategic/tdv`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `AMAT` | APPLIED MATERIALS INC | 4.42% |
| 2 | `KLAC` | KLA CORP | 4.08% |
| 3 | `LRCX` | LAM RESEARCH CORP | 4.05% |
| 4 | `KLIC` | KULICKE & SOFFA INDUSTRIES | 3.85% |
| 5 | `QCOM` | QUALCOMM INC | 3.29% |
| 6 | `CGNX` | COGNEX CORP | 3.25% |
| 7 | `CSCO` | CISCO SYSTEMS INC | 3.16% |
| 8 | `TXN` | TEXAS INSTRUMENTS INC | 3.08% |
| 9 | `POWI` | POWER INTEGRATIONS INC | 3.00% |
| 10 | `BMI` | BADGER METER INC | 2.96% |

### AMEX:VIG
- Source: Vanguard official vmf portfolio-holding API
- URL: `https://investor.vanguard.com/vmf/api/VIG/portfolio-holding/stock.json?asOfType=daily`
- As of: `2026-05-31`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `AVGO` | BROADCOM INC | 5.41% |
| 2 | `AAPL` | APPLE INC | 4.57% |
| 3 | `MSFT` | MICROSOFT CORP | 4.27% |
| 4 | `LLY` | ELI LILLY & CO | 3.85% |
| 5 | `JPM` | JPMORGAN CHASE | 3.32% |
| 6 | `XOM` | EXXON MOBIL CORP | 2.67% |
| 7 | `JNJ` | JOHNSON&JOHNSON | 2.39% |
| 8 | `V` | VISA INC-CLASS A | 2.25% |
| 9 | `WMT` | WALMART INC | 2.23% |
| 10 | `CSCO` | CISCO SYSTEMS | 2.09% |

### AMEX:VYM
- Source: Vanguard official vmf portfolio-holding API
- URL: `https://investor.vanguard.com/vmf/api/VYM/portfolio-holding/stock.json?asOfType=daily`
- As of: `2026-05-31`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `AVGO` | BROADCOM INC | 8.51% |
| 2 | `JPM` | JPMORGAN CHASE | 3.14% |
| 3 | `XOM` | EXXON MOBIL CORP | 2.53% |
| 4 | `JNJ` | JOHNSON&JOHNSON | 2.24% |
| 5 | `CSCO` | CISCO SYSTEMS | 1.98% |
| 6 | `CAT` | CATERPILLAR INC | 1.67% |
| 7 | `ABBV` | ABBVIE INC | 1.59% |
| 8 | `ORCL` | ORACLE CORP | 1.57% |
| 9 | `UNH` | UNITEDHEALTH GRP | 1.43% |
| 10 | `CVX` | CHEVRON CORP | 1.41% |

### NASDAQ:VIGI
- Source: Vanguard official vmf portfolio-holding API
- URL: `https://investor.vanguard.com/vmf/api/VIGI/portfolio-holding/stock.json?asOfType=daily`
- As of: `2026-05-31`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `RY` | ROYAL BANK OF CA | 4.47% |
| 2 | `8306` | MITSUBISHI UFJ F | 3.94% |
| 3 | `NESN` | NESTLE SA-REG | 3.80% |
| 4 | `NOVN` | NOVARTIS AG-REG | 3.55% |
| 5 | `TD` | TORONTO-DOM BANK | 3.40% |
| 6 | `ROP` | ROCHE HOLDING AG | 3.39% |
| 7 | `SAP` | SAP SE | 3.26% |
| 8 | `SU` | SCHNEIDER ELECTR | 3.01% |
| 9 | `6501` | HITACHI LTD | 2.62% |
| 10 | `NOVO B` | NOVO NORDISK-B | 2.57% |

### NASDAQ:VYMI
- Source: Vanguard official vmf portfolio-holding API
- URL: `https://investor.vanguard.com/vmf/api/VYMI/portfolio-holding/stock.json?asOfType=daily`
- As of: `2026-05-31`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `HSBA` | HSBC HOLDINGS PL | 1.72% |
| 2 | `ROP` | ROCHE HOLDING AG | 1.58% |
| 3 | `NOVN` | NOVARTIS AG-REG | 1.55% |
| 4 | `RY` | ROYAL BANK OF CA | 1.44% |
| 5 | `NESN` | NESTLE SA-REG | 1.40% |
| 6 | `SHEL` | SHELL PLC | 1.29% |
| 7 | `BHP` | BHP GROUP LTD | 1.17% |
| 8 | `8306` | MITSUBISHI UFJ F | 1.11% |
| 9 | `2454` | MEDIATEK | 1.06% |
| 10 | `CBA` | COMMONW BK AUSTR | 1.06% |

## Next Extraction Queue

- Resolve official issuer holdings endpoints for Vanguard, State Street SPDR, WisdomTree, ProShares, Invesco, Fidelity, First Trust, VanEck, ALPS, Global X, and regional exchanges.
- For every ETF, set one of: `official_holdings_found`, `official_lookup_failed`, or `source_not_available_after_check`; do not infer Top 10 holdings from fund name.
