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

ใช้ `check-etf-performance` sequential queue ต่อจาก row `17/125`. รอบนี้ตรวจ FLKR และ VPL ตามลำดับทีละ ticker, ทำ mandatory 10-year coverage audit จาก official product page/factsheet, และใช้ local pre-save fallback เนื่องจากไม่มี independent reviewer.

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Source URL | Gap / resolution note |
|---|---|---|---|---|---|---|
| FLKR | supported | NYSE Arca:FLKR | South Korea | 86.35% (2026-07-07) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26353/SINGLCLASS/franklin-ftse-south-korea-etf/FLKR | official inception 2017-11-02; issuer 10-year NAV return `—`; available official annual rows 2018-2025 |
| VPL | supported | NYSE Arca:VPL | Asia-Pacific | 19.62% (2026-07-17) | https://investor.vanguard.com/investment-products/etfs/profile/vpl | official rolling 10Y NAV TR 177.37% / CAGR 10.74% as of 2026-05-31; annual NAV TR rows 2016-2025 |
| ISSSF | supported | LSE:SAUS | Australia | 10.27% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/251851/ishares-msci-australia-ucits-etf | OTC alias; official rolling 10Y NAV TR 121.17% / CAGR 8.26% as of 2026-06-30; annual NAV TR rows 2016-2025 |

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
