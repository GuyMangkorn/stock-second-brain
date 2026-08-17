---
type: source-batch
topic: ETF performance
accessed: 2026-08-17
input_source: Trello ETF child cards GSSC, XSMO, SSEUF, FNDA, ZPRVF, NUSC, IMWSF, DES, FNDC, RWJ, ISHOF, DISV, CPLCF, BSVO, FYX, IWMI, VB, SCHA, SPSM, VBR, VTWO, VSS, IJR, IWM, IWN, IWO, AVUV, DFAS, AVDV, SCZ, BBSC, ISCF
input_count: 32
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## IWMI unsupported ETF type

| Scope | Source | Role | Evidence |
|---|---|---|---|
| IWMI | https://www.sec.gov/Archives/edgar/data/1848758/000199937126009956/iwmi-497k_050126.htm | Official SEC summary prospectus for NEOS Russell 2000® High Income ETF | Dated 2026-05-01; principal strategy identifies the fund as actively managed, uses Russell 2000 exposure plus written/sold RUT call options, and states the fund is not an index fund |
| IWMI | https://www.cboe.com/us/equities/notices/new_listings/details/?etf=true&firm_name=NEOS+Investment+Management+LLC&first_trade_dt=2024-06-25&ipo=true&symbols=IWMI | Official exchange listing confirmation | Cboe BZX listing for NEOS Russell 2000 High Income ETF, first trading date 2024-06-25 |

## IWMI scheduled-inline local review

- Status: `PASS` for the type gate; `BLOCKED` for ETF v1 performance processing.
- Confirmed the canonical fund identity as NEOS Russell 2000® High Income ETF (IWMI), Cboe BZX listing, active management, and options overlay from the official SEC prospectus.
- Classification: unsupported ETF type because the fund is actively managed and derivative-heavy rather than a passive index-tracking equity ETF.
- No performance page, region row, performance-index row, or ETF performance calculations were written.
- Local pre-save result: `PASS` for the blocking decision.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

annual_rows_as_of: "GSSC official 2018-2025; XSMO official 2016-2025; SSEUF canonical LSE:R2US official 2016-2025; FNDA secondary 2016-2025; ZPRVF canonical LSE:USSC official 2016-2025; NUSC official 2017-2025; IMWSF canonical LSE:WSML official 2019-2025; DES official 2016-2025; FNDC official 2016-2025; RWJ secondary 2016-2025; ISHOF canonical LSE:IDP6 official 2016-2025; DISV unsupported active ETF; CPLCF canonical LSE:CUSS official 2016-2025; BSVO unsupported active ETF; FYX official 2016-2025; IWMI unsupported active ETF; VB official 2016-2025; SCHA secondary 2016-2025; SPSM calendar rows not disclosed; VBR official 2016-2025; VTWO official 2016-2025; VSS official 2016-2025; IJR official 2016-2025; IWM official 2016-2025 at 0.1% precision; IWN official 2016-2025 at 0.1% precision; IWO official 2016-2025 at 0.1% precision; AVUV unsupported active ETF; DFAS unsupported active ETF; AVDV unsupported active ETF; SCZ official 2016-2025; BBSC official 2021-2025; ISCF official 2016-2024 SEC and 2025 factsheet; current NAV/YTD fields through 2026-08-15; S&P current cross-check through 2026-08-10"
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-08-17

## Scope and gate

Research-bearing lean source batch for GSSC, XSMO, SSEUF, FNDA, ZPRVF, NUSC, IMWSF, DES, FNDC, RWJ, ISHOF, DISV, CPLCF, BSVO, FYX, IWMI, VB, SCHA, SPSM, VBR, VTWO, VSS, IJR, IWM, IWN, IWO, AVUV, DFAS, AVDV, SCZ, BBSC, and ISCF. Source discovery, reading, reconciliation,
calculation, synthesis, and the complete pre-save checklist were performed
inline under `scheduled-inline`. No research worker, reviewer,
`source_verifier`, or other sub-agent was dispatched.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## DISV unsupported ETF record

- Input ticker: `DISV`; canonical identity: `Cboe BZX:DISV`; fund: Dimensional International Small Cap Value ETF; inception `2022-03-23`.
- Type gate: `unsupported ETF type`. Dimensional describes its ETF lineup as active ETFs, and the SEC summary prospectus identifies DISV as the Dimensional International Small Cap Value ETF with a long-term capital-appreciation objective rather than a passive index-tracking mandate. The reviewed ETF reference also identifies `No Underlying Index` / active management; this fails ETF v1’s passive, index-tracking equity scope.
- No NAV performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was created after the type gate. Current return observations were not used as performance evidence.

### DISV Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `Cboe BZX:DISV` | https://www.sec.gov/Archives/edgar/data/0001816125/000181612526000069/c497k.htm | Official SEC summary prospectus: fund identity, exchange, objective and formal fund context | Prospectus dated 2026-02-28 |
| `Cboe BZX:DISV` | https://www.cboe.com/us/equities/listings/listed_products/symbols/DISV | Official exchange listing and fund identity cross-check | Listing page reviewed 2026-08-17 |
| `Cboe BZX:DISV` | https://www.dimensional.com/us-en/etfs | Official issuer ETF lineup; Dimensional describes the lineup as active ETFs | Issuer page reviewed 2026-08-17 |
| `Cboe BZX:DISV` | https://www.ifa.com/pdfs/fund-documents/disv-fact-sheet.pdf | Secondary/authorized-distributor factsheet: active international small-cap value description, fee and benchmark context | Factsheet as of 2025-12-31; used only to corroborate classification |

### DISV scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, issuer classification, active/passive type gate, index status, scope exclusion, source URLs/as-of dates, no-performance-artifact decision, card result metadata, and next-card sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance artifact was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## ISHOF / IDP6 official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:IDP6 / input ISHOF | https://www.ishares.com/uk/individual/en/products/251920/ishares-s-p-smallcap-600-ucits-etf?siteEntryPassthrough=true | Official iShares product page: identity, listings, ISIN, index, structure, expense ratio, NAV, YTD, risk fields and calendar NAV TR rows | Product/current fields through 2026-07-31; NAV TR YTD through 2026-07-30; calendar rows 2016-2025 |
| LSE:IDP6 / input ISHOF | https://www.blackrock.com/uk/professional/en/literature/fact-sheet/isp6-ishares-s-p-smallcap-600-ucits-etf-fund-fact-sheet-en-gb.pdf | Official factsheet: USD distributing share class and calendar NAV performance | Calendar rows 2016-2025; factsheet capture dated 2026-03-31 / 2026-04-14 fields |
| LSE:IDP6 / input ISHOF | https://www.ishares.com/uk/professional/en/literature/kiid/ucits_kiid-ishares-sp-smallcap-600-ucits-etf-usd-dist-gb-ie00b2qwcy14-en.pdf | Official KIID: passive objective, benchmark, NAV return definition and small-cap/liquidity risk | KIID reviewed 2026-08-17 |
| S&P 500 TR current | https://www.slickcharts.com/sp500/returns/ytd | Secondary current benchmark cross-check | `10.14%` total return YTD through 2026-07-31; one day later than IDP6 current YTD |

## ISHOF / IDP6 raw observations and calculations

| Year | IDP6 NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 25.93% | 11.96% |
| 2017 | 12.62% | 21.83% |
| 2018 | -8.95% | -4.38% |
| 2019 | 22.04% | 31.49% |
| 2020 | 10.64% | 18.40% |
| 2021 | 26.25% | 28.71% |
| 2022 | -16.72% | -18.11% |
| 2023 | 15.43% | 26.29% |
| 2024 | 8.04% | 25.02% |
| 2025 | 5.55% | 17.88% |
| 2026 YTD | 21.36% | 10.14%† |

- Metric basis: official iShares NAV Total Return, with gross income reinvested where applicable and performance after ongoing charges; USD share-class values are used for the canonical USD line.
- `†` secondary S&P 500 current cross-check with a different as-of date; complete-year benchmark rows use the cached project convention.
- 2016-2025 IDP6 compound: `141.31%` cumulative; rounded-input CAGR `9.21%`.
- 2021-2025 IDP6 compound: `38.40%` cumulative; rounded-input CAGR `6.72%`.
- Annual-row positive/negative years: `8 / 2`; best 2016 `+25.93%`, worst 2022 `-16.72%`.
- Official current NAV TR YTD: `21.36%` as of 2026-07-30; NAV quote `US$117.48` as of 2026-07-31.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## ISHOF / IDP6 gaps, alias resolution, and scheduled-local gate

- ISHOF is an OTC input alias; official iShares listings for ISIN `IE00B2QWCY14` identify the USD London line as `IDP6`, while `ISP6` is the GBP London line of the same fund. Durable ownership uses `LSE:IDP6` and preserves ISHOF as `input_alias`.
- The latest official iShares current NAV TR field located is `21.36%` as of 2026-07-30. The latest displayed NAV quote is `US$117.48` as of 2026-07-31; these are separate as-of fields.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Complete pre-save checklist: identity/exchange/index, alias and ISIN, return basis, benchmark, candidate claims, periods, units/currencies, metric definitions, as-of dates, calculations, source URLs, unresolved gaps, exact planned page/batch/index/log contents, graph links, and ownership were reviewed locally before write.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Primary source | Gap / resolution note |
|---|---|---|---|---|---|---|
| GSSC | supported | NYSE Arca:GSSC | USA | 21.33% (2026-06-30) | https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681 | passive/index-tracking U.S. small-cap multi-factor equity; 10-year history not yet available; daily NAV drawdown/recovery not disclosed |
| XSMO | supported | NYSE Arca:XSMO | USA | 30.50% (2026-06-30, secondary NAV) | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/xsmo-invesco-s-p-smallcap-momentum-etf-fact-sheet.pdf | passive/index-tracking U.S. small-cap momentum equity; official current YTD not located; daily NAV drawdown/recovery not disclosed |
| SSEUF | supported | LSE:R2US | USA | 18.69% (2026-07-31) | https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-russell-2000-us-small-cap-ucits-etf-acc-zprr-gy | OTC alias for official USD LSE line; passive/index-tracking U.S. small-cap equity; daily NAV drawdown/recovery not disclosed |
| FNDA | supported | NYSE Arca:FNDA | USA | 21.18% (2026-06-30) | https://www.schwabassetmanagement.com/products/fnda | passive/index-tracking U.S. small-cap fundamental equity; annual calendar rows are secondary total-return proxy; daily NAV drawdown/recovery not disclosed |
| NUSC | supported | Cboe BZX:NUSC | USA | 16.76% (2026-06-30) | https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?uniqueId=8238272c-9326-4c32-93cb-40d80e4fc4a9 | passive/index-tracking U.S. small-cap ESG equity; history under 10 years; Nuveen HTML performance table rendered no records, official PDF factsheet used; daily NAV drawdown/recovery not disclosed |
| IMWSF | supported | LSE:WSML | International | 19.00% (2026-08-13) | https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-fund?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official USD LSE line by ISIN `IE00BF4RFH31`; passive/global developed small-cap equity; history under 10 years; daily NAV drawdown/recovery not disclosed |
| DES | supported | NYSE Arca:DES | USA | 22.93% (2026-07-31) | https://www.wisdomtree.com/us/products/equity/des | passive/index-tracking U.S. small-cap dividend equity; official 2016-2025 annual NAV rows; current S&P cross-check is not same-date; daily NAV drawdown/recovery not disclosed |
| FNDC | supported | NYSE Arca:FNDC | International | 10.96% (2026-07-31) | https://www.schwabassetmanagement.com/products/fndc | passive/index-tracking developed ex-U.S. small-cap fundamental equity; benchmark changed effective 2024-06-21; daily NAV drawdown/recovery not disclosed |
| RWJ | supported | NYSE Arca:RWJ | USA | 28.61% (2026-08-14, secondary proxy) | https://www.sec.gov/Archives/edgar/data/1378872/000119312525325669/d54028d497k.htm | passive/index-tracking U.S. small-cap revenue-weighted equity; annual/current fields use secondary dividend-reinvested proxy; official SEC average annual return kept separate |
| ISHOF | supported | LSE:IDP6 | USA | 21.36% (2026-07-30) | https://www.ishares.com/uk/individual/en/products/251920/ishares-s-p-smallcap-600-ucits-etf?siteEntryPassthrough=true | OTC alias resolved to official USD LSE line by ISIN; passive U.S. small-cap equity; daily NAV drawdown/recovery not disclosed |
| DISV | unsupported | Cboe BZX:DISV | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/0001816125/000181612526000069/c497k.htm | actively managed/no passive index-tracking mandate; no performance artifact created |
| CPLCF | supported | LSE:CUSS | USA | 14.97% (2026-07-29) | https://www.ishares.com/uk/individual/en/products/253480/cuss?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official USD LSE line by ISIN; passive U.S. small-cap ESG equity; benchmark changed 2022-06-01; daily NAV drawdown/recovery not disclosed |
| BSVO | unsupported | Nasdaq:BSVO | not assigned | not applicable | https://bridgewayetfs.com/bsvo/ | actively managed small-cap value ETF; no passive index-tracking mandate; no performance artifact created |
| FYX | supported | NASDAQ:FYX | USA | 28.10% (2026-06-30) | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FYX | passive/indexing U.S. small-cap rules-based equity; official 2016-2025 rows; index changed 2026-04-08; daily NAV drawdown/recovery not disclosed |
| IWMI | unsupported | Cboe BZX:IWMI | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1848758/000199937126009956/iwmi-497k_050126.htm | actively managed and written-call options ETF; not a passive index-tracking equity ETF; no performance artifact created |
| VB | supported | NYSE Arca:VB | USA | 19.48% (2026-08-07) | https://investor.vanguard.com/investment-products/etfs/profile/vb | passive/index-tracking U.S. small-cap equity; official 2016-2025 rows and rolling 10-year field; daily NAV drawdown/recovery not disclosed |
| SCHA | supported | NYSE Arca:SCHA | USA | 18.27% (2026-07-31) | https://www.schwabassetmanagement.com/products/scha | passive/index-tracking U.S. small-cap equity; official current/rolling fields, secondary annual proxy; daily NAV drawdown/recovery not disclosed |
| SPSM | supported | NYSE Arca:SPSM | USA | 21.54% (2026-07-31) | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-600-small-cap-etf-spsm | passive/index-tracking U.S. small-cap equity; issuer calendar rows and raw 10-year endpoints not disclosed; benchmark continuity is disclosed |
| IWN | supported | NYSE Arca:IWN | USA | 25.91% (2026-08-13) | https://www.ishares.com/us/products/239712/ishares-russell-2000-value-etf | passive/index-tracking U.S. small-cap value equity; official 2016-2025 rows at 0.1% precision; daily NAV drawdown/recovery not disclosed |
| IWO | supported | NYSE Arca:IWO | USA | 21.61% (2026-08-13) | https://www.ishares.com/us/products/239709/ishares-russell-2000-growth-etf | passive/index-tracking U.S. small-cap growth equity; official 2016-2025 rows at 0.1% precision; daily NAV drawdown/recovery not disclosed |
| AVUV | unsupported | NYSE Arca:AVUV | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000416/acetftavuv497k.htm | actively managed and does not seek to replicate a specified index; outside passive index-tracking equity scope; no performance artifact created |
| DFAS | unsupported | NYSE Arca:DFAS | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000081/c497k.htm | actively managed and does not seek to replicate a specific index; outside passive index-tracking equity scope; no performance artifact created |
| AVDV | unsupported | NYSE Arca:AVDV | not assigned | not applicable | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000402/acetftavdv497k.htm | actively managed and does not seek to replicate a specified index; outside passive index-tracking equity scope; no performance artifact created |
| SCZ | supported | NASDAQ:SCZ | International | 13.83% (2026-08-13) | https://www.ishares.com/us/products/239627/ | passive/index-tracking developed ex-U.S./Canada small-cap equity; official 2016-2025 rows; daily NAV drawdown/recovery not disclosed |
| BBSC | supported | Cboe BZX:BBSC | USA | 23.96% (2026-06-30) | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBSC.PDF | passive/index-tracking U.S. small-cap equity; history under 10 years; exchange transfer from NYSE Arca to Cboe BZX resolved; daily NAV drawdown/recovery not disclosed |
| ISCF | supported | NYSE Arca:ISCF | International | 12.52% (2026-08-13) | https://www.ishares.com/us/products/272823/ishares-international-small-cap-equity-factor-etf | passive/index-tracking international small-cap factor equity; benchmark changed from MSCI World ex USA Small Cap Diversified Multiple-Factor Index to STOXX International Small-Cap Equity Factor Index on 2023-03-01; daily NAV drawdown/recovery not disclosed |

## GSSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:GSSC | https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681 | Official Goldman Sachs product/fact card: fund identity, exchange, inception, expense ratio, NAV return definition, annual NAV rows, current NAV/YTD | Annual rows 2018-2025 and performance fields as of 2026-06-30 |
| NYSE Arca:GSSC | https://www.sec.gov/Archives/edgar/data/1479026/000119312525334837/d72082d497k.htm | SEC summary prospectus: passive objective, issuer benchmark, inception, NAV return definition, and risk quarters | Filed 2025-12-29; performance period through 2024-12-31; best/worst quarter disclosures |
| NYSE Arca:GSSC | https://www.sec.gov/Archives/edgar/data/1479026/000119312526206736/d120512dncsrs.htm | SEC semi-annual report: current fund classification and expense observation | Period ended 2026-02-28; annualized fund cost 0.20% |
| NYSE Arca:GSSC | https://www.etfcentral.com/fund/GSSC | Secondary current price/NAV and YTD context | Snapshot updated 2026-07-27; return basis not used for NAV TR ranking |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused for eligible 2018-2019 rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused for 2018-2022 rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused for 2022-2025 rows |

## GSSC raw observations and calculations

| Year | GSSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -8.72% | -4.38% |
| 2019 | 23.43% | 31.49% |
| 2020 | 15.80% | 18.40% |
| 2021 | 24.05% | 28.71% |
| 2022 | -16.87% | -18.11% |
| 2023 | 17.37% | 26.29% |
| 2024 | 10.94% | 25.02% |
| 2025 | 10.71% | 17.88% |
| 2026 YTD | 21.33% | not available from cached current-year benchmark |

- Metric basis: official GSSC NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: Goldman Sachs ActiveBeta U.S. Small Cap Equity Index; retained as metadata and not substituted for the common S&P 500 reference.
- 2018-2025 GSSC compound: `93.95%` cumulative; rounded-input CAGR `8.63%`.
- 2021-2025 GSSC compound: `48.66%` cumulative; rounded-input CAGR `8.25%`.
- S&P 500 cached 2018-2025 compound: `192.03%` cumulative; rounded-input CAGR `14.33%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official fact card also reports 5-year annualized NAV TR `8.46%` and since-inception annualized NAV TR `10.86%` as of 2026-06-30; these are not relabelled as a 10-year CAGR.
- Official prospectus risk observations: best quarter `+29.24%` in 4Q2020; worst quarter `-30.94%` in 1Q2020.

## GSSC gaps and conflicts

- Inception is 2017-06-28, so the 2017 partial year is excluded from complete-year ranking and the official history is under 10 years as of 2026-06-30.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- The latest official NAV TR YTD field located is 21.33% as of 2026-06-30. A later secondary snapshot reports a different YTD figure with an unclear return basis, so it is not mixed into the NAV table.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## VBR official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:VBR` | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F0937.pdf | Official Vanguard factsheet: passive/full-replication structure, benchmark, expense ratio, exchange, inception, annualized NAV TR, current YTD, and standard deviation | Factsheet as of 2026-06-30; annual rows through 2025-12-31 |
| `NYSE Arca:VBR` | https://investor.vanguard.com/investment-products/etfs/profile/vbr | Official Vanguard performance/quote page: annual NAV TR rows and price/NAV inputs | Annual rows as of 2025-12-31; quote as of 2026-06-18 |
| `NYSE Arca:VBR` | https://advisors.vanguard.com/content/dam/fas/pdfs/MRSTR.pdf | Official Vanguard ticker/CUSIP name-change list | New name effective 2026-07-29; ticker VBR and CUSIP 922908611 |
| `NYSE Arca:VBR` | https://corporate.vanguard.com/content/corporatesite/us/en/corp/who-we-are/pressroom/press-release-vanguard-to-update-names-of-us-equity-index-funds-tracking-morningstar-indexes-042926.html | Official Vanguard rebrand release: effective date and unchanged objective/management | Published 2026-04-29; changes effective 2026-07-29 |
| `NYSE Arca:VBR` | https://www.sec.gov/Archives/edgar/data/36405/000003640526000204/f44857d1.htm | SEC summary prospectus: passive objective, full replication, benchmark context, and fee schedule | Filed 2026-04-28 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## VBR raw observations and calculations

| Year | VBR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 24.80% | 11.96% |
| 2017 | 11.79% | 21.83% |
| 2018 | -12.22% | -4.38% |
| 2019 | 22.76% | 31.49% |
| 2020 | 5.82% | 18.40% |
| 2021 | 28.07% | 28.71% |
| 2022 | -9.29% | -18.11% |
| 2023 | 16.00% | 26.29% |
| 2024 | 12.39% | 25.02% |
| 2025 | 9.09% | 17.88% |
| 2026 YTD | 15.83% NAV / 15.92% market price | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:VBR`; current fund name `Vanguard Morningstar Small-Cap Value ETF`; passive, full-replication U.S. small-cap value equity ETF; inception `2004-01-26`; USD.
- Current issuer benchmark: `Morningstar US Small Cap Value Index`, formerly `CRSP US Small Cap Value Index`; Bloomberg ticker `CRSPSCVT`. The rebrand is effective 2026-07-29 and Vanguard states it does not change the investment objective or management.
- Metric basis: official Vanguard NAV Total Return is pre-tax, net of expenses, with dividends and capital-gains distributions reinvested. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Official period-ended-2026-06-30 fields: NAV YTD `15.83%`, market-price YTD `15.92%`, issuer benchmark YTD `15.86%`, 1-year `27.01%`, 3-year annualized `16.08%`, 5-year annualized `9.23%`, 10-year annualized `10.99%`, since-inception annualized `9.51%`, and three-year standard deviation `16.43%`.
- Latest captured quote: market price `US$238.40`, NAV `US$238.46`, quote date 2026-06-18; price/NAV discount `= 238.40 / 238.46 - 1 = -0.025%`, displayed as `-0.03%`.
- Using published rounded annual NAV returns, VBR 2016-2025 cumulative `162.85%`, CAGR `10.15%`, and 2021-2025 cumulative `65.22%`, CAGR `10.56%`; up/down count `8 / 2`, best `2021 +28.07%`, worst `2018 -12.22%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## VBR gaps, reconciliation, and scheduled-local gate

- The official English 2026-06-30 factsheet and historical Vanguard page retain the former CRSP wording for the reviewed performance rows; the official 2026 name-change list and release establish the current Morningstar name/index and effective date. The durable page preserves both labels and does not infer a strategy change.
- The issuer 10-year annualized field `10.99%` is retained as an official average annual return for the period ended 2026-06-30. Raw TR endpoints and exact elapsed years were not disclosed, so no endpoint-derived cumulative value is asserted.
- No newer official price/NAV quote than 2026-06-18 was verified; current YTD performance is available through 2026-06-30. Dates remain separate in the performance page.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric drawdown proxy is saved.
- Complete pre-save checklist: canonical ticker/exchange, current and former fund/index names, passive-equity type, return basis, distributions, annual rows, cached S&P 500 window, 10-year field and gap, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## VTWO official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:VTWO` | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3351.pdf | Official Vanguard factsheet: passive/full-replication structure, Russell 2000 benchmark, expense ratio, exchange, inception, annualized NAV TR, current YTD, assets, and standard deviation | Factsheet as of 2026-06-30; annualized fields through 2026-06-30 |
| `NASDAQ:VTWO` | https://investor.vanguard.com/investment-products/etfs/profile/vtwo | Official Vanguard performance/quote page: complete annual NAV TR rows and price/NAV inputs | Annual rows as of 2025-12-31; quote as of 2026-06-22 |
| `NASDAQ:VTWO` | https://fund-docs.vanguard.com/FA3351_SPM.pdf | Official Vanguard factsheet mirror used to reconcile fund identity, exchange, return basis, and risk fields | Same 2026-06-30 data as the English factsheet |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## VTWO raw observations and calculations

| Year | VTWO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 21.33% | 11.96% |
| 2017 | 14.70% | 21.83% |
| 2018 | -10.98% | -4.38% |
| 2019 | 25.61% | 31.49% |
| 2020 | 20.10% | 18.40% |
| 2021 | 14.81% | 28.71% |
| 2022 | -20.40% | -18.11% |
| 2023 | 17.00% | 26.29% |
| 2024 | 11.57% | 25.02% |
| 2025 | 12.88% | 17.88% |
| 2026 YTD | 22.60% NAV TR | not available from cached current-year benchmark |

- Canonical identity: `NASDAQ:VTWO`; Vanguard Russell 2000 ETF; passive, full-replication U.S. small-cap broad equity ETF; inception `2010-09-20`; USD; issuer benchmark `Russell 2000 Index`.
- Metric basis: official Vanguard NAV Total Return is pre-tax, net of expenses, with dividends and capital-gains distributions reinvested. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Official period-ended-2026-06-30 fields: NAV YTD `22.60%`, market-price YTD `22.63%`, issuer benchmark YTD `22.57%`, 1-year `40.87%`, 3-year annualized `18.65%`, 5-year annualized `7.03%`, 10-year annualized `11.68%`, since-inception annualized `11.55%`, and three-year standard deviation `19.99%`.
- Latest captured quote: market price `US$120.46`, NAV `US$120.52`, quote date 2026-06-22; price/NAV discount `= 120.46 / 120.52 - 1 = -0.050%`, displayed as `-0.05%`.
- Using published rounded annual NAV returns, VTWO 2016-2025 cumulative `151.67%`, CAGR `9.67%`, and 2021-2025 cumulative `34.66%`, CAGR `6.13%`; up/down count `8 / 2`, best `2019 +25.61%`, worst `2022 -20.40%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## VTWO gaps, reconciliation, and scheduled-local gate

- The Vanguard profile's complete annual table as of 2025-12-31 is used for the 2016-2025 calendar window. A later quarterly capture can show revised-looking historical rows; those observations are not mixed into this complete-calendar table.
- Separate Vanguard advisor/fund-list captures returned different YTD or inception metadata in the reviewed HTML context, including an inconsistent inception display and YTD values that did not match the direct 2026-06-30 factsheet. The direct factsheet and product-profile identity (`2010-09-20`) are retained; the conflicting captures are not used as performance inputs.
- The issuer 10-year annualized field `11.68%` is retained as an official average annual return for the period ended 2026-06-30. Raw TR endpoints and exact elapsed years were not disclosed, so no endpoint-derived cumulative value is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric drawdown proxy is saved. Quarterly distributions are disclosed, but the reviewed sources do not provide a complete distribution schedule in the performance table.
- Complete pre-save checklist: canonical ticker/exchange, fund/index identity, passive-equity type, return basis, distributions, annual rows, cached S&P 500 window, 10-year field and gap, current YTD, quote inputs, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## VSS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:VSS` | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3184.pdf | Official Vanguard factsheet: passive/index-sampling structure, FTSE benchmark, expense ratio, exchange, inception, annualized NAV TR, current factsheet YTD, distributions, holdings, and standard deviation | Factsheet as of 2026-06-30; current factsheet YTD `8.18%`, rolling 10-year `8.26%`, standard deviation `14.43%` vs benchmark `15.27%` |
| `NYSE Arca:VSS` | https://advisors.vanguard.com/investments/products/vss/vanguard-ftse-all-world-ex-us-small-cap-etf | Official Vanguard product/quote page: complete annual NAV TR rows, rolling 10-year field, and later price/NAV/YTD capture | Annual rows as of 2025-12-31; rolling 10-year `7.42%` as of 2026-07-31; quote and current YTD as of 2026-08-11 |
| `NYSE Arca:VSS` | https://investor.vanguard.com/investment-products/etfs/profile/vss | Official Vanguard product-page identity and performance-page cross-check | Accessed 2026-08-17; dynamic page did not expose stable line-level data in the web capture |
| `NYSE Arca:VSS` | https://fund-docs.vanguard.com/p3184.pdf | Official Vanguard prospectus: legal fund identity, benchmark, and strategy context | Reviewed with the prior source batch; fee effective 2026-02-27 |
| VSS drawdown context | https://totalrealreturns.com/n/VSS | Secondary price total-return history | Data ending 2026-08-10; drawdown proxy only, not NAV Total Return |

