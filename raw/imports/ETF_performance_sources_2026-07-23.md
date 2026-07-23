---
type: source-batch
topic: ETF performance
accessed: 2026-07-23
input_source: raw/imports/tradingview_etf_list_filtered_2026-07-22.md
input_count: 125
verified_passive_pages: 78
existing_canonical_alias_coverage: 1
unresolved_or_unsupported: 46
review_gate: INDEPENDENT_REVIEW_PASS_AFTER_REGION_COUNT_AND_INDEX_DEDUP_FIX
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-07-23

## Scope and gate

ใช้ check-etf-performance กับ ticker ทั้ง 125 รายการจาก input source. แยก NAV Total Return ออกจาก market price และใช้ S&P 500 Total Return cache 2016-2025 เป็น common reference เมื่อมี annual rows. unsupported ETF type หมายถึง active, derivative-heavy, bond, currency, multi-strategy หรือ single-stock product ที่อยู่นอก ETF v1; unresolved หมายถึงยังยืนยัน canonical issuer/exchange ticker ไม่ได้. Independent reviewer and final re-review returned `PASS`; findings on stale region totals, the `DXJ / DXJJF` alias count, and duplicate region links were corrected.

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Source URL | Gap / resolution note |
|---|---|---|---|---|---|---|
| AAXJ | supported | NASDAQ:AAXJ | Asia ex Japan | 20.12% (2026-07-16) | https://www.ishares.com/us/products/239601/ishares-msci-all-country-asia-ex-japan-etf | raw 10Y endpoints not disclosed |
| ADIV | unsupported | NYSE Arca:ADIV | Asia-Pacific | not applicable | https://www.gafunds.com/our-funds/ | active equity |
| ADVE | unsupported | NYSE Arca:ADVE | Asia-Pacific | not applicable | https://www.matthewsasia.com/funds/etfs/asia-dividend-active-etf/ | active equity |
| AIA | supported | NASDAQ:AIA | Asia ex Japan | NAV US$136.34; date-to-date YTD 40.47% (2026-07-21) | https://www.ishares.com/us/products/239730/ishares-asia-50-etf | official rolling 10Y NAV TR cumulative 298.99% / CAGR 14.84% (2026-06-30); standardized month-end YTD 46.79% (2026-06-30); raw endpoints not disclosed |
| ASEA | supported | NYSE Arca:ASEA | Southeast Asia | not disclosed (not disclosed) | https://www.globalxetfs.com/funds/asea | calendar rows and current YTD not disclosed |
| ASHR | supported | NYSE Arca:ASHR | China | not disclosed (not disclosed) | https://etf.dws.com/en-us/AssetDownload/Index/e73aaa93-92c6-4a51-9233-38ccb329e09b/ASHR-Fact-Sheet.pdf | 2025 annual row and current NAV/YTD not disclosed |
| ASHS | supported | NYSE:ASHS | China | 3.36% (2026-03-31) | https://etf.dws.com/en-us/AssetDownload/Index/1bfed1b5-c933-4199-bdcc-30b0ed651740/ASHS-Fact-Sheet.pdf | current data stale; annual rows and raw 10Y endpoints not disclosed |
| ASIA | unsupported | NYSE Arca:ASIA | Asia ex Japan | not applicable | https://www.matthewsasia.com/funds/etfs/pacific-tiger-active-etf/ | active equity |
| BABO | unsupported | NYSE Arca:BABO | China | not applicable | https://yieldmaxetfs.com/wp-content/uploads/Annual%20TSR/YieldMax%E2%84%A2%20BABA%20Option%20Income%20Strategy%20ETF.pdf | active option-income/derivative |
| BBAX | supported | NYSE Arca:BBAX | Asia-Pacific | 8.20% (2026-06-30) | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBAX.PDF | current NAV and 10Y not disclosed |
| CAS | unsupported | NYSE:CAS | China | not applicable | https://www.simplify.us/etfs/cas-simplify-china-shares-plus-income-etf | derivative-heavy/multi-strategy |
| CBON | unsupported | NYSE Arca:CBON | China | not applicable | https://www.vaneck.com/us/en/investments/chinaamc-china-bond-etf-cbon/overview/?redirectVE=generic | bond ETF |
| CETFF | unresolved | OTC Markets:CETFF | Unresolved | not applicable | https://www.ishares.com/us/products | exact sub-fund not disclosed |
| CGRO | unsupported | NYSE:CGRO | China | not applicable | https://www.cvafunds.com/cgro/ | active equity |
| CHIQ | supported | NYSE Arca:CHIQ | China | not disclosed (not disclosed) | https://www.globalxetfs.com/funds/CHIQ | annual rows and current YTD not disclosed; raw 10Y endpoints not disclosed |
| CNQQ | supported | NASDAQ:CNQQ | China | 14.95% (2026-06-30) | https://funds.rayliant.com/cnqq/ | new fund; exact NAV date and annual rows not disclosed |
| CNXT | supported | NYSE Arca:CNXT | China | 18.65% (2026-04-30) | https://www.vaneck.com/us/en/investments/chinext-etf-cnxt/overview/?redirectVE=generic | current data stale; annual rows and raw 10Y endpoints not disclosed |
| CNYA | supported | Cboe BZX:CNYA | China | 1.13% (2026-07-17) | https://www.ishares.com/us/products/273318/ishares-msci-china-a-etf | annual rows and raw 10Y endpoints not disclosed |
| CQQQ | supported | NYSE Arca:CQQQ | China | not disclosed (not disclosed) | https://www.invesco.com/us/en/financial-products/etfs/invesco-china-technology-etf.html | current NAV/YTD and raw 10Y endpoints not disclosed |
| CSKRF | supported | LSE:CSKR | South Korea | 70.53% (2026-07-21) | https://www.ishares.com/uk/professional/en/products/253733/ishares-msci-korea-ucits-etf-acc-fund?siteEntryPassthrough=true&switchLocale=y | OTC alias; annual rows and 10Y not disclosed |
| CXSE | supported | NASDAQ:CXSE | China | -3.69% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/cxse | annual rows and raw 10Y endpoints not disclosed |
| DBJP | supported | NYSE Arca:DBJP | Japan | not disclosed (not disclosed) | https://etf.dws.com/en-us/AssetDownload/Index/f0a852db-a1b3-40a7-8a97-5dca027cf1b0/DBJP-Fact-Sheet.pdf | annual NAV rows and current NAV/YTD not disclosed |
| DGIN | supported | NYSE Arca:DGIN | India | -12.56% (2026-06-22) | https://www.vaneck.com/us/en/investments/digital-india-etf-dgin/overview/ | current data stale; annual rows not disclosed |
| DXJJF | supported | LSE:DXJ | Japan | 21.90% (2026-06-30) | https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged | existing canonical page refreshed; official 2016-2025 NAV TR rows and normalized 10-year calculation; latest NAV US$55.035 (2026-07-22); OTC alias retained |
| EEMA | supported | NASDAQ:EEMA | Emerging Markets | 17.88% (2026-07-17) | https://www.ishares.com/us/products/239629/ishares-msci-emerging-markets-asia-etf | raw 10Y endpoints not disclosed |
| EIDO | supported | NYSE Arca:EIDO | Indonesia | -30.08% (2026-07-21) | https://www.ishares.com/ch/professionals/en/products/239661/ishares-msci-indonesia-etf?switchLocale=Y | raw 10Y endpoints not disclosed; earlier annual rows not surfaced |
| ENZL | supported | NASDAQ:ENZL | New Zealand | 3.45% (2026-07-21) | https://www.ishares.com/us/products/239672/ishares-msci-new-zealand-capped-etf | raw 10Y endpoints not disclosed |
| EPHE | supported | NYSE Arca:EPHE | Philippines | 3.93% (2026-07-21) | https://www.ishares.com/us/products/239675/ishares-msci-philippines-etf | raw 10Y endpoints not disclosed; earlier annual rows not shown |
| EPI | supported | NYSE Arca:EPI | India | -7.91% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/epi | raw 10Y endpoints not disclosed |
| EPP | supported | NYSE Arca:EPP | Asia-Pacific | 11.23% (2026-07-21) | https://www.ishares.com/us/products/239674/ishares-msci-pacific-ex-japan-etf | official rolling 10Y NAV TR cumulative 103.63% / CAGR 7.37%; annual rows 2016-2025; raw NAV endpoint levels not disclosed |
| EWJV | supported | NASDAQ:EWJV | Japan | 17.90% (2026-07-21) | https://www.ishares.com/us/products/307263/ishares-msci-japan-value-etf | fund under 10 years; raw 10Y not available |
| EWM | supported | NYSE Arca:EWM | Malaysia | 4.62% (2026-07-17) | https://www.ishares.com/us/products/239669/EWM | raw 10Y endpoints not disclosed; earlier annual rows not surfaced |
| EWS | supported | NYSE Arca:EWS | Singapore | 16.50% (2026-07-21) | https://www.ishares.com/us/products/239678/ishares-msci-singapore-capped-etf | raw 10Y endpoints not disclosed; earlier annual rows not shown |
| EWT | supported | NYSE Arca:EWT | Taiwan | 54.11% (2026-07-17) | https://www.ishares.com/us/products/239686/EWT | raw 10Y endpoints not disclosed |
| EWY | supported | NYSE Arca:EWY | South Korea | 75.82% (2026-07-21) | https://www.ishares.com/us/products/239681/ | raw endpoints not disclosed |
| FCA | supported | NASDAQ:FCA | China | not disclosed (not disclosed) | https://www.ftportfolios.com/Retail/etf/ETFsummary.aspx?Ticker=FCA | annual rows and current YTD not disclosed |
| FJP | supported | NASDAQ:FJP | Japan | 14.26% (2026-06-30) | https://www.ftportfolios.com/Retail/etf/etfsummary.aspx?Ticker=FJP | raw 10Y endpoints not disclosed; methodology changed |
| FLAX | supported | NYSE Arca:FLAX | Asia ex Japan | 22.35% (2026-07-10) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26346/SINGLCLASS/franklin-ftse-asia-ex-japan-etf/FLAX | annual rows not disclosed; fund under 10 years; current snapshot stale |
| FLCH | supported | NYSE Arca:FLCH | China | -10.65% (2026-07-10) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26362/SINGLCLASS/franklin-ftse-china-etf/FLCH | annual rows not disclosed; current snapshot stale |
| FLIBF | supported | OTC Markets:FLIBF | India | -9.47% (2026-05-31) | https://www.franklintempleton.co.uk/our-funds/etf/price-and-performance/products/27853/SINGLCLASS/franklin-ftse-india-ucits-etf/IE00BHZRQZ17 | OTC alias; official listings LSE FRIN/FLXI; current NAV not disclosed |
| FLIN | supported | NYSE Arca:FLIN | India | not disclosed (not disclosed) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26348/SINGLCLASS/franklin-ftse-india-etf/FLIN | current performance and annual rows not disclosed; fund under 10 years |
| FLJH | supported | NYSE Arca:FLJH | Japan | 22.91% (2026-07-07) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26355/SINGLCLASS/franklin-ftse-japan-hedged-etf/FLJH | annual rows not disclosed; current snapshot stale |
| FLKR | supported | NYSE Arca:FLKR | South Korea | 86.35% (2026-07-07) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26353/SINGLCLASS/franklin-ftse-south-korea-etf/FLKR | raw 10Y unavailable; current snapshot 2026-07-07 |
| FLTW | supported | NYSE Arca:FLTW | Taiwan | 63.10% (2026-07-10) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26351/SINGLCLASS/franklin-ftse-taiwan-etf/FLTW | official NAV annual rows 2018-2025; history under 10 years; 2021-2025 CAGR 13.48% |
| FPA | supported | NASDAQ:FPA | Asia ex Japan | 42.71% (2026-06-30) | https://www.ftportfolios.com/Retail/etf/EtfSummary.aspx?Ticker=FPA | raw 10Y endpoints not disclosed; methodology changed |
| FXA | unsupported | NYSE Arca:FXA | Australia | not applicable | https://www.invesco.com/us/en/financial-products/etfs/invesco-currencyshares-australian-dollar-trust.html | currency trust |
| FXY | unsupported | NYSE Arca:FXY | Japan | not applicable | https://www.invesco.com/us/en/financial-products/etfs/invesco-currencyshares-japanese-yen-trust.html | currency trust |
| GIND | unsupported | NASDAQ:GIND | India | not applicable | https://am.gs.com/public-assets/documents/16dd63b3-1093-11f0-a26b-87cd5783a190?view=true | active semi-transparent equity |
| GLIN | supported | NYSE Arca:GLIN | India | 0.47% (2026-06-24) | https://www.vaneck.com/us/en/investments/india-growth-leaders-etf-glin/ | annual rows and current July data not disclosed |
| GMF | supported | NYSE Arca:GMF | Asia-Pacific | 12.56% (2026-06-30) | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-emerging-asia-pacific-etf-gmf | annual rows and current YTD refresh not disclosed |
| GSJY | supported | NYSE Arca:GSJY | Japan | not disclosed (not disclosed) | https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e | current performance and annual rows not disclosed |
| GXC | supported | NYSE Arca:GXC | China | -10.99% (2026-06-30) | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-china-etf-gxc | current NAV and annual rows not disclosed; raw 10Y endpoints not disclosed |
| HEWJ | supported | NYSE Arca:HEWJ | Japan | 18.81% (2026-07-17) | https://www.ishares.com/us/products/259624/ishares-currency-hedged-msci-japan-etf | raw 10Y endpoints not disclosed |
| ICNYF | unsupported | LSE:CNYB | China | not applicable | https://www.ishares.com/uk/individual/en/literature/fact-sheet/cnyb-ishares-china-cny-bond-ucits-etf-fund-fact-sheet-en-gb.pdf | bond ETF and input alias unresolved |
| IHREF | unresolved | OTC Markets:IHREF | Japan | not applicable | https://www.ishares.com/uk/individual/en/literature/fact-sheet/sjpa-ishares-core-msci-japan-imi-ucits-etf-fund-fact-sheet-en-gb.pdf | primary listing code not verified |
| IHRMF | unresolved | OTC Markets:IHRMF | Japan | not applicable | https://www.ishares.com/uk/individual/en/products/251866/ishares-msci-japan-ucits-etf-inc-fund | primary listing code not verified |
| IHRPF | supported | OTC Markets:IHRPF | China | not disclosed (not disclosed) | https://www.ishares.com/uk/individual/en/products/251798/ishares-china-large-cap-ucits-etf | OTC alias; official listings FXC/IDFX; current NAV/YTD not disclosed |
| IHSEF | supported | LSE:IAPD | Asia-Pacific | 14.55% (2026-07-21) | https://www.ishares.com/uk/individual/en/products/251567/ishares-asia-pacific-dividend-ucits-etf?siteEntryPassthrough=true&switchLocale=y | OTC alias; fee and raw 10Y endpoints not disclosed |
| IMSCF | supported | LSE:CJPU | Japan | 12.11% (2026-07-17) | https://www.ishares.com/uk/professional/en/products/253732/ishares-msci-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y | OTC alias; annual rows and 10Y not disclosed |
| IMVP | supported | NYSE Arca:IMVP | India | not disclosed (not disclosed) | https://www.sec.gov/Archives/edgar/data/1419139/000119312526062436/d71791d497k.htm | ticker changed from PIN; current NAV/YTD and annual rows not disclosed |
| INCO | supported | NYSE Arca:INCO | India | -9.92% (2026-05-31) | https://www.columbiathreadneedleus.com/investment-products/mutual-funds/columbia-india-consumer-etf/class-/details?cusip=19762B707 | official 10-year average annual NAV TR 8.72% as of 2026-05-31; annual rows 2021-2025; latest NAV US$59.45 as of 2026-06-23; 2016-2020 annual rows and raw endpoints not disclosed |
| IND | supported | NASDAQ:IND | India | not disclosed (not disclosed) | https://etf.dws.com/download/asset/048952ad-b7d4-462d-95c8-e726ff2484bd | new fund; no complete annual history and current YTD not disclosed |
| INDA | supported | Cboe BZX:INDA | India | -9.33% (2026-07-17) | https://www.ishares.com/us/products/239659/INDA | raw 10Y endpoints not disclosed |
| INDE | unsupported | NYSE Arca:INDE | India | not applicable | https://us.matthewsasia.com/funds/etfs/india-active-etf/ | active equity |
| INDH | supported | Nasdaq:INDH | India | -9.04% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/indh | new fund; annual rows not disclosed |
| INDQ | supported | Nasdaq:INDQ | India | not disclosed (not disclosed) | https://www.paceretfs.com/products/indq | new fund; current performance and annual rows not disclosed |
| INDZ | unsupported | not disclosed:INDZ | India | not applicable | https://www.vaneck.com/us/en/investments/india-select-etf-indz/ | active equity and exchange unresolved |
| INQQ | supported | NYSE Arca:INQQ | India | not disclosed (not disclosed) | https://emqqglobaletfs.com/inqq-fund-materials | fiscal rows only; current NAV/YTD not disclosed |
| IOPP | unsupported | NYSE:IOPP | India | not applicable | https://www.simplify.us/etfs/iopp-simplify-tara-india-opportunities-etf | active equity |
| IPAC | supported | NYSE Arca:IPAC | Asia-Pacific | 13.97% (2026-07-21) | https://www.ishares.com/us/products/264619/ishares-core-msci-pacific-etf | raw 10Y endpoints not disclosed |
| ISAGF | unsupported | OTC Markets:ISAGF | Emerging Markets | not applicable | https://www.ishares.com/uk/individual/en/products/251723/ishares-emerging-asia-local-government-bond-ucits-etf | bond ETF and official listing SGEA |
| ISMJF | supported | LSE:CPXJ | Asia-Pacific | not disclosed (not disclosed) | https://www.ishares.com/uk/professional/en/products/253735/ishares-core-msci-pacific-ex-japan-ucits-etf-acc-fund?siteEntryPassthrough=true&switchLocale=y | OTC alias; inception/current performance not disclosed |
| ISRVF | supported | LSE:IJPD | Japan | 17.84% (2026-07-20) | https://www.ishares.com/uk/professional/en/products/257514/ijpd?siteEntryPassthrough=true | OTC alias; official rolling 10Y NAV TR CAGR 17.02%; calendar rows 2016-2025; currency-hedge derivatives are an overlay |
| ISSSF | supported | LSE:SAUS | Australia | 14.49% (2026-05-07) | https://www.ishares.com/uk/professional/en/products/251851/saus | OTC alias; current data only as of May 2026 |
| ISVBF | supported | OTC Markets:ISVBF | China | -9.29% (2026-07-20) | https://www.ishares.com/uk/individual/en/products/308751/ishares-msci-china-ucits-etf | OTC alias; official listing ICHN; raw endpoints not disclosed |
| JAPN | unsupported | NYSE Arca:JAPN | Japan | not applicable | https://horizonkinetics.com/products/etf/japn/ | active equity |
| JCHI | unsupported | NYSE Arca:JCHI | China | not applicable | https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JCHI.PDF | active equity |
| JPAN | unsupported | NYSE Arca:JPAN | Japan | not applicable | https://us.matthewsasia.com/funds/etfs/japan-active-etf/ | active equity |
| JPXN | unresolved | TSE:1364 | Japan | not applicable | https://www.blackrock.com/jp/individual-en/en/literature/fact-sheet/1364-ishares-jpx-nikkei-400-etf-fund-fact-sheet-en-jp.pdf | input alias not resolved to canonical ticker |
| JPY | unsupported | NYSE Arca:JPY | Japan | not applicable | https://www.lazardassetmanagement.com/us/en_us/investment-solutions/how-to-invest/108/6244 | active equity |
| KBA | supported | NYSE:KBA | China | 11.37% (2026-06-30) | https://kraneshares.com/etf/kba/ | annual rows and raw 10Y endpoints not disclosed |
| KBUF | unsupported | NYSE:KBUF | China | not applicable | https://kraneshares.com/etf/kbuf/ | derivative-heavy defined outcome |
| KCAI | supported | NYSE:KCAI | China | 4.27% (2026-06-30) | https://kraneshares.com/etf/kcai/ | new fund; calendar rows and net expense not disclosed |
| KDEF | supported | NYSE Arca:KDEF | South Korea | -8.13% (2026-06-30) | https://plusetf.com/kdef | new fund; no complete annual NAV rows |
| KGRN | supported | NYSE Arca:KGRN | China | -13.22% (2026-06-30) | https://kraneshares.com/etf/kgrn/ | fiscal-year return, not calendar-year; calendar rows not disclosed |
| KHYB | unsupported | NYSE Arca:KHYB | Asia-Pacific | not applicable | https://kraneshares.com/etf/khyb/ | active bond/fixed income |
| KLIP | unsupported | NYSE Arca:KLIP | China | not applicable | https://kraneshares.com/etf/klip/ | active covered-call/derivative |
| KMCA | supported | NYSE Arca:KMCA | South Korea | -5.14% (2026-06-30) | https://plusetf.com/kmca | new fund; no complete annual history |
| KPHO | supported | NYSE Arca:KPHO | Vietnam | -2.52% (2026-06-30) | https://kraneshares.com/etf/kpho/ | new fund; no complete annual history and current NAV not disclosed |
| KPRO | unsupported | NYSE:KPRO | China | not applicable | https://kraneshares.com/etf/kpro/ | derivative-heavy defined outcome |
| KRANF | unresolved | OTC Markets:KRANF | China | not applicable | https://kraneshares.com/resources/KIID-for-Class-USD-KraneShares-ICAV-KraneShares-CSI-China-Internet-U-1.pdf | OTC alias and official listing not verified |
| KSTR | supported | NYSE Arca:KSTR | China | 71.70% (2026-06-30) | https://kraneshares.com/etf/kstr/ | newer fund; annual rows not disclosed |
| KTEC | supported | NYSE Arca:KTEC | Hong Kong | -22.88% (2026-06-30) | https://kraneshares.com/etf/ktec/ | newer fund; annual rows not disclosed |
| KURE | supported | NYSE Arca:KURE | China | -8.80% (2026-06-30) | https://kraneshares.com/etf/kure/ | fiscal-year return only; calendar rows not disclosed |
| MAGC | unsupported | CBOE BZX:MAGC | China | not applicable | https://www.roundhillinvestments.com/etf/magc/ | active equity/total-return swaps |
| MCH | unsupported | NYSE Arca:MCH | China | not applicable | https://us.matthewsasia.com/funds/etfs/china-active-etf/ | active equity |
| MCHI | supported | NASDAQ:MCHI | China | -9.33% (2026-07-21) | https://www.ishares.com/us/products/239619/ishares-msci-china-etf | raw 10Y endpoints not disclosed; earlier annual rows not shown |
| MCHS | unsupported | NYSE Arca:MCHS | China | not applicable | https://www.matthewsasia.com/funds/etfs/china-innovators-active-etf/ | active equity |
| MINV | unsupported | NYSE Arca:MINV | Asia ex Japan | not applicable | https://us.matthewsasia.com/funds/etfs/asia-innovators-active-etf/ | active equity |
| MJSC | unsupported | NYSE Arca:MJSC | Japan | not applicable | https://www.mufgetfs.com/mjsc | active equity |
| MKOR | unsupported | NYSE:MKOR | South Korea | not applicable | https://us.matthewsasia.com/funds/etfs/korea-active-etf/ | active equity |
| NBCE | unsupported | NYSE Arca:NBCE | China | not applicable | https://www.nb.com/products/etfs/china-equity-etf | active equity |
| NBJP | unsupported | NYSE Arca:NBJP | Japan | not applicable | https://www.nb.com/products/etfs/japan-equity-etf | active equity |
| NDIA | unsupported | NYSE Arca:NDIA | India | not applicable | https://www.globalxetfs.com/funds/ndia | active equity |
| NFTY | supported | NASDAQ:NFTY | India | -7.45% (2026-06-30) | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Print=Y&Ticker=NFTY | raw 10Y endpoints not disclosed; methodology changed |
| PCCE | unsupported | NYSE Arca:PCCE | China | not applicable | https://www.polencapital.com/sites/default/files/Polen_ETF%20Suite%20Brochure_Final.pdf | active equity |
| PGJ | supported | NASDAQ:PGJ | China | not disclosed (not disclosed) | https://www.invesco.com/us-rest/contentdetail?contentId=bc42fd05f0e21410VgnVCM100000c2f1bf0aRCRD&dnsName=us | current NAV/YTD and inception not disclosed; raw 10Y endpoints not disclosed |
| RAYJ | unsupported | NYSE:RAYJ | Japan | not applicable | https://funds.rayliant.com/rayj/ | active equity |
| SCJ | supported | NYSE Arca:SCJ | Japan | 14.73% (2026-07-17) | https://www.ishares.com/us/products/239666/ishares-msci-japan-smallcap-etf | raw 10Y endpoints not disclosed |
| SMHC | supported | NASDAQ:SMHC | China | not disclosed (not disclosed) | https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/ | new fund; no complete annual history and current YTD not disclosed |
| SMIN | supported | Cboe BZX:SMIN | India | -0.58% (2026-07-21) | https://www.ishares.com/us/products/239660/SMIN | annual rows and raw 10Y endpoints not disclosed |
| TCHI | supported | NASDAQ:TCHI | China | -0.38% (2026-07-20) | https://www.ishares.com/us/products/325390/ishares-msci-china-multisector-tech-etf | fund under 10 years; raw 10Y not available |
| THD | supported | NYSE Arca:THD | Thailand | 26.86% (2026-07-21) | https://www.ishares.com/us/products/239688/ishares-msci-thailand-capped-etf | raw 10Y endpoints not disclosed |
| TMH | unsupported | NYSE Arca:TMH | Japan | not applicable | https://adrhedged.com/security/toyota-motor-corporation-adrhedged/ | single-stock ADR-hedged ETF |
| TSMY | unsupported | NYSE Arca:TSMY | Taiwan | not applicable | https://yieldmaxetfs.com/our-etfs/tsmy/ | active derivative/option-income |
| VFJUF | unresolved | OTC Markets:VFJUF | Unresolved | not applicable | https://www.vanguard.co.uk/uk-fund-directory/product?product-type=etf | OTC symbol not mapped to unique fund/ISIN |
| VFPAF | unresolved | OTC Markets:VFPAF | Unresolved | not applicable | https://www.vanguard.co.uk/uk-fund-directory/product?product-type=etf | OTC symbol not mapped to unique fund/ISIN |
| VGDTF | unresolved | OTC Markets:VGDTF | Unresolved | not applicable | https://www.vanguard.co.uk/uk-fund-directory/product?product-type=etf | OTC symbol not mapped to unique fund/ISIN |
| VGUDF | unresolved | OTC Markets:VGUDF | Unresolved | not applicable | https://www.vanguard.co.uk/uk-fund-directory/product?product-type=etf | OTC symbol not mapped to unique fund/ISIN |
| VNAM | supported | NYSE Arca:VNAM | Vietnam | not disclosed (not disclosed) | https://www.globalxetfs.com/funds/vnam | annual rows and current YTD not disclosed |
| VNFGF | unresolved | OTC Markets:VNFGF | Japan | not applicable | https://www.vanguard.co.uk/professional/product/etf/equity/9505/ftse-japan-ucits-etf-usd-distributing | primary listing code not verified |
| VNM | supported | NYSE Arca:VNM | Vietnam | -2.31% (2026-06-23) | https://www.vaneck.com/us/en/investments/vietnam-etf-vnm/ | inception, fee, annual rows not disclosed; current snapshot stale |
| VPL | supported | NYSE Arca:VPL | Asia-Pacific | 28.39% (2026-05-31) | https://investor.vanguard.com/investment-products/etfs/profile/vpl | current NAV and annual rows not disclosed |
| WDAF | supported | Nasdaq:WDAF | Asia-Pacific | 6.77% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/wdaf | new fund; annual rows not disclosed |
| WDTRF | supported | LSE:DXJA | Japan | 21.90% (2026-06-30) | https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BYQCZD50/ | OTC alias; official 2018-2025 annual rows; history under 10 years; since-inception NAV TR CAGR 17.07% |

