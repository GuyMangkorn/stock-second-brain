---
type: source-batch
topic: ETF performance
accessed: 2026-07-24
input_source: raw/imports/tradingview_etf_list_filtered_2026-07-22.md
input_count: 125
review_gate: local_fallback_pass
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-07-24

## Scope and gate

ใช้ `check-etf-performance` sequential queue ต่อเนื่องตามลำดับทีละ ticker. รอบนี้รวมผลถึง row `62/125`, ทำ mandatory 10-year coverage audit จาก official product page/factsheet/presentation/prospectus และใช้ local pre-save fallback เนื่องจากไม่มี independent reviewer.

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Source URL | Gap / resolution note |
|---|---|---|---|---|---|---|
| FLKR | supported | NYSE Arca:FLKR | South Korea | 86.35% (2026-07-07) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26353/SINGLCLASS/franklin-ftse-south-korea-etf/FLKR | official inception 2017-11-02; issuer 10-year NAV return `—`; available official annual rows 2018-2025 |
| VPL | supported | NYSE Arca:VPL | Asia-Pacific | 19.62% (2026-07-17) | https://investor.vanguard.com/investment-products/etfs/profile/vpl | official rolling 10Y NAV TR 177.37% / CAGR 10.74% as of 2026-05-31; annual NAV TR rows 2016-2025 |
| ISSSF | supported | LSE:SAUS | Australia | 10.27% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/251851/ishares-msci-australia-ucits-etf | OTC alias; official rolling 10Y NAV TR 121.17% / CAGR 8.26% as of 2026-06-30; annual NAV TR rows 2016-2025 |
| SCJ | supported | NYSE Arca:SCJ | Japan | 16.10% (2026-07-21) | https://www.ishares.com/us/products/239666/ishares-msci-japan-smallcap-etf | official rolling 10Y NAV TR 119.60% / CAGR 8.18% as of 2026-06-30; annual NAV TR rows 2016-2025 |
| EEMA | supported | NASDAQ:EEMA | Emerging Markets | 20.51% (2026-07-22) | https://www.ishares.com/us/products/239629/ishares-msci-emerging-markets-asia-etf | official rolling 10Y NAV TR 172.29% / CAGR 10.54% as of 2026-06-30; official NAV rows 2016-2025; index change on 2018-06-01 |
| VNFGF | supported | LSE:VDJP | Japan | 16.30% (2026-05-31) | https://www.vanguard.co.uk/professional/product/etf/equity/9504/ftse-japan-ucits-etf-usd-distributing | OTC alias resolved to USD LSE ticker VDJP by ISIN IE00B95PGT31; official rolling 10Y NAV TR CAGR 9.45% as of 2026-05-31; official rolling 12-month rows; current-page NAV US$50.23 as of 2026-07-22 |
| CSKRF | supported | LSE:CSKR | South Korea | 70.53% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/253733/cskr | OTC alias; official rolling 10Y NAV TR cumulative 369.63% / CAGR 16.73% as of 2026-06-30; official calendar NAV rows 2016-2025; benchmark change 2020-02-11 |
| GSJY | supported | NYSE Arca:GSJY | Japan | 12.86% (2026-06-30) | https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e | official rolling 10Y NAV TR CAGR 9.29% as of 2026-06-30; official calendar NAV/ActiveBeta index rows 2017-2025; 2016 inception partial; rules-based index and not actively managed |
| IHSEF | supported | LSE:IAPD | Asia-Pacific | 14.55% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/251567/iapd?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official LSE:IAPD listing; official rolling 10Y NAV TR CAGR 6.75% as of 2026-06-30; official calendar NAV/benchmark rows 2016-2025; physical/replicated passive equity; TER 0.59% |
| MINV | unsupported ETF type | NYSE Arca:MINV | Asia | not applicable | https://us.matthewsasia.com/funds/etfs/asia-innovators-active-etf/ | Matthews identifies MINV as an active, high-conviction, all-cap fundamental equity ETF; active share 74.8% as of 2026-06-30; passive ETF scope excludes active funds |
| IMSCF | supported | LSE:CJPU | Japan | 12.11% (2026-07-17) | https://www.ishares.com/uk/professional/en/products/253732/ishares-msci-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official LSE:CJPU USD listing; official rolling 10Y NAV TR CAGR 9.46% as of 2026-06-30; official calendar NAV/benchmark rows 2016-2025; physical/replicated passive equity; TER 0.12% |
| IHRMF | supported | LSE:IJPU | Japan | 15.45% (2026-07-22) | https://www.ishares.com/uk/professional/en/products/251866/ijpn?siteEntryPassthrough=true | OTC alias resolved to official LSE:IJPU USD listing; official rolling 10Y NAV TR CAGR 9.36% as of 2026-06-30; official calendar NAV/benchmark rows 2016-2025; physical/replicated passive equity; TER 0.12% |
| EWJV | supported | NASDAQ:EWJV | Japan | 18.04% (2026-07-22) | https://www.ishares.com/us/products/307263/ishares-msci-japan-value-etf | official inception 2019-03-05; official 10-year field unavailable; available official since-inception NAV TR annualised 12.13% as of 2026-06-30; official 2021-2025 rows; passive index-tracking value equity |
| VGUDF | supported | LSE:VDPX | Asia-Pacific | not disclosed | https://www.vanguard.co.uk/professional/product/etf/equity/9522/ftse-developed-asia-pacific-ex-japan-ucits-etf-usd-distributing | OTC alias resolved to official USD-distributing share class ISIN IE00B9F5YL18 / LSE:VDPX; official 10Y NAV TR CAGR 8.80% for 2016-03-31 to 2026-03-31; calendar NAV rows 2016-2025; current YTD not disclosed in reviewed official capture |
| INDA | supported | Cboe BZX:INDA | India | -10.12% (2026-07-20) | https://www.ishares.com/us/products/239659/ishares-msci-india-etf | official rolling 10Y NAV TR cumulative 98.09% / CAGR 7.07% as of 2026-06-30; official calendar NAV/benchmark rows 2021-2025; 2016-2020 calendar rows not disclosed; current YTD -10.12% as of 2026-07-20 |
| KDEF | supported | NYSE Arca:KDEF | South Korea | -8.13% (2026-06-30) | https://plusetf.com/kdef | official inception 2025-02-05; 10-year NAV TR unavailable; official since-inception NAV TR cumulative 105.69% / annualized 67.39% as of 2026-06-30; complete-calendar annual NAV rows not disclosed |
| ENZL | supported | NASDAQ:ENZL | New Zealand | 3.45% (2026-07-21) | https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239672&seoSlug=ishares-msci-new-zealand-capped-etf | official rolling 10Y NAV TR cumulative 38.78% / CAGR 3.33% as of 2026-06-30; official calendar NAV rows 2021-2025; 2016-2020 and annual benchmark rows not disclosed; current YTD 3.45% as of 2026-07-21 |
| FJP | supported | NASDAQ:FJP | Japan | 14.26% (2026-06-30) | https://www.ftportfolios.com/Retail/etf/etfsummary.aspx?Ticker=FJP | official rolling 10Y NAV TR CAGR 7.55% as of 2026-06-30; official calendar NAV rows 2016-2025; 2021-2025 CAGR 8.38%; current YTD 14.26% as of 2026-06-30; index changed 2015-07-14 |
| NFTY | supported | NASDAQ:NFTY | India | -7.45% (2026-06-30) | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=NFTY | official rolling 10Y NAV TR CAGR 7.99% for 2016-06-30 to 2026-06-30; raw endpoints not disclosed; official calendar NAV rows 2016-2025; 2021-2025 CAGR 10.83%; index changed 2018-04-17; current YTD -7.45% as of 2026-06-30 |
| FLJH | supported | NYSE Arca:FLJH | Japan | 22.91% (2026-07-07) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26355/SINGLCLASS/franklin-ftse-japan-hedged-etf/FLJH | official inception 2017-11-02; 10-year NAV TR unavailable; official available-period NAV TR annualized 13.63% through 2026-03-31; official calendar NAV rows 2018-2025; current YTD 22.91% as of 2026-07-07 |
| GXC | supported | NYSE Arca:GXC | China | -10.99% (2026-06-30) | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-china-etf-gxc | official rolling 10Y NAV TR CAGR 4.37% for 2016-06-30 to 2026-06-30; raw endpoints and annual NAV rows not disclosed in reviewed capture; current YTD -10.99% as of 2026-06-30 |
| JPAN | unsupported ETF type | NYSE Arca:JPAN | Japan | not applicable | https://us.matthewsasia.com/funds/etfs/japan-active-etf/ | Matthews identifies JPAN as a high-conviction, unconstrained all-cap fundamental active Japan ETF; outside passive/index-tracking equity scope; no performance page created |
| EPI | supported | NYSE Arca:EPI | India | -7.91% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/epi | official rolling 10Y NAV TR CAGR `9.18%` for 2016-06-30 to 2026-06-30; official 2016-2025 NAV rows; 2021-2025 CAGR `11.52%`; current NAV TR YTD `-7.91%` as of 2026-06-30 |
| ASHS | supported | NYSE Arca:ASHS | China | 3.36% (2026-03-31) | https://etf.dws.com/download/asset/1bfed1b5-c933-4199-bdcc-30b0ed651740 | official rolling 10Y NAV TR CAGR `1.96%` for 2016-03-31 to 2026-03-31; annual NAV/index rows not disclosed in reviewed official capture; current NAV TR YTD `3.36%` as of 2026-03-31; 2026-06-30 current YTD not disclosed |
| PGJ | supported | NASDAQ:PGJ | China | not disclosed | https://www.invesco.com/us/en/financial-products/etfs/invesco-golden-dragon-china-etf.html | official rolling 10Y NAV TR CAGR `0.35%` for 2015-12-31 to 2025-12-31; official 2016-2025 NAV/index/benchmark rows; 2021-2025 CAGR `-12.65%`; current 2026 NAV TR YTD not disclosed |
| VFJUF | supported | LSE:VJPU | Japan | 19.41% (2026-05-31) | https://www.vanguard.co.uk/professional/product/etf/equity/9541/ftse-japan-ucits-etf-usd-hedged-accumulating | OTC alias resolved to Vanguard FTSE Japan UCITS ETF USD Hedged Accumulating; official inception `2020-01-31`, `10-year NAV TR unavailable`; available-period NAV TR CAGR `20.29%` for 2020-01-31 to 2026-05-31; rolling 12-month NAV rows disclosed; current 2026-07-22 YTD not disclosed |
| MCHS | unsupported ETF type | NASDAQ:MCHS | China | not applicable | https://www.matthewsasia.com/funds/etfs/china-innovators-active-etf/ | Matthews identifies MCHS as an active/fundamental China equity ETF; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| IPAC | supported | NYSE Arca:IPAC | Asia-Pacific | 13.75% (2026-07-22) | https://www.ishares.com/us/products/264619/ishares-core-msci-pacific-etf | official rolling 10Y NAV TR cumulative 141.81% / CAGR 9.23% for 2016-06-30 to 2026-06-30; official annual NAV/benchmark rows 2021-2025; 2016-2020 annual rows not disclosed; current YTD 13.75% as of 2026-07-22 |
| ASIA | unsupported ETF type | NYSE Arca:ASIA | Asia-Pacific | not applicable | https://www.matthewsasia.com/funds/etfs/pacific-tiger-active-etf/ | Matthews identifies ASIA as Pacific Tiger Active ETF with a high-conviction, all-cap fundamental approach; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| VFPAF | supported | LSE:VAPU | Asia-Pacific | 47.09% (2026-06-30) | https://www.vanguard.co.uk/uk-fund-directory/product/etf/equity/9676/ftse-developed-asia-pacific-ex-japan-ucits-etf-usd-accumulating | OTC alias resolved to official USD LSE ticker VAPU for ISIN IE00BK5BQZ41; share-class inception 2019-09-24 means 10-year NAV TR unavailable; official available-period NAV TR CAGR 13.96% through 2026-06-30; rolling 12-month rows disclosed; current 2026-07-22 YTD not disclosed |
| NBCE | unsupported ETF type | NYSE Arca:NBCE | China | not applicable | https://www.nb.com/products/etfs/china-equity-etf | Neuberger identifies NBCE as an actively managed China equity ETF using fundamental/security-selection research; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| JPY | unsupported ETF type | NASDAQ:JPY | Japan | not applicable | https://www.lazardassetmanagement.com/us/en_us/investment-solutions/how-to-invest/etfs/japanese-equity-etf | Lazard identifies JPY as an actively managed Japanese equity ETF using bottom-up stock selection and fundamental research; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| FPA | supported | NASDAQ:FPA | Asia-Pacific | 42.71% (2026-06-30) | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FPA | official rolling 10Y NAV TR CAGR 10.31% for 2016-06-30 to 2026-06-30; official 2016-2025 NAV rows from prospectus compound to 89.03% / CAGR 6.57%; 2021-2025 CAGR 7.23%; index changed 2015-10-13; current standardized YTD 42.71% as of 2026-06-30 |
| CXSE | supported | NASDAQ:CXSE | China | -3.69% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/cxse | passive/index-tracking China equity ETF; official rolling 10Y NAV TR CAGR 6.85% for 2016-06-30 to 2026-06-30; official 2016-2025 NAV rows compound to 82.98% / CAGR 6.23%; 2021-2025 CAGR -8.00%; 2015-07-01 objective/index change disclosed; current standardized YTD -3.69% as of 2026-06-30 |
| ADVE | unsupported ETF type | NYSE Arca:ADVE | Asia | not applicable | https://us.matthewsasia.com/funds/etfs/asia-dividend-active-etf/ | Matthews identifies ADVE as an unconstrained all-cap active Asia equity ETF with a quality bias; official strategy requires at least 80% in dividend-paying equity securities; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| FLAX | supported | NYSE Arca:FLAX | Asia ex Japan | 24.71% (2026-06-30) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26346/SINGLCLASS/franklin-ftse-asia-ex-japan-etf/FLAX | passive/index-tracking Asia ex Japan equity ETF; official inception 2018-02-06; 10-year field `—`; available-period NAV TR CAGR 7.85% for 2018-02-06 to 2026-06-30; official 2019-2025 NAV rows compound to 77.17% / CAGR 8.51%; current standardized YTD 24.71% |
| VGDTF | supported | XETRA:VJPA | Japan | 15.27% (2026-06-30) | https://www.vanguard.co.uk/professional/product/etf/equity/9674/vanguard-ftse-japan-ucits-etf-usd-accumulating | OTC alias cross-checked to Vanguard FTSE Japan UCITS ETF (USD) Accumulating, ISIN IE00BFMXYX26; official Deutsche Börse EUR line VJPA; passive physical/index-tracking equity; inception 2019-09-24; 10-year field `—`; since-inception NAV TR CAGR 9.96%; official KIID 2020-2025 calendar rows; current standardized YTD 15.27% |
| RAYJ | unsupported ETF type | NYSE Arca:RAYJ | Japan | not applicable | https://funds.rayliant.com/rayj/ | Rayliant identifies RAYJ as an active Japan equity strategy using SMDAM fundamental research and Rayliant quantitative models; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| THD | supported | NYSE Arca:THD | Thailand | 25.53% (2026-07-22) | https://www.ishares.com/us/products/239688/ishares-msci-thailand-capped-etf | passive/index-tracking equity ETF; official rolling 10Y NAV TR CAGR 3.35% for 2016-06-30 to 2026-06-30 (`10.00` years); 2021-2025 NAV rows compound to -10.24% / CAGR -2.14%; 2016-2020 annual rows and raw rolling endpoints not disclosed; benchmark/index change 2013-02-12 |
| FLIN | supported | NYSE Arca:FLIN | India | -8.34% (2026-06-30) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26348/SINGLCLASS/franklin-ftse-india-etf/FLIN | passive/index-tracking equity ETF; inception 2018-02-06; official 10-year field `—`; available-period NAV TR annualized 5.91% for 2018-02-06 to 2026-06-30 (`8.39` years); 2019-2025 NAV rows compound to 88.74% / CAGR 9.50%; 2021-2025 CAGR 9.33%; current standardized NAV TR YTD -8.34% |
| CNYA | supported | Cboe BZX:CNYA | China | 5.39% (2026-07-21) | https://www.ishares.com/us/products/273318/ishares-msci-china-a-etf | passive/index-tracking China A-share equity ETF; official rolling 10Y NAV TR cumulative 91.51% / CAGR 6.71% for 2016-06-30 to 2026-06-30; official 2021-2025 NAV/benchmark rows; 2016-2020 annual rows not disclosed; current NAV TR YTD 5.39% as of 2026-07-21; benchmark change 2018-04-26 |
| CETFF | supported | LSE:CEMA | Emerging Markets | 28.17% (2026-06-30) | https://www.ishares.com/uk/professional/en/products/253723/ishares-msci-em-asia-ucits-etf?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official iShares MSCI EM Asia UCITS ETF USD (Acc), ISIN IE00B5L8K969 / LSE:CEMA; official rolling 10Y NAV TR cumulative 185.06% / CAGR 11.04% as of 2026-06-30; official calendar rows 2016-2025 |

## CSKRF Sequential Queue Record

