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

## Additional Verified Holdings Extracted - Batch 2026-07-01C
### Source Patterns Added
- Invesco official pages expose CUSIP metadata and holdings through `https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/{CUSIP}/holdings/fund?idType=cusip&productType=ETF`; parsed `DJD`, `PEY`, `PFM`, `PID`, `KBWY`, and `KBWD`.
- First Trust official holdings pages expose `Holdings of the Fund` HTML tables; parsed `TDIV`, `FVD`, and `FDD`.
- ALPS/Alerian official fund pages call `https://www.alpsfunds.com/_hcms/api/getData?api_url=https://secure.alpsinc.com/MarketingAPI/api/v1/Holding/{TICKER}/Full`; parsed `SDOG`, `IDOG`, `ENFR`, and `AMLP`.
- Global X official fund page links a full holdings CSV; parsed `SDIV` from `https://assets.globalxetfs.com/funds/holdings/sdiv_full-holdings_20260630.csv`.

### AMEX:DJD
- Source: Invesco official holdings API
- URL: `https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46137V605/holdings/fund?idType=cusip&productType=ETF`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `UNH` | UnitedHealth Group Inc | 8.65% |
| 2 | `CVX` | Chevron Corp | 6.49% |
| 3 | `CSCO` | Cisco Systems Inc | 6.26% |
| 4 | `IBM` | International Business Machines Corp | 6.22% |
| 5 | `MRK` | Merck & Co Inc | 6.01% |
| 6 | `KO` | Coca-Cola Co/The | 5.39% |
| 7 | `GS` | Goldman Sachs Group Inc/The | 5.06% |
| 8 | `AMGN` | Amgen Inc | 4.90% |
| 9 | `HD` | Home Depot Inc/The | 4.84% |
| 10 | `PG` | Procter & Gamble Co/The | 4.76% |

### AMEX:SDOG
- Source: ALPS/Alerian official holdings API via ALPS fund page proxy
- URL: `https://www.alpsfunds.com/_hcms/api/getData?api_url=https://secure.alpsinc.com/MarketingAPI/api/v1/Holding/SDOG/Full`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `GPC` | Genuine Parts Co. | 2.32% |
| 2 | `ABBV` | AbbVie Inc. | 2.25% |
| 3 | `WSO` | Watsco Inc. | 2.23% |
| 4 | `MRK` | Merck & Co. Inc. | 2.20% |
| 5 | `SW` | Smurfit Westrock PLC | 2.18% |
| 6 | `AMCR` | Amcor PLC | 2.18% |
| 7 | `IP` | International Paper Co. | 2.15% |
| 8 | `KVUE` | Kenvue Inc. | 2.15% |
| 9 | `ES` | Eversource Energy | 2.15% |
| 10 | `SNA` | Snap-On Inc. | 2.12% |

### NASDAQ:PEY
- Source: Invesco official holdings API
- URL: `https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46137V563/holdings/fund?idType=cusip&productType=ETF`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `FLO` | Flowers Foods Inc | 4.03% |
| 2 | `PRGO` | Perrigo Co PLC | 3.67% |
| 3 | `RHI` | Robert Half Inc | 3.31% |
| 4 | `NSP` | Insperity Inc | 3.30% |
| 5 | `UVV` | Universal Corp/VA | 2.52% |
| 6 | `MO` | Altria Group Inc | 2.51% |
| 7 | `UPS` | United Parcel Service Inc | 2.45% |
| 8 | `MAIN` | Main Street Capital Corp | 2.41% |
| 9 | `PFE` | Pfizer Inc | 2.39% |
| 10 | `KMB` | Kimberly-Clark Corp | 2.33% |

### NASDAQ:TDIV
- Source: First Trust official holdings page HTML
- URL: `https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=TDIV`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `IBM` | International Business Machines Corporation | 8.09% |
| 2 | `AVGO` | Broadcom Inc. | 7.24% |
| 3 | `MSFT` | Microsoft Corporation | 7.10% |
| 4 | `TXN` | Texas Instruments Incorporated | 7.06% |
| 5 | `ORCL` | Oracle Corporation | 5.34% |
| 6 | `TSM` | Taiwan Semiconductor Manufacturing Company Limited (ADR) | 4.89% |
| 7 | `AMAT` | Applied Materials, Inc. | 3.54% |
| 8 | `QCOM` | QUALCOMM Incorporated | 3.15% |
| 9 | `ADI` | Analog Devices, Inc. | 2.87% |
| 10 | `KLAC` | KLA Corporation | 2.35% |