## VSS raw observations and calculations

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
| 2026 current | 10.86% NAV / 11.40% market price | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:VSS`; Vanguard FTSE All-World ex-US Small-Cap ETF; passive/index-tracking equity ETF using index sampling; inception `2009-04-02`; USD; issuer benchmark `FTSE Global Small Cap ex US Index` (`TGPVA09U`).
- Metric basis: official Vanguard NAV Total Return is pre-tax, net of expenses, with dividends and capital-gains distributions reinvested. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Latest product-page capture: market price `US$158.81`, NAV `US$158.05`, price/NAV premium `0.48%`, NAV YTD `10.86%`, and market-price YTD `11.40%`, all as of 2026-08-11.
- Official factsheet cross-check as of 2026-06-30: NAV YTD `8.18%`, market-price YTD `8.23%`, issuer benchmark YTD `7.53%`, 1-year `18.74%`, 3-year annualized `15.50%`, 5-year annualized `5.71%`, 10-year annualized `8.26%`, since-inception annualized `9.51%`, and standard deviation `14.43%` versus benchmark `15.27%`.
- Using published rounded annual NAV returns, VSS 2016-2025 cumulative `106.58%`, CAGR `7.53%`, and 2021-2025 cumulative `36.70%`, CAGR `6.45%`; up/down count `8 / 2`, best `2017 +30.26%`, worst `2022 -21.22%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## VSS gaps, reconciliation, and scheduled-local gate

- The latest product-page capture through 2026-08-11 is used for current YTD and quote fields. The 2026-06-30 factsheet is retained for the standardized current facts and risk cross-check; the two as-of windows are not mixed.
- The issuer rolling 10-year NAV TR field is `7.42%` as of 2026-07-31, while the factsheet's earlier 2026-06-30 field is `8.26%`; both are official issuer fields for different month-end windows and raw TR endpoints are not disclosed.
- Official complete-calendar-year NAV rows are available for 2016-2025. Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; the secondary `-43.51%` price total-return drawdown ending 2020-03-23 and current `-2.11%` price drawdown ending 2026-08-10 remain clearly marked as non-NAV context.
- Complete pre-save checklist: canonical ticker/exchange, international primary region, passive-equity type, return basis, distributions, annual rows, cached S&P 500 window, current/rolling fields, standard-deviation fields, quote inputs, separate as-of dates, calculations, source URLs, candidate page/source-batch contents, International navigation link, canonical tags, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## IJR official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:IJR` | https://www.ishares.com/us/products/239774/ishares-core-sp-smallcap-etf?fundSearch=true&qt=IJR | Official iShares product page: identity, exchange, benchmark, inception, expense ratio, current NAV/price, premium/discount, current YTD, rolling annualized return, standard deviation, and calendar rows | Current NAV/price as of 2026-08-14; NAV YTD as of 2026-08-13; rolling 10-year field as of 2026-06-30; standard deviation as of 2026-07-31; annual rows through 2025-12-31 |
| `NYSE Arca:IJR` | https://www.ishares.com/us/literature/fact-sheet/ijr-ishares-core-s-p-small-cap-etf-fund-fact-sheet-en-us.pdf | Official iShares factsheet: passive/index-tracking objective, S&P SmallCap 600 benchmark, calendar rows, fee, exchange, distributions, and risk fields | Factsheet as of 2026-06-30; standard deviation `19.42%` and annual rows 2021-2025 |
| `NYSE Arca:IJR` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-s-and-p-small-cap-etf-3-31.pdf | Official iShares summary prospectus: fund identity, strategy, benchmark, and fee context | Current prospectus source reviewed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| IJR drawdown context | https://totalrealreturns.com/s/IJR | Secondary price total-return history | Drawdown context only; not authoritative NAV maximum drawdown/recovery |

## IJR raw observations and calculations

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
| 2026 current | 25.09% NAV TR | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:IJR`; iShares Core S&P Small-Cap ETF; passive/index-tracking U.S. small-cap equity ETF; inception `2000-05-22`; USD; issuer benchmark `S&P SmallCap 600 Index` (`SPTRSMCP`).
- Metric basis: official iShares NAV Total Return includes reinvested dividends/distributions after fund expenses. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Latest official product-page fields: NAV `US$150.41`, closing price `US$150.44`, premium/discount `0.02%`, all as of 2026-08-14; NAV Total Return YTD `25.09%` as of 2026-08-13; three-year standard deviation `19.36%` as of 2026-07-31; quarterly distributions.
- Official issuer 10-year NAV Total Return annualized field is `11.47%` as of 2026-06-30. This is retained separately from the rounded-input 2016-2025 calendar CAGR `9.76%`; raw endpoints are not used to derive a second cumulative value.
- Using published rounded annual NAV returns, IJR 2016-2025 cumulative `153.87%`, CAGR `9.76%`, and 2021-2025 cumulative `41.75%`, CAGR `7.23%`; up/down count `8 / 2`, best `2021 +26.69%`, worst `2022 -16.20%`.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## IJR gaps, reconciliation, and scheduled-local gate

- The direct iShares product page supplies current NAV/price/YTD fields through 2026-08-14/13, while annualized 10-year and standard-deviation fields have separate June/July month-end as-of dates; these dates remain explicit and are not combined.
- The factsheet's 2026-06-30 standard deviation is `19.42%`; the later product-page field is `19.36%` as of 2026-07-31 and is used for the current page risk snapshot.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified. Secondary price-total-return sources report materially different methodology outputs, so they remain context only and no authoritative NAV recovery date is asserted.
- Complete pre-save checklist: canonical ticker/exchange, passive-equity type, return basis, benchmark identity, annual rows, cached S&P 500 window, issuer 10-year field and calendar CAGR separation, current YTD/quote fields, standard deviation, distributions, units/currencies, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## IWM official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:IWM` | https://www.ishares.com/us/products/239710/ishares-russell-2000-etf | Official iShares U.S. product page: identity, exchange, Russell 2000 benchmark, inception, fee, current NAV/price, premium/discount, current YTD, rolling annualized return, standard deviation, and 2021-2025 calendar rows | Current NAV/price as of 2026-08-14; NAV YTD as of 2026-08-13; rolling 10-year field as of 2026-06-30; standard deviation as of 2026-07-31 |
| `NYSE Arca:IWM` | https://www.ishares.com/us/literature/fact-sheet/iwm-ishares-russell-2000-etf-fund-fact-sheet-en-us.pdf | Official iShares factsheet: passive/index-tracking objective, benchmark, fee, exchange, distribution frequency, 2021-2025 calendar rows, and risk fields | Factsheet as of 2026-06-30; standard deviation `19.98%`; annual rows 2021-2025 |
| `NYSE Arca:IWM` | https://www.ishares.com/uk/professionals/en/products/239710/ishares-russell-2000-etf?siteEntryPassthrough=true&switchLocale=y | Official BlackRock/iShares professional page used for the complete 2016-2025 calendar table | 2016-2020 rows are published at 0.1% precision; table capture accessed 2026-08-17 |
| `NYSE Arca:IWM` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-russell-2000-etf-3-31.pdf | Official iShares summary prospectus: fund objective, passive index exposure, benchmark, and fee context | Current prospectus source reviewed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| IWM drawdown context | https://totalrealreturns.com/n/IWM | Secondary price total-return history | Context only; not authoritative NAV maximum drawdown/recovery |

## IWM raw observations and calculations

| Year | IWM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 21.4% | 11.96% |
| 2017 | 14.7% | 21.83% |
| 2018 | -11.0% | -4.38% |
| 2019 | 25.4% | 31.49% |
| 2020 | 19.9% | 18.40% |
| 2021 | 14.6% | 28.71% |
| 2022 | -20.5% | -18.11% |
| 2023 | 16.8% | 26.29% |
| 2024 | 11.4% | 25.02% |
| 2025 | 12.7% | 17.88% |
| 2026 current | 23.73% NAV TR | not available from cached current-year benchmark |

- Canonical identity: `NYSE Arca:IWM`; iShares Russell 2000 ETF; passive/index-tracking U.S. small-cap equity ETF; inception `2000-05-22`; USD; issuer benchmark `Russell 2000 Index` (`RU20INTR`).
- Metric basis: official iShares NAV Total Return includes reinvested dividends/distributions after fund expenses. The S&P 500 comparison is the cached USD Total Return convention with dividends reinvested.
- Latest official product-page fields: NAV `US$304.98`, closing price `US$305.09`, premium/discount `0.04%`, all as of 2026-08-14; NAV Total Return YTD `23.73%` as of 2026-08-13; three-year standard deviation `19.97%` as of 2026-07-31; quarterly distributions.
- Official issuer 10-year NAV Total Return annualized field is `11.53%` as of 2026-06-30. This is retained separately from the rounded-input 2016-2025 calendar CAGR `9.55%`; raw endpoints are not used to derive a second cumulative value.
- The official BlackRock/iShares professional page publishes the complete 2016-2025 rows at 0.1% precision. Using those consistent rounded inputs, IWM 2016-2025 cumulative `148.94%`, CAGR `9.55%`, and 2021-2025 cumulative `33.60%`, CAGR `5.96%`; up/down count `8 / 2`, best `2019 +25.4%`, worst `2022 -20.5%`.
- The current U.S. factsheet gives a higher-precision 2021-2025 cross-check (`14.62%`, `-20.48%`, `16.80%`, `11.35%`, `12.69%`); those rows are not mixed into the complete 0.1%-precision calculation.
- S&P 500 cached 2016-2025 cumulative `298.33%`, CAGR `14.82%`; 2021-2025 cumulative `96.17%`, CAGR `14.43%`.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## IWM gaps, reconciliation, and scheduled-local gate

- The direct U.S. iShares page supplies current NAV/price/YTD fields through 2026-08-14/13, while the issuer 10-year field is as of 2026-06-30 and standard deviation is as of 2026-07-31; dates remain explicit.
- The complete official 2016-2025 table used for calculation is available at 0.1% precision in the professional iShares capture. The U.S. factsheet's exact 2021-2025 rows are retained as a reconciliation note, not silently substituted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; secondary price-total-return history remains context only and no authoritative NAV recovery date is asserted.
- Complete pre-save checklist: canonical ticker/exchange, passive-equity type, return basis, benchmark identity, annual rows and precision, cached S&P 500 window, issuer 10-year field and calendar CAGR separation, current YTD/quote fields, standard deviation, distributions, units/currencies, as-of dates, calculations, source URLs, candidate page/source-batch contents, USA navigation link, canonical tag, and single log bullet were reviewed locally. No critical/high finding remained.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## VB official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:VB | https://investor.vanguard.com/investment-products/etfs/profile/vb | Official Vanguard product page: identity, annual NAV/market-price returns, rolling return, current NAV/price, historical-price observations, and current-period fields | Latest numeric product-page capture retained through 2026-08-07; direct scheduled recheck on 2026-08-17 found no newer machine-readable current return field |
| NYSE Arca:VB | https://fund-docs.vanguard.com/F0969.pdf | Official Vanguard factsheet: passive/full-replication approach, benchmark, expense ratio, NAV return definition, current YTD, rolling returns, standard deviation, holdings and fund facts | Factsheet as of 2026-06-30 |
| NYSE Arca:VB | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/investment-profiles/0969.pdf | Official Vanguard investment profile: complete annual and quarterly NAV return rows, recent distributions, risk measures and fund facts | Profile as of 2026-06-30; annual rows through 2025-12-31 |
| NYSE Arca:VB | https://www.sec.gov/Archives/edgar/data/36405/000003640526000206/f44854d1.htm | SEC summary prospectus: structure, passive index exposure and expense-ratio evidence | Prospectus dated 2026-04-28 |
| NYSE Arca:VB | https://advisors.vanguard.com/content/dam/fas/pdfs/MRSTR.pdf | Official Vanguard name-change list | Morningstar fund/benchmark names effective 2026-07-29; VB CUSIP 922908751 |
| NYSE Arca:VB | https://www.vanguardmexico.com/es/inicio/noticias/name-changes-for-vanguard-equity-index-funds-and-crsp-morningstar-benchmarks | Official Vanguard transition notice | Name-only CRSP → Morningstar transition; objectives, strategy, index construction, ticker, CUSIP and expense ratios unchanged |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## VB raw observations and calculations

| Year | VB NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 18.31% | 11.96% |
| 2017 | 16.24% | 21.83% |
| 2018 | -9.30% | -4.38% |
| 2019 | 27.37% | 31.49% |
| 2020 | 19.08% | 18.40% |
| 2021 | 17.72% | 28.71% |
| 2022 | -17.60% | -18.11% |
| 2023 | 18.21% | 26.29% |
| 2024 | 14.23% | 25.02% |
| 2025 | 8.83% | 17.88% |
| 2026 YTD | 19.48% (official NAV) | 13.58% (official S&P 500 TR, as of 2026-08-05; not synchronized) |