- Input row: `27/125`; input ticker: `CSKRF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:CSKR`; iShares' official product page maps ISIN `IE00B5W4TY14` to London Stock Exchange USD ticker `CSKR`, identifies the share class as iShares MSCI Korea UCITS ETF USD (Acc), issuing company iShares VII plc, physical/replicated, benchmark MSCI Korea 20/35 Index, and launch `2010-08-24`. `CSKRF` is retained as the input OTC alias; no provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had stale YTD and no benchmark, inception, rolling 10-year result, or annual table. Rechecking the current official product page, March 2026 factsheet and official annual-report/document links confirms a genuine `10.00` elapsed-year NAV TR window; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `369.63%` and average annual `16.73%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `469.63`; raw NAV endpoints are not disclosed.
- Official calendar observations: iShares publishes NAV and benchmark rows for `2016-2025`. NAV rows compound to `141.88%` / CAGR `9.23%`; common `2021-2025` rows compound to `21.32%` / CAGR `3.94%`; positive / negative years are `2 / 3`. S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`.
- Benchmark caveat: iShares states that the benchmark changed from MSCI Korea Index to MSCI Korea 20/35 Index on `2020-02-11`; benchmark rows are kept separate from the fund NAV TR metric.
- Official current observation: iShares reports NAV `US$462.74` and NAV Total Return YTD `70.53%` as of `2026-07-21`; total expense ratio `0.65%`, 77 holdings as of `2026-07-20`, and 3-year standard deviation `44.57%` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CSKRF / CSKR Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:CSKR` | [iShares CSKR product and performance page](https://www.ishares.com/uk/professional/en/products/253733/cskr) | Canonical listing, ISIN/share class, fund identity, physical/replicated classification, benchmark, inception, annual NAV/benchmark rows, rolling 10Y NAV TR, current NAV/YTD, fees and risks | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-21`; holdings `2026-07-20` |
| `LSE:CSKR` | [iShares CSKR factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/cskr-ishares-msci-korea-ucits-etf-usd-acc-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | Corroborates passive/physical/replicated structure, benchmark change, launch date, fee, NAV basis and risk disclosures | Factsheet March 2026; performance data through `2026-03-31` |
| `iShares VII plc` | Official annual report/document links on the CSKR product page | Legal structure and document cross-check | Page accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CSKRF / CSKR Raw Observations And Calculations

| Year | CSKR NAV TR | MSCI Korea benchmark TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 8.0% | 8.7% | 11.96% |
| 2017 | 46.4% | 47.3% | 21.83% |
| 2018 | -21.4% | -20.9% | -4.38% |
| 2019 | 11.8% | 12.5% | 31.49% |
| 2020 | 43.5% | 44.7% | 18.40% |
| 2021 | -8.4% | -8.0% | 28.71% |
| 2022 | -29.2% | -29.0% | -18.11% |
| 2023 | 21.8% | 22.9% | 26.29% |
| 2024 | -22.9% | -22.5% | 25.02% |
| 2025 | 99.2% | 99.8% | 17.88% |

- Official rolling 10-year NAV TR is `+369.63%` with CAGR `16.73%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `469.63`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+141.88%` and annualize to `9.23%` over 10 complete calendar years. Common rows `2021-2025` compound to `+21.32%` and annualize to `3.94%`; positive / negative years are `2 / 3`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; CSKR trails by approximately `10.49 pp` CAGR in that common window.
- Official current NAV TR YTD is `+70.53%` as of `2026-07-21`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CSKRF / CSKR Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, benchmark change, as-of dates, rankings, filenames, South Korea region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## FLAX Sequential Queue Record

- Input row: `57/125`; input ticker: `FLAX`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:FLAX`; Franklin's official product page and June 2026 factsheet identify the listing exchange, ticker, CUSIP `35473P660`, and ISIN `US35473P6604`. No provider slug or guessed exchange is used.
- Type gate: Franklin classifies FLAX as an indexed equity ETF. The official prospectus says the fund uses a passive/indexing approach, invests at least 80% of assets in FTSE Asia ex Japan Capped Index component securities or related depositary receipts, and may use replication or representative sampling.
- Mandatory 10-year coverage audit: official inception is `2018-02-06`; the June 2026 factsheet reports the 10-year NAV field as `—`, so `10-year NAV TR unavailable`. Available-period official NAV TR coverage is `2018-02-06` to `2026-06-30`, approximately `8.39` elapsed years.
- Official available-period performance: NAV Total Return average annual return `7.85%`. Raw NAV TR start/end values are not disclosed. A normalized calculation from the official CAGR gives `100.00` to approximately `188.58`; this is explicitly a calculated normalized illustration, not a raw endpoint or proxy.
- Official calendar observations: NAV TR rows are disclosed for complete years `2019-2025`: `17.32%`, `24.96%`, `-3.72%`, `-19.01%`, `6.39%`, `10.92%`, and `31.33%`, respectively. The 2018 inception year is partial and shown as not disclosed on the performance page/factsheet. These rows compound to `77.17%` / CAGR `8.51%`; common `2021-2025` rows compound to `20.85%` / CAGR `3.86%`.
- S&P 500 comparison: cached USD Total Return rows are used for complete calendar years `2019-2025` and `2021-2025`; FLAX trails by `8.78 pp` and `10.57 pp` CAGR, respectively. The 2026 S&P row is not used because the current-year cache is not complete.
- Official current observation: NAV TR YTD `24.71%` as of `2026-06-30`; 3-year NAV standard deviation `18.07%`; country exposures as of `2026-06-30` include Taiwan `28.97%`, South Korea `24.81%`, China `22.63%`, and India `13.69%`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### FLAX Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FLAX` | [Franklin FLAX product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26346/SINGLCLASS/franklin-ftse-asia-ex-japan-etf/FLAX) | Canonical listing, fund identity, passive/indexed classification, benchmark, inception, expense ratio, current NAV/YTD and official performance fields | Page accessed `2026-07-24`; current page observations through `2026-07-10`; month-end performance through `2026-06-30` |
| `NYSE Arca:FLAX` | [Franklin FLAX June 2026 factsheet](https://www.franklintempleton.com/forms-literature/download/FLAX-FF) | Official NAV Total Return basis, available-period CAGR, calendar NAV/index rows, holdings, exposure and risk statistics | Factsheet dated `2026-06-30`; performance data through `2026-06-30` |
| `NYSE Arca:FLAX` | [Franklin passive-funds prospectus](https://www.franklintempleton.com/forms-literature/download/ETF5-P) | Passive/indexing strategy, 80% policy, replication/sampling, benchmark definition and risks | Prospectus accessed `2026-07-24`; fund summary dated `2025-08-01` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### FLAX Raw Observations And Calculations

| Year | FLAX NAV TR | FTSE Asia ex Japan Capped Index-NR | S&P 500 TR |
|---|---:|---:|---:|
| 2018 | not disclosed (partial inception year) | not disclosed | not comparable; ETF partial |
| 2019 | 17.32% | 17.60% | 31.49% |
| 2020 | 24.96% | 25.40% | 18.40% |
| 2021 | -3.72% | -3.10% | 28.71% |
| 2022 | -19.01% | -18.86% | -18.11% |
| 2023 | 6.39% | 7.04% | 26.29% |
| 2024 | 10.92% | 11.75% | 25.02% |
| 2025 | 31.33% | 31.67% | 17.88% |
| 2026 YTD | 24.71% | 24.30% | not comparable; current year not cached |

- Available-period official NAV TR CAGR: `7.85%`; actual date window `2018-02-06` to `2026-06-30`; elapsed years approximately `8.39`; normalized calculated endpoint approximately `188.58` from a `100.00` starting value; raw NAV endpoints `not disclosed`.
- Complete-calendar `2019-2025`: FLAX cumulative `77.17%`, CAGR `8.51%`; S&P 500 TR cumulative `205.41%`, CAGR `17.29%`; difference `-8.78 pp`.
- Common `2021-2025`: FLAX cumulative `20.85%`, CAGR `3.86%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; difference `-10.57 pp`.
- Current standardized NAV TR YTD: `24.71%` as of `2026-06-30`. The product page's later date-to-date capture is not substituted for the month-end convention used in the page's annual comparison.

### FLAX Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, available-period date window, normalized-endpoint disclosure, annual-row completeness, S&P 500 basis/window, current-YTD as-of date, primary region assignment, canonical filename, geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VGDTF Sequential Queue Record

- Input row: `58/125`; input ticker: `VGDTF`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `XETRA:VJPA`; the official Vanguard factsheet maps share class ISIN `IE00BFMXYX26` to the EUR Deutsche Börse trading line `VJPA` and also lists the same share class on Borsa Italiana as `VJPA`. Because the input is an OTC alias labelled as the EUR accumulating line, the canonical record uses the Deutsche Börse/Xetra line and retains `VGDTF` as the input alias. The OTC alias cross-check is secondary; NAV TR data comes from Vanguard.
- Type gate: Vanguard identifies the fund as an equity ETF using a passive/indexing approach, physical acquisition of FTSE Japan Index constituents, and sampling only when full replication is not practicable. It is not bond, commodity, currency, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock exposure.
- Mandatory 10-year coverage audit: share-class inception is `2019-09-24`; the June 2026 factsheet reports 10-year NAV performance as `—`, so `10-year NAV TR unavailable`. Available-period official NAV TR coverage is `2019-09-24` to `2026-06-30`, approximately `6.77` elapsed years.
- Official available-period performance: Vanguard reports NAV Total Return since-inception CAGR `9.96%`, net of fees with gross income reinvested. Raw NAV TR start/end values are not disclosed. A normalized calculation from the official CAGR gives `100.00` to approximately `190.09`; this is explicitly a calculated normalized illustration, not a raw endpoint or proxy.
- Official calendar observations: KIID rows for complete years `2020-2025` are reported to one decimal: `14.1%`, `1.1%`, `-15.9%`, `19.5%`, `7.7%`, and `25.2%`, respectively. These rounded rows compound to approximately `56.32%` / CAGR `7.73%`; common `2021-2025` rows compound to approximately `37.00%` / CAGR `6.50%`.
- S&P 500 comparison: cached USD Total Return rows are used for complete calendar years `2020-2025` and `2021-2025`; VJPA trails by approximately `7.35 pp` and `7.93 pp` CAGR, respectively. The 2026 S&P row is not used because the current-year cache is not complete.
- Official current observation: NAV TR YTD `15.27%` as of `2026-06-30`; latest issuer NAV `US$81.79` as of `2026-07-22`; 476 stocks and Japan exposure `100.00%` as of `2026-06-30`; P/E `18.9x` and P/B `1.9x` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### VGDTF / VJPA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `XETRA:VJPA` | [Vanguard FTSE Japan UCITS ETF (USD) Accumulating product page](https://www.vanguard.co.uk/professional/product/etf/equity/9674/vanguard-ftse-japan-ucits-etf-usd-accumulating) | Official share-class identity, passive/index classification, physical method, FTSE Japan benchmark, inception, current NAV, holdings, valuation and exchange-code routes | Page accessed `2026-07-24`; current NAV `2026-07-22`; portfolio/valuation data `2026-06-30` |
| `XETRA:VJPA` | [Vanguard FTSE Japan UCITS ETF June 2026 factsheet](https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Accumulating_9674_EU_INT_EN.pdf) | Official ISIN, Deutsche Börse EUR VJPA mapping, OCF, available-period NAV TR CAGR, annualized performance and rolling-period data | Factsheet dated `2026-06-30`; performance calculated on closing NAV `2026-06-30` |
| `XETRA:VJPA` | [Vanguard KIID for ISIN IE00BFMXYX26](https://fund-docs.vanguard.com/ie00bfmxyx26-en.pdf) | Official calendar-year fund/index returns for 2020-2025; rounded one-decimal rows | KIID accessed `2026-07-24`; calendar rows through `2025` |
| `OTC:VGDTF` | [OTC alias cross-check](https://stockanalysis.com/quote/otc/VGDTF/) | Secondary mapping evidence for the input OTC alias; not used for NAV TR or performance calculations | Page accessed `2026-07-24`; delayed market-data page |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### VGDTF / VJPA Raw Observations And Calculations

| Year | VJPA NAV TR | FTSE Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2019 | not disclosed (partial inception year) | not disclosed | not comparable; ETF partial |
| 2020 | 14.1% | 14.2% | 18.40% |
| 2021 | 1.1% | 1.2% | 28.71% |
| 2022 | -15.9% | -15.8% | -18.11% |
| 2023 | 19.5% | 19.6% | 26.29% |
| 2024 | 7.7% | 7.8% | 25.02% |
| 2025 | 25.2% | 25.3% | 17.88% |
| 2026 YTD | 15.27% | not disclosed in reviewed capture | not comparable; current year not cached |

- Available-period official NAV TR CAGR: `9.96%`; actual date window `2019-09-24` to `2026-06-30`; elapsed years approximately `6.77`; normalized calculated endpoint approximately `190.09` from a `100.00` starting value; raw NAV endpoints `not disclosed`.
- Complete-calendar `2020-2025`: VJPA rounded-row cumulative approximately `56.32%`, CAGR `7.73%`; S&P 500 TR cumulative `132.26%`, CAGR `15.08%`; difference approximately `-7.35 pp`.
- Common `2021-2025`: VJPA rounded-row cumulative approximately `37.00%`, CAGR `6.50%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; difference approximately `-7.93 pp`.
- Current standardized NAV TR YTD: `15.27%` as of `2026-06-30`. The issuer page's current NAV observation at `2026-07-22` is retained separately from the month-end performance convention.

### VGDTF / VJPA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias/share-class/ISIN mapping, canonical exchange selection from issuer-listed EUR line, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual-row precision caveat, available-period date window, normalized-endpoint disclosure, S&P 500 basis/window, current-YTD as-of date, Japan region assignment, canonical filename, geography tags, breadcrumbs, stale unresolved-state replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. The prior `2026-07-23` unresolved record is superseded by this issuer/share-class mapping; the underlying OTC alias remains disclosed as a gap in the source map.

## RAYJ Sequential Queue Record

- Input row: `59/125`; input ticker: `RAYJ`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:RAYJ`; Rayliant's official fund page identifies the ticker and reports the primary exchange as NYSE, while the official prospectus identifies the principal listing exchange as NYSE Arca, Inc. The issuer-qualified canonical record uses `NYSE Arca:RAYJ`.
- Type gate: Rayliant explicitly identifies RAYJ as an active strategy for pursuing growth in Japan's stock market. The strategy uses Sumitomo Mitsui DS Asset Management's fundamental research and local portfolio-management insights together with Rayliant's quantitative models. The official prospectus names Rayliant Investment Research as adviser and SMDAM as sub-adviser. This is active management, not passive/index tracking, so the workflow stops at the type gate.
- Mandatory 10-year coverage audit: not applicable after the confirmed unsupported-type classification. No NAV Total Return history, annual-return table, S&P 500 comparison, or proxy was created.
- Official page observations retained only for classification context: inception `2024-04-04`, net expense ratio `0.72%`, and NAV YTD `25.42%` as of `2026-06-30`; these figures are not used in a performance page because RAYJ is outside the supported ETF scope.

### RAYJ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:RAYJ` | [Rayliant RAYJ official fund page](https://funds.rayliant.com/rayj/) | Canonical ticker/fund identity, exchange context, inception, active strategy, current facts and performance context | Page accessed `2026-07-24`; performance table as of `2026-06-30`; page last updated `2026-07-07` |
| `NYSE Arca:RAYJ` | [RAYJ official prospectus](https://funds.rayliant.com/wp-content/uploads/ETF/RAYJ/Rayliant-RAYJ-Prospectus.pdf) | Principal listing exchange, adviser/sub-adviser and official active-fund description | Prospectus dated `2024-04-01`, supplemented `2024-07-29` |

### RAYJ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, unsupported-type reason, no accidental performance-page creation, source URLs, ledger update, queue pointer, and no region/index navigation update for an unsupported ETF.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## FLJH Sequential Queue Record

- Input row: `41/125`; input ticker: `FLJH`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:FLJH`; Franklin's official product page and factsheet identify Franklin FTSE Japan Hedged ETF, NYSE Arca listing, CUSIP `35473P637`, ISIN `US35473P6372`, inception `2017-11-02`, expense ratio `0.09%`, equity asset class, and benchmark FTSE Japan RIC Capped Hedged to USD Index. No provider slug or guessed exchange is used.
- Type gate: official materials describe a passive/indexed equity ETF tracking a market-capitalization-weighted Japan large/mid-cap index with currency hedging. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had a stale YTD and no verified benchmark, inception or annual rows. Rechecking the official product page, March 2026 factsheet, annual report/total-return report and summary prospectus confirms inception `2017-11-02`; the official 10-year field is `—`, and inception through `2026-03-31` is approximately `8.41` years. This is an actual history gap, so `10-year NAV TR unavailable` is recorded.
- Official available-period performance: Franklin reports NAV TR annualized `13.63%` from inception through `2026-03-31`; raw start/end TR values and cumulative return are not disclosed. The 2018-2025 complete calendar rows compound to `177.49%` / CAGR `13.61%`.
- Official calendar observations: Franklin factsheet provides FLJH NAV rows `2018-2025` of `-13.96%`, `20.52%`, `9.44%`, `12.78%`, `-1.47%`, `35.04%`, `26.07%`, `29.25%`; matching FTSE Japan Capped Hedged Index rows are `-14.00%`, `20.79%`, `9.46%`, `12.82%`, `-1.35%`, `34.92%`, `25.98%`, `29.20%`. Common `2021-2025` FLJH rows compound to `144.52%` / CAGR `19.58%`; positive/negative years are `7/1` in complete rows.
- S&P 500 rows use the cached USD Total Return convention; common 2021-2025 CAGR is `14.43%`, so FLJH leads by approximately `5.15 pp` CAGR. S&P rows are shown as a common reference benchmark, not the issuer benchmark.
- Official current observation: Franklin reports NAV TR YTD `22.91%` as of `2026-07-07`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.
- Hedging caveat: the fund seeks to reduce Yen currency risk, so hedge costs, hedge timing and basis differences can cause returns to diverge from unhedged Japan equity funds and from the local-currency index.

### FLJH Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FLJH` | [Franklin FLJH product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26355/SINGLCLASS/franklin-ftse-japan-hedged-etf/FLJH) | Canonical listing, identity, passive/index classification, benchmark, inception, current NAV/YTD, holdings, fee and risk data | Page accessed `2026-07-24`; current NAV/YTD `2026-07-07`; rolling summary `2026-05-31` |
| `NYSE Arca:FLJH` | [Franklin FLJH factsheet](https://www.franklintempleton.com/forms-literature/download/FLJH-FF) | Fund objective, equity/index classification, inception, fee, benchmark, annual NAV/index rows and available-period NAV TR | Factsheet as of `2026-03-31` |
| `NYSE Arca:FLJH` | [Franklin FLJH annual report / total-return report](https://www.franklintempleton.com/tools-and-resources/literature/info/FLJH-ATSR) | Historical performance and annual-report cross-check | Publication `2026-03`; report periods through `2025-03-31` in reviewed capture |
| `NYSE Arca:FLJH` | [Franklin FLJH summary prospectus](https://www.franklintempleton.com/forms-literature/download-preview/FLJH-PSUM) | Passive strategy, fee, currency-hedging and risk disclosures | Prospectus dated `2025-08-01` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### FLJH Raw Observations And Calculations

| Year | FLJH NAV TR | FTSE Japan Capped Hedged TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not applicable (pre-inception) | not applicable | 11.96% |
| 2017 | not applicable (partial inception year) | not applicable | 21.83% |
| 2018 | -13.96% | -14.00% | -4.38% |
| 2019 | 20.52% | 20.79% | 31.49% |
| 2020 | 9.44% | 9.46% | 18.40% |
| 2021 | 12.78% | 12.82% | 28.71% |
| 2022 | -1.47% | -1.35% | -18.11% |
| 2023 | 35.04% | 34.92% | 26.29% |
| 2024 | 26.07% | 25.98% | 25.02% |
| 2025 | 29.25% | 29.20% | 17.88% |

- `10-year NAV TR unavailable`; inception `2017-11-02` to factsheet as-of `2026-03-31` is approximately `8.41` years.
- Official available-period NAV TR annualized return is `13.63%`; raw start/end values and raw cumulative return are `not disclosed`.
- Official calendar rows `2018-2025` compound to `+177.49%` / CAGR `13.61%`; S&P 500 TR rows compound to `+192.03%` / CAGR `14.33%`.
- Common rows `2021-2025` compound to `+144.52%` / CAGR `19.58%`; S&P 500 compounds to `+96.17%` / CAGR `14.43%`; FLJH leads by approximately `5.15 pp` CAGR.
- Official current NAV TR YTD is `+22.91%` as of `2026-07-07`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### FLJH Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange and share-class resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, available-period table, annual rows, issuer benchmark, S&P 500 basis/window, current-YTD as-of date, calculations, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## GXC Sequential Queue Record

- Input row: `42/125`; input ticker: `GXC`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:GXC`; State Street's official product page and January 31, 2026 SEC summary prospectus identify State Street SPDR S&P China ETF, NYSE Arca listing, CUSIP `78463X400`, ISIN `US78463X4007`, inception `2007-03-20`, gross expense ratio `0.59%`, equity asset class and benchmark S&P China BMI Index. No provider slug or guessed exchange is used.
- Type gate: State Street identifies the fund as passively managed and the objective as tracking the total return performance of an equity index. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund. The page's `Options Available` field refers to exchange-traded options on the ETF, not a derivative-heavy fund strategy.
- Mandatory 10-year audit: the prior page had no verified benchmark, inception, rolling result or annual table. Rechecking the current State Street product page, June 2026 factsheet and January 31, 2026 SEC summary prospectus confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page gap, not an actual history gap.
- Official rolling performance: State Street reports NAV TR CAGR `4.37%` for the 10-year window as of `2026-06-30`; raw start/end TR values and raw cumulative return are not disclosed. The implied cumulative return from the official CAGR is approximately `53.38%`, explicitly shown as a calculation rather than a raw endpoint.
- Official annual-data gap: the reviewed current product page and June 2026 factsheet provide rolling performance but no readable annual NAV/index rows for `2016-2025`; no third-party annual proxy is created. Annual table rows remain `not disclosed`, while S&P 500 cached reference rows are shown separately.
- Official current observation: State Street reports NAV `US$88.69` as of `2026-07-22`, 1,309 holdings as of `2026-07-22`, and current NAV TR YTD `-10.99%` as of `2026-06-30`. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; exact GXC annual-window CAGR and common-window spread are `not disclosed` because issuer annual rows were not disclosed in the reviewed official capture.

### GXC Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:GXC` | [State Street GXC product and performance page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-china-etf-gxc) | Canonical listing, identity, passive classification, benchmark, inception, rolling 10Y NAV TR, current NAV/YTD, holdings, fee and risk data | Page accessed `2026-07-24`; rolling/YTD summary `2026-06-30`; NAV/holdings `2026-07-22` |
| `NYSE Arca:GXC` | [State Street GXC factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gxc.pdf) | Objective, equity/index classification, inception, fee, rolling NAV TR, holdings/sector/country data and total-return basis | Factsheet as of `2026-06-30` |
| `NYSE Arca:GXC` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031213/d92286d497k.htm) | Objective, passive sampling, index, fee and risk disclosure; annual-return section cross-check | Prospectus dated `2026-01-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### GXC Raw Observations And Calculations

| Year | GXC NAV TR | S&P China BMI TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | not disclosed | not disclosed | 28.71% |
| 2022 | not disclosed | not disclosed | -18.11% |
| 2023 | not disclosed | not disclosed | 26.29% |
| 2024 | not disclosed | not disclosed | 25.02% |
| 2025 | not disclosed | not disclosed | 17.88% |

- Official rolling 10-year NAV TR CAGR is `4.37%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints/cumulative rolling return are `not disclosed`; implied cumulative from CAGR is approximately `53.38%`.
- Official annual GXC NAV/index rows and 2016-2025 / 2021-2025 GXC CAGRs are `not disclosed` in the reviewed current official capture; no proxy is created.
- S&P 500 TR rows compound to `+298.33%` / CAGR `14.82%` for `2016-2025` and `+96.17%` / CAGR `14.43%` for `2021-2025`; these are reference-only comparisons.
- Official current NAV TR YTD is `-10.99%` as of `2026-06-30`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### GXC Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange and share-class resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual-data gap, issuer benchmark, S&P 500 basis/window, current-YTD as-of date, calculations, filenames, China region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## JPAN Sequential Queue Record

- Input row: `43/125`; input ticker: `JPAN`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:JPAN`; Matthews' official Japan Active ETF page and March 31, 2026 factsheet identify Matthews Japan Active ETF, ticker JPAN, primary exchange NYSE Arca, CUSIP `577-130-594`, inception `2023-09-21`, benchmark MSCI Japan Index and gross expense ratio `0.79%`. No provider slug or guessed exchange is used.
- Type gate result: Matthews describes a high-conviction growth strategy, unconstrained all-cap approach and fundamental research based on balance sheet, cash flow, management, product lines, governance and financial health. The official prospectus classifies it as an active ETF. This is outside the required passive, index-tracking equity ETF scope.
- Terminal reason: `unsupported ETF type` — active equity ETF; no performance page, annual NAV table, 10-year audit or Japan region/index row is created.

### JPAN Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:JPAN` | [Matthews Japan Active ETF product page](https://us.matthewsasia.com/funds/etfs/japan-active-etf/) | Canonical exchange/ticker, active strategy, inception, benchmark, NAV/YTD and fund facts | Page accessed `2026-07-24`; current data through `2026-07-17` |
| `NYSE Arca:JPAN` | [Matthews JPAN factsheet](https://www.matthewsasia.com/siteassets/resources/fund-documents/factsheets/etfs/fact_sheet_jpan.pdf) | Active objective/strategy, equity asset class, inception, exchange, benchmark and fee | Factsheet as of `2026-03-31` |
| `NYSE Arca:JPAN` | [Matthews ETF prospectus](https://www.matthewsasia.com/siteassets/resources/fund-documents/prospectus/etf-prospectus.pdf) | Legal structure and active-fund classification | Prospectus dated `2026-04-30` |

### JPAN Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange resolution, issuer identity, active/passive type gate, reason for terminal unsupported status, filename non-creation, source register, Japan region non-update, and link-scope check.
- Local fallback verdict: `PASS`; no performance page was created because the unsupported type gate is terminal. Reviewer-availability fallback is disclosed here as required.

## NFTY Sequential Queue Record

- Input row: `40/125`; input ticker: `NFTY`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:NFTY`; First Trust's official summary and May 1, 2026 summary prospectus identify First Trust India NIFTY 50 Equal Weight ETF, Nasdaq listing, CUSIP `33737J802`, ISIN `US33737J8027`, inception `2012-02-14`, total expense ratio `0.80%`, and tracked index NIFTY 50 Equal Weight Index. No provider slug or guessed exchange is used.
- Type gate: the official objective is to seek results corresponding to the price and yield of an equity index, normally investing at least 90% in index securities and using an indexing approach. It is a passive, index-tracking equity ETF; it is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had annual rows but lacked verified inception, tracked index, rolling 10-year dates and issuer benchmark. Rechecking the current First Trust summary, June 2026 factsheet, May 1, 2026 summary prospectus and SEC XBRL records confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page gap, not an actual history gap.
- Official rolling performance: First Trust reports NAV Total Return CAGR `7.99%` for the 10-year window as of `2026-06-30`; raw start/end TR values and raw cumulative rolling return are not disclosed. The implied cumulative return from the official CAGR is approximately `115.69%`, explicitly shown as a calculation rather than a raw endpoint.
- Official calendar observations from the latest factsheet: NFTY rows `2016-2025` are `10.31%`, `22.54%`, `-2.67%`, `0.88%`, `10.83%`, `26.22%`, `-4.45%`, `24.39%`, `5.30%`, `5.84%`. These rows compound to `145.94%` / CAGR `9.42%`; common `2021-2025` rows compound to `67.19%` / CAGR `10.83%`; positive/negative years are `8/2`. Annual NIFTY 50 Equal Weight rows were not disclosed in the reviewed official capture.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so NFTY trails by approximately `3.60 pp` CAGR. S&P rows are shown as a common reference benchmark, not the issuer benchmark.
- Official current observation: First Trust reports NAV TR YTD `-7.45%` as of `2026-06-30`; latest summary-page NAV/holdings capture is dated `2026-07-21`. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.
- Methodology caveat: the underlying index changed from Nasdaq AlphaDEX Taiwan Index to NIFTY 50 Equal Weight Index on `2018-04-17`; earlier fund NAV history remains fund history but is not a pure current-index backtest. The NIFTY 50 Equal Weight Index inception is `2017-04-13`.

### NFTY Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:NFTY` | [First Trust NFTY summary page](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=NFTY) | Canonical listing, identity, inception, index, NAV TR, current NAV/YTD, holdings, fee and risk data | Page accessed `2026-07-24`; rolling/annual summary `2026-06-30`; NAV/holdings `2026-07-21` |
| `NASDAQ:NFTY` | [First Trust NFTY factsheet](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=4ce8e98a-434e-452d-89fb-89f33f070e32) | Fund identity, passive objective, inception, fee, index inception, 10-year NAV TR, current YTD and 2016-2025 annual rows | Factsheet as of `2026-06-30` |
| `NASDAQ:NFTY` | [First Trust summary prospectus](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=9c00e478-c2d3-49d2-b8db-229055716c36) | Indexing approach, 90% policy, fee, risk and index-history caveat | Prospectus dated `2026-05-01` |
| `NASDAQ:NFTY` | [SEC annual-return XBRL record](https://www.sec.gov/Archives/edgar/data/1510337/000144554626003180/R11.htm) and [average-annual-return XBRL record](https://www.sec.gov/Archives/edgar/data/1510337/000144554626003180/R12.htm) | SEC cross-check of annual and 10-year NAV total return disclosures | Performance through `2025-12-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### NFTY Raw Observations And Calculations

| Year | NFTY NAV TR | NIFTY 50 Equal Weight TR | NIFTY 50 TR | MSCI India TR | S&P 500 TR |
|---|---:|---:|---:|---:|---:|
| 2016 | 10.31% | not disclosed | 1.89% | -1.43% | 11.96% |
| 2017 | 22.54% | not disclosed | 37.95% | 38.75% | 21.83% |
| 2018 | -2.67% | not disclosed | -3.76% | -7.30% | -4.38% |
| 2019 | 0.88% | not disclosed | 11.88% | 7.58% | 31.49% |
| 2020 | 10.83% | not disclosed | 12.50% | 15.55% | 18.40% |
| 2021 | 26.22% | not disclosed | 23.48% | 26.23% | 28.71% |
| 2022 | -4.45% | not disclosed | -5.14% | -7.95% | -18.11% |
| 2023 | 24.39% | not disclosed | 20.82% | 20.81% | 26.29% |
| 2024 | 5.30% | not disclosed | 7.00% | 11.21% | 25.02% |
| 2025 | 5.84% | not disclosed | 6.57% | 2.62% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `7.99%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints are `not disclosed`; implied cumulative from CAGR is approximately `115.69%`.
- Official calendar rows `2016-2025` compound to `+145.94%` / CAGR `9.42%`; S&P 500 TR rows in the same window compound to `+298.33%` / CAGR `14.82%`.
- Common rows `2021-2025` compound to `+67.19%` / CAGR `10.83%`; S&P 500 compounds to `+96.17%` / CAGR `14.43%`; NFTY trails by approximately `3.60 pp` CAGR.
- Official current NAV TR YTD is `-7.45%` as of `2026-06-30`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### NFTY Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange and share-class resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, issuer benchmark and index-history caveat, S&P 500 basis/window, current-YTD as-of date, calculations, filenames, India region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## GSJY Sequential Queue Record

- Input row: `28/125`; input ticker: `GSJY`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:GSJY`; Goldman Sachs' official factsheet identifies ticker GSJY, NYSE Arca, inception `2016-03-02`, and the Goldman Sachs ActiveBeta Japan Equity Index. The official summary prospectus states the Fund is not actively managed; this is a rules-based smart-beta/index-tracking equity ETF.
- Mandatory coverage audit: the existing page lacked the benchmark, inception, rolling 10-year result and annual rows. Rechecking the official June 2026 factsheet and summary prospectus confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; 2016 calendar year remains partial and is not labeled complete.
- Official rolling performance: Goldman Sachs reports NAV 10-year annualized total return `9.29%` as of `2026-06-30`. Raw endpoints/cumulative are not disclosed; normalized TR `100.00` to `243.11` is calculated from the rounded CAGR.
- Official calendar observations: NAV rows are 2017 `24.52%`, 2018 `-10.52%`, 2019 `18.28%`, 2020 `12.52%`, 2021 `0.60%`, 2022 `-15.60%`, 2023 `18.92%`, 2024 `9.09%`, and 2025 `25.07%`; the corresponding ActiveBeta index rows are `23.99%`, `-12.88%`, `19.61%`, `14.44%`, `1.71%`, `-16.65%`, `20.32%`, `8.28%`, and `24.60%`. NAV 2017-2025 cumulative is `104.29%` / CAGR `8.26%`; common 2021-2025 cumulative is `37.76%` / CAGR `6.62%`; positive/negative years are `3/2` in the common window.
- S&P 500 rows use the cached USD TR convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so GSJY trails by `7.81 pp` CAGR.
- Official current observation: NAV YTD is `12.86%` as of `2026-06-30`; latest NAV price is `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed capture; total expense ratio is `0.25%` and holdings are `155`.

### GSJY Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:GSJY` | [Goldman Sachs GSJY factsheet](https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e) | identity, exchange, inception, passive/not actively managed classification, index, NAV TR, annual rows, fees and risk | Factsheet as of `2026-06-30` |
| `NYSE Arca:GSJY` | [Goldman Sachs summary prospectus](https://am.gs.com/public-assets/documents/179d857b-24e3-11ef-ad18-377468fbef87?view=true) | objective, not-actively-managed classification, fund structure and risk | Prospectus accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | cached USD TR rows as of `2025-12-31` |

### GSJY Raw Observations And Calculations

| Year | GSJY NAV TR | ActiveBeta Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed (partial inception year) | not disclosed | 11.96% |
| 2017 | 24.52% | 23.99% | 21.83% |
| 2018 | -10.52% | -12.88% | -4.38% |
| 2019 | 18.28% | 19.61% | 31.49% |
| 2020 | 12.52% | 14.44% | 18.40% |
| 2021 | 0.60% | 1.71% | 28.71% |
| 2022 | -15.60% | -16.65% | -18.11% |
| 2023 | 18.92% | 20.32% | 26.29% |
| 2024 | 9.09% | 8.28% | 25.02% |
| 2025 | 25.07% | 24.60% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `9.29%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `243.11`, actual years `10.00`. The normalized end is calculated from the rounded issuer CAGR; raw endpoints are not disclosed.
- Official calendar rows `2017-2025` compound to `104.29%` / CAGR `8.26%`; common rows `2021-2025` compound to `37.76%` / CAGR `6.62%`.

### GSJY Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## IHSEF Sequential Queue Record

- Input row: `29/125`; input ticker: `IHSEF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:IAPD`; the input OTC alias is resolved by iShares' official listing table to the iShares Asia Pacific Dividend UCITS ETF, ISIN `IE00B14X4T88`, with London Stock Exchange ticker `IAPD` in GBP and the same fund's USD line `IDAP`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page already had calendar rows but lacked verified benchmark, inception, rolling 10-year calculation, fee and current-source details. Rechecking the current official iShares product page and factsheet confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page-data gap, not a history gap.
- Type gate: official iShares identifies the asset class as Equity, the product as physical/replicated, and the objective as tracking an index of 50 high-dividend Asia-Pacific stocks. It is a passive/index-tracking equity ETF, not a bond, commodity, currency trust, active, leveraged, inverse, option-income or derivative-heavy fund.
- Official rolling performance: iShares reports NAV Total Return annualised `6.75%` for the 10-year window as of `2026-06-30`. Raw NAV endpoints are not disclosed; normalized TR `100.00` to `192.17` is calculated from the rounded CAGR.
- Official calendar observations: NAV rows 2016-2025 are `20.5%`, `16.6%`, `-15.1%`, `14.4%`, `-10.2%`, `4.0%`, `-2.3%`, `13.8%`, `5.9%`, and `29.7%`; the official benchmark rows are `21.0%`, `16.8%`, `-14.8%`, `14.9%`, `-9.6%`, `4.4%`, `-1.9%`, `14.3%`, `6.5%`, and `30.4%`. NAV 2016-2025 rows compound to approximately `94.63%` / CAGR `6.89%`; common 2021-2025 rows compound to `58.82%` / CAGR `9.69%`; positive/negative years are `4/1` in the common window.
- Benchmark caveat: iShares notes that the Fund used a different benchmark before `2020-06-22`; the official benchmark rows are retained separately from the fund NAV TR metric.
- S&P 500 rows use the cached USD TR convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so IHSEF trails by approximately `4.74 pp` CAGR.
- Official current observations: NAV TR YTD is `14.55%` and NAV is `US$31.26`, both as of `2026-07-21`; TER is `0.59%`, holdings are `50` as of `2026-07-16`, and 3-year standard deviation is `14.36%` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### IHSEF / IAPD Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:IAPD` | [iShares IAPD official product and performance page](https://www.ishares.com/uk/professional/en/products/251567/iapd?siteEntryPassthrough=true&switchLocale=y) | canonical listing, ISIN, fund identity, equity/passive physical-replicated classification, benchmark, inception, NAV TR, annual rows, current NAV/YTD, fee and risk data | Page accessed `2026-07-24`; rolling summary `2026-06-30`; NAV/YTD `2026-07-21`; holdings `2026-07-16` |
| `LSE:IAPD` | [iShares IAPD official factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/iapd-ishares-asia-pacific-dividend-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | corroborates share class, passive objective, ISIN, fee, distribution policy, benchmark and fund structure | Factsheet March 2026; performance/portfolio data through `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | cached USD TR rows as of `2025-12-31` |

### IHSEF / IAPD Raw Observations And Calculations

| Year | IAPD NAV TR | Dow Jones Asia/Pacific Select Dividend 50 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 20.5% | 21.0% | 11.96% |
| 2017 | 16.6% | 16.8% | 21.83% |
| 2018 | -15.1% | -14.8% | -4.38% |
| 2019 | 14.4% | 14.9% | 31.49% |
| 2020 | -10.2% | -9.6% | 18.40% |
| 2021 | 4.0% | 4.4% | 28.71% |
| 2022 | -2.3% | -1.9% | -18.11% |
| 2023 | 13.8% | 14.3% | 26.29% |
| 2024 | 5.9% | 6.5% | 25.02% |
| 2025 | 29.7% | 30.4% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `6.75%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `192.17`, actual years `10.00`. The normalized end is calculated from the rounded issuer CAGR; raw endpoints are not disclosed.
- Calendar rows `2016-2025` compound to approximately `94.63%` / CAGR `6.89%`; common rows `2021-2025` compound to `58.82%` / CAGR `9.69%`.

### IHSEF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, benchmark-change caveat, as-of dates, rankings, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## MINV Sequential Queue Record

- Input row: `30/125`; input ticker: `MINV`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:MINV`; Matthews' official fund page identifies the ticker, primary exchange, inception `2022-07-13`, benchmark `MSCI All Country Asia ex Japan Index`, and the Matthews Asia Innovators Active ETF. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. The official strategy is an active, high-conviction, all-cap fundamental approach investing at least 80% of net assets in companies Matthews believes are innovators. Official portfolio characteristics report active share `74.8%` as of `2026-06-30`; the page explicitly labels the product `Active ETF`. This is outside the required passive/index-tracking equity ETF scope.
- Per the type gate, no 10-year historical performance calculation, annual table, performance page, region performance row or S&P 500 comparison was created. Official current observations are not used as a performance deliverable.

### MINV Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:MINV` | [Matthews Asia Innovators Active ETF official page](https://us.matthewsasia.com/funds/etfs/asia-innovators-active-etf/) | canonical ticker/exchange, active classification, strategy, inception, benchmark and active share | Page accessed `2026-07-24`; portfolio characteristics `2026-06-30` |
| `NYSE Arca:MINV` | [Matthews MINV factsheet](https://us.matthewsasia.com/siteassets/resources/fund-documents/factsheets/etfs/fact_sheet_minv.pdf) | corroborates active strategy, inception, exchange, benchmark and fee | Factsheet March 2026 |

### MINV Pre-save Review Note

- No performance page save was required after the unsupported type gate. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## IMSCF Sequential Queue Record

- Input row: `31/125`; input ticker: `IMSCF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:CJPU`; iShares' official listing table maps the input OTC alias to London Stock Exchange ticker `CJPU` in USD for iShares MSCI Japan UCITS ETF, ISIN `IE00B53QDK08`, issued by iShares VII plc. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had current YTD but no verified fund identity, benchmark, inception, rolling 10-year calculation or annual rows. Rechecking the current official product page and factsheet confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page-data gap, not a history gap.
- Type gate: official iShares identifies the asset class as Equity, product structure Physical, methodology Replicated, and objective to track an index of Japanese companies. It is a passive/index-tracking equity ETF.
- Official rolling performance: iShares reports NAV Total Return annualised `9.46%` for the 10-year window as of `2026-06-30`. Raw NAV endpoints are not disclosed; normalized TR `100.00` to `246.92` is calculated from the rounded CAGR.
- Official calendar observations: NAV rows 2016-2025 are `1.9%`, `23.4%`, `-13.3%`, `19.1%`, `14.0%`, `1.2%`, `-17.0%`, `19.8%`, `8.2%`, and `24.5%`; the official MSCI Japan benchmark rows are `2.4%`, `24.0%`, `-12.9%`, `19.6%`, `14.5%`, `1.7%`, `-16.6%`, `20.3%`, `8.3%`, and `24.6%`. NAV 2016-2025 rows compound to approximately `100.65%` / CAGR `7.21%`; common 2021-2025 rows compound to `35.55%` / CAGR `6.27%`; positive/negative years are `4/1` in the common window.
- S&P 500 rows use the cached USD TR convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so IMSCF trails by approximately `8.16 pp` CAGR.
- Official current observations: NAV TR YTD is `12.11%` as of `2026-07-17`; NAV is `US$277.43` as of `2026-07-20`; TER `0.12%`, holdings `168` as of `2026-07-17`, and 3-year standard deviation `15.00%` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### IMSCF / CJPU Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:CJPU` | [iShares CJPU official product and performance page](https://www.ishares.com/uk/professional/en/products/253732/ishares-msci-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y) | canonical listing, ISIN, fund identity, equity/passive physical-replicated classification, benchmark, inception, NAV TR, annual rows, current NAV/YTD, fee and risk data | Page accessed `2026-07-24`; rolling summary `2026-06-30`; NAV/YTD `2026-07-20` / `2026-07-17`; holdings `2026-07-17` |
| `LSE:CJPU` | [iShares CJPU official factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/csjp-ishares-msci-japan-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | corroborates share class, passive objective, ISIN, fee, accumulating policy, benchmark and fund structure | Factsheet March 2026; performance/portfolio data through `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | cached USD TR rows as of `2025-12-31` |

### IMSCF / CJPU Raw Observations And Calculations

| Year | CJPU NAV TR | MSCI Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 1.9% | 2.4% | 11.96% |
| 2017 | 23.4% | 24.0% | 21.83% |
| 2018 | -13.3% | -12.9% | -4.38% |
| 2019 | 19.1% | 19.6% | 31.49% |
| 2020 | 14.0% | 14.5% | 18.40% |
| 2021 | 1.2% | 1.7% | 28.71% |
| 2022 | -17.0% | -16.6% | -18.11% |
| 2023 | 19.8% | 20.3% | 26.29% |
| 2024 | 8.2% | 8.3% | 25.02% |
| 2025 | 24.5% | 24.6% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `9.46%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `246.92`, actual years `10.00`. The normalized end is calculated from the rounded issuer CAGR; raw endpoints are not disclosed.
- Calendar rows `2016-2025` compound to approximately `100.65%` / CAGR `7.21%`; common rows `2021-2025` compound to `35.55%` / CAGR `6.27%`.

### IMSCF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## IHRMF Sequential Queue Record

- Input row: `32/125`; input ticker: `IHRMF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:IJPU`; iShares' official listing table maps the input OTC alias to London Stock Exchange ticker `IJPU` in USD for iShares MSCI Japan UCITS ETF USD (Dist), ISIN `IE00B02KXH56`, issued by iShares plc. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the prior register marked IHRMF unresolved because the primary listing code was not verified. Rechecking the current official iShares product page and factsheet confirms the IJPU listing, fund identity, and a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a listing-resolution/page gap, not a history gap.
- Type gate: official iShares identifies the asset class as Equity, product structure Physical, methodology Replicated, and objective to track an index of Japanese companies. It is a passive/index-tracking equity ETF.
- Official rolling performance: iShares reports NAV Total Return annualised `9.36%` for the 10-year window as of `2026-06-30`. Raw NAV endpoints are not disclosed; normalized TR `100.00` to `244.67` is calculated from the rounded CAGR.
- Official calendar observations: NAV rows 2016-2025 are `1.8%`, `23.3%`, `-13.4%`, `19.0%`, `13.8%`, `1.1%`, `-17.1%`, `19.7%`, `8.2%`, and `24.5%`; the official MSCI Japan benchmark rows are `2.4%`, `24.0%`, `-12.9%`, `19.6%`, `14.5%`, `1.7%`, `-16.6%`, `20.3%`, `8.3%`, and `24.6%`. NAV 2016-2025 rows compound to approximately `98.94%` / CAGR `7.12%`; common 2021-2025 rows compound to `35.14%` / CAGR `6.21%`; positive/negative years are `4/1` in the common window.
- S&P 500 rows use the cached USD TR convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so IHRMF trails by approximately `8.22 pp` CAGR.
- Official current observations: NAV TR YTD is `15.45%` and NAV is `US$24.18`, both as of `2026-07-22`; TER `0.12%`, holdings `168` as of `2026-07-14`, and 3-year standard deviation `15.00%` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### IHRMF / IJPU Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:IJPU` | [iShares IJPU official product and performance page](https://www.ishares.com/uk/professional/en/products/251866/ijpn?siteEntryPassthrough=true) | canonical listing, ISIN, fund identity, equity/passive physical-replicated classification, benchmark, inception, NAV TR, annual rows, current NAV/YTD, fee and risk data | Page accessed `2026-07-24`; rolling summary `2026-06-30`; NAV/YTD `2026-07-22`; holdings `2026-07-14` |
| `LSE:IJPU` | [iShares IJPU official factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/ijpn-ishares-msci-japan-ucits-etf-usd-dist-fund-fact-sheet-en-gb.pdf) | corroborates share class, passive objective, ISIN, fee, distributing policy, benchmark and fund structure | Factsheet April 2026; performance/portfolio data through `2026-04-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | cached USD TR rows as of `2025-12-31` |

### IHRMF / IJPU Raw Observations And Calculations

| Year | IJPU NAV TR | MSCI Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 1.8% | 2.4% | 11.96% |
| 2017 | 23.3% | 24.0% | 21.83% |
| 2018 | -13.4% | -12.9% | -4.38% |
| 2019 | 19.0% | 19.6% | 31.49% |
| 2020 | 13.8% | 14.5% | 18.40% |
| 2021 | 1.1% | 1.7% | 28.71% |
| 2022 | -17.1% | -16.6% | -18.11% |
| 2023 | 19.7% | 20.3% | 26.29% |
| 2024 | 8.2% | 8.3% | 25.02% |
| 2025 | 24.5% | 24.6% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `9.36%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `244.67`, actual years `10.00`. The normalized end is calculated from the rounded issuer CAGR; raw endpoints are not disclosed.
- Calendar rows `2016-2025` compound to approximately `98.94%` / CAGR `7.12%`; common rows `2021-2025` compound to `35.14%` / CAGR `6.21%`.

### IHRMF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## EWJV Sequential Queue Record

- Input row: `33/125`; input ticker: `EWJV`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NASDAQ:EWJV`; iShares' official U.S. product page identifies the exchange, fund, benchmark `MSCI Japan Value Index (USD) (Net)`, asset class Equity, inception `2019-03-05`, and passive index-tracking objective. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had only 2021-2025 rows and stale current YTD. Rechecking the issuer product page, current performance table, prospectus/factsheet links and inception date confirms actual history is under 10 years; official 10-year fields are `—`. This is a genuine history gap, so the status is `completed_available_period_no_10Y`, not `completed_10Y`.
- Official available-period performance: iShares reports NAV Total Return since-inception annualised `12.13%` as of `2026-06-30`; the period is `2019-03-05` to `2026-06-30`, approximately `7.32` elapsed years. Raw NAV endpoints are not disclosed; normalized TR `100.00` to `231.22` is calculated from the rounded since-inception CAGR. `10-year NAV TR unavailable` is stated explicitly.
- Official calendar observations: NAV rows 2021-2025 are `6.16%`, `-5.68%`, `23.05%`, `11.77%`, and `33.56%`; benchmark rows are `5.88%`, `-5.26%`, `23.11%`, `12.76%`, and `32.00%`. NAV rows compound to `83.93%` / CAGR `12.96%`; positive/negative years are `4/1`.
- S&P 500 rows use the cached USD TR convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so EWJV trails by approximately `1.47 pp` CAGR.
- Official current observations: NAV TR YTD is `18.04%` and NAV is `US$46.21`, both as of `2026-07-22`; expense ratio `0.15%`, holdings `109` as of `2026-07-22`, 3-year standard deviation `12.83%`, and 3-year beta `0.42` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### EWJV Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:EWJV` | [iShares EWJV official product and performance page](https://www.ishares.com/us/products/307263/ishares-msci-japan-value-etf) | identity, exchange, inception, passive objective, benchmark, NAV TR, available-period performance, annual rows, current NAV/YTD, fee and risk data | Page accessed `2026-07-24`; since-inception/annual summary `2026-06-30`; NAV/YTD/holdings `2026-07-22` |
| `NASDAQ:EWJV` | [iShares EWJV factsheet](https://www.ishares.com/us/literature/fact-sheet/ewjv-ishares-msci-japan-value-etf-fund-fact-sheet-en-us.pdf) | corroborates fund description, inception, benchmark, fee, value-factor structure and performance basis | Factsheet as of `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | cached USD TR rows as of `2025-12-31` |

### EWJV Raw Observations And Calculations

| Year | EWJV NAV TR | MSCI Japan Value Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | 6.16% | 5.88% | 28.71% |
| 2022 | -5.68% | -5.26% | -18.11% |
| 2023 | 23.05% | 23.11% | 26.29% |
| 2024 | 11.77% | 12.76% | 25.02% |
| 2025 | 33.56% | 32.00% | 17.88% |

- Official available-period NAV TR annualised return is `12.13%` for `2019-03-05` to `2026-06-30`, actual years approximately `7.32`; normalized end `231.22` is calculated from the rounded issuer CAGR. `10-year NAV TR unavailable`.
- Calendar rows `2021-2025` compound to `83.93%` / CAGR `12.96%`; this is not a 10-year result.

### EWJV Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and mandatory 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, explicit no-10Y labeling, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VNFGF Sequential Queue Record

- Input row: `26/125`; input ticker: `VNFGF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:VDJP`; Vanguard's official product page and May 2026 factsheet identify Vanguard FTSE Japan UCITS ETF (USD) Distributing, ISIN `IE00B95PGT31`, USD London Stock Exchange ticker `VDJP`, benchmark `FTSE Japan Index`, inception `2013-05-21`, passive physical/index strategy, and Vanguard Funds PLC as legal entity. `VNFGF` is retained as the input OTC alias; no provider slug or guessed exchange is used.
- Mandatory coverage audit: the previous source register left VNFGF unresolved because the primary listing code was not verified. Rechecking Vanguard's product page, factsheet, current prospectus and annual-report links resolves the share class to LSE:VDJP and confirms a genuine `10.00` elapsed-year NAV TR window. This was an alias/listing-resolution gap, not a history gap.
- Official rolling performance: Vanguard reports NAV-to-NAV total returns with gross income invested and all dividends/capital-gains distributions reinvested. The factsheet as of `2026-05-31` reports 10-year NAV annualized performance `9.45%` for `2016-06-01` to `2026-05-31`; normalized TR is `100.00` to `246.69`, calculated as `100 × (1 + 9.45%)^10` from the rounded issuer CAGR, not an official raw endpoint.
- Official annual observations: Vanguard publishes rolling 12-month NAV rows `2016-06-01 to 2026-05-31`, which compound to approximately `146.61%` and annualize to `9.45%` using the displayed rounded rows. These are not calendar-year rows; calendar 2021-2025 CAGR remains `not disclosed`. The official FTSE Japan benchmark rows are kept beside them.
- S&P 500 comparison: cached complete-calendar-year USD Total Return rows 2016-2025 are shown separately; they compound to `298.33%` / CAGR `14.82%`. This is directional only because the S&P window is calendar-year and the VDJP window is June-May.
- Official current observations: Vanguard's product page reports NAV `US$50.23` at closure `2026-07-22`; the latest standardized YTD disclosed in the official factsheet is `16.30%` as of `2026-05-31`. Ongoing charges figure is `0.10%`, Japan exposure `100.0%`, and holdings `476` as of `2026-06-30`. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### VNFGF / VDJP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:VDJP` | [Vanguard FTSE Japan UCITS ETF USD Distributing product page](https://www.vanguard.co.uk/professional/product/etf/equity/9504/ftse-japan-ucits-etf-usd-distributing) | Canonical share-class mapping, exchange tickers, ISIN, fund identity, passive/physical classification, benchmark, inception, current NAV and holdings | Page accessed `2026-07-24`; current NAV `2026-07-22`; portfolio data `2026-06-30` |
| `LSE:VDJP` | [Vanguard VDJP factsheet](https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Distributing_9504_EU_INT_UK_EN.pdf) | Rolling 12-month NAV TR rows, 10-year NAV CAGR, reinvestment/NAV basis, fees, benchmark, exchange tickers and ISIN | Factsheet as of `2026-05-31` |
| `Vanguard Funds PLC` | [Vanguard ETF prospectus](https://fund-docs.vanguard.com/etf-prospectus-en.pdf) and annual-report link | Legal structure and official document cross-check | Prospectus dated `2026-06-02`; annual-report link accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### VNFGF / VDJP Raw Observations And Calculations

| Official rolling 12-month period | VDJP NAV TR | FTSE Japan Index TR |
|---|---:|---:|
| 2016-06-01 to 2017-05-31 | 15.56% | 15.76% |
| 2017-06-01 to 2018-05-31 | 14.79% | 14.94% |
| 2018-06-01 to 2019-05-31 | -10.92% | -10.74% |
| 2019-06-01 to 2020-05-31 | 6.92% | 7.06% |
| 2020-06-01 to 2021-05-31 | 24.81% | 24.97% |
| 2021-06-01 to 2022-05-31 | -13.73% | -13.64% |
| 2022-06-01 to 2023-05-31 | 4.48% | 4.57% |
| 2023-06-01 to 2024-05-31 | 17.73% | 17.85% |
| 2024-06-01 to 2025-05-31 | 11.48% | 11.59% |
| 2025-06-01 to 2026-05-31 | 32.20% | 32.31% |

- Official rolling 10-year NAV TR CAGR is `9.45%` for `2016-06-01` to `2026-05-31`; actual years `10.00`; normalized end `246.69` is derived from the rounded CAGR.
- Official displayed rolling rows compound to approximately `+146.61%` and annualize to `9.45%`; calendar-year 2021-2025 CAGR is `not disclosed`.
- S&P 500 TR calendar rows 2016-2025 compound to `+298.33%` / CAGR `14.82%`; this comparison is not date-aligned.
- Latest standardized NAV TR YTD is `+16.30%` as of `2026-05-31`; current-page NAV is `US$50.23` as of `2026-07-22`. Market-price return is kept separate.

### VNFGF / VDJP Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, rolling annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## EEMA Sequential Queue Record

- Input row: `25/125`; input ticker: `EEMA`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:EEMA`; iShares' official product page and factsheet identify ticker `EEMA` on NASDAQ, fund inception `2012-02-08`, asset class `Equity`, passive/index-tracking exposure, and benchmark `MSCI EM Asia Custom Capped Index (Net)`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had only 2021-2025 annual rows, stale YTD, and no benchmark, inception, or rolling 10-year calculation. Rechecking the current official product page, official factsheet, summary prospectus, and official document links confirms a genuine `10.00` elapsed-year NAV TR window; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `172.29%` and average annual `10.54%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `272.29`; raw NAV endpoints are not disclosed.
- Official calendar observations: NAV rows `2016-2020` were recovered from the official summary prospectus, while `2021-2025` rows were confirmed in the current official product page and March 2026 factsheet. Calendar rows compound to `121.24%` / CAGR `8.26%`; common `2021-2025` rows compound to `17.94%` / CAGR `3.36%`. S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`.
- Index/source caveat: the official factsheet and prospectus state that on `2018-06-01` EEMA began tracking MSCI EM Asia Custom Capped Index (Net); historical index data before that date is MSCI Emerging Markets Asia Index (Net). The rolling 10-year fund NAV TR remains the primary metric; benchmark rows are kept separate.
- Official current observation: iShares reports NAV `US$112.84` and NAV Total Return YTD `20.51%` as of `2026-07-22`; expense ratio `0.49%`, 879 holdings, and key geography exposures China `31.53%`, Taiwan `31.06%`, South Korea `16.82%`, India `16.09%` as of the same date. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### EEMA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:EEMA` | [iShares EEMA product and performance page](https://www.ishares.com/us/products/239629/ishares-msci-emerging-markets-asia-etf) | Canonical listing, fund identity, passive/index classification, benchmark, inception, rolling NAV TR, current NAV/YTD, annual 2021-2025 rows, fees and exposures | Page accessed `2026-07-24`; rolling/annual performance `2026-06-30` / `2025-12-31`; current NAV/YTD `2026-07-22` |
| `NASDAQ:EEMA` | [iShares EEMA factsheet](https://www.ishares.com/us/literature/fact-sheet/eema-ishares-msci-emerging-markets-asia-etf-fund-fact-sheet-en-us.pdf) | Corroborates passive structure, benchmark, launch date, 2021-2025 NAV rows, index change, fee and risk basis | Factsheet as of `2026-03-31`; its 10-year field is older and not used instead of the current product-page figure |
| `NASDAQ:EEMA` | [iShares EEMA summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-emerging-markets-asia-etf-8-31.pdf) | Historical calendar rows 2016-2020, fund performance basis, index splice and inception confirmation | Prospectus accessed `2026-07-24`; performance table through `2024-12-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### EEMA Raw Observations And Calculations

| Year | EEMA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.59% | 11.96% |
| 2017 | 41.94% | 21.83% |
| 2018 | -15.54% | -4.38% |
| 2019 | 18.36% | 31.49% |
| 2020 | 25.20% | 18.40% |
| 2021 | -4.19% | 28.71% |
| 2022 | -21.45% | -18.11% |
| 2023 | 6.98% | 26.29% |
| 2024 | 10.71% | 25.02% |
| 2025 | 32.32% | 17.88% |

- Official rolling 10-year NAV TR is `+172.29%` with CAGR `10.54%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `272.29`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+121.24%` and annualize to `8.26%` over 10 complete calendar years. Common rows `2021-2025` compound to `+17.94%` and annualize to `3.36%`; positive / negative years are `3 / 2`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; EEMA trails by approximately `11.07 pp` CAGR in that common window.
- Official current NAV TR YTD is `+20.51%` as of `2026-07-22`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### EEMA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows from official documents, S&P 500 basis/window, index splice, as-of dates, rankings, filenames, Emerging Markets region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.
| CQQQ | supported | NYSE Arca:CQQQ | China | not disclosed (not disclosed) | https://www.invesco.com/us/en/financial-products/etfs/invesco-china-technology-etf.html | official complete calendar NAV TR rows 2016-2025; 10Y calendar CAGR 4.44%; predecessor/index methodology breaks disclosed; current NAV/YTD not disclosed |
| ISMJF | supported | LSE:CPXJ | Asia-Pacific | 8.15% (2026-07-08) | https://www.ishares.com/uk/professional/en/products/253735/ishares-core-msci-pacific-ex-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y | OTC alias; official rolling 10Y NAV TR 108.94% / CAGR 7.65% as of 2026-06-30; annual NAV TR rows 2016-2025 |

## FLKR Sequential Queue Record

- Input row: `18/125`; input ticker: `FLKR`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:FLKR`; Franklin's official page identifies ticker `FLKR`, listing exchange `NYSE Arca`, fund inception `2017-11-02`, asset class `Equity`, and indexed/passive exposure to the FTSE South Korea Capped Index-NR. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page contained 2018-2025 annual rows only. Rechecking the official product page and factsheet confirms inception `2017-11-02`, official 10-year NAV return `—`, and no official 10.00-year NAV/TR window as of 2026-07-24. The 2017 partial inception year is excluded; 2018-2025 gives eight complete calendar years.
- Official current observations: NAV `US$59.71`, NAV TR YTD `86.35%`, and 157 holdings as of `2026-07-07`; gross/net expense ratio `0.09%` as of `2025-08-01`; 3-year NAV standard deviation `34.71%` in the factsheet as of `2026-03-31`.

### FLKR Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FLKR` | [Franklin FLKR product and performance page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26353/SINGLCLASS/franklin-ftse-south-korea-etf/FLKR) | Fund identity, exchange, benchmark, inception, passive classification, fee, current NAV/YTD, annual NAV returns, and official 10-year availability field | Page accessed `2026-07-24`; current NAV/YTD/holdings `2026-07-07`; average annual performance `2026-05-31` |
| `NYSE Arca:FLKR` | [Franklin FLKR factsheet](https://www.franklintempleton.com/forms-literature/download/FLKR-FF) | Corroborates NAV-return basis, distribution reinvestment, fee, inception, indexed category, 2018-2025 history, and 10-year unavailable field | Factsheet as of `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### FLKR Raw Observations And Calculations

| Year | FLKR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -20.34% | -4.38% |
| 2019 | 8.05% | 31.49% |
| 2020 | 42.82% | 18.40% |
| 2021 | -6.59% | 28.71% |
| 2022 | -28.31% | -18.11% |
| 2023 | 20.99% | 26.29% |
| 2024 | -19.46% | 25.02% |
| 2025 | 91.79% | 17.88% |

- Official available-period rows `2018-2025` compound to `+53.85%` and annualize to `5.53%` over `8.00 complete calendar years`. Normalized TR is `100.00` to `153.85`; raw NAV endpoint levels are `ไม่พบข้อมูลที่ยืนยันได้`.
- Complete common rows `2021-2025` compound to `+25.15%` and annualize to `4.59%`. S&P 500 TR compounds to `+96.17%` and annualizes to `14.43%`; FLKR trails by approximately `9.84 pp` CAGR.
- Official 10-year NAV TR is `unavailable`: issuer shows `—`, and inception `2017-11-02` to access date `2026-07-24` is `8.72 years` / `3,186 days`, below the required `10.00 elapsed years`.
- Official current NAV TR YTD is `+86.35%` as of `2026-07-07`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### FLKR Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, South Korea region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## CNXT Sequential Queue Record

- Input row: `24/125`; input ticker: `CNXT`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:CNXT`; VanEck's official product page and factsheet identify `CNXT` on NYSE Arca, inception `2014-07-23`, passive/index-tracking equity exposure, and the `ChiNext Index (SZ988107)`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had stale YTD data and no benchmark, inception, rolling 10-year result, or annual table. Rechecking the current official product page and factsheet confirms a genuine `10.00` elapsed-year NAV TR window; this was a page gap, not a history gap. The issuer also discloses a methodology/index change: before market close `2021-12-10`, the table reflects SME-ChiNext 100 Index (CNI6109); thereafter it reflects ChiNext Index (SZ988107).
- Official rolling performance: VanEck reports CNXT NAV average annual total return `7.37%` for the month ended `2026-06-30`, used as the 10-year CAGR for `2016-06-30` to `2026-06-30`. Raw start/end NAV TR values are not disclosed. Normalized TR is `100.00` to `203.62`, calculated as `100 × (1 + 7.37%)^10` from the rounded issuer CAGR and explicitly not treated as an official endpoint.
- Official calendar-year NAV rows: not disclosed in the reviewed issuer capture, so 2016-2025 CNXT rows, 2021-2025 CAGR, best/worst years, and common-window cumulative return remain `not disclosed`. S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`.
- Official current observation: VanEck reports NAV `US$51.14` and NAV YTD `16.05%` as of `2026-07-22`; net expense ratio `0.65%`, gross `1.00%`, and 99 holdings as of the same date. Daily NAV history sufficient for drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CNXT Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CNXT` | [VanEck CNXT product and performance page](https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt/) | Fund identity, exchange, passive/index classification, benchmark, inception, rolling NAV TR CAGR, current NAV/YTD, fees, holdings and methodology break | Page accessed `2026-07-24`; rolling/annual performance `2026-06-30`; current NAV/YTD and holdings `2026-07-22` |
| `NYSE Arca:CNXT` | [VanEck CNXT factsheet](https://www.vaneck.com/us/en/investments/chinext-innovators-etf-cnxt-fact-sheet.pdf/) | Corroborates index, inception, NAV return basis, fees, holdings and issuer performance table | Factsheet as of `2026-06-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CNXT Raw Observations And Calculations

| Year | CNXT NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |

- Official rolling 10-year NAV TR CAGR is `7.37%` for `2016-06-30` to `2026-06-30`; actual years `10.00`; normalized end `203.62` is derived from the rounded CAGR, not an official raw endpoint.
- 2021-2025 common-window CAGR and cumulative return: `not disclosed` because annual CNXT NAV TR rows are not disclosed.
- Current NAV TR YTD is `16.05%` as of `2026-07-22`; market-price return is kept separate. Daily NAV history for max drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### CNXT Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, calendar-row gap, S&P 500 basis/window, methodology/index break, as-of dates, rankings, filenames, China region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ISMJF Sequential Queue Record

- Input row: `23/125`; input ticker: `ISMJF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:CPXJ`; iShares' official listing table maps the input OTC alias to London Stock Exchange ticker `CPXJ`, ISIN `IE00B52MJY50`. The official product page identifies the share class as iShares Core MSCI Pacific ex-Japan UCITS ETF, issued by iShares VII plc. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page lacked annual rows, inception, benchmark and rolling performance. Rechecking the official iShares product/performance view and factsheet confirms physical/replicated passive equity structure, inception `2010-01-12`, and official 10.00-year NAV TR coverage; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `108.94%` and annualised `7.65%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `208.94`; actual years `10.00`.
- Official annual observations: iShares calendar NAV rows `2016-2025` and issuer benchmark rows were captured from the official performance view. The source states performance is NAV-based with gross income reinvested where applicable.
- Official current observation: iShares reports NAV `US$237.50` and NAV Total Return YTD `8.15%` as of `2026-07-08`; market-price return is kept separate.

### ISMJF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:CPXJ` | [iShares CPXJ product and performance page](https://www.ishares.com/uk/professional/en/products/253735/ishares-core-msci-pacific-ex-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y) | Canonical identity/listing, passive physical/replicated classification, benchmark, inception, fee, holdings, annual NAV TR, rolling 10Y and current NAV/YTD | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-08` |
| `LSE:CPXJ` | [iShares CPXJ factsheet](https://www.ishares.com/nl/professionele-belegger/nl/literature/fact-sheet/cspxj-ishares-core-msci-pacific-ex-japan-ucits-etf-fund-fact-sheet-en-nl.pdf?siteEntryPassthrough=true&switchLocale=y) | Corroborates passive structure, benchmark, launch/fee and NAV-return basis | Issuer factsheet 2026-Q1/2026-03-31 |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### ISMJF Raw Observations And Calculations

| Year | ISMJF / CPXJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.70% | 11.96% |
| 2017 | 25.80% | 21.83% |
| 2018 | -10.40% | -4.38% |
| 2019 | 18.20% | 31.49% |
| 2020 | 6.40% | 18.40% |
| 2021 | 4.70% | 28.71% |
| 2022 | -6.10% | -18.11% |
| 2023 | 6.30% | 26.29% |
| 2024 | 4.50% | 25.02% |
| 2025 | 20.40% | 17.88% |

- Official rolling 10-year NAV TR is `+108.94%` with CAGR `7.65%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `208.94`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+100.75%` and annualize to `7.22%` over 10 complete calendar years. Common rows `2021-2025` compound to `+31.49%` and annualize to `5.63%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; ISMJF/CPXJ trails by approximately `8.80 pp` CAGR.
- Official current NAV TR YTD is `+8.15%` as of `2026-07-08`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### ISMJF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## CQQQ Sequential Queue Record

- Input row: `22/125`; input ticker: `CQQQ`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:CQQQ`; Invesco's SEC summary prospectus identifies CQQQ on NYSE Arca, inception `2009-12-08`, asset class equity exposure, full-replication implementation and the `FTSE China Incl A 25% Technology Capped Index`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page already contained 2016-2025 annual rows but lacked the official benchmark, inception, rolling/complete-window calculation and continuity caveat. Rechecking the Invesco product link, official factsheet link and SEC prospectus confirms 10 complete calendar years of NAV performance; this is a data/documentation gap, not a history-length gap.
- Strategy continuity audit: the SEC prospectus states CQQQ succeeded the Guggenheim China Technology ETF after the `2018-05-18` reorganization and that performance before that date belongs to the predecessor. It also states the current FTSE index began `2019-06-22`, with a blended AlphaShares/FTSE series before then. The 10-year result is therefore accepted as historical calendar coverage with an explicit strategy/index break, not as a continuous current-methodology series.
- Official annual observations: calendar NAV TR rows `2016-2025` were retained from the verified Invesco performance capture. Official annual rows compound to `+54.48%`; normalized TR is `100.00` to `154.48`; actual coverage is `10.00` complete calendar years and CAGR `4.44%`.
- Official current observation: current NAV/YTD was `ไม่พบข้อมูลที่ยืนยันได้` in the Invesco capture as of `2026-07-24`; no value is backfilled from a secondary provider.

### CQQQ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CQQQ` | [Invesco CQQQ product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-china-technology-etf.html) | Issuer product identity and official performance-document entry point | Page accessed `2026-07-24`; current NAV/YTD not disclosed in capture |
| `NYSE Arca:CQQQ` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1378872/000119312525040714/d834062d497k.htm) | Exchange, inception, index, full-replication/passive structure, fee, predecessor and methodology continuity | Prospectus dated `2025-02-28`; performance periods through `2024-12-31` |
| `NYSE Arca:CQQQ` | [Invesco CQQQ factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/cqqq-invesco-china-technology-etf-fact-sheet.pdf) | Official issuer performance document link for calendar and standardized NAV returns | Latest indexed issuer factsheet capture `2026-Q1`; current extraction did not expose current NAV/YTD |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CQQQ Raw Observations And Calculations

| Year | CQQQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -0.07% | 11.96% |
| 2017 | 72.54% | 21.83% |
| 2018 | -34.21% | -4.38% |
| 2019 | 32.46% | 31.49% |
| 2020 | 58.33% | 18.40% |
| 2021 | -25.13% | 28.71% |
| 2022 | -29.74% | -18.11% |
| 2023 | -16.97% | 26.29% |
| 2024 | 11.24% | 25.02% |
| 2025 | 33.65% | 17.88% |

- Official complete calendar rows `2016-2025` compound to `+54.48%` and annualize to `4.44%` over `10.00` complete calendar years. Normalized TR is `100.00` to `154.48`.
- Common rows `2021-2025` compound to `-35.06%` and annualize to `-8.27%`. S&P 500 TR compounds to `+96.17%` and annualizes to `14.43%`; CQQQ trails by approximately `22.70 pp` CAGR.
- Current NAV/YTD: `ไม่พบข้อมูลที่ยืนยันได้`; daily NAV history sufficient for max drawdown and recovery is also `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### CQQQ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, issuer identity, passive-equity classification, inception and 10-calendar-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, predecessor/index breaks, as-of dates, rankings, filenames, China region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## SCJ Sequential Queue Record

- Input row: `21/125`; input ticker: `SCJ`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:SCJ`; iShares' official U.S. page identifies the product, exchange, fund launch `2007-12-20`, asset class `Equity`, benchmark `MSCI Japan Small Cap Index (Net)`, expense ratio `0.50%`, and ticker `SCJ`. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page contained only 2021-2025 rows and no inception, benchmark or rolling calculation. Rechecking the official U.S./international performance views and factsheet confirms official 10.00-year NAV TR coverage; the existing page gap was repaired rather than treated as a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `119.60%` and average annual return `8.18%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `219.60`; actual years `10.00`.
- Official annual observations: the international iShares performance view supplies NAV and issuer benchmark rows for `2016-2025`; the U.S. factsheet corroborates precise NAV rows for `2021-2025`. The source states growth-of-hypothetical-investment performance assumes reinvestment of dividends/capital gains and deducts fund expenses.
- Official current observation: the iShares international performance view reports NAV `US$105.49` and NAV Total Return YTD `16.10%` as of `2026-07-21`; the U.S. page's earlier observation was `14.73%` as of `2026-07-17`, so the later official date is used.

### SCJ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:SCJ` | [iShares SCJ U.S. product page](https://www.ishares.com/us/products/239666/ishares-msci-japan-smallcap-etf) | Canonical exchange, fund identity, benchmark, inception, fees, current NAV/YTD and rolling standardized NAV TR | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-17` |
| `NYSE Arca:SCJ` | [iShares SCJ international performance view](https://www.ishares.com/uk/professional/en/products/239666/ishares-msci-japan-smallcap-etf?siteEntryPassthrough=true&switchLocale=y) | 2016-2025 NAV/issuer benchmark rows and fresher current observation | Annual rows `2025-12-31`; current NAV/YTD `2026-07-21` |
| `NYSE Arca:SCJ` | [iShares SCJ factsheet](https://www.ishares.com/us/literature/fact-sheet/scj-ishares-msci-japan-small-cap-etf-fund-fact-sheet-en-us.pdf) | Corroborates passive equity objective, benchmark, launch, fee, 2021-2025 NAV rows and reinvestment/expense basis | Factsheet as of `2026-03-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### SCJ Raw Observations And Calculations

| Year | SCJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.60% | 11.96% |
| 2017 | 30.90% | 21.83% |
| 2018 | -16.40% | -4.38% |
| 2019 | 19.00% | 31.49% |
| 2020 | 6.30% | 18.40% |
| 2021 | -2.40% | 28.71% |
| 2022 | -12.70% | -18.11% |
| 2023 | 12.95% | 26.29% |
| 2024 | 3.26% | 25.02% |
| 2025 | 29.66% | 17.88% |

- Official rolling 10-year NAV TR is `+119.60%` with CAGR `8.18%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `219.60`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+92.14%` and annualize to `6.75%` over 10 complete calendar years. Precise common rows `2021-2025` compound to `+28.85%` and annualize to `5.20%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; SCJ trails by approximately `9.23 pp` CAGR in that common window.
- Official current NAV TR YTD is `+16.10%` as of `2026-07-21`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### SCJ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ISSSF Sequential Queue Record

- Input row: `20/125`; input ticker: `ISSSF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:SAUS`; the iShares official product page and factsheet identify the product as `iShares MSCI Australia UCITS ETF`, ticker `SAUS` on the London Stock Exchange, issued by `iShares III plc`, ISIN `IE00B5377D42`. `ISSSF` is retained as the input OTC alias; no provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page already had calendar rows but lacked issuer benchmark, inception and rolling 10-year calculation. Rechecking the official product page, current factsheet and listing table confirms share-class launch `2010-01-22`, passive/replicated physical equity structure, and official 10.00-year NAV TR coverage; this was a page gap, not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `121.17%` and annualised `8.26%` for `2016-06-30` to `2026-06-30`. Normalized TR is `100.00` to `221.17`; actual years `10.00`.
- Official annual observations: iShares calendar-year NAV rows 2016-2025 and the issuer benchmark rows were captured from the official performance table. The source states performance is NAV-based with gross income reinvested where applicable.
- Official current observation: iShares reports NAV `US$62.24` and NAV Total Return YTD `10.27%` as of `2026-07-21`; market-price return is kept separate.

### ISSSF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:SAUS` | [iShares SAUS product and performance page](https://www.ishares.com/uk/professional/en/products/251851/ishares-msci-australia-ucits-etf) | Canonical listing, fund identity, passive/physical/replicated classification, benchmark, inception, annual NAV TR, rolling 10Y return, current NAV/YTD and risk facts | Page accessed `2026-07-24`; rolling summary `2026-06-30`; current NAV/YTD `2026-07-21` |
| `LSE:SAUS` | [iShares SAUS factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/saus-ishares-msci-australia-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | Corroborates passive structure, benchmark, launch date, fee, NAV return basis and calendar rows | Factsheet February 2026; calendar performance through 2025-12-31 |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### ISSSF Raw Observations And Calculations

| Year | ISSSF / SAUS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.00% | 11.96% |
| 2017 | 19.60% | 21.83% |
| 2018 | -12.30% | -4.38% |
| 2019 | 22.50% | 31.49% |
| 2020 | 8.40% | 18.40% |
| 2021 | 9.00% | 28.71% |
| 2022 | -5.70% | -18.11% |
| 2023 | 14.30% | 26.29% |
| 2024 | 0.80% | 25.02% |
| 2025 | 14.30% | 17.88% |

- Official rolling 10-year NAV TR is `+121.17%` with CAGR `8.26%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `221.17`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+109.27%` and annualize to `7.66%` over 10 complete calendar years. Common rows `2021-2025` compound to `+35.36%` and annualize to `6.24%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; ISSSF/SAUS trails by approximately `8.19 pp` CAGR in that common window.
- Official current NAV TR YTD is `+10.27%` as of `2026-07-21`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### ISSSF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Australia region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VPL Sequential Queue Record

- Input row: `19/125`; input ticker: `VPL`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:VPL`; Vanguard's official factsheet identifies ticker `VPL`, exchange `NYSE Arca`, fund inception `2005-03-04`, and passive full-replication exposure to the FTSE Developed Asia Pacific All Cap Index. No provider slug or guessed exchange is used.
- Mandatory coverage audit: the existing page had current YTD but no annual rows, inception, benchmark, or 10-year calculation. Rechecking Vanguard's product page and June 2026 factsheet confirms a genuine 10.00-year NAV TR window and a 10-year field; the page gap was repaired rather than treated as a history gap.
- Official rolling performance: Vanguard reports 10-year NAV TR cumulative `177.37%` and average annual return `10.74%` for `2016-05-31` to `2026-05-31`. Normalized TR is `100.00` to `277.37`; actual years `10.00`.
- Official annual observations: NAV total returns and benchmark rows for calendar years `2016-2025` were captured from Vanguard's annual performance table as of `2025-12-31`. Official factsheet as of `2026-06-30` separately reports 10-year NAV return `10.68%`, YTD `28.00%`, expense ratio `0.07%`, and 3-year standard deviation `16.27%`.
- Official current observation: Vanguard Advisors' official product page reports NAV YTD `19.62%` as of `2026-07-17`; this later date is kept separate from the month-end rolling/annual observations.

### VPL Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:VPL` | [Vanguard VPL product and performance page](https://investor.vanguard.com/investment-products/etfs/profile/vpl) | Fund identity, exchange, benchmark, passive/index classification, inception, annual NAV TR rows, rolling 10Y cumulative/CAGR, and distribution/expense basis | Page accessed `2026-07-24`; annual table `2025-12-31`; rolling summary `2026-05-31` |
| `NYSE Arca:VPL` | [Vanguard VPL factsheet](https://fund-docs.vanguard.com/F0962.pdf) | Corroborates index, inception, 10-year NAV TR, YTD, expense ratio, holdings/exposure and standard deviation | Factsheet as of `2026-06-30` |
| `NYSE Arca:VPL` | [Vanguard Advisors VPL page](https://advisors.vanguard.com/investments/products/vpl/vanguard-ftse-pacific-etf) | Fresher official current YTD observation | NAV YTD `19.62%` as of `2026-07-17` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### VPL Raw Observations And Calculations

| Year | VPL NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.31% | 11.96% |
| 2017 | 28.60% | 21.83% |
| 2018 | -13.85% | -4.38% |
| 2019 | 17.61% | 31.49% |
| 2020 | 16.58% | 18.40% |
| 2021 | 1.51% | 28.71% |
| 2022 | -15.21% | -18.11% |
| 2023 | 15.58% | 26.29% |
| 2024 | 1.27% | 25.02% |
| 2025 | 33.16% | 17.88% |

- Official rolling 10-year NAV TR is `+177.37%` with CAGR `10.74%` for `2016-05-31` to `2026-05-31`; normalized TR is `100.00` to `277.37`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+114.60%` and annualize to `7.94%` over 10 complete calendar years. Common rows `2021-2025` compound to `+34.15%` and annualize to `6.05%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; VPL trails by approximately `8.38 pp` CAGR in that common window.
- Official current NAV TR YTD is `+19.62%` as of `2026-07-17`; market-price return is kept separate. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### VPL Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, as-of dates, rankings, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VGUDF Sequential Queue Record

- Input row: `34/125`; input ticker: `VGUDF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:VDPX`; Vanguard's official USD-distributing factsheet identifies the fund as Vanguard FTSE Developed Asia Pacific ex Japan UCITS ETF (USD) Distributing, ISIN `IE00B9F5YL18`, with London Stock Exchange USD ticker `VDPX`. The OTC alias `VGUDF` is cross-checked to the same fund name/share class; no provider slug or guessed exchange is used.
- Type gate: official Vanguard identifies an Irish UCITS, physical, passive/index-tracking equity ETF that seeks to track the FTSE Developed Asia Pacific ex Japan Index. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the existing source register had VGUDF unresolved. Rechecking the issuer product page, official factsheet, share-class identifiers and current product data resolves the page/alias gap and confirms a genuine `10.00` elapsed-year NAV TR window `2016-03-31` to `2026-03-31`; this is not a history gap.
- Official rolling performance: Vanguard reports NAV Total Return annualised `8.80%` for the 10-year window. Raw NAV endpoints are not disclosed; normalized TR is `100.00` to `232.43`, calculated from the rounded CAGR.
- Official calendar observations: Vanguard's official factsheet provides NAV and FTSE Developed Asia Pacific ex Japan Index total-return rows for `2016-2025`. Fund rows compound to `122.03%` / CAGR `8.30%`; common `2021-2025` rows compound to `30.23%` / CAGR `5.42%`; positive/negative years are `4/1` in the common window.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common `2021-2025` CAGR is `14.43%`, so VDPX trails by approximately `9.00 pp` CAGR.
- Official current observation: Vanguard's product page shows latest NAV `US$42.5244` as of `2026-07-20`; current YTD NAV TR is `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture and is not inferred from price or distribution data.

### VGUDF / VDPX Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:VDPX` | [Vanguard VDPX product and performance page](https://www.vanguard.co.uk/professional/product/etf/equity/9522/ftse-developed-asia-pacific-ex-japan-ucits-etf-usd-distributing) | Fund identity, passive physical equity classification, benchmark, inception, current NAV, holdings and regional exposure | Page accessed `2026-07-24`; portfolio data `2026-06-30`; latest NAV `2026-07-20` |
| `LSE:VDPX` | [Vanguard VDPX official factsheet](https://fund-docs.vanguard.com/FTSE_Developed_Asia_Pacific_ex_Japan_UCITS_ETF_USD_Distributing_9522_EU_INT_UK_EN.pdf?management-style=Index) | ISIN/share-class and exchange mapping, official NAV TR basis, 10-year result, calendar NAV/benchmark rows, fee and distribution policy | Factsheet performance through `2026-03-31`; calendar rows `2016-2025` |
| `VGUDF` alias | [Schwab VGUDF OTC chart page](https://www.schwab.wallst.com/schwab/Prospect/charts/interactive/popup.asp?symbol=VGUDF) | Secondary OTC alias/name cross-check only; not used as the NAV TR source | Page accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### VGUDF / VDPX Raw Observations And Calculations

| Year | VDPX NAV TR | FTSE Developed Asia Pacific ex Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 8.49% | 8.62% | 11.96% |
| 2017 | 32.21% | 32.41% | 21.83% |
| 2018 | -14.37% | -14.23% | -4.38% |
| 2019 | 16.97% | 17.09% | 31.49% |
| 2020 | 18.67% | 18.59% | 18.40% |
| 2021 | 1.05% | 1.25% | 28.71% |
| 2022 | -12.65% | -12.62% | -18.11% |
| 2023 | 11.00% | 11.03% | 26.29% |
| 2024 | -5.67% | -5.59% | 25.02% |
| 2025 | 40.91% | 40.99% | 17.88% |

- Official rolling 10-year NAV TR is `8.80%` annualised for `2016-03-31` to `2026-03-31`; normalized TR is `100.00` to `232.43`, actual years `10.00`. The normalized end is calculated from the rounded issuer CAGR; raw endpoints are not disclosed.
- Official calendar rows `2016-2025` compound to `+122.03%` and annualize to `8.30%` over 10 complete calendar years. Common rows `2021-2025` compound to `+30.23%` and annualize to `5.42%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; VDPX trails by approximately `9.00 pp` CAGR in that common window.
- Official current NAV is `US$42.5244` as of `2026-07-20`; current YTD NAV TR is `ไม่พบข้อมูลที่ยืนยันได้` in this reviewed capture. Daily NAV history sufficient for max drawdown and recovery is also `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### VGUDF / VDPX Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, current-YTD gap disclosure, as-of dates, rankings, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## CETFF Sequential Queue Record

- Input row: `35/125`; input ticker: `CETFF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:CEMA`; iShares' official product page identifies CEMA / Bloomberg `CEMA LN`, ISIN `IE00B5L8K969`, iShares MSCI EM Asia UCITS ETF USD (Acc), issuing company iShares VII plc. The OTC alias `CETFF` is cross-checked to the same fund and ISIN; no provider slug or guessed exchange is used.
- Type gate: official iShares identifies an equity, physical, replicated, passively managed UCITS ETF tracking MSCI EM Asia Index Net. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the previous source register marked CETFF unresolved. Rechecking the official iShares product page, current returns table, factsheet, KIID and share-class identifiers resolves the alias gap and confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this is not a history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `185.06%` and annualised `11.04%` for the 10-year window. Normalized TR is `100.00` to `285.06`; raw NAV endpoints are not disclosed.
- Official calendar observations: iShares provides precise 2016-2025 NAV and MSCI EM Asia Index Net rows in the official factsheet. NAV rows compound to `126.95%` / CAGR `8.54%`; common `2021-2025` rows compound to `19.44%` / CAGR `3.62%`; positive/negative years are `3/2` in the common window.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common `2021-2025` CAGR is `14.43%`, so CEMA trails by approximately `10.81 pp` CAGR.
- Official current observation: iShares reports NAV Total Return YTD `28.17%` as of `2026-06-30`; later current NAV/YTD was not exposed in the reviewed official capture and is not inferred from OTC price data.

### CETFF / CEMA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:CEMA` | [iShares CEMA product and performance page](https://www.ishares.com/uk/professional/en/products/253723/ishares-msci-em-asia-ucits-etf?siteEntryPassthrough=true&switchLocale=y) | Canonical ticker/share class, ISIN, passive physical/replicated classification, benchmark, inception, rolling 10Y NAV TR, annual rows, current NAV TR YTD, fee, holdings and risk data | Page accessed `2026-07-24`; rolling/current summary `2026-06-30`; holdings `2026-07-20` |
| `LSE:CEMA` | [iShares CEMA factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/csemas-ishares-msci-em-asia-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | Corroborates ISIN, passive objective, launch date, benchmark, fee and precise 2016-2025 NAV/benchmark rows | Factsheet April 2026; annual performance through `2025-12-31` |
| `LSE:CEMA` | [iShares CEMA KIID](https://www.ishares.com/uk/individual/en/literature/kiid/ucits_kiid-ishares-msci-em-asia-ucits-etf-usd-acc-gb-ie00b5l8k969-en.pdf?siteEntryPassthrough=true&switchLocale=y) | Confirms passive management, equity exposure, share-class identity and index objective | Document dated `2026-04-09` |
| `CETFF` alias | [StockAnalysis CETFF OTC page](https://stockanalysis.com/quote/otc/CETFF/) | Secondary OTC alias/name/ISIN cross-check only; not used as NAV TR source | Page accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CETFF / CEMA Raw Observations And Calculations

| Year | CEMA NAV TR | MSCI EM Asia Index Net TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 5.48% | 6.14% | 11.96% |
| 2017 | 41.88% | 42.83% | 21.83% |
| 2018 | -15.99% | -15.45% | -4.38% |
| 2019 | 18.47% | 19.24% | 31.49% |
| 2020 | 27.57% | 28.38% | 18.40% |
| 2021 | -5.20% | -5.08% | 28.71% |
| 2022 | -21.00% | -21.11% | -18.11% |
| 2023 | 7.57% | 7.76% | 26.29% |
| 2024 | 11.98% | 11.96% | 25.02% |
| 2025 | 32.40% | 32.11% | 17.88% |

- Official rolling 10-year NAV TR is `+185.06%` with CAGR `11.04%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `285.06`, actual years `10.00`.
- Official calendar rows `2016-2025` compound to `+126.95%` and annualize to `8.54%` over 10 complete calendar years. Common rows `2021-2025` compound to `+19.44%` and annualize to `3.62%`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; CEMA trails by approximately `10.81 pp` CAGR in that common window.
- Official current NAV TR YTD is `+28.17%` as of `2026-06-30`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### CETFF / CEMA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, current-YTD as-of date, rankings, filenames, Emerging Markets region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## INDA Sequential Queue Record

- Input row: `36/125`; input ticker: `INDA`; terminal status: `completed_10Y`.
- Canonical entity key: `Cboe BZX:INDA`; iShares' official U.S. product page identifies iShares MSCI India ETF, Cboe BZX listing, ISIN `US46429B5984`, inception `2012-02-02`, benchmark MSCI India Index (Net), equity asset class, 165 holdings, and expense ratio `0.61%` as of the reviewed current page. No provider slug is used.
- Type gate: official iShares identifies a passive/index-tracking equity ETF. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had only 2021-2025 annual rows and no 10-year field. Rechecking the official product page, factsheet, summary prospectus, inception and benchmark/share-class identifiers confirms a genuine rolling `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page-data gap, not an actual history gap. Official calendar rows for 2016-2020 remain not disclosed in the reviewed current official capture.
- Official rolling performance: iShares reports NAV Total Return cumulative `98.09%` and annualised `7.07%` for the 10-year window. Normalized TR is `100.00` to `198.09`; raw NAV endpoints are not disclosed. The official method reflects reinvested distributions and fund expenses.
- Official calendar observations: iShares provides 2021-2025 INDA NAV TR rows `22.41%`, `-9.38%`, `17.49%`, `8.99%`, `2.47%`; matching MSCI India Index (Net) rows are `26.23%`, `-7.95%`, `20.81%`, `11.22%`, `2.62%`. The 2021-2025 INDA rows compound to `45.55%` / CAGR `7.80%`; positive/negative years are `4/1`.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so INDA trails by approximately `6.63 pp` CAGR. S&P rows are shown as a common reference benchmark, not the issuer benchmark.
- Official current observation: iShares reports latest NAV `US$48.65` and current NAV TR YTD `-10.12%` as of `2026-07-20`. The standardized month-end YTD shown on the official performance table is `-9.09%` as of `2026-06-30`; these are kept separate by as-of date. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### INDA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Cboe BZX:INDA` | [iShares INDA product and performance page](https://www.ishares.com/us/products/239659/ishares-msci-india-etf) | Canonical listing, fund identity, passive/index classification, benchmark, inception, rolling 10Y NAV TR, annual 2021-2025 rows, current NAV/YTD, fee, holdings and risk data | Page accessed `2026-07-24`; rolling/annual summary `2026-06-30`; current NAV/YTD `2026-07-20` |
| `Cboe BZX:INDA` | [iShares INDA factsheet](https://www.ishares.com/us/literature/fact-sheet/inda-ishares-msci-india-etf-fund-fact-sheet-en-us.pdf) | Corroborates equity asset class, benchmark, launch date, exchange, fee, and hypothetical-growth total-return basis | Factsheet as of `2026-03-31` |
| `Cboe BZX:INDA` | [iShares INDA summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-india-etf-8-31.pdf) | Prospectus and historical-performance/document cross-check for legal structure, benchmark and history audit | Official document accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### INDA Raw Observations And Calculations

| Year | INDA NAV TR | MSCI India Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 22.41% | 26.23% | 28.71% |
| 2022 | -9.38% | -7.95% | -18.11% |
| 2023 | 17.49% | 20.81% | 26.29% |
| 2024 | 8.99% | 11.22% | 25.02% |
| 2025 | 2.47% | 2.62% | 17.88% |

- Official rolling 10-year NAV TR is `+98.09%` with CAGR `7.07%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `198.09`, actual years `10.00`.
- Official calendar rows `2021-2025` compound to `+45.55%` and annualize to `7.80%`; S&P 500 TR rows in the same window compound to `+96.17%` and annualize to `14.43%`; INDA trails by approximately `6.63 pp` CAGR.
- Current official NAV TR YTD is `-10.12%` as of `2026-07-20`; standardized month-end YTD is `-9.09%` as of `2026-06-30`. Annual NAV/benchmark rows for `2016-2020` are `not disclosed` in the reviewed official capture and no proxy is created.

### INDA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange and share-class resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, current-YTD as-of dates, rankings, filenames, India region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## KDEF Sequential Queue Record

- Input row: `37/125`; input ticker: `KDEF`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:KDEF`; official PLUS product page and SEC summary prospectus identify the PLUS Korea Defense Industry Index ETF, principal listing exchange NYSE Arca, ticker KDEF, CUSIP `30151E491`, inception `2025-02-05`, and tracked index Korea Defense Industry Index. No provider slug or guessed exchange is used.
- Type gate: official prospectus says the fund normally invests at least 80% of net assets in securities comprising the index and is not actively managed. It is a passive, index-tracking equity ETF; it is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: reviewed the existing page, official PLUS product/performance page, official SEC summary prospectus, inception date, index objective and exchange identity. Inception `2025-02-05` to `2026-06-30` is `510` elapsed days, approximately `1.40` years, so `10-year NAV TR unavailable` is an actual history gap rather than a page-only gap.
- Official available-period performance: PLUS reports Fund NAV total return cumulative `105.69%` and since-inception annualized `67.39%` as of `2026-06-30`; normalized TR is `100.00` to `205.69`. Raw NAV endpoints and a complete-calendar annual NAV table are not disclosed.
- Official current observation: PLUS reports NAV `US$38.83` as of `2026-07-17`; standardized NAV TR YTD is `-8.13%` as of `2026-06-30`; current YTD as of 2026-07-17 is `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture.
- S&P 500 rows use the cached USD Total Return convention for the complete 2025 calendar year (`17.88%`). A matching S&P 500 TR series for KDEF's exact inception-to-date period and current 2026 YTD was not disclosed in the reviewed official source set; no proxy is created and the comparison table keeps the gap explicit.

### KDEF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KDEF` | [PLUS ETF KDEF product and performance page](https://plusetf.com/kdef) | Canonical exchange/ticker, fund identity, inception, index, NAV TR, available-period performance, current NAV, holdings, fee and risk disclosures | Page accessed `2026-07-24`; performance summary `2026-06-30`; NAV/holdings `2026-07-17` |
| `NYSE Arca:KDEF` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1547950/000121390026036312/ea0282658-04_497k.htm) | Objective, passive/index classification, 80% policy, concentration, non-diversified status, index methodology and fee | Prospectus dated `2026-03-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and complete 2025 row | Cached USD Total Return row as of `2025-12-31`; current 2026 TR YTD not disclosed in reviewed official capture |

### KDEF Raw Observations And Calculations

| Period | KDEF NAV TR | S&P 500 TR | Note |
|---|---:|---:|---|
| 2025 calendar year | not disclosed | 17.88% | KDEF began 2025-02-05; official complete-calendar KDEF NAV row not disclosed |
| 2026 YTD through 2026-06-30 | -8.13% | not disclosed | Official KDEF issuer YTD; matching S&P 500 TR YTD not disclosed in reviewed official source set |
| 2025-02-05 to 2026-06-30 | 105.69% cumulative / 67.39% annualized | not disclosed | Official KDEF since-inception period; no same-window S&P 500 TR series |

- `10-year NAV TR unavailable`; inception-to-as-of period is approximately `1.40` years, not 10 years.
- Official since-inception NAV TR cumulative is `+105.69%`; official issuer annualized value is `67.39%`; normalized end value `205.69` is based on the official cumulative return.
- Up years / down years, best/worst complete calendar year and drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้` because the official capture does not disclose a complete annual NAV history or daily NAV series.

### KDEF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange and fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, available-period table, S&P 500 basis/window and explicit gaps, current-YTD as-of date, filenames, South Korea region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ENZL Sequential Queue Record

- Input row: `38/125`; input ticker: `ENZL`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:ENZL`; official iShares U.S. product page identifies iShares MSCI New Zealand ETF, Nasdaq listing, CUSIP `464289123`, inception `2010-09-01`, equity asset class and benchmark MSCI New Zealand All Cap Top 25 Capped Index (Net). No provider slug or guessed exchange is used.
- Type gate: official prospectus identifies a passive/indexing approach, representative sampling and at least 80% investment in underlying-index securities. It is a passive, index-tracking equity ETF; it is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had no tracked index, inception or 10-year result. Rechecking the official product page, factsheet, summary prospectus and annual report confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page gap, not an actual history gap. The benchmark splice caveat from `2024-09-03` is recorded.
- Official rolling performance: iShares current standardized table reports NAV Total Return cumulative `38.78%` and average annual `3.33%` for the 10-year window. Normalized TR is `100.00` to `138.78`; raw NAV endpoints are not disclosed. The factsheet's March 2026 snapshot reports `3.25%` 10-year annualized performance, which is kept as a separate as-of observation and not mixed with the June window.
- Official calendar observations: iShares factsheet provides ENZL NAV TR rows `2021-2025` of `-10.86%`, `-16.63%`, `3.53%`, `-4.55%`, `1.68%`; annual rows for `2016-2020` and annual MSCI benchmark rows are not disclosed in the reviewed official capture. The 2021-2025 ENZL rows compound to `-25.33%` / CAGR `-5.67%`; positive/negative years are `2/3`.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so ENZL trails by approximately `20.10 pp` CAGR. S&P rows are shown as a common reference benchmark, not the issuer benchmark.
- Official current observation: iShares reports NAV `US$46.36` and current NAV TR YTD `3.45%` as of `2026-07-21`; the standardized month-end YTD table is `-0.07%` as of `2026-06-30`. These are kept separate by as-of date. Daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### ENZL Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:ENZL` | [iShares ENZL product and performance page](https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239672&seoSlug=ishares-msci-new-zealand-capped-etf) | Canonical listing, fund identity, equity/passive classification, benchmark, inception, rolling 10Y NAV TR, annual rows, current NAV/YTD, fee, holdings and risk data | Page accessed `2026-07-24`; rolling/annual summary `2026-06-30`; current NAV/YTD `2026-07-21` |
| `NASDAQ:ENZL` | [iShares ENZL factsheet](https://www.ishares.com/us/literature/fact-sheet/enzl-ishares-msci-new-zealand-etf-fund-fact-sheet-en-us.pdf) | Corroborates equity class, launch date, exchange, expense ratio, 2021-2025 NAV rows, holdings/risk data, reinvestment/expense basis and benchmark splice | Factsheet as of `2026-03-31`; annual rows through `2025-12-31` |
| `NASDAQ:ENZL` | [iShares ENZL summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-new-zealand-capped-etf-8-31.pdf) | Objective, passive indexing/representative sampling, 80% policy, index composition, fees and risk | Prospectus dated `2025-12-30` |
| `NASDAQ:ENZL` | [iShares ENZL annual report](https://www.blackrock.com/us/individual/literature/annual-report/ar-enzl-en.pdf) | Annual report performance cross-check and index-splice documentation | Reporting period ended `2025-08-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### ENZL Raw Observations And Calculations

| Year | ENZL NAV TR | MSCI New Zealand Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | -10.86% | not disclosed | 28.71% |
| 2022 | -16.63% | not disclosed | -18.11% |
| 2023 | 3.53% | not disclosed | 26.29% |
| 2024 | -4.55% | not disclosed | 25.02% |
| 2025 | 1.68% | not disclosed | 17.88% |

- Official rolling 10-year NAV TR is `+38.78%` with CAGR `3.33%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `138.78`, actual years `10.00`.
- Official calendar rows `2021-2025` compound to `-25.33%` and annualize to `-5.67%`; S&P 500 TR rows in the same window compound to `+96.17%` and annualize to `14.43%`; ENZL trails by approximately `20.10 pp` CAGR.
- Official current NAV TR YTD is `+3.45%` as of `2026-07-21`; standardized month-end YTD is `-0.07%` as of `2026-06-30`. Annual NAV/benchmark rows for `2016-2020` / annual benchmark observations are `not disclosed` in the reviewed official capture and no proxy is created.

### ENZL Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange and share-class resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, benchmark splice, S&P 500 basis/window, current-YTD as-of dates, rankings, filenames, New Zealand region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## FJP Sequential Queue Record

- Input row: `39/125`; input ticker: `FJP`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:FJP`; official First Trust summary page and SEC summary prospectus identify First Trust Japan AlphaDEX Fund, ticker FJP, Nasdaq listing, ISIN `US33737J1584`, CUSIP `33737J158`, inception `2011-04-18`, expense ratio `0.80%`, and tracked index Nasdaq AlphaDEX Japan Index. No provider slug or guessed exchange is used.
- Type gate: official objective is to seek results corresponding to the price and yield of an equity index, with semi-annual index reconstitution/rebalance. It is a passive, index-tracking equity ETF; it is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had annual rows but no tracked index, inception or rolling 10-year result. Rechecking the official summary page, factsheet, SEC summary prospectus, annual-report performance cross-check and index-change disclosure confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page gap, not an actual history gap.
- Official rolling performance: First Trust reports NAV TR CAGR `7.55%` for the 10-year window as of `2026-06-30`; raw rolling endpoints and cumulative return are not disclosed. The official factsheet's complete calendar rows `2016-2025` compound to `76.82%` / CAGR `5.87%`; the current rolling result is kept separate from the calendar-window calculation.
- Official calendar observations: First Trust factsheet provides FJP rows `2016-2025` of `2.91%`, `26.70%`, `-17.66%`, `8.27%`, `1.71%`, `-0.69%`, `-12.04%`, `22.42%`, `5.84%`, `32.14%`. The same factsheet provides MSCI Japan reference rows; annual Nasdaq AlphaDEX Japan rows are not disclosed in the reviewed capture. FJP's 2021-2025 rows compound to `49.56%` / CAGR `8.38%`; positive/negative years are `3/2`.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common 2021-2025 CAGR is `14.43%`, so FJP trails by approximately `6.04 pp` CAGR. S&P rows are shown as a common reference benchmark, not the issuer benchmark.
- Official current observation: First Trust reports NAV `US$73.56` as of `2026-07-21`; standardized NAV TR YTD is `14.26%` as of `2026-06-30`; current YTD as of 2026-07-21 is `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture.
- Methodology caveat: the fund's underlying index changed from Defined Japan Index to Nasdaq AlphaDEX Japan Index on `2015-07-14`; pre-change FJP history remains fund NAV history but is not a pure current-index backtest.

### FJP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:FJP` | [First Trust FJP summary page](https://www.ftportfolios.com/Retail/etf/etfsummary.aspx?Ticker=FJP) | Canonical listing, identity, inception, index, NAV TR, current NAV, YTD, holdings, fee and risk data | Page accessed `2026-07-24`; rolling/annual summary `2026-06-30`; NAV/holdings `2026-07-21` |
| `NASDAQ:FJP` | [First Trust FJP factsheet](https://www.ftportfolios.jp/content/funds/etf/fjp/firsttrustjapanfactsheetinstitutional) | Corroborates fund identity, passive index objective, inception, fee, 2016-2025 NAV/MSCI Japan rows, risk data and index-change caveat | Factsheet as of `2026-03-31`; annual rows through `2025-12-31` |
| `NASDAQ:FJP` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1510337/000144554626003319/fjp_497k.htm) | Objective, equity/index classification, fee, annual-return methodology and 2015-07-14 index-change disclosure | Prospectus dated `2026-05-01` |
| `NASDAQ:FJP` | [SEC annual report / N-CSR performance cross-check](https://www.sec.gov/Archives/edgar/data/1510337/000144554626001916/adex2_ncsr.htm) | Cross-checks 2021-2025 performance and annual-report fund statistics | Performance as of `2025-12-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### FJP Raw Observations And Calculations

| Year | FJP NAV TR | Nasdaq AlphaDEX Japan TR | MSCI Japan TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2016 | 2.91% | not disclosed | 2.38% | 11.96% |
| 2017 | 26.70% | not disclosed | 23.99% | 21.83% |
| 2018 | -17.66% | not disclosed | -12.88% | -4.38% |
| 2019 | 8.27% | not disclosed | 19.61% | 31.49% |
| 2020 | 1.71% | not disclosed | 14.48% | 18.40% |
| 2021 | -0.69% | not disclosed | 1.71% | 28.71% |
| 2022 | -12.04% | not disclosed | -16.65% | -18.11% |
| 2023 | 22.42% | not disclosed | 20.32% | 26.29% |
| 2024 | 5.84% | not disclosed | 8.31% | 25.02% |
| 2025 | 32.14% | not disclosed | 24.60% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `7.55%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints/cumulative rolling return are `not disclosed`.
- Official calendar rows `2016-2025` compound to `+76.82%` and annualize to `5.87%`; S&P 500 TR rows in the same window compound to `+298.33%` and annualize to `14.82%`.
- Common rows `2021-2025` compound to `+49.56%` / CAGR `8.38%`; S&P 500 compounds to `+96.17%` / CAGR `14.43%`; FJP trails by approximately `6.04 pp` CAGR.
- Official current NAV TR YTD is `+14.26%` as of `2026-06-30`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### FJP Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange and share-class resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, index-change caveat, S&P 500 basis/window, current-YTD as-of date, rankings, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## EPI Sequential Queue Record

- Input row: `44/125`; input ticker: `EPI`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:EPI`; WisdomTree's official product page, factsheet and prospectus identify WisdomTree India Earnings Fund, ticker EPI, NYSE Arca listing, inception `2008-02-22`, expense ratio `0.84%`, and the WisdomTree India Earnings Index. No provider slug or guessed exchange is used.
- Type gate: the official objective is to track the investment results of profitable companies in the Indian equity market through the WisdomTree India Earnings Index. The fund is a passive, index-tracking equity ETF; it is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had annual rows but no tracked index, inception or rolling 10-year result. Rechecking the current WisdomTree product/performance page, the March 2026 factsheet, the Q1 2026 presentation and the SEC summary prospectus confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page gap, not an actual history gap.
- Official rolling performance: WisdomTree reports NAV TR CAGR `9.18%` for the 10-year window as of `2026-06-30`; raw rolling start/end TR values and cumulative return are not disclosed. The shown implied cumulative return is approximately `140.67%` from the published CAGR, not a substitute for raw endpoints.
- Official calendar observations: WisdomTree's Q1 2026 presentation provides EPI NAV TR rows `2016-2025` of `2.24%`, `39.03%`, `-10.44%`, `1.70%`, `18.07%`, `28.02%`, `-5.72%`, `26.31%`, `11.11%`, `1.83%`. These compound to `163.67%` / CAGR `10.18%`; common `2021-2025` rows compound to `72.49%` / CAGR `11.52%`; positive/negative years are `8/2`. Annual WisdomTree India Earnings Index rows were not disclosed in the reviewed official capture. MSCI India rows are retained as an additional official reference, not as the issuer benchmark.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; S&P 500 common `2021-2025` CAGR is `14.43%`, so EPI trails by approximately `2.91 pp` CAGR. S&P rows are shown as a common reference benchmark, not the issuer benchmark.
- Official current observation: WisdomTree reports NAV `US$42.028` as of `2026-07-22` and standardized NAV TR YTD `-7.91%` for the month-end period ended `2026-06-30`.

### EPI Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:EPI` | [WisdomTree EPI product and performance page](https://www.wisdomtree.com/us/products/equity/epi) | Canonical listing/fund identity, passive/index objective, inception, NAV TR, rolling 10Y CAGR, current NAV/YTD, fee, holdings and risk data | Page accessed `2026-07-24`; product/NAV data `2026-07-22`; performance summary `2026-06-30` |
| `NYSE Arca:EPI` | [WisdomTree EPI quarterly factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-epi-1066.pdf?la=en) | Corroborates exchange, passive objective, tracked index, inception, fee, NAV TR methodology and standardized performance | Factsheet performance as of `2026-03-31` |
| `NYSE Arca:EPI` | [WisdomTree Q1 2026 India-equity presentation](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/presentations/equity/epi_indh_presentation.pdf) | Official 2016-2025 calendar NAV rows, MSCI India reference rows and 10-year standardized performance cross-check | Performance through `2026-03-31` |
| `NYSE Arca:EPI` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465924020138/epi120924497k.htm) | Objective, legal structure, index-tracking classification, fee and historical-performance cross-check | Prospectus dated `2024-12-10` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### EPI Raw Observations And Calculations

| Year | EPI NAV TR | WisdomTree India Earnings Index TR | MSCI India TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2016 | 2.24% | not disclosed | -1.43% | 11.96% |
| 2017 | 39.03% | not disclosed | 38.75% | 21.83% |
| 2018 | -10.44% | not disclosed | -7.30% | -4.38% |
| 2019 | 1.70% | not disclosed | 7.58% | 31.49% |
| 2020 | 18.07% | not disclosed | 15.55% | 18.40% |
| 2021 | 28.02% | not disclosed | 26.23% | 28.71% |
| 2022 | -5.72% | not disclosed | -7.95% | -18.11% |
| 2023 | 26.31% | not disclosed | 20.81% | 26.29% |
| 2024 | 11.11% | not disclosed | 11.21% | 25.02% |
| 2025 | 1.83% | not disclosed | 2.62% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `9.18%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints/cumulative rolling return are `not disclosed`; implied cumulative from CAGR is approximately `140.67%`.
- Official calendar rows `2016-2025` compound to `+163.67%` and annualize to `10.18%`; S&P 500 TR rows in the same window compound to `+298.33%` and annualize to `14.82%`.
- Common rows `2021-2025` compound to `+72.49%` / CAGR `11.52%`; S&P 500 compounds to `+96.17%` / CAGR `14.43%`; EPI trails by approximately `2.91 pp` CAGR.
- Official current NAV TR YTD is `-7.91%` as of `2026-06-30`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### EPI Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/share-class resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, issuer-index gap, S&P 500 basis/window, current-YTD as-of date, rankings, filenames, India region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ASHS Sequential Queue Record

- Input row: `45/125`; input ticker: `ASHS`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:ASHS`; DWS/Xtrackers and SEC identify Xtrackers Harvest CSI 500 China A-Shares Small Cap ETF, ticker ASHS, NYSE Arca listing, inception `2014-05-20`, CUSIP `233051754`, and expense ratio `0.65%`. No provider slug or guessed exchange is used.
- Type gate: the official objective is to track the CSI 500 Index, composed of predominantly small-cap China A-share companies. The fund uses a passive/indexing approach and is an equity ETF; it is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had an incorrect exchange key, no inception/index and no rolling result. Rechecking the current DWS product finder, Q1 2026 factsheet, October 2025 summary prospectus, SEC prospectus cross-check and annual shareholder report confirms a genuine `10.00` elapsed-year NAV TR window `2016-03-31` to `2026-03-31`; this was a page gap, not an actual history gap.
- Official rolling performance: DWS reports NAV TR CAGR `1.96%` for the 10-year window as of `2026-03-31`; raw rolling start/end TR values and cumulative return are not disclosed. The shown implied cumulative return is approximately `21.42%` from the published CAGR, not a substitute for raw endpoints.
- Official annual-data audit: the Q1 2026 factsheet discloses 1-, 3-, 5- and 10-year standardized periods but not readable annual NAV/index rows. The 2025 annual shareholder report provides a growth-of-$10,000 chart, not a complete annual return table. No chart-derived proxy or third-party annual series is substituted; 2016-2025 and 2021-2025 fund CAGRs remain `not disclosed`.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; S&P 500 reference CAGR is `14.82%` for 2016-2025 and `14.43%` for 2021-2025, but no ASHS spread is calculated because fund annual rows are missing.
- Official current observation: DWS reports NAV TR YTD `3.36%` as of `2026-03-31`; a `2026-06-30` current NAV TR YTD value was not disclosed in the reviewed official source capture.

### ASHS Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ASHS` | [Xtrackers ASHS product finder](https://etf.dws.com/en-us/etf-products/) | Official product discovery/current issuer source, fund identity and performance-document route | Page accessed `2026-07-24`; dynamic product data not readable in capture |
| `NYSE Arca:ASHS` | [Xtrackers ASHS Q1 2026 factsheet](https://etf.dws.com/download/asset/1bfed1b5-c933-4199-bdcc-30b0ed651740) | Canonical ticker/exchange, objective, index, inception, passive classification, NAV TR standardized performance, holdings, fee and risk data | Factsheet as of `2026-03-31` |
| `NYSE Arca:ASHS` | [Xtrackers ASHS summary prospectus](https://etf.dws.com/download/asset/7a928aa7-d2cc-490b-a3de-fb6144afc0cb) | Objective, passive/indexing strategy, exchange, fee, A-share access and risk disclosures | Prospectus dated `2025-10-01` |
| `NYSE Arca:ASHS` | [SEC ASHS summary prospectus cross-check](https://www.sec.gov/Archives/edgar/data/1503123/000008805324000976/k100124ashs.htm) | Independent regulator-hosted cross-check of canonical exchange, objective and historical-performance disclosure limitations | Prospectus dated `2024-10-01` |
| `NYSE Arca:ASHS` | [Xtrackers ASHS annual shareholder report](https://etf.dws.com/download/asset/cd4f449d-b77e-49df-8486-46f48efe43cc) | Growth-of-$10,000 and annual-report performance cross-check; confirms chart rather than complete annual-row disclosure | Reporting period ended `2025-05-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### ASHS Raw Observations And Calculations

| Year | ASHS NAV TR | CSI 500 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | not disclosed | not disclosed | 28.71% |
| 2022 | not disclosed | not disclosed | -18.11% |
| 2023 | not disclosed | not disclosed | 26.29% |
| 2024 | not disclosed | not disclosed | 25.02% |
| 2025 | not disclosed | not disclosed | 17.88% |

- Official rolling 10-year NAV TR CAGR is `1.96%` for `2016-03-31` to `2026-03-31`, actual years `10.00`; raw endpoints/cumulative rolling return are `not disclosed`; implied cumulative from CAGR is approximately `21.42%`.
- ASHS annual NAV/index rows for `2016-2025` and `2021-2025` are `not disclosed` in the reviewed official capture, so fund CAGRs, up/down counts and best/worst years are not calculated.
- S&P 500 TR rows in the common reference windows compound to `+298.33%` / CAGR `14.82%` for `2016-2025` and `+96.17%` / CAGR `14.43%` for `2021-2025`.
- Official current NAV TR YTD is `+3.36%` as of `2026-03-31`; current `2026-06-30` value and daily NAV history sufficient for max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

### ASHS Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, exchange correction from `NYSE` to issuer-confirmed `NYSE Arca`, CUSIP/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual-row gap, S&P 500 basis/window, current-YTD as-of date, rankings, canonical filename, China region assignment, canonical geography tag, breadcrumbs, old-link removal, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## PGJ Sequential Queue Record

- Input row: `46/125`; input ticker: `PGJ`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:PGJ`; Invesco's official product page/report and SEC filing identify Invesco Golden Dragon China ETF, ticker PGJ, Nasdaq listing, inception `2004-12-09`, CUSIP `46137V571`, and total expense ratio `0.70%`. No provider slug or guessed exchange is used.
- Type gate: the official objective is to track the Nasdaq Golden Dragon China Index, with at least 90% in equity securities of U.S.-listed companies headquartered or incorporated in China. The fund is passive/index-tracking equity; it is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had annual rows but no tracked index, inception, benchmark or rolling 10-year result. Rechecking Invesco's current product page, Q4 2025 report, SEC filing and index description confirms a genuine `10.00` elapsed-year NAV TR window `2015-12-31` to `2025-12-31`; this was a page gap, not an actual history gap.
- Official rolling performance: Invesco reports NAV TR CAGR `0.35%` for the 10-year window as of `2025-12-31`; raw rolling start/end TR values and cumulative return are not disclosed. The shown implied cumulative return is approximately `3.55%` from the published CAGR, not a substitute for raw endpoints.
- Official calendar observations: Invesco's Q4 2025 report provides PGJ NAV TR rows `2016-2025` of `-11.36%`, `59.97%`, `-29.16%`, `31.91%`, `53.58%`, `-42.76%`, `-24.36%`, `-2.45%`, `5.88%`, `13.73%`. These compound to `3.50%` / CAGR `0.34%`; common `2021-2025` rows compound to `-49.14%` / CAGR `-12.65%`; positive/negative years are `5/5` over 2016-2025.
- Benchmark caveat: the issuer benchmark is FTSE China 50 Index (USD); it is kept separate from the tracked Nasdaq Golden Dragon China Index and the common S&P 500 reference.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; S&P 500 common `2021-2025` CAGR is `14.43%`, so PGJ trails by approximately `27.08 pp` CAGR.
- Official current observation: current 2026 NAV TR YTD was not disclosed in the reviewed official Invesco capture; the latest standardized report is as of `2025-12-31`.

### PGJ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:PGJ` | [Invesco PGJ product and performance page](https://www.invesco.com/us/en/financial-products/etfs/invesco-golden-dragon-china-etf.html) | Canonical listing/fund identity, index objective, exchange and current product/document route | Page accessed `2026-07-24`; dynamic performance fields not readable in capture |
| `NASDAQ:PGJ` | [Invesco PGJ Q4 2025 report](https://www.invesco.com/us-rest/contentdetail?contentId=bc42fd05f0e21410VgnVCM100000c2f1bf0aRCRD&dnsName=us) | Official NAV TR 10-year result, 2016-2025 NAV/index/FTSE China 50 rows, inception and fund facts | Performance and facts as of `2025-12-31` |
| `NASDAQ:PGJ` | [SEC PGJ filing cross-check](https://www.sec.gov/Archives/edgar/data/1209466/000120946625000313/edgar.htm) | Regulator-hosted legal/fund and holdings cross-check | Filing data through `2025-07-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### PGJ Raw Observations And Calculations

| Year | PGJ NAV TR | Nasdaq Golden Dragon China Index TR | FTSE China 50 Index TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2016 | -11.36% | -11.13% | 2.87% | 11.96% |
| 2017 | 59.97% | 60.51% | 35.99% | 21.83% |
| 2018 | -29.16% | -28.84% | -11.51% | -4.38% |
| 2019 | 31.91% | 32.42% | 14.89% | 31.49% |
| 2020 | 53.58% | 54.41% | 11.52% | 18.40% |
| 2021 | -42.76% | -42.60% | -19.82% | 28.71% |
| 2022 | -24.36% | -24.24% | -19.32% | -18.11% |
| 2023 | -2.45% | -2.72% | -12.66% | 26.29% |
| 2024 | 5.88% | 5.89% | 32.41% | 25.02% |
| 2025 | 13.73% | 13.25% | 29.51% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `0.35%` for `2015-12-31` to `2025-12-31`, actual years `10.00`; raw endpoints/cumulative rolling return are `not disclosed`; implied cumulative from CAGR is approximately `3.55%`.
- Official calendar rows `2016-2025` compound to `+3.50%` and annualize to `0.34%`; S&P 500 TR rows in the same window compound to `+298.33%` and annualize to `14.82%`.
- Common rows `2021-2025` compound to `-49.14%` / CAGR `-12.65%`; S&P 500 compounds to `+96.17%` / CAGR `14.43%`; PGJ trails by approximately `27.08 pp` CAGR.
- Official current 2026 NAV TR YTD is `ไม่พบข้อมูลที่ยืนยันได้`; daily NAV history sufficient for max drawdown and recovery is also `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### PGJ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, tracked-index and issuer-benchmark separation, annual rows, S&P 500 basis/window, current-YTD gap, rankings, filename, China region assignment, canonical geography tag, breadcrumbs, duplicate old-link removal, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VFJUF Sequential Queue Record

- Input row: `47/125`; input ticker: `VFJUF`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `LSE:VJPU`; Vanguard's official product page and factsheet identify the fund as Vanguard FTSE Japan UCITS ETF - USD Hedged Accumulating, ISIN `IE00BFMXZJ56`, London Stock Exchange USD ticker `VJPU`, share-class inception `2020-01-31`, Vanguard Funds plc as legal entity, physical/index strategy, and OCF `0.13%`. `VFJUF` is retained as the input OTC alias; no provider slug or guessed exchange is used.
- Type gate: official objective is passive/indexing through physical acquisition of securities to track the FTSE Japan Index; the USD share class uses currency hedging. It is an equity ETF and is not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy.
- Mandatory 10-year audit: rechecked the official product page, May 2026 factsheet and FY2025 annual report. The share class began on `2020-01-31`; the factsheet's 10-year field is `—`, and the annual report identifies USD-Hedged Accumulating since inception from `2020-01-31`. Therefore the 10-year gap is an actual history gap, not only a page gap.
- Official available-period performance: Vanguard reports NAV TR since-inception CAGR `20.29%` for `2020-01-31` to `2026-05-31`, actual years approximately `6.33`; raw endpoints/cumulative return are not disclosed. Normalized end approximately `322.00` from the published rounded CAGR is a calculation, not a disclosed NAV endpoint.
- Official rolling 12-month observations from the 2026-05-31 factsheet are `26.97%`, `1.54%`, `17.88%`, `39.31%`, `6.90%`, and `50.56%` for 2020-06-01 to 2026-05-31; corresponding hedged FTSE Japan Index returns are `27.16%`, `1.94%`, `18.26%`, `39.68%`, `6.83%`, and `51.02%`. Complete calendar-year NAV rows were not disclosed in the reviewed official capture, so no calendar-year CAGR or up/down count is fabricated.
- S&P 500 TR uses cached USD rows as of `2025-12-31`; complete calendar years 2020-2025 compound to `132.26%` / CAGR `15.08%`. This is a reference-only comparison because dates do not match the fund's available-period window. Vanguard's official five-year NAV TR CAGR is `21.83%` as of `2026-05-31`; it is not a 10-year result.
- Official current observation: NAV `US$81.79` as of `2026-07-22`; latest standardized NAV TR YTD `19.41%` as of `2026-05-31`; 2026-07-22 YTD and daily history sufficient for drawdown/recovery are not disclosed in the reviewed official capture.

### VFJUF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:VJPU` | [Vanguard VJPU product page](https://www.vanguard.co.uk/professional/product/etf/equity/9541/ftse-japan-ucits-etf-usd-hedged-accumulating) | Canonical share-class mapping, LSE ticker, ISIN, fund identity, passive/physical classification, benchmark, inception, current NAV, holdings and risk data | Page accessed `2026-07-24`; NAV `2026-07-22`; holdings/risk `2026-06-30` |
| `OTC:VFJUF` | [OTC VFJUF market identity cross-check](https://stockanalysis.com/quote/otc/VFJUF/) | Secondary exchange-alias cross-check linking the input OTC symbol to Vanguard FTSE Japan UCITS ETF; canonical issuer share class remains `LSE:VJPU` | Page accessed `2026-07-24`; delayed market page, not used for NAV TR |
| `LSE:VJPU` | [Vanguard VJPU May 2026 factsheet](https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Hedged_Accumulating_9541_EU_INT_UK_EN.pdf) | Official NAV TR basis, available-period CAGR, five-year CAGR, YTD, rolling 12-month rows, fee and share-class details | Factsheet as of `2026-05-31` |
| `Vanguard Funds plc` | [Vanguard Funds plc annual report](https://fund-docs.vanguard.com/etf-annual-report.pdf) | Annual-report cross-check for USD-Hedged Accumulating inception and NAV total-return treatment | Reporting period ended `2025-06-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### VFJUF Raw Observations And Calculations

| Period | VJPU NAV TR | FTSE Japan Index Hedged in USD TR |
|---|---:|---:|
| 2020-06-01 to 2021-05-31 | 26.97% | 27.16% |
| 2021-06-01 to 2022-05-31 | 1.54% | 1.94% |
| 2022-06-01 to 2023-05-31 | 17.88% | 18.26% |
| 2023-06-01 to 2024-05-31 | 39.31% | 39.68% |
| 2024-06-01 to 2025-05-31 | 6.90% | 6.83% |
| 2025-06-01 to 2026-05-31 | 50.56% | 51.02% |

- Available-period official NAV TR CAGR is `20.29%` for `2020-01-31` to `2026-05-31`, actual years approximately `6.33`; normalized end is approximately `322.00` from `100 × (1 + 20.29%)^6.33`; raw endpoints are not disclosed.
- Official five-year NAV TR CAGR is `21.83%` as of `2026-05-31`; the official 10-year field is `—`, so the page is explicitly marked `10-year NAV TR unavailable`.
- S&P 500 cached rows for 2020-2025 are `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`; these compound to `132.26%` / CAGR `15.08%`, but the date window is not aligned with the fund's available-period return.
- Official current NAV TR YTD is `19.41%` as of `2026-05-31`; current `2026-07-22` YTD and daily history sufficient for max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

### VFJUF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE mapping, ISIN/share-class identity, passive-equity classification, inception and mandatory 10-year audit, official NAV TR/reinvestment/expense basis, rolling-period labels, available-period gap, S&P 500 basis/window, current-YTD as-of date, canonical filename, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## MCHS Sequential Queue Record

- Input row: `48/125`; input ticker: `MCHS`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NASDAQ:MCHS`; Matthews' official product page identifies Matthews China Innovators Active ETF (formerly Matthews China Discovery Active ETF), ticker `MCHS`, primary exchange `NASDAQ`, inception `2024-01-10`, and China geographic focus.
- Type gate: official objective and strategy state that the fund invests at least 80% in companies Matthews believes are innovators, using an active/fundamental approach. Matthews' launch material describes MCHS as an active ETF. This fails the required passive/index-tracking equity gate; it is not processed for historical NAV TR.
- No performance page, region/index performance row, annual table, S&P 500 comparison or 10-year audit was created because the type gate terminated the ticker as `unsupported ETF type`.

### MCHS Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:MCHS` | [Matthews China Innovators Active ETF product page](https://www.matthewsasia.com/funds/etfs/china-innovators-active-etf/) | Canonical exchange/ticker, current fund name, former name, inception, active strategy and geographic focus | Page accessed `2026-07-24`; performance page current capture as of `2026-06-30` |
| `NASDAQ:MCHS` | [Matthews MCHS factsheet](https://www.matthewsasia.com/siteassets/resources/fund-documents/factsheets/etfs/fact_sheet_mchs.pdf) | Official active classification, ticker, primary exchange, inception and expense ratios | Factsheet as of `2026-03-31` |
| `NASDAQ:MCHS` | [Matthews launch announcement](https://www.matthewsasia.com/about/our-story/press-releases/new-discovery-active-etfs/) | Independent issuer wording that MCHS launched as an active ETF on Nasdaq | Published `2024-01-11` |

### MCHS Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/ticker, issuer/fund identity, active-versus-passive type gate, unsupported-type reason, no-performance-page decision, source links/as-of dates, and next queue pointer.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ASIA Sequential Queue Record

- Input row: `50/125`; input ticker: `ASIA`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:ASIA`; Matthews' official product page identifies Matthews Pacific Tiger Active ETF, ticker `ASIA`, primary exchange NYSE Arca, inception `2023-09-21`, benchmark MSCI All Country Asia ex Japan Index, and gross expense ratio `0.79%`. No provider slug or guessed exchange is used.
- Type gate: Matthews describes the ETF as a high-conviction equity portfolio using an all-cap fundamental approach driven by proprietary research. The strategy invests at least 80% in common and preferred stocks of companies located in Asia ex Japan, but it is explicitly active rather than passive/index-tracking. This fails the required ETF scope and terminates the ticker as `unsupported ETF type`.
- No performance page, annual table, S&P 500 comparison, 10-year audit, region snapshot row or performance-index row was created because the type gate terminated the ticker.

### ASIA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ASIA` | [Matthews Pacific Tiger Active ETF product page](https://www.matthewsasia.com/funds/etfs/pacific-tiger-active-etf/) | Canonical exchange/ticker, fund identity, inception, active strategy, benchmark, geographic focus and fees | Page accessed `2026-07-24`; current product capture includes NAV/YTD fields as of `2026-07-16` |
| `NYSE Arca:ASIA` | [Matthews ASIA factsheet](https://www.matthewsasia.com/siteassets/resources/fund-documents/factsheets/etfs/fact_sheet_asia.pdf) | Official active classification, objective, strategy and fund facts cross-check | Factsheet accessed `2026-07-24`; current document |
| `Matthews Pacific Tiger Active ETF` | [Matthews ETF prospectus](https://www.matthewsasia.com/siteassets/resources/fund-documents/prospectus/etf-prospectus.pdf) | Legal/fund and active-strategy risk disclosure cross-check | Prospectus accessed `2026-07-24`; current document |

### ASIA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/ticker, issuer/fund identity, active-versus-passive type gate, unsupported-type reason, no-performance-page decision, source links/as-of dates, and next queue pointer.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## VFPAF Sequential Queue Record

- Input row: `51/125`; input ticker: `VFPAF`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `LSE:VAPU`; Vanguard's official USD accumulating share-class page and factsheet identify the fund as Vanguard FTSE Developed Asia Pacific ex Japan UCITS ETF (USD) Accumulating, ISIN `IE00BK5BQZ41`, London Stock Exchange USD ticker `VAPU`, share-class inception `2019-09-24`, physical investment method, and OCF `0.15%`. `VFPAF` is retained as the input OTC alias; the canonical issuer listing is not an OTC provider slug.
- Type gate: Vanguard describes a passive/indexing equity approach through physical acquisition or sampling of securities to track the FTSE Developed Asia Pacific ex Japan Index. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: rechecked the official product page, June 2026 factsheet and Vanguard Funds plc annual report/prospectus. The share-class inception is `2019-09-24`, and the official 10-year field is `—`; inception to `2026-06-30` is approximately `6.765` years. This is an actual history gap, not only a page gap, so `10-year NAV TR unavailable` is recorded.
- Official available-period performance: Vanguard reports since-inception NAV TR CAGR `13.96%` for the available share-class history through `2026-06-30`; raw start/end TR values and cumulative return are not disclosed. The official five-year NAV TR CAGR is `11.95%` as of `2026-06-30`; it is not a 10-year result.
- Official rolling 12-month observations: fund NAV TR net of expenses `44.95%`, `-21.91%`, `7.54%`, `7.31%`, `12.95%`, `72.75%` for `2020-07-01 to 2026-06-30` successive periods; corresponding benchmark rows are `45.13%`, `-21.88%`, `7.62%`, `7.41%`, `12.97%`, `72.97%`. Complete calendar-year NAV rows were not disclosed in the reviewed official capture.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; calendar reference `2020-2025` compounds to `132.26%` / CAGR `15.08%`, but this is not date-aligned with the fund's `2019-09-24` to `2026-06-30` available-period window.
- Official current observation: Vanguard reports NAV `US$55.71` as of `2026-07-22` and standardized NAV TR YTD `47.09%` as of `2026-06-30`; current `2026-07-22` date-to-date YTD and daily NAV history sufficient for drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

### VFPAF / VAPU Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:VAPU` | [Vanguard VAPU product page](https://www.vanguard.co.uk/uk-fund-directory/product/etf/equity/9676/ftse-developed-asia-pacific-ex-japan-ucits-etf-usd-accumulating) | Canonical share-class mapping, LSE ticker, ISIN, fund identity, passive/physical classification, benchmark, inception, current NAV, holdings and risk data | Page accessed `2026-07-24`; NAV `2026-07-22`; holdings/risk `2026-06-30` |
| `LSE:VAPU` | [Vanguard VAPU June 2026 factsheet](https://fund-docs.vanguard.com/FTSE_Developed_Asia_Pacific_ex_Japan_UCITS_ETF_USD_Accumulating_9676_EU_INT_UK_EN.pdf) | Official NAV TR basis, available-period CAGR, five-year CAGR, YTD, rolling 12-month rows, fee and share-class details | Factsheet as of `2026-06-30` |
| `Vanguard Funds plc` | [Vanguard Funds plc annual report](https://fund-docs.vanguard.com/etf-annual-report.pdf) | Annual-report cross-check for passive strategy, fund legal structure and tracking-error disclosure | Reporting period ended `2025-06-30` |
| `Vanguard Funds plc` | [Vanguard ETF prospectus](https://fund-docs.vanguard.com/etf-prospectus-en.pdf) | Legal/fund objective and risk cross-check | Current document accessed `2026-07-24` |
| `OTC:VFPAF` | [OTC VFPAF market identity cross-check](https://stockanalysis.com/quote/otc/VFPAF/) | Secondary alias/name/inception cross-check only; not used as NAV TR source | Page accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### VFPAF / VAPU Raw Observations And Calculations

| Period | VAPU NAV TR | FTSE Developed Asia Pacific ex Japan Index TR |
|---|---:|---:|
| 2020-07-01 to 2021-06-30 | 44.95% | 45.13% |
| 2021-07-01 to 2022-06-30 | -21.91% | -21.88% |
| 2022-07-01 to 2023-06-30 | 7.54% | 7.62% |
| 2023-07-01 to 2024-06-30 | 7.31% | 7.41% |
| 2024-07-01 to 2025-06-30 | 12.95% | 12.97% |
| 2025-07-01 to 2026-06-30 | 72.75% | 72.97% |

- Available-period official NAV TR CAGR is `13.96%` for `2019-09-24` to `2026-06-30`, actual years `6.765`; raw endpoints/cumulative return are `not disclosed`.
- Official five-year NAV TR CAGR is `11.95%` as of `2026-06-30`; the official 10-year field is `—`, so the performance page is explicitly marked `10-year NAV TR unavailable`.
- S&P 500 cached rows for calendar `2020-2025` are `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`; these compound to `132.26%` / CAGR `15.08%`, but the dates do not align with the fund's available-period window.
- Official current NAV TR YTD is `47.09%` as of `2026-06-30`; current `2026-07-22` date-to-date YTD and daily NAV history sufficient for max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

### VFPAF / VAPU Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, OTC-alias-to-LSE canonical resolution, ISIN/share-class match, fund identity, passive-equity classification, inception and mandatory 10-year eligibility audit, official NAV TR/reinvestment/expense basis, available-period and rolling rows, S&P 500 basis/window, current-YTD gap, rankings, canonical filename, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, old-link check, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## NBCE Sequential Queue Record

- Input row: `52/125`; input ticker: `NBCE`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:NBCE`; Neuberger's official China Equity ETF page identifies ticker `NBCE`, CUSIP `64135A507`, primary exchange NYSE Arca, ETF listing date `2023-10-16`, predecessor inception `2013-07-17`, equity asset class and reference benchmark MSCI China A Onshore Index (Net). No provider slug or guessed exchange is used.
- Type gate: the official issuer describes NBCE as an actively managed ETF that seeks broad onshore China equity exposure through fundamental/security-selection research; the issuer page explicitly labels the fund `Actively Managed`. It fails the required passive/index-tracking equity gate and terminates as `unsupported ETF type`.
- No performance page, annual table, S&P 500 comparison, 10-year audit, region snapshot row or performance-index row was created because the type gate terminated the ticker.

### NBCE Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:NBCE` | [Neuberger China Equity ETF product page](https://www.nb.com/products/etfs/china-equity-etf) | Canonical exchange/ticker, fund identity, active classification, listing date, predecessor inception, benchmark and fund facts | Page accessed `2026-07-24`; fund facts capture as of `2026-06-22` |
| `NYSE Arca:NBCE` | [Neuberger China Equity ETF factsheet](https://www.nb.com/handlers/documents.ashx?id=7455304d-2402-468d-bb78-92032237edd6&name=China+Equity+ETF+-+Factsheet) | Official active strategy and fund-facts cross-check | Factsheet as of `2026-03-31` |
| `Neuberger Berman ETF Trust` | [ETF Statement of Additional Information](https://www.nb.com/handlers/documents.ashx?id=47663e8f-0b22-4bda-b97c-4b535e979cab&name=Statement+of+Additional+Information+NBDS+NBCC+NBCT) | Legal/fund and exchange/ticker cross-check | SAI dated `2025-12-18` |

### NBCE Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/ticker, issuer/fund identity, active-versus-passive type gate, unsupported-type reason, no-performance-page decision, source links/as-of dates, and next queue pointer.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## JPY Sequential Queue Record

- Input row: `53/125`; input ticker: `JPY`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NASDAQ:JPY`; Lazard's official Japanese Equity ETF materials identify ticker `JPY`, CUSIP `52110K103`, NASDAQ exchange, inception `2025-04-04`, listing date `2025-04-07`, equity asset class, benchmark TOPIX with Dividend Index, and net expense ratio `0.60%`. No provider slug or guessed exchange is used.
- Type gate: Lazard describes JPY as an actively managed ETF designed to uncover opportunities and capitalize on market inefficiencies in Japanese equities, using a bottom-up stock-selection strategy. It fails the required passive/index-tracking equity gate and terminates as `unsupported ETF type`.
- No performance page, annual table, S&P 500 comparison, 10-year audit, region snapshot row or performance-index row was created because the type gate terminated the ticker.

### JPY Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:JPY` | [Lazard Japanese Equity ETF product page](https://www.lazardassetmanagement.com/us/en_us/investment-solutions/how-to-invest/etfs/japanese-equity-etf) | Canonical exchange/ticker, fund identity, active classification and strategy | Page accessed `2026-07-24`; current product page |
| `NASDAQ:JPY` | [Lazard JPY 1Q26 factsheet](https://www.lazardassetmanagement.com/content/dam/lazard-asset-management/lmap-documents/253582/294521.pdf) | Official active strategy, inception, exchange, benchmark and fee cross-check | Factsheet as of `2026-03-31` |
| `NASDAQ:JPY` | [Lazard active ETF launch release](https://www.lazardassetmanagement.com/ams/en_us/about/media-relations/press-releases/lazard-asset-management-launches-its-first-three-active-etfs-in-the-us) | Independent issuer wording that JPY launched as an actively managed ETF | Published `2025-04-07` |

### JPY Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/ticker, issuer/fund identity, active-versus-passive type gate, unsupported-type reason, no-performance-page decision, source links/as-of dates, and next queue pointer.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## FPA Sequential Queue Record

- Input row: `54/125`; input ticker: `FPA`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:FPA`; First Trust's official product page identifies First Trust Asia Pacific ex-Japan AlphaDEX Fund, CUSIP `33737J109`, ISIN `US33737J1097`, Nasdaq exchange, inception `2011-04-18`, tracked index Nasdaq AlphaDEX Asia Pacific Ex-Japan Index, and total expense ratio `0.80%` as of `2026-05-01`. No provider slug or guessed exchange is used.
- Type gate: the official prospectus states the fund is an exchange-traded index fund, not actively managed, seeking to correspond to the Nasdaq AlphaDEX Asia Pacific Ex-Japan Index. It is a passive/index-tracking equity ETF, not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: rechecked the current official product page, June 2026 monthly performance report and May 2026 prospectus. The official rolling 10-year field is `10.31%` as of `2026-06-30`; the window `2016-06-30` to `2026-06-30` is `10.00` elapsed years. This is confirmed 10-year coverage, not a proxy.
- Official rolling performance: First Trust reports NAV Total Return CAGR `10.31%` for the latest 10-year window; raw start/end TR values and cumulative rolling return are not disclosed.
- Official calendar observations: the May 2026 prospectus provides FPA NAV TR rows `2016-2025` of `0.29%`, `35.93%`, `-20.71%`, `7.35%`, `14.89%`, `2.75%`, `-15.62%`, `10.67%`, `3.84%`, and `42.31%`. These compound to `89.03%` / CAGR `6.57%`; common `2021-2025` rows compound to `41.79%` / CAGR `7.23%`.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common `2021-2025` S&P CAGR is `14.43%`, so FPA trails by approximately `7.20 pp` CAGR. S&P is kept separate from the issuer's Nasdaq AlphaDEX benchmark.
- Methodology gap: First Trust states the underlying index changed from Defined Asia Pacific Ex-Japan Index to Nasdaq AlphaDEX Asia Pacific Ex-Japan Index on `2015-10-13`; the page discloses this break and does not present pre-change returns as a pure current-index backtest.
- Official current observation: First Trust's June 2026 monthly performance report gives NAV TR YTD `42.71%` as of `2026-06-30`; later current date-to-date YTD and daily NAV history sufficient for max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture.

### FPA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:FPA` | [First Trust FPA product/performance page](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FPA) | Canonical listing, fund identity, Nasdaq exchange, inception, index objective, fees, holdings, risk and performance route | Page accessed `2026-07-24`; standardized product data through `2026-05-29` in page capture |
| `NASDAQ:FPA` | [First Trust June 2026 monthly performance report](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b363655b-cc73-4f42-a7b1-4c1e00306c7c) | Latest official standardized NAV TR 10-year CAGR, YTD, rolling performance and benchmark rows | Returns as of `2026-06-30` |
| `NASDAQ:FPA` | [First Trust Exchange-Traded AlphaDEX Fund II prospectus](https://www.ftportfolios.com/LoadContent/gradkqbz8r4y) | Passive/index-fund classification, calendar-year NAV TR rows `2016-2025`, index-change disclosure, expense and fund objective | Prospectus dated `2026-05-01`; calendar observations through `2025-12-31` |
| `NASDAQ:FPA` | [FPA fund documents route](https://www.ftportfolios.com/fund-documents/etf/FPA) | Official factsheet, prospectus, annual-report and disclosure route | Page accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### FPA Raw Observations And Calculations

| Year | FPA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.29% | 11.96% |
| 2017 | 35.93% | 21.83% |
| 2018 | -20.71% | -4.38% |
| 2019 | 7.35% | 31.49% |
| 2020 | 14.89% | 18.40% |
| 2021 | 2.75% | 28.71% |
| 2022 | -15.62% | -18.11% |
| 2023 | 10.67% | 26.29% |
| 2024 | 3.84% | 25.02% |
| 2025 | 42.31% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `10.31%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints/cumulative rolling return are `not disclosed`.
- Official calendar rows `2016-2025` compound to `+89.03%` and annualize to `6.57%`; positive / negative years are `8 / 2`.
- Common `2021-2025` FPA rows compound to `+41.79%` / CAGR `7.23%`; S&P 500 rows compound to `+96.17%` / CAGR `14.43%`; FPA trails by approximately `7.20 pp` CAGR.
- Official current NAV TR YTD is `+42.71%` as of `2026-06-30`; later current date-to-date YTD and daily NAV history sufficient for max drawdown and recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

### FPA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive/index-fund classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, current-YTD as-of date, index-methodology break, rankings, canonical filename, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## CXSE Sequential Queue Record

- Input row: `55/125`; input ticker: `CXSE`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:CXSE`; WisdomTree's official product page and factsheet identify WisdomTree China ex-State-Owned Enterprises Fund, NASDAQ listing, CUSIP `97717X719`, inception `2012-09-19`, tracked index `WisdomTree China ex-State-Owned Enterprises Index` / Bloomberg symbol `CHXSOE`, and net expense ratio `0.32%` as of `2026-07-22`. No provider slug or guessed exchange is used.
- Type gate: the official prospectus describes passive management/indexing with representative sampling and at least 80% of assets in index constituents or substantially identical securities. CXSE is a passive/index-tracking equity ETF, not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: rechecked the current WisdomTree product/performance page, 2025-12-31 official factsheet, 2024 and 2025 SEC summary prospectuses, and the official CHXSOE index page. The issuer's current month-end performance field confirms a genuine `10.00` elapsed-year NAV TR window from `2016-06-30` to `2026-06-30`; this is not a short-period proxy.
- Official rolling performance: WisdomTree reports NAV Total Return CAGR `6.85%` for the 10-year window; raw start/end TR values and cumulative rolling return are not disclosed.
- Official calendar observations: SEC prospectus charts provide CXSE NAV TR rows `2016-2024` of `-1.20%`, `78.04%`, `-27.95%`, `36.44%`, `60.58%`, `-23.77%`, `-28.89%`, `-18.67%`, and `9.59%`; the official WisdomTree factsheet as of `2025-12-31` provides 2025 `36.39%`. These compound to `82.98%` / CAGR `6.23%`; common `2021-2025` rows compound to `-34.10%` / CAGR `-8.00%`.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; common `2021-2025` S&P CAGR is `14.43%`, so CXSE trails by approximately `22.43 pp` CAGR. S&P is kept separate from CXSE's issuer benchmark.
- Methodology gap: the SEC prospectus states the fund objective changed on `2015-07-01`; performance before that date reflects the former WisdomTree China Dividend ex-Financials Fund and its former index. The 2016-2025 table is post-change history.
- Official current observation: WisdomTree reports NAV TR YTD `-3.69%` as of `2026-06-30` and latest NAV `US$38.035` as of `2026-07-22`; later current date-to-date YTD and daily NAV history sufficient for max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture.

### CXSE Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:CXSE` | [WisdomTree CXSE product/performance page](https://www.wisdomtree.com/us/products/equity/cxse) | Canonical listing, fund identity, passive/indexing objective, tracked index, inception, fee, rolling 10Y NAV TR, YTD, NAV and portfolio risk data | Page accessed `2026-07-24`; performance as of `2026-06-30`; product/NAV/holdings data through `2026-07-22` |
| `NASDAQ:CXSE` | [WisdomTree CXSE factsheet as of 2025-12-31](https://www.wisdomtree.com/nb-no/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-cxse-1061.pdf) | Official 2025 NAV annual return and fund/exchange/fee cross-check | Factsheet as of `2025-12-31` |
| `NASDAQ:CXSE` | [SEC CXSE summary prospectus, August 1, 2024](https://www.sec.gov/Archives/edgar/data/1350487/000121465924013472/cxse73024497k.htm) | Passive strategy, index definition, objective-change caveat and official 2016-2023 chart | Filing dated `2024-08-01`; chart through `2023-12-31` |
| `NASDAQ:CXSE` | [SEC CXSE summary prospectus, August 1, 2025](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011285/cxse73125497k.htm) | Official 2016-2024 chart and latest SEC performance disclosures | Filing dated `2025-08-01`; chart through `2024-12-31` |
| `NASDAQ:CXSE` | [WisdomTree CHXSOE index page](https://www.wisdomtree.com/us/indexes/chxsoe) | Index definition, total-return convention and index facts | Page accessed `2026-07-24`; index facts through `2026-07-14` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### CXSE Raw Observations And Calculations

| Year | CXSE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -1.20% | 11.96% |
| 2017 | 78.04% | 21.83% |
| 2018 | -27.95% | -4.38% |
| 2019 | 36.44% | 31.49% |
| 2020 | 60.58% | 18.40% |
| 2021 | -23.77% | 28.71% |
| 2022 | -28.89% | -18.11% |
| 2023 | -18.67% | 26.29% |
| 2024 | 9.59% | 25.02% |
| 2025 | 36.39% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `6.85%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints/cumulative rolling return are `not disclosed`.
- Official calendar rows `2016-2025` compound to `+82.98%` and annualize to `6.23%`; positive / negative years are `5 / 5`.
- Common `2021-2025` CXSE rows compound to `-34.10%` / CAGR `-8.00%`; S&P 500 rows compound to `+96.17%` / CAGR `14.43%`; CXSE trails by approximately `22.43 pp` CAGR.
- Official current NAV TR YTD is `-3.69%` as of `2026-06-30`; later current date-to-date YTD and daily NAV history sufficient for max drawdown and recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

### CXSE Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive/indexing classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual rows, S&P 500 basis/window, current-YTD as-of date, objective/index change, rankings, canonical filename, China region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## IPAC Sequential Queue Record

- Input row: `49/125`; input ticker: `IPAC`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:IPAC`; iShares' official product page identifies iShares Core MSCI Pacific ETF, primary exchange NYSE Arca, inception `2014-06-10`, asset class Equity, tracked index MSCI Pacific IMI Index (Net), and expense ratio `0.09%`. No provider slug or guessed exchange is used.
- Type gate: official iShares materials describe a passive/index-tracking equity ETF. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: the prior page had no verified inception, tracked index or rolling 10-year result. Rechecking the current official product page, factsheet, summary prospectus and semi-annual report confirms a genuine `10.00` elapsed-year NAV TR window `2016-06-30` to `2026-06-30`; this was a page gap, not an actual history gap.
- Official rolling performance: iShares reports NAV Total Return cumulative `141.81%` and average annual `9.23%` for the 10-year window. Raw start/end NAV TR values are not disclosed; normalized TR is `100.00` to `241.81` from the published cumulative result.
- Official calendar observations: the reviewed iShares performance capture provides NAV and MSCI Pacific IMI Index (Net) rows for `2021-2025`: NAV `3.03%`, `-13.31%`, `14.33%`, `5.56%`, `25.62%`; benchmark `2.53%`, `-13.06%`, `14.36%`, `6.26%`, `24.42%`. Rows for `2016-2020` are not disclosed and are left as `not disclosed`.
- Common `2021-2025` IPAC NAV rows compound to `35.41%` / CAGR `6.25%`; S&P 500 cached USD Total Return rows compound to `96.17%` / CAGR `14.43%`; IPAC trails by approximately `8.18 pp` CAGR.
- S&P 500 rows use the cached USD Total Return convention as of `2025-12-31`; this is a common reference benchmark, kept separate from IPAC's issuer benchmark.
- Official current observation: iShares reports NAV Total Return YTD `13.75%` as of `2026-07-22`; the prior page's `13.97%` observation was stale and is superseded by the later official as-of date. Daily NAV history sufficient for max drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### IPAC Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:IPAC` | [iShares IPAC product and performance page](https://www.ishares.com/us/products/264619/ishares-core-msci-pacific-etf) | Canonical listing, fund identity, passive-equity classification, tracked index, inception, fees, rolling 10Y NAV TR, annual rows, current YTD and risk/holdings data | Page accessed `2026-07-24`; rolling/annual performance `2026-06-30`; current YTD `2026-07-22`; holdings/risk `2026-07-22` |
| `NYSE Arca:IPAC` | [iShares IPAC factsheet](https://www.ishares.com/us/literature/fact-sheet/ipac-ishares-core-msci-pacific-etf-fund-fact-sheet-en-us.pdf) | Official factsheet cross-check for fund identity, benchmark, fee, performance and calendar observations | Factsheet accessed `2026-07-24`; performance through `2026-06-30` |
| `NYSE Arca:IPAC` | [iShares IPAC summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-msci-pacific-etf-7-31.pdf) | Legal/fund objective and passive/index-tracking structure cross-check | Prospectus accessed `2026-07-24` |
| `NYSE Arca:IPAC` | [iShares semi-annual report](https://www.ishares.com/us/literature/semi-annual-report/sar-ipac-en.pdf) | Issuer report and NAV/performance-document route cross-check | Report accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### IPAC Raw Observations And Calculations

| Year | IPAC NAV TR | MSCI Pacific IMI Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 3.03% | 2.53% | 28.71% |
| 2022 | -13.31% | -13.06% | -18.11% |
| 2023 | 14.33% | 14.36% | 26.29% |
| 2024 | 5.56% | 6.26% | 25.02% |
| 2025 | 25.62% | 24.42% | 17.88% |

- Official rolling 10-year NAV TR is `+141.81%` with CAGR `9.23%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to `241.81`, actual years `10.00`; raw endpoints are not disclosed.
- Official disclosed calendar rows `2021-2025` compound to `+35.41%` and annualize to `6.25%`; positive / negative years are `4 / 1`.
- S&P 500 TR rows `2021-2025` compound to `+96.17%` and annualize to `14.43%`; IPAC trails by approximately `8.18 pp` CAGR in that common window.
- Official current NAV TR YTD is `+13.75%` as of `2026-07-22`; daily NAV history sufficient for max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### IPAC Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, annual-row gap, S&P 500 basis/window, current-YTD as-of date, rankings, canonical filename, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ADVE Sequential Queue Record

- Input row: `56/125`; input ticker: `ADVE`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:ADVE`; Matthews' official fund page identifies the ticker, fund name, and primary exchange. No provider slug or guessed exchange is used.
- Type gate: Matthews identifies ADVE as the Matthews Asia Dividend Active ETF, an unconstrained all-cap portfolio with a quality bias. Its strategy states that, under normal circumstances, at least `80%` of net assets are invested in dividend-paying equity securities of companies located in Asia, and the official prospectus lists the fund among the issuer's active ETFs. This is active management rather than passive/index tracking, so the ETF performance workflow stops at the type gate.
- Mandatory 10-year coverage audit: not applicable after the confirmed unsupported-type classification. No NAV Total Return history, annual-return table, S&P 500 comparison, or proxy was created.

### ADVE Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ADVE` | [Matthews Asia Dividend Active ETF product page](https://us.matthewsasia.com/funds/etfs/asia-dividend-active-etf/) | Canonical ticker/exchange, fund identity, active strategy, objective, geographic focus, and inception | Page accessed `2026-07-24`; fund facts and strategy current on page; inception `2023-09-21` |
| `NYSE Arca:ADVE` | [Matthews Asia Funds ETF prospectus](https://www.matthewsasia.com/siteassets/resources/fund-documents/prospectus/etf-prospectus.pdf) | Official prospectus cross-check for active-fund lineup, strategy, and listing venue | Prospectus dated `2026-04-30`; ADVE fund summary and listing note |

### ADVE Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, unsupported-type reason, no accidental performance-page creation, source URLs, ledger update, queue pointer, and no region/index navigation update for an unsupported ETF.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## THD Sequential Queue Record

- Input row: `60/125`; input ticker: `THD`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:THD`; iShares' official product page identifies iShares MSCI Thailand ETF, primary exchange NYSE Arca, inception `2008-03-26`, asset class Equity, tracked index `MSCI Thailand IMI 25/50 Index (Net)`, and expense ratio `0.59%`. The input ticker is already the issuer-qualified U.S. listing; no provider slug or guessed exchange is used.
- Type gate: official iShares materials describe a passive/indexing approach for Thai equities. The fund is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy ETF. The summary prospectus states that at least 80% of assets normally goes to index constituents or economically equivalent DRs, with limited permitted use of futures/options/swaps/cash.
- Mandatory 10-year audit: official iShares performance data provides a genuine `10.00` elapsed-year NAV Total Return window from `2016-06-30` to `2026-06-30`. The issuer reports NAV TR average annual return/CAGR `3.35%`; raw start/end NAV TR values are not disclosed. Normalized calculation is `100.00 × (1 + 3.35%)^10.00 = 139.03`, clearly labeled as derived from the official CAGR rather than raw NAV.
- Official calendar observations: factsheet rows provide THD NAV TR `1.66%`, `1.55%`, `-12.18%`, `-1.85%`, `0.87%` for `2021-2025`; issuer benchmark rows are `1.89%`, `1.80%`, `-12.20%`, `-1.69%`, `1.00%`. Current factsheet capture did not disclose THD or benchmark rows for `2016-2020`; those cells remain `not disclosed`.
- Common `2021-2025` THD NAV rows compound to `-10.24%` / CAGR `-2.14%`; S&P 500 cached USD Total Return rows compound to `+96.17%` / CAGR `14.43%`; THD trails by approximately `16.56 pp` CAGR. Positive / negative years are `2 / 3`; best is `2022` at `1.55%`, worst is `2023` at `-12.18%`.
- Benchmark caveat: iShares states that THD began tracking `MSCI Thailand IMI 25/50 Index` on `2013-02-12`; earlier history used MSCI Thailand Investable Market Index (Net). The issuer benchmark remains separate from the common S&P 500 comparison.
- Official current observation: product page reports NAV Total Return YTD `25.53%` as of `2026-07-22`, 82 holdings as of `2026-07-22`, 3-year standard deviation `21.96%`, P/E `17.92`, and P/B `1.82` on the current page. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### THD Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:THD` | [iShares THD product and performance page](https://www.ishares.com/us/products/239688/ishares-msci-thailand-capped-etf) | Canonical listing, fund identity, passive/index classification, tracked index, inception, fee, rolling 10Y NAV TR, current NAV/YTD, holdings and risk data | Page accessed `2026-07-24`; rolling/annual performance `2026-06-30`; current NAV/YTD and current metrics `2026-07-22` |
| `NYSE Arca:THD` | [iShares THD factsheet](https://www.ishares.com/us/literature/fact-sheet/thd-ishares-msci-thailand-etf-fund-fact-sheet-en-us.pdf) | Official factsheet cross-check for objective, benchmark, index-history change, NAV TR basis, annual rows and rolling performance | Factsheet accessed `2026-07-24`; performance through `2026-06-30` |
| `NYSE Arca:THD` | [iShares THD summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-thailand-capped-etf-8-31.pdf) | Legal/fund objective and passive/indexing structure, sampling and permitted derivative-use cross-check | Prospectus accessed `2026-07-24`; current prospectus dated `2025-08-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31`; rows reused for `2016-2025` without a new search |

### THD Raw Observations And Calculations

| Year | THD NAV TR | MSCI Thailand IMI 25/50 Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 1.66% | 1.89% | 28.71% |
| 2022 | 1.55% | 1.80% | -18.11% |
| 2023 | -12.18% | -12.20% | 26.29% |
| 2024 | -1.85% | -1.69% | 25.02% |
| 2025 | 0.87% | 1.00% | 17.88% |

- Official rolling 10-year NAV TR CAGR is `3.35%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; normalized TR is `100.00` to approximately `139.03`; raw endpoints are not disclosed.
- THD official `2021-2025` rows compound to `-10.24%` and annualize to `-2.14%`; S&P 500 TR rows compound to `+96.17%` and annualize to `14.43%`; THD trails by approximately `16.56 pp` CAGR.
- Positive / negative years in the complete THD rows are `2 / 3`; best is `2022 +1.55%`; worst is `2023 -12.18%`. Current official NAV TR YTD is `+25.53%` as of `2026-07-22`; it is not treated as a complete calendar year.

### THD Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, normalized endpoint disclosure, annual-row gaps, S&P 500 basis/window, benchmark/index change, current-YTD as-of date, rankings, canonical filename, Thailand region assignment, canonical geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## FLIN Sequential Queue Record

- Input row: `61/125`; input ticker: `FLIN`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:FLIN`; Franklin's official product page identifies Franklin FTSE India ETF, primary exchange NYSE Arca, ticker FLIN, inception `2018-02-06`, asset class Equity, ETF type Indexed, benchmark `FTSE India Capped Index-NR`, and net expense ratio `0.19%`. No provider slug or guessed exchange is used.
- Type gate: Franklin describes passive index exposure to a market-cap weighted large- and mid-cap India index. The summary prospectus states that at least 80% of assets normally goes to FTSE India Capped Index components or related depositary receipts. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy ETF.
- Mandatory 10-year audit: official Franklin product page and June 2026 factsheet show the 10-year field as `—`; inception `2018-02-06` means the available period through `2026-06-30` is only `8.39` years. The workflow therefore records `10-year NAV TR unavailable`, not a shorter period labeled as 10-year.
- Official available-period performance: Franklin reports NAV Returns annualized `5.91%` from `2018-02-06` through `2026-06-30`. Raw start/end NAV TR values are not disclosed. Normalized calculation is `100.00 × (1 + 5.91%)^8.394 = 161.93`, clearly labeled as derived from the issuer-reported available-period annualized return.
- Official calendar observations: factsheet NAV rows are `4.93%`, `15.16%`, `24.82%`, `-8.19%`, `20.71%`, `10.47%`, `2.21%` for `2019-2025`; matching benchmark rows are `6.38%`, `16.53%`, `28.77%`, `-8.36%`, `25.30%`, `12.99%`, `3.84%`. The `2018` inception year is partial and retained as `not applicable`, not ranked as a complete year.
- Complete `2019-2025` FLIN NAV rows compound to `88.74%` / CAGR `9.50%`; benchmark rows compound to `115.06%` / CAGR `11.56%`. Common `2021-2025` FLIN NAV rows compound to `56.19%` / CAGR `9.33%`; S&P 500 cached USD Total Return rows compound to `96.17%` / CAGR `14.43%`; FLIN trails by approximately `5.10 pp` CAGR. Positive / negative years are `4 / 1`; best is `2021 +24.82%`, worst is `2022 -8.19%`.
- Official current observation: Franklin factsheet reports NAV TR YTD `-8.34%` as of `2026-06-30`; the product page separately shows NAV `$35.30` and YTD `-8.31%` as of `2026-06-23`, which is earlier and is not mixed into the month-end standardized metric. Factsheet reports 283 holdings, 3-year NAV standard deviation `15.09%`, P/E `21.58x`, and P/B `3.34x` as of `2026-06-30`. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### FLIN Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FLIN` | [Franklin FLIN product and performance page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26348/SINGLCLASS/franklin-ftse-india-etf/FLIN) | Canonical listing, fund identity, passive/index classification, benchmark, inception, fee, current NAV/YTD and performance field | Page accessed `2026-07-24`; current snapshot NAV/YTD `2026-06-23`; standardized performance field `2026-05-31` |
| `NYSE Arca:FLIN` | [Franklin FLIN factsheet](https://www.franklintempleton.com/forms-literature/download/FLIN-FF) | Official factsheet for objective, benchmark, equity/index classification, inception, fee, annual NAV/index rows, available-period NAV TR, current YTD and risk statistics | Factsheet as of `2026-06-30`; accessed `2026-07-24` |
| `NYSE Arca:FLIN` | [Franklin FLIN summary prospectus](https://www.franklintempleton.com/tools-and-resources/literature/info/FLIN-PSUM) | Legal/fund objective and passive 80% index-investment structure, index construction and risks | Publication August `2025`; accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31`; rows reused for `2016-2025` without a new search |

### FLIN Raw Observations And Calculations

| Year | FLIN NAV TR | FTSE India Capped Index-NR TR | S&P 500 TR |
|---|---:|---:|---:|
| 2018 | not applicable (partial inception year) | not applicable (partial inception year) | -4.38% |
| 2019 | 4.93% | 6.38% | 31.49% |
| 2020 | 15.16% | 16.53% | 18.40% |
| 2021 | 24.82% | 28.77% | 28.71% |
| 2022 | -8.19% | -8.36% | -18.11% |
| 2023 | 20.71% | 25.30% | 26.29% |
| 2024 | 10.47% | 12.99% | 25.02% |
| 2025 | 2.21% | 3.84% | 17.88% |

- Official available-period NAV TR annualized return is `5.91%` for `2018-02-06` to `2026-06-30`, actual years `8.394` (displayed as `8.39`); normalized TR is `100.00` to approximately `161.93`; raw endpoints are not disclosed. `10-year NAV TR unavailable`.
- Complete `2019-2025` FLIN rows compound to `+88.74%` / CAGR `9.50%`; matching benchmark rows compound to `+115.06%` / CAGR `11.56%`.
- Common `2021-2025` FLIN rows compound to `+56.19%` / CAGR `9.33%`; S&P 500 TR rows compound to `+96.17%` / CAGR `14.43%`; FLIN trails by approximately `5.10 pp` CAGR. Positive / negative years are `4 / 1`; best `2021 +24.82%`; worst `2022 -8.19%`.
- Official standardized NAV TR YTD is `-8.34%` as of `2026-06-30`; it is not treated as a complete calendar year.

### FLIN Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and under-10-year eligibility audit, official NAV TR/reinvestment/expense basis, available-period normalized endpoint disclosure, annual rows, partial inception-year marker, S&P 500 basis/window, current-YTD as-of date, rankings, canonical filename, India region assignment, canonical geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## CNYA Sequential Queue Record

- Input row: `62/125`; input ticker: `CNYA`; terminal status: `completed_10Y`.
- Canonical entity key: `Cboe BZX:CNYA`; iShares' official product page identifies iShares MSCI China A ETF, Cboe BZX listing, inception `2016-06-13`, asset class Equity, benchmark `MSCI China A Inclusion Index`, and expense ratio `0.60%`. No provider slug or guessed exchange is used.
- Type gate: official iShares materials describe a passive/index-tracking equity ETF investing in Chinese equities traded on the Shanghai or Shenzhen exchanges. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy ETF. The fund uses Stock Connect to access A-shares; the prospectus remains the source for detailed permitted instruments and risks.
- Mandatory 10-year audit: official iShares performance data provides a genuine `10.00` elapsed-year NAV Total Return window from `2016-06-30` to `2026-06-30`. The issuer reports NAV/Total Return cumulative `91.51%` and CAGR `6.71%`; raw start/end NAV TR values are not disclosed. Normalized TR is `100.00` to `191.51` from the published cumulative result.
- Official calendar observations: iShares provides CNYA NAV rows `2.96%`, `-26.31%`, `-13.51%`, `11.08%`, `25.59%` for `2021-2025`; benchmark rows are `3.20%`, `-25.90%`, `-13.47%`, `11.70%`, `26.48%`. Rows for `2016-2020` are not disclosed in the reviewed current product/factsheet capture; `2016` is retained as a partial inception marker.
- Common `2021-2025` CNYA NAV rows compound to `-8.46%` / CAGR `-1.75%`; benchmark rows compound to `-6.52%` / CAGR `-1.34%`; S&P 500 cached USD Total Return rows compound to `+96.17%` / CAGR `14.43%`; CNYA trails S&P by approximately `16.18 pp` CAGR. Positive / negative years are `3 / 2`; best is `2025 +25.59%`, worst is `2022 -26.31%`.
- Benchmark caveat: iShares states that CNYA began tracking `MSCI China A Inclusion Index (Net)` on `2018-04-26`; historical index data before that date is for MSCI China A International Index. Benchmark rows are kept separate from the fund NAV TR metric and the common S&P 500 comparison.
- Official current observation: iShares reports NAV Total Return YTD `5.39%` as of `2026-07-21`; NAV is `$36.26` as of `2026-07-21`. The standardized month-end performance table separately reports 2026 YTD `12.01%` and benchmark `11.74%` as of `2026-06-30`; these dates are not mixed. Current page reports 411 holdings as of `2026-07-21`, 3-year standard deviation `19.36%` as of `2026-06-30`, P/E `18.42`, and P/B `2.02` as of `2026-07-21`. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

### CNYA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Cboe BZX:CNYA` | [iShares CNYA product and performance page](https://www.ishares.com/us/products/273318/ishares-msci-china-a-etf) | Canonical listing, fund identity, passive-equity classification, benchmark, inception, fee, rolling 10Y NAV TR, annual rows, current NAV/YTD, holdings and risk data | Page accessed `2026-07-24`; rolling/annual performance `2026-06-30`; current NAV/YTD `2026-07-21` |
| `Cboe BZX:CNYA` | [iShares CNYA factsheet](https://www.ishares.com/us/literature/fact-sheet/cnya-ishares-msci-china-a-etf-fund-fact-sheet-en-us.pdf) | Official factsheet cross-check for objective, benchmark, index change, fee, calendar rows, NAV TR basis and risk data | Factsheet as of `2026-03-31`; accessed `2026-07-24` |
| `Cboe BZX:CNYA` | [iShares CNYA summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-a-etf-7-31.pdf) | Legal/fund objective and passive/indexing structure, Stock Connect and risk cross-check | Prospectus dated `2025-11-28`; accessed `2026-07-24` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31`; rows reused for `2016-2025` without a new search |

### CNYA Raw Observations And Calculations

| Year | CNYA NAV TR | MSCI China A Inclusion Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not applicable (partial inception year) | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 2.96% | 3.20% | 28.71% |
| 2022 | -26.31% | -25.90% | -18.11% |
| 2023 | -13.51% | -13.47% | 26.29% |
| 2024 | 11.08% | 11.70% | 25.02% |
| 2025 | 25.59% | 26.48% | 17.88% |

- Official rolling 10-year NAV TR cumulative is `+91.51%` with CAGR `6.71%` for `2016-06-30` to `2026-06-30`, actual years `10.00`; normalized TR is `100.00` to `191.51`; raw endpoints are not disclosed.
- Common `2021-2025` CNYA NAV rows compound to `-8.46%` / CAGR `-1.75%`; issuer benchmark rows compound to `-6.52%` / CAGR `-1.34%`; S&P 500 TR rows compound to `+96.17%` / CAGR `14.43%`; CNYA trails by approximately `16.18 pp` CAGR.
- Positive / negative years in the complete CNYA rows are `3 / 2`; best `2025 +25.59%`; worst `2022 -26.31%`. Current official NAV TR YTD is `+5.39%` as of `2026-07-21`; it is not treated as a complete calendar year.

### CNYA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, normalized endpoint disclosure, annual-row gap, S&P 500 basis/window, current-YTD as-of date separation, benchmark change, rankings, canonical filename, China region assignment, canonical geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.