### NASDAQ:PFM
- Source: Invesco official holdings API
- URL: `https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46137V506/holdings/fund?idType=cusip&productType=ETF`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `LLY` | Eli Lilly & Co | 4.13% |
| 2 | `AAPL` | Apple Inc | 3.68% |
| 3 | `AVGO` | Broadcom Inc | 3.36% |
| 4 | `WMT` | Walmart Inc | 3.30% |
| 5 | `MSFT` | Microsoft Corp | 3.29% |
| 6 | `JPM` | JPMorgan Chase & Co | 3.21% |
| 7 | `JNJ` | Johnson & Johnson | 2.24% |
| 8 | `V` | Visa Inc | 2.08% |
| 9 | `XOM` | Exxon Mobil Corp | 2.07% |
| 10 | `LRCX` | Lam Research Corp | 1.98% |

### AMEX:FVD
- Source: First Trust official holdings page HTML
- URL: `https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=FVD`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `JKHY` | Jack Henry & Associates, Inc. | 0.44% |
| 2 | `REYN` | Reynolds Consumer Products Inc. | 0.44% |
| 3 | `RLI` | RLI Corp. | 0.44% |
| 4 | `SON` | Sonoco Products Company | 0.44% |
| 5 | `ABBV` | AbbVie Inc. | 0.43% |
| 6 | `AJG` | Arthur J. Gallagher & Co. | 0.43% |
| 7 | `BRO` | Brown & Brown, Inc. | 0.43% |
| 8 | `CMCSA` | Comcast Corporation (Class A) | 0.43% |
| 9 | `IBM` | International Business Machines Corporation | 0.43% |
| 10 | `JNJ` | Johnson & Johnson | 0.43% |

### NASDAQ:PID
- Source: Invesco official holdings API
- URL: `https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46137V548/holdings/fund?idType=cusip&productType=ETF`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `ITUB` | Itau Unibanco Holding SA | 4.35% |
| 2 | `TLK` | Telkom Indonesia Persero Tbk PT | 3.61% |
| 3 | `TU` | TELUS Corp | 3.58% |
| 4 | `SNY` | Sanofi SA | 3.21% |
| 5 | `FINV` | FinVolution Group | 3.16% |
| 6 | `BTI` | British American Tobacco PLC | 3.11% |
| 7 | `ENB` | Enbridge Inc | 2.97% |
| 8 | `OTEX` | Open Text Corp | 2.52% |
| 9 | `BIP` | Brookfield Infrastructure Partners LP | 2.51% |
| 10 | `E` | Eni SpA | 2.50% |

### AMEX:ENFR
- Source: ALPS/Alerian official holdings API via ALPS fund page proxy
- URL: `https://www.alpsfunds.com/_hcms/api/getData?api_url=https://secure.alpsinc.com/MarketingAPI/api/v1/Holding/ENFR/Full`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `ENB CN` | Enbridge Inc. | 8.26% |
| 2 | `ET` | Energy Transfer LP | 7.82% |
| 3 | `EPD` | Enterprise Products Partners LP | 7.05% |
| 4 | `WMB` | The Williams Cos. Inc. | 6.33% |
| 5 | `DTM` | DT Midstream Inc. | 5.27% |
| 6 | `KMI` | Kinder Morgan Inc. | 5.14% |
| 7 | `MPLX` | MPLX LP | 5.02% |
| 8 | `LNG` | Cheniere Energy Inc. | 5.02% |
| 9 | `PAGP` | Plains GP Holdings LP | 5.02% |
| 10 | `TRGP` | Targa Resources Corp. | 5.01% |

### AMEX:IDOG
- Source: ALPS/Alerian official holdings API via ALPS fund page proxy
- URL: `https://www.alpsfunds.com/_hcms/api/getData?api_url=https://secure.alpsinc.com/MarketingAPI/api/v1/Holding/IDOG/Full`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `SIA SP` | Singapore Airlines Ltd. | 2.27% |
| 2 | `BNP FP` | BNP Paribas SA | 2.18% |
| 3 | `7267 JP` | Honda Motor Co. Ltd. | 2.16% |
| 4 | `BAMI IM` | Banco BPM SpA | 2.15% |
| 5 | `ENEL IM` | Enel SpA | 2.11% |
| 6 | `EDP PL` | EDP SA | 2.11% |
| 7 | `ML FP` | Cie Generale des Etablissements Michelin SCA | 2.10% |
| 8 | `4503 JP` | Astellas Pharma Inc. | 2.09% |
| 9 | `BMPS IM` | Banca Monte dei Paschi di Siena SpA | 2.09% |
| 10 | `4502 JP` | Takeda Pharmaceutical Co. Ltd. | 2.08% |

