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

ใช้ `check-etf-performance` sequential queue ต่อเนื่องตามลำดับทีละ ticker. รอบนี้รวมผลถึง row `125/125`, ทำ mandatory 10-year coverage audit จาก official product page/factsheet/SEC prospectus/annual report และใช้ local pre-save fallback เนื่องจากไม่มี independent reviewer.

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
| SMHC | supported | Nasdaq:SMHC | China | not disclosed | https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/ | passive/index-tracking China semiconductor equity ETF; official inception 2026-06-23; 10-year NAV TR unavailable; official fund NAV/market-price rows and current NAV YTD not disclosed; underlying-index 1-month return not used as ETF proxy; new-fund history gap |
| FCA | supported | Nasdaq:FCA | China | -1.23% (2026-06-30) | https://www.ftportfolios.com/Retail/etf/ETFsummary.aspx?Ticker=FCA | passive/index-tracking China equity ETF; official rolling 10Y NAV TR CAGR 8.19% for 2016-06-30 to 2026-06-30; official calendar NAV rows 2016-2025; 2021-2025 CAGR 4.16%; 2015-07-14 index change; factsheet 2024/2025 annual-row conflict resolved in favor of annual report/summary prospectus |
| IND | supported | Nasdaq:IND | India | not disclosed | https://etf.dws.com/download/asset/048952ad-b7d4-462d-95c8-e726ff2484bd | passive/index-tracking India broad equity ETF tracking Nifty 500 Index; official inception 2025-11-24 (listing/commencement 2025-11-25); 10-year NAV TR unavailable; latest official 3-month NAV TR -18.41% through 2026-03-31; inception-to-date endpoints and current YTD not disclosed; no annualization of short-period return |
| VNAM | supported | NYSE Arca:VNAM | Vietnam | not disclosed | https://www.globalxetfs.com/funds/vnam?download_full_holdings=true | passive/index-tracking Vietnam equity ETF tracking MSCI Vietnam Select 25-50 Index; official inception 2021-12-07; 10-year NAV TR unavailable; official available-period NAV TR annualized 0.34% since inception, 1Y 45.10% and 3Y 15.86% as of 2026-06-30; raw endpoints, annual NAV rows and current YTD not disclosed |
| ISAGF | unsupported ETF type | LSE:IGEA | not applicable | not applicable | https://www.ishares.com/ch/professionals/en/products/251723/ishares-emerging-asia-local-government-bond-ucits-etf | Input OTC alias `ISAGF` maps to the official USD London Stock Exchange line `IGEA` for ISIN `IE00B6QGFW01`; iShares classifies the fund as `Fixed Income` and tracks local-currency government bonds from Asian Emerging Market countries; bond ETF is outside passive/index-tracking equity scope; no performance artifact created |
| FLIBF | supported | LSE:FLXI | India | -8.42% (2026-06-30) | https://www.franklintempleton.co.uk/our-funds/etf/price-and-performance/products/27853/SINGLCLASS/franklin-ftse-india-ucits-etf/IE00BHZRQZ17 | Input OTC alias `FLIBF` resolves to the official USD London Stock Exchange line `FLXI` for ISIN `IE00BHZRQZ17`; passive/indexed physical full-replication India equity ETF tracking FTSE India 30/18 Capped Index-NR; inception 2019-06-25; 10-year NAV TR unavailable; official June 2026 factsheet gives available-period NAV TR cumulative 64.43% / annualized 7.35%, calendar NAV rows 2020-2025, and YTD -8.42% |
| IHRPF | supported | LSE:FXC | China | -17.31% (2026-06-30) | https://www.ishares.com/ch/individual/en/products/251798/ishares-china-large-cap-ucits-etf | Input OTC alias `IHRPF` resolves to the official USD London Stock Exchange line `FXC` for ISIN `IE00B02KXK85`; passive/physical China large-cap equity ETF tracking FTSE China 50 Index - USD Net Div; official rolling 10Y NAV TR cumulative 18.61% / CAGR 1.72% for 2016-06-30 to 2026-06-30; official 2016-2025 calendar NAV rows; benchmark changed 2014-09-19 |
| FLCH | supported | NYSE Arca:FLCH | China | -10.65% (2026-07-10) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26362/SINGLCLASS/franklin-ftse-china-etf/FLCH | Passive/indexed physical China large-/mid-cap equity ETF tracking FTSE China RIC Capped Index; inception 2017-11-02 means 10-year NAV TR unavailable; official available-period NAV TR average annual -0.24% through 2026-06-30; official calendar rows 2018-2025; current YTD -10.65% as of 2026-07-10 |
| KPHO | supported | NYSE:KPHO | Vietnam | -2.52% (2026-06-30) | https://kraneshares.com/etf/kpho/ | Passive/index-tracking Vietnam equity ETF tracking Dragon Capital MerQube Vietnam Growth Total Return Index; inception 2025-12-02 means 10-year NAV TR unavailable; official available-period NAV TR cumulative -4.05% through 2026-06-30; no annualization because period is under one year; current page/report says NYSE while older prospectus says NYSE Arca |
| INQQ | supported | NYSE Arca:INQQ | India | -26.17% (2026-03-31; latest numeric official static capture) | https://emqqglobaletfs.com/inqq-fund-materials | Passive/index-tracking non-diversified India internet/e-commerce equity ETF; inception 2022-04-05 means 10-year NAV TR unavailable; official available-period NAV TR annualized -7.83% and numeric YTD -26.17% as of 2026-03-31; calendar NAV rows and later numeric month-end YTD not disclosed in reviewed official capture; current page/factsheet use NYSE while SEC/report/factsheet formal listing says NYSE Arca |
| TSMY | unsupported ETF type | NYSE Arca:TSMY | Taiwan single-stock/options | not applicable | https://yieldmaxetfs.com/our-etfs/tsmy/ | YieldMax identifies TSMY as an actively managed option-income ETF selling call spreads on Taiwan Semiconductor Manufacturing Co. (TSM); single-issuer and derivative/option-income structure is outside passive/index-tracking equity ETF scope; no performance page or region/index row created |
| IMVP | completed_10Y | NYSE Arca:IMVP | India | not disclosed (2026-07-26) | https://www.sec.gov/Archives/edgar/data/1419139/000119312526062436/d71791d497k.htm | Passive/index-tracking Invesco India ETF; official NAV TR 10Y CAGR `9.19%` for 2015-12-31 to 2025-12-31; official calendar rows 2016-2025; current post-change 2026 YTD not disclosed; PIN → IMVP and FTSE → Bloomberg index change disclosed |
| KMCA | completed_available_period_no_10Y | NYSE Arca:KMCA | South Korea | -5.14% (2026-06-30) | https://plusetf.com/kmca | Passive/index-tracking South Korea thematic equity ETF tracking Akros Korea Manufacturing Core Alliance Index; inception `2026-05-06`; 10-year NAV TR unavailable; official Fund NAV since-inception/YTD `-5.14%` through `2026-06-30`; no complete calendar year and no annualization of 55-day period |
| MAGC | unsupported ETF type | Cboe BZX:MAGC | China | not applicable | https://www.roundhillinvestments.com/etf/magc/ | Roundhill identifies MAGC as actively managed; the fund uses total-return swaps and concentrated China single-country/sector exposure, outside the required passive/index-tracking equity ETF scope; no performance page or region/index row created |
| ISVBF | completed_available_period_no_10Y | Euronext Amsterdam:ICHN | China | -8.79% (2026-07-21) | https://www.ishares.com/uk/individual/en/products/308751/ishares-msci-china-ucits-etf?siteEntryPassthrough=true | OTC alias maps by ISIN `IE00BJ5JPG56` to the official Euronext Amsterdam USD line `ICHN`; passive physical/replicated China equity ETF; inception `2019-06-20`; official 2020-2025 rows compound to `8.36%` / `1.35%` CAGR; 10-year NAV TR unavailable; 2016-2019 rows and raw endpoints not disclosed |
| KURE | completed_available_period_no_10Y | NYSE Arca:KURE | China | -8.80% (2026-06-30) | https://kraneshares.com/etf/kure/ | Passive/index-tracking China healthcare equity ETF tracking MSCI China All Shares Health Care 10/40 Index; inception `2018-01-31`; 10-year NAV TR unavailable; official since-inception NAV TR cumulative `-23.43%` / annualized `-3.12%` through `2026-06-30`; exact calendar NAV rows not disclosed in reviewed official capture; current NAV `US$17.53` as of `2026-07-23` |
| FXY | unsupported ETF type | NYSE Arca:FXY | not applicable | not applicable | https://www.invesco.com/us/en/financial-products/etfs/invesco-currencyshares-japanese-yen-trust.html | Invesco identifies FXY as a CurrencyShares Japanese Yen Trust designed to track the Japanese yen; SEC identifies it as a grantor trust holding Japanese yen. Currency trust/FX exposure is outside the required passive index-tracking equity ETF scope; no performance page or region/index row created |
| KRANF | completed_available_period_no_10Y | LSE:KWEB | China | -28.96% (2026-06-30) | https://kraneshares.eu/etf/kwebln/ | OTC alias resolves by fund identity to the official USD UCITS line `KWEB LN`, ISIN `IE00BFXR7892`; passive physical/index-tracking China internet equity ETF; inception `2018-11-21`; 10-year NAV TR unavailable; official since-inception NAV TR cumulative `-26.60%` / annualized `-3.98%`; corrected KIID annual rows 2019-2025; current NAV `US$19.82` as of `2026-07-24` |
| KHYB | unsupported ETF type | NYSE:KHYB | not applicable | not applicable | https://kraneshares.com/etf/khyb/ | KraneShares identifies KHYB as an active ETF investing in USD-denominated Asian high-yield debt; fixed-income and active management are outside the required passive index-tracking equity ETF scope. Current issuer page says NYSE; 2025 SEC prospectus says NYSE Arca, and the conflict is disclosed. No performance page or region/index row created |
| VNM | completed_10Y | Cboe BZX:VNM | Vietnam | -12.07% (2026-07-24) | https://www.vaneck.com/us/en/investments/vietnam-etf-vnm/ | Current prospectus identifies Cboe BZX; passive Vietnam equity ETF; official rolling 10Y NAV TR CAGR `3.65%` for 2016-06-30 to 2026-06-30; official annual NAV rows 2016-2025; June month-end YTD `-1.41%` versus later current snapshot `-12.07%` |
| EIDO | completed_10Y | NYSE Arca:EIDO | Indonesia | -31.36% (2026-07-23) | https://www.ishares.com/us/products/239661/ishares-msci-indonesia-etf | Passive/index-tracking Indonesia equity ETF; official rolling 10Y NAV TR cumulative `-40.80%` / CAGR `-5.11%` for 2016-06-30 to 2026-06-30; official 2016-2025 annual NAV rows; June month-end YTD `-38.53%` versus later current snapshot `-31.36%` |
| GLIN | completed_10Y | NYSE Arca:GLIN | India | -4.15% (2026-07-24) | https://www.vaneck.com/us/en/investments/india-growth-leaders-etf-glin/ | Passive/index-tracking India factor/growth-leaders equity ETF; official rolling 10Y NAV TR CAGR `1.92%` for 2016-06-30 to 2026-06-30; official 2016-2025 annual NAV rows; June month-end YTD `0.25%` versus later current snapshot `-4.15%` |
| KTEC | completed_available_period_no_10Y | NYSE Arca:KTEC | Hong Kong | -22.88% (2026-06-30) | https://kraneshares.com/etf/ktec/ | Passive/index-tracking Hong Kong technology equity ETF; inception `2021-06-08`; 10-year NAV TR unavailable; available-period NAV TR `-49.08%` cumulative / issuer annualized `-12.48%`; official 2022-2024 annual rows; 2025 row not disclosed; current-page exchange wording `NYSE` versus formal `NYSE Arca` disclosed |
| EWM | completed_10Y | NYSE Arca:EWM | Malaysia | 4.62% (2026-07-17) | https://www.ishares.com/us/products/239669/ishares-msci-malaysia-etf | Passive/index-tracking Malaysia equity ETF; official rolling 10Y NAV TR cumulative `24.54%` / CAGR `2.22%` for 2016-06-30 to 2026-06-30; official 2021-2025 annual NAV rows; earlier annual rows/raw rolling endpoints not disclosed |
| BABO | unsupported ETF type | NYSE Arca:BABO | not applicable | not applicable | https://yieldmaxetfs.com/our-etfs/babo/ | YieldMax identifies BABO as actively managed, single-issuer BABA option-income ETF selling call spreads; derivative/option-income structure fails the passive index-tracking equity scope; no performance artifact created |
| KLIP | unsupported ETF type | NYSE Arca:KLIP | not applicable | not applicable | https://kraneshares.com/etf/klip/ | KraneShares identifies KLIP as active covered-call/buy-write ETF owning KWEB and selling KWEB call options; formal prospectus says NYSE Arca while current page says NYSE; covered-call/derivative structure fails passive index-tracking equity scope; no performance artifact created |
| ADVE | unsupported ETF type | NYSE Arca:ADVE | Asia | not applicable | https://us.matthewsasia.com/funds/etfs/asia-dividend-active-etf/ | Matthews identifies ADVE as an unconstrained all-cap active Asia equity ETF with a quality bias; official strategy requires at least 80% in dividend-paying equity securities; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| FLAX | supported | NYSE Arca:FLAX | Asia ex Japan | 24.71% (2026-06-30) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26346/SINGLCLASS/franklin-ftse-asia-ex-japan-etf/FLAX | passive/index-tracking Asia ex Japan equity ETF; official inception 2018-02-06; 10-year field `—`; available-period NAV TR CAGR 7.85% for 2018-02-06 to 2026-06-30; official 2019-2025 NAV rows compound to 77.17% / CAGR 8.51%; current standardized YTD 24.71% |
| VGDTF | supported | XETRA:VJPA | Japan | 15.27% (2026-06-30) | https://www.vanguard.co.uk/professional/product/etf/equity/9674/vanguard-ftse-japan-ucits-etf-usd-accumulating | OTC alias cross-checked to Vanguard FTSE Japan UCITS ETF (USD) Accumulating, ISIN IE00BFMXYX26; official Deutsche Börse EUR line VJPA; passive physical/index-tracking equity; inception 2019-09-24; 10-year field `—`; since-inception NAV TR CAGR 9.96%; official KIID 2020-2025 calendar rows; current standardized YTD 15.27% |
| RAYJ | unsupported ETF type | NYSE Arca:RAYJ | Japan | not applicable | https://funds.rayliant.com/rayj/ | Rayliant identifies RAYJ as an active Japan equity strategy using SMDAM fundamental research and Rayliant quantitative models; it fails the passive/index-tracking equity gate, so no performance page or NAV TR comparison is created |
| THD | supported | NYSE Arca:THD | Thailand | 25.53% (2026-07-22) | https://www.ishares.com/us/products/239688/ishares-msci-thailand-capped-etf | passive/index-tracking equity ETF; official rolling 10Y NAV TR CAGR 3.35% for 2016-06-30 to 2026-06-30 (`10.00` years); 2021-2025 NAV rows compound to -10.24% / CAGR -2.14%; 2016-2020 annual rows and raw rolling endpoints not disclosed; benchmark/index change 2013-02-12 |
| FLIN | supported | NYSE Arca:FLIN | India | -8.34% (2026-06-30) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26348/SINGLCLASS/franklin-ftse-india-etf/FLIN | passive/index-tracking equity ETF; inception 2018-02-06; official 10-year field `—`; available-period NAV TR annualized 5.91% for 2018-02-06 to 2026-06-30 (`8.39` years); 2019-2025 NAV rows compound to 88.74% / CAGR 9.50%; 2021-2025 CAGR 9.33%; current standardized NAV TR YTD -8.34% |
| CNYA | supported | Cboe BZX:CNYA | China | 5.39% (2026-07-21) | https://www.ishares.com/us/products/273318/ishares-msci-china-a-etf | passive/index-tracking China A-share equity ETF; official rolling 10Y NAV TR cumulative 91.51% / CAGR 6.71% for 2016-06-30 to 2026-06-30; official 2021-2025 NAV/benchmark rows; 2016-2020 annual rows not disclosed; current NAV TR YTD 5.39% as of 2026-07-21; benchmark change 2018-04-26 |
| NBJP | unsupported ETF type | NYSE Arca:NBJP | Japan | not applicable | https://www.nb.com/products/etfs/japan-equity-etf | Neuberger identifies NBJP as an actively managed, all-cap Japan equity ETF using a proprietary scoring system and direct engagements; official factsheet reports active share 63.87% as of 2026-03-31; outside passive/index-tracking ETF scope, so no performance page or NAV TR comparison is created |
| ASHR | supported | NYSE Arca:ASHR | China | not disclosed | https://etf.dws.com/download/asset/e73aaa93-92c6-4a51-9233-38ccb329e09b | passive/index-tracking China A-share equity ETF; official rolling 10Y NAV TR CAGR 5.84% for 2016-06-30 to 2026-06-30; normalized endpoint approx. 176.40; official 2016-2024 NAV rows compound to 4.89% / CAGR 0.53%; 2025/current YTD and CSI 300 annual rows not disclosed |
| ASEA | supported | NYSE Arca:ASEA | Southeast Asia | 8.67% (2026-05-31) | https://www.globalxetfs.com/funds/asea | passive/index-tracking Southeast Asia equity ETF; official rolling 10Y NAV TR CAGR 7.12% for 2016-06-30 to 2026-06-30; official 2016-2025 NAV rows compound to 102.43% / CAGR 7.31%; latest official factsheet YTD 8.67% as of 2026-05-31; 2021-2025 CAGR 8.82%; index annual rows not disclosed |
| KCAI | supported | NYSE Arca:KCAI | China | 4.27% (2026-06-30) | https://kraneshares.com/etf/kcai/ | passive/rules-based index-tracking China A-share equity ETF; official inception 2024-08-27 means 10-year NAV TR unavailable; official since-inception NAV TR cumulative 76.27% / annualized 36.06% as of 2026-06-30; official current YTD 4.27%; current product page says NYSE while official prospectus/factsheet/annual report say NYSE Arca, so NYSE Arca is used and conflict is disclosed |
| EWS | supported | NYSE Arca:EWS | Singapore | 16.50% (2026-07-21) | https://www.ishares.com/us/products/239678/ishares-msci-singapore-capped-etf | passive/index-tracking Singapore equity ETF; official rolling 10Y NAV TR cumulative 112.54% / CAGR 7.83% for 2016-06-30 to 2026-06-30; official 2021-2025 NAV/index rows; 2016-2020 annual NAV rows not disclosed; current NAV TR YTD 16.50% as of 2026-07-21; benchmark change to MSCI Singapore 25/50 Index (Net) on 2016-12-01 |
| BBAX | supported | Cboe BZX:BBAX | Asia-Pacific | 8.20% (2026-06-30) | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBAX.PDF | passive/index-tracking developed Asia-Pacific equity ETF; official class launch 2018-08-07 means 10-year NAV TR unavailable; available-period NAV TR cumulative 64.48% / annualized CAGR 6.50% through 2026-06-30; official 2019-2025 NAV rows; Cboe/SEC listing confirmation |
| PCCE | unsupported ETF type | NYSE Arca:PCCE | China | not applicable | https://www.polencapital.com/perspectives/polen-expands-active-etf-lineup-two-credit-etfs | official Polen/SEC materials identify PCCE as an actively managed China equity ETF; passive/index-tracking equity scope excludes it; no performance page or region/index row created |
| MJSC | unsupported ETF type | NYSE Arca:MJSC | Japan | not applicable | https://www.mufgetfs.com/mjsc | official MUFG product page confirms NYSE Arca listing, `Active ETF` classification and an actively managed Japan small-cap strategy; passive/index-tracking equity scope excludes it; no performance page or region/index row created |
| INDE | unsupported ETF type | NYSE Arca:INDE | India | not applicable | https://us.matthewsasia.com/funds/etfs/india-active-etf/ | official Matthews factsheet/page identify NYSE Arca listing and an actively managed all-cap India equity strategy; passive/index-tracking equity scope excludes it; no performance page or region/index row created |
| KBA | supported | NYSE Arca:KBA | China | 11.37% (2026-06-30) | https://kraneshares.com/etf/kba/ | passive/index-tracking China A-share ETF tracking MSCI China A 50 Connect Index; official rolling 10Y NAV TR CAGR 6.90% for 2016-06-30 to 2026-06-30; official 2016-2024 calendar NAV rows; 2025 calendar row not disclosed; current product page says `NYSE` while official prospectus/annual report say `NYSE Arca`, so the canonical key is corrected to NYSE Arca:KBA |
| JCHI | unsupported ETF type | NYSE Arca:JCHI | China | not applicable | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JCHI.PDF | official JPMorgan factsheet identifies JPMorgan Active China ETF and a bottom-up stock-selection approach; SEC shareholder-report data identify NYSE Arca listing; passive/index-tracking equity scope excludes it; no performance page or region/index row created |
| MCH | unsupported ETF type | NYSE Arca:MCH | China | not applicable | https://www.matthewsasia.com/funds/etfs/china-active-etf/ | official Matthews page identifies MCH as Matthews China Active ETF, primary exchange NYSE Arca, and an all-cap fundamental GARP strategy; passive/index-tracking equity scope excludes it; no performance page or region/index row created |
| CGRO | unsupported ETF type | NYSE Arca:CGRO | China | not applicable | https://www.cvafunds.com/cgro/ | official CoreValues summary prospectus identifies CGRO as an actively managed Greater China growth ETF and lists NYSE Arca; current website displays `NYSE`, but the formal prospectus is retained for canonical exchange resolution; passive/index-tracking equity scope excludes it; no performance page or region/index row created |
| KBUF | unsupported ETF type | NYSE Arca:KBUF | China | not applicable | https://kraneshares.com/etf/kbuf/ | official KraneShares sources identify KBUF as a defined-outcome ETF using FLEX options, an upside cap and a 90% downside buffer on KWEB; derivative-heavy/active strategy scope excludes it; no performance page or region/index row created |
| KPRO | unsupported ETF type | NYSE Arca:KPRO | China | not applicable | https://kraneshares.com/etf/kpro/ | official KraneShares sources identify KPRO as a defined-outcome ETF using FLEX options, a 20.01% upside cap and a 100% downside buffer on KWEB; derivative-heavy/active strategy scope excludes it; no performance page or region/index row created |
| KSTR | supported | NYSE Arca:KSTR | China | 71.70% (2026-06-30) | https://kraneshares.com/etf/kstr/ | passive/index-tracking China STAR 50 technology/semi equity ETF; official inception 2021-01-26 means 10-year NAV TR unavailable; official since-inception NAV TR cumulative 27.40% / annualized 4.56% through 2026-06-30; calendar NAV rows not disclosed |
| NDIA | unsupported | NYSE Arca:NDIA | India | not applicable | https://www.globalxetfs.com/funds/NDIA | official Global X sources identify NDIA as the actively managed Global X India Active ETF; it fails the passive/index-tracking equity gate and no performance artifact is created |
| CHIQ | supported | NYSE Arca:CHIQ | China | -25.23% (2026-07-21) | https://www.globalxetfs.com/funds/CHIQ | passive/index-tracking China consumer discretionary equity ETF; official 10 complete calendar NAV TR rows 2016-2025 compound to 99.05% / CAGR 7.13%; official rolling 10Y NAV TR CAGR 5.31% through 2026-06-30; benchmark/strategy change effective 2018-12-06 disclosed |
| IOPP | unsupported | NYSE Arca:IOPP | India | not applicable | https://www.simplify.us/etfs/iopp-simplify-tara-india-opportunities-etf | official Simplify sources identify IOPP as an actively managed India equity ETF using bottom-up stock selection and a goal of outperforming MSCI India; it fails the passive/index-tracking equity gate and no performance artifact is created |
| MCHI | supported | NASDAQ:MCHI | China | -9.33% (2026-07-21) | https://www.ishares.com/us/products/239619/ishares-msci-china-etf | passive/index-tracking China equity ETF; official rolling 10Y NAV TR cumulative 45.52% / CAGR 3.82% through 2026-06-30; official 2021-2025 annual NAV rows; 2016-2020 rows not disclosed in reviewed capture; expense ratio 0.59% |
| ADIV | unsupported | NYSE Arca:ADIV | Asia-Pacific | not applicable | https://www.gafunds.com/our-funds/ | official Guinness Atkinson prospectus identifies ADIV as actively managed using proprietary research and fundamental analysis; it fails the passive/index-tracking equity gate and no performance artifact is created |
| EPHE | supported | NYSE Arca:EPHE | Philippines | 3.93% (2026-07-21) | https://www.ishares.com/us/products/239675/ishares-msci-philippines-etf | passive/index-tracking Philippines equity ETF; official rolling 10Y NAV TR cumulative -28.05% / CAGR -3.24% through 2026-06-30; official 2021-2025 annual rows; 2016-2020 rows not disclosed; index change 2020-12-01; expense ratio 0.59% |
| CAS | unsupported | NYSE Arca:CAS | China | not applicable | https://www.simplify.us/etfs/cas-simplify-china-shares-plus-income-etf | official Simplify page and formal prospectus identify CAS as actively managed with China A-share exposure via total return swaps plus an options overlay; derivative-heavy/option-income/multi-strategy, outside passive/index-tracking equity scope; formal prospectus says NYSE Arca while 1Q26 factsheet compact field says NYSE |
| INDZ | unsupported | NYSE Arca:INDZ | India | not applicable | https://www.vaneck.com/us/en/investments/india-select-etf-indz/ | official VanEck product page, factsheet and summary prospectus identify INDZ as actively managed with a multi-step/security-selection process for Indian companies; it fails the passive/index-tracking equity gate and no performance artifact is created |
| INDQ | supported | Nasdaq:INDQ | India | not disclosed (official field N/A) | https://www.paceretfs.com/products/indq | passive/rules-based India equity ETF tracking ActiveAlpha India Quality Index; official inception 2026-03-31 means 10-year NAV TR unavailable; official Pacer page/factsheet show available-period NAV TR and YTD fields as N/A; no proxy used |
| ICNYF | unsupported | LSE:CNYB | China | not applicable | https://www.ishares.com/uk/individual/en/products/308851/ishares-china-cny-bond-ucits-etf?siteEntryPassthrough=true | OTC alias resolved to iShares China CNY Bond UCITS ETF USD (Dist), ISIN IE00BYPC1H27 / LSE:CNYB; official fund is fixed income/bond exposure to Chinese government and policy-bank bonds, outside passive/index-tracking equity scope |
| CNQQ | supported | NASDAQ:CNQQ | China | 14.95% (2026-06-30) | https://funds.rayliant.com/cnqq/ | passive/index-tracking China technology equity ETF tracking Solactive ChinaAMC Transformative China Tech Index; inception 2025-09-24 means 10-year NAV TR unavailable; official available-period NAV TR cumulative 6.54% / derived annualized 8.65% through 2026-06-30; total-return-swap implementation and factsheet one-day inception conflict disclosed |
| INDH | supported | Nasdaq:INDH | India | -9.04% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/indh | passive/index-tracking India equity ETF with INR hedge; official inception 2024-05-09 means 10-year NAV TR unavailable; official available-period NAV TR cumulative 1.84% / average annual 0.85% through 2026-06-30; annual rows not disclosed; aggregate hedge ratio 100.25% as of 2026-07-17 |
| DGIN | supported | NYSE Arca:DGIN | India | -14.23% (2026-06-23) | https://www.vaneck.com/us/en/investments/digital-india-etf-dgin/overview/ | passive/index-tracking India digital-economy equity ETF; official inception 2022-02-15 means 10-year NAV TR unavailable; standardized since-inception NAV TR average annual -0.37% through 2026-05-31; latest product-page YTD -14.23% through 2026-06-23; raw endpoints and complete annual rows not disclosed; stale 2026-03-31 performance block and 2026-03-20 index-methodology change disclosed |
| CBON | unsupported ETF type | NYSE Arca:CBON | China | not applicable | https://www.vaneck.com/us/en/investments/chinaamc-china-bond-etf-cbon/overview/ | official issuer/factsheet identify CBON as a fixed-income China bond ETF tracking FTSE Chinese Broad Bond 0-10 Diversified Select Index; bond exposure is outside passive/index-tracking equity scope; no performance page or region/index row created |
| TMH | unsupported ETF type | NYSE Arca:TMH | Japan | not applicable | https://adrhedged.com/security/toyota-motor-corporation-adrhedged/ | input name resolves to Toyota Motor Corporation ADRhedged; official issuer says the series invests at least 95% in Toyota ADRs plus a currency hedge contract; single-stock/derivative-heavy structure is outside passive/index-tracking equity scope; no performance page or region/index row created |
| WDAF | supported | Nasdaq:WDAF | Asia-Pacific | 6.77% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/wdaf | passive/index-tracking Asia-Pacific defense thematic equity ETF tracking WisdomTree Asia Defense Index; official inception 2025-09-12 means 10-year NAV TR unavailable; official since-inception NAV TR cumulative 0.56% through 2026-06-30; derived short-period CAGR 0.70%; complete annual rows unavailable because 2025 is an incomplete inception year |
| GIND | unsupported ETF type | Nasdaq:GIND | India | not applicable | https://am.gs.com/public-assets/documents/93d0d388-7dee-11f0-8231-f3a13ac1f6ac?view=true | official Goldman Sachs materials identify GIND as an active, local stock-picking India equity ETF seeking to go beyond the benchmark; active/discretionary management is outside passive/index-tracking equity scope; no performance page or region/index row created |
| TCHI | supported | NASDAQ:TCHI | China | -0.45% (2026-07-17) | https://www.ishares.com/us/products/325390/ishares-msci-china-multisector-tech-etf | passive/index-tracking China technology/multisector equity ETF tracking MSCI China Technology Sub-Industries Select Capped Index; official inception 2022-01-25 means 10-year NAV TR unavailable; official available-period NAV TR cumulative 18.39% / average annual 3.88% through 2026-06-30; official 2023-2025 NAV rows; latest current YTD -0.45% as of 2026-07-17; month-end standardized YTD 13.46% as of 2026-06-30 disclosed separately |
| JAPN | unsupported ETF type | NASDAQ:JAPN | Japan | not applicable | https://horizonkinetics.com/products/etf/japn/ | official Horizon Kinetics/SEC sources identify JAPN as an actively managed Japan owner-operator equity ETF using fundamental selection; active/discretionary management is outside passive/index-tracking equity scope; no performance page or region/index row created |
| FXA | unsupported ETF type | NYSE Arca:FXA | Australia | not applicable | https://www.invesco.com/us/en/financial-products/etfs/invesco-currencyshares-australian-dollar-trust.html | official Invesco sources identify FXA as a CurrencyShares grantor trust designed to track the Australian dollar plus accrued interest, not an equity ETF; currency trust/FX exposure is outside passive/index-tracking equity scope; no performance page or region/index row created |
| KGRN | supported | NYSE Arca:KGRN | China | -13.22% (2026-06-30) | https://kraneshares.com/etf/kgrn/ | passive/index-tracking China clean-technology thematic equity ETF tracking MSCI China IMI Environment 10/40 Index; official inception 2017-10-12 means 10-year NAV TR unavailable; official available-period NAV TR cumulative 7.53% / annualized 0.84% through 2026-06-30; current YTD -13.22%; complete calendar-year rows not disclosed; current-page NYSE vs formal NYSE Arca conflict disclosed |
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

## NBJP Sequential Queue Record

