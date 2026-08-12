---
type: etf-performance-source-batch
workflow: check-etf-performance
tickers:
  - SPSM
  - VBR
  - VSS
  - IJR
mode: lean
run_date: 2026-08-12
return_basis: NAV total return
benchmark_basis: S&P 500 Total Return, USD, dividends reinvested
review_status: PASS; VSS and IJR local checklist fallback after source_verifier timeout
---

# SPSM Performance Sources — 2026-08-12

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-600-small-cap-etf-spsm | Official issuer product page | accessed 2026-08-12; price/NAV 2026-08-11; performance 2026-06-30 | identity, exchange, inception/listing, benchmark, expense ratio, NAV/price, premium/discount, AUM, distribution frequency, period NAV TR |
| https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-spsm.pdf | Official issuer factsheet | 2026-06-30 | fund facts, passive objective, standardized performance, return definitions |
| https://www.spglobal.com/spdji/en/indices/equity/sp-600/ | Official index provider | accessed 2026-08-12 | S&P SmallCap 600 benchmark context |
| https://www.spglobal.com/spdji/en/methodology/article/sp-us-indices-methodology/ | Official index methodology | accessed 2026-08-12 | float-adjusted market-cap weighting and rebalancing context |
| https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official index provider | accessed 2026-08-12 | S&P 500 Total Return benchmark definition |

## Verified observations

- Canonical identity: `NYSE Arca:SPSM`; State Street SPDR Portfolio S&P 600 Small Cap ETF; passive/index-tracking U.S. small-cap equity exposure; inception 2013-07-08; listing date 2013-07-09.
- Issuer benchmark: S&P SmallCap 600 Index; historical benchmark labels changed from Russell 2000 through 2017-11-16 and SSGA Small Cap Index through 2020-01-24 before S&P SmallCap 600.
- Gross/net expense ratio: `0.03%`; quarterly distributions.
- NAV: `US$57.68`; bid/ask midpoint `US$57.70`; closing price `US$57.69`; official premium/discount `+0.02%`; AUM `US$17,250.35M`; all as of 2026-08-11.
- Official NAV Total Return as of 2026-06-30: 1-month `7.28%`, QTD `19.67%`, YTD `23.89%`, 1-year `37.47%`, 3-year annualized `16.02%`, 5-year annualized `7.34%`, 10-year annualized `11.61%`, since-inception annualized `10.31%`.
- Corresponding issuer benchmark returns: 1-month `7.29%`, QTD `19.70%`, YTD `23.90%`, 1-year `37.50%`, 3-year annualized `16.05%`, 5-year annualized `7.37%`, 10-year annualized `11.65%`, since-inception annualized `10.32%`.
- Tracking differences calculated as fund NAV TR minus issuer benchmark: `-0.01 pp` YTD, `-0.03 pp` 1-year, `-0.03 pp` 3-year, `-0.03 pp` 5-year, `-0.04 pp` 10-year, `-0.01 pp` since inception.
- All fund returns are USD total returns with distributions/capital gains reinvested and net of fees; index returns are unmanaged and do not deduct fees.

## Cached benchmark

- S&P 500 Total Return cache: complete calendar years 2016-2025, USD, dividends reinvested, reference as-of 2025-12-31. Rows: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; cumulative `298.33%`, cached CAGR `14.82%`.
- Cached source URLs: https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/; https://www.spglobal.com/spdji/en/indices/equity/sp-500/.

## Calculations and gaps

- No SPSM calendar-year NAV TR CAGR, best/worst year, up/down count, volatility, max drawdown, or recovery calculation was performed because the reviewed issuer capture did not disclose complete annual NAV rows or daily NAV history.
- The official issuer 10-year annualized field `11.61%` is retained as a source fact. Raw 10-year endpoints and exact elapsed years were not disclosed; no endpoint-derived CAGR or normalized cumulative return is asserted.
- Current issuer YTD `23.89%` is as of 2026-06-30; newer price/NAV facts are as of 2026-08-11, so the dates are intentionally separate.
- Direct prospectus PDF URL and prospectus calendar-return table were not exposed by the issuer document viewer; the issuer product page and factsheet remain the primary evidence.
- No new web verification was performed for cached S&P 500 TR rows; they were reused under the project cache convention.