- Metric basis: official VB NAV Total Return in USD, with dividends and capital-gains distributions reinvested and fund expenses reflected in NAV.
- Issuer benchmark: Morningstar US Small Cap Index, formerly CRSP US Small Cap Index; the 2026-07-29 change is a name transition and is not treated as a methodology change.
- VB 2016-2025 compound: `169.68%` cumulative; rounded-input CAGR `10.43%`.
- VB 2021-2025 compound: `42.55%` cumulative; rounded-input CAGR `7.35%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR: `10.90%` annualized as of 2026-07-31; raw rolling endpoints are not disclosed and this field is not relabelled as the 2016-2025 calendar CAGR.
- Official 36-month monthly standard deviation: `17.26%` as of 2026-06-30.
- Quarter-end NAV-TR drawdown calculation: high-water index `1.58849` at 2019-12-31 to trough `1.11067` at 2020-03-31 equals `-30.08%`; recovery index `1.89154` at 2020-12-31 confirms the prior peak was recovered. This is not a daily maximum-drawdown series.
- Official recent distributions visible in the investment profile: ex-dividend 2026-06-26 `US$0.89` and 2026-03-27 `US$0.98`; payment dates are not disclosed in the reviewed capture.

## VB gaps, conflicts, and scheduled-inline local review

- The current product-page return snapshot is as of 2026-08-07 while factsheet/risk fields are as of 2026-06-30 and rolling 10-year return is as of 2026-07-31; these are kept separate.
- The 2026-07-29 CRSP → Morningstar change is a name/benchmark-label transition; Vanguard states that objectives, strategies, index construction, rebalancing, securities, ticker, CUSIP and expense ratios are unchanged.
- Official daily NAV history sufficient for a daily maximum drawdown and recovery calculation was not verified; the quarter-end calculation and monthly NAV-price-only proxy remain clearly labelled and are not substituted for daily NAV TR.
- Local pre-save result: `PASS`. Confirmed canonical identity `NYSE Arca:VB`, passive/full-replication classification, current fund/benchmark naming, official 2016-2025 annual rows, current YTD, rolling 10-year field, S&P cache basis/window, calculations, distribution observations, USA region ownership, breadcrumb links, and disclosed gaps.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## SCHA official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:SCHA | https://www.schwabassetmanagement.com/products/scha | Official Schwab Asset Management product page: objective, index, passive style, expense ratio, current NAV/AUM/holdings, current returns, risk fields and distributions | Current quote/NAV through 2026-08-14; performance and risk fields through 2026-07-31; holdings through 2026-08-13 |
| NYSE Arca:SCHA | https://www.schwabassetmanagement.com/products/scha/documents | Official documents hub for the SCHA factsheet, ETF performance summary, monthly fund report and distribution schedule | Factsheet last updated 2026-06-30; ETF performance summary and monthly report last updated 2026-07-31 |
| NYSE Arca:SCHA | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=scha | Official Schwab ETF research capture: current NAV YTD, rolling performance, current quote and best/worst three-month observations | Performance through 2026-07-31; close/price through 2026-08-14 |
| NYSE Arca:SCHA | https://www.sec.gov/Archives/edgar/data/1454889/000110465925123320/tm2526338-13_497k.htm | SEC summary prospectus: objective, index construction, 90% policy, passive indexing strategy and risks | Prospectus dated 2025-12-22; current product page supersedes its older 0.04% expense ratio with 0.03% effective 2026-06-11 |
| NYSE Arca:SCHA annual proxy rows | https://www.etfreplay.com/etf/scha | Secondary dividend-reinvested annual total-return history; used only as a labelled proxy because the issuer annual table did not render in the reviewed capture | 2016-2025 annual rows; secondary proxy, not official issuer NAV rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## SCHA raw observations and calculations

| Year | SCHA total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 19.97%* | 11.96% |
| 2017 | 14.93%* | 21.83% |
| 2018 | -11.77%* | -4.38% |
| 2019 | 26.50%* | 31.49% |
| 2020 | 19.34%* | 18.40% |
| 2021 | 16.45%* | 28.71% |
| 2022 | -19.81%* | -18.11% |
| 2023 | 18.46%* | 26.29% |
| 2024 | 11.16%* | 25.02% |
| 2025 | 11.60%* | 17.88% |
| 2026 YTD | 18.27% (official NAV) | not available from cached current-year benchmark |

- Metric basis: official SCHA NAV Total Return for current-period fields; annual rows are secondary dividend-reinvested proxy observations and are not relabelled as official issuer NAV rows.
- Issuer benchmark: Dow Jones U.S. Small-Cap Total Stock Market Index; retained as metadata and not substituted for the common S&P 500 reference.
- SCHA 2016-2025 proxy compound: `152.02%` cumulative; rounded-input CAGR `9.68%`.
- SCHA 2021-2025 proxy compound: `37.23%` cumulative; rounded-input CAGR `6.53%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR field: `10.48%` annualized as of 2026-07-31; raw rolling endpoints are not disclosed.
- Official risk fields as of 2026-07-31: beta `1.00` and standard deviation `19.78%`; holdings `1,711` as of 2026-08-13; turnover `13.99%` as of 2026-07-31.
- Official 2026 distributions visible: `US$0.1004` ex/pay 2026-06-24/2026-06-29 and `US$0.0384` ex/pay 2026-03-25/2026-03-30.

## SCHA gaps and scheduled-inline local review

- The issuer page supplied current NAV/rolling fields but the reviewed machine-readable issuer capture did not expose the complete 2016-2025 annual NAV table; secondary rows are therefore marked `*` and excluded from claims of official annual coverage.
- Official current fields are split across 2026-07-31 performance/risk, 2026-08-13 holdings, and 2026-08-14 quote snapshots; these dates are kept separate.
- Official daily NAV history sufficient for a numeric maximum drawdown and recovery calculation was not verified; no daily drawdown proxy is saved.
- Local pre-save result: `PASS`. Confirmed canonical identity `NYSE Arca:SCHA`, passive/index-tracking classification, index objective, expense ratio, current NAV/YTD, rolling field, proxy markers, S&P cache basis/window, risk/distribution observations, USA region ownership, graph breadcrumb, and disclosed gaps.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## SPSM official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:SPSM | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-600-small-cap-etf-spsm | Official State Street product page: passive objective, index, exchange/listing, inception, NAV/AUM, expense ratio, holdings, characteristics, current performance and benchmark continuity | Product page accessed 2026-08-17; fund facts through 2026-08-15; NAV/AUM/characteristics as of 2026-08-13; performance as of 2026-07-31 |
| NYSE Arca:SPSM | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-spsm.pdf | Official State Street factsheet: fund facts, passive index objective, standardized NAV/market-value/index performance and risk context | Factsheet as of 2026-06-30; accessed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## SPSM raw observations and calculations

| Period | SPSM NAV TR | Linked benchmark series |
|---|---:|---:|
| 1 month to 2026-07-31 | -1.90% | -1.90% |
| QTD to 2026-07-31 | -1.90% | -1.90% |
| 2026 YTD | 21.54% | 21.55% |
| 1 year to 2026-07-31 | 33.62% | 33.64% |
| 3 years annualized to 2026-07-31 | 13.24% | 13.26% |
| 5 years annualized to 2026-07-31 | 7.45% | 7.48% |
| 10 years annualized to 2026-07-31 | 10.75% | 10.79% |
| Since inception annualized to 2026-07-31 | 10.08% | 10.09% |

- Metric basis: official State Street fund NAV total return, net of fees, with dividends and capital gains reinvested. The linked benchmark series is gross of fund fees.
- Current quote/fund facts: NAV `US$58.20`, bid/ask midpoint `US$58.22`, premium/discount `+0.02%`, AUM `US$17,415.46M`, 606 holdings, gross expense ratio `0.03%`, 30-day SEC yield `1.44%`, and quarterly distributions as of 2026-08-13 or the applicable official fund-facts snapshot.
- Tracking differences, calculated as fund NAV minus linked benchmark from the same issuer table, are `-0.01 pp` YTD, `-0.02 pp` for 1 year, `-0.02 pp` for 3 years, `-0.03 pp` for 5 years, and `-0.04 pp` for 10 years.
- The issuer's benchmark history is linked across Russell 2000 from inception through 2017-11-16, SSGA Small Cap Index from 2017-11-16 through 2020-01-24, and S&P SmallCap 600 Index from 2020-01-24 onward.
- Official SPSM calendar-year NAV rows for 2016-2025 and raw rolling 10-year endpoints were not disclosed in the reviewed issuer capture; no annual-row CAGR or up/down-year count is calculated.
- S&P 500 annual rows reuse the cached USD total-return convention and are not mixed with the current SPSM YTD date window.

## SPSM gaps and scheduled-inline local review

- The latest official current-period performance located is through 2026-07-31; the latest official quote, AUM, holdings and characteristics are separate 2026-08-13/15 snapshots and remain separately labelled.
- Official calendar-year NAV rows for 2016-2025 and raw endpoints for the 10-year field remain `ไม่พบข้อมูลที่ยืนยันได้`; the issuer-labeled `10.75%` annualized field is retained as a source fact, not recomputed.
- Official daily NAV history sufficient for a numeric maximum drawdown and recovery calculation was not verified; no drawdown proxy is saved.
- Complete local pre-save checklist: confirmed canonical identity `NYSE Arca:SPSM`, passive/index-tracking classification, S&P SmallCap 600 objective, inception, fee, return basis, benchmark continuity, current/rolling fields, units/currencies, as-of dates, tracking calculations, cached S&P window/basis, graph breadcrumb, USA primary-region ownership, planned page/index/source-batch/log contents, and disclosed gaps.
- Local pre-save result: `PASS`.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## FYX official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NASDAQ:FYX | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FYX | Official First Trust product page: fund identity, Nasdaq listing, objective, index methodology, expense ratio, current NAV/market price, rolling NAV performance, risk fields, and distribution context | Product/current fields through 2026-08-03; performance fields through 2026-06-30 |
| NASDAQ:FYX | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b4ab133b-7d16-4b63-81f3-83640709b936 | Official First Trust factsheet: inception, Nasdaq listing, expense ratio, index identity, 2016-2025 calendar NAV total-return rows, 2026 YTD, and 3-year risk statistics | Factsheet as of 2026-06-30 |
| NASDAQ:FYX | https://www.ftportfolios.com/Funds/ETF/Prospectus/FYT | Official prospectus: indexing approach, at-least-90% index exposure, 2016-04-08 index change, annual return chart, and best/worst quarter observations | Prospectus dated 2025-12-01; annual chart through 2024 |
| NASDAQ:FYX | https://www.ftportfolios.com/Retail/Etf/EtfPriceHistory.aspx?Ticker=FYX | Official historical pricing: NAV/market price and net assets | Latest visible quote `2026-08-03` |
| NASDAQ:FYX | https://www.ftportfolios.com/Retail/Etf/EtfDividHistory.aspx?Ticker=FYX | Official cash distribution history | 2026 records visible through 2026-06-30 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/; https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached project reference for complete calendar years | 2016-2025 USD total return, dividends reinvested, as of 2025-12-31 |

## FYX raw observations and calculations

| Year | FYX NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 22.72% | 11.96% |
| 2017 | 14.45% | 21.83% |
| 2018 | -10.26% | -4.38% |
| 2019 | 21.04% | 31.49% |
| 2020 | 19.23% | 18.40% |
| 2021 | 27.48% | 28.71% |
| 2022 | -18.39% | -18.11% |
| 2023 | 18.12% | 26.29% |
| 2024 | 12.20% | 25.02% |
| 2025 | 12.90% | 17.88% |
| 2026 YTD | 28.10% (official NAV TR) | not available from cached current-year benchmark |

- Metric basis: official FYX NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: Nasdaq AlphaDEX Small Cap Core™ Index (`NQDXUSSCT`); retained as metadata and not substituted for the common S&P 500 reference.
- FYX 2016-2025 compound: `183.16%` cumulative; rounded-input CAGR `10.97%`.
- FYX 2021-2025 compound: `55.67%` cumulative; rounded-input CAGR `9.25%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR field: `13.26%` annualized as of 2026-06-30; raw rolling endpoints are not disclosed and the field is not relabelled as the 2016-2025 calendar CAGR.
- Official 3-year risk fields as of 2026-06-30: standard deviation `19.91%`, alpha `4.99`, beta `1.02`, Sharpe ratio `0.87`, correlation `0.99`.
- Official 2026 distributions visible in the reviewed archive: `US$0.4369` ex/pay 2026-06-25/2026-06-30 and `US$0.2029` ex/pay 2026-03-26/2026-03-31.

## FYX gaps and conflicts

- The latest official performance fields located are as of 2026-06-30, while the latest visible official NAV/market-price quote is as of 2026-08-03; these are separate snapshots and are not presented as one same-date observation.
- The underlying index changed from the Defined Small Cap Core Index to the Nasdaq AlphaDEX Small Cap Core™ Index on 2026-04-08. The 2016 full-year fund return remains an official NAV observation, but pre-change performance is not necessarily indicative of the current index methodology.
- Official daily NAV history sufficient for a numeric maximum drawdown and recovery calculation was not verified; no secondary drawdown proxy is saved.
- The reviewed official distribution archive exposed only the two 2026 records above; older distributions are not inferred because they are not needed to calculate NAV Total Return.

## FYX scheduled-inline local review

- Status: `PASS`
- Confirmed canonical identity `NASDAQ:FYX`, Nasdaq listing, passive/indexing classification, inception, expense ratio, issuer benchmark, NAV Total Return definition, official 2016-2025 annual rows, official 2026 YTD, issuer rolling 10-year field, risk statistics, distributions, S&P cache window/basis, best/worst ranking, calculations, source links, USA primary-region ownership, graph breadcrumb, and no unsupported drawdown/recovery inference.
- All material durable values map to official First Trust sources or the cached S&P 500 convention; annual rows and YTD are clearly separated from the current quote snapshot.
- No proxy marker is used because the factsheet provides the complete official 2016-2025 annual row set.
- Local pre-save result: `PASS`.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## BSVO unsupported ETF record

- Input ticker: `BSVO`; canonical identity: `Nasdaq:BSVO`; fund: EA Bridgeway Omni Small-Cap Value ETF; inception `2010-12-31`.
- Type gate: `unsupported ETF type`. Bridgeway’s official fund page labels BSVO `Fund Type: Active`, and the SEC summary prospectus describes a broad small-cap value portfolio managed by an adviser/sub-adviser rather than a passive index-tracking mandate. ETF v1 excludes active ETFs even when the holdings are equity securities.
- No NAV performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was created after the type gate. Current return observations were not used as performance evidence.

### BSVO Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `Nasdaq:BSVO` | https://bridgewayetfs.com/bsvo/ | Official issuer fund page: active classification, ticker, Nasdaq exchange, inception, expense, NAV and current month-end performance context | Page reviewed 2026-08-17; current facts shown as of 2026-07-29 / month-end performance through 2026-06-30 |
| `Nasdaq:BSVO` | https://www.sec.gov/Archives/edgar/data/1592900/000159290024002170/eabridgewayomnismall-capva.htm | SEC summary prospectus: fund objective, active portfolio management and formal listing | Prospectus dated 2024-10-31 |
| `Nasdaq:BSVO` | https://www.sec.gov/Archives/edgar/data/1592900/000159290025001783/bridgewaysaibbluandbsvo.htm | SEC SAI: exchange and adviser/sub-adviser context | SAI dated 2024-10-31, supplemented 2025-07-10 |

### BSVO scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, issuer classification, active/passive type gate, index status, scope exclusion, source URLs/as-of dates, no-performance-artifact decision, card result metadata, and final-round sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance artifact was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## FNDC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:FNDC | https://www.schwabassetmanagement.com/products/fndc | Official product page: fund identity, passive management style, index, expense, NAV, rolling/YTD performance, risk fields, and portfolio snapshot | NAV/quote fields through 2026-08-14; performance and risk fields through 2026-07-31 |
| NYSE Arca:FNDC | https://www.schwabassetmanagement.com/products/fndc/documents?page=0 | Official document hub and performance/factsheet entry points | Hub reviewed 2026-08-17; performance summary entry updated 2026-07-31; factsheet entry updated 2026-06-30 |
| NYSE Arca:FNDC | https://www.sec.gov/Archives/edgar/data/1454889/000088454626000301/c497k.htm | SEC summary prospectus: annual total returns, index methodology, passive/index-fund treatment, benchmark change, and return definitions | Prospectus dated 2026-06-26; annual rows through 2025 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common benchmark definition | USD total return, dividends reinvested; page reviewed 2026-08-17 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current cross-check | `14.04%` YTD displayed on page dated 2026-08-10; not synchronized with FNDC YTD 2026-07-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-2021/; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached project convention for complete calendar years | 2016-2025 USD gross total return, dividends reinvested, as of 2025-12-31 |

## FNDC raw observations and calculations

| Year | FNDC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 8.87% | 11.96% |
| 2017 | 29.04% | 21.83% |
| 2018 | -18.77% | -4.38% |
| 2019 | 20.02% | 31.49% |
| 2020 | 7.11% | 18.40% |
| 2021 | 9.83% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 15.21% | 26.29% |
| 2024 | 1.57% (source precision 1.5698548%) | 25.02% |
| 2025 | 35.79% (source precision 35.7881285%) | 17.88% |
| 2026 YTD | 10.96% (official NAV, 2026-07-31) | 14.04% (official current page dated 2026-08-10; not same date) |

- FNDC 2016-2025 compound: `118.08%` cumulative; rounded-input CAGR `8.11%`.
- FNDC 2021-2025 compound: `48.65%` cumulative; rounded-input CAGR `8.25%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- The official rolling 10-year FNDC NAV TR field is `8.48%` as of 2026-07-31; raw rolling endpoints were not disclosed in the reviewed issuer capture. The `8.11%` figure is the separate 2016-2025 calendar-window calculation using the SEC annual rows.
- Annual-row sample standard deviation is `17.24%`; issuer-reported 3-year standard deviation is `15.14%` as of 2026-07-31. These are different windows and neither is daily maximum drawdown.
- Year-end cumulative-path drawdown approximation is `-18.77%` at the 2018 year-end observation, with recovery above the prior year-end high by 2020; no daily maximum drawdown is claimed.
- The 2024 and 2025 source rows retain additional precision in this batch, while page/index displays are rounded to two decimals.