### AMEX:AMLP
- Source: ALPS/Alerian official holdings API via ALPS fund page proxy
- URL: `https://www.alpsfunds.com/_hcms/api/getData?api_url=https://secure.alpsinc.com/MarketingAPI/api/v1/Holding/AMLP/Full`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `SUN` | Sunoco LP | 12.58% |
| 2 | `ET` | Energy Transfer LP | 12.31% |
| 3 | `MPLX` | MPLX LP | 12.05% |
| 4 | `WES` | Western Midstream Partners LP | 12.05% |
| 5 | `PAA` | Plains All American Pipeline LP | 11.98% |
| 6 | `EPD` | Enterprise Products Partners LP | 11.91% |
| 7 | `HESM` | Hess Midstream LP | 8.29% |
| 8 | `CQP` | Cheniere Energy Partners LP | 4.23% |
| 9 | `USAC` | USA Compression Partners LP | 3.68% |
| 10 | `GEL` | Genesis Energy LP | 2.66% |

### AMEX:FDD
- Source: First Trust official holdings page HTML
- URL: `https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=FDD`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `LGEN.LN` | Legal & General Group Plc | 6.11% |
| 2 | `TW/.LN` | Taylor Wimpey Plc | 4.63% |
| 3 | `AGN.NA` | Aegon Ltd. | 4.25% |
| 4 | `BME.LN` | B&M European Value Retail SA | 4.18% |
| 5 | `ABN.NA` | ABN AMRO Group N.V. | 4.06% |
| 6 | `NWG.LN` | Natwest Group Plc | 3.98% |
| 7 | `LIGHT.NA` | Signify NV | 3.97% |
| 8 | `INVP.LN` | Investec Plc | 3.93% |
| 9 | `AKRBP.NO` | Aker BP ASA | 3.92% |
| 10 | `TEP.FP` | Teleperformance SE | 3.85% |

### AMEX:SDIV
- Source: Global X official full holdings CSV
- URL: `https://assets.globalxetfs.com/funds/holdings/sdiv_full-holdings_20260630.csv`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `TFG-R TB` | THAIFOODS GROUP PCL-NVDR | 2.01% |
| 2 | `IIPR` | INNOVATIVE INDUSTRIAL PROPER | 1.36% |
| 3 | `PK` | PARK HOTELS & RESORTS INC | 1.28% |
| 4 | `HAUTO NO` | HOEGH AUTOLINERS ASA | 1.25% |
| 5 | `NAT` | NORDIC AMERICAN TANKERS LTD | 1.23% |
| 6 | `SAUD3 BZ` | BRADSAUDE SA | 1.22% |
| 7 | `TFSL` | TFS FINANCIAL CORP | 1.20% |
| 8 | `QFIN` | QFIN HOLDINGS INC-ADR | 1.20% |
| 9 | `RHI` | ROBERT HALF INC | 1.18% |
| 10 | `ALX` | ALEXANDER'S INC | 1.18% |

### NASDAQ:KBWY
- Source: Invesco official holdings API
- URL: `https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46138E594/holdings/fund?idType=cusip&productType=ETF`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `IIPR` | Innovative Industrial Properties Inc | 6.47% |
| 2 | `CHCT` | Community Healthcare Trust Inc | 5.30% |
| 3 | `MRP` | Millrose Properties Inc | 5.14% |
| 4 | `PK` | Park Hotels & Resorts Inc | 4.41% |
| 5 | `GOOD` | Gladstone Commercial Corp | 4.16% |
| 6 | `HIW` | Highwoods Properties Inc | 3.97% |
| 7 | `AHRT` | AH Realty Trust Inc | 3.91% |
| 8 | `DEA` | Easterly Government Properties Inc | 3.50% |
| 9 | `CTO` | CTO Realty Growth Inc | 3.47% |
| 10 | `GNL` | Global Net Lease Inc | 3.47% |

