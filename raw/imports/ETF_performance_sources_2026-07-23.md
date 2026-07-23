---
type: source-batch
topic: ETF performance
accessed: 2026-07-23
input_source: raw/imports/tradingview_etf_list_filtered_2026-07-22.md
input_count: 125
verified_passive_pages: 78
existing_canonical_alias_coverage: 1
unresolved_or_unsupported: 46
review_gate: LOCAL_PASS_REVIEWER_UNAVAILABLE
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-07-23

## Scope and gate

ใช้ check-etf-performance กับ ticker ทั้ง 125 รายการจาก input source. แยก NAV Total Return ออกจาก market price และใช้ S&P 500 Total Return cache 2016-2025 เป็น common reference เมื่อมี annual rows. unsupported ETF type หมายถึง active, derivative-heavy, bond, currency, multi-strategy หรือ single-stock product ที่อยู่นอก ETF v1; unresolved หมายถึงยังยืนยัน canonical issuer/exchange ticker ไม่ได้. Pre-save reviewer status: independent reviewer was dispatched but returned no verdict after bounded waits; local checklist PASS was applied before saving.

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Source URL | Gap / resolution note |
|---|---|---|---|---|---|---|
| AAXJ | supported | NASDAQ:AAXJ | Asia ex Japan | 20.12% (2026-07-16) | https://www.ishares.com/us/products/239601/ishares-msci-all-country-asia-ex-japan-etf | raw 10Y endpoints not disclosed |
| ADIV | unsupported | NYSE Arca:ADIV | Asia-Pacific | not applicable | https://www.gafunds.com/our-funds/ | active equity |
| ADVE | unsupported | NYSE Arca:ADVE | Asia-Pacific | not applicable | https://www.matthewsasia.com/funds/etfs/asia-dividend-active-etf/ | active equity |
| AIA | supported | NASDAQ:AIA | Asia ex Japan | 34.89% (2026-07-17) | https://www.ishares.com/us/products/239730/AIA | raw 10Y endpoints not disclosed |
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
| DXJJF | existing | LSE:DXJ | Japan | not applicable | https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged | existing canonical page covers OTC alias |
| EEMA | supported | NASDAQ:EEMA | Emerging Markets | 17.88% (2026-07-17) | https://www.ishares.com/us/products/239629/ishares-msci-emerging-markets-asia-etf | raw 10Y endpoints not disclosed |
| EIDO | supported | NYSE Arca:EIDO | Indonesia | -30.08% (2026-07-21) | https://www.ishares.com/ch/professionals/en/products/239661/ishares-msci-indonesia-etf?switchLocale=Y | raw 10Y endpoints not disclosed; earlier annual rows not surfaced |
| ENZL | supported | NASDAQ:ENZL | New Zealand | 3.45% (2026-07-21) | https://www.ishares.com/us/products/239672/ishares-msci-new-zealand-capped-etf | raw 10Y endpoints not disclosed |
| EPHE | supported | NYSE Arca:EPHE | Philippines | 3.93% (2026-07-21) | https://www.ishares.com/us/products/239675/ishares-msci-philippines-etf | raw 10Y endpoints not disclosed; earlier annual rows not shown |
| EPI | supported | NYSE Arca:EPI | India | -7.91% (2026-06-30) | https://www.wisdomtree.com/us/products/equity/epi | raw 10Y endpoints not disclosed |
| EPP | supported | NYSE Arca:EPP | Asia-Pacific | 10.77% (2026-07-17) | https://www.ishares.com/us/products/239674/ishares-msci-pacific-ex-japan-etf | annual rows and raw 10Y endpoints not disclosed |
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
| FLTW | supported | NYSE Arca:FLTW | Taiwan | 63.10% (2026-07-10) | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26351/SINGLCLASS/franklin-ftse-taiwan-etf/FLTW | annual NAV rows not disclosed; fund under 10 years |
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
| INCO | supported | NYSE Arca:INCO | India | not disclosed (not disclosed) | https://www.columbiathreadneedleus.com/investment-products/mutual-funds/columbia-india-consumer-etf/class-/details?cusip=19762B707 | inception, fee, current performance and annual rows not disclosed |
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
| ISRVF | supported | LSE:IJPD | Japan | not disclosed (not disclosed) | https://www.ishares.com/uk/individual/en/products/257514/ishares-msci-japan-usd-hedged-ucits-etf?siteEntryPassthrough=true&switchLocale=y | OTC alias; current performance and annual rows not disclosed |
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
| WDTRF | supported | LSE:DXJA | Japan | not disclosed (not disclosed) | https://www.wisdomtree.eu/-/media/eu-media-files/key-documents/factsheet/wt/factsheet-wisdomtree-japan-equity-ucits-etf-usd-hedged-acc.pdf?sc_lang=de-de | OTC alias; current performance and annual rows not disclosed |

## Benchmark convention

Annual benchmark rows use S&P 500 Total Return in USD with dividends reinvested, cached as of 2025-12-31: 2016 11.96%, 2017 21.83%, 2018 -4.38%, 2019 31.49%, 2020 18.40%, 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%. It is a common reference, not each ETF's issuer benchmark. Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/

## Ownership and graph notes

- Numeric owner is each wiki/analysis/performance/ETF_* Performance.md page; region pages are static navigation summaries only.
- Missing values remain not disclosed; no annual return was inferred from price return, fiscal-year return, or a shorter rolling period.
- Cleanup on 2026-07-23 removed 45 empty annual NAV Total Return placeholder rows (`| — | not disclosed | not disclosed |`) from the corresponding performance pages; no sourced numeric values were changed.
- Existing canonical coverage: DXJJF is the OTC alias for existing ETF_LSE_DXJ Performance; no duplicate page was created.
- Unresolved aliases retained in the register: IHREF, JPXN, VNFGF, IHRMF, KRANF and the Vanguard/iShares OTC symbols.