## FNDC pre-save checklist

- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Entity and exchange reconciled as `NYSE Arca:FNDC`; passive/index-fund classification confirmed from Schwab and SEC sources.
- Return basis, USD currency, issuer benchmark, common benchmark, annual coverage, current-field as-of dates, rolling-vs-calendar distinction, and separate distribution-yield field were checked before write.
- Benchmark/index change effective 2024-06-21 is disclosed; the historical fund NAV return series is not spliced with an unverified proxy.
- Every durable number above maps to an official URL or the cached S&P convention; rounded-input calculations are labeled and no synchronized S&P current-YTD spread is asserted.
- Existing international-region navigation was updated with canonical `NYSE Arca:FNDC`; no duplicate performance page was found.
- Local pre-save result: `PASS`.

## FNDC gaps and conflicts

- The issuer changed the comparative index effective 2024-06-21; pre-change and post-change benchmark identities are preserved rather than treated as one unchanged index series.
- FNDC YTD is as of 2026-07-31 while the official S&P current cross-check is displayed for 2026-08-10; no same-date benchmark spread is claimed.
- Annual issuer rows are rounded in the page display; source precision for 2024 and 2025 is retained, and cumulative/CAGR/annual-row volatility calculations remain input-dependent.
- Official daily NAV history sufficient for a daily maximum-drawdown and recovery statistic was not verified; only the labeled year-end observation approximation is retained.

## DES official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:DES | https://www.wisdomtree.com/us/products/equity/des | Official product page: fund identity, passive/index-tracking description, NAV/market price, rolling and YTD performance, expense, and distributions | NAV/price and expense through 2026-08-14; rolling 10Y and YTD performance through 2026-07-31; distributions through 2026-07-28 |
| NYSE Arca:DES | https://www.wisdomtree.com/us/media/des-presentation | Official issuer presentation: calendar-year NAV total returns and methodology | 2016-2025 annual NAV rows; presentation data as of 2026-03-31 |
| NYSE Arca:DES | https://www.wisdomtree.com/us/media/wisdomtree-factsheet-des-1008 | Official quarterly factsheet: exchange, inception, index, expense, and return definition | Factsheet data as of 2026-03-31 |
| NYSE Arca:DES | https://www.sec.gov/Archives/edgar/data/1350487/000121465925011322/des73125497k.htm | SEC summary prospectus: passive indexing, listing, fees, and return treatment | Filing reviewed 2026-08-17 |
| WTSDI | https://www.wisdomtree.com/us/indexes/wtsdi | Official tracked-index methodology and identity | Index methodology page reviewed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common benchmark definition | USD total return convention; page reviewed 2026-08-17 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current cross-check | `14.04%` YTD displayed on page dated 2026-08-10; not synchronized with DES YTD 2026-07-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-2021/; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached project convention for complete calendar years | 2016-2025 USD gross total return, dividends reinvested, as of 2025-12-31 |

## DES raw observations and calculations

| Year | DES NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.06% | 11.96% |
| 2017 | 8.66% | 21.83% |
| 2018 | -12.74% | -4.38% |
| 2019 | 20.30% | 31.49% |
| 2020 | -4.41% | 18.40% |
| 2021 | 26.71% | 28.71% |
| 2022 | -10.94% | -18.11% |
| 2023 | 16.40% | 26.29% |
| 2024 | 9.79% | 25.02% |
| 2025 | 0.26% | 17.88% |
| 2026 YTD | 22.93% (official NAV, 2026-07-31) | 14.04% (official current page dated 2026-08-10; not same date) |

- DES 2016-2025 compound: `106.62%` cumulative; rounded-input CAGR `7.53%`.
- DES 2021-2025 compound: `44.59%` cumulative; rounded-input CAGR `7.65%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- The official rolling 10-year DES NAV TR field is `8.04%` as of 2026-07-31; raw rolling endpoints were not disclosed in the reviewed issuer capture. The `7.53%` figure is the separate 2016-2025 calendar-window calculation from rounded annual rows.
- DES annual-row sample standard deviation is `15.30%`; this is calculated from the ten rounded annual NAV TR observations and is not a daily risk measure.
- Year-end cumulative-path drawdown approximation is `-12.74%` at the 2018 year-end observation, with recovery above the prior year-end high by 2019; no daily maximum drawdown is claimed.
- Latest four official cash distributions reviewed sum to `$0.305`; latest listed distribution is `$0.045` ex/pay 2026-07-28/30, and the product page shows distribution yield `1.30%` as of 2026-08-14. These are separate from total return.

## DES pre-save checklist

- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Entity and exchange reconciled as `NYSE Arca:DES`; passive/index-tracking classification confirmed from issuer and SEC sources.
- Return basis, USD currency, issuer benchmark, common benchmark, annual coverage, current-field as-of dates, and separate NAV/price/distribution fields were checked before write.
- Every durable number above maps to an official URL or the cached S&P convention; rounded-input calculations are labeled and no synchronized S&P current-YTD spread is asserted.
- Existing DES performance path and USA-region navigation were updated in place; no duplicate canonical page was created.
- Local pre-save result: `PASS`.

## DES gaps and conflicts

- DES official rolling 10-year performance is available, but raw endpoint values were not disclosed in the reviewed issuer capture; it is not substituted with the calendar-window CAGR.
- DES YTD is as of 2026-07-31 while the official S&P current cross-check is displayed for 2026-08-10; no same-date benchmark spread is claimed.
- Annual issuer rows are rounded; cumulative, CAGR, and annual-row volatility are rounded-input calculations.
- Official daily NAV history sufficient for a daily maximum-drawdown and recovery statistic was not verified; only the labeled year-end observation approximation is retained.

## SSEUF / R2US official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:R2US / SSEUF | https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-russell-2000-us-small-cap-ucits-etf-acc-zprr-gy | Official State Street product page: fund identity, listing table, benchmark, official Fund Net/NAV performance, current NAV/YTD, standard deviation and tracking error | Annual rows 2016-2025 and rolling/current fields as of 2026-07-31; NAV quote as of 2026-07-17 |
| LSE:R2US / SSEUF | https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprr-gy.pdf | Official State Street factsheet: ISIN, USD LSE ticker R2US, inception, TER, accumulating share class, optimized replication, benchmark and performance | Factsheet dated 30 Jun 2026; performance table through 31 Jul 2026 |
| LSE:R2US / SSEUF | https://www.ssga.com/library-content/kids?country=ie&documentType=kid&isin=IE00BJ38QD84&language=en_gb&ticker=zprr-gy | Official KID: index-tracking/passive objective, optimization policy, accumulating income treatment and risk disclosures | Accurate as of 2026-02-19 |
| SSEUF alias | https://www.google.com/finance/beta/quote/SSEUF%3AOTCMKTS | Secondary OTC alias and USD quote cross-check; canonical exchange key remains LSE:R2US | Search snapshot accessed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## SSEUF / R2US raw observations and calculations

| Year | R2US Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 20.97% | 11.96% |
| 2017 | 13.98% | 21.83% |
| 2018 | -11.34% | -4.38% |
| 2019 | 24.98% | 31.49% |
| 2020 | 19.36% | 18.40% |
| 2021 | 14.70% | 28.71% |
| 2022 | -20.78% | -18.11% |
| 2023 | 16.27% | 26.29% |
| 2024 | 11.19% | 25.02% |
| 2025 | 12.32% | 17.88% |
| 2026 YTD | 18.69% | not available from cached current-year benchmark |

- Input ticker `SSEUF` is an OTC alias; official State Street listing data maps the same ISIN/share class to USD `LSE:R2US`. The primary listing is Deutsche Börse `ZPRR`, but the durable key uses the USD London line matching the input currency.
- Metric basis: official R2US Fund Net performance is NAV-based and net of fees; the accumulating share class retains income in NAV.
- Issuer benchmark: Russell 2000 Index Net Total Return (`RU20N30U`); retained as metadata and not substituted for the common S&P 500 reference.
- Official 10-year rolling NAV TR: `163.53%` cumulative / `10.18%` annualized as of 2026-07-31; since-inception: `177.36%` cumulative / `8.81%` annualized.
- 2016-2025 R2US compound: `140.61%` cumulative; rounded-input CAGR `9.18%`.
- 2021-2025 R2US compound: `31.94%` cumulative; rounded-input CAGR `5.70%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: 3-year standard deviation `19.67%` and tracking error `0.08%` as of 2026-07-31.

## SSEUF / R2US gaps and conflicts

- The input is an OTC alias (`SSEUF`) rather than the official USD London ticker; the canonical exchange-qualified key is `LSE:R2US` and the official primary listing is Deutsche Börse `ZPRR`. The alias, ISIN, share-class currency and index identity were reconciled before save.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## SCZ official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:SCZ` | https://www.ishares.com/us/products/239627/ | Official iShares product page: identity, NASDAQ listing, inception, benchmark, current NAV/YTD, expense ratio, holdings and risk fields | Current NAV/price 2026-08-14; NAV TR YTD 2026-08-13; holdings 2026-08-13; risk fields through 2026-07-31 |
| `NASDAQ:SCZ` | https://www.ishares.com/ch/professionals/en/products/239627/ishares-msci-eafe-smallcap-etf?switchLocale=Y | Official iShares performance table with complete 2016-2025 calendar rows | Table reviewed 2026-08-17; rows displayed at one decimal |
| `NASDAQ:SCZ` | https://www.ishares.com/us/literature/fact-sheet/scz-ishares-msci-eafe-small-cap-etf-fund-fact-sheet-en-us.pdf | Official factsheet: NAV return basis, 2021-2025 rows, benchmark, inception and expense ratio | Factsheet as of 2026-06-30 |
| `NASDAQ:SCZ` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-eafe-small-cap-etf-7-31.pdf | Official summary prospectus: objective, index-tracking scope and fee/risk context | Dated 2025-11-28 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | Cached USD total-return convention; annual rows as of 2025-12-31 |

## SCZ raw observations and calculations

| Year | SCZ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.40% | 11.96% |
| 2017 | 32.50% | 21.83% |
| 2018 | -17.80% | -4.38% |
| 2019 | 24.70% | 31.49% |
| 2020 | 12.10% | 18.40% |
| 2021 | 10.02% | 28.71% |
| 2022 | -21.22% | -18.11% |
| 2023 | 12.90% | 26.29% |
| 2024 | 1.35% | 25.02% |
| 2025 | 32.10% | 17.88% |

- Metric basis: official iShares NAV total return with dividends/capital gains reinvested and fund expenses deducted; USD.
- Issuer benchmark: `MSCI EAFE Small Cap Index (Net)`; retained as metadata and not substituted for the common S&P 500 reference.
- SCZ 2016-2025 compound from displayed annual rows: `104.25%` cumulative; rounded-input CAGR `7.40%`.
- SCZ 2021-2025 compound from displayed annual rows: `31.01%` cumulative; rounded-input CAGR `5.55%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Current NAV TR YTD: `13.83%` as of 2026-08-13; current NAV `US$87.17` and closing price `US$87.14` as of 2026-08-14.
- Issuer rolling 10-year NAV TR average annual: `8.60%` as of 2026-06-30; raw endpoints are not disclosed and this is not substituted for the calendar-window CAGR.
- Official risk fields: 3-year standard deviation `14.97%` and beta `0.78` as of 2026-07-31; holdings `2,056` as of 2026-08-13.

## SCZ gaps and local review

- The annual rows are official but rounded at different displayed precision: 2016-2020 one decimal in the product performance table and 2021-2025 two decimals in the June 2026 factsheet. Calculations preserve the displayed inputs and are labelled rounded-input.
- The current S&P 500 TR field reviewed is not synchronized to the SCZ current YTD observation, so no current-year cross-asset comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no secondary proxy is used.
- Planned durable paths: create `wiki/analysis/performance/ETF_NASDAQ_SCZ Performance.md`; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `International`; add breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; add `geography/International` and `geography/international-ex-US`; preserve numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## AVUV unsupported ETF type

- Input ticker: `AVUV`; canonical identity: `NYSE Arca:AVUV`; fund: Avantis U.S. Small Cap Value ETF.
- Type gate: `unsupported ETF type`. The official Avantis product page says the fund is actively managed and does not seek to replicate the performance of a specified index. The current SEC summary prospectus states the same and describes portfolio-manager security selection using profitability/value characteristics plus possible derivatives. This fails ETF v1's passive, index-tracking equity scope.

### AVUV Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:AVUV` | https://www.avantisinvestors.com/avantis-investments/avantis-us-small-cap-value-etf/?aud=indiv | Official issuer product page: identity, exchange, active-management classification, and index-replication exclusion | Page reviewed 2026-08-17; current issuer page |
| `NYSE Arca:AVUV` | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000416/acetftavuv497k.htm | Official SEC summary prospectus: identity, exchange, expense ratio, active security-selection strategy, derivatives context, and no-specified-index statement | Summary Prospectus dated 2026-01-01; reviewed 2026-08-17 |