### NASDAQ:KBWD
- Source: Invesco official holdings API
- URL: `https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46138E610/holdings/fund?idType=cusip&productType=ETF`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `IVR` | Invesco Mortgage Capital Inc | 4.27% |
| 2 | `ORC` | Orchid Island Capital Inc | 4.25% |
| 3 | `ARR` | ARMOUR Residential REIT Inc | 3.94% |
| 4 | `PMT` | PennyMac Mortgage Investment Trust | 3.82% |
| 5 | `DX` | Dynex Capital Inc | 3.66% |
| 6 | `MFA` | MFA Financial Inc | 3.65% |
| 7 | `GSBD` | Goldman Sachs BDC Inc | 3.63% |
| 8 | `FSK` | FS KKR Capital Corp | 3.62% |
| 9 | `AGNC` | AGNC Investment Corp | 3.41% |
| 10 | `PFLT` | PennantPark Floating Rate Capital Ltd | 3.21% |

## Additional Verified Holdings Extracted - Batch 2026-07-01D
### Source Patterns Added
- State Street/SPDR official fund pages expose `Top Holdings` / `Fund Top 10 Holdings` tables directly in HTML for U.S., Europe, and Australia locales; parsed `DWX`, `SPYW`, `ZPRG`, `ZPRA`, `WDIV` on ASX, and `SYI`.
- State Street/SPDR top-holdings tables in this batch did not disclose security tickers, so ticker fields are recorded as `not disclosed` rather than inferred.

### XETR:SPYW
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/de/en_gb/intermediary/etfs/state-street-spdr-sp-euro-dividend-aristocrats-ucits-etf-dist-spyw-gy`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | ageas SA/NV | 3.71% |
| 2 | `not disclosed` | NN Group N.V. | 3.54% |
| 3 | `not disclosed` | Teleperformance SE | 3.52% |
| 4 | `not disclosed` | Hannover Rueck SE | 3.46% |
| 5 | `not disclosed` | Munchener Ruckversicherungs-Gesellschaft AG | 3.45% |
| 6 | `not disclosed` | UPM-Kymmene Oyj | 3.43% |
| 7 | `not disclosed` | UNIPOL ASSICURAZIONI SPA | 3.40% |
| 8 | `not disclosed` | Sanofi SA | 3.31% |
| 9 | `not disclosed` | Elisa Oyj Class A | 3.27% |
| 10 | `not disclosed` | Poste Italiane SpA | 3.17% |

### XETR:ZPRG
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/de/en_gb/intermediary/etfs/state-street-spdr-sp-global-dividend-aristocrats-ucits-etf-dist-zprg-gy`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | Highwoods Properties Inc. | 1.98% |
| 2 | `not disclosed` | Getty Realty Corp. | 1.84% |
| 3 | `not disclosed` | Verizon Communications Inc. | 1.68% |
| 4 | `not disclosed` | Edison International | 1.66% |
| 5 | `not disclosed` | John Wiley & Sons Inc. Class A | 1.64% |
| 6 | `not disclosed` | LTC Properties Inc. | 1.55% |
| 7 | `not disclosed` | Northwest Bancshares Inc. | 1.53% |
| 8 | `not disclosed` | United Parcel Service Inc. Class B | 1.51% |
| 9 | `not disclosed` | Energizer Holdings Inc. | 1.48% |
| 10 | `not disclosed` | ONEOK Inc. | 1.48% |

### ASX:WDIV
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/au/en_gb/intermediary/etfs/state-street-spdr-sp-global-dividend-etf-wdiv`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | Lenovo Group | 2.27% |
| 2 | `not disclosed` | Legal & General Group | 1.81% |
| 3 | `not disclosed` | Altria Group | 1.78% |
| 4 | `not disclosed` | Highwoods Prop | 1.78% |
| 5 | `not disclosed` | Getty Realty | 1.64% |
| 6 | `not disclosed` | Northwest Bancshares | 1.59% |
| 7 | `not disclosed` | Verizon Communications | 1.50% |
| 8 | `not disclosed` | Edison International | 1.49% |
| 9 | `not disclosed` | Apa Group | 1.47% |
| 10 | `not disclosed` | Vanguard International Semiconductor | 1.46% |

### ASX:SYI
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/au/en_gb/intermediary/etfs/state-street-spdr-msci-australia-select-high-dividend-yield-etf-syi`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | Natl Australia Bk | 9.76% |
| 2 | `not disclosed` | Anz Group Hldgs Li | 9.69% |
| 3 | `not disclosed` | Westpac Bkg Corp | 9.42% |
| 4 | `not disclosed` | Telstra Group Ltd | 8.41% |
| 5 | `not disclosed` | Csl Ltd | 8.20% |
| 6 | `not disclosed` | Qbe Ins Group | 5.58% |
| 7 | `not disclosed` | Coles Group Ltd | 4.82% |
| 8 | `not disclosed` | Evolution Mining | 3.51% |
| 9 | `not disclosed` | Santos Limited | 3.45% |
| 10 | `not disclosed` | Suncorp Group Ltd | 3.08% |