## Planned durable outputs

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_SPSM Performance.md` as the numeric source of truth with the complete candidate content supplied in the review packet.
- Update `wiki/analysis/comparisons/USA ETF.md` with SPSM and increase USA count in `wiki/analysis/comparisons/ETF Region Index.md` from 19 to 20.
- Update `wiki/analysis/performance/ETF Performance Index.md` with SPSM coverage; no common-window row because annual SPSM rows are not disclosed.
- Append one `etf-performance` bullet to `log.md`.
- Add the breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]` and canonical `geography/United-States` tag; no duplicate performance page is planned.

## Review record

- Project-scoped `source_verifier` returned `PASS` after correcting the issuer URL in the source map; the complete review packet preserved the disclosed gaps and separate as-of dates.

# VBR Performance Sources — 2026-08-12

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| https://institutional.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F0937.pdf | Official Vanguard factsheet | 2026-06-30 | identity, inception, passive structure, benchmark, expense ratio, rolling NAV TR, YTD, market-price YTD |
| https://investor.vanguard.com/investment-products/etfs/profile/vbr | Official Vanguard performance/quote page | annual rows 2025-12-31; quote 2026-06-18 | 2016-2025 NAV Total Return rows and quote price/NAV inputs |
| https://www.sec.gov/Archives/edgar/data/36405/000110465926021502/R2.htm | SEC shareholder report | accessed 2026-08-12 | fund/benchmark and reporting context |
| https://www.sec.gov/Archives/edgar/data/36405/000168386323004080/f25242d1.htm | SEC prospectus | accessed 2026-08-12 | passive/full-replication structure and benchmark context |

## Verified observations

- Canonical identity: `NYSE Arca:VBR`; Vanguard Small-Cap Value ETF; passive, full-replication U.S. small-cap value equity ETF; inception 2004-01-26; USD.
- Issuer benchmark: CRSP US Small Cap Value Index; Bloomberg ticker `CRSPSCVT`.
- Expense ratio: `0.05%` as of 2026-06-30.
- Official VBR NAV Total Return annual rows as of 2025-12-31: 2016 `24.80%`, 2017 `11.79%`, 2018 `-12.22%`, 2019 `22.76%`, 2020 `5.82%`, 2021 `28.07%`, 2022 `-9.29%`, 2023 `16.00%`, 2024 `12.39%`, 2025 `9.09%`.
- Official Vanguard period-ended-2026-06-30 returns: NAV YTD `15.83%`, 1-year `27.01%`, 3-year annualized `16.08%`, 5-year annualized `9.23%`, 10-year annualized `10.99%`, since-inception annualized `9.51%`; benchmark YTD `15.86%`; market-price YTD `15.92%`.
- Latest captured Vanguard quote: market price `US$238.40`, NAV `US$238.46`, quote date 2026-06-18; price/NAV discount calculated as `(238.40 / 238.46) - 1 = -0.025%`, displayed as `-0.03%`; source is the Vanguard VBR profile page.

## Calculations

- Using the published rounded annual NAV returns: 2016-2025 cumulative `162.85%`, CAGR `10.15%`; 2021-2025 cumulative `65.22%`, CAGR `10.56%`.
- Formula: `Π(1 + annual return) - 1`; CAGR = `(1 + cumulative return)^(1 / years) - 1`.
- S&P 500 cached common reference 2016-2025: cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.

## Gaps and reconciliation

- The rolling 10-year issuer annualized return `10.99%` is a separate period-ended-2026-06-30 observation from the 2016-2025 calendar CAGR `10.15%`; the page labels both windows and does not mix them.
- The reviewed Vanguard factsheet names CRSP US Small Cap Value Index. Any later benchmark-name change or effective date is not disclosed in this evidence packet; no rebranding conclusion is made.
- No newer official price/NAV quote than 2026-06-18 was captured; current YTD performance is available through 2026-06-30.
- Max drawdown, recovery, and volatility were not calculated because daily NAV history was not supplied.