### AVUV scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, official issuer and SEC classification, active/passive type gate, index status, ETF v1 scope exclusion, source URLs/as-of dates, no-performance-artifact decision, Trello result metadata, and next-card sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## DFAS unsupported ETF type

- Input ticker: `DFAS`; canonical identity: `NYSE Arca:DFAS`; fund: Dimensional U.S. Small Cap ETF.
- Type gate: `unsupported ETF type`. The current SEC summary prospectus identifies DFAS as an actively managed ETF that does not seek to replicate the performance of a specific index, and describes flexible portfolio-management decisions plus possible futures/options use. Dimensional's official materials also describe DFAS within its active ETF lineup. This fails ETF v1's passive, index-tracking equity scope.

### DFAS Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:DFAS` | https://www.sec.gov/Archives/edgar/data/1816125/000181612526000081/c497k.htm | Official SEC summary prospectus: identity, exchange, objective, active-management classification, index-replication exclusion, flexible process and derivative context | Summary Prospectus dated 2026-02-28; reviewed 2026-08-17 |
| `NYSE Arca:DFAS` | https://www.dimensional.com/us-en/our-approach/dimensional-equity-solutions | Official issuer equity-solutions page: DFAS identity and placement in Dimensional's component/small-cap active ETF lineup | Issuer page reviewed 2026-08-17 |
| `NYSE Arca:DFAS` | https://www.dimensional.com/us-en/newsroom/dimensional-lists-four-new-etfs-following-the-industrys-largest-mutual-fund-to-etf-conversion | Official issuer listing announcement: NYSE Arca listing and explicit active transparent ETF description | Published 2021-06-14; reviewed 2026-08-17 |

### DFAS scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, official issuer and SEC classification, active/passive type gate, index status, ETF v1 scope exclusion, source URLs/as-of dates, no-performance-artifact decision, Trello result metadata, and next-card sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## AVDV unsupported ETF type

- Input ticker: `AVDV`; canonical identity: `NYSE Arca:AVDV`; fund: Avantis International Small Cap Value ETF.
- Type gate: `unsupported ETF type`. The official Avantis product page says the fund is actively managed and does not seek to replicate the performance of a specified index. The current SEC summary prospectus states the same and describes portfolio-manager buy/sell/hold decisions using profitability and value characteristics, with possible derivative use. This fails ETF v1's passive, index-tracking equity scope.

### AVDV Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:AVDV` | https://www.avantisinvestors.com/avantis-investments/avantis-international-small-cap-value-etf/ | Official issuer product page: identity, exchange, active-management classification, index-replication exclusion and portfolio-manager decision context | Page reviewed 2026-08-17; current issuer page |
| `NYSE Arca:AVDV` | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000402/acetftavdv497k.htm | Official SEC summary prospectus: identity, exchange, objective, fee, active security-selection strategy, derivatives context, and no-specified-index statement | Summary Prospectus dated 2026-01-01; reviewed 2026-08-17 |

### AVDV scheduled-local review

- Complete pre-save checklist reviewed locally: canonical identity/exchange, official issuer and SEC classification, active/passive type gate, index status, ETF v1 scope exclusion, source URLs/as-of dates, no-performance-artifact decision, Trello result metadata, and final-card sequencing.
- Result: local `PASS` for the unsupported-type classification; no performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was written.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## IWN official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:IWN | https://www.ishares.com/us/products/239712/ishares-russell-2000-value-etf | Official iShares product page: identity, exchange, inception, benchmark, fee, current NAV/price, NAV YTD, standard deviation, beta, holdings, and fund facts | Current NAV/price and key facts through 2026-08-14; NAV TR YTD through 2026-08-13; risk fields through 2026-07-31 |
| NYSE Arca:IWN | https://www.ishares.com/us/literature/fact-sheet/iwn-ishares-russell-2000-value-etf-fund-fact-sheet-en-us.pdf | Official factsheet: NAV total-return definition, 2021-2025 calendar rows, annualized returns, fee and risk cross-check | Factsheet as of 2026-06-30 |
| NYSE Arca:IWN | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-russell-2000-value-etf-3-31.pdf | Official summary prospectus: passive objective, benchmark, complete 2016-2025 calendar-year table, YTD, and best/worst quarter | Prospectus performance table through 2025-12-31; YTD field through 2026-06-30 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached annual reference rows | 2022-2025; reused without new search |

## IWN raw observations and calculations

| Year | IWN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.64% | 11.96% |
| 2017 | 7.73% | 21.83% |
| 2018 | -12.94% | -4.38% |
| 2019 | 22.17% | 31.49% |
| 2020 | 4.50% | 18.40% |
| 2021 | 27.96% | 28.71% |
| 2022 | -14.67% | -18.11% |
| 2023 | 14.42% | 26.29% |
| 2024 | 7.74% | 25.02% |
| 2025 | 12.41% | 17.88% |
| 2026 YTD | 25.91% | not available from cached current-year benchmark |

- Metric basis: official iShares IWN NAV Total Return in USD; dividends and capital-gains distributions are reinvested and fund expenses are reflected in NAV. The complete 2016-2025 annual rows are published at 0.1% precision.
- Issuer benchmark: `Russell 2000 Value Index`; it is retained as metadata and is not substituted for the common S&P 500 reference.
- 2016-2025 IWN compound: `138.50%` cumulative; rounded-input CAGR `9.08%`.
- 2021-2025 IWN compound: `51.31%` cumulative; rounded-input CAGR `8.64%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Annual-row positive/negative years: `8 / 2`; best 2016 `+31.64%`, least positive 2024 `+7.74%`, worst 2022 `-14.67%`, least bad down year 2018 `-12.94%`.
- Official issuer rolling 10-year NAV TR annualized: `10.69%` as of 2026-06-30; raw endpoints were not disclosed and this field is kept separate from the annual-row CAGR.
- Official current NAV TR YTD: `25.91%` as of 2026-08-13; market price `US$227.43` and NAV `US$227.41` as of 2026-08-14; calculated premium `0.01%`.
- Official three-year standard deviation `19.10%` and equity beta `1.08` as of 2026-07-31; holdings `1,389` as of 2026-08-11; best quarter `+33.29%` and worst quarter `-35.70%` from the official prospectus.
- Formula: cumulative `= product(1 + annual TR) - 1`; rounded-input CAGR `= product(1 + annual TR)^(1 / number of years) - 1`.

## IWN gaps and scheduled-inline local review

- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- The issuer rolling 10-year field is a separate annualized observation as of 2026-06-30; raw endpoints and exact elapsed years were not disclosed.
- The complete annual table is official but rounded to 0.1%, so cumulative and CAGR outputs are explicitly rounded-input calculations.
- Complete pre-save checklist reviewed locally: canonical ticker/exchange, passive/index-tracking type, issuer benchmark, NAV return definition, distributions, annual rows, cached S&P 500 window, current YTD and price/NAV as-of dates, calculations, source URLs, unresolved gaps, exact planned page/source-batch/index/region/log contents, graph links, canonical geography tag, and single primary region.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## CPLCF / CUSS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:CUSS / input CPLCF | https://www.ishares.com/uk/individual/en/products/253480/cuss?siteEntryPassthrough=true&switchLocale=y | Official iShares product page: identity, USD listing, ISIN, current index, name/benchmark change, NAV, YTD and calendar NAV TR rows | Product/current fields through 2026-07-29; calendar rows 2016-2025 |
| LSE:CUSS / input CPLCF | https://www.ishares.com/uk/professional/en/products/253480/csuss | Official professional page: USD share-class facts, expense, holdings and risk fields | Holdings/current fields through 2026-07-30; risk fields through 2026-06-30 |
| LSE:CUSS / input CPLCF | https://www.ishares.com/ch/privatkunden/de/literature/fact-sheet/csuss-ishares-msci-usa-small-cap-ctb-enhanced-esg-ucits-etf-fund-fact-sheet-de-ch.pdf | Official factsheet: calendar NAV performance and return definition | Calendar rows 2016-2025; factsheet capture reviewed 2026-08-17 |
| LSE:CUSS / input CPLCF | https://www.londonstockexchange.com/stock/CUSS/ishares/company-page | Official exchange listing cross-check | USD CUSS line reviewed 2026-08-17 |
| S&P 500 TR current | https://www.slickcharts.com/sp500/returns/ytd | Secondary current benchmark cross-check | `10.14%` total return YTD through 2026-07-31; later than CUSS current YTD |

## CPLCF / CUSS raw observations and calculations

| Year | CUSS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 19.13% | 11.96% |
| 2017 | 16.49% | 21.83% |
| 2018 | -10.49% | -4.38% |
| 2019 | 26.56% | 31.49% |
| 2020 | 18.15% | 18.40% |
| 2021 | 18.86% | 28.71% |
| 2022 | -16.94% | -18.11% |
| 2023 | 15.63% | 26.29% |
| 2024 | 10.71% | 25.02% |
| 2025 | 9.60% | 17.88% |
| 2026 YTD | 14.97% | 10.14%† |

- Metric basis: official iShares NAV Total Return, with gross income reinvested where applicable and performance after ongoing charges; USD accumulating share class values are used for the canonical USD line.
- `†` secondary S&P 500 current cross-check with a different as-of date; complete-year benchmark rows use the cached project convention.
- 2016-2025 CUSS compound: `157.28%` cumulative; rounded-input CAGR `9.91%`.
- 2021-2025 CUSS compound: `38.51%` cumulative; rounded-input CAGR `6.73%`.
- Annual-row positive/negative years: `8 / 2`; best 2019 `+26.56%`, worst 2022 `-16.94%`.
- Official current NAV TR YTD: `14.97%` as of 2026-07-29; NAV quote `US$675.97` as of 2026-07-29.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## CPLCF / CUSS gaps, benchmark change, and scheduled-local gate

- CPLCF is an OTC input alias; official iShares listings identify the USD London line as `CUSS` for ISIN `IE00B3VWM098`. The fund changed name/objective and benchmark on 2022-06-01; the pre-change benchmark was MSCI USA Small Cap Index and the current benchmark is MSCI USA Small Cap ESG Enhanced Focus CTB Index.
- The latest official iShares current NAV TR field located is `14.97%` as of 2026-07-29. The latest displayed NAV quote in the same capture is `US$675.97`; these are separate as-of fields.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Complete pre-save checklist: identity/exchange/index, alias and ISIN, benchmark-history change, return basis, candidate claims, periods, units/currencies, metric definitions, as-of dates, calculations, source URLs, unresolved gaps, exact planned page/batch/index/log contents, graph links, and ownership were reviewed locally before write.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## RWJ official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:RWJ | https://www.sec.gov/Archives/edgar/data/1378872/000119312525325669/d54028d497k.htm | Official SEC summary prospectus: fund identity, exchange, passive objective, index, expense ratio, risks, inception, annualized performance and official benchmark context | Prospectus filed 2025-12-18; performance period ended 2024-12-31 |
| NYSE Arca:RWJ | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/rwj-invesco-s-p-smallcap-600-revenue-etf-fact-sheet.pdf | Official Invesco factsheet entry point and product identity | Link reviewed 2026-08-17; current PDF capture did not expose a synchronized annual table |
| NYSE Arca:RWJ | https://www.etfrc.com/RWJ | Secondary standardized performance and expense snapshot | Total returns through 2026-07-31; expense/AUM snapshot as displayed on page |
| NYSE Arca:RWJ | https://totalrealreturns.com/n/AVUV%2CRWJ%2CXSVM | Secondary dividend-reinvested annual rows, YTD, rolling returns and drawdown proxy | Daily/annual observations through 2026-08-14 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.slickcharts.com/sp500/returns/ytd | Secondary current benchmark cross-check | `10.14%` total return YTD through 2026-07-31; not synchronized with RWJ 2026-08-14 |

## RWJ raw observations and calculations

| Year | RWJ total-return proxy | S&P 500 TR |
|---|---:|---:|
| 2016 | 30.72%* | 11.96% |
| 2017 | 5.09%* | 21.83% |
| 2018 | -16.95%* | -4.38% |
| 2019 | 20.29%* | 31.49% |
| 2020 | 20.83%* | 18.40% |
| 2021 | 52.83%* | 28.71% |
| 2022 | -10.97%* | -18.11% |
| 2023 | 16.22%* | 26.29% |
| 2024 | 11.81%* | 25.02% |
| 2025 | 7.75%* | 17.88% |
| 2026 YTD | 28.61%* | 10.14%† |

- Metric basis: RWJ rows are a secondary dividend-reinvested total-return proxy; official SEC average annual returns are net of expenses but do not provide the same 2016-2025 calendar series in the reviewed capture. S&P rows are USD total return with dividends reinvested.
- `*` secondary TotalRealReturns observations; `†` secondary Slickcharts current cross-check with a different as-of date.
- 2016-2025 RWJ compound: `215.92%` cumulative; rounded-input CAGR `12.19%`.
- 2021-2025 RWJ compound: `90.51%` cumulative; rounded-input CAGR `13.76%`.
- Annual-row sample standard deviation from rounded observations: `19.95%`; this is not daily NAV volatility.
- Official SEC average annual total return: `10.33%` for the 10-year period ended 2024-12-31; kept separate from the calendar-row proxy.
- Secondary drawdown proxy: maximum drawdown `-45.04%` on 2020-03-18 from 2019-12-26 peak; recovery date not disclosed. Current drawdown was `-0.83%` on 2026-08-14 from 2026-08-04 peak.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.

## RWJ gaps, conflicts, and scheduled-local gate

- Official annual NAV rows and a synchronized official current NAV YTD field were not verified in the reviewed capture. The page labels all annual/current proxy values explicitly and does not mix them with the official SEC rolling figure.
- ETFRC standardized return was `25.7%` YTD as of 2026-07-31, versus TotalRealReturns `28.61%` through 2026-08-14; the later source was used for the current proxy, with the conflict/as-of difference preserved.
- Official daily NAV history was not verified; the `-45.04%` drawdown is a secondary total-return proxy and recovery timing is not disclosed.
- Complete pre-save checklist: identity/exchange/index, return basis, benchmark, candidate claims, periods, units/currencies, metric definitions, as-of dates, calculations, source URLs, unresolved gaps, exact planned page/batch/index/log contents, graph links, and ownership were reviewed locally before write.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## XSMO official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:XSMO | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/xsmo-invesco-s-p-smallcap-momentum-etf-fact-sheet.pdf | Official Invesco fact sheet: fund identity, exchange, inception, expense ratio, index, annual NAV rows, issuer average annual returns, and benchmark continuity note | Annual rows 2016-2025 and standard performance as of 2025-12-31 |
| NYSE Arca:XSMO | https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-momentum-etf.html | Official Invesco product page and product identity cross-check | Current product page accessed 2026-08-17; current numeric YTD field not extractable |
| NYSE Arca:XSMO | https://www.sec.gov/Archives/edgar/data/1209466/000119312525190429/d56632d497k.htm | SEC summary prospectus: passive objective, ticker/exchange, fee breakdown, index exposure, inception, and risk quarters | Filed 2025; risk/performance table through 2024-12-31 |
| NYSE Arca:XSMO | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=xsmo | Secondary NAV performance snapshot used only for current YTD context | NAV YTD +30.5% as of 2026-06-30 |
| NYSE Arca:XSMO | https://totalrealreturns.com/n/XSMO | Secondary total-return cross-check | Snapshot +18.10% YTD as of 2026-07-29; return basis/as-of conflict, not mixed into NAV ranking |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## XSMO raw observations and calculations

| Year | XSMO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.17% | 11.96% |
| 2017 | 23.42% | 21.83% |
| 2018 | -2.88% | -4.38% |
| 2019 | 28.35% | 31.49% |
| 2020 | 21.84% | 18.40% |
| 2021 | 19.28% | 28.71% |
| 2022 | -15.48% | -18.11% |
| 2023 | 21.43% | 26.29% |
| 2024 | 17.57% | 25.02% |
| 2025 | 9.81% | 17.88% |
| 2026 YTD | 30.50% (secondary NAV) | not available from cached current-year benchmark |

- Metric basis: official XSMO NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: S&P SmallCap 600 Momentum Index; retained as metadata and not substituted for the common S&P 500 reference.
- 2016-2025 XSMO compound: `217.50%` cumulative; rounded-input CAGR `12.25%`.
- 2021-2025 XSMO compound: `58.05%` cumulative; rounded-input CAGR `9.59%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official fact sheet reports 10-year average annual NAV TR `12.25%` and inception average annual NAV TR `8.38%` as of 2025-12-31; the 10-year issuer field is not relabelled as a raw cumulative endpoint.
- SEC prospectus risk observations: best quarter `+23.72%` in 2Q2020; worst quarter `-25.15%` in 1Q2020.