### AMEX:DWX
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-international-dividend-etf-dwx`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | TOTALENERGIES SE | 2.52% |
| 2 | `not disclosed` | EVONIK INDUSTRIES AG | 2.00% |
| 3 | `not disclosed` | DCC PLC | 1.98% |
| 4 | `not disclosed` | PEMBINA PIPELINE CORP | 1.89% |
| 5 | `not disclosed` | ORANGE | 1.79% |
| 6 | `not disclosed` | AMBEV SA | 1.78% |
| 7 | `not disclosed` | VEOLIA ENVIRONNEMENT | 1.77% |
| 8 | `not disclosed` | SNAM SPA | 1.73% |
| 9 | `not disclosed` | NEDBANK GROUP LTD | 1.65% |
| 10 | `not disclosed` | ZURICH INSURANCE GROUP AG | 1.64% |

### XETR:ZPRA
- Source: State Street/SPDR official fund page HTML
- URL: `https://www.ssga.com/de/en_gb/intermediary/etfs/state-street-spdr-sp-pan-asia-dividend-aristocrats-ucits-etf-dist-zpra-gy`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | APA Group | 5.93% |
| 2 | `not disclosed` | Bosideng International Holdings Limited | 4.49% |
| 3 | `not disclosed` | Bank of China Limited Class H | 4.37% |
| 4 | `not disclosed` | KrungThai Card Public Co. Ltd. NVDR | 3.87% |
| 5 | `not disclosed` | Industrial and Commercial Bank of China Limited Class H | 3.64% |
| 6 | `not disclosed` | China Communications Services Corp. Ltd. Class H | 3.45% |
| 7 | `not disclosed` | Sonic Healthcare Limited | 3.45% |
| 8 | `not disclosed` | CK Infrastructure Holdings Limited | 3.42% |
| 9 | `not disclosed` | Tsingtao Brewery Co. Ltd. Class H | 3.23% |
| 10 | `not disclosed` | China Merchants Bank Co. Ltd. Class H | 2.61% |

## Additional Verified Holdings Extracted - Batch 2026-07-02A
### Source Patterns Added
- Fidelity Canada official ETF pages expose `window.FidelityAPI.fidelityApiFidcaProductsAPIRootUrl` and `data-fund-axis-code`; holdings are fetched from `https://fidcaproductsapi.fidelity.ca/FidcaProductsAPI/api/fundPage/fund/EN/{axisCode}`. Parsed `FCCD` and `FCID`.
- Fidelity Canada API holdings in this batch disclosed security names and weights but not security tickers, so ticker fields are recorded as `not disclosed`.
- Fidelity U.S. official `FDVV` pages checked in this environment returned temporary unavailable / HTTP 403 responses; `FDVV` remains `pending_source_check` rather than inferred.

### TSX:FCCD
- Source: Fidelity Canada official fundPage holdings API
- URL: `https://fidcaproductsapi.fidelity.ca/FidcaProductsAPI/api/fundPage/fund/EN/FCCD`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | ROYAL BANK OF CANADA | 6.65% |
| 2 | `not disclosed` | TORONTO-DOMINION BANK | 4.74% |
| 3 | `not disclosed` | ENBRIDGE INC | 4.55% |
| 4 | `not disclosed` | MAGNA INTL INC | 3.72% |
| 5 | `not disclosed` | CANADIAN NATL RESOURCES LTD | 3.47% |
| 6 | `not disclosed` | FORTIS INC | 3.46% |
| 7 | `not disclosed` | RESTAURANT BRANDS INTERNATIONAL INC | 3.35% |
| 8 | `not disclosed` | TC ENERGY CORP | 3.18% |
| 9 | `not disclosed` | EMERA INC | 3.09% |
| 10 | `not disclosed` | SUNCOR ENERGY INC | 2.95% |

### TSX:FCID
- Source: Fidelity Canada official fundPage holdings API
- URL: `https://fidcaproductsapi.fidelity.ca/FidcaProductsAPI/api/fundPage/fund/EN/FCID`
- As of: `2026-06-30`

