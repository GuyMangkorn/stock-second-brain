---
type: source-note
source_profile: etf-performance-delta
accessed: 2026-07-14
canonical_outputs:
  - wiki/analysis/performance/ETF_NASDAQ_OPPJ Performance.md
  - wiki/analysis/performance/ETF Performance Index.md
tags:
  - source/etf
  - source/performance
  - source/benchmark
---

# ETF Performance Source Batch - 2026-07-14

## OPPJ Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NASDAQ:OPPJ` | [WisdomTree product page](https://www.wisdomtree.com/us/products/equity/oppj), [factsheet](https://www.wisdomtree.com/us/media/wisdomtree-factsheet-oppj) | Fund identity, NAV return definition, expense ratio, current YTD, rolling returns, NAV/price, hedge ratio, distributions | Performance 2026-06-30; expense/NAV/hedge 2026-07-13; market price 2026-07-10 |
| `NASDAQ:OPPJ` | [SEC 2025 summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj73125497k.htm), [annual-return chart](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj_chart.jpg) | Exchange, passive classification, strategy change, 2015-2024 annual NAV Total Return, return basis | Prospectus 2025-08-01; annual returns through 2024-12-31 |
| OPPJ index | [WisdomTree index page](https://www.wisdomtree.com/us/indexes/WTJOP), [methodology](https://www.wisdomtree.com/us/media/core-equity-index-methodology) | Issuer benchmark and dynamic JPY/USD hedge methodology | accessed 2026-07-14 |
| `NASDAQ:OPPJ` 2025 | [Schwab standardized ETF report](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=OPPJ) | Secondary 2025 NAV total return, rounded; marked `*` | 2025-12-31 |
| `NASDAQ:OPPJ` risk | [PortfoliosLab](https://portfolioslab.com/symbol/OPPJ) | Secondary dividend-adjusted max drawdown and recovery | accessed 2026-07-14 |
| `S&P 500 TR cache` | [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reusable complete-year S&P 500 Total Return common-reference rows | 2016-2025; reference as-of 2025-12-31 |

## Classification And Continuity

- OPPJ เป็น U.S.-domiciled passive, index-tracking Japan equity ETF; listing
  exchange คือ NASDAQ และ reporting/trading currency คือ USD.
- Fund inception คือ `2013-06-28`, แต่ current strategy/ticker เริ่ม
  `2025-07-01`. ก่อนหน้านั้นเป็น WisdomTree Japan Hedged SmallCap Equity Fund
  (`DXJS`); objective/index เปลี่ยน effective `2025-06-30`.
- Current issuer benchmark คือ WisdomTree Japan Opportunities Index. Index ใช้
  dynamic JPY/USD hedge 0-100%; latest fund aggregate hedge ratio `0.02%` ณ
  2026-07-13.
- Expense ratio: management `0.58%`, other expenses `0.00%`, total/net `0.58%`.
- Product page แสดง NAV USD `56.571` ณ 2026-07-13 และ closing market price USD
  `58.180` ณ 2026-07-10. Dates ไม่ตรงกัน จึงไม่คำนวณ premium/discount จากคู่นี้.

## Extracted Facts

Return basis ของ annual rows คือ pre-tax `NAV Total Return` รวม reinvested
distributions และหัก fund expenses. 2025* เป็น secondary standardized NAV total
return; S&P 500 TR เป็น common reference ไม่ใช่ issuer benchmark.

| Year | OPPJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 6.88% | 11.96% |
| 2017 | 29.46% | 21.83% |
| 2018 | -17.82% | -4.38% |
| 2019 | 18.33% | 31.49% |
| 2020 | -4.64% | 18.40% |
| 2021 | 11.98% | 28.71% |
| 2022 | 6.84% | -18.11% |
| 2023 | 36.69% | 26.29% |
| 2024 | 20.68% | 25.02% |
| 2025* | 36.20% | 17.88% |

- Official 2026 YTD NAV Total Return: `24.67%` ณ 2026-06-30.
- Official 1-/3-/5-/10-year NAV average annual returns: `58.06%`, `32.86%`,
  `24.84%`, `17.89%` ณ 2026-06-30.
- Official since-inception cumulative/CAGR: `541.90%` / `15.37%` ณ 2026-06-30.
- Latest four official distributions: USD `0.34000` (2026-06-25), `0.05500`
  (2026-03-26), `0.23981` (2025-12-26), `0.01000` (2025-09-25). Distribution
  analysis was not requested.

## Calculations

- 2016-2025 cumulative/CAGR: `244.89%` / `13.18%`; includes secondary 2025*.
- S&P 500 TR 2016-2025 cumulative/CAGR: `298.33%` / `14.82%` from cached annual
  rows. OPPJ gap is `-53.44 percentage points` cumulative and `-1.64 percentage
  points` annualized.
- OPPJ 2021-2025 cumulative/CAGR: `168.80%` / `21.87%*`; S&P 500 TR:
  `96.17%` / `14.43%`. This OPPJ window spans the mid-2025 strategy change.
- Issuer-reported rolling 10-year NAV TR CAGR `17.89%` implies a normalized
  `100.00 -> 518.52` over 10.00 years via `100 x (1 + 17.89%)^10`. This is a
  shown calculation, not disclosed issuer TR endpoints.
- Secondary adjusted-price max drawdown: `-39.30%`; peak 2018-01-09, trough
  2020-03-16, recovery 2021-03-15. This is not official NAV history.

## Source Conflicts And Gaps

- Official index symbols conflict: product page `WTJOPN`; index page `WTJOP` /
  `JOPN`; methodology `JPOP`; 2026 factsheet still shows predecessor symbol
  `WTJSEH`. ใช้ full index name เป็น canonical label และเก็บ conflict นี้ไว้.
- Official raw daily/monthly NAV total-return index levels and 10-year endpoints
  are `ไม่พบข้อมูลที่ยืนยันได้`; official max drawdown/recovery จึงคำนวณไม่ได้.
- No current issuer table with 2025 calendar-year NAV return was captured. The
  `36.20%*` row comes from a secondary standardized report and is not silently
  treated as an issuer row.
- Pre-2025-06-30 performance belongs to the predecessor objective. The 2025
  calendar year itself mixes about six months of each strategy.

## Handoff For Performance Page

Create `[[ETF_NASDAQ_OPPJ Performance]]`, add OPPJ to `[[ETF Performance Index]]`,
and retain the strategy-break warning beside all long-history interpretations.
Do not route this ETF through company financial ingest or DCF.

## Preliminary Holdings Groups Expansion

Batch นี้รัน `check-etf-performance` กับ 39 ticker ที่ไม่ถูกขีดฆ่าและยังไม่มี
performance page ใน section `Preliminary Holdings-Based Groups`: 37 กองผ่าน
passive index-tracking equity guardrail; `QDPL` เป็น derivative-heavy dividend-
futures strategy และ `MDIV` เป็น multi-asset fund-of-funds จึงบันทึกเป็น
`unsupported ETF type` และไม่จัดอันดับร่วม.

| Entity | Official source | Latest performance date used | Gap / note |
|---|---|---|---|
| `NYSE Arca:DEM` | [issuer](https://www.wisdomtree.com/us/products/equity/dem) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DES` | [issuer](https://www.wisdomtree.com/us/products/equity/des) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DFJ` | [issuer](https://www.wisdomtree.com/us/products/equity/dfj) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DGS` | [issuer](https://www.wisdomtree.com/us/products/equity/dgs) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DHS` | [issuer](https://www.wisdomtree.com/us/products/equity/dhs) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DLN` | [issuer](https://www.wisdomtree.com/us/products/equity/dln) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DLS` | [issuer](https://www.wisdomtree.com/us/products/equity/dls) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DON` | [issuer](https://www.wisdomtree.com/us/products/equity/don) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DTH` | [issuer](https://www.wisdomtree.com/us/products/equity/dth) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:DWM` | [issuer](https://www.wisdomtree.com/us/products/equity/dwm) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `Cboe BZX:DDWM` | [issuer](https://www.wisdomtree.com/us/products/equity/ddwm) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `Cboe BZX:DDLS` | [issuer](https://www.wisdomtree.com/us/products/equity/ddls) | 2026-06-30 | official 2017-2024 calendar NAV TR; 2016 unavailable; 2025 secondary NAV TR* |
| `NYSE Arca:DJD` | [issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-dow-jones-industrial-average-dividend-etf.html) | 2025-12-31 | official calendar NAV TR 2016-2025 |
| `Nasdaq:PEY` | [issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-high-yield-equity-dividend-achievers-etf.html) | 2026-05-31 | official calendar NAV TR 2016-2025 |
| `Nasdaq:PFM` | [issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-dividend-achievers-etf.html) | 2026-05-31 | official calendar NAV TR 2016-2025 |
| `Nasdaq:PID` | [issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-international-dividend-achievers-etf.html) | 2026-03-31 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:VYM` | [issuer](https://investor.vanguard.com/investment-products/etfs/profile/vym) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `Nasdaq:VYMI` | [issuer](https://investor.vanguard.com/investment-products/etfs/profile/vymi) | 2025-12-31 | official NAV calendar rows 2016†-2025; 2016 inception-year partial |
| `Cboe BZX:NOBL` | [issuer](https://www.proshares.com/our-etfs/strategic/nobl) | 2026-05-31 | official calendar NAV TR table not exposed |
| `Cboe BZX:REGL` | [issuer](https://www.proshares.com/our-etfs/strategic/regl) | 2026-05-31 | official calendar NAV TR table not exposed |
| `Cboe BZX:SMDV` | [issuer](https://www.proshares.com/our-etfs/strategic/smdv) | 2026-05-31 | official calendar NAV TR table not exposed |
| `Cboe BZX:TDV` | [issuer](https://www.proshares.com/our-etfs/strategic/tdv) | 2026-05-31 | fund history shorter than 10 years; official calendar table gap |
| `NYSE Arca:DIVI` | [Franklin product](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/21412/SINGLCLASS/franklin-international-core-dividend-tilt-index-etf/DIVI), [factsheet](https://www.franklintempleton.com/forms-literature/download/DIVI-FF) | 2026-06-30 | NAV TR 10Y average annual `11.24%`; inception annualized `11.02%`; raw TR endpoints not disclosed |
| `NYSE Arca:FLCA` | [Franklin product](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26364/SINGLCLASS/franklin-ftse-canada-etf/FLCA), [factsheet](https://www.franklintempleton.com/forms-literature/download/FLCA-FF) | 2026-06-30 | NAV TR 10Y `—`; inception 2017-11-02, so history is shorter than 10 years |
| `NYSE Arca:SPYD` | [issuer](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-sp-500-high-dividend-etf-spyd) | 2026-05-31 | official calendar NAV TR table not exposed |
| `NYSE Arca:SDY` | [issuer](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-dividend-etf-sdy) | 2026-06-30 | official calendar NAV TR table not exposed |
| `NYSE Arca:WDIV` | [issuer](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-global-dividend-etf-wdiv) | 2026-06-30 | official calendar NAV TR table not exposed |
| `NYSE Arca:DWX` | [issuer](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-international-dividend-etf-dwx), [factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-dwx.pdf) | 2026-06-30 | official rolling 10Y/YTD; calendar NAV TR table not exposed |
| `NYSE Arca:AMLP` | [issuer](https://www.alpsfunds.com/exchange-traded-funds/amlp) | 2026-07-02 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:ENFR` | [issuer](https://www.alpsfunds.com/exchange-traded-funds/enfr) | 2026-07-02 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:IDOG` | [issuer](https://www.alpsfunds.com/exchange-traded-funds/idog) | 2026-07-02 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:SDOG` | [issuer](https://www.alpsfunds.com/exchange-traded-funds/sdog) | 2026-06-18 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:SDIV` | [issuer](https://www.globalxetfs.com/funds/SDIV) | 2026-07-10 | prospectus chart captured but year-label mapping was not machine-verifiable |
| `Nasdaq:KBWD` | [issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-kbw-high-dividend-yield-financial-etf.html) | 2025-12-31 | official calendar NAV TR 2016-2025 |
| `Nasdaq:KBWY` | [issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-kbw-premium-yield-equity-reit-etf.html) | 2026-03-31 | official calendar NAV TR 2016-2025 |
| `NYSE Arca:FDD` | [issuer](https://www.ftportfolios.com/retail/etf/etfsummary.aspx?Ticker=FDD), [2025 prospectus](https://www.ftportfolios.com/Funds/ETF/Prospectus/FAN) | 2026-06-30 | official calendar NAV TR 2016-2025; 10Y CAGR 9.11%; chart annual rows through 2025 |
| `Nasdaq:TDIV` | [issuer](https://www.ftportfolios.com/retail/etf/EtfSummary.aspx?Ticker=TDIV) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `Nasdaq:DVY` | [issuer](https://www.ishares.com/us/products/239500/ishares-select-dividend-etf) | 2026-06-30 | official calendar NAV TR 2016-2025 |
| `Cboe BZX:IDV` | [issuer](https://www.ishares.com/us/products/239499/ishares-international-select-dividend-etf), [international issuer table](https://www.ishares.com/ch/professionelle-anleger/de/produkte/239499/ishares-international-select-dividend-etf?switchLocale=Y) | 2026-06-30 | official calendar NAV TR 2016-2025; rolling 10Y 10.10% |

## 2016-2020 Annual NAV TR Inputs

ตัวเลขด้านล่างเป็น NAV Total Return รายปีของช่วงที่เพิ่งเติมลงใน performance
pages; เงินปันผล reinvested และหัก fund expenses ตามนิยามของ issuer. ปี 2021-2025
อยู่ในตารางรายกองเดิม. `*`/`†` ใช้ตามกติกาใน skill และ `ไม่พบข้อมูลที่ยืนยันได้`
ยังคงใช้เมื่อ issuer ไม่เปิด annual row.

| Ticker | 2016 | 2017 | 2018 | 2019 | 2020 | As-of / official source |
|---|---:|---:|---:|---:|---:|---|
| `AMLP` | 15.15% | -7.80% | -12.67% | 5.95% | -32.53% | 2026-07-02; [ALPS issuer](https://www.alpsfunds.com/exchange-traded-funds/amlp) |
| `DEM` | 22.54% | 24.87% | -7.31% | 19.37% | -5.64% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/dem-presentation) |
| `DES` | 31.06% | 8.66% | -12.74% | 20.30% | -4.41% | 2025-12-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/des-presentation) |
| `DFJ` | 11.04% | 31.62% | -17.63% | 17.02% | -0.06% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/dfj-presentation) |
| `DGS` | 14.91% | 35.48% | -15.39% | 17.28% | 4.14% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/dgs-presentation) |
| `DHS` | 17.85% | 11.68% | -7.25% | 22.58% | -5.68% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/dhs-presentation) |
| `DJD` | 16.93% | 21.63% | 0.11% | 22.37% | 0.94% | 2025-12-31; [Invesco issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-dow-jones-industrial-average-dividend-etf.html) |
| `DLN` | 15.37% | 18.21% | -5.77% | 29.03% | 4.55% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/dln-presentation) |
| `DLS` | 7.00% | 30.95% | -18.69% | 22.11% | -1.23% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/dls-presentation) |
| `DON` | 20.30% | 14.86% | -8.27% | 23.42% | -5.40% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/don-presentation) |
| `DTH` | 5.10% | 20.33% | -12.57% | 17.74% | -7.05% | 2025-12-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/dth-presentation) |
| `DWM` | 2.88% | 23.46% | -13.54% | 19.07% | -1.94% | 2026-03-31; [WisdomTree presentation](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/presentations/equity/dwm_presentation.pdf) |
| `DDWM` | 14.18% | 18.52% | -11.05% | 21.03% | -4.20% | 2025-12-31; [WisdomTree presentation](https://www.wisdomtree.com/us/media/ddwm-presentation-pdf-c6778c) |
| `DDLS` | ไม่พบข้อมูลที่ยืนยันได้ | 25.02% | -16.59% | 24.74% | -1.78% | 2026-06-30; [WisdomTree issuer performance](https://www.wisdomtree.com/us/products/equity/ddls) |
| `ENFR` | 41.95% | -0.09% | -18.29% | 21.20% | -24.31% | 2026-07-02; [ALPS issuer](https://www.alpsfunds.com/exchange-traded-funds/enfr) |
| `FDD` | 2.58% | 19.04% | -8.83% | 23.09% | -2.64% | 2025-12-31; [First Trust prospectus](https://www.ftportfolios.com/Funds/ETF/Prospectus/FAN) |
| `IDOG` | 3.97% | 25.81% | -13.09% | 20.86% | -1.34% | 2026-07-02; [ALPS summary prospectus](https://www.alpsfunds.com/hubfs/alps-docs/reg/sum-pro/alps-international-sector-dividend-dogs-etf-idog-sum-pro.pdf) |
| `SDOG` | 22.36% | 12.67% | -11.30% | 24.09% | -0.37% | 2026-06-18; [ALPS issuer](https://www.alpsfunds.com/exchange-traded-funds/sdog) |
| `VYM` | 16.87% | 16.42% | -5.87% | 24.20% | 1.14% | 2026-06-30; [Vanguard issuer](https://investor.vanguard.com/investment-products/etfs/profile/vym) |
| `DVY` | 21.50% | 15.00% | -6.30% | 22.70% | -4.90% | 2026-06-30; [iShares issuer table](https://www.ishares.com/uk/professional/en/products/239500/ishares-select-dividend-etf?siteEntryPassthrough=true&switchLocale=y) |
| `IDV` | 7.70% | 19.60% | -10.50% | 23.10% | -5.40% | 2026-06-30; [iShares issuer table](https://www.ishares.com/ch/professionelle-anleger/de/produkte/239499/ishares-international-select-dividend-etf?switchLocale=Y) |
| `KBWD` | 20.62% | 11.93% | -8.78% | 20.56% | -15.21% | 2025-12-31; [Invesco issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-kbw-high-dividend-yield-financial-etf.html) |
| `KBWY` | 33.05% | 0.86% | -18.04% | 23.44% | -25.82% | 2026-03-31; [Invesco issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-kbw-premium-yield-equity-reit-etf.html) |
| `PEY` | 31.56% | 8.64% | -7.36% | 24.61% | -3.76% | 2025-12-31; [Invesco issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-high-yield-equity-dividend-achievers-etf.html) |
| `PFM` | 14.64% | 17.35% | -4.40% | 26.79% | 9.54% | 2025-12-31; [Invesco issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-dividend-achievers-etf.html) |
| `PID` | 9.92% | 19.03% | -11.08% | 25.44% | -6.55% | 2026-03-31; [Invesco issuer](https://www.invesco.com/us/en/financial-products/etfs/invesco-international-dividend-achievers-etf.html) |
| `TDIV` | 19.63% | 21.90% | -3.01% | 33.31% | 17.27% | 2025-12-31; [First Trust prospectus](https://www.ftportfolios.com/Funds/ETF/Prospectus/FID) |

## Common Benchmark And Calculations

- 2021-2025 common benchmark rows copied from the cached `S&P 500 Total Return`
  convention: `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`.
- S&P 500 TR 2021-2025 CAGR: `14.43%`; 2016-2025 CAGR: `14.82%`.
- ETF common-window CAGR formula: `(Π(1 + annual NAV TR))^(1/5) - 1`.
- `DDLS 2025 +29.10%*` is secondary Schwab standardized NAV return; excluded
  from strict official-only cross-fund ranking.
- ProShares/State Street calendar tables remain unavailable in the captured
  official pages; rolling official figures are retained and missing annual rows
  are shown as `ไม่พบข้อมูลที่ยืนยันได้`. Vanguard VYMI now has official annual
  NAV rows 2016†-2025 from the issuer page.
- `DWX` official NAV TR as of 2026-06-30: YTD `6.97%`, 1-year `14.11%`,
  3-year `14.96%`, 5-year `7.73%`, and 10-year `7.44%`; gross expense ratio
  `0.45%`, inception `2008-02-12`.
- `DIVI` official NAV TR as of 2026-06-30: 10-year average annual return
  `11.24%`, since-inception annualized return `11.02%`; the latest factsheet
  exposes calendar NAV rows for 2017-2025 but not raw 10-year TR endpoints.

## Unsupported ETF Types

- `NYSE Arca:QDPL`: derivative-heavy dividend-multiplier exposure through
  S&P 500 annual dividend futures; excluded by skill guardrail.
- `Nasdaq:MDIV`: multi-asset diversified income fund-of-funds; excluded by
  skill guardrail.