- Input row: `63/125`; input ticker: `NBJP`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:NBJP`; Neuberger's official Japan Equity ETF factsheet identifies NBJP and the listed exchange as NYSE Arca. No provider slug or guessed exchange is used.
- Type gate: Neuberger's official product materials describe NBJP as an actively managed, all-cap Japan equity ETF. The strategy seeks high-quality Japanese companies positioned for durable growth, uses a proprietary scoring system, and relies on direct collaborative engagements by active portfolio managers. The March 2026 factsheet reports active share `63.87%` as of `2026-03-31`. This is active management, not passive/index tracking, so the workflow stops at the type gate.
- Mandatory 10-year coverage audit: not applicable after the confirmed unsupported-type classification. No NAV Total Return history, annual-return table, S&P 500 comparison, or proxy was created.
- Classification context only: official factsheet identifies benchmark MSCI Japan (Net), `62` holdings, and standard deviation `18.63` as of `2026-03-31`; these figures are not used to create a performance page because NBJP is outside supported ETF scope.

### NBJP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:NBJP` | [Neuberger Japan Equity ETF product page](https://www.nb.com/products/etfs/japan-equity-etf) | Canonical fund identity, active strategy, investment approach and risk context | Page accessed `2026-07-24`; current issuer page and product materials |
| `NYSE Arca:NBJP` | [Neuberger NBJP factsheet](https://www.nb.com/handlers/documents.ashx?item_id=180e87bb-9bfe-4095-afb8-16e775b3427f) | Exchange, active-share evidence, benchmark, holdings and risk-statistics cross-check | Factsheet `1Q26` as of `2026-03-31` |
| `NYSE Arca:NBJP` | [Neuberger official prospectus/SAI document route](https://www.nb.com/handlers/documents.ashx?id=47663e8f-0b22-4bda-b97c-4b535e979cab&name=Statement+of+Additional+Information+NBDS+NBCC+NBCT) | Adviser/portfolio-management and active-fund documentation route | Prospectus dated `2025-12-18`, supplemented `2026-01-26`; document route accessed `2026-07-24` |

### NBJP Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, unsupported-type reason, no accidental performance-page creation, source URLs, ledger update, queue pointer, and no region/index navigation update for an unsupported ETF.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ASHR Sequential Queue Record

- Input row: `64/125`; input ticker: `ASHR`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:ASHR`; DWS official prospectus identifies the Xtrackers Harvest CSI 300 China A-Shares ETF on NYSE Arca with ticker `ASHR`. No provider slug or guessed exchange is used.
- Type gate: the prospectus describes a passive/indexing investment approach, a policy of investing at least `80%` in A-shares or qualifying exposure instruments, and tracking of the `CSI 300 Index`. The reviewed strategy is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock ETF.
- Mandatory 10-year coverage audit: the official DWS Q2 2026 factsheet reports ETF-at-NAV 10-year NAV Total Return CAGR `5.84%` for `2016-06-30` to `2026-06-30`, actual elapsed years `10.00`, as of `2026-06-30`. Raw start/end NAV TR values and issuer cumulative rolling return are not disclosed in the reviewed capture. A normalized illustration from `100.00` to approximately `176.40` is derived only from the disclosed CAGR and is labeled as such; it is not a proxy.
- Annual NAV Total Return: the official DWS prospectus discloses calendar rows through `2024`: 2016 `-15.06%`, 2017 `31.81%`, 2018 `-28.05%`, 2019 `35.57%`, 2020 `37.42%`, 2021 `-2.17%`, 2022 `-26.98%`, 2023 `-13.07%`, and 2024 `12.55%`. The reviewed official materials do not disclose an ASHR 2025 calendar NAV row, current NAV TR YTD, or CSI 300 annual TR rows; these are recorded as `not disclosed` rather than backfilled.
- Calculations from disclosed rows: 2016-2024 ASHR NAV TR compounds to `+4.89%` / CAGR `+0.53%` over 9 complete years; common 2021-2024 ASHR compounds to `-30.11%` / CAGR `-8.57%`, versus cached S&P 500 TR `+66.41%` / CAGR `+13.58%`, a difference of approximately `-22.15 pp` CAGR. ASHR has `4` positive and `5` negative years in 2016-2024; best year `2020 +37.42%`; worst year `2018 -28.05%`.
- Current-YTD check: `ไม่พบข้อมูลที่ยืนยันได้` / `not disclosed` in the reviewed official Q2 2026 factsheet/product capture; no short window is labeled as 10-year performance.

### ASHR Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ASHR` | [DWS Xtrackers Q2 2026 factsheet](https://etf.dws.com/download/asset/e73aaa93-92c6-4a51-9233-38ccb329e09b) | Official NAV Total Return rolling-period table, inception, index, holdings, assets, expenses and current disclosure check | Q2 `2026-06-30`; 10-year NAV TR CAGR `5.84%` |
| `NYSE Arca:ASHR` | [DWS Xtrackers Harvest CSI 300 China A-Shares ETF prospectus](https://etf.dws.com/en-us/AssetDownload/Index/ce51b065-fc18-496f-9b88-8996a37d16b3/CHINA-1-Prospectus.pdf) | Canonical exchange/ticker, passive/indexing strategy, 80% policy and official calendar-year NAV Total Return rows | Prospectus reviewed `2026-07-24`; calendar rows through `2024-12-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common benchmark identity; cached USD Total Return convention for complete calendar years | Cached rows `2016-2025`, as of `2025-12-31`; no new search used |

### ASHR Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, normalized-endpoint disclosure, annual-row completeness, S&P 500 basis/window, current-YTD as-of date, primary China region assignment, canonical filename, geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## ASEA Sequential Queue Record

- Input row: `65/125`; input ticker: `ASEA`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:ASEA`; Global X's official product page and March 2026 summary prospectus identify the Global X FTSE Southeast Asia ETF on NYSE Arca with ticker `ASEA`. No provider slug or guessed exchange is used.
- Type gate: the official prospectus describes an indexing approach, an at-least-80% policy in FTSE/ASEAN 40 Index securities or related ADR/GDR exposure, and equity exposure to Singapore, Malaysia, Indonesia, Thailand and the Philippines. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock ETF.
- Mandatory 10-year coverage audit: Global X's official product page reports Fund NAV annualized total return `7.12%` for `10 Years` as of `2026-06-30`, so the elapsed window is `2016-06-30` to `2026-06-30`, actual years `10.00`. The page does not disclose raw start/end NAV TR values or a cumulative rolling figure. A normalized illustration from `100.00` to approximately `198.93` is derived only from the disclosed CAGR and is labeled as such; it is not a proxy.
- Annual NAV Total Return: the March 2026 summary prospectus bar chart discloses calendar rows: 2016 `8.39%`, 2017 `31.89%`, 2018 `-6.35%`, 2019 `7.78%`, 2020 `-8.05%`, 2021 `5.26%`, 2022 `5.16%`, 2023 `4.43%`, 2024 `11.42%`, and 2025 `18.46%`. Annual FTSE/ASEAN 40 Index rows are not disclosed in the reviewed official capture and remain `not disclosed`.
- Calculations from disclosed rows: complete-calendar `2016-2025` ASEA NAV TR compounds to `+102.43%` / CAGR `+7.31%`; common `2021-2025` compounds to `+52.57%` / CAGR `+8.82%`, versus cached S&P 500 TR `+96.17%` / CAGR `+14.43%`, a difference of approximately `-5.61 pp` CAGR. Over `2016-2025`, ASEA has `8` positive and `2` negative years; best year `2017 +31.89%`; worst year `2020 -8.05%`.
- Current-YTD check: the latest official Global X factsheet in the reviewed capture reports NAV TR YTD `8.67%` as of `2026-05-31`. The newer product-page performance table is as of `2026-06-30` but does not expose a separate YTD field, so the page labels the YTD as-of date explicitly and does not extrapolate it to 2026-07-24.

### ASEA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ASEA` | [Global X ASEA product page](https://www.globalxetfs.com/funds/asea) | Official exchange/ticker, index objective, inception, expenses, current holdings and rolling NAV Total Return table | Page accessed `2026-07-24`; current facts as of `2026-07-22`; rolling performance as of `2026-06-30`; 10-year NAV TR CAGR `7.12%` |
| `NYSE Arca:ASEA` | [Global X ASEA factsheet](https://assets.globalxetfs.com/funds/documents/asea/Fact-Sheet_ASEA.pdf) | Official NAV TR YTD and cross-check of index, exchange, inception, expenses and region exposure | Factsheet as of `2026-05-31`; NAV TR YTD `8.67%`, 10-year NAV TR CAGR `7.67%` |
| `NYSE Arca:ASEA` | [Global X ASEA 2026 summary prospectus](https://assets.globalxetfs.com/funds/documents/asea/prospectus-regulatory/Summary-Prospectus_ASEA.pdf) | Passive/indexing classification, 80% policy and annual total-return bar-chart rows | Prospectus dated `2026-03-01`; annual rows through `2025-12-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common benchmark identity; cached USD Total Return convention for complete calendar years | Cached rows `2016-2025`, as of `2025-12-31`; no new search used |

### ASEA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, normalized-endpoint disclosure, annual-row completeness, S&P 500 basis/window, current-YTD as-of date separation, primary Southeast Asia region assignment, canonical filename, geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## KCAI Sequential Queue Record

- Input row: `66/125`; input ticker: `KCAI`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:KCAI`; KraneShares' official prospectus, factsheet and March 2026 annual shareholder report identify the principal listing exchange as NYSE Arca. The current product page displays `Primary Exchange NYSE`; this is recorded as an issuer-source conflict. The prospectus/factsheet/annual-report listing is retained because it is the repeated principal-listing disclosure in the official fund documents. No provider slug or guessed exchange is used.
- Type gate: the official prospectus describes a passive index strategy, an at-least-80% policy in Qi China Alpha Index securities or economically similar instruments, long-only China A-share selection from the CSI 300 universe, and monthly rebalancing. It also states the fund is not actively managed. The fund is not a bond, commodity, currency trust, multi-asset, leveraged, inverse, option-income, derivative-heavy, or single-stock ETF.
- Mandatory 10-year coverage audit: official inception is `2024-08-27`, so `10-year NAV TR unavailable`. Official KraneShares performance as of `2026-06-30` reports since-inception Fund NAV Total Return cumulative `76.27%` and annualized `36.06%` for approximately `1.84` elapsed years (`2024-08-27` to `2026-06-30`). Raw NAV start/end values are not disclosed. The performance page uses `100.00` as a normalized start and `176.27` as the endpoint derived from disclosed cumulative return; this is not a proxy.
- Available-period performance: official NAV TR YTD `4.27%` as of `2026-06-30`; official 1-year NAV TR `42.84%` as of `2026-06-30`; official since-inception NAV TR annualized `36.06%`. No short period is labeled as 10-year performance.
- Annual NAV Total Return: official product page, factsheet and reviewed annual report do not disclose complete calendar-year Fund NAV rows for 2024 or 2025. The page therefore records `2024` as `not disclosed (partial inception year)`, `2025` as `not disclosed`, and `2026 YTD` as `4.27%`. S&P 500 rows are shown only as a common reference and are not treated as a same-window ETF proxy.
- Window comparison: since-inception KCAI NAV TR cumulative `76.27%` / annualized `36.06%` cannot be compared to complete calendar-year S&P 500 CAGR without introducing a mismatched start-date proxy. The annual table keeps S&P rows separate and marks unavailable KCAI calendar rows explicitly.

### KCAI Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KCAI` | [KraneShares KCAI product page](https://kraneshares.com/etf/kcai/) | Current fund identity, strategy, current performance table, YTD, inception, expense and current holdings; also records the conflicting current `Primary Exchange NYSE` field | Page accessed `2026-07-24`; current facts as of `2026-07-20/22`; performance as of `2026-06-30` |
| `NYSE Arca:KCAI` | [KraneShares KCAI factsheet](https://kraneshares.com/resources/factsheet/kcai_factsheet.pdf) | Official principal exchange, inception, index, expenses, holdings and since-inception/YTD NAV TR | Factsheet as of `2026-06-30`; cumulative `76.27%`, annualized `36.06%`, YTD `4.27%` |
| `NYSE Arca:KCAI` | [KraneShares KCAI 2026 annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_kcai_annual.TSR.report.pdf) | Principal listing exchange and official NAV/market-price/index total-return cross-check | Report for period ended `2026-03-31`; since-inception NAV annualized `42.01%` at that earlier as-of date |
| `NYSE Arca:KCAI` | [KraneShares KCAI statutory prospectus](https://kraneshares.com/resources/compliance/2024_08_28_kcai_statutory.prospectus.pdf) | Passive/index strategy, 80% policy, index construction, inception-period scope and principal listing exchange | Prospectus dated `2024-08-26`; fund commenced operations `2024-08-27` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common benchmark identity; cached USD Total Return convention for complete calendar years | Cached rows `2024-2025`, as of `2025-12-31`; not used as a proxy for KCAI's since-inception period |

### KCAI Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange conflict resolution, fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, available-period date window, normalized-endpoint disclosure, annual-row gap, S&P 500 basis/window, current-YTD as-of date, primary China region assignment, canonical filename, geography tag, breadcrumbs, stale-value replacement, old filename/link replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Exchange-source conflict and the 10-year history gap are disclosed here as required.

## EWS Sequential Queue Record

- Input row: `67/125`; input ticker: `EWS`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:EWS`; iShares' official product page identifies EWS on NYSE Arca, fund inception `1996-03-12`, asset class Equity, and benchmark `MSCI Singapore 25/50 Index`. No provider slug or guessed exchange is used.
- Type gate: the official product page states that EWS seeks to track an index composed of Singaporean equities. It is a passive/index-tracking single-country equity ETF, not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock ETF.
- Mandatory 10-year coverage audit: iShares reports NAV Total Return cumulative `112.54%` and average annual `7.83%` for the 10-year period ended `2026-06-30`, corresponding to `2016-06-30` to `2026-06-30`, actual years `10.00`. Raw start/end NAV TR values are not disclosed. Normalized TR is `100.00` to the official cumulative endpoint `212.54`; no proxy is used.
- Annual NAV Total Return: iShares discloses Fund NAV and benchmark rows for complete calendar years `2021-2025`: Fund `5.22%`, `-9.15%`, `5.27%`, `22.53%`, `31.56%`; benchmark `5.65%`, `-8.76%`, `6.10%`, `23.15%`, `32.17%`. Fund rows for `2016-2020` are not disclosed in the reviewed current official capture. The benchmark changed to MSCI Singapore 25/50 Index (Net) on `2016-12-01`; benchmark rows remain separate from the NAV TR metric.
- Calculations: EWS 2021-2025 NAV rows compound to `62.22%` / CAGR `10.16%`; issuer benchmark rows compound to `67.32%` / CAGR `10.83%`; cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%`. EWS trails S&P by approximately `4.27 pp` CAGR in the common 2021-2025 window. Positive / negative EWS years are `4 / 1`; best `2025 +31.56%`; worst `2022 -9.15%`.
- Current-YTD check: official iShares NAV Total Return YTD is `16.50%` as of `2026-07-21`; the current month-end performance table is as of `2026-06-30` and reports calendar/rolling figures separately.

### EWS Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:EWS` | [iShares EWS product page](https://www.ishares.com/us/products/239678/ishares-msci-singapore-capped-etf) | Canonical exchange/fund identity, index, inception, expense ratio, current NAV/YTD, rolling 10-year and annual performance tables | Page accessed `2026-07-24`; current NAV/YTD through `2026-07-21`; month-end performance through `2026-06-30` |
| `NYSE Arca:EWS` | [iShares EWS factsheet](https://www.ishares.com/us/literature/fact-sheet/ews-ishares-msci-singapore-etf-fund-fact-sheet-en-us.pdf) | Official NAV/index calendar rows 2021-2025, annualized performance and benchmark-change note | Factsheet accessed `2026-07-24`; data through `2025-12-31` / current quarter-end fields |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common benchmark identity; cached USD Total Return rows for complete calendar years | Cached rows `2016-2025`, as of `2025-12-31`; no new search used |

### EWS Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, normalized-endpoint disclosure, annual-row completeness, S&P 500 basis/window, current-YTD as-of date separation, benchmark/index-change note, primary Singapore region assignment, canonical filename, geography tag, breadcrumbs, stale-value replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## BBAX Sequential Queue Record

- Input row: `68/125`; input ticker: `BBAX`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `Cboe BZX:BBAX`; the current Cboe issuer listing identifies JPMorgan BetaBuilders Developed Asia Pacific ex-Japan ETF as listed on Cboe, and the official SEC prospectus identifies the listing exchange as `Cboe BZX Exchange, Inc.`. The earlier compact capture used `NYSE Arca:BBAX`; that stale exchange label is corrected here and the old duplicate performance path is removed. No provider slug or guessed exchange is used.
- Type gate: JPMorgan's official June 2026 factsheet describes an indexed approach and a `passive` investment approach that attempts to replicate the Morningstar Developed Asia Pacific ex-Japan Target Market Exposure Index. The exposure is equity in Australia, Hong Kong, New Zealand and Singapore. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock ETF.
- Mandatory 10-year coverage audit: official class launch / fund performance inception is `2018-08-07`; the official factsheet ends at `2026-06-30`, only `2,884 / 365.25 = 7.90` elapsed years later. Therefore `10-year NAV TR unavailable`; no shorter period is relabeled as 10-year.
- Available-period NAV Total Return: JPMorgan's official growth-of-$10,000 chart shows an ending value of `$16,448` from the `2018-08-07` launch to `2026-06-30`. The performance page normalizes this to start `100.00` and end `164.48`, giving available-period cumulative return `64.48%` and official launch average annual return `6.50%`; raw NAV TR endpoints are not disclosed. The normalized endpoint is derived from the official chart, not a proxy.
- Official current performance: NAV Total Return YTD `8.20%` as of `2026-06-30`; 3-month `2.02%`, 1-year `14.20%`, 3-year annualized `12.04%`, 5-year annualized `5.22%`, and launch annualized `6.50%`. NAV total return assumes reinvested distributions and includes management fees and operating expenses according to the fact sheet disclosure; market-price returns remain separate.
- Annual NAV Total Return: the official factsheet discloses F1 NAV rows for 2019 `18.44%`, 2020 `8.20%`, 2021 `5.36%`, 2022 `-4.45%`, 2023 `5.60%`, 2024 `1.69%`, and 2025 `20.73%`. These rows compound to `67.26%` / CAGR `7.62%`; the common 2021-2025 rows compound to `30.52%` / CAGR `5.47%`. S&P 500 TR uses the cached USD dividend-reinvested convention: 2021-2025 cumulative `96.17%` / CAGR `14.43%`, a BBAX gap of approximately `-8.96 pp` CAGR.
- S&P 500 comparison: the annual table uses cached complete-calendar S&P 500 Total Return rows for 2019-2025, as of `2025-12-31`; the 2019-2025 S&P rows compound to `205.41%` / CAGR `17.29%`. The benchmark is a common reference, not BBAX's issuer benchmark.
- Risk/gap notes: the official factsheet reports gross and net annual expenses `0.190%`, fund assets `$6.25 B`, and 97 holdings as of `2026-06-30`. It describes Asia-Pacific liquidity, currency and volatility risks. Daily NAV TR observations needed for fund-level drawdown/recovery are `not disclosed` in the reviewed official capture.

### BBAX Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Cboe BZX:BBAX` | [JPMorgan BBAX fact sheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBAX.PDF) | Official fund identity, passive/index approach, Morningstar index, inception, NAV TR, expenses, holdings and risk disclosures | Fact sheet dated `2026-06-30`; NAV TR YTD `8.20%`; launch annualized `6.50%`; growth-of-$10,000 ending value `$16,448` |
| `Cboe BZX:BBAX` | [Cboe JPMorgan issuer listing](https://www.cboe.com/us/equities/listings/listed_products/issuer_detail/JMAM/) | Current exchange/ticker confirmation | Cboe listing page accessed `2026-07-24`; BBAX listed/transfer date `2018-08-08` |
| `Cboe BZX:BBAX` | [SEC JPMorgan ETF prospectus](https://www.sec.gov/Archives/edgar/data/1485894/000119312523046804/d439474d485bpos.htm) | Official listing-exchange confirmation | Prospectus dated `2023-03-01`; listing exchange `Cboe BZX Exchange, Inc.` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common benchmark identity; cached USD Total Return convention for complete calendar years | Cached rows `2016-2025`, as of `2025-12-31`; no new search used |

### BBAX Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, normalized-endpoint disclosure, annual-row completeness, S&P 500 basis/window, current-YTD as-of date, primary Asia-Pacific region assignment, canonical filename, geography tag, breadcrumbs, stale-value replacement, old filename/link replacement, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. The earlier `NYSE Arca` label and `current NAV and 10Y not disclosed` compact capture were corrected from the current official Cboe/JPMorgan/SEC evidence; reviewer-availability fallback is disclosed here as required.

## PCCE Sequential Queue Record

- Input row: `69/125`; input ticker: `PCCE`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:PCCE`; Polen's official 2025 active-ETF announcement places PCCE in the existing NYSE Arca active ETF lineup, and the official SEC 2026 shareholder-report data identifies PCCE's security exchange as `NYSEArca`. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. The SEC April 30, 2026 summary prospectus describes PCCE as a non-diversified, `actively-managed` ETF seeking long-term capital growth through a portfolio of Chinese-company equity securities selected in the sub-advisor's opinion. Polen's official materials also describe its active ETF framework. It is not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### PCCE Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:PCCE` | [Polen Capital active ETF lineup announcement](https://www.polencapital.com/perspectives/polen-expands-active-etf-lineup-two-credit-etfs) | Official issuer exchange context and active ETF classification | Announcement dated `2025-03-24`; PCCE listed in the existing NYSE Arca active ETF lineup |
| `NYSE Arca:PCCE` | [SEC 2026 shareholder-report data](https://www.sec.gov/Archives/edgar/data/1020425/000119312526100256/R2.htm) | Official ticker/exchange record and fund report context | Report data filed `2026`; `Security Exchange Name: NYSEArca`; 2025 NAV return `21.83%` is not used because the fund fails the type gate |
| `NYSE Arca:PCCE` | [SEC April 30, 2026 summary prospectus](https://www.sec.gov/Archives/edgar/data/1020425/000119312526197037/d119372d497k.htm) | Official active/non-diversified strategy classification | Prospectus dated `2026-04-30`; actively managed China equity ETF |

### PCCE Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because PCCE failed the passive/index-tracking equity gate, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## MJSC Sequential Queue Record

- Input row: `70/125`; input ticker: `MJSC`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:MJSC`; MUFG's official product page identifies the primary exchange as `NYSE ARCA`, ticker `MJSC`, and the issuer launch announcement identifies the same listing. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. The official product page names it the `MUFG Japan Small Cap Active ETF`, describes a research-intensive strategy seeking companies with pioneering business models and long-term growth potential at reasonable valuations, and explicitly states that it is an actively managed ETF. The issuer launch notice further describes an actively managed all-Japan equity strategy using thematic analysis and portfolio-manager selection. It is not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### MJSC Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:MJSC` | [MUFG MJSC official product page](https://www.mufgetfs.com/mjsc) | Official primary exchange/ticker, active classification, strategy, inception, current fund details and performance gap | Page accessed `2026-07-24`; fund details as of `2026-07-16`; inception `2025-09-16` |
| `NYSE Arca:MJSC` | [MUFG/Clearbrook launch announcement](https://www.mufgetfs.com/posts/mufg-clearbrook-launch-first-etf-mjsc-nyse-arca) | Official issuer exchange and active-strategy confirmation | Announcement dated `2025-09-17`; active all-Japan equity strategy |

### MJSC Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because MJSC failed the passive/index-tracking equity gate, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## INDE Sequential Queue Record

- Input row: `71/125`; input ticker: `INDE`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:INDE`; Matthews' official factsheet identifies the primary exchange as `NYSE Arca`, ticker `INDE`. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. Matthews' official page describes INDE as an unconstrained all-cap strategy using fundamental bottom-up research, seeking companies with sustainable competitive edge and pricing power; the official active-ETF materials explicitly position the ETF as active and the strategy invests at least 80% in Indian securities. It is not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### INDE Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:INDE` | [Matthews India Active ETF official page](https://us.matthewsasia.com/funds/etfs/india-active-etf/) | Official fund identity, active strategy, inception, current performance and portfolio characteristics | Page accessed `2026-07-24`; performance/current data through `2026-06-30` / `2026-07-17`; active share `58.9` as of `2026-06-30` |
| `NYSE Arca:INDE` | [Matthews INDE factsheet](https://www.matthewsasia.com/siteassets/resources/fund-documents/factsheets/etfs/fact_sheet_inde.pdf) | Official primary exchange, inception, 80% India strategy, expense and benchmark metadata | Factsheet dated `2026-03-31`; primary exchange `NYSE Arca`; gross expense ratio `0.79%`; benchmark change to MSCI India on `2024-04-29` |
| `NYSE Arca:INDE` | [Matthews active ETF overview](https://www.matthewsasia.com/active-etfs/explore/) | Official active ETF classification and active-vs-indexing distinction | Page accessed `2026-07-24`; active ETF lineup |

### INDE Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because INDE failed the passive/index-tracking equity gate, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## KBA Sequential Queue Record

- Input row: `72/125`; input ticker: `KBA`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:KBA`; the official 2026 summary prospectus and annual shareholder report identify the principal listing exchange as `NYSE Arca` and ticker `KBA`. The current product page displays `Primary Exchange NYSE`; this conflict is retained in the record and resolved in favor of the formal fund documents. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking equity ETF. The official prospectus states that KBA seeks to track the price and yield performance of the `MSCI China A 50 Connect Index` and normally invests at least 80% in underlying-index securities or economically similar instruments. The index covers large-cap Shanghai/Shenzhen A-shares accessible through Stock Connect. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy or single-stock fund.
- Mandatory coverage audit: official KraneShares performance history reports NAV average annualized return `6.90%` for the 10-year period ended `2026-06-30`; official inception is `2014-03-04`, so the window covers `10.00` elapsed years. Normalized TR is `100.00` to approximately `194.88`, calculated from the official CAGR because raw endpoints and cumulative rolling NAV TR are not disclosed.
- Official calendar observations: the current reviewed summary prospectus discloses KBA NAV TR rows for `2015-2024`; the page uses `2016-2024` for the complete disclosed comparison. The 2025 calendar NAV row is `not disclosed`. The `2016-2024` rows compound to `6.41%` / CAGR `0.69%`; the common disclosed `2021-2024` rows compound to `128.27%` / CAGR `22.92%`.
- S&P 500 comparison: cached USD Total Return rows are used for complete calendar years `2016-2025`; the common `2021-2024` S&P window compounds to `66.41%` / CAGR `13.58%`. No 2026 S&P value is manufactured.
- Official current observation: KBA NAV TR YTD is `11.37%` as of `2026-06-30`; gross expense ratio is `0.79%`, net expense after fee waiver is `0.56%` through `2026-08-01`. The official index history changed from earlier MSCI China A variants to MSCI China A 50 Connect on `2022-01-05`; this is disclosed on the performance page.

### KBA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KBA` | [KraneShares KBA official product/performance page](https://kraneshares.com/etf/kba/) | Fund identity, current product-page exchange field, index, inception, expense ratio, NAV TR performance, current NAV/YTD and distribution history | Page accessed `2026-07-24`; current NAV/product data through `2026-07-22`; performance summary through `2026-06-30` |
| `NYSE Arca:KBA` | [KraneShares KBA summary prospectus](https://kraneshares.com/resources/compliance/2026_02_20_kba_summary.prospectus.pdf) | Formal principal listing exchange, passive/index-tracking objective, 80% policy, expenses, 2015-2024 calendar return chart, index-history footnote and reinvestment basis | Prospectus package dated `2025-08-01` with supplement filed `2026-02-20`; calendar return chart through `2024-12-31` |
| `NYSE Arca:KBA` | [KraneShares KBA annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_kba_annual.TSR.report.pdf) | Independent official listing cross-check and separate 10-year return cross-check | Report period ended `2026-03-31`; separate 10-year NAV return `4.68%` and $10,000 ending value `$15,800`; not mixed with the current `2026-06-30` series |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### KBA Raw Observations And Calculations

| Year | KBA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -19.37% | 11.96% |
| 2017 | 28.64% | 21.83% |
| 2018 | -26.25% | -4.38% |
| 2019 | -26.49% | 31.49% |
| 2020 | -17.10% | 18.40% |
| 2021 | 34.50% | 28.71% |
| 2022 | 2.70% | -18.11% |
| 2023 | 16.06% | 26.29% |
| 2024 | 42.39% | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | 11.37% | not comparable; current year not cached |

- Official rolling 10-year NAV TR CAGR is `6.90%` for `2016-06-30` to `2026-06-30`; normalized TR is `100.00` to approximately `194.88`, actual years `10.00`.
- Complete disclosed calendar rows `2016-2024` compound to `6.41%` / CAGR `0.69%`; S&P 500 TR over the same nine-year window compounds to `237.91%` / CAGR `14.49%`; KBA trails by `13.80 pp` CAGR.
- Common disclosed rows `2021-2024` compound to `128.27%` / CAGR `22.92%`; S&P 500 TR compounds to `66.41%` / CAGR `13.58%`; KBA leads by `9.34 pp` CAGR. This is not labeled a five-year `2021-2025` result because KBA's 2025 row is not disclosed.

### KBA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange conflict resolution, fund/index identity, passive-equity classification, inception and 10-year eligibility audit, official NAV TR/reinvestment/expense basis, normalized-endpoint disclosure, annual-row completeness, S&P 500 basis/window, current-YTD as-of date, index-history caveat, stale old filename/link replacement, China region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required.

## JCHI Sequential Queue Record

- Input row: `73/125`; input ticker: `JCHI`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:JCHI`; the official SEC shareholder-report data identify the ticker as `JCHI` on `NYSE Arca`. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. JPMorgan's official factsheet names the fund `JPMorgan Active China ETF` and describes an investment approach primarily driven by bottom-up stock selection; the official prospectus describes the sub-adviser seeking to add value through security-selection decisions. It is an actively managed China equity ETF, not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### JCHI Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:JCHI` | [JPMorgan JCHI factsheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JCHI.PDF) | Official fund identity, active approach, inception, expenses and current performance context | Factsheet dated `2026-06-30`; class launch `2023-03-15`; gross expense `0.650%`; net expense `0.150%`; current performance through `2026-06-30` |
| `NYSE Arca:JCHI` | [SEC JCHI summary prospectus](https://www.sec.gov/Archives/edgar/data/1485894/000119312524042757/d669354d497k.htm) | Official active stock-selection process, China equity policy and exchange/trading-risk context | Prospectus dated `2024-03-01`; at least 80% China-tied equity/equity-related instruments; bottom-up security selection |
| `NYSE Arca:JCHI` | [SEC JCHI shareholder-report data](https://www.sec.gov/Archives/edgar/data/1485894/000119312525336832/d43117dncsr.htm) | Official ticker and principal listing exchange cross-check | Report data filed `2025`; `JCHI - NYSE Arca, Inc.` |

### JCHI Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because JCHI failed the passive/index-tracking equity gate, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## MCH Sequential Queue Record

- Input row: `74/125`; input ticker: `MCH`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:MCH`; Matthews' official fund page identifies the primary exchange as `NYSE Arca` and ticker `MCH`. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. Matthews names the fund `Matthews China Active ETF` and describes a high-conviction, all-cap fundamental GARP approach driven by on-the-ground proprietary research; the strategy invests at least 80% in China company stocks selected using fundamental characteristics. It is actively managed, not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### MCH Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:MCH` | [Matthews China Active ETF official page](https://www.matthewsasia.com/funds/etfs/china-active-etf/) | Official fund identity, primary exchange, active strategy, inception, benchmark and current performance context | Page accessed `2026-07-24`; fund facts/assets through `2026-07-20`; performance through `2026-06-30`; inception `2022-07-13` |
| `NYSE Arca:MCH` | [Matthews MCH factsheet](https://us.matthewsasia.com/siteassets/resources/fund-documents/factsheets/etfs/fact_sheet_mch.pdf) | Official active-equity strategy and fund facts cross-check | Factsheet accessed `2026-07-24`; gross/net expense and performance disclosures as dated in the factsheet |
| `NYSE Arca:MCH` | [Matthews ETF prospectus](https://www.matthewsasia.com/siteassets/resources/fund-documents/prospectus/etf-prospectus.pdf) | Official active ETF lineup and exchange context | Prospectus dated `2026-04-30`; MCH listed on `NYSE Arca` |

### MCH Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange/fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because MCH failed the passive/index-tracking equity gate, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## CGRO Sequential Queue Record

- Input row: `75/125`; input ticker: `CGRO`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:CGRO`; CoreValues' current product page displays `Exchange NYSE`, while the official February 2026 summary prospectus identifies the trading symbol `CGRO` as listed on `NYSE Arca, Inc.`. The formal prospectus is used for the canonical key and the conflict is disclosed. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. The official summary prospectus states that CGRO is an `actively managed exchange-traded fund`; its portfolio is built through the sub-adviser's core-values approach, top-down macro research, on-ground due diligence and bottom-up fundamental company analysis. It is not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### CGRO Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CGRO` | [CoreValues CGRO official product page](https://www.cvafunds.com/cgro/) | Official fund identity, current website exchange field, inception, holdings and current fund details | Page accessed `2026-07-24`; profile/market data through `2026-07-22`; current website exchange field `NYSE`; inception `2023-10-16` |
| `NYSE Arca:CGRO` | [CoreValues CGRO February 2026 summary prospectus](https://www.cvafunds.com/wp-content/uploads/fund-docs/CGRO/CGRO_SummaryProspectus.pdf) | Formal listing exchange, explicit active classification, investment process, Greater China policy and performance context | Prospectus dated `2026-02-02`; incorporated prospectus dated `2026-02-01`; listed on `NYSE Arca`; actively managed; at least 80% Greater China equity policy |
| `NYSE Arca:CGRO` | [CGRO 2024 annual shareholder report](https://www.sec.gov/Archives/edgar/data/1924868/000183988224044108/corevalues-ncsr_093024.htm) | SEC listing cross-check and fund-history context | Report period ended `2024-09-30`; identifies CGRO as listed on `NYSE Arca` |

### CGRO Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange conflict resolution, fund identity, passive-versus-active classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because CGRO failed the passive/index-tracking equity gate, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## KBUF Sequential Queue Record

- Input row: `76/125`; input ticker: `KBUF`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:KBUF`; the official summary prospectus and factsheet identify KBUF as listed on `NYSE Arca`, while the current product page displays `Primary Exchange NYSE`; the formal fund documents are used for the canonical key and the conflict is disclosed. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. KraneShares describes KBUF as a defined-outcome ETF that uses the underlying KWEB ETF plus `FLEX options` to seek a predetermined upside cap and a `90% downside buffer` over a specified outcome period. It is derivative-heavy and actively managed around an outcome structure, not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### KBUF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KBUF` | [KraneShares KBUF official product/performance page](https://kraneshares.com/etf/kbuf/) | Official defined-outcome strategy, FLEX-option structure, cap/buffer, current product-page exchange field and outcome-period data | Page accessed `2026-07-24`; fund/outcome data through `2026-07-21`; current outcome period `2025-01-27` to `2027-01-15`; product page exchange field `NYSE` |
| `NYSE Arca:KBUF` | [KraneShares KBUF factsheet](https://kraneshares.com/resources/factsheet/kbuf_factsheet.pdf) | Official primary exchange and defined-outcome strategy cross-check | Factsheet dated `2026-01-30`; primary exchange `NYSE Arca, Inc.`; 90% buffer / 40.01% starting cap |
| `NYSE Arca:KBUF` | [SEC KBUF summary prospectus](https://www.sec.gov/Archives/edgar/data/1547576/000182912625005548/kraneshares_497k.htm) | Official principal listing exchange and explicit options/defined-outcome classification | Prospectus dated `2025-08-01`; principal listing `NYSE Arca`; uses options including FLEX options |

### KBUF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange conflict resolution, fund identity, passive-versus-derivative-heavy classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because KBUF failed the passive/index-tracking equity gate as derivative-heavy, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## KPRO Sequential Queue Record

- Input row: `77/125`; input ticker: `KPRO`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:KPRO`; the official summary prospectus and annual shareholder report identify KPRO as listed on `NYSE Arca`, while the current product page displays `Primary Exchange NYSE`; the formal fund documents are used for the canonical key and the conflict is disclosed. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. KraneShares describes KPRO as a defined-outcome ETF using the underlying KWEB ETF and `FLEX options` to seek a predetermined `20.01%` upside cap and a `100% downside buffer` over a specified outcome period. It is derivative-heavy and actively managed around an outcome structure, not a passive/index-tracking equity ETF.
- Per the type gate, no 10-year historical performance calculation, annual NAV TR table, performance page, region row, index row, or S&P 500 comparison was created. Status is terminal under the requested ETF v1 scope.

### KPRO Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KPRO` | [KraneShares KPRO official product/performance page](https://kraneshares.com/etf/kpro/) | Official defined-outcome strategy, FLEX-option structure, cap/buffer, current product-page exchange field and outcome-period data | Page accessed `2026-07-24`; fund/outcome/holdings data through `2026-07-20`; current outcome period `2025-01-27` to `2027-01-15`; product page exchange field `NYSE` |
| `NYSE Arca:KPRO` | [KraneShares KPRO summary prospectus](https://kraneshares.com/resources/compliance/2026_06_25_kpro_summary.prospectus.pdf) | Official principal listing exchange and explicit options/defined-outcome classification | Prospectus dated `2025-08-01`; principal listing `NYSE Arca`; uses options including FLEX options |
| `NYSE Arca:KPRO` | [KraneShares KPRO annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_kpro_annual.TSR.report.pdf) | Official listing cross-check and outcome-structure fund-history context | Report period ended `2026-03-31`; principal listing `NYSE Arca`; fund NAV return `6.76%` for the report period is not used because the fund fails the type gate |

### KPRO Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange conflict resolution, fund identity, passive-versus-derivative-heavy classification, terminal-status selection, source URL, filename decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical or high-severity finding remained. Because KPRO failed the passive/index-tracking equity gate as derivative-heavy, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed here as required.

## KSTR Sequential Queue Record

- Input row: `78/125`; input ticker: `KSTR`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:KSTR`; official product page, factsheet and annual shareholder report identify the NYSE Arca listing. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking equity ETF. KraneShares says KSTR seeks to track the SSE Science and Technology Innovation Board 50 Index, representing 50 large STAR Market companies by market capitalization and liquidity. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy or single-stock fund. Derivatives may be permitted for implementation or risk management but are not the fund's defining structure.
- Mandatory coverage audit: official inception `2021-01-26`; as of `2026-06-30` only approximately `5.43` years, so `10-year NAV TR unavailable`. Official since-inception NAV TR cumulative `27.40%` / annualized `4.56%`; normalized TR `100.00` to `127.40`; raw endpoints not disclosed.
- Official calendar observations: current official page/factsheet disclose rolling, YTD and since-inception performance but no complete calendar-year NAV rows in the reviewed capture; annual table leaves 2021-2025 `not disclosed`; current YTD is `71.70%` as of 2026-06-30.
- S&P 500 comparison: cached USD Total Return rows are used for 2021-2025 common reference only; no 2026 S&P value is used.
- Official current observation: NAV TR YTD `71.70%` as of `2026-06-30`; 1-year `131.80%`; 3-year `29.49%`; 5-year `3.10%`; since inception `4.56%`; gross/net expense `0.89%/0.65%`; 53 holdings and Information Technology sector `92.90%` in the June factsheet. The annual report's separate March 31 2026 trailing values are retained as a cross-check and not mixed into the current June series.

### KSTR Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KSTR` | [KraneShares KSTR official product/performance page](https://kraneshares.com/etf/kstr/) | identity, index, exchange, inception, fees, current NAV/YTD and rolling/available-period NAV TR | Page accessed `2026-07-24`; product data through `2026-07-22`; performance summary through `2026-06-30` |
| `NYSE Arca:KSTR` | [KraneShares KSTR factsheet](https://kraneshares.com/resources/factsheet/kstr_factsheet.pdf) | passive/index-tracking classification, official NAV TR basis, since-inception/rolling performance, fees, holdings/sector risk | Factsheet dated `2026-06-30`; performance through `2026-06-30`; 53 holdings |
| `NYSE Arca:KSTR` | [KraneShares KSTR annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_kstr_annual.TSR.report.pdf) | official listing cross-check and separate fiscal trailing performance cross-check | Report period ended `2026-03-31`; KSTR 12-month NAV return `28.85%`; not mixed with current June series |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### KSTR Raw Observations And Calculations

| Period | KSTR NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | not disclosed (partial inception year) | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | 71.70% | not comparable; current year not cached |

- `10-year NAV TR unavailable`: official inception `2021-01-26` is under 10 years as of `2026-06-30`.
- Available-period official NAV TR: cumulative `27.40%`; issuer annualized return `4.56%`; actual elapsed period approximately `5.43` years; normalized start/end `100.00`/`127.40`; raw endpoints not disclosed.
- Annual NAV rows `2021-2025` are not disclosed in the reviewed official capture; no annual CAGR or best/worst year ranking is manufactured.
- Current NAV TR YTD `71.70%` as of `2026-06-30`; S&P current year not used.

### KSTR Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period normalized endpoint, annual-row gaps, S&P cache, current-YTD, region/index links, stale-value replacement, filename/tags/breadcrumbs/link targets.
- Local fallback verdict: `PASS`; no critical/high finding remained. Reviewer-availability fallback is disclosed as required.

## NDIA Sequential Queue Record

- Input row: `79/125`; input ticker: `NDIA`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:NDIA`; Global X's official product page, current factsheet, summary prospectus and annual shareholder report identify the NYSE Arca listing. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. Global X explicitly labels NDIA the `Global X India Active ETF`, describes it as an actively managed ETF, and states that its strategy uses stock picking and portfolio management across sectors. The factsheet labels the category `Equity - International - Single Country` and the prospectus objective is long-term capital growth rather than tracking a disclosed index. It therefore fails the required passive/index-tracking equity gate.
- Per the type gate, no 10-year coverage calculation, annual NAV TR table, S&P 500 comparison, performance page, region row or performance-index coverage row was created. Any official performance figures reviewed remain source context only and are not treated as ETF v1 performance coverage.
- Official current context: product-page NAV total-return summary shows since-inception annualized `4.88%` through `2026-06-30`, current product details as of `2026-07-17` show inception `2023-08-17`, total expense ratio `0.75%`, 30 holdings and primary exchange NYSE Arca. These values are not used for the unsupported ETF performance artifact.

### NDIA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:NDIA` | [Global X NDIA official product page](https://www.globalxetfs.com/funds/NDIA) | identity, explicit active classification, objective, inception, current fund details and official performance context | Page accessed `2026-07-24`; fund details through `2026-07-17`; performance summary through `2026-06-30` |
| `NYSE Arca:NDIA` | [Global X NDIA factsheet](https://assets.globalxetfs.com/funds/documents/ndia/Fact-Sheet_NDIA.pdf) | official active strategy, exchange, inception, expense ratio and fund classification | Factsheet dated `2026-04-30`; 30 holdings; total expense ratio `0.75%` |
| `NYSE Arca:NDIA` | [Global X NDIA summary prospectus](https://assets.globalxetfs.com/funds/documents/ndia/prospectus-regulatory/Summary-Prospectus.pdf) | formal listing and explicit investment objective / fund structure | Prospectus dated `2025-04-01`; ticker NDIA; exchange NYSE Arca; management fee `0.75%` and total annual operating expenses `0.76%` in that document |
| `NYSE Arca:NDIA` | [Global X NDIA annual shareholder report](https://assets.globalxetfs.com/funds/documents/ndia/prospectus-regulatory/Annual-Shareholder-Report.pdf) | principal listing and active-fund cross-check | Report period ended `2025-11-30`; principal listing exchange NYSE Arca; annual report calls NDIA actively managed |

### NDIA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order, canonical exchange, fund identity, passive-versus-active classification, terminal-status selection, source URL/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. Because NDIA failed the passive/index-tracking equity gate as actively managed, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed as required.

## CHIQ Sequential Queue Record

- Input row: `80/125`; input ticker: `CHIQ`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:CHIQ`; Global X's official product page, factsheet, summary prospectus and annual shareholder report identify the NYSE Arca listing. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking equity ETF. Global X states that CHIQ seeks to provide investment results corresponding generally to the price and yield performance of the MSCI China Consumer Discretionary 10/50 Index; the annual shareholder report states the fund is passively managed and generally seeks full replication.
- Mandatory coverage audit: the stale page had no verified annual rows. Rechecking the official 2026 summary prospectus, current product page, factsheet and annual shareholder report found ten complete official calendar-year NAV total-return observations for 2016-2025, so 10-year coverage is accepted. The fund's name/objective/strategy and underlying index changed effective 2018-12-06; pre-change returns use the predecessor Solactive China Consumer Total Return Index and post-change returns use MSCI China Consumer Discretionary 10/50 Index. This break is disclosed rather than silently treated as one unchanged index history.
- Calendar-window calculation: 2015-12-31 to 2025-12-31, actual `10.00` years; normalized TR `100.00` to `199.05`; cumulative `99.05%`; CAGR `7.13%`. The normalized endpoint is calculated from official annual NAV TR rows and is not a proxy.
- Current rolling observation: official Global X product page reports NAV TR CAGR `5.31%` for the rolling 10-year period through `2026-06-30`; raw rolling endpoints are not disclosed, so this is shown separately from the calendar-window calculation. Official Explore data reports current NAV TR YTD `-25.23%` as of `2026-07-21`.
- Annual NAV observations: 2016 `-5.88%`, 2017 `65.28%`, 2018 `-27.72%`, 2019 `43.06%`, 2020 `93.43%`, 2021 `-27.23%`, 2022 `-22.07%`, 2023 `-10.92%`, 2024 `12.16%`, 2025 `12.91%`; 2021-2025 CAGR `-8.55%`.
- S&P 500 comparison: cached USD Total Return rows are used for 2016-2025 common reference only; no 2026 S&P value is used.

### CHIQ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CHIQ` | [Global X CHIQ official product/performance page](https://www.globalxetfs.com/funds/CHIQ) | identity, index, exchange, inception, fees, current NAV/YTD and rolling NAV TR | Page accessed `2026-07-24`; product/holdings data through `2026-07-21`; performance summary through `2026-06-30` |
| `NYSE Arca:CHIQ` | [Global X CHIQ factsheet](https://assets.globalxetfs.com/funds/documents/chiq/Fact-Sheet_CHIQ.pdf) | passive/index-tracking classification, NAV TR basis, inception, benchmark, fee and index-change disclosure | Factsheet dated `2026-03-31`; historical performance through `2026-03-31`; 10Y NAV CAGR in that factsheet `6.92%` as of its date |
| `NYSE Arca:CHIQ` | [Global X CHIQ 2026 summary prospectus](https://assets.globalxetfs.com/funds/documents/chiq/prospectus-regulatory/Summary-Prospectus_CHIQ.pdf) | official annual NAV total-return rows 2016-2025, formal listing, objective, fee and benchmark/index history | Prospectus dated `2026-03-01`; annual returns through `2025-12-31`; 10Y NAV return `7.13%` through `2025-12-31` |
| `NYSE Arca:CHIQ` | [Global X CHIQ annual shareholder report](https://assets.globalxetfs.com/funds/documents/chiq/prospectus-regulatory/Annual-Shareholder-Report.pdf) | passive/full-replication and annual performance cross-check | Report period ended `2025-10-31`; one-year NAV return `14.55%`; 10Y NAV return `7.10%` as of report date; not mixed into the calendar-year window |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### CHIQ Raw Observations And Calculations

| Period | CHIQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -5.88% | 11.96% |
| 2017 | 65.28% | 21.83% |
| 2018 | -27.72% | -4.38% |
| 2019 | 43.06% | 31.49% |
| 2020 | 93.43% | 18.40% |
| 2021 | -27.23% | 28.71% |
| 2022 | -22.07% | -18.11% |
| 2023 | -10.92% | 26.29% |
| 2024 | 12.16% | 25.02% |
| 2025 | 12.91% | 17.88% |
| 2026 YTD | -25.23% | not comparable; current year not cached |

- Calendar TR product: `100.00 × 1.99053623 = 199.05`; cumulative `99.05%`; `CAGR = (1.99053623^(1/10)) - 1 = 7.13%`.
- 2021-2025 comparison slice: product `0.63974613 - 1 = -36.03%`; CAGR `-8.55%`.
- Rolling official 10Y NAV TR CAGR: `5.31%` through `2026-06-30`; normalized endpoint from the rounded issuer CAGR would be approximately `167.76`, but raw endpoints are not disclosed and this normalized check is not mixed with the calendar-window endpoint.
- Best calendar year: `2020 +93.43%`; worst: `2022 -22.07%`.

### CHIQ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, calendar and rolling windows, benchmark cache, current-YTD, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The 2018 index/strategy change, rolling-versus-calendar as-of difference, current YTD date, and benchmark cache boundary are explicitly disclosed.

## IOPP Sequential Queue Record

- Input row: `81/125`; input ticker: `IOPP`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:IOPP`; the official Simplify summary prospectus states that shares are listed and traded on NYSE Arca, Inc.; the prospectus and current fund page identify ticker IOPP. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. Simplify labels IOPP the `Simplify Tara India Opportunities ETF`, says it is actively managed with a goal of outperforming the MSCI India Index, and describes bottom-up company-specific research, factor screening, portfolio-manager judgment and flexible position changes. It is an active India equity ETF, not a passive/index-tracking equity ETF.
- The official page identifies inception `2024-03-04`, current gross/net expense ratios `1.03%/0.73%` as of `2026-07-17`, and no options available. These facts are recorded as classification context only. Per the type gate, no 10-year coverage calculation, annual NAV TR table, S&P 500 comparison, performance page, region row or performance-index coverage row was created.

### IOPP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:IOPP` | [Simplify IOPP official product page](https://www.simplify.us/etfs/iopp-simplify-tara-india-opportunities-etf) | identity, explicit active classification, objective, current fund details, expense ratio and limited-history context | Page accessed `2026-07-24`; fund details through `2026-07-17`; performance summary through `2026-06-30` |
| `NYSE Arca:IOPP` | [Simplify IOPP 1Q26 factsheet](https://www.simplify.us/sites/default/files/etfs/factsheet/2026-04/IOPP-Fact-Sheet-1Q26.pdf) | active strategy, bottom-up/high-conviction process, inception, exchange, fees and risk context | Factsheet dated `2026-03-31`; gross expense `1.03%`; net expense `0.73%`; inception `2024-03-04` |
| `NYSE Arca:IOPP` | [SEC IOPP summary prospectus](https://www.sec.gov/Archives/edgar/data/1810747/000182912625008758/simplifyetf-iopp_497k.htm) | formal listing exchange, explicit active classification, investment process, fee table and risk disclosures | Prospectus dated `2025-11-01`; shares listed on NYSE Arca; actively managed; fee waiver through at least `2026-10-31` |
| `NYSE Arca:IOPP` | [Simplify IOPP prospectus](https://www.simplify.us/sites/default/files/etfs/prospectus/2024-10/Simplify_IOPP_Prospectus.pdf) | original formal listing and fund-structure cross-check | Prospectus dated `2024-11-01`; ticker/exchange `IOPP (NYSE Arca, Inc.)`; inception-period financial highlights |

### IOPP Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, fund identity, passive-versus-active classification, terminal-status selection, source URL/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. Because IOPP failed the passive/index-tracking equity gate as actively managed, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed as required.

## MCHI Sequential Queue Record

- Input row: `82/125`; input ticker: `MCHI`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:MCHI`; iShares' official product page, factsheet and summary prospectus identify NASDAQ as the exchange. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking equity ETF. iShares states that MCHI seeks to track an index composed of Chinese equities available to international investors; the benchmark is MSCI China Index (Net). Exchange-traded index futures may be used to offset cash/receivables for tracking, but the fund is not derivative-heavy by strategy.
- Mandatory coverage audit: the existing page had annual NAV rows only for 2021-2025. Rechecking the official iShares product page, current factsheet, summary prospectus, annual financial statements and distribution/performance disclosures confirms official rolling 10-year NAV TR coverage, so the fund qualifies for `completed_10Y`. The current page reports 10-year NAV TR cumulative `45.52%` / annualized `3.82%` for 2016-06-30 to 2026-06-30.
- 10-year calculation: normalized TR `100.00` to `145.52`; raw NAV endpoints are not disclosed. `145.52 = 100.00 × (1 + 45.52%)`; `CAGR = (145.52/100.00)^(1/10)-1 = 3.82%` using the issuer's rounded cumulative and annualized figures.
- Annual observations: official current capture discloses 2021 `-22.38%`, 2022 `-22.53%`, 2023 `-11.07%`, 2024 `18.06%`, 2025 `31.07%`; 2016-2020 annual NAV rows remain `not disclosed`. The disclosed 2021-2025 rows compound to `-17.25%` / CAGR `-3.72%`.
- Current official observation: NAV TR YTD `-9.33%` as of `2026-07-21`; iShares also reports month-end YTD `-14.65%` as of `2026-06-30`. These are kept separate by as-of date.
- S&P 500 comparison: cached USD Total Return rows are used for 2021-2025 common reference and for the displayed 2016-2020 benchmark comparison; no 2026 S&P value is used.

### MCHI Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:MCHI` | [iShares MCHI official product/performance page](https://www.ishares.com/us/products/239619/ishares-msci-china-etf) | identity, exchange, inception, benchmark, fees, current NAV/YTD, rolling NAV TR, disclosed calendar rows, holdings and exposures | Page accessed `2026-07-24`; NAV/current YTD through `2026-07-21` / NAV as of `2026-07-22`; standardized performance through `2026-06-30` |
| `NASDAQ:MCHI` | [iShares MCHI factsheet](https://www.ishares.com/us/literature/fact-sheet/mchi-ishares-msci-china-etf-fund-fact-sheet-en-us.pdf) | passive/index-tracking classification, benchmark, inception, expense ratio and official annual rows 2021-2025 | Factsheet dated `2026-03-31`; annual rows through `2025-12-31`; expense ratio `0.59%` |
| `NASDAQ:MCHI` | [iShares MCHI summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-etf-8-31.pdf) | formal listing, investment objective, index strategy and fund risk/implementation disclosures | Prospectus dated `2025-12-30`; NASDAQ listing; MSCI China Index (Net) objective |
| `NASDAQ:MCHI` | [iShares MCHI 2025 annual financial statements](https://www.ishares.com/us/literature/annual-financial-statements/afs-ishares-trust-msci-country-etfs-book1-08-31-en.pdf) | annual financial/document cross-check and legal fund identity | Annual statements dated `2025-08-31`; MCHI listed on NASDAQ; not used to fill missing annual NAV rows |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### MCHI Raw Observations And Calculations

| Period | MCHI NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | -22.38% | 28.71% |
| 2022 | -22.53% | -18.11% |
| 2023 | -11.07% | 26.29% |
| 2024 | 18.06% | 25.02% |
| 2025 | 31.07% | 17.88% |
| 2026 YTD | -9.33% as of 2026-07-21 | not comparable; current year not cached |

- Rolling 10Y official NAV TR: cumulative `45.52%`, annualized `3.82%`, 2016-06-30 to 2026-06-30; normalized endpoint `145.52` from `100.00`.
- 2021-2025 disclosed calendar slice: cumulative `-17.25%`, CAGR `-3.72%`.
- 2026-06-30 month-end official YTD `-14.65%` is retained as a separate as-of observation from latest current YTD `-9.33%` at 2026-07-21.
- Among disclosed annual rows, best is `2025 +31.07%`; worst is `2022 -22.53%`. Full 10-year best/worst ranking is not claimed because 2016-2020 rows are not disclosed.

### MCHI Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, rolling and annual windows, benchmark cache, current-YTD, region/index links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The 10-year rolling window, 2021-2025 annual disclosure, 2016-2020 gap, current-versus-month-end YTD difference, and futures implementation note are explicitly disclosed.

## ADIV Sequential Queue Record

- Input row: `83/125`; input ticker: `ADIV`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:ADIV`; Guinness Atkinson's April 30, 2026 prospectus and summary prospectus identify ADIV as listed on NYSE Arca. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. The official prospectus says ADIV invests in dividend-producing Asia-Pacific equity securities but is `actively managed`; the adviser selects holdings using proprietary and independent research and traditional fundamental analysis of business prospects, valuation, dividend history, leverage and dividend-growth potential. It is not a passive/index-tracking equity ETF.
- The fund's official page lists inception `2021-03-27` for the ETF series/reorganization, current gross/net expense ratios `1.95%/0.78%` as of `2026-07-20`, and a predecessor mutual-fund performance history. These facts are classification context only. Per the type gate, no 10-year coverage calculation, annual NAV TR table, S&P 500 comparison, performance page, region row or performance-index coverage row was created.
- The prospectus also records a primary benchmark change effective `2026-05-01` from MSCI AC Pacific ex Japan Net Return to MSCI AC Asia Pacific ex Japan Net Return; this does not change the active classification and is not used to create a performance artifact.

### ADIV Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:ADIV` | [Guinness Atkinson funds page](https://www.gafunds.com/our-funds/) | official identity, current NAV/fees, fund name and current product context | Page accessed `2026-07-24`; data as of `2026-07-20`; gross/net expense `1.95%/0.78%` |
| `NYSE Arca:ADIV` | [Guinness Atkinson ADIV summary prospectus](https://www.sec.gov/Archives/edgar/data/919160/000121390026052640/ea0287226-07_497k.htm) | formal listing, active classification, investment process, fees, predecessor history and benchmark-change disclosure | Prospectus dated `2026-04-30`; NYSE Arca; active management; primary benchmark changed `2026-05-01` |
| `NYSE Arca:ADIV` | [Guinness Atkinson ADIV annual shareholder report](https://www.sec.gov/Archives/edgar/data/919160/000139834426004881/fp0097165-1_ncsrixbrl.htm) | legal fund identity, ETF/predecessor mutual-fund structure and annual-report cross-check | Report for year ended `2025-12-31`; identifies the ETF series and predecessor reorganization dated `2021-03-27` |

### ADIV Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, fund identity, passive-versus-active classification, terminal-status selection, source URL/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. Because ADIV failed the passive/index-tracking equity gate as actively managed, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed as required.

## EPHE Sequential Queue Record

- Input row: `84/125`; input ticker: `EPHE`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:EPHE`; official iShares product/data pages identify the exchange, fund and ticker. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking Philippines equity ETF. iShares states that EPHE seeks to track an index composed of Philippine equities and identifies the benchmark as `MSCI Philippines IMI 25/50 Index (USD) (Net)`.
- Mandatory coverage audit: the stale page had only 2021-2025 annual rows and did not identify the benchmark. Rechecking the official product page, data page, factsheet, prospectus and shareholder report confirmed official rolling 10-year NAV TR coverage, so the fund qualifies for `completed_10Y`.
- Rolling 10-year window: `2016-06-30` to `2026-06-30`, `10.00 elapsed years`; official cumulative NAV TR `-28.05%` and average annual/CAGR `-3.24%`. Raw endpoints are not disclosed. The page uses normalized `100.00` to `71.95` only to represent the published cumulative return.
- Annual observations: official NAV TR rows 2021 `-2.10%`, 2022 `-14.37%`, 2023 `-0.27%`, 2024 `1.08%`, 2025 `-0.54%`; 2016-2020 annual rows remain `not disclosed`. The disclosed 2021-2025 rows compound to `-15.95%` / CAGR `-3.42%`.
- Current official observation: NAV TR YTD `3.93%` as of `2026-07-21`; the month-end page also reports YTD `0.06%` as of `2026-06-30`. These are retained as separate as-of observations.
- Index-history gap: iShares states that EPHE began tracking the current MSCI Philippines IMI 25/50 Index (Net) on `2020-12-01`; the performance page discloses this change and does not treat earlier history as perfectly like-for-like.

### EPHE Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:EPHE` | [iShares EPHE official product/performance page](https://www.ishares.com/us/products/239675/ishares-msci-philippines-etf) | identity, exchange, inception, benchmark, expense ratio, current YTD, rolling NAV TR, annual rows and sector exposure | Page accessed `2026-07-24`; current YTD `3.93%` as of `2026-07-21`; rolling/standardized data through `2026-06-30`; exposure as of `2026-07-17` |
| `NYSE Arca:EPHE` | [iShares EPHE official data page](https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239675&seoSlug=ishares-msci-philippines-etf) | current NAV/YTD cross-check | Current YTD `3.93%` and NAV as of `2026-07-21` |
| `NYSE Arca:EPHE` | [iShares EPHE factsheet](https://www.ishares.com/us/literature/fact-sheet/ephe-ishares-msci-philippines-etf-fund-fact-sheet-en-us.pdf) | passive classification, benchmark, expense ratio, annual NAV rows and index-change disclosure | Factsheet accessed `2026-07-24`; annual rows through `2025-12-31`; current-index tracking from `2020-12-01` |
| `NYSE Arca:EPHE` | [iShares EPHE prospectus material](https://www.ishares.com/uk/individual/en/literature/prospectus/p-ishares-trust-emerging-8-31-emea.pdf?siteEntryPassthrough=true&switchLocale=y) | objective and index implementation cross-check | Official prospectus material accessed `2026-07-24` |
| `NYSE Arca:EPHE` | [BlackRock EPHE annual shareholder report](https://www.blackrock.com/us/individual/literature/annual-report/ar-ephe-en.pdf) | legal fund identity and annual-report cross-check | Annual report for period ended `2025-08-31` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### EPHE Raw Observations And Calculations

| Period | EPHE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | -2.10% | 28.71% |
| 2022 | -14.37% | -18.11% |
| 2023 | -0.27% | 26.29% |
| 2024 | 1.08% | 25.02% |
| 2025 | -0.54% | 17.88% |
| 2026 YTD | 3.93% as of 2026-07-21 | not comparable; current year not cached |

- Rolling 10Y official NAV TR: cumulative `-28.05%`, annualized `-3.24%`, 2016-06-30 to 2026-06-30; normalized endpoint `71.95` from `100.00`.
- `71.95 = 100.00 × (1 - 28.05%)`; `CAGR = (71.95 / 100.00)^(1 / 10.00) - 1`, with the issuer's rounded CAGR retained.
- 2021-2025 disclosed calendar slice: cumulative `-15.95%`, CAGR `-3.42%`.
- Disclosed best/worst rows are `2024 +1.08%` and `2022 -14.37%`; full 10-year ranking is not claimed because 2016-2020 rows are not disclosed.

### EPHE Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, rolling and annual windows, S&P 500 cache, current-YTD dates, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The 2016-2020 annual-row gap, 2020-12-01 index change, rolling-versus-calendar as-of difference, current-YTD date, normalized endpoint disclosure and benchmark cache boundary are explicitly recorded.

## CAS Sequential Queue Record

- Input row: `85/125`; input ticker: `CAS`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:CAS`; Simplify's formal summary prospectus identifies CAS as listed and traded on NYSE Arca. The 1Q26 factsheet compact details field says `NYSE`, so the exchange-field conflict is disclosed and the formal prospectus is retained as canonical. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. Simplify describes CAS as actively managed, with China A-share exposure obtained through total return swaps and a risk-managed options strategy layered on top. The strategy writes short-term spreads on equity, fixed-income and commodity indices or ETFs. This is derivative-heavy/option-income/multi-strategy exposure, not a passive/index-tracking equity ETF.
- The official product page lists inception `2025-01-13`, expense ratio `0.88%`, and fund overview data as of `2026-07-17`; these facts are classification context only. Per the type gate, the `check-etf-performance` calculation step is not run, and no 10-year NAV TR table, S&P 500 comparison, performance page, region row or performance-index coverage row is created.

### CAS Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CAS` | [Simplify CAS official product page](https://www.simplify.us/etfs/cas-simplify-china-shares-plus-income-etf) | identity, current fund details, explicit active classification, total-return-swap implementation, options overlay, expense ratio and inception | Page accessed `2026-07-24`; fund overview as of `2026-07-17`; inception `2025-01-13`; expense ratio `0.88%` |
| `NYSE Arca:CAS` | [SEC CAS summary prospectus](https://www.sec.gov/Archives/edgar/data/1810747/000182912625008765/simplifyetf-cas_497k.htm) | formal listing exchange, investment objective, active-management classification and fee table | Prospectus dated `2025-11-01`; shares listed and traded on NYSE Arca |
| `NYSE Arca:CAS` | [Simplify CAS 1Q26 factsheet](https://www.simplify.us/sites/default/files/etfs/factsheet/2026-04/CAS-Fact-Sheet-1Q26.pdf) | strategy, options overlay, inception, fee and compact exchange-field cross-check | Factsheet dated `2026-03-31`; compact exchange field says `NYSE`; inception `2025-01-13`; expense ratio `0.88%` |
| `NYSE Arca:CAS` | [Simplify CAS launch announcement](https://www.simplify.us/news-media/simplify-introduces-cas-china-shares-plus-income-etf) | issuer description of active China A-share strategy, total-return swaps and options overlay | Announcement dated `2025-01-14`; identifies CAS as actively managed |

### CAS Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange and conflict, fund identity, passive-versus-active classification, derivative-heavy/option-income gate, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. Because CAS failed the passive/index-tracking equity gate as actively managed and derivative-heavy/option-income, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed as required.

## INDZ Sequential Queue Record

- Input row: `86/125`; input ticker: `INDZ`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:INDZ`; VanEck's May 1, 2026 summary prospectus identifies the principal U.S. listing exchange as NYSE Arca. No provider slug or guessed exchange is used.
- Type-gate result: `unsupported ETF type`. VanEck identifies INDZ as the actively managed VanEck India Select ETF. The strategy uses fundamental research and a disciplined multi-step process to select Indian companies with strong long-term return profiles, high capital efficiency and resilient business models, across small-, mid- and large-capitalization issuers. It is not a passive/index-tracking equity ETF.
- The official product page lists inception `2026-02-18`, performance since inception, and an expense waiver limiting operating expenses to `0.75%` through at least `2027-05-01`; these facts are classification context only. Per the type gate, no 10-year NAV TR calculation, annual NAV TR table, S&P 500 comparison, performance page, region row or performance-index coverage row is created.

### INDZ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:INDZ` | [VanEck INDZ official product page](https://www.vaneck.com/us/en/investments/india-select-etf-indz/) | identity, active classification, investment process, inception, current NAV/performance context and fee waiver | Page accessed `2026-07-24`; product data through `2026-06-22`; inception `2026-02-18`; expense waiver cap `0.75%` through at least `2027-05-01` |
| `NYSE Arca:INDZ` | [SEC VanEck INDZ summary prospectus](https://www.sec.gov/Archives/edgar/data/768847/000076884726000084/vefvaneckindiaselectetfsum.htm) | formal listing exchange, investment objective, active strategy and fee disclosure | Prospectus dated `2026-05-01`; principal U.S. listing exchange NYSE Arca |
| `NYSE Arca:INDZ` | [VanEck INDZ factsheet](https://www.vaneck.com/us/en/investments/india-select-etf-indz-fact-sheet.pdf) | explicit active classification, exchange, inception and portfolio context | Factsheet as of `2026-02-28`; exchange NYSE Arca; inception `2026-02-18`; options `No` |
| `NYSE Arca:INDZ` | [VanEck INDZ launch release](https://www.vaneck.com/us/en/press-releases/vaneck-expands-emerging-market-and-sector-investing-suites-with-launch-of-india-select-etf-indz-and-communications-services-trusector-etf-truc/) | issuer confirmation of active, research-led security selection | Release dated `2026-02-19` |

### INDZ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, fund identity, passive-versus-active classification, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. Because INDZ failed the passive/index-tracking equity gate as actively managed, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed as required.

## INDQ Sequential Queue Record

- Input row: `87/125`; input ticker: `INDQ`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `Nasdaq:INDQ`; Pacer's official factsheet and SEC SAI identify the listing as Nasdaq Stock Market LLC. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/rules-based India equity ETF. Pacer states that INDQ seeks to track the total return performance of the `ActiveAlpha India Quality Index`; the strategy uses objective quality, value and momentum screens and quarterly reconstitution rather than discretionary stock selection.
- Mandatory coverage audit: the existing page had no verified inception, index or return values. Official Pacer product/factsheet/prospectus materials confirm inception `2026-03-31`, so `10-year NAV TR unavailable`. The official performance table and factsheet show the numeric NAV TR fields as `N/A`; available-period NAV TR, CAGR and current YTD are therefore recorded as `not disclosed`, not calculated from the quoted NAV.
- The official factsheet discloses NAV `$25.00` and expense ratio `0.88%` as of `2026-03-31`, but a NAV level alone is not a total-return endpoint and is not used to create a proxy return.

### INDQ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Nasdaq:INDQ` | [Pacer INDQ official product/performance page](https://www.paceretfs.com/products/indq) | identity, passive/rules-based strategy, related index, inception, expense ratio, NAV-return convention and performance-data gap | Page accessed `2026-07-24`; performance snapshot dated `2026-03-31`; inception `2026-03-31`; expense ratio `0.88%`; numeric performance fields N/A |
| `Nasdaq:INDQ` | [Pacer INDQ factsheet](https://www.paceretfs.com/media/indq.pdf) | passive classification, index, exchange, inception, NAV/expense snapshot, distributions-reinvestment convention and official N/A performance table | Factsheet data as of `2026-03-31`; NAV `$25.00`; expense ratio `0.88%`; exchange Nasdaq; NAV TR fields N/A |
| `Nasdaq:INDQ` | [Pacer INDQ documents](https://docs.paceretfs.com/indq) | official document hub and summary-prospectus access | Accessed `2026-07-24`; summary prospectus dated `2025-12-22` |
| `Nasdaq:INDQ` | [SEC INDQ statement of additional information](https://www.sec.gov/Archives/edgar/data/1616668/000089418926007588/paceractivealphaindiaquali.htm) | formal listing, index-tracking objective, adviser/sub-adviser and fund-structure cross-check | SAI dated `2025-12-22`, amended `2026-03-05`; Nasdaq listing |
| `Nasdaq:INDQ` | [Pacer INDQ launch release](https://www.paceretfs.com/media/Pacer_ETFs_INDQ_Launch_Press_Release.pdf) | launch date and factor-based passive strategy context | Release dated `2026-04-01`; launch/inception context |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### INDQ Raw Observations And Calculations

| Period | INDQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not applicable; before inception | 25.02% |
| 2025 | not applicable; before inception | 17.88% |
| 2026 YTD | not disclosed; official field N/A | not comparable; current year not cached |

- `10-year NAV TR unavailable`: official inception is `2026-03-31`.
- Available-period endpoints and annual NAV TR rows: `not disclosed` / official fields `N/A`.
- No CAGR, cumulative return, up/down count, best/worst year or proxy was calculated.

### INDQ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period and annual windows, benchmark cache, current-YTD gap, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The sub-10-year history, official N/A performance fields, NAV-level-versus-total-return distinction, and no-proxy decision are explicitly disclosed.

## ICNYF Sequential Queue Record

- Input row: `88/125`; input ticker: `ICNYF`; terminal status: `unsupported ETF type`.
- Canonical entity key: `LSE:CNYB`; iShares' official listings identify the USD distributing share class as `CNYB` on the London Stock Exchange, ISIN `IE00BYPC1H27`, with share-class launch date `2019-07-24`. The input OTC symbol `ICNYF` is treated as an alias; the canonical exchange-qualified key is not a provider slug.
- Type-gate result: `unsupported ETF type`. iShares identifies the fund as fixed income and states that it tracks an index of fixed-rate PRC Ministry of Finance treasury bonds and Chinese policy-bank debt. It is a bond ETF, outside the passive/index-tracking equity ETF scope.
- Because the fund failed the asset-class gate, the `check-etf-performance` calculation step is not run and no 10-year NAV TR table, S&P 500 comparison, performance page, region row or performance-index coverage row is created.

### ICNYF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:CNYB` | [iShares China CNY Bond UCITS ETF official listing/performance page](https://www.ishares.com/uk/individual/en/products/308851/ishares-china-cny-bond-ucits-etf?siteEntryPassthrough=true) | identity, share-class/listing mapping, fixed-income classification, benchmark and holdings | Page accessed `2026-07-24`; listings and portfolio data through `2026-07-17`; LSE ticker CNYB; ISIN IE00BYPC1H27 |
| `LSE:CNYB` | [iShares CNYB factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/cnyb-ishares-china-cny-bond-ucits-etf-fund-fact-sheet-en-gb.pdf) | formal share-class identity, passive bond objective, LSE listing and fixed-income exposure | Factsheet dated `May 2026`; performance/portfolio data through `2026-05-31`; share-class launch `2019-07-24`; TER `0.35%` |
| `LSE:CNYB` | [London Stock Exchange CNYB company page](https://www.londonstockexchange.com/stock/CNYB/ishares/company-page) | exchange-level cross-check for canonical LSE ticker and fund name | Page accessed `2026-07-24`; CNYB listed as iShares China CNY Bond UCITS ETF (Dist) |

### ICNYF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, OTC-alias resolution, canonical exchange, exact share class, asset-class/type gate, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. Because ICNYF resolved to a fixed-income bond ETF, no performance artifact or graph-navigation update was required; reviewer-availability fallback is disclosed as required.

## CNQQ Sequential Queue Record

- Input row: `89/125`; input ticker: `CNQQ`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NASDAQ:CNQQ`; Rayliant's official product page and SEC summary prospectus identify the primary exchange as NASDAQ. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking China technology equity ETF. Rayliant states that CNQQ seeks to track the `Solactive ChinaAMC Transformative China Tech Index`; the fund generally invests at least 80% in index securities or participatory notes. Total-return swaps may be used for index exposure and are disclosed as implementation/counterparty risk, not as the fund's classification.
- Mandatory coverage audit: the existing page had no verified inception, index or reproducible return. Official product page, summary prospectus and annual report confirm inception `2025-09-24`, so `10-year NAV TR unavailable`. The latest official product-page table reports NAV since-inception cumulative `6.54%` and YTD `14.95%` as of `2026-06-30`.
- Available-period window: `2025-09-24` to `2026-06-30`, `279 days / 0.763876 years`; normalized NAV TR `100.00` to `106.54`; derived annualized CAGR `8.65%`. This is a short-period annualization and is not labeled as 10-year performance.
- Inception-date conflict: the factsheet says `2025-09-25`, while the official product page, summary prospectus and annual shareholder report use `2025-09-24`; the formal product/prospectus date is used and the conflict is disclosed.
- Annual observations: no complete calendar-year NAV TR row is disclosed since inception; 2025 is an incomplete inception year. The factsheet's earlier since-inception NAV return was `-15.16%` as of `2026-03-31`; the later product-page observation `6.54%` as of `2026-06-30` is used for the current record.

### CNQQ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:CNQQ` | [Rayliant CNQQ official product/performance page](https://funds.rayliant.com/cnqq/) | identity, exchange, inception, index objective, current NAV/YTD, since-inception NAV return, strategy and swap disclosure | Page last updated `2026-07-07`; performance as of `2026-06-30`; NAV TR since inception `6.54%`; YTD `14.95%`; expense ratio `0.75%` |
| `NASDAQ:CNQQ` | [Rayliant CNQQ factsheet](https://funds.rayliant.com/wp-content/uploads/FactSheets/Rayliant-CNQQ-ETF.pdf) | passive/index-tracking classification, index, fee, holdings and earlier performance cross-check | Factsheet data as of `2026-03-31`; since-inception NAV return `-15.16%`; factsheet inception `2025-09-25` |
| `NASDAQ:CNQQ` | [SEC CNQQ summary prospectus](https://www.sec.gov/Archives/edgar/data/2061770/000158064226000606/rayliantchinaetf497k.htm) | formal listing, investment objective, index tracking, fee table and derivative implementation | Prospectus dated `2026-01-28`; NASDAQ listing; inception `2025-09-24` in formal fund history |
| `NASDAQ:CNQQ` | [Rayliant CNQQ prospectus](https://funds.rayliant.com/wp-content/uploads/ETF/CNQQ/Rayliant-CAMC-CNQQ-Prospectus.pdf) | audited financial highlights and reinvested-distribution total-return convention | Financial highlights for period ended `2025-09-30`; inception date `2025-09-24`; NAV total return `1.84%` for the short period |
| `NASDAQ:CNQQ` | [Rayliant CNQQ annual shareholder report](https://funds.rayliant.com/wp-content/uploads/ETF/CNQQ/Rayliant-CNQQ-Annual-Shareholder-Report.pdf) | annual-report cross-check for fund identity and benchmark | Report accessed `2026-07-24`; period ended `2025-09-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### CNQQ Raw Observations And Calculations

| Period | CNQQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not applicable; before inception | 25.02% |
| 2025 | not disclosed; incomplete inception year | 17.88% |
| 2026 YTD | 14.95% as of 2026-06-30 | not comparable; current year not cached |

- Available-period NAV TR: cumulative `6.54%`, `2025-09-24` to `2026-06-30`.
- `106.54 = 100.00 × (1 + 6.54%)`; actual years `279 / 365.2425 = 0.763876`.
- `CAGR = (106.54 / 100.00)^(1 / 0.763876) - 1 = 8.65%`; derived and short-period only.
- Complete calendar-year up/down count and best/worst year: not disclosed.

### CNQQ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period and annual windows, benchmark cache, current-YTD dates, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The sub-10-year history, normalized short-period endpoint, derived annualization, 2025 incomplete-year gap, 2026 YTD as-of date, inception-date conflict and swap implementation are explicitly disclosed.

## INDH Sequential Queue Record

- Input row: `90/125`; input ticker: `INDH`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `Nasdaq:INDH`; WisdomTree's official product page, factsheet and SEC summary prospectus identify the NASDAQ listing. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking India equity ETF with a currency-hedge overlay. WisdomTree states that INDH tracks the `WisdomTree India Hedged Equity Index`, does not attempt to outperform its index, and hedges USD/INR exposure.
- Mandatory coverage audit: the existing page had no verified inception, index or reproducible return. Official WisdomTree materials confirm inception `2024-05-09`, so `10-year NAV TR unavailable`. The official month-end table reports since-inception NAV return `1.84%` cumulative and `0.85%` average annual through `2026-06-30`; current NAV TR YTD is `-9.04%` through the same date.
- Available-period window: `2024-05-09` to `2026-06-30`, `782 days / 2.141043 years`; normalized NAV TR `100.00` to `101.84`; official CAGR/average annual `0.85%`. Raw NAV endpoints are not disclosed as a time series.
- Annual observations: complete calendar-year NAV rows are not disclosed in the reviewed official capture; 2024 is an incomplete inception year and 2025 remains `not disclosed`.

### INDH Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Nasdaq:INDH` | [WisdomTree INDH official product/performance page](https://www.wisdomtree.com/us/products/equity/indh) | identity, exchange, inception, index, expense ratio, month-end NAV TR, current YTD, hedge ratio and exposures | Page accessed `2026-07-24`; month-end performance through `2026-06-30`; current fund/holdings data as of `2026-07-17`; inception `2024-05-09`; expense `0.64%`; YTD `-9.04%` |
| `Nasdaq:INDH` | [WisdomTree INDH factsheet](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-indh.pdf) | passive/index-tracking classification, index, exchange, inception, expense and since-inception return cross-check | Factsheet as of `2026-03-31`; inception `2024-05-09`; NASDAQ; NAV since inception `-0.98%` as of `2026-03-31`; performance less than one year cumulative note |
| `Nasdaq:INDH` | [SEC INDH summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011298/indh73125497k.htm) | formal listing, index objective, 80% policy and hedge/index implementation | Prospectus dated `2025-08-01`; NASDAQ listing; tracks WisdomTree India Hedged Equity Index |
| `Nasdaq:INDH` | [WisdomTree India Hedged Equity Index](https://www.wisdomtree.com/indexes/wtieqh) | index methodology and constituent universe context | Page accessed `2026-07-24`; index includes the 75 largest Indian companies |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### INDH Raw Observations And Calculations

| Period | INDH NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not disclosed; incomplete inception year | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | -9.04% as of 2026-06-30 | not comparable; current year not cached |

- Available-period NAV TR: cumulative `1.84%`, `2024-05-09` to `2026-06-30`.
- `101.84 = 100.00 × (1 + 1.84%)`; actual years `782 / 365.2425 = 2.141043`.
- `CAGR = (101.84 / 100.00)^(1 / 2.141043) - 1 = 0.85%`, agreeing with the issuer's average annual since-inception return.
- One-year NAV TR: `-7.52%` through `2026-06-30`; 3-, 5- and 10-year fields are N/A.
- Aggregate hedge ratio: `100.25%` as of `2026-07-17`.

### INDH Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, hedge-overlay disclosure, available-period and annual windows, benchmark cache, current-YTD dates, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The sub-10-year history, normalized available-period endpoint, annual-row gap, current-YTD date, index hedge and hedge-ratio facts are explicitly disclosed.

## DGIN Sequential Queue Record

- Input row: `91/125`; input ticker: `DGIN`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:DGIN`; VanEck's official product page, factsheet and SEC summary prospectus identify the NYSE Arca listing. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking India thematic equity ETF. VanEck states that DGIN seeks to track the `MVIS Digital India Index (MVDINDTR)` before fees and expenses.
- Mandatory coverage audit: official inception is `2022-02-15`, so `10-year NAV TR unavailable`. The official May 31 performance table reports since-inception NAV TR average annual return `-0.37%`; the latest official product snapshot reports current YTD `-14.23%` as of `2026-06-23`.
- Available-period window: `2022-02-15` to `2026-05-31`, `1,566 days / 4.287562 years`; raw TR endpoints are not disclosed. A normalized start of `100.00` and derived endpoint `98.42` imply approximate cumulative `-1.58%`; the official CAGR/average annual return remains `-0.37%`.
- Annual observations: complete calendar-year NAV TR rows for 2023-2025 are not disclosed; 2022 is an incomplete inception year. S&P 500 TR rows for 2016-2025 reuse the cached USD convention.
- Source-quality choice: the current product page's June 23 YTD is used for the latest YTD field; the dated May factsheet is used for standardized since-inception performance. VanEck's page also exposes an older block consistent with the 2026-03-31 fund profile (`-25.12%` YTD and `-3.25%` life), which is retained as a disclosed stale/conflicting observation and not mixed into the primary record.

### DGIN Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:DGIN` | [VanEck DGIN official product page](https://www.vaneck.com/us/en/investments/digital-india-etf-dgin/overview/) | identity, exchange, index objective, inception, current YTD and expense ratio | Current snapshot as of `2026-06-23`; inception `2022-02-15`; YTD `-14.23%`; expense `0.70%` |
| `NYSE Arca:DGIN` | [VanEck DGIN official performance page](https://www.vaneck.com/us/en/investments/digital-india-etf-dgin/performance/) | NAV TR table, sector/country exposure and distribution history | Standardized NAV table through `2026-05-31`; sector/country data as of `2026-05-31`; stale comparison block also disclosed |
| `NYSE Arca:DGIN` | [VanEck DGIN factsheet](https://www.vaneck.com/us/en/investments/digital-india-etf-dgin-fact-sheet.pdf) | passive/index-tracking classification and standardized return cross-check | As of `2026-05-31`; NAV life average annual `-0.37%`; 10-year field unavailable |
| `NYSE Arca:DGIN` | [SEC DGIN summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736023000421/vaneckdigitalindiaetfdgin-.htm) | formal listing and investment objective | Prospectus confirms NYSE Arca and index-tracking objective |
| `NYSE Arca:DGIN` | [SEC DGIN index-methodology supplement](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000237/ck0001137360-20260227.htm) | methodology-change gap | Change effective `2026-03-20` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### DGIN Raw Observations And Calculations

| Period | DGIN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not disclosed; incomplete inception year | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | -14.23% as of 2026-06-23 | not comparable; current year not cached |

- Available-period NAV TR: official average annual `-0.37%`, `2022-02-15` to `2026-05-31`.
- Actual years: `1,566 / 365.2425 = 4.287562`.
- Normalized endpoint: `100 × (1 - 0.0037)^4.287562 = 98.42`; derived cumulative is approximately `-1.58%` and depends on the issuer's rounded CAGR.
- Complete-calendar up/down count and best/worst year: not disclosed.

### DGIN Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period and annual windows, benchmark cache, current-YTD dates, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The sub-10-year history, normalized endpoint, rounded-CAGR limitation, unavailable raw endpoints/annual rows, separate YTD and standardized as-of dates, stale block, and methodology-change gap are explicitly disclosed.

## CBON Sequential Queue Record

- Input row: `92/125`; input ticker: `CBON`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:CBON`; VanEck's official factsheet identifies the exchange as NYSE Arca and the official product page identifies the fund as VanEck China Bond ETF. No provider slug or guessed exchange is used.
- Type-gate result: unsupported — bond ETF. VanEck states that CBON tracks the `FTSE Chinese Broad Bond 0-10 Diversified Select Index`, composed of RMB-denominated fixed-rate bonds issued by Chinese credit, governmental and quasi-governmental issuers. Bond exposure is outside the required passive/index-tracking equity ETF scope.
- Because the type gate failed, `check-etf-performance` was not called for CBON, and no NAV TR/10-year equity comparison, performance page, region page update, or performance-index row was created.

### CBON Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:CBON` | [VanEck CBON official product page](https://www.vaneck.com/us/en/investments/chinaamc-china-bond-etf-cbon/overview/) | identity, exchange-level product identity, bond objective and tracked index | Page accessed `2026-07-24`; fixed-rate RMB bond exposure; index `FTSE Chinese Broad Bond 0-10 Diversified Select Index` |
| `NYSE Arca:CBON` | [VanEck CBON factsheet](https://www.vaneck.com/us/en/investments/chinaamc-china-bond-etf-cbon-fact-sheet.pdf) | formal exchange, inception and asset-class cross-check | Factsheet as of `2026-04-30`; exchange `NYSE Arca`; inception `2014-11-10`; bond ETF |
| `NYSE Arca:CBON` | [VanEck CBON fund profile](https://www.vaneck.com/us/en/cbon-access-chinas-onshore-bonds-fund-profile.pdf) | fixed-income strategy and performance context, not used for equity analysis | Profile as of `2026-03-31`; bond-index performance only |

### CBON Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, asset-class/type gate, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. CBON is explicitly recorded as an unsupported bond ETF and no equity-performance artifact was created.

## TMH Sequential Queue Record

- Input row: `93/125`; input ticker: `TMH`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:TMH`; the official ADRhedged page identifies the `Toyota Motor Corporation ADRhedged` series and Nasdaq's official listing circular identifies TMH as an exchange-traded fund; exchange-level fund references identify NYSE Arca. The input description `Toyota Motor Corporation` is retained as an alias/context, not treated as the ordinary Toyota stock ticker `TM`.
- Type-gate result: unsupported — single-stock and derivative-heavy structure. The official issuer states that the series normally invests at least 95% of net assets in Toyota ADRs and uses a currency hedge contract. It therefore fails the required diversified passive/index-tracking equity ETF gate.
- Because the type gate failed, `check-etf-performance` was not called for TMH, and no NAV TR/10-year comparison, performance page, region page update, or performance-index row was created.

### TMH Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:TMH` | [ADRhedged Toyota Motor Corporation ADRhedged official page](https://adrhedged.com/security/toyota-motor-corporation-adrhedged/) | identity, objective, holdings, structure, inception and fee | Page updated `2026-07-06`; inception `2025-03-13`; Toyota ADR `97.47%` and cash `2.53%` as of `2026-07-06`; expense `0.19%` |
| `NYSE Arca:TMH` | [Nasdaq official TMH information circular](https://www.nasdaqtrader.com/content/newsalerts/2025/infocircular/TMH_Circular.pdf) | formal ETF/listing and investment-structure cross-check | Circular dated `2025-03-14`; TMH identified as Toyota Motor Corporation ADRhedged exchange-traded fund |

### TMH Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, passive/index-tracking gate, single-stock/derivative-heavy test, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. TMH is explicitly recorded as an unsupported single-stock/hedged ETF and no equity-performance artifact was created.

## WDAF Sequential Queue Record

- Input row: `94/125`; input ticker: `WDAF`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `Nasdaq:WDAF`; WisdomTree's official investment case and launch materials identify Nasdaq as the exchange and the product page identifies the U.S. fund. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking Asia-Pacific thematic equity ETF. WisdomTree states that WDAF seeks to track the `WisdomTree Asia Defense Index (WTADEFN)` before fees and expenses and does not attempt to outperform its index.
- Mandatory coverage audit: official inception `2025-09-12` means `10-year NAV TR unavailable`. The official month-end table reports NAV since-inception cumulative return `0.56%` and current standardized YTD `6.77%` through `2026-06-30`.
- Available-period window: `2025-09-12` to `2026-06-30`, `291 days / 0.796731 years`; normalized NAV TR `100.00` to `100.56`; official cumulative `0.56%`; derived annualized CAGR `0.70%`. It is a short-period annualization and is not labeled 10-year performance.
- Annual observations: 2025 is an incomplete inception year; no complete calendar-year NAV TR row is available. S&P 500 TR rows for 2016-2025 reuse the cached USD convention.

### WDAF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Nasdaq:WDAF` | [WisdomTree WDAF official product page](https://www.wisdomtree.com/us/products/equity/wdaf) | identity, index, inception, fee, NAV TR, YTD and holdings | Product page accessed `2026-07-24`; performance through `2026-06-30`; inception `2025-09-12`; NAV since inception `0.56%`; YTD `6.77%`; net expense `0.45%` as of `2026-07-20` |
| `Nasdaq:WDAF` | [WisdomTree WDAF factsheet](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-wdaf.pdf) | passive/index-tracking classification and return cross-check | Factsheet capture through `2026-03-31`; inception `2025-09-12`; index `WTADEFN`; 10-year field unavailable |
| `Nasdaq:WDAF` | [WisdomTree WDAF investment case](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/investment-case/the-case-for-asia-defense-fund-wdaf.pdf) | formal exchange and index objective | Investment case identifies exchange `Nasdaq`; objective tracks WisdomTree Asia Defense Index |
| `Nasdaq:WDAF` | [WisdomTree Asia Defense Index](https://www.wisdomtree.com/us/indexes/wtadef) | index universe and methodology context | Page accessed `2026-07-24`; developed/emerging Asia-Pacific defense-related companies |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### WDAF Raw Observations And Calculations

| Period | WDAF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not applicable; before inception | 25.02% |
| 2025 | not disclosed; incomplete inception year | 17.88% |
| 2026 YTD | 6.77% as of 2026-06-30 | not comparable; current year not cached |

- Available-period NAV TR: cumulative `0.56%`, `2025-09-12` to `2026-06-30`.
- Actual years: `291 / 365.2425 = 0.796731`.
- Normalized endpoint: `100.00 × (1 + 0.0056) = 100.56`.
- Derived CAGR: `(100.56 / 100.00)^(1 / 0.796731) - 1 = 0.70%`; short-period only.
- Complete-calendar up/down count and best/worst year: not disclosed.

### WDAF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period and annual windows, benchmark cache, current-YTD dates, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The sub-10-year history, normalized endpoint, derived short-period CAGR, incomplete 2025 year, current-YTD as-of date, and benchmark cache convention are explicitly disclosed.

## GIND Sequential Queue Record

- Input row: `95/125`; input ticker: `GIND`; terminal status: `unsupported ETF type`.
- Canonical entity key: `Nasdaq:GIND`; Goldman Sachs' official factsheet and summary prospectus identify the NASDAQ listing and GIND share class. No provider slug or guessed exchange is used.
- Type-gate result: unsupported — active equity ETF. The official factsheet presents “The Benefits of an Active,” “Local Stock-Picking,” and “Beyond the Benchmark”; the prospectus describes a discretionary India equity portfolio and permits derivatives. It fails the required passive/index-tracking equity ETF gate.
- Because the type gate failed, `check-etf-performance` was not called for GIND, and no NAV TR/10-year comparison, performance page, region page update, or performance-index row was created.

### GIND Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Nasdaq:GIND` | [Goldman Sachs GIND factsheet](https://am.gs.com/public-assets/documents/93d0d388-7dee-11f0-8231-f3a13ac1f6ac?view=true) | active classification, exchange, inception and fee | Factsheet as of `2026-05-31`; NASDAQ listing; inception `2025-04-01`; total annual fund operating expenses `0.75%`; active/local stock-picking positioning |
| `Nasdaq:GIND` | [Goldman Sachs GIND summary prospectus](https://am.gs.com/public-assets/documents/16dd63b3-1093-11f0-a26b-87cd5783a190?view=true) | formal listing, objective and strategy/derivative disclosure | Prospectus dated `2025-12-29`; NASDAQ; discretionary India equity strategy; options/futures/forwards may be used |

### GIND Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, passive/active gate, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. GIND is explicitly recorded as an unsupported active ETF and no equity-performance artifact was created.

## TCHI Sequential Queue Record

- Input row: `96/125`; input ticker: `TCHI`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NASDAQ:TCHI`; iShares' official product page and factsheet identify the NASDAQ listing and TCHI share class. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking China technology/multisector equity ETF. iShares states that TCHI seeks to track the `MSCI China Technology Sub-Industries Select Capped Index (USD) (Net)`.
- Mandatory coverage audit: official inception `2022-01-25` means `10-year NAV TR unavailable`. The official performance table reports NAV since-inception cumulative `18.39%` and average annual `3.88%` through `2026-06-30`; the latest current-page NAV TR YTD is `-0.45%` as of `2026-07-17`.
- Available-period window: `2022-01-25` to `2026-06-30`, `1,617 days / 4.427196 years`; normalized NAV TR `100.00` to `118.39`; official cumulative `18.39%`; official average annual `3.88%`; endpoint-derived CAGR `3.89%` after rounding.
- Annual observations: official NAV TR rows are disclosed for 2023 `-5.69%`, 2024 `9.08%`, and 2025 `33.36%`; 2022 is an incomplete inception year. S&P 500 TR rows for 2016-2025 reuse the cached USD convention.
- As-of separation: the later current/date-to-date YTD `-0.45%` as of `2026-07-17` is used for the latest-YTD field; the standardized month-end YTD `13.46%` as of `2026-06-30` is retained separately and not mixed into the same window.

### TCHI Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:TCHI` | [iShares TCHI official product and performance page](https://www.ishares.com/us/products/325390/ishares-msci-china-multisector-tech-etf) | identity, exchange, index, inception, NAV TR, current YTD and exposures | Page accessed `2026-07-24`; standardized performance through `2026-06-30`; current NAV TR YTD `-0.45%` as of `2026-07-17`; inception `2022-01-25`; expense `0.59%` |
| `NASDAQ:TCHI` | [iShares TCHI factsheet](https://www.ishares.com/us/literature/fact-sheet/tchi-ishares-msci-china-multisector-tech-etf-fund-fact-sheet-en-us.pdf) | passive/index-tracking classification and fund-detail cross-check | Factsheet as of `2026-03-31`; exchange `NASDAQ`; index and inception confirmed |
| `NASDAQ:TCHI` | [iShares TCHI summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-multisector-tech-etf-8-31.pdf) | formal investment objective and index tracking | Prospectus dated `2025-12-30`; tracks an index of Chinese technology-related equities |
| `iShares TCHI` | [iShares TCHI annual report](https://www.ishares.com/us/literature/annual-report/ar-tchi-en.pdf) | fund identity and reporting cross-check | Annual report accessed `2026-07-24`; reporting period includes 2025 |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### TCHI Raw Observations And Calculations

| Period | TCHI NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not disclosed; incomplete inception year | -18.11% |
| 2023 | -5.69% | 26.29% |
| 2024 | 9.08% | 25.02% |
| 2025 | 33.36% | 17.88% |
| 2026 YTD | -0.45% as of 2026-07-17 | not comparable; current year not cached |

- Available-period NAV TR: cumulative `18.39%`, official average annual `3.88%`, `2022-01-25` to `2026-06-30`.
- Actual years: `1,617 / 365.2425 = 4.427196`.
- Normalized endpoint: `100.00 × (1 + 0.1839) = 118.39`.
- Endpoint-derived CAGR: `(118.39 / 100.00)^(1 / 4.427196) - 1 = 3.89%`; official average annual `3.88%` is retained as the primary issuer metric.
- Disclosed annual rows 2023-2025 compound to `37.19%`; complete 2021-2025 CAGR is not calculable because 2021-2022 are not available.

### TCHI Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period and annual windows, benchmark cache, current-YTD dates, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The sub-10-year history, normalized endpoint, official/derived CAGR distinction, 2022 incomplete-year gap, 2023-2025 rows, separate current/month-end YTD dates, and systematic-fair-value note are explicitly disclosed.

## JAPN Sequential Queue Record

- Input row: `97/125`; input ticker: `JAPN`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NASDAQ:JAPN`; Horizon Kinetics' official product page and SEC/Nasdaq materials identify the NASDAQ listing. No provider slug or guessed exchange is used.
- Type-gate result: unsupported — active equity ETF. Horizon Kinetics labels JAPN an `Active Equity ETF` and states that it invests primarily in Japanese companies operated by individuals with significant ownership, using a discretionary owner-operator selection process. It fails the required passive/index-tracking equity ETF gate.
- Because the type gate failed, `check-etf-performance` was not called for JAPN, and no NAV TR/10-year comparison, performance page, region page update, or performance-index row was created.

### JAPN Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:JAPN` | [Horizon Kinetics JAPN official product page](https://horizonkinetics.com/products/etf/japn/) | active classification, exchange, inception, strategy and holdings | Page data as of `2026-07-21`; `Active Equity ETF`; NASDAQ; inception `2025-05-12`; expense `0.85%` |
| `NASDAQ:JAPN` | [SEC JAPN summary prospectus](https://www.sec.gov/Archives/edgar/data/1683471/000114554925055230/horizonkineticsjapnsummary.htm) | formal listing, objective and active strategy | Prospectus dated `2025-05-04`; listed on Nasdaq; actively managed owner-operator Japan equity strategy |
| `NASDAQ:JAPN` | [Nasdaq official JAPN information circular](https://www.nasdaqtrader.com/content/newsalerts/2025/InfoCircular/JAPN_Circular_NQ.pdf) | exchange-level launch and ETF classification cross-check | Circular anticipates Nasdaq trading from `2025-05-13`; explicitly calls JAPN an actively managed ETF |

### JAPN Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, passive/active gate, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. JAPN is explicitly recorded as an unsupported active ETF and no equity-performance artifact was created.

## FXA Sequential Queue Record

- Input row: `98/125`; input ticker: `FXA`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:FXA`; Invesco's official product page identifies FXA, and the official filing confirms its primary listing on NYSE Arca. No provider slug or guessed exchange is used.
- Type-gate result: unsupported — currency trust/FX exposure. Invesco states that the CurrencyShares Australian Dollar Trust is designed to track the price of the Australian dollar plus accrued interest, less trust expenses; it holds Australian dollars rather than an equity portfolio. Currency trusts are outside the required passive/index-tracking equity ETF scope.
- Because the type gate failed, `check-etf-performance` was not called for FXA, and no NAV TR/10-year equity comparison, performance page, region page update, or performance-index row was created.

### FXA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FXA` | [Invesco FXA official product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-currencyshares-australian-dollar-trust.html) | identity, currency-trust objective, exchange, inception and expense | Page accessed `2026-07-24`; NYSE Arca; inception `2006-06-21`; total expense ratio `0.40%`; designed to track Australian dollar price plus accrued interest |
| `NYSE Arca:FXA` | [Invesco FXA 10-Q / official filing](https://www.invesco.com/us-rest/contentdetail?contentId=a95d37e7-4857-49ec-90d9-a57915fb4c68&dnsName=us) | formal grantor-trust and listing confirmation | Filing states grantor trust, primary listing transferred to NYSE Arca on `2007-10-30`, and no derivative products held or used |
| `NYSE Arca:FXA` | [Invesco FXA factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/fxa-invesco-currencyshares-australian-dollar-trust-fact-sheet.pdf) | asset-class and benchmark cross-check | Factsheet as of `2025-06-30`; FXA tracks WM/Reuters Australian Dollar Closing Spot Rate; listing exchange NYSE Arca |

### FXA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact trust identity, asset-class/type gate, terminal-status selection, source URLs/as-of dates, no-performance-file decision, no-region/index update decision, and ledger/source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. FXA is explicitly recorded as an unsupported currency trust and no equity-performance artifact was created.

## KGRN Sequential Queue Record

- Input row: `99/125`; input ticker: `KGRN`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:KGRN`; KraneShares' formal annual shareholder report identifies NYSE Arca as the principal listing exchange. The current product page displays `NYSE`; the formal document is retained as canonical and the conflict is disclosed.
- Type-gate result: supported passive/index-tracking China clean-technology thematic equity ETF. KraneShares states that KGRN seeks to track the `MSCI China IMI Environment 10/40 Index`, whose constituents derive at least 50% of revenue from environmentally beneficial products/services.
- Mandatory coverage audit: official inception `2017-10-12` means `10-year NAV TR unavailable` through 2026-06-30. Official NAV TR since inception is cumulative `7.53%` and annualized `0.84%`; current standardized YTD is `-13.22%` through 2026-06-30.
- Available-period window: `2017-10-12` to `2026-06-30`, `3,183 days / 8.714758 years`; normalized NAV TR `100.00` to `107.53`; official cumulative `7.53%`; official annualized `0.84%`. Raw endpoints are not disclosed.
- Annual observations: complete calendar-year NAV TR rows are not disclosed in the current official performance history. The 2025 annual shareholder report's `27.07%` is a fiscal-year period ended 2025-03-31 and is not used as calendar-year 2025.

### KGRN Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KGRN` | [KraneShares KGRN official product/performance page](https://kraneshares.com/etf/kgrn/) | identity, index, current NAV/YTD, inception, fee and current exchange-page field | Page data as of `2026-07-20`; primary exchange displayed `NYSE`; inception `2017-10-12`; NAV YTD `-13.22%` as of `2026-06-30`; expense `0.79%` |
| `NYSE Arca:KGRN` | [KraneShares KGRN factsheet](https://kraneshares.com/resources/factsheet/kgrn_factsheet.pdf) | passive/index-tracking classification and index methodology | Factsheet accessed `2026-07-24`; MSCI China IMI Environment 10/40 Index |
| `NYSE Arca:KGRN` | [KraneShares KGRN annual shareholder report](https://kraneshares.com/resources/compliance/2025_05_28_kgrn_annual.TSR.report.pdf) | formal principal listing and fiscal-year context | Report period ended `2025-03-31`; principal exchange `NYSE Arca`; fiscal-year NAV return `27.07%` not used as calendar-year data |
| `NYSE Arca:KGRN` | [KraneShares KGRN listing announcement](https://kraneshares.com/kraneshares-msci-china-environment-etf-ticker-kgrn-lists-on-the-new-york-stock-exchange/) | original listing and index-objective cross-check | Launch/listing announcement; former name and index objective disclosed |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### KGRN Raw Observations And Calculations

| Period | KGRN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not disclosed; incomplete inception year | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed; fiscal-year observation not calendar-comparable | 17.88% |
| 2026 YTD | -13.22% as of 2026-06-30 | not comparable; current year not cached |

- Available-period NAV TR: cumulative `7.53%`, official annualized `0.84%`, `2017-10-12` to `2026-06-30`.
- Actual years: `3,183 / 365.2425 = 8.714758`.
- Normalized endpoint: `100.00 × (1 + 0.0753) = 107.53`.
- Complete-calendar up/down count and best/worst year: not disclosed.

### KGRN Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, passive classification, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period and annual windows, benchmark cache, current-YTD dates, index/region links, stale-value replacement, filename/tags/breadcrumbs/link targets, and source-batch consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The sub-10-year history, normalized endpoint, unavailable calendar rows, fiscal-year/calendar distinction, exchange conflict, and current-YTD as-of date are explicitly disclosed.

## SMHC Sequential Queue Record

- Input row: `100/125`; input ticker: `SMHC`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `Nasdaq:SMHC`; VanEck's official launch release identifies the fund as `Nasdaq:SMHC`. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking China semiconductor equity ETF. VanEck states that SMHC tracks the MarketVector China Semiconductor 25 Index (`MVSMHCTR`) and its Q&A explicitly describes SMHC as passively managed. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: official inception `2026-06-23` means `10-year NAV TR unavailable`. The reviewed official product page shows SMHC fund NAV and market-price performance rows as `--` and does not disclose current fund NAV YTD. The underlying index's 1-month `20.18%` observation is not used as an ETF NAV TR proxy.
- Available-period window: `2026-06-23` to `2026-07-20`, `27 days / 0.073973 years`; start/end NAV TR values, cumulative return and CAGR are not disclosed. No value is inferred from the index or market price.
- Annual observations: 2016-2025 are not applicable before inception; 2026 YTD NAV TR is not disclosed. S&P 500 cached USD Total Return rows for 2016-2025 are shown separately only as a common benchmark reference.

### SMHC Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Nasdaq:SMHC` | [VanEck SMHC official product/performance page](https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/) | identity, passive/index-tracking objective, index, inception, expense and fund performance-field audit | Reviewed `2026-07-24`; inception `2026-06-23`; MarketVector China Semiconductor 25 Index; total expense ratio `0.65%`; fund NAV/market-price performance rows `--`; current NAV YTD not disclosed |
| `Nasdaq:SMHC` | [VanEck SMHC launch release](https://www.vaneck.com/us/en/press-releases/vaneck-launches-smhc-offering-pure-play-access-to-chinas-semiconductor-build-out/) | formal ticker/exchange, fund identity and new-fund risk cross-check | Release dated `2026-06-24`; Nasdaq: SMHC; exposure to 25 Chinese semiconductor companies; new-fund/no-active-market risk disclosed |
| `Nasdaq:SMHC` | [VanEck SMHC Q&A](https://www.vaneck.com/us/en/blogs/thematic-investing/smhc-etf-question-answer/) | passive classification and index cross-check | Reviewed `2026-07-24`; explicitly states SMHC is passively managed and tracks MVSMHCTR |
| `Nasdaq:SMHC` | [VanEck SMHC fund profile](https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/smhc-chinas-race-to-the-future-fund-profile.pdf) | inception, index ticker, fee and performance-field cross-check | Profile data as of `2026-03-31`; inception `2026-06-23`; index ticker `MVSMHCTR`; expense `0.65%`; return fields `-` because fund was new |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### SMHC Raw Observations And Calculations

| Period | SMHC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not applicable; before inception | 25.02% |
| 2025 | not applicable; before inception | 17.88% |
| 2026 YTD | not disclosed | not comparable; current year not cached |

- Available-period NAV TR: not disclosed for `2026-06-23` to `2026-07-20`; actual elapsed time is `27 / 365.2425 = 0.073973` years.
- No normalized endpoint, cumulative return, CAGR, up/down count or best/worst year is calculated because official start/end fund NAV TR values are not disclosed.
- The official underlying-index 1-month return `20.18%` is intentionally excluded from ETF performance calculations.

### SMHC Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, passive/index-tracking gate, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period and annual windows, benchmark cache, current-YTD disclosure, index/region links, filename/tags/breadcrumbs/link targets, no-proxy rule, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The verified new-fund identity, sub-10-year history, unavailable official fund NAV fields, non-use of the underlying-index proxy, S&P cache convention, and explicit no-CAGR gap are disclosed.

## FCA Sequential Queue Record

- Input row: `101/125`; input ticker: `FCA`; terminal status: `completed_10Y`.
- Canonical entity key: `Nasdaq:FCA`; First Trust's official product page, factsheet and summary prospectus identify the primary listing as Nasdaq. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking China equity ETF. First Trust states that FCA seeks to track the equity index Nasdaq AlphaDEX China Index (`NQDXCNN`), and the official prospectus describes the fund as an exchange-traded index fund. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: official inception `2011-04-18` and the First Trust monthly performance report provide a genuine `10.00` elapsed-year NAV TR window from `2016-06-30` to `2026-06-30`. Official rolling 10-year NAV TR CAGR is `8.19%`; raw rolling start/end NAV TR values are not disclosed.
- Rolling-window calculation: normalized start `100.00`; implied normalized end `100 × (1 + 0.0819)^10 = 219.72`. This is derived from the official CAGR and is not presented as a raw endpoint.
- Official current YTD: NAV TR `-1.23%` as of `2026-06-30`; market-price YTD `-1.27%` is kept separate and is not used as the primary metric.
- Official calendar NAV TR observations from the May 2026 summary prospectus: 2016 `-4.96%`, 2017 `58.35%`, 2018 `-17.87%`, 2019 `17.34%`, 2020 `13.58%`, 2021 `-1.18%`, 2022 `-17.10%`, 2023 `-9.32%`, 2024 `15.43%`, 2025 `42.95%`. These compound to `101.92%` / CAGR `7.28%`; 2021-2025 compounds to `22.58%` / CAGR `4.16%`.
- Source conflict: the First Trust factsheet as of `2025-12-31` shows 2024 `14.98%` and 2025 `43.51%`, while the annual shareholder report and May 2026 summary prospectus show 2025 `42.95%`. The annual report/summary-prospectus values are used for the durable annual table because they are the formal reporting documents; the conflict is retained rather than smoothed.

### FCA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Nasdaq:FCA` | [First Trust FCA official product/performance page](https://www.ftportfolios.com/Retail/etf/ETFsummary.aspx?Ticker=FCA) | identity, objective, index, listing, inception, expense, current fund data and performance fields | Page reviewed `2026-07-26`; Nasdaq; inception `2011-04-18`; index Nasdaq AlphaDEX China Index; total expense `0.80%`; current page performance capture includes 2026-06-30 NAV TR YTD `-1.23%` and 10Y `8.19%` |
| `Nasdaq:FCA` | [First Trust FCA factsheet](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=091b3012-692d-4750-966f-8e1e69ce35bf) | passive/index objective, listing, inception, index, fee, annual-row cross-check and index-change note | Factsheet as of `2025-12-31`; Nasdaq; inception `2011-04-18`; expense `0.80%`; factsheet rows conflict with formal report for 2024/2025 and are not chosen for the durable annual table |
| `Nasdaq:FCA` | [First Trust monthly performance report](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b363655b-cc73-4f42-a7b1-4c1e00306c7c) | current NAV TR YTD, rolling 10Y NAV TR and market-price separation | Returns as of `2026-06-30`; NAV YTD `-1.23%`; NAV 10Y `8.19%`; market-price YTD `-1.27%`; tracked-index 10Y `9.38%` |
| `Nasdaq:FCA` | [FCA May 2026 summary prospectus](https://www.sec.gov/Archives/edgar/data/1510337/000144554626003311/fca_497k.htm) | formal calendar-year NAV rows, 10Y annualized return, inception and current-index change | Prospectus dated `2026-05-01`; calendar NAV rows 2016-2025; 10Y return as of `2025-12-31` `7.28%`; inception `2011-04-18`; index changed `2015-07-14` |
| `Nasdaq:FCA` | [FCA 2025 annual shareholder report](https://www.sec.gov/Archives/edgar/data/1510337/000144554626001916/adex2_ncsr.htm) | formal annual-report cross-check for 2025 total return and fund costs | Period ended `2025-12-31`; NAV return `42.95%`; cost example expense ratio `0.80%` excluding extraordinary expenses |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used for annual comparison |

### FCA Raw Observations And Calculations

| Period | FCA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -4.96% | 11.96% |
| 2017 | 58.35% | 21.83% |
| 2018 | -17.87% | -4.38% |
| 2019 | 17.34% | 31.49% |
| 2020 | 13.58% | 18.40% |
| 2021 | -1.18% | 28.71% |
| 2022 | -17.10% | -18.11% |
| 2023 | -9.32% | 26.29% |
| 2024 | 15.43% | 25.02% |
| 2025 | 42.95% | 17.88% |
| 2016-2025 compound / CAGR | 101.92% / 7.28% | 298.33% / 14.82% |
| 2021-2025 compound / CAGR | 22.58% / 4.16% | 96.17% / 14.43% |
| 2026 YTD | -1.23% as of 2026-06-30 | not comparable; current year not cached |

- 10-year rolling NAV TR CAGR: `8.19%` for `2016-06-30` to `2026-06-30`.
- Actual elapsed years: `(2026-06-30 − 2016-06-30) / 365.2425 = 10.000000` years.
- CAGR formula: `(end TR value / start TR value)^(1 / actual years) − 1`; raw endpoint values are not disclosed, so the official CAGR is primary and `219.72` is an implied normalized endpoint only.
- 2016-2025 up/down count: `5 / 5`; best `2017 +58.35%`; worst `2022 -17.10%`.
- 10-year rolling comparison versus S&P 500 TR: FCA `8.19%` versus S&P 500 TR `14.82%`, a `-6.63` percentage-point difference. The annual-row CAGR is a separate calendar window and is not substituted for the rolling 10-year figure.

### FCA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, passive/index-tracking gate, inception/10Y audit, NAV TR/reinvestment/expense basis, raw-endpoint disclosure, annual NAV rows, S&P cache, current-YTD dates, index-change caveat, index/region links, conflict disclosure, filename/tags/breadcrumbs/link targets, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The separate rolling and calendar windows, raw-endpoint gap, factsheet/report annual-row conflict, index-change break, market-price separation, and current-YTD as-of date are explicitly disclosed.

## IND Sequential Queue Record

- Input row: `102/125`; input ticker: `IND`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `Nasdaq:IND`; the DWS prospectus and Nasdaq listing alert identify the Xtrackers Nifty 500 India ETF on Nasdaq. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking India equity ETF. DWS states that the fund uses a passive/indexing approach to track the Nifty 500 Index, an equity index covering large-, mid- and small-cap companies traded on India's NSE. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: official inception is `2025-11-24` on the Q1 factsheet; DWS launch/Nasdaq listing and the first holdings report identify listing/commencement on `2025-11-25`. Either date confirms a history far shorter than 10 years. `10-year NAV TR unavailable`.
- Latest official performance observation: the Q1 factsheet reports 3-month NAV TR `-18.41%` through `2026-03-31`; the factsheet does not disclose raw start/end NAV TR values or an inception-to-date cumulative result. Actual 3-month date window is `2025-12-31` to `2026-03-31`, `90 days / 0.246412 years`.
- No CAGR is calculated from the rounded 3-month snapshot, and the value is not relabelled as current 2026 YTD. Current NAV TR YTD through the current review date is `not disclosed` in the reviewed official sources.
- Annual observations: no complete calendar-year NAV TR table is available. 2025 is an incomplete inception year and is marked not disclosed; 2026 YTD is not disclosed.

### IND Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Nasdaq:IND` | [DWS Xtrackers IND Q1 2026 factsheet](https://etf.dws.com/download/asset/048952ad-b7d4-462d-95c8-e726ff2484bd) | fund identity, passive/index classification, index, inception, fee, latest official performance snapshot and holdings | Factsheet as of `2026-03-31`; ticker IND; Nifty 500 Index; inception `2025-11-24`; 3-month NAV TR `-18.41%`; 499 holdings; net/gross expense `0.19%` |
| `Nasdaq:IND` | [DWS launch release](https://www.dws.com/en-us/about-us/media/media-releases/xtrackers-by-dws-launches-nifty-500-india-etf-nasdaq-ind/) | formal launch date, ticker/exchange, index objective and fee cross-check | Release dated `2025-11-24`; Nasdaq trading begins `2025-11-25`; Nifty 500 Index; net/gross expense `0.19%` |
| `Nasdaq:IND` | [SEC/DBX ETF Trust prospectus and SAI](https://www.sec.gov/Archives/edgar/data/1503123/000008805325000603/dbxetf-20250531.htm) | formal passive strategy, listing, expenses and no-prior-performance disclosure | Prospectus dated `2025-07-29`; Nasdaq; passive/indexing approach; total annual fund operating expenses `0.19%`; no performance reported because fund had not commenced operations at prospectus date |
| `Nasdaq:IND` | [Nasdaq IND listing alert](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETP2025-204) | exchange-level ticker and commencement cross-check | Alert dated `2025-11-24`; listing effective `2025-11-25`; daily valuation dissemination begins `2025-11-25` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 not used |

### IND Raw Observations And Calculations

| Period | IND NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016-2024 | not applicable; fund had not launched | cached reference rows available separately |
| 2025 | not disclosed; incomplete inception year | 17.88% |
| 2025-12-31 to 2026-03-31 | -18.41% official 3-month NAV TR snapshot | not comparable to this short fund observation |
| 2026 YTD | not disclosed | not comparable; current year not cached |

- Available-period observation: official 3-month cumulative NAV TR `-18.41%`; raw endpoints are not disclosed.
- Actual years for the disclosed 3-month observation: `90 / 365.2425 = 0.246412` years.
- No normalized endpoint, inception-to-date cumulative return, CAGR, up/down count or best/worst year is calculated because the issuer does not disclose compatible inception-to-date NAV TR endpoints or a complete annual table.
- The official Q1 3-month return is kept distinct from current YTD, and no market-price return is substituted.

### IND Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, passive/index-tracking gate, inception/10Y audit, NAV TR/reinvestment/expense basis, short-period labeling, raw-endpoint disclosure, annual/YTD gaps, S&P cache, index/region links, filename/tags/breadcrumbs/link targets, no-proxy/no-annualization rule, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The inception/listing-date distinction, short-period result, unavailable inception-to-date and current-YTD fields, no-CAGR decision, and new-fund gap are explicitly disclosed.

## VNAM Sequential Queue Record

- Input row: `103/125`; input ticker: `VNAM`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:VNAM`; Global X's product page and SEC summary prospectus identify the primary exchange. No provider slug or guessed exchange is used.
- Type-gate result: supported passive/index-tracking Vietnam equity ETF. The SEC prospectus states that the adviser uses an indexing approach, generally replicates the `MSCI Vietnam Select 25-50 Index`, and does not attempt to outperform it. The fund is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy ETF.
- Mandatory 10-year audit: official inception `2021-12-07`; latest reviewed month-end is `2026-06-30`, only `4.561259` elapsed years. `10-year NAV TR unavailable`.
- Official available-period observations: Global X reports Fund NAV total-return performance, annualized, of `45.10%` for 1Y, `15.86%` for 3Y, and `0.34%` since inception, all as of `2026-06-30`. The page defines performance as total return with gross income reinvested where applicable and separates cumulative from annualized return. Raw start/end NAV TR values are not disclosed, so no independent cumulative result or CAGR is derived.
- Current NAV TR YTD through the review date is `not disclosed` in the reviewed official capture. The official product page's latest performance table has no YTD column. A Schwab secondary page was reviewed but its visible table was stale as of `2025-10-31`, so it was not used to fill the current-YTD gap.
- Annual observations: no complete calendar-year NAV TR rows were available in the reviewed official capture. 2021 is an incomplete inception year; 2022-2025 remain `not disclosed`. No up/down count or best/worst ranking is inferred.
- Risk observations used in the page: total expense ratio `0.51%`; 70 holdings; sector exposure as of `2026-06-30` of real estate `32.1%` and financials `29.2%`; largest holding `23.61%` as of `2026-07-17`; standard deviation `24.40%` as of `2026-06-30`.

### VNAM Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:VNAM` | [Global X VNAM official product/performance page](https://www.globalxetfs.com/funds/vnam?download_full_holdings=true) | identity, objective, index, inception, expense, official NAV TR, holdings, exposure and risk statistics | Page reviewed `2026-07-26`; primary exchange `NYSE Arca`; inception `2021-12-07`; expense `0.51%`; performance table as of `2026-06-30`: NAV 1Y `45.10%`, 3Y `15.86%`, since inception `0.34%`; performance basis is total return with gross income reinvested where applicable |
| `NYSE Arca:VNAM` | [SEC 2026 Summary Prospectus](https://www.sec.gov/Archives/edgar/data/1432353/000143235326000195/a497kmscivietnam.htm) | formal exchange, passive/indexing approach, index strategy, expenses, methodology and risk cross-check | Prospectus dated `2026-03-01`; ticker/exchange `VNAM / NYSE Arca`; total annual fund operating expenses `0.51%`; indexing approach and replication/representative-sampling language; index/name-methodology change effective `2023-12-01` |
| `NYSE Arca:VNAM` | [Global X launch article](https://www.globalxetfs.com/articles/introducing-the-global-x-msci-vietnam-etf-vnam) | listing-date cross-check | Launch article states NYSE Arca listing on `2021-12-09`; retained as a listing-date distinction from product-page inception `2021-12-07` |
| `NYSE Arca:VNAM` | [Schwab VNAM performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=vnam) | secondary current-YTD check | Reviewed `2026-07-26`; visible performance table is as of `2025-10-31`, so it is stale and not used for current YTD |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 current YTD not used |

### VNAM Raw Observations And Calculations

| Period | VNAM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016-2020 | not applicable; before inception | cached reference rows available separately |
| 2021 | not disclosed; incomplete inception year | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | not disclosed | not comparable; current year not cached |

- Actual elapsed years: `(2026-06-30 − 2021-12-07) / 365.25 = 4.561259` years (`1666` days).
- The official since-inception annualized NAV TR is `0.34%`; raw endpoints are not disclosed. No normalized endpoint, endpoint-derived CAGR, short-period annualization, or proxy is created.
- The official 1Y and 3Y NAV TR values are annualized observations, not complete calendar-year rows. They are kept separate from the S&P 500 cached calendar-year convention and are not presented as same-window S&P comparisons.

### VNAM Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: row/order, canonical exchange, exact fund identity, passive/index-tracking gate, inception/10Y audit, NAV TR/reinvestment/expense basis, annualized-versus-cumulative labels, raw-endpoint disclosure, annual/YTD gaps, S&P cache, index/region links, filename/tags/breadcrumbs/link targets, stale-secondary rejection, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The inception/listing-date distinction, short history, official annualized available-period figures, raw-endpoint gap, unavailable annual rows/current YTD, stale secondary page, and no-proxy/no-CAGR decision are explicitly disclosed.

## ISAGF Sequential Queue Record

- Input row: `104/125`; input ticker: `ISAGF`; terminal status: `unsupported ETF type`.
- Canonical entity key: `LSE:IGEA`. The input is an OTC alias. iShares' official listing table maps ISIN `IE00B6QGFW01` to London Stock Exchange ticker `IGEA` in USD; the same share class is also cross-listed on Xetra, SIX and Bolsa Mexicana. The USD LSE line is retained as the canonical exchange-qualified key; `OTC:ISAGF` is not used as the durable key.
- Type-gate result: unsupported. iShares identifies the fund as `iShares Emerging Asia Local Govt Bond UCITS ETF`, with asset class `Fixed Income`, objective to track an index of local-currency government bonds from Asian emerging-market countries, and benchmark `BBG EM Asia Local Currency Govt Country Cap NET Index`. The product is passive, but it is a bond ETF rather than a passive/index-tracking equity ETF, so it is outside scope.
- Official factsheet/page observations: share-class launch `2012-03-02`; total expense ratio `0.50%`; use of income `Distributing`; physical, sampled methodology; official page data as of `2026-07-21` show 156 holdings and 3-year standard deviation `8.22%`. These figures are recorded only as classification evidence; no NAV TR performance analysis is created.
- No 10-year NAV TR calculation, annual return table, current YTD comparison, S&P 500 comparison, performance page, region page update or performance-index row is applicable after the bond type gate.

### ISAGF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:IGEA` | [iShares official product page / listings](https://www.ishares.com/ch/professionals/en/products/251723/ishares-emerging-asia-local-government-bond-ucits-etf) | identity, ISIN, asset class, objective, benchmark, expenses, methodology and exchange-qualified alias resolution | Page reviewed `2026-07-26`; ISIN `IE00B6QGFW01`; asset class `Fixed Income`; LSE USD ticker `IGEA`; share-class launch `2012-03-02`; TER `0.50%`; LSE/Xetra/SIX/Mexico listings; holdings as of `2026-07-21` |
| `LSE:IGEA` | [iShares official UK product page](https://www.ishares.com/uk/individual/en/products/251723/ishares-emerging-asia-local-government-bond-ucits-etf) | issuer objective and fixed-income classification cross-check | Reviewed `2026-07-26`; objective is local-currency government bonds from Asian Emerging Market countries; asset class `Fixed Income`; issuing company `iShares III plc`; Bloomberg London ticker `SGEA LN` / page listing table separately identifies `IGEA` USD |
| `LSE:IGEA` | [iShares official March 2026 factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/sgea-ishares-emerging-asia-local-govt-bond-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) | share-class launch, passive bond objective, TER and issuer naming cross-check | Factsheet dated `2026-03`; ISIN `IE00B6QGFW01`; share-class launch `2012-03-02`; asset class `Fixed Income`; TER `0.50%`; iShares III plc; objective is Asian emerging-market government bonds |
| `LSE:IGEA` | [iShares official KIID](https://www.ishares.com/uk/individual/en/literature/kiid/ucits_kiid-ishares-emerging-asia-local-govt-bond-ucits-etf-usd-dist-gb-ie00b6qgfw01-en.pdf?siteEntryPassthrough=true&switchLocale=y) | legal product and passive fixed-income wording | KIID dated `2026-04-09`; ISIN `IE00B6QGFW01`; sub-fund of iShares III plc; passively managed; invests in fixed-income securities such as bonds |

### ISAGF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue order, exact OTC-alias resolution, official exchange listing, fund identity, asset-class/type gate, issuer objective, benchmark, fee, return-basis separation, source dates, no-performance-page rule for unsupported products, and ledger/source-batch/log consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The official fixed-income classification and government-bond objective are sufficient to stop before performance analysis; no equity NAV TR, CAGR, YTD or proxy value is inferred.

## FLIBF Sequential Queue Record

- Input row: `105/125`; input ticker: `FLIBF`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `LSE:FLXI`. The input is an OTC alias. Franklin's official June 2026 factsheet maps ISIN `IE00BHZRQZ17` to the USD London Stock Exchange ticker `FLXI`; `FRIN` is the separate GBP London line, while other EUR/CHF lines are also cross-listed. The USD LSE line is retained as the canonical exchange-qualified key.
- Type-gate result: supported passive/index-tracking India equity ETF. Franklin identifies the ETF as `Indexed`, physical and full replication, investing in medium- and large-capitalisation Indian equities and targeting the `FTSE India 30/18 Capped Index-NR`. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy fund.
- Mandatory 10-year audit: official fund inception `2019-06-25`; the latest official factsheet performance date is `2026-06-30`, only `7.014374` elapsed years. The official 10-year field is unavailable; `10-year NAV TR unavailable`.
- Latest official performance: Franklin's June 2026 factsheet reports USD NAV total returns of YTD `-8.42%`, 1-month `1.16%`, 3-month `9.66%`, 1-year `-10.72%`, 3-year cumulative `20.28%`, 5-year cumulative `29.22%`, and since-inception cumulative `64.43%` / average annual `7.35%`, all as of `2026-06-30`. Raw start/end NAV TR values are not disclosed.
- Annual observations: official complete calendar NAV rows are `2020-2025`: `12.48%`, `24.89%`, `-7.89%`, `22.37%`, `10.61%`, `2.63%`. 2019 is a partial inception year and is excluded from up/down ranking. Rounded-row compound for 2020-2025 is `79.74%` / CAGR `10.27%`; S&P 500 cached comparison is `132.26%` / `15.08%`.
- Current NAV is `US$41.63` as of `2026-07-07`; this is a NAV observation, not a return. The earlier May 2026 product-page snapshot showed YTD `-9.47%` and inception cumulative `62.54%`; the newer June 2026 factsheet is used for the durable current snapshot and the as-of difference is retained as a source-date refresh, not blended.

### FLIBF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:FLXI` | [Franklin Templeton official June 2026 factsheet](https://www.franklintempletonoffshore.com/download/en-os/factsheet/eb953849-e3ab-40a6-b777-15a7ba704486/Factsheet-FranklinFTSEIndiaUCITSETF-27853-FF-NRC-en-OS.PDF) | USD/LSE ticker mapping, fund identity, indexed equity classification, inception, benchmark, TER, annual rows, YTD and available-period NAV TR | Factsheet as of `2026-06-30`; ISIN `IE00BHZRQZ17`; LSE `FLXI` USD; inception `2019-06-25`; benchmark FTSE India 30/18 Capped Index-NR; physical/full replication; cumulative inception `64.43%`; average annual inception `7.35%`; YTD `-8.42%`; TER `0.19%` |
| `LSE:FLXI` | [Franklin Templeton official product/performance page](https://www.franklintempleton.co.uk/our-funds/etf/price-and-performance/products/27853/SINGLCLASS/franklin-ftse-india-ucits-etf/IE00BHZRQZ17) | current identity/NAV, indexed equity classification and official month-end performance cross-check | Page reviewed `2026-07-26`; current NAV `US$41.63` as of `2026-07-07`; page's latest standardized month-end table is as of `2026-05-31` and shows YTD `-9.47%`, inception cumulative `62.54%`, and 10-year `—`; newer June factsheet is chosen for durable current performance |
| `LSE:FLXI` | [Franklin Templeton official KIID](https://www.franklintempleton.co.uk/download/en-gb/KIID/36ada32a-c060-4f7d-87ad-83346b67d733/KIID_IE00BHZRQZ17_en_GB.pdf) | objective, accumulating share class and index-tracking policy | KIID for ISIN `IE00BHZRQZ17`; fund is a sub-fund of Franklin Templeton ICAV; accumulating USD share class and objective to track the FTSE India 30/18 Capped Index-NR |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 current YTD not used |

### FLIBF Raw Observations And Calculations

| Period | FLIBF / FLXI NAV TR | S&P 500 TR |
|---|---:|---:|
| 2019† | not disclosed; partial inception year | 31.49% |
| 2020 | 12.48% | 18.40% |
| 2021 | 24.89% | 28.71% |
| 2022 | -7.89% | -18.11% |
| 2023 | 22.37% | 26.29% |
| 2024 | 10.61% | 25.02% |
| 2025 | 2.63% | 17.88% |
| 2026 YTD | -8.42% as of 2026-06-30 | not comparable; current year not cached |

- Actual available-period years: `(2026-06-30 − 2019-06-25) / 365.25 = 7.014374` years (`2562` days).
- Issuer available-period result: cumulative `64.43%`; average annual `7.35%`. Using the rounded cumulative figure, `(1 + 0.6443)^(1 / 7.014374) − 1 = 7.35%` approximately; raw NAV endpoints remain not disclosed.
- Complete calendar-year rows `2020-2025` compound to `79.74%` / CAGR `10.27%`; S&P 500 TR compounds to `132.26%` / CAGR `15.08%` over the same six complete years. For `2021-2025`, ETF `59.80%` / `9.83%` versus S&P `96.17%` / `14.43%`.

### FLIBF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, OTC-alias and USD-share-class resolution, canonical exchange, exact fund identity, passive/indexing gate, inception/10Y audit, NAV TR/expense/currency basis, annual rows, current-YTD and NAV as-of dates, S&P cache, index/region links, filename/tags/breadcrumbs/link targets, source-date conflict handling, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The USD LSE line versus GBP/EUR/CHF cross-listings, shorter-than-10-year history, partial inception year, latest June-vs-May source refresh, raw-endpoint gap, and no-proxy/no-10Y relabelling rule are explicitly disclosed.

## IHRPF Sequential Queue Record

- Input row: `106/125`; input ticker: `IHRPF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:FXC`. The input is an OTC alias. iShares' official trading-information table maps ISIN `IE00B02KXK85` to ticker `FXC` on the London Stock Exchange in USD; the same fund is cross-listed in other currencies/exchanges. The USD LSE line is retained as the durable key; no OTC/provider slug is used.
- Type-gate result: supported passive/index-tracking China equity ETF. iShares identifies the asset class as Equity, physical replication, distributing share class, 50 holdings, and benchmark `FTSE China 50 Index - USD Net Div (USD)`. The product is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy ETF.
- Mandatory 10-year audit: official rolling window `2016-06-30` to `2026-06-30` equals `10.00` elapsed years. `10-year NAV TR available`.
- Official rolling result: NAV Total Return cumulative `18.61%`, annualized/CAGR `1.72%`, current NAV TR YTD `-17.31%`, all from the current iShares performance page as of `2026-06-30`. iShares states that performance is on a NAV basis with gross income reinvested where applicable.
- Endpoint disclosure: raw start/end TR values are not disclosed. The page reports the official cumulative return and CAGR, shows the dates and actual years, and leaves both endpoint values as `not disclosed`; no normalized endpoint is invented.
- Official annual observations: iShares factsheet rows for `2016-2025` are `1.80%`, `34.51%`, `-12.39%`, `13.76%`, `10.06%`, `-20.70%`, `-20.01%`, `-13.57%`, `31.03%`, `28.16%`. Current iShares page confirms the same series rounded to one decimal as of `2026-06-30`; the two-decimal rows are retained from the official factsheet dated `2026-03-31`.
- Calculations from complete calendar rows: 2016-2025 ETF NAV TR cumulative `38.28%` / CAGR `3.29%`; 2021-2025 ETF NAV TR cumulative `-7.93%` / CAGR `-1.64%`. S&P 500 cached USD Total Return for 2021-2025 compounds to `96.17%` / CAGR `14.43%`; ETF gap is approximately `-16.07` percentage points.
- Structural source caveat: iShares states that the benchmark changed from FTSE China 25 to FTSE China 50 effective at the close of `2014-09-19`; this benchmark splice is disclosed and no pre-change proxy is created.

### IHRPF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:FXC` | [iShares official product/performance page](https://www.ishares.com/ch/individual/en/products/251798/ishares-china-large-cap-ucits-etf) | identity, USD/LSE alias resolution, asset class, objective, benchmark, NAV TR, current NAV and risk facts | Page reviewed `2026-07-26`; ISIN `IE00B02KXK85`; share-class launch `2004-10-21`; asset class Equity; physical; 50 holdings; TER `0.74%`; NAV TR rolling window and YTD as of `2026-06-30`; latest NAV `US$91.61` as of `2026-07-02` |
| `LSE:FXC` | [iShares official FXC factsheet](https://www.ishares.com/ch/professionals/en/literature/fact-sheet/fxc-ishares-china-large-cap-ucits-etf-fund-fact-sheet-en-ch-institutional.pdf) | exact annual NAV/benchmark rows, inception and listing table cross-check | Factsheet reviewed `2026-07-26`; annual rows as of `2026-03-31`; ticker `FXC` on LSE in USD; benchmark `FTSE China 50 Index - USD Net Div (USD)`; annual NAV rows `2016-2025` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 current YTD not used |

### IHRPF Raw Observations And Calculations

| Period | IHRPF / FXC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.80% | 11.96% |
| 2017 | 34.51% | 21.83% |
| 2018 | -12.39% | -4.38% |
| 2019 | 13.76% | 31.49% |
| 2020 | 10.06% | 18.40% |
| 2021 | -20.70% | 28.71% |
| 2022 | -20.01% | -18.11% |
| 2023 | -13.57% | 26.29% |
| 2024 | 31.03% | 25.02% |
| 2025 | 28.16% | 17.88% |
| 2026 YTD | -17.31% as of 2026-06-30 | not comparable; current year not cached |

- 10-year actual period: `(2026-06-30 − 2016-06-30) / 365.25 = 10.000000` years (`3652` days); official cumulative `18.61%` and CAGR `1.72%`. Raw start/end TR values are `not disclosed`.
- Complete calendar rows `2016-2025` compound to `38.28%` / CAGR `3.29%`; positive / negative years are `6 / 4`. Best `2017 +34.51%`; worst `2021 -20.70%`.
- Common `2021-2025` rows compound to `-7.93%` / CAGR `-1.64%`; S&P 500 TR compounds to `+96.17%` / CAGR `+14.43%` over the same five complete years.

### IHRPF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, OTC-alias and USD-share-class resolution, canonical exchange, exact fund identity, passive/indexing gate, inception/10Y audit, NAV TR/reinvestment/expense basis, endpoint disclosure, annual/YTD dates, S&P cache, benchmark-change disclosure, index/region links, filename/tags/breadcrumbs/link targets, no-proxy rule, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The USD LSE listing choice, factsheet-vs-current-page date separation, 10.00-year rolling window, undisclosed endpoint levels, benchmark splice, raw return basis, and no-market-price-proxy rule are explicitly disclosed.

## FLCH Sequential Queue Record

- Input row: `107/125`; input ticker: `FLCH`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:FLCH`. Franklin's official product page and SEC summary prospectus identify the ticker and primary listing exchange; no guessed exchange or provider slug is used.
- Type-gate result: supported passive/index-tracking China equity ETF. Franklin classifies the ETF as `Indexed`, with physical index exposure to large- and mid-cap Chinese equities and objective to track the `FTSE China RIC Capped Index` / `FTSE China Capped Index-NR`. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy ETF.
- Mandatory 10-year audit: official fund inception `2017-11-02`; latest complete official month-end `2026-06-30` is only `8.657084` elapsed years (`3162` days). The official 10-year field is `—`; `10-year NAV TR unavailable`.
- Official available-period result: Franklin's June 2026 factsheet reports NAV total-return average annual `-0.24%` since inception through `2026-06-30`. Raw start/end NAV TR values and cumulative inception NAV TR are not disclosed, so no cumulative proxy or endpoint-derived CAGR is invented.
- Return basis: Franklin states total returns assume reinvestment of all distributions and deduction of all fund expenses. The product page separately shows the latest current NAV TR YTD `-10.65%` as of `2026-07-10`; the factsheet's month-end YTD is `-13.94%` as of `2026-06-30`, and the two source dates are not blended.
- Official annual observations: NAV rows for complete calendar years `2018-2025` are `-18.28%`, `22.92%`, `30.60%`, `-21.04%`, `-22.25%`, `-11.98%`, `19.17%`, `31.61%`. 2017 is a partial inception year and is excluded from rankings.
- Calculations from complete calendar rows: 2018-2025 ETF NAV TR cumulative `11.18%` / CAGR `1.33%`; 2021-2025 ETF NAV TR cumulative `-15.25%` / CAGR `-3.25%`. S&P 500 cached USD Total Return for 2021-2025 compounds to `96.17%` / CAGR `14.43%`; ETF gap is approximately `-17.68` percentage points.

### FLCH Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FLCH` | [Franklin official product/performance page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26362/SINGLCLASS/franklin-ftse-china-etf/FLCH) | identity, listing, indexed equity classification, objective, benchmark, inception, fees, current NAV/YTD and portfolio risk | Page reviewed `2026-07-26`; ticker `FLCH`; exchange `NYSE Arca`; inception `2017-11-02`; benchmark `FTSE China Capped Index-NR`; gross/net expense `0.19%`; current YTD NAV TR `-10.65%` as of `2026-07-10`; NAV `US$21.16` as of `2026-07-10` |
| `NYSE Arca:FLCH` | [Franklin official June 2026 factsheet](https://www.franklintempleton.com/forms-literature/download/FLCH-FF) | NAV TR basis, available-period return, annual NAV/benchmark rows, holdings and sector observations | Factsheet as of `2026-06-30`; NAV average annual inception `-0.24%`; NAV YTD `-13.94%`; annual NAV rows `2018-2025`; total returns reinvest distributions and deduct fund expenses; holdings/sector snapshot as of `2026-06-30` |
| `NYSE Arca:FLCH` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1655589/000137949118006818/filing173807320.htm) | formal exchange and passive investment-goal cross-check | Prospectus identifies `FLCH` on `NYSE Arca` and objective to track the FTSE China RIC Capped Index |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 current YTD not used |

### FLCH Raw Observations And Calculations

| Period | FLCH NAV TR | S&P 500 TR |
|---|---:|---:|
| 2017† | not disclosed; partial inception year | 21.83% |
| 2018 | -18.28% | -4.38% |
| 2019 | 22.92% | 31.49% |
| 2020 | 30.60% | 18.40% |
| 2021 | -21.04% | 28.71% |
| 2022 | -22.25% | -18.11% |
| 2023 | -11.98% | 26.29% |
| 2024 | 19.17% | 25.02% |
| 2025 | 31.61% | 17.88% |
| 2026 YTD | -10.65% as of 2026-07-10; factsheet month-end -13.94% as of 2026-06-30 | not comparable; current year not cached |

- Available-period actual years: `(2026-06-30 − 2017-11-02) / 365.25 = 8.657084` years (`3162` days). Official average annual NAV TR is `-0.24%`; raw endpoints and cumulative inception NAV TR are `not disclosed`.
- Complete calendar rows `2018-2025` compound to `+11.18%` / CAGR `+1.33%`; positive / negative years are `4 / 4`. Best `2025 +31.61%`; worst `2022 -22.25%`.
- Common `2021-2025` rows compound to `-15.25%` / CAGR `-3.25%`; S&P 500 TR compounds to `+96.17%` / CAGR `+14.43%` over the same five complete years.

### FLCH Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, canonical exchange, exact fund identity, passive/indexing gate, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period labeling, partial-year handling, current-YTD and factsheet as-of separation, S&P cache, index/region links, filename/tags/breadcrumbs/link targets, no-proxy/no-annualization rule, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The 8.657084-year history, official unavailable 10-year field, annualized-versus-cumulative distinction, June month-end versus July current-YTD refresh, partial 2017 year, raw-endpoint gap, and no-market-price-proxy rule are explicitly disclosed.

## KPHO Sequential Queue Record

- Input row: `108/125`; input ticker: `KPHO`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE:KPHO`. KraneShares' current product page and March 2026 annual shareholder report identify the primary exchange as `NYSE`; an October 2025 summary prospectus says `NYSE Arca`. The latest issuer page/report are used for the canonical key and the official exchange conflict is disclosed; no guessed exchange or provider slug is used.
- Type-gate result: supported passive/index-tracking Vietnam equity ETF. The prospectus says the fund seeks to correspond generally to the Dragon Capital MerQube Vietnam Growth Index, invests at least 80% in index securities/economic equivalents, and the issuer describes the strategy as an indexed Vietnam equity ETF. The index uses rules-based market-capitalization, liquidity and growth/fundamental screens; this is not an active discretionary fund. The current portfolio is equity/foreign-ETF exposure, not bond, commodity, currency trust, multi-asset, leveraged, inverse, option-income or derivative-heavy exposure.
- Mandatory 10-year audit: official inception `2025-12-02`; latest official month-end `2026-06-30` is only `0.574949` elapsed years (`210` days). `10-year NAV TR unavailable` and there is no complete calendar year.
- Official available-period result: KraneShares reports cumulative Fund NAV TR `-4.05%` from inception through `2026-06-30`; raw start/end NAV TR values are not disclosed. Because the period is under one year, no CAGR or annualized return is calculated.
- Current official NAV TR YTD is `-2.52%` as of `2026-06-30`; latest daily NAV is `US$21.46` as of `2026-07-23`. Market-price return is kept separate (`-5.01%` since inception and `-4.51%` YTD in the issuer table) and is not used as the NAV metric.
- Annual observations: no complete calendar-year NAV TR rows are available. The 2025 inception/operations period is partial and 2026 is an incomplete current year; no best/worst annual ranking is inferred.
- S&P 500 comparison: cached complete-calendar S&P rows are not a compatible same-window comparison for the sub-one-year KPHO history; no proxy or short-period annualization is created.
- Structural caveat: the factsheet reports `DCVFMVN DIAMOND ETF` at `24.01%` of holdings as of `2026-06-30`, and the prospectus notes that the fund may use other investment companies and derivatives within its tracking portfolio. This is recorded as an implementation/tracking risk, not classified as derivative-heavy based on the reviewed portfolio and index mandate.

### KPHO Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE:KPHO` | [KraneShares official product/performance page](https://kraneshares.com/etf/kpho/) | current identity, primary exchange, index, inception, expenses, NAV, NAV TR/YTD, portfolio and implementation | Page reviewed `2026-07-26`; primary exchange `NYSE`; inception `2025-12-02`; total annual operating expense `1.03%`; index `Dragon Capital MerQube Vietnam Growth Index`; NAV `US$21.46` as of `2026-07-23`; NAV TR YTD `-2.52%` and since-inception `-4.05%` as of `2026-06-30` |
| `NYSE:KPHO` | [KraneShares official factsheet](https://kraneshares.com/resources/factsheet/kpho_factsheet.pdf) | indexed-equity description, expense, inception, holdings, official NAV TR and underlying-index rows | Factsheet reviewed `2026-07-26`; data as of `2026-06-30`; primary exchange `NYSE`; inception `2025-12-02`; 38 holdings; DCVFMVN Diamond ETF `24.01%`; Fund NAV TR YTD/since inception `-2.52%` / `-4.05%` |
| `NYSE:KPHO` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1547576/000182912625008303/kraneshares_497k.htm) | formal objective, passive/index strategy, 80% policy, implementation and exchange cross-check | Prospectus dated `2025-10-20`; principal listing says `NYSE Arca`; current index is Dragon Capital MerQube Vietnam Growth Index; 80% policy; up to 20% may include other investments/derivatives/ETFs; total expenses `1.03%` including acquired-fund fees/expenses `0.24%` |
| `NYSE:KPHO` | [KraneShares annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_kpho_annual.TSR.report.pdf) | historical return and exchange cross-check | Report for period from commencement `2025-12-03` to `2026-03-31`; principal listing `NYSE`; NAV return `-5.25%` since commencement; not used for current month-end because newer June factsheet is available |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 current YTD not used |

### KPHO Raw Observations And Calculations

| Period | KPHO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2025† | not disclosed; partial inception/operations period | 17.88% (not comparable) |
| 2026 YTD | -2.52% as of 2026-06-30 | not comparable; current year not cached |
| Since inception | -4.05% cumulative as of 2026-06-30 | not comparable |

- Available-period actual years: `(2026-06-30 − 2025-12-02) / 365.25 = 0.574949` years (`210` days). No CAGR or annualized return is calculated because the period is under one year.
- Complete calendar-year up/down count, best year, worst year and annual CAGR: `not applicable`; no complete calendar year exists.
- The annual report's `-5.25%` NAV return from commencement `2025-12-03` to `2026-03-31` is retained as a source-date cross-check only, not blended with the June 2026 month-end result.

### KPHO Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, canonical exchange and conflict resolution, exact fund identity, passive/indexing gate, inception/10Y audit, NAV TR/reinvestment/expense basis, under-one-year no-annualization rule, partial-period handling, current-YTD/NAV dates, S&P cache, implementation risk, index/region links, filename/tags/breadcrumbs/link targets, no-proxy rule, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The NYSE-versus-NYSE-Arca source conflict, 0.574949-year history, official cumulative-only available-period result, no annual table, separate market-price return, acquired-fund/ETF implementation, and no-CAGR/no-proxy decision are explicitly disclosed.

## INQQ Sequential Queue Record

- Input row: `109/125`; input ticker: `INQQ`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:INQQ`. SEC summary prospectus, factsheet and annual shareholder report identify `NYSE Arca` as the principal listing exchange. The EMQQ Global current materials page and factsheet marketing text also display `NYSE`; this conflict is retained and the formal prospectus/report listing is used for the durable key.
- Type-gate result: supported passive/index-tracking non-diversified India internet/e-commerce equity ETF. The SEC objective is to correspond generally to the price and yield performance of the `INQQ The India Internet Index`; the fund invests in index securities or depositary receipts and uses a rules-based eligibility/liquidity/market-cap process. It is not a bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income or derivative-heavy ETF.
- Mandatory 10-year audit: official inception `2022-04-05`; latest official numeric static performance is as of `2026-03-31`, `3.986311` elapsed years (`1456` days). `10-year NAV TR unavailable`.
- Official available-period result: the March 2026 factsheet reports NAV average annual since-inception return `-7.83%`; the raw start/end NAV TR values and cumulative endpoint level are not disclosed. The August 2025 annual report separately reports fiscal-year NAV total return `-0.40%` and average annual since inception `-0.21%` as of `2025-08-31`; this older fiscal-period snapshot is not blended with March data.
- Official numeric YTD: NAV `-26.17%` as of `2026-03-31`. The later official fund-materials page is live but its reviewed HTML exposes placeholders (`nav_me_ytd`, `me_date`) rather than numeric values; a secondary Schwab capture was reviewed but not used to fill the later YTD gap.
- Return basis: issuer materials state total returns assume reinvestment of dividends/distributions; the SEC prospectus and fund materials describe returns before fees/expenses and the expense ratio is `0.86%`. Market-price values are kept separate.
- Annual observations: complete calendar NAV rows are not disclosed in the reviewed official capture. No up/down count or best/worst calendar-year ranking is inferred. The fiscal-year `-0.40%` is preserved only as a source-native annual report observation.
- S&P 500 comparison: cached S&P 500 rows are shown only as a common reference; no same-window 2022-2026 CAGR or proxy is calculated because fund calendar rows/current numeric month-end data are unavailable.

### INQQ Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:INQQ` | [EMQQ Global / INQQ official fund-materials page](https://emqqglobaletfs.com/inqq-fund-materials) | current identity, objective, exchange/page fields, inception, expense, official performance endpoint and data-gap check | Page reviewed `2026-07-26`; page identifies INQQ and primary exchange `NYSE`, inception `2022-04-05`, expense `0.86%`; later performance fields are placeholders in the reviewed HTML, so no later numeric YTD is inferred |
| `NYSE Arca:INQQ` | [Official INQQ factsheet](https://21674083.fs1.hubspotusercontent-na1.net/hubfs/21674083/Fund%20Documents/Fact%20Sheets/INQQ%20ETF%20Fact%20Sheet.pdf) | formal exchange, indexed-equity profile, available-period NAV TR, numeric YTD and holdings/sector snapshot | Factsheet reviewed `2026-07-26`; all data as of `2026-03-31`; exchange `NYSE Arca`; launch `2022-04-06`; 28 holdings; expense ratio `0.86%`; NAV annualized since inception `-7.83%`; NAV YTD `-26.17%`; India exposure `100%` |
| `NYSE Arca:INQQ` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1452937/000121390024113356/ea0224782-04_497k.htm) | formal listing, passive/index objective, index strategy, fees and risk cross-check | Prospectus dated `2024-12-30`; principal listing `NYSE Arca`; objective tracks INQQ The India Internet Index; management fee/total expenses `0.86%`; index universe uses India internet/e-commerce companies and liquidity/eligibility screens |
| `NYSE Arca:INQQ` | [Official annual shareholder report](https://emqqglobaletfs.com/hubfs/Fund%20Documents/Annual%20Report/INQQ%20Annual%20Report.pdf?hsLang=en) | fiscal-year NAV return and historical exchange cross-check | Fiscal year ended `2025-08-31`; principal listing `NYSE Arca`; NAV total return `-0.40%`; average annual since inception `-0.21%`; older fiscal-period observation not used as current month-end |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | common reference benchmark | Cached USD Total Return rows as of `2025-12-31`; 2026 current YTD not used |

### INQQ Raw Observations And Calculations

| Period | INQQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2022 | not disclosed; partial inception year | -18.11% (not comparable) |
| 2023 | not disclosed | 26.29% (not comparable) |
| 2024 | not disclosed | 25.02% (not comparable) |
| 2025 | not disclosed | 17.88% (not comparable) |
| FY ended 2025-08-31 | -0.40% | not comparable; fiscal-period result |
| 2026 YTD | -26.17% as of 2026-03-31 | not comparable; later current-year cache not used |
| Since inception | annualized -7.83% as of 2026-03-31 | not comparable |

- Available-period actual years: `(2026-03-31 − 2022-04-05) / 365.25 = 3.986311` years (`1456` days). Issuer annualized NAV TR is `-7.83%`; raw endpoints and cumulative since-inception NAV TR are `not disclosed`.
- Calendar-year up/down count, best year, worst year and calendar CAGR: `not disclosed`; official calendar NAV rows are unavailable in the reviewed capture.
- Fiscal-year cross-check: `-0.40%` NAV total return for `2024-09-01` to `2025-08-31`; this is not a calendar-year row and is not used to construct a 2021-2025 CAGR.

### INQQ Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, canonical exchange conflict resolution, exact fund identity, passive/indexing gate, inception/10Y audit, NAV TR/reinvestment/expense basis, available-period labeling, annual/fiscal-period distinction, current-YTD/date validation, S&P cache, source-gap handling, index/region links, filename/tags/breadcrumbs/link targets, no-proxy/no-annualization rule, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The NYSE-versus-NYSE-Arca conflict, one-day launch-date discrepancy, 3.986311-year history, official annualized available-period result, fiscal-year versus calendar-year separation, later dynamic-page numeric gap, raw-endpoint gap, and no-market-price-proxy rule are explicitly disclosed.

## TSMY Sequential Queue Record

- Input row: `110/125`; input ticker: `TSMY`; terminal status: `unsupported ETF type`.
- Canonical entity key: `NYSE Arca:TSMY`. YieldMax's official fund page identifies the primary exchange as NYSE Arca; the SEC summary prospectus also identifies the fund as listed on NYSE Arca. No provider slug or guessed exchange is used.
- Type-gate result: unsupported. YieldMax describes TSMY as an actively managed option-income ETF designed to generate weekly income by selling call spreads on Taiwan Semiconductor Manufacturing Co. (`TSM`). The fund does not invest directly in TSM, uses a derivative/option strategy, and carries single-issuer exposure. Active management, option-income and derivative-heavy structure are each outside the required passive/index-tracking equity ETF scope.
- Official classification observations: inception `2024-08-20`; gross expense ratio `1.01%`; latest reviewed NAV `US$15.77` as of `2026-07-22`; official page notes that the strategy captures only part of potential TSM upside while remaining exposed to losses if TSM declines. These observations are classification evidence only.
- No NAV TR/CAGR/annual table/S&P 500 comparison, performance page, region page update or ETF Performance Index row is created after the type gate. The official option-income distribution rate is not treated as a performance metric.

### TSMY Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:TSMY` | [YieldMax official TSMY product page](https://yieldmaxetfs.com/our-etfs/tsmy/) | issuer identity, exchange, strategy, option-income classification, single-issuer risk, inception, fee and current NAV | Page reviewed `2026-07-26`; primary exchange `NYSE Arca`; inception `2024-08-20`; gross expense ratio `1.01%`; NAV `US$15.77` as of `2026-07-22`; strategy sells call spreads on TSM and does not invest directly in TSM |
| `NYSE Arca:TSMY` | [SEC official summary prospectus](https://www.sec.gov/Archives/edgar/data/1924868/000199937125002066/tsmy-497k_022825.htm) | formal listing and active synthetic covered-call/option strategy cross-check | Prospectus dated `2025-02-28`; listed on NYSE Arca; primary objective current income; secondary objective indirect TSM ADR exposure; actively managed; synthetic covered-call/call-spread strategy |

### TSMY Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, canonical exchange, exact fund identity, asset-class/type gate, active/option-income/derivative-heavy classification, no-performance-page rule, no-region/index-update rule, source dates, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The official active management, call-spread strategy, single-issuer exposure and indirect TSM objective are sufficient to stop before performance analysis; no NAV TR, CAGR, YTD or proxy value is inferred.

## IMVP Sequential Queue Record

- Input row: `111/125`; input ticker: `IMVP`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:IMVP`. Invesco's official Q4 2025 product sheet identifies the fund's listing exchange as NYSE Arca; the current SEC summary prospectus identifies the current ticker `IMVP` and the same exchange. No provider slug or guessed exchange is used.
- Type-gate result: supported. The current SEC summary prospectus states that IMVP seeks to track the Bloomberg India MVP Index, generally invests at least 90% in index securities/ADRs/GDRs, and is non-diversified. The Invesco sheet states that the shares are not actively managed.
- Official identity/history: legal fund inception `2008-03-05`; the official Q4 2025 sheet reports the former ticker `PIN`, FTSE India Quality and Yield Select Index, total expense ratio `0.78%`, and NAV performance through `2025-12-31`. The SEC supplement says the ticker changed `PIN` → `IMVP` and the underlying index changed `FTSE India Quality and Yield Select Index` → `Bloomberg India MVP Index`, effective on/about `2026-02-23`.
- Mandatory 10-year coverage audit: official NAV performance data begin 10 years before the ending date `2025-12-31`; official NAV 10Y return is `9.19%` CAGR. The official calendar rows cover `2016-2025`, so the row satisfies the 10-year requirement. Normalized start/end TR values are `100.00` / `240.90`, with the end value calculated as `100 × (1 + 9.19%)^10`; raw issuer NAV endpoint levels are not disclosed.
- Current official 2026 NAV TR YTD: `not disclosed` in the reviewed Invesco capture as of `2026-07-26`. Secondary snippets were reviewed only as a gap check and were not used as the metric. No proxy, invented value or short-period annualization is created.

### IMVP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:IMVP` / former `PIN` | [Invesco official Q4 2025 performance PDF](https://www.invesco.com/us-rest/contentdetail?contentId=7d42fd05f0e21410VgnVCM100000c2f1bf0aRCRD) | Fund inception, exchange, passive status, fee, NAV TR definition/performance, 10Y CAGR and annual NAV rows | Reported through `2025-12-31`; former ticker `PIN`; 10Y NAV CAGR `9.19%`; annual rows `2016-2025` |
| `NYSE Arca:IMVP` | [SEC official current summary prospectus](https://www.sec.gov/Archives/edgar/data/1419139/000119312526062436/d71791d497k.htm) | Current identity, ticker, exchange, Bloomberg India MVP Index, passive/index-tracking strategy and 90% policy | Effective/current prospectus dated `2026-02-23`; current ticker `IMVP` |
| `NYSE Arca:IMVP` / former `PIN` | [SEC official ticker/index-change supplement](https://www.sec.gov/Archives/edgar/data/1419139/000110465925123131/tm2533678d1_497.htm) | Ticker and index transition, effective date and new index construction | Supplement dated `2025-12-19`; changes effective on/about `2026-02-23` |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### IMVP Raw Observations And Calculations

| Year | IMVP / PIN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.11% | 11.96% |
| 2017 | 37.12% | 21.83% |
| 2018 | -8.10% | -4.38% |
| 2019 | 4.83% | 31.49% |
| 2020 | 18.96% | 18.40% |
| 2021 | 23.94% | 28.71% |
| 2022 | -9.54% | -18.11% |
| 2023 | 22.61% | 26.29% |
| 2024 | 9.52% | 25.02% |
| 2025 | 1.72% | 17.88% |

- 2016-2025 IMVP/PIN NAV TR: `140.92%` cumulative / `9.19%` CAGR from `Π(1 + annual NAV TR) - 1`; S&P 500: `298.33%` / `14.82%`.
- 2021-2025 IMVP/PIN NAV TR: `53.14%` cumulative / `8.90%` CAGR; S&P 500: `96.17%` / `14.43%`; IMVP trails by approximately `5.53 pp` CAGR.
- Up/down years in 2016-2025: `8 / 2`; best `2017 +37.12%`; worst `2018 -8.10%`.
- Methodology break: 2016-2025 NAV rows are historical official NAV returns for the same legal fund under the former PIN/FTSE setup. They are not backfilled or proxied as post-change Bloomberg India MVP Index performance. The exact post-change 2026 YTD NAV TR is `not disclosed`.

### IMVP Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, canonical exchange and identity, passive/type gate, official NAV TR metric, 10-year coverage, calendar table, S&P 500 comparison, index/ticker break, current-YTD gap, source dates, region/index links, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The official 10-year NAV TR and annual rows pass the coverage gate; post-change current YTD remains explicitly `not disclosed`, and no proxy or invented value is written.

## KMCA Sequential Queue Record

- Input row: `112/125`; input ticker: `KMCA`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:KMCA`. The official PLUS product page identifies the primary exchange as NYSE ARCA and ticker `KMCA`; the SEC summary prospectus independently identifies NYSE Arca, Inc. as the principal listing exchange. No provider slug or guessed exchange is used.
- Type-gate result: supported. The SEC prospectus states that KMCA seeks to track the `Akros Korea Manufacturing Core Alliance Index`, normally invests at least 80% of net assets in index securities, and is not actively managed. It is a non-diversified South Korea equity ETF, not a bond, commodity, currency, multi-asset, leveraged, inverse, option-income or derivative-heavy product.
- Official identity: inception `2026-05-06`; management fee and total annual fund operating expenses `0.65%`; the PLUS page reports 36 holdings and NAV `US$18.78` as of `2026-07-23`.
- Mandatory 10-year coverage audit: the existing page had only an undisclosed-data placeholder. Rechecking the official PLUS performance table and the April 2026 SEC prospectus confirms the fund is new and has no complete calendar-year performance history; the SEC prospectus explicitly says the fund has no performance history until it completes a full calendar year. Therefore `10-year NAV TR unavailable` is a genuine history gap, not merely a page gap.
- Official available-period NAV TR: Fund NAV `-5.14%` cumulative from inception through `2026-06-30`; the PLUS page also reports `-5.14%` YTD at that month-end. The period is `55 days`, or `0.150582` years using `55 / 365.25`; returns under one year are explicitly not annualized. Normalized TR values are `100.00` / `94.86`, with raw issuer endpoints not disclosed.
- Official current YTD gap: the latest numeric official performance remains `-5.14%` as of `2026-06-30`; the page's later `2026-07-23` snapshot exposes current NAV but not a newer NAV TR YTD. No proxy, annualized value, invented annual row or mixed market-price return is used.

### KMCA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:KMCA` | [PLUS official KMCA product and performance page](https://plusetf.com/kmca) | Primary exchange, fund identity, inception, index/product description, holdings, fee, NAV, official Fund NAV/market-price performance and as-of dates | Page data as of `2026-07-23`; performance month/quarter end `2026-06-30`; inception `2026-05-06`; Fund NAV TR/YTD `-5.14%`; NAV `US$18.78` |
| `NYSE Arca:KMCA` | [SEC official summary prospectus](https://www.sec.gov/Archives/edgar/data/1547950/000121390026047871/ea0286568-02_497k.htm) | Principal exchange, objective, index, 80% policy, passive classification, fee, non-diversification, industry concentration and no-performance-history disclosure | Prospectus dated `2026-04-27` |
| `NYSE Arca:KMCA` | [SEC official prospectus and SAI filing](https://www.sec.gov/Archives/edgar/data/1547950/000121390026047633/ea0286568-01_485bpos.htm) | Formal listing and methodology/risk cross-check | Filing dated `2026-04-27` |
| `NYSE Arca:KMCA` | [Official NYSE Arca listing circular](https://www.nasdaqtrader.com/content/newsalerts/2026/infocircular/KMCA_Circular.pdf) | Listing-market and ticker cross-check | Circular reviewed `2026-07-26` |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31`; same-window 2026-06-30 TR not disclosed in reviewed official capture |

### KMCA Raw Observations And Calculations

| Period | KMCA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2026 YTD / since inception, 2026-05-06 to 2026-06-30 | -5.14% cumulative | not disclosed for the same official date window |

- Available-period normalized TR: `100.00 → 94.86`, calculated as `100 × (1 - 0.0514)` from the official cumulative Fund NAV return.
- Elapsed period: `55 days / 365.25 = 0.150582 years`; no CAGR is calculated because the issuer explicitly states returns for periods under one year are not annualized.
- Complete calendar-year observations: none; up/down/best/worst-year statistics are not applicable.
- Benchmark gap: the S&P 500 comparison is retained as a common reference, but no same-window numeric S&P 500 TR is inserted because it was not disclosed in the reviewed official benchmark capture. Cached 2016-2025 rows cannot be substituted for KMCA's 55-day period.

### KMCA Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, canonical exchange and identity, passive/type gate, official NAV TR metric, inception/history audit, available-period dates and formula, annualization rule, S&P 500 comparison, current-YTD gap, source dates, region/index links, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. The fund's new status and official 55-day NAV TR are recorded as an available-period result, with `10-year NAV TR unavailable`, no annualization, no proxy, and no invented calendar-year values.

## MAGC Sequential Queue Record

- Input row: `113/125`; input ticker: `MAGC`; terminal status: `unsupported ETF type`.
- Canonical entity key: `Cboe BZX:MAGC`. Roundhill's official product page identifies the primary exchange as Cboe BZX and the ticker as `MAGC`; the SEC summary prospectus identifies the same formal listing. The former ticker `DRAG` and name `Roundhill China Dragons ETF` changed to `MAGC` / `Roundhill China Magnificent Seven ETF` after market close on `2025-09-30`; the current canonical key is retained.
- Type-gate result: unsupported. Roundhill explicitly labels MAGC as `Actively Managed`. The official page also states that the fund uses total-return swaps to maintain compliance with RIC diversification tests; the strategy is concentrated in a small basket of seven Chinese companies. Active management and derivative-heavy total-return-swap exposure are outside the required passive/index-tracking equity ETF scope.
- Official observations: launch `2024-10-03`; gross/total expense ratio `0.59%`; Cboe BZX listing; no NAV TR/CAGR/annual table/S&P 500 comparison is created after the type gate.
- No performance page, China region row, or ETF Performance Index row is created or modified for MAGC. The former ticker/name change is retained as identity evidence only, not as a reason to merge the fund with another product.

### MAGC Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `Cboe BZX:MAGC` | [Roundhill official MAGC product page](https://www.roundhillinvestments.com/etf/magc/) | Current identity, primary exchange, active-management classification, total-return-swap rationale, inception, fee, strategy and holdings description | Page reviewed `2026-07-26`; launch `2024-10-03`; expense ratio `0.59%`; former `DRAG`/China Dragons change effective `2025-09-30` |
| `Cboe BZX:MAGC` | [SEC official summary prospectus](https://www.sec.gov/Archives/edgar/data/1976517/000139834425018708/fp0095512-2_497k.htm) | Formal listing, active investment objective/strategy, fees and risks | Prospectus dated `2025-09-30` |
| `Cboe BZX:MAGC` | [SEC official strategy/name/ticker supplement](https://www.sec.gov/Archives/edgar/data/1976517/000139834425018574/fp0095511-1_497.htm) | DRAG → MAGC transition and active strategy confirmation | Supplement dated `2025-09-26`; effective after market close `2025-09-30` |

### MAGC Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. Main agent performed the local checklist from `check-etf-performance/workflow.md`: queue/order, canonical exchange and identity, ticker/name change, passive/type gate, active-management test, derivative-heavy test, no-performance-page rule, no-region/index-update rule, source dates, and source-batch/ledger consistency.
- Local fallback verdict: `PASS`; no critical/high finding remained. Active management plus total-return-swap exposure is sufficient to stop before performance analysis; no NAV TR, CAGR, YTD or proxy value is inferred.

## ISVBF Sequential Queue Record

- Input row: `114/125`; input ticker: `ISVBF`; terminal status: `completed_available_period_no_10Y`.
- Canonical identity: `Euronext Amsterdam:ICHN`, the official USD listing for ISIN `IE00BJ5JPG56`. The input OTC alias `ISVBF` is retained as the queue label and identity bridge; the same share class is also listed on SIX Swiss Exchange as `ICHN`, Xetra as `ICGA`, and other venues. The canonical page uses the issuer/exchange-qualified Euronext Amsterdam identity, not an OTC provider slug.
- Type gate: supported passive, physical/replicated, accumulating equity ETF tracking `MSCI China Index (USD)`. iShares identifies the asset class as Equity, benchmark and TER as `0.28%`, and share-class launch as `2019-06-20`.
- 10-year coverage audit: `10-year NAV TR unavailable` because the share class launched in 2019. Official complete-calendar NAV TR rows are available for `2020-2025`; 2016-2019 rows are not disclosed. The six displayed rows compound from normalized `100.00` to `108.36`, or `8.36%` cumulative / `1.35%` CAGR over `6.00` complete calendar years. No incomplete 2019 period is annualized and no proxy is created.
- Comparison: the page includes the cached USD S&P 500 Total Return rows for `2020-2025`; S&P compounds to `132.26%` / `15.08%` CAGR. For `2021-2025`, ICHN is `-16.06%` cumulative / `-3.44%` CAGR versus S&P `96.17%` / `14.43%` CAGR. Latest official rolling 12-month NAV TR is `-5.07%` through `2026-06-30`; current official NAV TR YTD is `-8.79%` and NAV is `US$5.61`, both as of `2026-07-21`.
- Raw NAV endpoint levels, a directly calculated inception-to-date CAGR from the partial 2019 start, and 2016-2019 calendar rows are `not disclosed`; no values are filled or smoothed.

### ISVBF Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `Euronext Amsterdam:ICHN` | [iShares official ICHN product and performance page](https://www.ishares.com/uk/individual/en/products/308751/ishares-msci-china-ucits-etf?siteEntryPassthrough=true) | Fund identity, ISIN, official listings, equity/passive profile, benchmark, TER, share-class launch, NAV TR basis, annual NAV/benchmark rows, rolling 12-month rows, current NAV and YTD | Page reviewed `2026-07-26`; annual rows `2020-2025`; rolling window through `2026-06-30`; NAV/YTD as of `2026-07-21` |
| `Euronext Amsterdam:ICHN` | [iShares official ICHN factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/ichn-ishares-msci-china-ucits-etf-fund-fact-sheet-en-gb.pdf) | Passive physical/replicated classification, accumulating share class, ISIN, benchmark, TER and launch cross-check | Factsheet performance capture as of `2026-04-30`; reviewed `2026-07-26` |
| `Euronext Amsterdam:ICHN` | [Euronext Amsterdam official instrument page](https://live.euronext.com/en/product/etfs/IE00BJ5JPG56-XAMC/market-information) | Exchange-qualified canonical line, legal name, ISIN, USD ticker and listing cross-check | Page reviewed `2026-07-26`; listing/launch `2019-06-24` |
| `Euronext Amsterdam:ICHN` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) plus cached source-batch convention | USD S&P 500 Total Return comparison for complete calendar years `2020-2025` | Cache convention as of `2025-12-31`; no new web search required for this window |
| `OTC Markets:ISVBF` → `Euronext Amsterdam:ICHN` | [OTC identity/ISIN bridge](https://www.otcmarkets.com/stock/ISVBF/overview) | Secondary identity check linking input OTC alias to ISIN `IE00BJ5JPG56`; not used as the canonical performance source | Reviewed `2026-07-26`; official issuer/exchange sources take priority |

### ISVBF Raw Observations and Calculations

- Official annual NAV TR rows: `2020 29.10%`, `2021 -22.00%`, `2022 -22.10%`, `2023 -11.40%`, `2024 19.20%`, `2025 30.80%`.
- Official benchmark rows: `2020 29.50%`, `2021 -21.70%`, `2022 -21.90%`, `2023 -11.20%`, `2024 19.40%`, `2025 31.20%`.
- Calculation: `100 × Π(1 + annual NAV TR) = 108.361753`; cumulative `8.361753%` → `8.36%`; six-year CAGR `(108.361753 / 100)^(1/6) - 1 = 1.347414%` → `1.35%`.
- S&P cache rows for `2020-2025`: `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`; cumulative `132.264828%` → `132.26%`; six-year CAGR `15.079308%` → `15.08%`.

### ISVBF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `114/125`, canonical exchange-qualified entity key, OTC-to-ISIN identity bridge, issuer/fund identity, passive-equity type gate, official NAV TR basis, 10-year coverage threshold, available-period calculations, annual table and S&P comparison, source URLs/as-of dates, explicit gaps, page/index/region links, ledger status and next queue pointer.
- Result: local fallback `PASS`. Performance artifact and navigation updates were saved only after the checklist passed.

## KURE Sequential Queue Record

- Input row: `115/125`; input ticker: `KURE`; terminal status: `completed_available_period_no_10Y`.
- Canonical identity: `NYSE Arca:KURE`. KraneShares' official product page identifies KURE, its primary exchange as NYSE Arca, ISIN `US5007678353`, and inception date `2018-01-31`; no provider slug or guessed exchange is used.
- Type gate: supported passive/index-tracking equity ETF. The fund seeks to track the `MSCI China All Shares Health Care 10/40 Index (USD)` and the prospectus requires at least 80% of net assets in instruments in the underlying index or similar instruments. Exposure is to Chinese healthcare companies listed in Mainland China, Hong Kong and the United States.
- Metric: official Fund NAV Total Return. KraneShares' growth-of-$10,000 methodology assumes reinvestment of dividends and capital gains and deducts fund expenses; the SEC prospectus states that performance returns include reinvestment of dividends and distributions. Gross expense is `0.79%`; net after waiver is `0.65%` in the reviewed materials.
- 10-year coverage audit: `10-year NAV TR unavailable`; inception `2018-01-31` to performance date `2026-06-30` is `3,072 days / 365.25 = 8.410678` years and contains fewer than 10 complete calendar years. Official available-period Fund NAV TR is cumulative `-23.43%` and annualized `-3.12%`. Normalized TR is `100.00 → 76.57`; derived CAGR `-3.1243%` rounds to the official `-3.12%`.
- Official performance observations as of `2026-06-30`: Fund NAV cumulative 1M `-2.98%`, 3M `-7.56%`, 6M/YTD `-8.80%`, since inception `-23.43%`; average annualized 1Y `-3.15%`, 3Y `-2.80%`, 5Y `-16.07%`, since inception `-3.12%`. Daily NAV is `US$17.53` as of `2026-07-23`.
- Annual NAV TR rows: exact calendar-year Fund NAV rows are not disclosed in the reviewed current issuer text capture. The SEC summary prospectus exposes a calendar-return bar-chart image but exact rows were not extracted or reconstructed; the page retains `not disclosed` rather than inventing annual values.
- S&P comparison: cached USD S&P 500 TR rows for complete calendar years `2018-2025` are `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`; they compound to `192.03%` / `14.33%` CAGR. Exact same-start/same-end S&P TR for `2018-01-31` to `2026-06-30` is not disclosed, so the table labels the calendar reference as non-identical window.
- No annualized proxy, market-price return, or synthetic calendar NAV row is substituted for the unavailable official Fund NAV rows.

### KURE Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:KURE` | [KraneShares official KURE product and performance page](https://kraneshares.com/etf/kure/) | Fund identity, primary exchange, ISIN, inception, index, passive objective, fees, official NAV TR windows, current NAV/YTD, distributions and methodology | Page reviewed `2026-07-26`; fund details/NAV as of `2026-07-23`; performance table as of `2026-06-30` |
| `NYSE Arca:KURE` | [KraneShares official KURE factsheet](https://kraneshares.com/resources/factsheet/kure_factsheet.pdf) | Passive/index strategy, exchange, ISIN, inception, index and expense cross-check | Official factsheet capture as of `2026-01-30`; reviewed `2026-07-26` |
| `NYSE Arca:KURE` | [SEC official KURE summary prospectus](https://www.sec.gov/Archives/edgar/data/1547576/000182912625005533/kraneshares_497k.htm) | Objective, 80% policy, fee structure, risk/type gate, return basis and existence of calendar-return chart | Prospectus dated `2025-08-01`; performance text as of `2025-06-30` / average-return table through `2024-12-31` |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention | Common USD total-return reference for complete calendar years `2018-2025` | Cache convention as of `2025-12-31`; exact KURE start/end window not cached |

### KURE Raw Observations and Calculations

- Official cumulative Fund NAV rows: `1M -2.98%`, `3M -7.56%`, `6M -8.80%`, `YTD -8.80%`, `since inception -23.43%`, all as of `2026-06-30`.
- Official annualized Fund NAV rows: `1Y -3.15%`, `3Y -2.80%`, `5Y -16.07%`, `since inception -3.12%`, as of quarter end `2026-06-30`.
- Available-period calculation: `100 × (1 - 0.2343) = 76.57`; actual years `3,072 / 365.25 = 8.410678`; derived CAGR `(76.57 / 100)^(1 / 8.410678) - 1 = -3.1243%`.
- Cached S&P 500 TR reference: `2018 -4.38%`, `2019 31.49%`, `2020 18.40%`, `2021 28.71%`, `2022 -18.11%`, `2023 26.29%`, `2024 25.02%`, `2025 17.88%`; 2018-2025 cumulative `192.03%` / CAGR `14.33%`.

### KURE Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `115/125`, canonical exchange-qualified identity, issuer/fund identity, passive-equity type gate, official NAV TR/reinvestment/expense basis, inception and 10-year threshold, available-period start/end values and CAGR, annual-row gap, S&P reference and window caveat, current-YTD as-of date, source URLs/as-of dates, page/index/region links, ledger status and next queue pointer.
- Result: local fallback `PASS`. The page records the official available-period NAV TR and explicit calendar-row gap; no synthetic annual values or same-window S&P proxy is inserted.

## FXY Sequential Queue Record

- Input row: `116/125`; input ticker: `FXY`; terminal status: `unsupported ETF type`.
- Canonical identity: `NYSE Arca:FXY`. Invesco's official product page identifies the ticker, exchange, ISIN `US46138W1071`, inception `2007-02-12`, and CurrencyShares Japanese Yen Trust name. SEC's 2025 Form 10-K confirms the primary listing was transferred to NYSE Arca on `2007-10-30`.
- Type gate: unsupported. The product is a currency trust/grantor trust designed to reflect the USD price of Japanese yen plus accrued interest, less trust expenses. SEC states that the Trust holds Japanese yen and does not hold or use derivative products; this does not make it an equity ETF. Currency/FX exposure is expressly outside the required passive index-tracking equity ETF scope.
- No NAV Total Return, 10-year CAGR, annual equity-return table, S&P 500 comparison, performance page, region row, or ETF Performance Index addition is created after the type gate. Any current FXY return data would be irrelevant to the required equity-ETF performance output.

### FXY Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:FXY` | [Invesco official FXY product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-currencyshares-japanese-yen-trust.html) | Current fund identity, ticker, primary exchange, ISIN, inception, trust objective, currency exposure and expense ratio | Page reviewed `2026-07-26`; official page shows YTD NAV return as of `2026-05-31`, but it is not used after the type gate |
| `NYSE Arca:FXY` | [SEC 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1353613/000119312526083566/fxy-20251231.htm) | Grantor-trust structure, Japanese-yen holdings, listing history, passive vehicle description and no-derivatives statement | Fiscal year ended `2025-12-31`; filed `2026` |
| `NYSE Arca:FXY` | [Invesco official FXY factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/etf-snapshot/fxy-invesco-currencyshares-japanese-yen-trust-fact-sheet.pdf) | Secondary issuer cross-check for fund description, listing exchange, CUSIP and expense ratio | Factsheet as of `2025-06-30`; reviewed `2026-07-26` |

### FXY Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `116/125`, canonical exchange-qualified identity, issuer/trust identity, equity-versus-currency type gate, unsupported-type reason, no-performance-page rule, no-region/index-update rule, source URLs/as-of dates, ledger status and next queue pointer.
- Result: local fallback `PASS`. The currency-trust classification is sufficient to stop before performance analysis; no NAV TR, CAGR, YTD, proxy, or synthetic equity comparison is inferred.

## KRANF Sequential Queue Record

- Input row: `117/125`; input ticker: `KRANF`; terminal status: `completed_available_period_no_10Y`.
- Canonical identity: `LSE:KWEB`, the official USD London Stock Exchange line `KWEB LN` for ISIN `IE00BFXR7892`. KraneShares' current listing table also shows the same USD share class on Euronext Amsterdam as `KWEB NA`. The OTC input label `KRANF` is retained as the queue alias and is bridged by the fund name, inception, index and share-class identity; the US-listed KWEB product is not merged because it has a different ISIN.
- Type gate: supported passive, physical/index-tracking China internet equity UCITS ETF. The current KIID states that the fund is passively managed, tracks `CSI Overseas China Internet Index`, normally invests at least 80% in index securities or depositary receipts, reinvests income, and does not intend to use financial derivatives or total-return swaps.
- 10-year coverage audit: current product page, current KIID, and official annual financial reports confirm a USD share-class launch of `2018-11-21`; the fund launch date is shown as `2018-11-20` in the KIID. The verified period through `2026-06-30` is `2,778 days / 365.25 = 7.605749` years, so `10-year NAV TR unavailable` and no 10-year label is used.
- Official available-period Fund NAV TR: cumulative `-26.60%` and annualized `-3.98%` through `2026-06-30`. Normalized TR is `100.00 → 73.40`; derived CAGR `(73.40 / 100)^(1 / 7.605749) - 1 = -3.9844%`, matching the official rounded value.
- Official current performance: YTD `-28.96%` and 6-month `-28.96%`, both as of `2026-06-30`; 1Y `-24.33%`, 3Y `0.51%`, 5Y `-15.80%`, and since-inception annualized `-3.98%`. Daily USD-share-class NAV is `US$19.82` as of `2026-07-24`.
- Corrected KIID annual NAV rows for complete calendar years: `2019 28.20%`, `2020 59.50%`, `2021 -49.20%`, `2022 -16.40%`, `2023 -9.90%`, `2024 13.20%`, `2025 23.80%`. The same KIID gives index rows `29.20%`, `60.90%`, `-49.00%`, `-16.40%`, `-10.00%`, `11.90%`, `23.30%`. The KIID explicitly corrects the 2019 values; the corrected values are used.
- Complete calendar calculations: KWEB `2019-2025` compounds to `9.650487%` / `1.324809%` CAGR; `2021-2025` compounds to `-46.375673%` / `-11.717958%` CAGR. Cached S&P 500 USD TR `2019-2025` compounds to `205.405021%` / `17.291901%` CAGR; `2021-2025` is `96.169618%` / `14.426430%` CAGR.
- No market-price return, incomplete 2018 annual proxy, or non-USD share-class result is substituted for the official USD NAV TR metric.

### KRANF Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `LSE:KWEB` | [KraneShares Europe official KWEB UCITS product and performance page](https://kraneshares.eu/etf/kwebln/) | USD share-class identity, ISIN, listings, inception, passive structure, index, fee, official NAV TR windows, current NAV/YTD and as-of dates | Page reviewed `2026-07-26`; fund/listing/NAV as of `2026-07-24`; performance as of `2026-06-30` |
| `LSE:KWEB` | [Current official KWEB USD KIID](https://kraneshares.eu/resources/compliance/kiids/2026_02_20_kwebln_kiid_english_usd.pdf) | Passive/index policy, 80% policy, income reinvestment, no-derivatives statement, expense basis, corrected annual performance rows and launch dates | KIID accurate as of `2026-01-29`; annual rows through `2025` |
| `LSE:KWEB` | [Official KraneShares 2025 annual financial report](https://kraneshares.eu/resources/compliance/2026_01_29_europe_annual.financials.and.other.information.pdf) | Fiscal-year NAV-return cross-check and index methodology | Reporting period ended `2025-09-30`; reviewed `2026-07-26`; fiscal-year figures kept separate from calendar rows |
| `LSE:KWEB` | [Official London Stock Exchange KWEB page](https://www.londonstockexchange.com/stock/KWEB/kraneshares-icav/company-page) | Exchange-qualified USD listing and legal fund identity cross-check | Page reviewed `2026-07-26` |
| `OTC:KRANF` → `LSE:KWEB` | [Secondary OTC alias page](https://stockanalysis.com/quote/otc/KRANF/) | Input alias/name, OTC ticker, inception and index identity bridge only | Reviewed `2026-07-26`; secondary source not used for NAV TR or current YTD |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention | Common USD total-return reference for complete calendar years `2019-2025` and `2021-2025` | Cache convention as of `2025-12-31`; same inception-to-date window not cached |

### KRANF Raw Observations and Calculations

- Available-period calculation: `100 × (1 - 0.2660) = 73.40`; `2,778 / 365.25 = 7.605749`; derived CAGR `-3.9844%`.
- Annual Fund NAV TR / index TR: `2019 28.20% / 29.20%`; `2020 59.50% / 60.90%`; `2021 -49.20% / -49.00%`; `2022 -16.40% / -16.40%`; `2023 -9.90% / -10.00%`; `2024 13.20% / 11.90%`; `2025 23.80% / 23.30%`.
- S&P cache rows for the same complete calendar years: `2019 31.49%`, `2020 18.40%`, `2021 28.71%`, `2022 -18.11%`, `2023 26.29%`, `2024 25.02%`, `2025 17.88%`.

### KRANF Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `117/125`, OTC-to-official-LSE identity bridge, distinct US KWEB share-class check, passive-equity type gate, official NAV TR/reinvestment/expense basis, 10-year threshold, available-period dates/end value/formula, annual KIID rows and correction note, S&P comparison, current-YTD as-of date, source URLs/as-of dates, page/index/region links, region count, ledger status and next queue pointer.
- Result: local fallback `PASS`. The official USD UCITS page is saved under the canonical LSE identity, with the OTC alias retained and no US KWEB data merged into it.

## KHYB Sequential Queue Record

- Input row: `118/125`; input ticker: `KHYB`; terminal status: `unsupported ETF type`.
- Canonical identity: `NYSE:KHYB` based on the current KraneShares product page, which identifies the current primary exchange as NYSE, ticker `KHYB`, ISIN `US5007678437`, and inception `2018-06-26`. The 2025 SEC summary prospectus identifies the principal listing exchange as NYSE Arca; this exchange conflict is retained rather than guessed away.
- Type gate: unsupported for two independent reasons. KraneShares labels KHYB an `active ETF` managed by Amova Asset Management and describes exposure to USD-denominated Asia high-yield debt securities. It is a fixed-income bond ETF, not a passive index-tracking equity ETF; active management is also outside scope.
- The official page notes prior names/strategy history: KraneShares CCBS China Corporate High Yield Bond USD ETF before `2021-08-01`, KraneShares Asia Pacific High Income Bond ETF from `2021-08-02` to `2024-08-01`, and current KraneShares Asia Pacific High Income USD Bond ETF thereafter. This history does not change the terminal type classification.
- No NAV Total Return, 10-year CAGR, annual equity-return table, S&P 500 comparison, performance page, region row, or ETF Performance Index addition is created after the type gate.

### KHYB Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE:KHYB` | [Current KraneShares official KHYB product and performance page](https://kraneshares.com/etf/khyb/) | Current fund identity, ticker, current issuer exchange field, ISIN, inception, active-management classification, bond objective, benchmark, fees and current data | Page reviewed `2026-07-26`; fund/current NAV/yield data as of `2026-07-23`; current page says primary exchange `NYSE` |
| `NYSE Arca:KHYB` | [SEC 2025 summary prospectus](https://www.sec.gov/Archives/edgar/data/1547576/000182912625005532/kraneshares_497k.htm) | Principal listing exchange, objective, active management and fixed-income classification cross-check | Prospectus dated `2025-07-29`; SEC field says NYSE Arca |
| `NYSE Arca:KHYB` | [KraneShares 2026 annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_khyb_annual.TSR.report.pdf) | Annual-report identity and NAV/market-price return context; not used after type gate | Reporting period ended `2026-03-31`; principal listing exchange stated as NYSE Arca |

### KHYB Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `118/125`, canonical issuer identity, exchange conflict capture, fund/name history, active-versus-passive gate, equity-versus-bond gate, unsupported-type reason, no-performance-page rule, no-region/index-update rule, source URLs/as-of dates, ledger status and next queue pointer.
- Result: local fallback `PASS`. Bond exposure plus active management is sufficient to stop before performance analysis; no NAV TR, CAGR, YTD, proxy, or equity comparison is inferred.

## VNM Sequential Queue Record

- Input row: `119/125`; input ticker: `VNM`; terminal status: `completed_10Y`.
- Canonical identity: `Cboe BZX:VNM`. The current SEC summary prospectus identifies the principal U.S. listing exchange as Cboe BZX Exchange, Inc.; VanEck's current fact sheet labels the exchange `CBOE`. The stale `NYSE Arca:VNM` page is superseded and not used as the canonical identity.
- Type gate: supported passive/index-tracking Vietnam equity ETF. VanEck states that VNM seeks to replicate the MarketVector Vietnam Local Index; the SEC prospectus says the fund uses a passive/indexing approach, normally invests at least 80% in benchmark securities, and is not actively managed. It is not bond, commodity, currency trust, multi-asset, leveraged, inverse, option-income, derivative-heavy or single-stock exposure.
- Official rolling 10-year NAV TR: fact sheet reports `3.65%` average annual total return for `2016-06-30` to `2026-06-30`; actual years `10.00`. Raw NAV endpoints are not disclosed. Normalized `100.00 → 143.12` is an implied calculation from `100 × (1.0365^10)`, not a raw endpoint.
- Official calendar NAV TR: SEC annual chart reports `2016 -9.78%`, `2017 35.76%`, `2018 -14.14%`, `2019 8.86%`, `2020 9.72%`, `2021 22.52%`, `2022 -44.47%`, `2023 15.95%`, `2024 -10.19%`, `2025 62.42%`. These compound to `44.54%` / CAGR `3.75%` over 10 complete calendar years. Common `2021-2025` rows compound to `15.07%` / CAGR `2.85%`.
- S&P 500 comparison uses cached USD Total Return rows for `2016-2025` (`11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`); cumulative `298.33%` / CAGR `14.82%`. Common `2021-2025` S&P cumulative is `96.17%` / CAGR `14.43%`; VNM trails by approximately `11.58 pp` CAGR.
- Current observations: official VanEck product snapshot gives NAV `US$16.56` and YTD `-12.07%` as of `2026-07-24`; the June factsheet gives standardized month-end YTD `-1.41%` as of `2026-06-30`. The date/convention difference is disclosed; no value is blended or backfilled.

### VNM Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `Cboe BZX:VNM` | [VanEck official VNM product and performance page](https://www.vaneck.com/us/en/investments/vietnam-etf-vnm/) | Current fund identity, objective, current NAV/YTD, fee and current performance snapshot | Page reviewed `2026-07-26`; NAV/YTD `US$16.56` / `-12.07%` as of `2026-07-24` |
| `Cboe BZX:VNM` | [VanEck VNM fact sheet](https://www.vaneck.com/us/en/investments/vietnam-etf-vnm-fact-sheet.pdf) | Official NAV TR basis, rolling 10Y CAGR, annualized benchmark comparison, inception, exchange and fee | Fact sheet as of `2026-06-30`; rolling 10Y NAV CAGR `3.65%`; standardized YTD `-1.41%` |
| `Cboe BZX:VNM` | [SEC VNM summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000473/vaneckvietnametfvnmsumpro-.htm) | Principal listing, passive/indexing classification, 80% policy, benchmark transition and annual NAV TR chart | Prospectus dated `2026-05-01`; annual chart through `2025` |
| `Cboe BZX:VNM` | [VanEck VNM annual shareholder report](https://vaneck.onlineprospectus.net/VanEck/MOB_library/MOB_data/LIB_SummaryProspectus/vnmar/vnmar.pdf) | NAV total-return and hypothetical-$10,000 cross-check | Reporting period ended `2025-12-31`; Fund value `$14,454` from `$10,000` over the 10-year chart |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) plus cached source-batch convention | Common USD Total Return reference and annual rows | Cached rows as of `2025-12-31`; 2026 not used |

### VNM Raw Observations And Calculations

| Year | VNM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -9.78% | 11.96% |
| 2017 | 35.76% | 21.83% |
| 2018 | -14.14% | -4.38% |
| 2019 | 8.86% | 31.49% |
| 2020 | 9.72% | 18.40% |
| 2021 | 22.52% | 28.71% |
| 2022 | -44.47% | -18.11% |
| 2023 | 15.95% | 26.29% |
| 2024 | -10.19% | 25.02% |
| 2025 | 62.42% | 17.88% |

- Rolling official 10Y NAV TR: `3.65%` CAGR, `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints not disclosed; implied normalized endpoint `100.00 → 143.12`.
- Calendar calculation: `100 × Π(1 + annual NAV TR) = 144.540410`; cumulative `44.54%`; CAGR `(144.540410 / 100)^(1/10) - 1 = 3.752586%` → `3.75%`.
- Common-window calculation: `2021-2025` VNM cumulative `15.071988%` / CAGR `2.847544%` → `2.85%`; S&P cumulative `96.169618%` / CAGR `14.426430%` → `14.43%`.
- S&P reference calculation: `2016-2025` cumulative `298.329111%` / CAGR `14.821761%` → `14.82%`.
- Current NAV TR YTD is `-12.07%` as of `2026-07-24`; standardized June month-end YTD is `-1.41%` as of `2026-06-30`. Daily NAV drawdown/recovery history is `ไม่พบข้อมูลที่ยืนยันได้`.

### VNM Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `119/125`, canonical exchange-qualified identity, current-versus-stale exchange check, fund identity, passive-equity type gate, official NAV TR/reinvestment/expense basis, rolling 10-year threshold, normalized endpoint disclosure, annual NAV rows, S&P 500 cached basis/window, benchmark change, current-YTD as-of dates, filenames, Vietnam region assignment, canonical geography tag, breadcrumbs, stale-page replacement, ledger status and next queue pointer.
- Result: local fallback `PASS`; no critical or high-severity finding remained. The current Cboe BZX canonical listing replaces the stale NYSE Arca page, while the two official YTD observations remain separately labeled by as-of date.

## EIDO Sequential Queue Record

- Input row: `120/125`; input ticker: `EIDO`; terminal status: `completed_10Y`.
- Canonical identity: `NYSE Arca:EIDO`. iShares' current product page and December 30, 2025 summary prospectus both identify EIDO and NYSE Arca; no provider slug or guessed exchange is used.
- Type gate: supported passive/index-tracking Indonesia equity ETF. iShares identifies the asset class as Equity, tracks `MSCI Indonesia IMI 25/50 Index (USD) (Net)`, uses representative sampling/indexing, and generally invests at least 80% in index securities or substantially identical instruments. It is not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy or single-stock exposure.
- Official rolling 10-year NAV TR: iShares reports cumulative `-40.80%` and average annual `-5.11%` for `2016-06-30` to `2026-06-30`; actual years `10.00`; normalized `100.00 → 59.20` from the official cumulative value.
- Official calendar NAV TR: SEC summary prospectus chart reports `2016 16.83%`, `2017 18.43%`, `2018 -10.58%`, `2019 5.01%`, `2020 -8.09%`, `2021 0.87%`, `2022 -0.43%`, `2023 2.09%`, `2024 -11.41%`; June 2026 fact sheet reports `2025 2.98%`. These compound to `11.70%` / CAGR `1.11%` over 10 complete calendar years. Common `2021-2025` rows compound to `-6.46%` / CAGR `-1.33%`.
- S&P 500 comparison uses cached USD Total Return rows for `2016-2025`; cumulative `298.33%` / CAGR `14.82%`. Common `2021-2025` S&P cumulative is `96.17%` / CAGR `14.43%`; EIDO trails by approximately `15.75 pp` CAGR.
- Current observations: iShares current product snapshot gives NAV `US$12.30` as of `2026-07-24` and NAV TR YTD `-31.36%` as of `2026-07-23`; standardized June month-end YTD is `-38.53%` as of `2026-06-30`. The date/convention difference is disclosed; no value is blended or backfilled.

### EIDO Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:EIDO` | [iShares official EIDO product and performance page](https://www.ishares.com/us/products/239661/ishares-msci-indonesia-etf) | Current identity, NYSE Arca listing, benchmark, inception, fee, rolling/calendar NAV TR and current NAV/YTD | Page reviewed `2026-07-26`; NAV `US$12.30` as of `2026-07-24`; current YTD `-31.36%` as of `2026-07-23`; standardized performance through `2026-06-30` |
| `NYSE Arca:EIDO` | [iShares EIDO June 2026 fact sheet](https://www.ishares.com/us/literature/fact-sheet/eido-ishares-msci-indonesia-etf-fund-fact-sheet-en-us.pdf) | Official 2021-2025 calendar NAV rows, 10-year NAV TR, index rows, fee and fund facts | Fact sheet as of `2026-06-30`; 2025 NAV `2.98%`; 10Y NAV CAGR `-5.11%` |
| `NYSE Arca:EIDO` | [iShares EIDO summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-indonesia-etf-8-31.pdf) | Listing, indexing/representative sampling strategy, 80% policy, risks and 2016-2024 annual NAV chart | Prospectus dated `2025-12-30`; chart through `2024` |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) plus cached source-batch convention | Common USD Total Return reference and annual rows | Cached rows as of `2025-12-31`; 2026 not used |

### EIDO Raw Observations And Calculations

| Year | EIDO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 16.83% | 11.96% |
| 2017 | 18.43% | 21.83% |
| 2018 | -10.58% | -4.38% |
| 2019 | 5.01% | 31.49% |
| 2020 | -8.09% | 18.40% |
| 2021 | 0.87% | 28.71% |
| 2022 | -0.43% | -18.11% |
| 2023 | 2.09% | 26.29% |
| 2024 | -11.41% | 25.02% |
| 2025 | 2.98% | 17.88% |

- Rolling official 10Y NAV TR: cumulative `-40.80%`; normalized `100.00 → 59.20`; actual years `10.00`; CAGR `-5.11%`; raw NAV endpoints are not disclosed.
- Calendar calculation: `100 × Π(1 + annual NAV TR) = 111.700603`; cumulative `11.70%`; CAGR `(111.700603 / 100)^(1/10) - 1 = 1.112664%` → `1.11%`.
- Common-window calculation: `2021-2025` EIDO cumulative `-6.456994%` / CAGR `-1.326107%` → `-1.33%`; S&P cumulative `96.169618%` / CAGR `14.426430%` → `14.43%`.
- S&P reference calculation: `2016-2025` cumulative `298.329111%` / CAGR `14.821761%` → `14.82%`.
- Current NAV TR YTD is `-31.36%` as of `2026-07-23`; standardized June month-end YTD is `-38.53%` as of `2026-06-30`. Daily NAV drawdown/recovery history is `ไม่พบข้อมูลที่ยืนยันได้`.

### EIDO Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `120/125`, canonical exchange-qualified identity, fund identity, passive-equity type gate, official NAV TR/reinvestment/expense basis, rolling 10-year threshold, normalized endpoint disclosure, annual NAV rows from two official documents, S&P 500 cached basis/window, benchmark change, current-YTD as-of dates, filenames, Indonesia region assignment, canonical geography tag, breadcrumbs, stale-page replacement, ledger status and next queue pointer.
- Result: local fallback `PASS`; no critical or high-severity finding remained. The 2016-2024 annual rows are sourced from the official prospectus chart and 2025 from the official June 2026 fact sheet; the two current YTD observations remain separately labeled by as-of date.

## GLIN Sequential Queue Record

- Input row: `121/125`; input ticker: `GLIN`; terminal status: `completed_10Y`.
- Canonical identity: `NYSE Arca:GLIN`. VanEck's current fact sheet and May 1, 2026 SEC summary prospectus identify the NYSE Arca listing, ticker and fund; no provider slug or guessed exchange is used.
- Type gate: supported passive/index-tracking India equity ETF. VanEck's prospectus identifies a passive/indexing approach, at least 80% exposure to the MarketGrader India All-Cap Growth Leaders Index through a Mauritius subsidiary, and no attempt to beat the index. The factor name does not make the fund active.
- Official rolling 10-year NAV TR: June 2026 fact sheet reports average annual `1.92%` for `2016-06-30` to `2026-06-30`; actual years `10.00`. Raw NAV endpoints are not disclosed. Normalized `100.00 → 120.95` is an implied calculation from `100 × (1.0192^10)`, not a raw endpoint.
- Official calendar NAV TR: SEC annual chart reports `2016 -4.70%`, `2017 66.88%`, `2018 -38.00%`, `2019 0.80%`, `2020 -21.65%`, `2021 -21.99%`, `2022 29.15%`, `2023 35.50%`, `2024 -4.92%`, `2025 16.11%`. These compound to `17.36%` / CAGR `1.61%` over 10 complete calendar years. Common `2021-2025` rows compound to `50.71%` / CAGR `8.55%`.
- S&P 500 comparison uses cached USD Total Return rows for `2016-2025`; cumulative `298.33%` / CAGR `14.82%`. Common `2021-2025` S&P cumulative is `96.17%` / CAGR `14.43%`; GLIN trails by approximately `5.88 pp` CAGR.
- Current observations: official VanEck product snapshot gives NAV `US$44.35` and YTD `-4.15%` as of `2026-07-24`; the June fact sheet gives standardized month-end YTD `0.25%` as of `2026-06-30`. The date/convention difference is disclosed; no value is blended or backfilled.

### GLIN Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:GLIN` | [VanEck official GLIN product and performance page](https://www.vaneck.com/us/en/investments/india-growth-leaders-etf-glin/) | Current identity, objective, current NAV/YTD, fee and current performance snapshot | Page reviewed `2026-07-26`; NAV/YTD `US$44.35` / `-4.15%` as of `2026-07-24` |
| `NYSE Arca:GLIN` | [VanEck GLIN fact sheet](https://www.vaneck.com/us/en/investments/india-growth-leaders-etf-glin-fact-sheet.pdf) | Official NAV TR basis, rolling 10Y CAGR, benchmark comparison, inception, exchange, fees and exposures | Fact sheet as of `2026-06-30`; rolling 10Y NAV CAGR `1.92%`; standardized YTD `0.25%` |
| `NYSE Arca:GLIN` | [SEC GLIN summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000467/vaneckindiagrowthleaderset.htm) | Listing, passive/indexing classification, subsidiary/80% policy, index change and annual NAV TR chart | Prospectus dated `2026-05-01`; annual chart through `2025` |
| `NYSE Arca:GLIN` | [VanEck GLIN annual shareholder report](https://vaneck.onlineprospectus.net/VanEck/MOB_library/MOB_data/LIB_SummaryProspectus/glinar/glinar.pdf) | NAV total-return and hypothetical-$10,000 cross-check | Reporting period ended `2025-12-31`; official 10Y NAV CAGR `1.61%` in the report table |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) plus cached source-batch convention | Common USD Total Return reference and annual rows | Cached rows as of `2025-12-31`; 2026 not used |

### GLIN Raw Observations And Calculations

| Year | GLIN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -4.70% | 11.96% |
| 2017 | 66.88% | 21.83% |
| 2018 | -38.00% | -4.38% |
| 2019 | 0.80% | 31.49% |
| 2020 | -21.65% | 18.40% |
| 2021 | -21.99% | 28.71% |
| 2022 | 29.15% | -18.11% |
| 2023 | 35.50% | 26.29% |
| 2024 | -4.92% | 25.02% |
| 2025 | 16.11% | 17.88% |

- Rolling official 10Y NAV TR: `1.92%` CAGR, `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints not disclosed; implied normalized endpoint `100.00 → 120.95`.
- Calendar calculation: `100 × Π(1 + annual NAV TR) = 117.362998`; cumulative `17.36%`; CAGR `(117.362998 / 100)^(1/10) - 1 = 1.613900%` → `1.61%`.
- Common-window calculation: `2021-2025` GLIN cumulative `50.710247%` / CAGR `8.549682%` → `8.55%`; S&P cumulative `96.169618%` / CAGR `14.426430%` → `14.43%`.
- S&P reference calculation: `2016-2025` cumulative `298.329111%` / CAGR `14.821761%` → `14.82%`.
- Current NAV TR YTD is `-4.15%` as of `2026-07-24`; standardized June month-end YTD is `0.25%` as of `2026-06-30`. Daily NAV drawdown/recovery history is `ไม่พบข้อมูลที่ยืนยันได้`.

### GLIN Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `121/125`, canonical exchange-qualified identity, fund identity, passive-equity type gate, official NAV TR/reinvestment/expense basis, rolling 10-year threshold, normalized endpoint disclosure, annual NAV rows, prior-index change, S&P 500 cached basis/window, current-YTD as-of dates, filenames, India region assignment, canonical geography tag, breadcrumbs, stale-page replacement, ledger status and next queue pointer.
- Result: local fallback `PASS`; no critical or high-severity finding remained. The factor/index methodology is retained as passive, and the two official YTD observations remain separately labeled by as-of date.

## KTEC Sequential Queue Record

- Input row: `122/125`; input ticker: `KTEC`; terminal status: `completed_available_period_no_10Y`.
- Canonical identity: `NYSE Arca:KTEC`. The 2025 SEC summary prospectus and the 2026 KraneShares factsheet identify the principal listing exchange as NYSE Arca; the current product page displays a shortened `NYSE` field, which is retained as a disclosed current-page wording conflict rather than used to replace the formal canonical key.
- Type gate: supported passive/index-tracking Hong Kong technology equity ETF. The official prospectus says KTEC seeks to track the price and yield performance of the Hang Seng TECH Index; the index is composed of 30 Hong Kong-listed technology companies, and the fund is not active, leveraged, inverse, option-income, bond, commodity, currency-trust, multi-asset or single-stock.
- Official available-period NAV TR: KraneShares reports Fund NAV cumulative `-49.08%` from inception through `2026-06-30`, with issuer-reported since-inception annualized return `-12.48%`; inception `2021-06-08`; elapsed years `(2026-06-30 - 2021-06-08) / 365.25 = 5.059548`, shown as `5.06`. Raw start/end TR values are not disclosed. Implied normalized endpoint `100.00 → 50.92` is calculated only from the disclosed cumulative return.
- Official calendar NAV TR: SEC summary prospectus chart provides complete rows `2022 -25.01%`, `2023 -11.21%`, `2024 18.46%`; the 2021 inception-year partial row and 2025 calendar NAV row are `not disclosed` in the reviewed current official materials. These rows compound to `-21.13%` / CAGR `-7.61%` over the three disclosed complete years; this is not a 10-year metric.
- Current observations: current KraneShares product page gives NAV `US$12.87` as of `2026-07-24`; official month-end NAV TR YTD is `-22.88%` as of `2026-06-30`. Market-price returns remain separate and are not mixed into the NAV TR metric.
- S&P 500 comparison: cached USD Total Return rows are used for the disclosed common calendar rows `2022-2024`: `-18.11%`, `26.29%`, `25.02%`; cumulative `29.29%` / CAGR `8.94%`. This is a common-reference comparison only, not a 10-year comparison. The ETF's 2025 row is not disclosed, so 2025 is excluded from the common-window calculation.

### KTEC Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:KTEC` | [KraneShares official KTEC product/performance page](https://kraneshares.com/etf/ktec/) | Current identity, strategy, current page exchange wording, NAV, current data, issuer performance table and distributions | Page reviewed `2026-07-26`; current NAV `US$12.87` as of `2026-07-24`; performance table as of `2026-06-30` |
| `NYSE Arca:KTEC` | [KraneShares official KTEC factsheet](https://kraneshares.com/resources/factsheet/ktec_factsheet.pdf) | Formal exchange, inception, index, expense, NAV TR basis and available-period performance | Factsheet data as of `2026-06-30`; primary exchange `NYSE Arca, Inc.`; inception `2021-06-08`; expense `0.69%`; NAV TR since inception `-49.08%` / annualized `-12.48%` |
| `NYSE Arca:KTEC` | [SEC/KraneShares summary prospectus](https://kraneshares.com/resources/compliance/2026_02_20_ktec_summary.prospectus.pdf) | Formal listing, passive/index-tracking objective, index composition, fees and annual NAV TR chart | Prospectus dated `2025-08-01`; annual chart through `2024`; rows `2022-2024`; 2021 partial/2025 row not disclosed in reviewed capture |
| `NYSE Arca:KTEC` | [KraneShares annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_ktec_annual.TSR.report.pdf) | Total-return definition, reinvestment disclosure, fiscal-year NAV cross-check and since-inception graph | Reporting period ended `2026-03-31`; fund NAV return `-14.71%` for the fiscal year; since-inception annualized `-11.40%` to that fiscal period; not substituted for the June month-end calendar window |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) plus cached source-batch convention | Common USD Total Return reference and annual rows | Cached rows as of `2025-12-31`; only `2022-2024` used for KTEC common-window calculation |

### KTEC Raw Observations And Calculations

| Year | KTEC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2022 | -25.01% | -18.11% |
| 2023 | -11.21% | 26.29% |
| 2024 | 18.46% | 25.02% |
| 2025 | not disclosed | 17.88% |

- Available-period calculation: `(2026-06-30 - 2021-06-08) / 365.25 = 5.059548 years`; official cumulative NAV TR `-49.08%`; normalized implied endpoint `100.00 × (1 - 0.4908) = 50.92`; issuer-reported annualized NAV TR `-12.48%`. Raw start/end TR values remain `not disclosed`.
- Calendar calculation: `100 × (1 - 0.2501) × (1 - 0.1121) × (1 + 0.1846) = 78.874957`; cumulative `-21.13%`; CAGR `(78.874957 / 100)^(1/3) - 1 = -7.605445%` → `-7.61%`.
- S&P common-window calculation: `100 × (1 - 0.1811) × (1 + 0.2629) × (1 + 0.2502) = 129.294285`; cumulative `29.29%`; CAGR `8.941496%` → `8.94%`.
- Current NAV TR YTD is `-22.88%` as of `2026-06-30`; current NAV is `US$12.87` as of `2026-07-24`; daily NAV drawdown/recovery history is `ไม่พบข้อมูลที่ยืนยันได้`.

### KTEC Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `122/125`, canonical exchange-qualified identity, formal/current exchange conflict, fund identity, passive-equity type gate, official NAV TR/reinvestment/expense basis, available-period threshold and actual years, explicit 10-year gap, normalized endpoint disclosure, annual NAV rows, S&P 500 cached basis/window, current NAV/YTD as-of dates, filenames, Hong Kong region assignment, canonical geography tag, breadcrumbs, ledger status and next queue pointer.
- Result: local fallback `PASS`; no critical or high-severity finding remained. The 2021 partial and 2025 annual-row gaps are explicit, and the fiscal-year annual-report return is kept separate from the June calendar performance window.

## EWM Sequential Queue Record

- Input row: `123/125`; input ticker: `EWM`; terminal status: `completed_10Y`.
- Canonical identity: `NYSE Arca:EWM`. iShares current product page and SEC filing materials identify EWM as an NYSE Arca equity ETF; no provider slug or guessed exchange is used.
- Type gate: supported passive/index-tracking Malaysia equity ETF. iShares states that EWM seeks to track the MSCI Malaysia Index; current key facts classify it as `Equity`, with no active, leveraged, inverse, option-income, derivative-heavy, bond, commodity, currency-trust, multi-asset or single-stock structure identified in the reviewed official materials.
- Official rolling 10-year NAV TR: iShares performance table reports cumulative `24.54%` and average annual NAV total return `2.22%` for `2016-06-30` to `2026-06-30`; actual years `10.00`. Raw NAV TR endpoints are not disclosed. Normalized `100.00 → 124.54` is an implied endpoint from the official cumulative return, not a raw endpoint.
- Official calendar NAV TR: iShares current performance table reports `2021 -6.30%`, `2022 -6.25%`, `2023 -4.01%`, `2024 20.13%`, `2025 15.37%`. These compound to `16.86%` / CAGR `3.17%` over five complete calendar years. Earlier 2016-2020 annual rows are not surfaced in the reviewed current official capture.
- Current observations: official iShares page gives NAV `US$28.11` as of `2026-07-17` and NAV TR YTD `4.62%` as of `2026-07-17`; expense ratio `0.50%`, benchmark `MSCI Malaysia Index`, inception `1996-03-12`, distribution frequency semi-annual. Market-price return remains separate.
- S&P 500 comparison: cached USD Total Return rows are used for the same complete calendar years `2021-2025`; EWM cumulative `16.86%` / CAGR `3.17%` versus S&P cumulative `96.17%` / CAGR `14.43%`, a CAGR gap of approximately `-11.26 pp`. The cached full 2016-2025 S&P reference is `14.82%` CAGR, but it is not presented as an exact date-to-date match for EWM's rolling 2016-06-30 to 2026-06-30 window.

### EWM Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:EWM` | [iShares official EWM product/performance page](https://www.ishares.com/us/products/239669/ishares-msci-malaysia-etf) | Current identity, equity classification, exchange, benchmark, inception, NAV/YTD, rolling NAV TR, annual NAV TR rows, fees and distributions | Page reviewed `2026-07-26`; NAV/YTD `US$28.11` / `4.62%` as of `2026-07-17`; performance table through `2026-06-30` |
| `NYSE Arca:EWM` | [iShares EWM factsheet](https://www.ishares.com/us/literature/fact-sheet/ewm-ishares-msci-malaysia-etf-fund-fact-sheet-en-us.pdf) | Passive/index profile, benchmark, exchange, inception, expense and NAV TR basis cross-check | Official factsheet URL; reviewed `2026-07-26`; latest available factsheet capture is older than the product-page performance table |
| `NYSE Arca:EWM` | [SEC summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-malaysia-etf-8-31.pdf) | Formal fund identity, passive/index objective, listing and fee disclosures | Current summary prospectus dated `2025-12-30` |
| `NYSE Arca:EWM` | [iShares annual shareholder report](https://www.ishares.com/us/literature/annual-report/ar-ewm-en.pdf) | Official shareholder-report cross-check and total-return convention | Reporting period ending `2025-08-31`; not used to replace the latest June 2026 calendar performance |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) plus cached source-batch convention | Common USD Total Return reference and annual rows | Cached rows as of `2025-12-31`; same calendar years `2021-2025` used |

### EWM Raw Observations And Calculations

| Year | EWM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | -6.30% | 28.71% |
| 2022 | -6.25% | -18.11% |
| 2023 | -4.01% | 26.29% |
| 2024 | 20.13% | 25.02% |
| 2025 | 15.37% | 17.88% |

- Rolling official 10Y NAV TR: cumulative `24.54%`, CAGR `2.22%`, `2016-06-30` to `2026-06-30`, actual years `10.00`; raw endpoints not disclosed; implied normalized endpoint `100.00 → 124.54`.
- Calendar calculation: `100 × Π(1 + annual NAV TR) = 116.864130`; cumulative `16.86%`; CAGR `(116.864130 / 100)^(1/5) - 1 = 3.165918%` → `3.17%`.
- Common-window S&P calculation: cumulative `96.169618%` / CAGR `14.426430%` → `14.43%`; EWM trails by `11.260513 pp` CAGR.
- Current NAV TR YTD is `4.62%` as of `2026-07-17`; raw daily drawdown/recovery history is `ไม่พบข้อมูลที่ยืนยันได้`.

### EWM Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `123/125`, canonical exchange-qualified identity, fund identity, passive-equity type gate, official NAV TR/reinvestment/expense basis, rolling 10-year threshold, normalized endpoint disclosure, annual NAV rows, S&P 500 cached basis/window, current NAV/YTD as-of dates, filenames, Malaysia region assignment, canonical geography tag, breadcrumbs, ledger status and next queue pointer.
- Result: local fallback `PASS`; no critical or high-severity finding remained. The earlier annual-row gap and non-disclosed raw rolling endpoints are explicit; annual NAV and market-price returns are not mixed.

## BABO Sequential Queue Record

- Input row: `124/125`; input ticker: `BABO`; terminal status: `unsupported ETF type`.
- Canonical identity: `NYSE Arca:BABO`. YieldMax's current official product page and SEC summary prospectus identify the ticker and NYSE Arca listing.
- Type gate: unsupported. YieldMax identifies BABO as an `actively managed` ETF designed to generate weekly income by selling call spreads on Alibaba Group Holding Ltd. The official description also states that the fund does not invest directly in BABA, has single-issuer risk, and uses an option-income/derivative implementation. This fails the required passive, index-tracking equity ETF scope; no NAV TR performance artifact, region row, or performance-index row is created.
- Current issuer observations retained only for classification evidence: fund inception `2024-08-07`, gross expense ratio `1.00%`, NAV `US$8.42` and net assets `$14.32M` as of `2026-06-30`, current page data reviewed `2026-07-26`. Distribution rate and option-income figures are not used as performance metrics.

### BABO Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:BABO` | [YieldMax official BABO product page](https://yieldmaxetfs.com/our-etfs/babo/) | Current fund identity, active-management classification, option-income strategy, single-issuer risk, exchange, inception, fee and current fund fields | Page reviewed `2026-07-26`; fund details as of `2026-06-30`; current distribution snapshot as of `2026-07-22` not used as a return metric |
| `NYSE Arca:BABO` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1924868/000199937126004549/babo-497k_022726.htm) | Formal listing, investment objectives and option-income/underlying-security strategy | Prospectus dated `2026-02-27`; current filing for BABO |
| `NYSE Arca:BABO` | [YieldMax 2025 annual shareholder report](https://www.yieldmaxetfs.com/wp-content/uploads/Annual%20TSR/YieldMax%20BABA%20Option%20Income%20Strategy%20ETF.pdf) | Secondary official report identity cross-check only | Reporting period ended `2025-10-31`; not used to calculate ETF performance because type gate fails |

### BABO Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `124/125`, canonical exchange-qualified identity, active/passive classification, single-issuer risk, option-income/derivative structure, exclusion from NAV TR analysis, no performance page/region/index artifacts, ledger status and next queue pointer.
- Result: local fallback `PASS`; no critical or high-severity finding remained. The unsupported-type reason is source-backed and no performance values were inferred or saved.

## KLIP Sequential Queue Record

- Input row: `125/125`; input ticker: `KLIP`; terminal status: `unsupported ETF type`.
- Canonical identity: `NYSE Arca:KLIP`. KraneShares' formal summary prospectus and factsheet identify NYSE Arca; the current product page displays a shortened `NYSE` field, and the exchange wording conflict is disclosed rather than silently resolved to the current-page field.
- Type gate: unsupported. KraneShares identifies KLIP as an active covered-call/buy-write ETF. It buys shares of KWEB and writes/sells corresponding call options on KWEB; the formal prospectus states that the fund employs a covered-call strategy and writes FLEX call options. Covered-call/option-income and derivative-heavy implementation, plus active management, fail the required passive, index-tracking equity ETF scope.
- Current issuer observations retained only for classification evidence: fund inception `2023-01-11`, total annual fund operating expense `0.95%`, primary exchange formal `NYSE Arca`, and current page NAV `US$24.13` as of `2026-07-23`; distribution rate/SEC yield are not used as performance metrics. No performance page, region row, or ETF performance-index row is created.

### KLIP Official Source Map

| Entity | Source | Used for | As-of / note |
|---|---|---|---|
| `NYSE Arca:KLIP` | [KraneShares official KLIP product/performance page](https://kraneshares.com/etf/klip/) | Current fund identity, current-page exchange wording, covered-call strategy, active management, current NAV, fee and fund fields | Page reviewed `2026-07-26`; NAV/performance snapshot as of `2026-07-23` and performance table through `2026-06-30` not used after type gate |
| `NYSE Arca:KLIP` | [KraneShares KLIP factsheet](https://kraneshares.com/resources/factsheet/klip_factsheet.pdf) | Covered-call/buy-write structure and formal exchange cross-check | Factsheet data as of `2026-01-30`; primary exchange `NYSE Arca, Inc.` |
| `NYSE Arca:KLIP` | [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1547576/000182912625005546/kraneshares_497k.htm) | Formal listing, active current-income objective, covered-call strategy, KWEB investment and FLEX options | Prospectus dated `2025-08-01`; current fund name and formal strategy |
| `NYSE Arca:KLIP` | [KraneShares annual shareholder report](https://kraneshares.com/resources/compliance/2026_05_29_klip_annual.TSR.report.pdf) | Active-management and covered-call strategy cross-check | Reporting period ended `2026-03-31`; report explicitly notes the fund is actively managed and does not track an underlying index |

### KLIP Pre-save Review Note

- No independent reviewer or multi-agent reviewer was available in this single-ticker turn. The main agent performed the local checklist from `check-etf-performance/workflow.md`: input row/order `125/125`, canonical exchange-qualified identity, formal/current exchange conflict, active/passive classification, covered-call/option-income and FLEX-derivative structure, exclusion from NAV TR analysis, no performance page/region/index artifacts, ledger terminal status, queue completion and source-batch record.
- Result: local fallback `PASS`; no critical or high-severity finding remained. The queue now has terminal status for all 125 Remaining ETFs rows; no values were inferred for this unsupported fund.