## Cached benchmark

- S&P 500 TR cache: 2016-2025 complete calendar years, USD, dividends reinvested, reference as-of 2025-12-31; rows and source URLs are retained in the SPSM section above and reused here under the project cache convention.

## Review record

- Project-scoped `source_verifier` returned `PASS` after the corrections above; durable VBR outputs were written only after `PASS`.

# VSS Performance Sources — 2026-08-12

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| https://advisors.vanguard.com/investments/products/vss/vanguard-ftse-all-world-ex-us-small-cap-etf | Official Vanguard product/quote page | accessed 2026-08-12; annual performance 2025-12-31; rolling return 2026-07-31; price/NAV and YTD 2026-08-11 | identity, exchange, fund facts, benchmark, expense ratio, official annual NAV TR, rolling annualized NAV TR, current price/NAV, NAV and market-price YTD |
| https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3184.pdf | Official Vanguard factsheet | 2026-03-31; fee effective 2026-02-27 | passive index-sampling structure, NAV TR definition, expense ratio, standard deviation and risk disclosures |
| https://fund-docs.vanguard.com/p3184.pdf | Official Vanguard prospectus | 2026-02-27 | legal fund identity, benchmark and policy context |
| https://totalrealreturns.com/n/VSS | Secondary total-return history | data ending 2026-08-10 | price-based dividend-reinvested drawdown proxy only; not NAV Total Return |

## Verified observations

- Canonical identity: `NYSE Arca:VSS`; Vanguard FTSE All-World ex-US Small-Cap ETF; passive/index-tracking equity ETF using index sampling; inception `2009-04-02`.
- Issuer benchmark: `FTSE Global Small Cap ex US Index (TGPVA09U)`; expense ratio `0.06%` as of `2026-02-27`.
- Official NAV Total Return is USD, pre-tax, net of fund expenses, with dividends and capital-gains distributions reinvested.
- Current official closing market price: `US$158.81`; NAV: `US$158.05`; calculated premium `0.48%`; current NAV YTD `+10.86%` and market-price YTD `+11.40%`, all as of `2026-08-11`.
- Official rolling 10-year NAV TR average annual return: `7.42%` as of `2026-07-31`; raw TR endpoints and exact endpoint-derived cumulative value were not disclosed.
- Official three-year standard deviation: VSS `13.76%` versus issuer benchmark `14.26%`, based on monthly returns as of `2026-03-31`.

## Official annual NAV Total Return inputs

| Year | VSS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 4.37% | 11.96% |
| 2017 | 30.26% | 21.83% |
| 2018 | -18.43% | -4.38% |
| 2019 | 21.73% | 31.49% |
| 2020 | 11.95% | 18.40% |
| 2021 | 12.81% | 28.71% |
| 2022 | -21.22% | -18.11% |
| 2023 | 15.25% | 26.29% |
| 2024 | 2.67% | 25.02% |
| 2025 | 29.99% | 17.88% |

VSS rows are official complete-calendar-year NAV TR as of `2025-12-31`.
S&P 500 rows reuse the cached USD Total Return convention, dividends reinvested,
with reference as-of `2025-12-31`; no new benchmark search was run.

## Calculations and risk

- VSS 2016-2025 cumulative: `106.58%`; CAGR: `7.53%`; up/down: `8 / 2`.
- VSS 2021-2025 cumulative: `36.70%`; CAGR: `6.45%`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`; 2021-2025: `96.17%` / `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR `= product(1 + annual TR)^(1 / years) - 1`.
- Secondary price total-return history reports worst drawdown `-43.51%` on `2020-03-23` from the `2018-01-26` peak, and current drawdown `-2.11%` from the `2026-05-11` peak, with data ending `2026-08-10`. This is not NAV-specific.
- Official NAV maximum drawdown and recovery date: `ไม่พบข้อมูลที่ยืนยันได้`; no recovery date is inferred.

## Benchmark cache sources

- https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true
- https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf
- https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/
- https://www.spglobal.com/spdji/en/indices/equity/sp-500/

## VSS Review record

