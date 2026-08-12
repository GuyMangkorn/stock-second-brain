---
type: etf-performance-source-batch
workflow: check-etf-performance
tickers:
  - SPSM
  - VBR
mode: lean
run_date: 2026-08-12
return_basis: NAV total return
benchmark_basis: S&P 500 Total Return, USD, dividends reinvested
review_status: PASS after project-scoped source_verifier
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