| Rank | Ticker | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `not disclosed` | KLEPIERRE SA | 3.55% |
| 2 | `not disclosed` | SHELL PLC | 3.17% |
| 3 | `not disclosed` | LINK REAL ESTATE INVESTMENT TR | 3.02% |
| 4 | `not disclosed` | TOTALENERGIES SE | 2.99% |
| 5 | `not disclosed` | INVINCIBLE INVESTMENT CORP | 2.86% |
| 6 | `not disclosed` | EQUINOR ASA | 2.74% |
| 7 | `not disclosed` | BHP GROUP LIMITED | 2.63% |
| 8 | `not disclosed` | WOODSIDE ENERGY GROUP LTD | 2.54% |
| 9 | `not disclosed` | HSBC HOLDINGS PLC | 2.40% |
| 10 | `not disclosed` | RIO TINTO PLC | 2.19% |

## Additional Verified Holdings Extracted - Batch 2026-07-02B
### Source Patterns Added
- First Trust official holdings pages expose `Holdings of the Fund` HTML tables; parsed `MDIV`.
- Invesco UCITS product page exposes `productMetaData` with ISIN and a `dng-api.invesco.com` holdings endpoint; parsed `MLPD`.
- Global X Japan official fund page links Solactive PCF/all stock information CSV for `2564`; weights are calculated from official `Shares Amount * Stock Price` per line divided by the sum of stock market values, so these are shown calculations from source inputs rather than source-disclosed weights.
### Lookups Not Yet Resolved

- `AMEX:QDPL`: Pacer official product page `https://www.paceretfs.com/products/qdpl` returned HTTP 403 in this environment; left pending rather than inferred.
- `EURONEXT:TDIV`: Initial VanEck candidate holdings URL returned HTTP 404; left pending until correct official VanEck product URL/API is verified.
- `TSX:RBNK`: RBC official page exposed holdings as-of date but parseable embedded data did not include holdings rows in the extracted `fundData`; left pending rather than inferred.

### NASDAQ:MDIV
- Source: First Trust official holdings page HTML
- URL: `https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=MDIV`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `HYLS` | First Trust Tactical High Yield ETF | 19.64% |
| 2 | `PMT` | PennyMac Mortgage Investment Trust | 1.67% |
| 3 | `AGNC` | AGNC Investment Corp. | 1.61% |
| 4 | `MFA` | MFA Financial, Inc. | 1.60% |
| 5 | `IEP` | Icahn Enterprises, L.P. | 1.53% |
| 6 | `MNR` | Mach Natural Resources LP | 1.50% |
| 7 | `TXO` | TXO Partners, L.P. | 1.49% |
| 8 | `NLY` | Annaly Capital Management, Inc. | 1.47% |
| 9 | `RITM` | Rithm Capital Corp. | 1.21% |
| 10 | `CAPL` | CrossAmerica Partners LP | 1.13% |

### LSE:MLPD
- Source: Invesco official holdings API
- URL: `https://dng-api.invesco.com/cache/v1/accounts/en_GB/shareclasses/IE00B8CJW150/holdings/index?idType=isin`
- As of: `2026-07-01`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `US86765K1097` | SUNOCO UNT | 10.62% |
| 2 | `US55336V1008` | MPLX COM UNT | 10.17% |
| 3 | `US29273V1008` | ENERGY TRANSFER UNT | 10.10% |
| 4 | `US7265031051` | PLAINS ALL AMERICAN PIPELINE UNT | 10.00% |
| 5 | `US2937921078` | ENTERPRISE PRODUCTS PARTNERS UNT | 9.98% |
| 6 | `US9586691035` | WESTERN MIDSTREAM PARTNERS COM UNT | 9.97% |
| 7 | `US24664T1034` | DELEK LOGISTICS PARTNERS COM UNT | 5.11% |
| 8 | `US09225M1018` | BLACK STONE MINERALS UNT | 5.06% |
| 9 | `US37946R1095` | GLOBAL PARTNERS UNT | 4.98% |
| 10 | `US4511001012` | ICAHN ENTERPRISES UNT | 4.95% |

### TSE:2564
- Source: Global X Japan official PCF / Solactive all stock information; weights calculated from shares amount * stock price
- URL: `https://www.solactive.com/downloads/etfservices/tse-pcf/single/2564.csv`
- As of: `2026-07-03`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `7267` | HONDA MOTOR | 4.46% |
| 2 | `5938` | LIXIL GROUP CORP | 4.33% |
| 3 | `8601` | DAIWA SECURITIES GROUP INC ORD | 4.33% |
| 4 | `5451` | YODOGAWA STEEL WORKS LTD | 4.27% |
| 5 | `8616` | TOKAI TOKYO FINANCIAL HOLDINGS ORD | 4.25% |
| 6 | `4023` | KUREHA CORP | 4.13% |
| 7 | `8595` | JAFCO GROUP CO LTD | 4.12% |
| 8 | `7261` | MAZDA MOTOR CORP ORD | 4.09% |
| 9 | `8985` | JAPAN HOTEL REIT INVESTMENT | 4.07% |
| 10 | `4928` | NOEVIR HOLDING CO | 4.07% |