- Project-scoped `source_verifier` was dispatched but did not return a verdict after bounded wait. The main agent completed the documented local checklist fallback on 2026-08-12; no critical/high findings remained, and no source research was substituted locally.

# IJR Performance Sources — 2026-08-12

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| https://www.ishares.com/us/products/239774/ishares-core-sp-smallcap-etf?fundSearch=true&qt=IJR | Official iShares product page | accessed 2026-08-12; price/NAV 2026-08-11; NAV YTD 2026-08-10 | identity, exchange, benchmark, inception, expense ratio, current NAV/price, premium/discount, current NAV YTD |
| https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-s-and-p-small-cap-etf-3-31.pdf | Official iShares summary prospectus | 2026-07-31 | passive representative-sampling structure, official 2016-2025 annual NAV TR, return definition, fund facts |
| https://www.ishares.com/us/literature/fact-sheet/ijr-ishares-core-s-p-small-cap-etf-fund-fact-sheet-en-us.pdf | Official iShares factsheet | 2026-07-31 | 2021-2025 annual NAV TR corroboration and 3-year standard deviation |
| https://totalrealreturns.com/s/IJR | Secondary total-return history | data ending 2026-08-12 | inflation-adjusted dividend-reinvested drawdown context only |
| https://assetsanalyzer.com/etf/IJR/performance | Secondary performance history | accessed 2026-08-12 | alternate drawdown/recovery context; methodology differs and is not authoritative NAV |

## Verified observations

- Canonical identity: `NYSE Arca:IJR`; iShares Core S&P Small-Cap ETF, an equity passive index-tracking fund using representative sampling; inception `2000-05-22`; issuer benchmark `S&P SmallCap 600 Index`; expense ratio `0.06%`; currency USD.
- Official NAV Total Return includes reinvested dividends/distributions and reflects fund expenses. Complete calendar-year observations are through `2025-12-31`.
- Current official NAV: `US$148.34`; closing market price: `US$148.41`; calculated premium `0.05%`; all as of `2026-08-11`.
- Current official NAV YTD Total Return: `+23.66%` as of `2026-08-10`.
- Official three-year standard deviation: `19.36%` as of `2026-07-31`; official best quarter `+31.29%` (2020-12-31) and worst quarter `-32.65%` (2020-03-31).

## Official annual NAV Total Return inputs

| Year | IJR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 26.49% | 11.96% |
| 2017 | 13.20% | 21.83% |
| 2018 | -8.43% | -4.38% |
| 2019 | 22.79% | 31.49% |
| 2020 | 11.24% | 18.40% |
| 2021 | 26.69% | 28.71% |
| 2022 | -16.20% | -18.11% |
| 2023 | 16.03% | 26.29% |
| 2024 | 8.61% | 25.02% |
| 2025 | 5.95% | 17.88% |

IJR rows are official complete-calendar-year NAV TR from the iShares summary
prospectus, periods ended `2025-12-31`; 2021-2025 rows are corroborated by the
official factsheet. S&P 500 rows reuse the cached USD Total Return convention,
dividends reinvested, reference as-of `2025-12-31`; no new benchmark search was run.

## Calculations and risk

- IJR 2016-2025 cumulative: `153.87%`; CAGR: `9.76%`; up/down: `8 / 2`.
- IJR 2021-2025 cumulative: `41.75%`; CAGR: `7.23%`.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%`; 2021-2025: `96.17%` / `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; CAGR `= product(1 + annual TR)^(1 / years) - 1`.
- Secondary inflation-adjusted dividend-reinvested history reports maximum drawdown `-58.94%` on `2009-03-09` from the `2007-07-19` peak.
- AssetsAnalyzer reports an alternate `-58.15%` drawdown and 484 trading sessions to recovery; methodologies differ, so no nominal NAV max-drawdown/recovery figure is treated as authoritative.

## Benchmark cache sources

- https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true
- https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf
- https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/
- https://www.spglobal.com/spdji/en/indices/equity/sp-500/

## IJR Review record

- Project-scoped `source_verifier` was dispatched but did not return a verdict after bounded wait. The main agent completed the documented local checklist fallback on 2026-08-12; no critical/high findings remained, and no source research was substituted locally.