## XSMO gaps and conflicts

- Official current XSMO NAV TR YTD was not located in the issuer materials read on 2026-08-17. The latest usable current snapshot is a secondary NAV return of `30.50%` as of 2026-06-30.
- Another secondary source reports `18.10%` YTD as of 2026-07-29, but its return basis and date convention are not reconciled with the Schwab NAV snapshot; it is retained as a conflict and excluded from the ranking table.
- The tracked-index history includes predecessor methodologies before 2019-06-21; calendar rows remain issuer fund NAV observations, not a synthetic backfilled index series.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## FNDA official and secondary source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:FNDA | https://www.schwabassetmanagement.com/products/fnda | Official Schwab product page: objective, index, passive style, fee, current NAV/YTD, holdings, turnover, beta and standard deviation | Official NAV/YTD and risk fields as of 2026-06-30; quote/NAV profile as of 2026-07-30 |
| NYSE Arca:FNDA | https://www.schwabassetmanagement.com/resource/fnda-fact-sheet | Official Schwab factsheet entry | Last updated 2026-06-30; PDF viewer download was not text-extractable in the web session |
| NYSE Arca:FNDA | https://www.sec.gov/Archives/edgar/data/1454889/000110465925063127/tm2513735-8_497k.htm | SEC summary prospectus: passive objective, fee, index methodology, 2024 index change, risk quarters and official 2024 performance table | Filed 2025-06-27; performance table through 2024-12-31 |
| NYSE Arca:FNDA | https://www.etfreplay.com/etf/fnda | Secondary dividend-adjusted total-return annual rows used for 2016-2025 common-window calculations | Data as of 2026-08-03; complete annual rows through 2025 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## FNDA raw observations and calculations

| Year | FNDA secondary total-return proxy | S&P 500 TR |
|---|---:|---:|
| 2016 | 23.54% | 11.96% |
| 2017 | 12.66% | 21.83% |
| 2018 | -12.10% | -4.38% |
| 2019 | 24.33% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 31.11% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 20.31% | 26.29% |
| 2024 | 8.99% | 25.02% |
| 2025 | 7.44% | 17.88% |
| 2026 YTD | 21.18% (official NAV) | not available from cached current-year benchmark |

- Metric basis for the current field: official Schwab NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Annual-row basis: ETFreplay dividend-adjusted total-return proxy; it is not relabelled as official issuer NAV return.
- Issuer benchmark: current RAFI Fundamental High Liquidity US Small Index; the fund changed from Russell RAFI US Small Company Index effective 2024-06-21.
- Official rolling 10-year NAV TR: annualized `11.53%` as of 2026-06-30; raw endpoints are not disclosed.
- 2016-2025 secondary proxy compound: `159.56%` cumulative; rounded-input CAGR `10.01%`.
- 2021-2025 secondary proxy compound: `57.34%` cumulative; rounded-input CAGR `9.49%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: best quarter `+30.46%` in 4Q2020; worst quarter `-35.49%` in 1Q2020; 3-year standard deviation `18.38%` and beta `1.00` as of 2026-06-30.

## FNDA gaps and conflicts

- Official current NAV/YTD and rolling 10-year fields are available only through 2026-06-30 in the product-page extract; the profile quote/NAV is newer at 2026-07-30 but is not a return metric.
- Schwab's SEC table reports 2024 before-tax return `8.96%`; the secondary annual proxy reports `8.99%`. The values are retained as a source conflict and not silently merged.
- Official annual NAV rows for 2016-2025 were not text-extractable from the issuer bar-chart/factsheet materials, so the common-window annual table remains explicitly secondary.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual proxy observations are rounded values; cumulative and CAGR outputs are rounded-input calculations.

## Scheduled-inline local review

- Status: `PASS`
- Confirmed GSSC, XSMO, SSEUF, and FNDA ticker/exchange, passive classification, inception, expense ratio, issuer benchmark, NAV TR definition, official annual/current fields, secondary annual proxy basis, S&P cache window/basis, best/worst ranking, formulas, source links, graph breadcrumb, region ownership, and unresolved gaps.
- XSMO-specific local checklist: verified the official 2016-2025 annual rows, issuer 10-year average annual field, secondary current NAV snapshot, separate return-basis treatment, predecessor-index continuity note, 8/2 up/down count, and no unsupported drawdown/recovery inference.
- SSEUF-specific local checklist: verified OTC-to-`LSE:R2US` alias mapping, ISIN/share-class currency, passive classification, official 2016-2025 rows, official 10-year/current NAV fields, S&P cache convention, 8/2 up/down count, risk metrics, graph breadcrumb, primary-region ownership, and no unsupported drawdown/recovery inference.
- FNDA-specific local checklist: verified passive/index classification, exchange, inception, fee, current tracked index, official NAV 10Y/YTD fields, secondary annual-row basis, 2024 benchmark splice, 8/2 up/down count, risk metrics, source conflict, graph breadcrumb, primary-region ownership, and no unsupported drawdown/recovery inference.
- ZPRVF-specific local checklist: resolved the OTC input alias to official USD `LSE:USSC` by ISIN `IE00BSPLC413`, verified passive/index-tracking equity classification, inception, TER, accumulation, issuer benchmark, official 2016-2025 Fund Net rows, rolling 10-year NAV TR, current YTD, S&P cache window/basis, current benchmark date mismatch, 8/2 up/down count, risk metrics, graph breadcrumb, USA primary-region ownership, and no unsupported drawdown/recovery inference.
- NUSC-specific local checklist: verified Cboe BZX identity, passive/index classification, inception, 0.31% fee, Nuveen ESG USA Small-Cap Index, official 2017-2025 NAV/index rows, official 2026 YTD NAV/index fields, under-10-year history, SEC best/worst-quarter corroboration, S&P cache window/basis, 7/2 up/down count, HTML/PDF performance-rendering conflict, graph breadcrumb, USA primary-region ownership, and no unsupported drawdown/recovery inference.
- IMWSF-specific local checklist: resolved OTC `IMWSF` to USD `LSE:WSML` by ISIN `IE00BF4RFH31`, verified passive/physical/optimised UCITS structure, inception, TER, accumulating treatment, official 2019-2025 NAV/index rows, current product-page NAV/YTD, factsheet July YTD, S&P cache/current date mismatch, 6/1 up/down count, 3-year standard deviation and beta, graph breadcrumb, International primary-region ownership, and no unsupported drawdown/recovery inference.
- Planned durable files reviewed before save: `wiki/analysis/performance/ETF_NYSE_ARCA_GSSC Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_XSMO Performance.md`, `wiki/analysis/performance/ETF_LSE_R2US Performance.md`, `wiki/analysis/performance/ETF_LSE_USSC Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_FNDA Performance.md`, `wiki/analysis/performance/ETF_CBOE_BZX_NUSC Performance.md`, `wiki/analysis/performance/ETF_LSE_WSML Performance.md`, this source batch, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `wiki/analysis/comparisons/ETF Region Index.md`, and `log.md`.

## ZPRVF / USSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:USSC / input ZPRVF | https://www.ssga.com/ie/en_gb/institutional/etfs/state-street-spdr-msci-usa-small-cap-value-weighted-ucits-etf-zprv-gy | Official State Street product page: fund identity, listings, inception, TER context, official NAV, Fund Net/NAV performance, annual rows, standard deviation and tracking error | Fund performance through 2026-07-31; NAV 2026-08-14; characteristics 2026-08-13 |
| LSE:USSC / input ZPRVF | https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprv-gy.pdf | Official State Street factsheet: ISIN, USD LSE ticker, index, inception, TER, accumulation, optimized replication and performance | Factsheet dated 2026-06-30; performance table through 2026-07-31 |
| Input ZPRVF alias | https://stockanalysis.com/quote/otc/ZPRVF/ | Secondary OTC identity/exchange cross-check; not used for NAV TR ranking | OTC ticker identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current S&P 500 (TR) YTD cross-check | 14.04% as of 2026-08-16; not synchronized with ETF 2026-07-31 YTD and not used in annual table |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached annual reference rows | 2022-2025; reused without a new search |

## ZPRVF / USSC raw observations and calculations

| Year | USSC Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 25.83% | 11.96% |
| 2017 | 9.37% | 21.83% |
| 2018 | -14.31% | -4.38% |
| 2019 | 23.80% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 35.40% | 28.71% |
| 2022 | -10.23% | -18.11% |
| 2023 | 21.18% | 26.29% |
| 2024 | 9.67% | 25.02% |
| 2025 | 13.89% | 17.88% |
| 2026 YTD | 20.29% (official Fund Net/NAV) | 14.04% (official current page, as of 2026-08-16; not same date) |

- Metric basis: official State Street Fund Net performance is NAV-based and net of fees; the accumulating USD share class retains income in NAV.
- Issuer benchmark: `MSCI USA Small Cap Value Weighted Index` (Net Total Return); retained as metadata and not substituted for the common S&P 500 reference.
- Official rolling 10-year NAV TR: `213.35%` cumulative / `12.10%` annualized as of 2026-07-31. Because raw NAV endpoints are not disclosed, the performance page uses a normalized index calculation `100.00 → 313.35` over `10.00` years; this is not presented as a raw provider index level.
- 2016-2025 USSC compound: `191.31%` cumulative; rounded-input CAGR `11.28%`.
- 2021-2025 USSC compound: `83.97%` cumulative; rounded-input CAGR `12.97%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk fields: 3-year standard deviation `18.28%` and annualized tracking error `0.07%` as of 2026-07-31; official NAV `US$96.48` as of 2026-08-14.

## ZPRVF / USSC gaps and conflicts

- The input ticker `ZPRVF` is an OTC alias. State Street's official listings for ISIN `IE00BSPLC413` identify the USD line as `LSE:USSC` and the primary EUR line as `Deutsche Börse:ZPRV`; the durable key uses `LSE:USSC` to match the USD share class while preserving the input alias in metadata.
- The latest official ETF YTD field is `20.29%` as of 2026-07-31. The latest official S&P 500 TR page reviewed shows `14.04%` as of 2026-08-16; the as-of dates differ, so the current benchmark figure is disclosed but not used as a same-date annual-table comparator.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations. Market-price observations from different currency listings are not mixed into the NAV Total Return ranking.

## NUSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:NUSC | https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?uniqueId=8238272c-9326-4c32-93cb-40d80e4fc4a9 | Official Nuveen factsheet: identity, passive/indexing approach, exchange, fee, NAV/index calendar returns, current YTD, holdings and risk context | Factsheet as of 2026-06-30; calendar rows 2017-2025; current NAV/index YTD 2026-06-30 |
| Cboe BZX:NUSC | https://www.nuveen.com/en-us/exchange-traded-funds/nusc-nuveen-esg-small-cap-etf | Official product page: identity, methodology, primary exchange, fee, inception, quote/NAV snapshot and current page-rendering check | Product-page quote/NAV as of 2026-06-26; performance component rendered no records in the reviewed capture |
| Cboe BZX:NUSC | https://www.sec.gov/Archives/edgar/data/1635073/000119312526080215/d91437d497k.htm | SEC summary prospectus: listing, objective, fees, index strategy, annual return chart and best/worst quarters | Filed 2026-02-27; annual rows through 2025; best/worst quarter history through 2025-12-31 |
| MSCI Nuveen ESG USA Small-Cap Index | https://www.msci.com/indexes/index/711741/nuveen-esg-usa-small-cap-index | Issuer benchmark identity and index-provider cross-check | Index identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## NUSC raw observations and calculations