## Additional Verified Holdings Extracted - Batch 2026-07-02C
### Source Patterns Added
- BlackRock/iShares official product-data API was reused only after matching `fundName` to the target ETF; parsed `DVY` and `DPYA`.
- Rejected mismatched iShares regional `portfolioId` candidates for `IUKD`, `EXSB`, `EXSG`, and `EXX5` because the API returned different official fund names; those ETFs remain pending rather than inferred.
- Canada/Australia iShares guessed pages for `XEI` and `IHD` were also rejected because they resolved to different funds (`XRE` and `IOZ`).

### NASDAQ:DVY
- Source: BlackRock/iShares official product-data API, portfolioId 239500
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=en_US&portfolioId=239500&targetSite=us-ishares&userType=individual&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `MO` | ALTRIA GROUP INC | 2.26% |
| 2 | `TROW` | T ROWE PRICE GROUP INC | 2.22% |
| 3 | `PRU` | PRUDENTIAL FINANCIAL INC | 2.01% |
| 4 | `PFE` | PFIZER INC | 1.99% |
| 5 | `OKE` | ONEOK INC | 1.71% |
| 6 | `HPQ` | HP INC | 1.68% |
| 7 | `KMB` | KIMBERLY CLARK CORP | 1.68% |
| 8 | `EIX` | EDISON INTERNATIONAL | 1.63% |
| 9 | `VZ` | VERIZON COMMUNICATIONS INC | 1.62% |
| 10 | `F` | FORD MOTOR CO | 1.58% |

### LSE:DPYA
- Source: BlackRock/iShares official product-data API, portfolioId 251801
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=en_GB&portfolioId=251801&targetSite=uk-ishares&userType=individual&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `PLD` | PROLOGIS REIT INC | 7% |
| 2 | `EQIX` | EQUINIX REIT INC | 6% |
| 3 | `SPG` | SIMON PROPERTY GROUP REIT INC | 4% |
| 4 | `DLR` | DIGITAL REALTY TRUST REIT INC | 4% |
| 5 | `O` | REALTY INCOME REIT CORP | 3% |
| 6 | `PSA` | PUBLIC STORAGE REIT | 3% |
| 7 | `VTR` | VENTAS REIT INC | 2% |
| 8 | `IRM` | IRON MOUNTAIN INC | 2% |
| 9 | `EXR` | EXTRA SPACE STORAGE REIT INC | 2% |
| 10 | `VICI` | VICI PPTYS INC | 2% |


## Additional Verified Holdings Extracted - Batch 2026-07-02D
### Source Patterns Added
- BlackRock/iShares DE official product-data API was scanned by `portfolioId` and accepted only when `fundName` matched the target ETF; parsed `EXSB`, `EXXW`, `EXX5`, `EXSG`, and `IUKD`.
- Additional BlackRock scan for remaining iShares candidates was stopped after no clear matching output in the bounded continuation window; unresolved iShares ETFs remain pending rather than inferred.
- `EXXW` official `fundName` is `iShares Dow Jones Asia Pacific Select Dividend 50 UCITS ETF (DE)`; this corrects the prior universe display name that said Select Dividend 30.

### XETR:EXSB
- Source: BlackRock/iShares official product-data API, portfolioId 251763
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=de_DE&portfolioId=251763&targetSite=de-ishares&userType=privatanleger&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `ALV` | ALLIANZ | 11% |
| 2 | `MUV2` | MUENCHENER RUECKVERSICHERUNGS-GESE | 11% |
| 3 | `DHL` | DEUTSCHE POST AG | 10% |
| 4 | `RWE` | RWE AG | 10% |
| 5 | `EOAN` | E.ON N | 10% |
| 6 | `BAS` | BASF N | 10% |
| 7 | `MBG` | MERCEDES-BENZ GROUP N AG | 9% |
| 8 | `DTG` | DAIMLER TRUCK HOLDING E AG | 6% |
| 9 | `BMW` | BMW AG | 6% |
| 10 | `VNA` | VONOVIA SE | 5% |