## Benchmark convention

Annual benchmark rows use S&P 500 Total Return in USD with dividends reinvested, cached as of 2025-12-31: 2016 11.96%, 2017 21.83%, 2018 -4.38%, 2019 31.49%, 2020 18.40%, 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%. It is a common reference, not each ETF's issuer benchmark. Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/

## Ownership and graph notes

- Numeric owner is each wiki/analysis/performance/ETF_* Performance.md page; region pages are static navigation summaries only.
- Missing values remain not disclosed; no annual return was inferred from price return, fiscal-year return, or a shorter rolling period.
- Cleanup on 2026-07-23 removed 45 empty annual NAV Total Return placeholder rows (`| — | not disclosed | not disclosed |`) from the corresponding performance pages; no sourced numeric values were changed.
- Existing canonical coverage: DXJJF is the OTC alias for existing ETF_LSE_DXJ Performance; no duplicate page was created.
- Unresolved aliases retained in the register: IHREF, JPXN, VNFGF, IHRMF, KRANF and the Vanguard/iShares OTC symbols.

## EWY Sequential Queue Record

- Input row: `1/125`; input ticker: `EWY`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:EWY`; issuer page explicitly identifies the exchange and fund as iShares MSCI South Korea ETF. No provider slug or unverified exchange alias is used.
- Classification: supported passive/index-tracking single-country South Korea equity ETF. Issuer benchmark: `MSCI Korea 25/50 Index (Net)`. Inception: `2000-05-09`. Expense ratio: `0.59%`. Distribution frequency: annual.
- Official current observations: NAV `US$169.65` as of `2026-07-22`; NAV Total Return YTD `+75.82%` as of `2026-07-21`; 3-year standard deviation `41.20%` and equity beta `1.87` as of `2026-06-30`.

### EWY Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:EWY` | [iShares US product page](https://www.ishares.com/us/products/239681/ishares-msci-south-korea-capped-etf) | Fund identity, exchange, benchmark, inception, current NAV/YTD, expense ratio, classification and risk statistics | Page accessed `2026-07-23`; NAV `2026-07-22`; YTD `2026-07-21`; risk fields `2026-06-30` / `2026-07-22` |
| `NYSE Arca:EWY` | [iShares UK professional performance page](https://www.ishares.com/uk/professional/en/products/239681/ewy?siteEntryPassthrough=true&switchLocale=y) | Official calendar-year NAV Total Return rows 2016-2025 and rolling 10-year performance | Performance as of `2026-06-30`; 2016-2020 issuer display is one decimal; 2021-2025 rows corroborated by US factsheet |
| `NYSE Arca:EWY` | [iShares EWY US factsheet](https://www.ishares.com/us/literature/fact-sheet/ewy-ishares-msci-south-korea-etf-fund-fact-sheet-en-us.pdf) | NAV return definition, distributions reinvested, expenses deducted, annual rows 2021-2025 and fee | Factsheet as of `2026-06-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source batch convention | Common-reference benchmark identity and 2016-2025 annual rows | Cached benchmark as of `2025-12-31`; USD Total Return with dividends reinvested |

### EWY Raw Observations And Calculations

| Year | EWY NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.10% | 11.96% |
| 2017 | 44.40% | 21.83% |
| 2018 | -20.30% | -4.38% |
| 2019 | 8.30% | 31.49% |
| 2020 | 39.70% | 18.40% |
| 2021 | -7.56% | 28.71% |
| 2022 | -26.70% | -18.11% |
| 2023 | 19.05% | 26.29% |
| 2024 | -20.79% | 25.02% |
| 2025 | 97.57% | 17.88% |

- Official rolling 10-year cumulative NAV Total Return: `369.17%` as of `2026-06-30`; normalized start/end values are `100.00` and `469.17` for `2016-06-30` to `2026-06-30`, actual elapsed `10.00` years. Raw NAV TR endpoint levels are `ไม่พบข้อมูลที่ยืนยันได้`.
- Official rolling 10-year NAV TR CAGR: `(469.17 / 100.00)^(1 / 10.00) - 1 = 16.72%`, using the issuer's rounded cumulative display. This is not the 2016-2025 calendar-row CAGR.
- Rounded 2016-2025 calendar rows compound to cumulative `135.42%` and CAGR `8.94%`; 2021-2025 rows compound to `26.24%` and CAGR `4.77%`; up/down years are `6 / 4`.
- Best / least positive / worst / least bad down year: `2025 +97.57%` / `2019 +8.30%` / `2022 -26.70%` / `2021 -7.56%`.
- Exact June-to-June S&P 500 TR for the rolling 10-year endpoints is `ไม่พบข้อมูลที่ยืนยันได้`; S&P rows in the performance page are the cached complete calendar-year comparison only.
- Official daily NAV history sufficient to reproduce max drawdown and recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

### EWY Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from `check-etf-performance/workflow.md` before writing: ticker/exchange, passive-equity classification, NAV Total Return definition, distributions, annual rows, rolling 10-year endpoints and formula, S&P 500 basis/window, as-of dates, best/worst ranking, filenames, region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable `lean` workflow.

## EPP Sequential Queue Record

- Input row: 6/125; input ticker: EPP; terminal status: completed_10Y.
- Canonical entity key: NYSE Arca:EPP; the official iShares product page identifies the NYSE Arca listing, EPP ticker, fund identity, equity asset class, and MSCI Pacific ex Japan Index (Net). No provider slug or guessed exchange is used.
- Classification: supported passive/index-tracking developed Asia-Pacific equity ETF. The issuer objective is to track Pacific region developed-market equities excluding Japan; it is not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock.
- Inception: 2001-10-25. Expense ratio: 0.47%. Distribution frequency: semi-annual. Current NAV: US$55.53 as of 2026-07-22; current NAV Total Return YTD: 11.23% as of 2026-07-21.

### EPP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:EPP | [iShares US EPP product page](https://www.ishares.com/us/products/239674/ishares-msci-pacific-ex-japan-etf) | Canonical listing, identity, asset class, tracked index, inception, current NAV/YTD, fee, holdings, exposure, risk and performance | Page accessed 2026-07-23; NAV 2026-07-22; YTD 2026-07-21; risk/portfolio fields 2026-06-30 and 2026-07-22 |
| NYSE Arca:EPP | [iShares EPP professional performance page](https://www.ishares.com/ch/professionals/en/products/239674/ishares-msci-pacific-ex-japan-etf) | Official NAV Total Return basis, calendar rows 2016-2025 and rolling 10-year return | Performance as of 2026-06-30; 2016-2020 issuer display is one decimal; 2021-2025 rows are shown at two decimals in current rendering |
| S&P 500 TR | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common-reference benchmark identity and annual rows | Cached USD Total Return rows as of 2025-12-31 |

### EPP Raw Observations And Calculations

| Year | EPP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.40% | 11.96% |
| 2017 | 25.40% | 21.83% |
| 2018 | -10.70% | -4.38% |
| 2019 | 17.90% | 31.49% |
| 2020 | 6.00% | 18.40% |
| 2021 | 4.42% | 28.71% |
| 2022 | -6.45% | -18.11% |
| 2023 | 5.92% | 26.29% |
| 2024 | 4.04% | 25.02% |
| 2025 | 20.16% | 17.88% |

- Official rolling 10-year cumulative NAV Total Return: 103.63% as of 2026-06-30, represented by 2016-06-30 to 2026-06-30; actual elapsed years 10.00. Raw NAV endpoint levels are ไม่พบข้อมูลที่ยืนยันได้.
- Normalized calculation used on the performance page: start 100.00; end 203.63; (203.63 / 100.00)^(1 / 10.00) - 1 = 7.37%. The normalized endpoints represent the issuer cumulative display, not published NAV levels.
- Rounded complete calendar rows 2016-2025 compound to 94.42% and annualize to 6.87% over 10 years. Rows 2021-2025 compound to 29.35% and annualize to 5.28% over 5 years.
- Up/down years among complete rows: 8 / 2. Best 2017 +25.40%; least positive 2024 +4.04%; worst 2018 -10.70%; least bad down year 2022 -6.45%.
- Official current NAV Total Return YTD: 11.23% as of 2026-07-21. This is kept separate from the NAV level of US$55.53 as of 2026-07-22.
- Exact June-to-June S&P 500 TR for the rolling 10-year endpoints is ไม่พบข้อมูลที่ยืนยันได้; annual S&P rows are the cached complete-calendar-year comparison only.
- Daily NAV history sufficient to reproduce max drawdown and recovery is ไม่พบข้อมูลที่ยืนยันได้.

### EPP Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from check-etf-performance/workflow.md before writing: ticker/exchange, passive-equity classification, NAV Total Return definition, income reinvestment and expenses, annual rows and source precision, rolling 10-year coverage/endpoints/formula, S&P 500 basis/window, as-of dates, best/worst ranking, filenames, Asia-Pacific region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: PASS; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable lean workflow.

## DXJJF Sequential Queue Record

- Input row: 7/125; input ticker: DXJJF; terminal status: completed_10Y.
- Canonical entity key: LSE:DXJ. WisdomTree's official page identifies LSE ticker DXJ, ISIN IE00BVXC4854, and the same USD-distributing share class; the input DXJJF is retained as an OTC alias and is not used as the canonical displayed key.
- Classification: supported passive/index-tracking single-country Japan equity ETF. The fund is physical and fully replicated; monthly currency forwards are a JPY/USD hedge overlay, not a derivative-heavy classification. It is not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, or single-stock.
- Issuer benchmark: WisdomTree Japan Hedged Equity UCITS Index, USD, Bloomberg WTIDJHUT. Inception: 2015-05-18. TER: 0.48% as of 2026-07-22. Distribution frequency: semi-annual; use of income: distributing.

### DXJJF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:DXJ | [WisdomTree official product page](https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged) | Canonical listing, ISIN, identity, passive physical structure, inception, current NAV, TER, holdings, sector/country exposure and index | Page accessed 2026-07-23; product/NAV/holdings/sector fields as of 2026-07-22; NAV US$55.035 |
| LSE:DXJ | [Official WisdomTree factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BVXC4854/) | Official NAV Total Return basis, annual 2016-2025 rows, current YTD, benchmark and fees | Document/data as of 2026-06-30; YTD 21.90%; annual rows net of fees |
| LSE:DXJ | [WisdomTree performance definition](https://www.wisdomtree.eu/de-de/etfs/export-tilted/wisdomtree-japan-equity-ucits-etf-usd-hedged) | Daily NAV, net-of-fees, dividend-reinvestment convention | Page accessed 2026-07-23 |
| S&P 500 TR | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of 2025-12-31 |

### DXJJF Raw Observations And Calculations

| Year | DXJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.73% | 11.96% |
| 2017 | 22.17% | 21.83% |
| 2018 | -18.71% | -4.38% |
| 2019 | 18.53% | 31.49% |
| 2020 | 2.82% | 18.40% |
| 2021 | 18.07% | 28.71% |
| 2022 | 6.48% | -18.11% |
| 2023 | 40.46% | 26.29% |
| 2024 | 30.55% | 25.02% |
| 2025 | 31.19% | 17.88% |

- Ten official complete calendar-year rows 2016-2025 compound to cumulative 268.73% and CAGR 13.94% over 10 years. Start date is 2015-12-31, end date is 2025-12-31, normalized start/end TR values are 100.00 and 368.73, and actual years are 10.00. Raw NAV endpoint levels are ไม่พบข้อมูลที่ยืนยันได้.
- Formula: (368.73 / 100.00)^(1 / 10.00) - 1 = approximately 13.94%; the normalized end value and CAGR use rounded official annual inputs.
- Rows 2021-2025 compound to cumulative 202.44% and CAGR 24.77%; corresponding cached S&P 500 TR is 96.17% and 14.43%.
- Up/down years among complete rows: 9 / 1. Best 2023 +40.46%; least positive 2016 +0.73%; worst and least bad down year 2018 -18.71%.
- Official NAV Total Return YTD: 21.90% as of 2026-06-30. Official performance beyond that date is ไม่พบข้อมูลที่ยืนยันได้. Latest issuer NAV is US$55.035 as of 2026-07-22 and is not a return metric.
- Annual-return population standard deviation from rounded rows: 16.69%; this is a calculation, not an issuer 3-year volatility statistic.
- Official daily NAV history sufficient to reproduce max drawdown and recovery: ไม่พบข้อมูลที่ยืนยันได้. OTC quote history is not used for NAV TR.

### DXJJF Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from check-etf-performance/workflow.md before writing: ticker/alias and exchange resolution, passive-equity classification, NAV Total Return definition, distributions and expenses, annual rows and complete-year eligibility, normalized endpoints and formula, S&P 500 basis/window, visible as-of dates, best/worst ranking, filenames, Japan region assignment, canonical geography tag, breadcrumbs, existing-page ownership, and link targets.
- Local verdict: PASS; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable lean workflow.

## INCO Sequential Queue Record

- Input row: 8/125; input ticker: INCO; terminal status: completed_10Y.
- Canonical entity key: NYSE Arca:INCO; the official Columbia Threadneedle page identifies the NYSE Arca exchange, INCO ticker, CUSIP 19762B707, and Columbia India Consumer ETF.
- Classification: supported passive/index-tracking equity ETF. The issuer lists management style as Indexed and the objective seeks results corresponding to the Indxx India Consumer Index. The underlying is India consumer equity; it is not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock.
- Inception: 2011-08-10. Issuer benchmark: Indxx India Consumer Index. Net expense ratio: 0.75%; gross expense ratio: 0.76%; waiver expiration: 2026-07-31. Distribution schedule: annual.

### INCO Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:INCO | [Columbia Threadneedle INCO product/performance page](https://www.columbiathreadneedleus.com/investment-products/mutual-funds/columbia-india-consumer-etf/class-/details?cusip=19762B707) | Canonical listing, indexed classification, objective, benchmark, inception, fees, NAV/YTD, return definition and annual rows | Page accessed 2026-07-23; performance as of 2026-05-31; NAV as of 2026-06-23 |
| NYSE Arca:INCO | [Columbia India Consumer ETF factsheet](https://www.columbiathreadneedleus.com/binaries/content/assets/cti/public/columbia_india_consumer_etf_fs.pdf) | Official product and NAV-return corroboration | Factsheet as of 2026-03-31 |
| S&P 500 TR | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common-reference benchmark identity and annual rows | Cached USD Total Return rows as of 2025-12-31 |

### INCO Raw Observations And Calculations

| Year | INCO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 19.70% | 28.71% |
| 2022 | -7.40% | -18.11% |
| 2023 | 34.12% | 26.29% |
| 2024 | 13.78% | 25.02% |
| 2025 | 0.35% | 17.88% |

- Official issuer 10-year average annual NAV Total Return: 8.72% as of 2026-05-31. The implied date window is 2016-05-31 to 2026-05-31, actual years 10.00; raw NAV endpoint levels are ไม่พบข้อมูลที่ยืนยันได้.
- Normalized calculation used on the performance page: start 100.00; end 230.72; (230.72 / 100.00)^(1 / 10.00) - 1 = approximately 8.72%. The normalized end is derived from the issuer's rounded 10-year annualized metric, not an issuer-published endpoint or proxy.
- Complete disclosed calendar rows 2021-2025 compound to 69.74% and annualize to 11.16% over 5 years; corresponding cached S&P 500 TR is 96.17% and 14.43%.
- Up/down years among disclosed complete rows: 4 / 1. Best 2023 +34.12%; least positive 2025 +0.35%; worst and least bad down year 2022 -7.40%.
- Official current NAV Total Return YTD: -9.92% as of 2026-05-31. Latest official NAV is US$59.45 as of 2026-06-23 and is not a return metric.
- Annual rows for 2016-2020 are ไม่พบข้อมูลที่ยืนยันได้ in the selected official source; no values were inferred.
- Annual-return population standard deviation from rounded 2021-2025 rows: 14.59%; this is a calculation, not an issuer 3-year volatility statistic.
- Official daily NAV history sufficient to reproduce max drawdown and recovery: ไม่พบข้อมูลที่ยืนยันได้.

### INCO Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from check-etf-performance/workflow.md before writing: ticker/exchange, indexed passive-equity classification, NAV Total Return definition, reinvested distributions and expenses, issuer 10-year eligibility and normalized endpoints, available annual rows, S&P 500 basis/window, as-of dates, best/worst ranking, filenames, India region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: PASS; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable lean workflow.
## ISRVF Sequential Queue Record

- Input row: `5/125`; input ticker: `ISRVF`; terminal status: `completed_10Y`.
- Canonical entity key: `LSE:IJPD`; official iShares product and performance pages identify the London Stock Exchange ticker `IJPD` for ISIN `IE00BCLWRG39`. `ISRVF` is retained as the input OTC alias and is not used as the canonical exchange-qualified key.
- Classification: supported passive/index-tracking single-country Japan equity ETF. The share class is accumulating and physical/optimised. It uses derivatives for monthly JPY/USD currency hedging; this is a currency hedge overlay, not a derivative-heavy product classification.
- Issuer benchmark: `MSCI Japan 100% Hedged to USD Index (Net)`. Fund launch: `2013-09-30`. Total expense ratio: `0.64%`. Rebalance frequency: quarterly.

### ISRVF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:IJPD` | [iShares UK professional IJPD page](https://www.ishares.com/uk/professional/en/products/257514/ijpd?siteEntryPassthrough=true) | Canonical listing, identity, benchmark, structure, fee, risk fields, annual/rolling performance and current NAV/YTD | Rolling performance as of `2026-06-30`; current NAV/YTD snapshot as of `2026-07-20`; YTD `17.84%` |
| `LSE:IJPD` | [iShares IJPD factsheet](https://www.ishares.com/ch/individual/en/literature/fact-sheet/ijpd-ishares-msci-japan-usd-hedged-ucits-etf-acc-fund-fact-sheet-en-ch.pdf) | Passive classification, NAV return definition, accumulating structure, physical/optimised methodology and fee | Performance as of `2026-02-28`; other data as of `2026-03-05` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### ISRVF Raw Observations And Calculations

| Year | ISRVF / IJPD NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -1.90% | 11.96% |
| 2017 | 20.70% | 21.83% |
| 2018 | -14.10% | -4.38% |
| 2019 | 20.40% | 31.49% |
| 2020 | 9.00% | 18.40% |
| 2021 | 12.80% | 28.71% |
| 2022 | -2.70% | -18.11% |
| 2023 | 34.50% | 26.29% |
| 2024 | 25.60% | 25.02% |
| 2025 | 27.70% | 17.88% |

- Official rolling 10-year cumulative NAV TR: `381.35%` as of `2026-06-30`, represented by `2016-06-30` to `2026-06-30`; actual elapsed years `10.00`. Raw NAV endpoint levels are `ไม่พบข้อมูลที่ยืนยันได้`.
- Normalized calculation used on the performance page: start `100.00`; end `481.35`; `(481.35 / 100.00)^(1 / 10.00) - 1 = 17.02%`. The normalized endpoints represent the issuer's cumulative total-return display, not published NAV levels.
- Rounded complete calendar rows `2016-2025` compound to `+216.04%` and annualize to `12.20%` over `10` years. Rows `2021-2025` compound to `+136.77%` and annualize to `18.81%` over `5` years.
- Up/down years among complete rows: `7 / 3`. Best `2023 +34.50%`; least positive `2019 +20.40%`; worst `2018 -14.10%`; least bad down year `2022 -2.70%`.
- Official current YTD NAV TR: `17.84%` as of `2026-07-20`. This is a NAV total-return figure and is kept separate from the market price/NAV level.
- Exact June-to-June S&P 500 TR for the rolling 10-year window is `ไม่พบข้อมูลที่ยืนยันได้`; annual S&P rows are the cached complete-calendar-year comparison only.
- Daily NAV history sufficient to reproduce max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### ISRVF Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from `check-etf-performance/workflow.md` before writing: ticker/alias and exchange resolution, passive-equity classification, NAV Total Return definition, income reinvestment, annual rows and source precision, rolling 10-year cumulative endpoints and formula, S&P 500 basis/window, as-of dates, best/worst ranking, hedge-overlay classification, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable `lean` workflow.

## FLTW Sequential Queue Record

- Input row: `4/125`; input ticker: `FLTW`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `NYSE Arca:FLTW`; the official Franklin product page identifies the fund, ticker, and NYSE Arca listing. No provider slug or guessed exchange is used.
- Classification: supported passive/indexed single-country Taiwan equity ETF. Franklin describes passive index exposure, an indexed ETF type, and a market-cap weighted large/mid-cap index. It is not bond, commodity, currency trust, multi-asset, active, leveraged, inverse, option-income, derivative-heavy, or single-stock.
- Issuer benchmark: `FTSE Taiwan Capped Index-NR`. Inception: `2017-11-02`. Net expense ratio: `0.19%` as of `2025-08-01`. Distribution frequency: semi-annual.

### FLTW Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:FLTW` | [Franklin FLTW product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26351/SINGLCLASS/franklin-ftse-taiwan-etf/FLTW) | Fund identity, exchange, benchmark, inception, indexed classification, current NAV/YTD, expenses and portfolio snapshot | Product data as of `2026-07-10`; YTD NAV TR `63.10%`; portfolio snapshot `2026-07-10` / `2026-07-12` |
| `NYSE Arca:FLTW` | [Franklin FLTW factsheet](https://www.franklintempleton.com/forms-literature/download/FLTW-FF) | Official NAV Returns and calendar-year returns | Factsheet as of `2026-03-31`; annual rows `2018-2025`; NAV basis assumes distributions reinvested and expenses deducted |
| `NYSE Arca:FLTW` | [Franklin FLTW annual shareholder report](https://www.franklintempleton.com/forms-literature/download-preview/FLTW-ATSR) | Regulatory corroboration of indexed fund structure and NAV performance | Period ended `2026-03-31`; not used for calendar rows because it is a fiscal-year period |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### FLTW Raw Observations And Calculations

| Year | FLTW NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -8.93% | -4.38% |
| 2019 | 30.89% | 31.49% |
| 2020 | 30.41% | 18.40% |
| 2021 | 29.72% | 28.71% |
| 2022 | -27.74% | -18.11% |
| 2023 | 29.78% | 26.29% |
| 2024 | 17.29% | 25.02% |
| 2025 | 31.91% | 17.88% |

- Official 10-year NAV TR is unavailable: inception `2017-11-02` to latest official annual-performance date `2026-06-30` is `3,162` days / `8.66` years, below the required `10.00 elapsed years`; no 10-year proxy was created.
- Complete official calendar rows `2018-2025` compound to `+192.58%` and annualize to `14.36%` over `8` years. Complete rows `2021-2025` compound to `+88.21%` and annualize to `13.48%` over `5` years. Calculations use rounded official NAV inputs.
- Up/down years among complete rows: `6 / 2`. Best `2025 +31.91%`; least positive `2024 +17.29%`; worst `2022 -27.74%`; least bad down year `2018 -8.93%`.
- Official current YTD NAV TR: `63.10%` as of `2026-07-10`; this is an aggregate NAV total return, not an annualized return.
- Exact date-to-date S&P 500 TR for the available since-inception window is `ไม่พบข้อมูลที่ยืนยันได้`; annual S&P rows are the cached complete-calendar-year comparison only.
- Daily NAV history sufficient to reproduce max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### FLTW Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from `check-etf-performance/workflow.md` before writing: ticker/exchange, passive/indexed-equity classification, NAV Total Return definition, reinvested distributions and expenses, annual rows, inception/elapsed-years test, 10-year-unavailable statement, S&P 500 basis/window, as-of dates, best/worst ranking, filenames, Taiwan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable `lean` workflow.

## WDTRF Sequential Queue Record

- Input row: `3/125`; input ticker: `WDTRF`; terminal status: `completed_available_period_no_10Y`.
- Canonical entity key: `LSE:DXJA`; official WisdomTree product and London Stock Exchange pages identify the LSE ticker `DXJA` for ISIN `IE00BYQCZD50`. `WDTRF` is retained as the input OTC alias and is not used as the canonical exchange-qualified key.
- Classification: supported passive/index-tracking single-country Japan equity ETF. The share class is accumulating and physically fully replicated; the USD/JPY hedge uses currency forward contracts, which is a hedging overlay rather than derivative-heavy classification.
- Issuer benchmark: `WisdomTree Japan Hedged Equity UCITS Index`. Inception: `2017-03-07`. Total expense ratio: `0.48%` as of `2026-07-22`. Distribution frequency: `N/A` because the share class is accumulating.

### WDTRF Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `LSE:DXJA` | [WisdomTree UK DXJA product page](https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged-acc) | Canonical product identity, current NAV/AUM, TER, structure, holdings, risk context and official listings | Product data as of `2026-07-22`; NAV `US$70.719`; LSE ticker `DXJA` |
| `LSE:DXJA` | [WisdomTree DXJA factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BYQCZD50/) | Official NAV performance, index, inception and annual calendar returns | Document date `2026-06-30`; YTD `21.90%`, since-inception CAGR `17.07%`, annual rows `2018-2025` |
| `LSE:DXJA` | [London Stock Exchange DXJA company page](https://www.londonstockexchange.com/stock/DXJA/wisdomtree/company-page) | Exchange/listing verification | LSE listing and ISIN `IE00BYQCZD50`; page accessed `2026-07-23` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### WDTRF Raw Observations And Calculations

| Year | WDTRF / DXJA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -18.62% | -4.38% |
| 2019 | 18.47% | 31.49% |
| 2020 | 2.79% | 18.40% |
| 2021 | 18.04% | 28.71% |
| 2022 | 6.58% | -18.11% |
| 2023 | 40.52% | 26.29% |
| 2024 | 30.79% | 25.02% |
| 2025 | 31.14% | 17.88% |

- Official 10-year NAV TR is unavailable: inception `2017-03-07` to latest official performance date `2026-06-30` is `3,402` days / `9.31` years, below the required `10.00 elapsed years`; no 10-year proxy was created.
- Official available-period NAV TR CAGR: `17.07%` since inception as of `2026-06-30`; the issuer does not disclose raw start/end TR levels in the factsheet.
- Official current YTD NAV TR: `21.90%` as of `2026-06-30`; official 1-year NAV TR `52.96%` and 3-year annualized NAV TR `31.38%` as of the same date.
- Complete official calendar rows `2018-2025` compound to `+200.49%` and annualize to `14.74%` over `8` years. Complete rows `2021-2025` compound to `+203.22%` and annualize to `24.84%` over `5` years. Both calculations use rounded issuer annual inputs.
- Up/down years among complete rows: `7 / 1`. Best `2023 +40.52%`; least positive `2020 +2.79%`; worst and least bad down year `2018 -18.62%`.
- Exact date-to-date S&P 500 TR for the since-inception window is `ไม่พบข้อมูลที่ยืนยันได้`; annual S&P rows are the cached complete-calendar-year comparison only.
- Daily NAV history sufficient to reproduce max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### WDTRF Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from `check-etf-performance/workflow.md` before writing: ticker/alias and exchange resolution, passive-equity classification, accumulating NAV Total Return basis, annual rows and partial-year exclusion, available-period coverage and elapsed-years test, since-inception CAGR, S&P 500 basis/window, as-of dates, best/worst ranking, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable `lean` workflow.

## DBJP Sequential Queue Record

- Input row: `2/125`; input ticker: `DBJP`; terminal status: `completed_10Y`.
- Canonical entity key: `NYSE Arca:DBJP`; the official DWS factsheet and summary prospectus identify the NYSE Arca listing and Xtrackers MSCI Japan Hedged Equity ETF. No provider slug or guessed exchange is used.
- Classification: supported passive/index-tracking single-country Japan equity ETF. The fund uses USD/JPY forward contracts for currency hedging; this is a hedging overlay, not a derivative-heavy product classification.
- Issuer benchmark: `MSCI Japan US Dollar Hedged Index`. Inception: `2011-06-08`. Expense ratio: `0.45%` as of `2026-06-30`. Distribution schedule: annual.

### DBJP Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NYSE Arca:DBJP` | [DWS Q2 2026 DBJP factsheet](https://www.dws.com/US/EN/resources/Xtrackers-MSCI-Japan-Hedged-Equity-ETF/DBJP_fact-sheet.pdf) | Fund identity, exchange, tracked index, inception, NAV Total Return, expense ratio, holdings and risk fields | Factsheet as of `2026-06-30`; official NAV TR 10-year `17.28%` |
| `NYSE Arca:DBJP` | [DWS summary prospectus](https://etf.dws.com/en-us/AssetDownload/Index/c7bca405-12a0-486d-8a66-5d3558c23fa0/DBJP-SUM.pdf) | Passive/indexing approach and calendar-year total returns | Official NAV rows `2015-2024`; rows used in page `2016-2024` |
| `NYSE Arca:DBJP` | [DWS 2025 dividend schedule](https://etf.dws.com/en-us/AssetDownload/Index/6b4403da-1256-4e11-8e8a-14254534db91/Dividend-Schedule.pdf) | Distribution timing/frequency context | 2025 annual distribution schedule |
| `NYSE Arca:DBJP` | [DWS currency-hedged ETF explanation](https://etf.dws.com/en-us/etf-knowledge/focus-topics-etf-investment-strategies/currency-hedged-etfs-mitigating-currency-risks-from-international-equities/) | USD/JPY hedge mechanism | Educational issuer page accessed `2026-07-23` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### DBJP Raw Observations And Calculations

| Year | DBJP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -2.00% | 11.96% |
| 2017 | 20.83% | 21.83% |
| 2018 | -14.03% | -4.38% |
| 2019 | 20.78% | 31.49% |
| 2020 | 9.49% | 18.40% |
| 2021 | 12.89% | 28.71% |
| 2022 | -2.54% | -18.11% |
| 2023 | 34.97% | 26.29% |
| 2024 | 26.05% | 25.02% |
| 2025 | not disclosed | 17.88% |

- Official rolling 10-year NAV TR CAGR: `17.28%` as of `2026-06-30`, represented by `2016-06-30` to `2026-06-30`; actual elapsed years `10.00`. Raw NAV endpoint levels are `ไม่พบข้อมูลที่ยืนยันได้`.
- Normalized calculation required for the performance page: start `100.00`; end `(1 + 0.1728)^10 = 492.31`; normalized cumulative return `+392.31%`; `(492.31 / 100.00)^(1 / 10.00) - 1 ≈ 17.28%`. The end value is derived from the issuer's rounded annualized return, not an issuer-published NAV level.
- Complete official calendar rows `2016-2024` compound to `+51.99%` and annualize to `10.81%` over `9` years. This is not the rolling 10-year CAGR.
- Up/down years among complete rows: `6 / 3`. Best `2023 +34.97%`; least positive `2020 +9.49%`; worst `2018 -14.03%`; least bad down year `2022 -2.54%`.
- Official issuer current YTD is `ไม่พบข้อมูลที่ยืนยันได้` in the latest factsheet. A secondary Schwab report shows `+21.80%` NAV cumulative YTD as of `2026-06-30`, but it is not used as the primary page claim because the issuer factsheet omits YTD.
- Exact June-to-June S&P 500 TR for the rolling 10-year endpoint is `ไม่พบข้อมูลที่ยืนยันได้`; annual S&P rows are the cached complete-calendar-year comparison only.
- Daily NAV history sufficient to reproduce max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### DBJP Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from `check-etf-performance/workflow.md` before writing: ticker/exchange, passive-equity classification, NAV Total Return definition, reinvested distributions and expenses, annual rows, rolling 10-year coverage and formula, S&P 500 basis/window, as-of dates, best/worst ranking, 2025/current-YTD gaps, filenames, Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable `lean` workflow.

## AIA Sequential Queue Record

- Input row: `9/125`; input ticker: `AIA`; terminal status: `completed_10Y`.
- Canonical entity key: `NASDAQ:AIA`; the official iShares product page identifies the NASDAQ listing and iShares Asia 50 ETF. No provider slug or guessed exchange is used.
- Classification: supported passive/index-tracking Asia ex Japan equity ETF. Issuer benchmark: `S&P Asia 50 Capped Index (Net)`. Inception: `2007-11-13`. Expense ratio: `0.50%`. Distribution frequency: semi-annual.
- Official current observations: NAV `US$136.34` as of `2026-07-21`; date-to-date NAV Total Return YTD `+40.47%` as of `2026-07-21`; exposure as of the same date includes Taiwan `37.23%`, South Korea `26.21%`, and China `25.48%`.

### AIA Official Source Map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| `NASDAQ:AIA` | [iShares US AIA product and performance page](https://www.ishares.com/us/products/239730/ishares-asia-50-etf) | Fund identity, exchange, benchmark, inception, NAV, fee, classification, current YTD, rolling NAV Total Return and calendar rows | Page accessed `2026-07-24`; NAV/current YTD and exposure `2026-07-21`; performance table `2026-06-30` |
| `S&P 500 TR` | [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached convention | Common reference benchmark identity and annual rows | Cached USD Total Return rows as of `2025-12-31` |

### AIA Raw Observations And Calculations

| Year | AIA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | -10.75% | 28.71% |
| 2022 | -24.07% | -18.11% |
| 2023 | 4.84% | 26.29% |
| 2024 | 20.42% | 25.02% |
| 2025 | 47.01% | 17.88% |

- Official rolling 10-year NAV TR: cumulative `298.99%` and average annual/CAGR `14.84%` as of `2026-06-30`, represented by `2016-06-30` to `2026-06-30`; actual elapsed years `10.00`. Raw NAV endpoint levels are `ไม่พบข้อมูลที่ยืนยันได้`.
- Normalized calculation required for the performance page: start `100.00`; end `398.99`; `(398.99 / 100.00)^(1 / 10.00) - 1 ≈ 14.84%`. The normalized endpoint is derived from the rounded official cumulative return, not an issuer-published NAV level.
- Complete official calendar rows `2021-2025` compound to `+25.77%` and annualize to `4.69%` over `5` years. Up/down years are `3 / 2`; best `2025 +47.01%`; least positive `2023 +4.84%`; worst `2022 -24.07%`; least bad down year `2021 -10.75%`.
- Official current date-to-date NAV Total Return YTD is `+40.47%` as of `2026-07-21`; standardized month-end YTD is `+46.79%` as of `2026-06-30`. These are separate observations and are not mixed.
- Exact June-to-June S&P 500 TR for the rolling 10-year endpoint is `ไม่พบข้อมูลที่ยืนยันได้`; annual S&P rows are the cached complete-calendar-year comparison only.
- Daily NAV history sufficient to reproduce max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### AIA Pre-save Review Note

- No multi-agent reviewer was available in this thread. The main agent performed the complete local checklist from `check-etf-performance/workflow.md` before writing: ticker/exchange, passive-equity classification, NAV Total Return definition, reinvested distributions and expenses, annual rows, rolling 10-year coverage and normalized formula, S&P 500 basis/window, separate current/month-end as-of dates, best/worst ranking, filenames, Asia ex Japan region assignment, canonical geography tag, breadcrumbs, and link targets.
- Local verdict: `PASS`; no critical or high-severity finding remained. Reviewer-availability fallback is disclosed here as required by the durable `lean` workflow.