| Year | NUSC NAV TR | Nuveen ESG USA Small-Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 16.62% | 17.13% | 21.83% |
| 2018 | -9.28% | -8.88% | -4.38% |
| 2019 | 26.82% | 27.37% | 31.49% |
| 2020 | 23.48% | 23.97% | 18.40% |
| 2021 | 17.83% | 18.26% | 28.71% |
| 2022 | -17.68% | -17.55% | -18.11% |
| 2023 | 15.50% | 15.80% | 26.29% |
| 2024 | 8.48% | 8.79% | 25.02% |
| 2025 | 7.60% | 7.85% | 17.88% |
| 2026 YTD | 16.76% (official NAV) | 16.94% (official issuer index) | not available from cached current-year benchmark |

- Metric basis: official Nuveen NAV total return includes reinvested distributions and fund expenses; the issuer index excludes fund expenses.
- Issuer benchmark: `Nuveen ESG USA Small-Cap Index`, calculated by MSCI; retained as metadata and not substituted for the common S&P 500 reference.
- NUSC 2017-2025 compound: `116.65%` cumulative; rounded-input CAGR `8.97%`.
- NUSC 2021-2025 compound: `30.77%` cumulative; rounded-input CAGR `5.51%`.
- Issuer index 2017-2025 compound: `123.26%` cumulative; rounded-input CAGR `9.33%`; 2021-2025 CAGR `5.79%`.
- S&P 500 cached 2017-2025 compound: `255.78%` cumulative; rounded-input CAGR `15.14%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: best quarter `+29.98%` in 4Q2020 and worst quarter `-30.76%` in 1Q2020 from the SEC summary prospectus; official daily NAV history for maximum drawdown/recovery was not verified.

## NUSC gaps and conflicts

- Inception was 13 Dec 2016, so 2016 is a partial inception period and the fund has not reached a full 10-year history as of 2026-06-30; no 10-year NAV CAGR is claimed.
- Nuveen's HTML product page rendered `No Records Available` for the performance component in the reviewed capture, while the official PDF factsheet dated 2026-06-30 supplied numeric calendar/YTD fields; the factsheet is used for performance and the rendering conflict is preserved here.
- The latest official NUSC performance field reviewed is `16.76%` NAV TR YTD as of 2026-06-30; the common S&P cache has no synchronized 2026 current-year row, so no current S&P YTD comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## IMWSF / WSML official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:WSML / input IMWSF | https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-fund?siteEntryPassthrough=true&switchLocale=y | Official iShares product page: USD share-class identity, listings, benchmark, TER, structure, current NAV/YTD, holdings and risk metrics | Current page observations: NAV 2026-08-14; NAV TR YTD 2026-08-13; portfolio/risk fields through 2026-07-31 |
| LSE:WSML / input IMWSF | https://www.ishares.com/gls-download/literature/fact-sheet/wsml-ishares-msci-world-small-cap-ucits-etf-fund-fact-sheet-en-gb.pdf | Official iShares factsheet: ISIN, launch, USD accumulating share class, physical/optimised structure, annual NAV/index rows, July YTD and listings | Factsheet dated July 2026; performance and NAV data as of 2026-07-31; other data as of 2026-08-07 |
| Input IMWSF alias | https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=IMWSF | Secondary OTC alias / ISIN cross-check; not used for NAV Total Return ranking | OTC identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current S&P 500 TR YTD cross-check | 14.04% as of 2026-08-16; not synchronized with WSML 2026-08-13 YTD |

## IMWSF / WSML raw observations and calculations

| Year | WSML NAV TR | MSCI World Small Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2019 | 25.73% | 26.19% | 31.49% |
| 2020 | 15.83% | 15.96% | 18.40% |
| 2021 | 15.81% | 15.75% | 28.71% |
| 2022 | -18.64% | -18.75% | -18.11% |
| 2023 | 16.02% | 15.76% | 26.29% |
| 2024 | 7.93% | 8.15% | 25.02% |
| 2025 | 19.84% | 19.88% | 17.88% |
| 2026 YTD | 19.00% (official NAV) | not available from same-date official product-page field | 14.04% (official current page, as of 2026-08-16; not same date) |

- Metric basis: official iShares NAV total return is shown on NAV basis with gross income reinvested where applicable; the accumulating USD share class retains income in NAV.
- Issuer benchmark: `MSCI World Small Cap Index (Net)`; retained as metadata and not substituted for the common S&P 500 reference.
- WSML 2019-2025 compound: `105.92%` cumulative; rounded-input CAGR `10.87%`.
- WSML 2021-2025 compound: `41.39%` cumulative; rounded-input CAGR `7.17%`.
- Issuer index 2019-2025 compound: `106.54%` cumulative; rounded-input CAGR `10.92%`; 2021-2025 CAGR `7.14%`.
- S&P 500 cached 2019-2025 compound: `205.41%` cumulative; rounded-input CAGR `17.29%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk fields: 3-year standard deviation `16.16%` and beta `1.000` as of 2026-06-30; holdings `3,558` as of 2026-07-30; official daily NAV history for maximum drawdown/recovery was not verified.

## IMWSF / WSML gaps and conflicts

- The OTC input `IMWSF` is not the canonical issuer listing. Official iShares listings for ISIN `IE00BF4RFH31` identify the USD line as `LSE:WSML`, with additional GBP/CHF/EUR listings; the durable key uses `LSE:WSML` while preserving the input alias.
- Inception was 27 Mar 2018; 2018 is a partial/inception period whose annual return is not disclosed in the reviewed official materials, and no 10-year NAV CAGR is claimed.
- The July factsheet reports NAV YTD `13.88%` as of 2026-07-31 while the newer product page reports `19.00%` as of 2026-08-13; these are separate as-of dates, so the newer product-page field is used as current and both observations are preserved.
- The current official S&P 500 TR page reports `14.04%` as of 2026-08-16, one date after the ETF current YTD; no synchronized current benchmark comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## BBSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Cboe BZX:BBSC` | https://am.jpmorgan.com/us/en/asset-management/adv/products/jpmorgan-betabuilders-us-small-cap-equity-etf-etf-shares-46641q290 | Official JPMorgan product page: identity, objective, tracked index and product context | Page reviewed 2026-08-17; current exchange context cross-checked against SEC materials |
| `Cboe BZX:BBSC` | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBSC.PDF | Official factsheet: passive approach, benchmark, inception, fee, annual NAV returns, current NAV/market-price/benchmark fields and return basis | Factsheet dated 2026-06-30; annual rows 2021-2025 and current fields as of 2026-06-30 |
| `Cboe BZX:BBSC` | https://www.sec.gov/Archives/edgar/data/1485894/000119312526071799/d46741d497k.htm | SEC summary prospectus: objective, index strategy, fees and passive structure | Filed 2026-03-01; listing and strategy context reviewed 2026-08-17 |
| `Cboe BZX:BBSC` | https://www.sec.gov/Archives/edgar/data/1485894/000119312526128970/d123344d497k.htm | SEC supplement: exchange-transfer notice | Dated 2026-03-27; transfer from NYSE Arca to Cboe BZX effective 2026-04-16 |
| `Cboe BZX:BBSC` | https://www.sec.gov/Archives/edgar/data/1485894/000119312526152486/d134932d8a12b.htm | SEC Form 8-A: current Cboe BZX registration cross-check | Filed 2026-04-16; BBSC registered on Cboe BZX |
| `Cboe BZX:BBSC` | https://am.jpmorgan.com/us/en/asset-management/per/about-us/media/press-releases/jp-morgan-transfer-14-etfs-from-current-exchanges/ | JPMorgan exchange-transfer announcement | Reviewed 2026-08-17 |
| Parent input identity | `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md` | Exact parent backlog row used to disambiguate U.S. BBSC from the Ireland UCITS ticker | Line 16: JPMorgan BetaBuilders U.S. Small Cap Equity ETF, parent input snapshot |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## BBSC raw observations and calculations

| Year | BBSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 15.55% | 28.71% |
| 2022 | -19.71% | -18.11% |
| 2023 | 20.03% | 26.29% |
| 2024 | 12.37% | 25.02% |
| 2025 | 10.56% | 17.88% |

- Metric basis: official JPMorgan NAV total return assumes dividends and capital gains are reinvested; NAV return reflects fund fees and expenses; currency USD.
- Issuer benchmark: `Morningstar US Small Cap Target Market Exposure Extended Index`; retained as metadata and not substituted for the common S&P 500 reference.
- BBSC 2021-2025 compound: `38.35%` cumulative; rounded-input CAGR `6.71%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Up years / down years: `4 / 1`; best `2021 +15.55%`; least positive `2025 +10.56%`; worst and least bad down year `2022 -19.71%`.
- Current official fields as of 2026-06-30: NAV TR YTD `23.96%`, market-price return `24.13%`, issuer benchmark `24.11%`.

## BBSC gaps and scheduled-inline local review

- The exact parent input row at `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md:16` identifies the intended U.S. fund. This resolves the ticker ambiguity with the Ireland UCITS BBSC listing before saving.
- Current canonical exchange is `Cboe BZX`; the prior NYSE Arca listing and 2026-04-16 transfer are preserved in the SEC source map. No old exchange slug is used for the durable page.
- Inception was 2020-11-16; 2020 is an inception-year partial period and no 10-year NAV CAGR is claimed. Complete annual calculations use official 2021-2025 rows only.
- The latest official current performance fields reviewed are as of 2026-06-30; no synchronized 2026-08-17 official NAV/price snapshot is asserted.
- The common S&P 500 annual cache ends 2025-12-31; no current-year S&P comparison is asserted against BBSC's 2026-06-30 fields.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.
- Planned durable paths: create `wiki/analysis/performance/ETF_CBOE_BZX_BBSC Performance.md`; update `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `USA`; add breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`; add `geography/United-States`; link the new page from USA navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

## ISCF official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ISCF` | https://www.ishares.com/us/products/272823/ishares-international-small-cap-equity-factor-etf | Official iShares product page: identity, exchange, benchmark, inception, current NAV/price/YTD, holdings and risk fields | Current NAV/price 2026-08-14; NAV TR YTD 2026-08-13; holdings 2026-08-13; risk fields through 2026-07-31 |
| `NYSE Arca:ISCF` | https://www.ishares.com/us/literature/fact-sheet/iscf-ishares-international-small-cap-equity-factor-etf-fund-fact-sheet-en-us.pdf | Official factsheet: NAV/market-price/benchmark rows 2021-2025, return basis, current benchmark metadata and fund characteristics | Factsheet as of 2026-06-30; 2025 row and annual benchmark rows through 2025 |
| `NYSE Arca:ISCF` | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-edge-msci-multifactor-intl-small-cap-etf-7-31.pdf | Official summary prospectus: passive objective, fees, 2016-2024 calendar NAV rows, best/worst quarters and benchmark splice | Dated 2025-11-28; annual chart through 2024; calendar YTD field in prospectus is stale and not used for current YTD |
| Parent input identity | `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md` | Exact parent backlog row used to confirm the intended iShares fund and current quote snapshot | Line 17: iShares International Small-Cap Equity Factor ETF, input price `46.04` |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## ISCF raw observations and calculations

| Year | ISCF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.01% | 11.96% |
| 2017 | 36.24% | 21.83% |
| 2018 | -18.18% | -4.38% |
| 2019 | 25.94% | 31.49% |
| 2020 | 7.89% | 18.40% |
| 2021 | 13.22% | 28.71% |
| 2022 | -15.06% | -18.11% |
| 2023 | 11.52% | 26.29% |
| 2024 | 4.33% | 25.02% |
| 2025 | 34.07% | 17.88% |

- Metric basis: official iShares NAV total return assumes reinvestment of dividends/capital gains and deducts fund expenses; currency USD.
- Issuer benchmark annual rows in the June 2026 factsheet for 2021-2025 are `13.43%`, `-15.01%`, `11.75%`, `4.67%`, and `33.75%`; they are retained as issuer metadata and not substituted for the common S&P 500 reference.
- Benchmark splice: historical index data before 2023-03-01 is `MSCI World ex USA Small Cap Diversified Multiple-Factor Index (Net)`; data from 2023-03-01 is `STOXX International Small-Cap Equity Factor Index (Net)`.
- ISCF 2016-2025 compound: `127.24%` cumulative; rounded-input CAGR `8.55%`.
- ISCF 2021-2025 compound: `50.01%` cumulative; rounded-input CAGR `8.45%`.
- Issuer rolling 10-year NAV TR average annual: `9.69%` as of 2026-06-30; raw rolling endpoints are not disclosed and this is not substituted for the calendar-window CAGR.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Up years / down years: `8 / 2`; best `2017 +36.24%`; least positive `2016 +0.01%`; worst `2018 -18.18%`; least bad down year `2022 -15.06%`.
- Current official fields: NAV TR YTD `12.52%` as of 2026-08-13; NAV `US$45.93` and closing price `US$46.04` as of 2026-08-14; 3-year standard deviation `14.21%` and beta `0.73` as of 2026-07-31; holdings `1,161` as of 2026-08-13.

## ISCF gaps, benchmark splice, and scheduled-inline local review

- The exact parent input row at `/Users/mangkornkatawong/Documents/md_output/current-filtered-etfs-14.md:17` identifies the intended iShares International Small-Cap Equity Factor ETF; no ticker alias conflict was found.
- The annual evidence is intentionally spliced by source date: SEC summary prospectus rows for 2016-2024 and the June 2026 official factsheet row for 2025. The overlapping 2021-2024 NAV rows reconcile exactly.
- The issuer benchmark changed on 2023-03-01 from the MSCI World ex USA Small Cap Diversified Multiple-Factor Index (Net) to the STOXX International Small-Cap Equity Factor Index (Net); this is preserved and not treated as a homogeneous single-index history.
- The latest official current NAV TR field reviewed is `12.52%` as of 2026-08-13; the common S&P cache has no synchronized 2026 current-year row, so no current S&P comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.
- Planned durable paths: create `wiki/analysis/performance/ETF_NYSE_ARCA_ISCF Performance.md`; update `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/comparisons/ETF Region Index.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Planned graph changes: primary region `International`; add breadcrumb `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`; add `geography/International` and `geography/international-ex-US`; link the new page from International navigation and the performance index; keep annual numeric ownership in the performance page.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