### XETR:EXXW
- Source: BlackRock/iShares official product-data API, portfolioId 251764
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=de_DE&portfolioId=251764&targetSite=de-ishares&userType=privatanleger&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `BHP` | BHP GROUP LTD | 9% |
| 2 | `FMG` | FORTESCUE LTD | 5% |
| 3 | `D05` | DBS GROUP HOLDINGS LTD | 5% |
| 4 | `7267` | HONDA MOTOR LTD | 5% |
| 5 | `O39` | OVERSEA-CHINESE BANKING LTD | 4% |
| 6 | `ANZ` | ANZ GROUP HOLDINGS LTD | 4% |
| 7 | `STO` | SANTOS LTD | 4% |
| 8 | `WBC` | WESTPAC BANKING CORPORATION | 3% |
| 9 | `U11` | UNITED OVERSEAS BANK LTD | 3% |
| 10 | `QBE` | QBE INSURANCE GROUP LTD | 3% |

### XETR:EXX5
- Source: BlackRock/iShares official product-data API, portfolioId 251771
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=de_DE&portfolioId=251771&targetSite=de-ishares&userType=privatanleger&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `MO` | ALTRIA GROUP INC | 2% |
| 2 | `TROW` | T ROWE PRICE GROUP INC | 2% |
| 3 | `PRU` | PRUDENTIAL FINANCIAL INC | 2% |
| 4 | `PFE` | PFIZER INC | 2% |
| 5 | `OKE` | ONEOK INC | 2% |
| 6 | `HPQ` | HP INC | 2% |
| 7 | `KMB` | KIMBERLY CLARK CORP | 2% |
| 8 | `EIX` | EDISON INTERNATIONAL | 2% |
| 9 | `VZ` | VERIZON COMMUNICATIONS INC | 2% |
| 10 | `F` | FORD MOTOR CO | 2% |

### XETR:EXSG
- Source: BlackRock/iShares official product-data API, portfolioId 251788
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=de_DE&portfolioId=251788&targetSite=de-ishares&userType=privatanleger&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `ABN` | ABN AMRO BANK NV | 5% |
| 2 | `LIGHT` | SIGNIFY NV | 5% |
| 3 | `OMV` | OMV AG | 5% |
| 4 | `NN` | NN GROUP NV | 4% |
| 5 | `PST` | POSTE ITALIANE | 4% |
| 6 | `ASRNL` | ASR NEDERLAND NV | 4% |
| 7 | `CS` | AXA SA | 4% |
| 8 | `BNP` | BNP PARIBAS SA | 4% |
| 9 | `ACA` | CREDIT AGRICOLE SA | 4% |
| 10 | `RAND` | RANDSTAD HOLDING | 4% |

### LSE:IUKD
- Source: BlackRock/iShares official product-data API, portfolioId 251807
- URL: `https://www.blackrock.com/varnish-api/blk-one01-product-data/product-data/api/v2/get-product-data?appSubType=ISHARES&appType=PRODUCT_PAGE&component=holdings.all&locale=de_DE&portfolioId=251807&targetSite=de-ishares&userType=privatanleger&excludeContent=true&asOfDate=&includeConfig=true`
- As of: `2026-06-30`

| Rank | Ticker / ID | Holding | Weight |
| ---: | --- | --- | ---: |
| 1 | `LGEN` | LEGAL AND GENERAL GROUP PLC | 5% |
| 2 | `BATS` | BRITISH AMERICAN TOBACCO | 5% |
| 3 | `NWG` | NATWEST GROUP PLC | 4% |
| 4 | `HSBA` | HSBC HOLDINGS PLC | 4% |
| 5 | `BP.` | BP PLC | 4% |
| 6 | `AV.` | AVIVA PLC | 4% |
| 7 | `RIO` | RIO TINTO PLC | 4% |
| 8 | `ADM` | ADMIRAL GROUP PLC | 3% |
| 9 | `LLOY` | LLOYDS BANKING GROUP PLC | 3% |
| 10 | `SDLF` | STANDARD LIFE PLC | 3% |


## Next Extraction Queue

- Resolve official issuer holdings endpoints for Vanguard, State Street SPDR, WisdomTree, ProShares, Invesco, Fidelity, First Trust, VanEck, ALPS, Global X, and regional exchanges.
- For every ETF, set one of: `official_holdings_found`, `official_lookup_failed`, or `source_not_available_after_check`; do not infer Top 10 holdings from fund name.
