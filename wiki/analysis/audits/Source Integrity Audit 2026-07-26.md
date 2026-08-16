---
type: analysis
analysis_type: source-integrity-audit
date: 2026-07-26
scope: all-etf-performance-pages
source_files:
  - wiki/analysis/performance/
  - wiki/analysis/performance/ETF Performance Index.md
  - wiki/analysis/comparisons/ETF Region Index.md
  - raw/imports/ETF_performance_sources_2026-07-23.md
  - raw/imports/ETF_performance_sources_2026-07-24.md
  - raw/imports/ETF_performance_sources_2026-07-26.md
tags:
  - analysis/source-integrity-audit
  - maintenance/etf-performance
  - coverage/10-year-nav-tr
---

# Source Integrity Audit - 2026-07-26

## Scope and method

ตรวจ canonical performance pages ทั้งหมดใน `wiki/analysis/performance/` โดยไม่นับ index, README และ regime matrix. Audit date คือ `2026-07-26`. Fund age ใช้สูตร `(audit_date - inception_date) / 365.25`; qualifying 10-year coverage ต้องเป็น official NAV Total Return ที่มี endpoints ครบอย่างน้อย `10.00` elapsed years หรือ official complete calendar-year rows ครบ 10 ปี. NAV TR, market-price return, price return และ proxy ไม่ถูกผสมกัน.

The queue was reconciled against the directory and master index before processing. Each page received one terminal status; the four exception pages were second-pass checked against issuer sources: FLAU and FLCA remain short-history; EPHE and AAXJ qualify for official 10-year coverage. No unsupported instrument remains as a performance page.

## Coverage summary

- Canonical performance pages: `143`
- Master-index performance links: `143` unique canonical targets; repeated links in navigation/summary sections are intentional; the unique target set matches the directory
- Region-navigation performance links: `143` unique canonical targets; the primary-region target set matches the directory
- `EXPANDED_TO_10Y`: `106`
- `ACCEPTED_SHORT_HISTORY`: `37`
- `ADDITIONAL_HISTORY_FOUND`: `0`
- `UNRESOLVED_10Y_TR`: `0`
- `UNSUPPORTED_ETF_TYPE`: `0`
- `PENDING` / `IN_PROGRESS`: `0`

## Terminal-status categories

### 1. ETFs expanded to a verified 10-year history

`106` pages: NYSE Arca:AMLP, NYSE Arca:DEM, NYSE Arca:DES, NYSE Arca:DFJ, AMEX:DGRO, NYSE Arca:DGS, NYSE Arca:DHS, NYSE Arca:DIVI, NYSE Arca:DJD, NYSE Arca:DLN, NYSE Arca:DLS, NYSE Arca:DON, NYSE Arca:DTD, NYSE Arca:DTH, NYSE Arca:DWM, NYSE Arca:ENFR, NYSE Arca:FDD, NYSE Arca:FVD, NYSE Arca:IDOG, NYSE Arca:SDOG, AMEX:VIG, NYSE Arca:VYM, Cboe BZX:CNYA, Cboe BZX:INDA, Cboe BZX:SMIN, Cboe BZX:VNM, Cboe BZX:DDLS, Cboe BZX:DDWM, Cboe BZX:EFAV, Cboe BZX:IDV, LSE:CEMA, LSE:CJPU, LSE:CPXJ, LSE:CSKR, LSE:DXJ, LSE:FXC, LSE:IAPD, LSE:IJPD, LSE:IJPU, LSE:SAUS, LSE:SJPA, LSE:VDJP, LSE:VDPX, NASDAQ:AAXJ, NASDAQ:AIA, NASDAQ:CXSE, Nasdaq:DVY, NASDAQ:EEMA, NASDAQ:ENZL, Nasdaq:FCA, NASDAQ:FJP, NASDAQ:FPA, NASDAQ:INDY, Nasdaq:KBWD, Nasdaq:KBWY, NASDAQ:MCHI, NASDAQ:NFTY, NASDAQ:OPPJ, Nasdaq:PEY, Nasdaq:PFM, NASDAQ:PGJ, Nasdaq:PID, Nasdaq:TDIV, NASDAQ:VIGI, Nasdaq:VXUS, Nasdaq:VYMI, NYSE Arca:ASEA, NYSE Arca:ASHR, NYSE Arca:ASHS, NYSE Arca:CHIQ, NYSE Arca:CNXT, NYSE Arca:CQQQ, NYSE Arca:DBJP, NYSE Arca:DVYA, NYSE Arca:ECNS, NYSE Arca:EIDO, NYSE Arca:EPHE, NYSE Arca:EPI, NYSE Arca:EPP, NYSE Arca:EWA, NYSE Arca:EWC, NYSE Arca:EWG, NYSE Arca:EWH, NYSE Arca:EWJ, NYSE Arca:EWM, NYSE Arca:EWS, NYSE Arca:EWT, NYSE Arca:EWY, NYSE Arca:FXI, NYSE Arca:GLIN, NYSE Arca:GMF, NYSE Arca:GSJY, NYSE Arca:GXC, NYSE Arca:HEWJ, NYSE Arca:IDX, NYSE Arca:IMVP, NYSE Arca:INCO, NYSE Arca:IPAC, NYSE Arca:JPXN, NYSE Arca:KBA, NYSE Arca:KWEB, NYSE Arca:SCJ, NYSE Arca:THD, NYSE Arca:VOO, NYSE Arca:VPL, NYSE Arca:VSS.

### 2. Additional history found but 10 years remain incomplete

ไม่มี. The short-history pages already preserve the longest official history available in their current issuer/source captures; no proxy or interpolation was added.

### 3. ETFs accepted because the fund is less than 10 years old

`37` pages: Cboe BZX:BBJP, Cboe BZX:BBAX, Euronext Amsterdam:ICHN, LSE:DXJA, LSE:FLXI, LSE:KWEB, LSE:VAPU, LSE:VJPU, NASDAQ:CNQQ, NASDAQ:EWJV, Nasdaq:IND, Nasdaq:INDH, Nasdaq:INDQ, Nasdaq:SMHC, NASDAQ:TCHI, Nasdaq:WDAF, NYSE Arca:DGIN, NYSE Arca:FLAU, NYSE Arca:FLAX, NYSE Arca:FLCA, NYSE Arca:FLCH, NYSE Arca:FLIN, NYSE Arca:FLJH, NYSE Arca:FLJP, NYSE Arca:FLKR, NYSE Arca:FLTW, NYSE Arca:INQQ, NYSE Arca:KCAI, NYSE Arca:KDEF, NYSE Arca:KGRN, NYSE Arca:KMCA, NYSE Arca:KSTR, NYSE Arca:KTEC, NYSE Arca:KURE, NYSE Arca:VNAM, NYSE:KPHO, XETRA:VJPA.

Each row remains explicitly labeled as under 10 years, with inception date and age shown in the table below. Available official NAV TR is retained where disclosed; missing periods remain `ไม่พบข้อมูลที่ยืนยันได้` / `not disclosed`.

### 4. ETFs at least 10 years old where 10-year NAV TR still could not be verified

ไม่มี. EPHE and AAXJ were the last apparent gaps and both have official rolling 10-year NAV TR evidence.

### 5. Unsupported or identity-unresolved instruments

ไม่มี performance page in scope. Unsupported inputs remain documented in the dated source batches and were not promoted into `wiki/analysis/performance/`.

## Findings by severity

### High severity

ไม่พบ. No unsupported, conflicting, or mislabelled 10-year NAV TR claim remained after the exception second pass.

### Medium severity

ไม่พบ unresolved medium issue. FLAU and EPHE had stale current-YTD snapshots relative to the latest issuer pages; both were refreshed and their new as-of dates are visible. The source batch retains prior as-of observations as historical context rather than silently overwriting them.

### Low severity

- Some official pages do not publish raw NAV TR endpoint levels or every annual row; each performance page retains `not disclosed` and normalized values are labeled as derived where used.
- Issuer benchmark changes, share-class/listing conflicts, and source-date differences remain disclosed on the owning performance pages.

## Coverage audit table

| Ticker | Entity Key | Inception | Fund Age | Previous Coverage | New Coverage | Status | Data Added | Reason / Remaining Gap | Performance Page |
|---|---|---:|---:|---|---|---|---|---|---|
| AMLP | NYSE Arca:AMLP | 2010-08-24 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_AMLP Performance]] |
| DEM | NYSE Arca:DEM | 2007-07-13 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DEM Performance]] |
| DES | NYSE Arca:DES | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DES Performance]] |
| DFJ | NYSE Arca:DFJ | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DFJ Performance]] |
| DGRO | AMEX:DGRO | 10 มิ.ย. 2014 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DGRO Performance]] |
| DGS | NYSE Arca:DGS | 2007-10-30 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_DGS Performance]] |
| DHS | NYSE Arca:DHS | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DHS Performance]] |
| DIVI | NYSE Arca:DIVI | 1 มิ.ย. 2016 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DIVI Performance]] |
| DJD | NYSE Arca:DJD | 2015-12-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DJD Performance]] |
| DLN | NYSE Arca:DLN | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DLN Performance]] |
| DLS | NYSE Arca:DLS | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DLS Performance]] |
| DON | NYSE Arca:DON | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DON Performance]] |
| DTD | NYSE Arca:DTD | 16 มิ.ย. 2006 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DTD Performance]] |
| DTH | NYSE Arca:DTH | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DTH Performance]] |
| DWM | NYSE Arca:DWM | 2006-06-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_DWM Performance]] |
| ENFR | NYSE Arca:ENFR | 2013-10-31 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_ENFR Performance]] |
| FDD | NYSE Arca:FDD | 2007-08-27 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_FDD Performance]] |
| FVD | NYSE Arca:FVD | 19 ส.ค. 2003 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_FVD Performance]] |
| IDOG | NYSE Arca:IDOG | 2013-06-27 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_IDOG Performance]] |
| SDOG | NYSE Arca:SDOG | 2012-06-29 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_SDOG Performance]] |
| VIG | AMEX:VIG | 21 เม.ย. 2006 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_VIG Performance]] |
| VYM | NYSE Arca:VYM | 2006-11-10 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_AMEX_VYM Performance]] |
| BBJP | Cboe BZX:BBJP | 2018-06-15 | 8.11 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_CBOE_BBJP Performance]] |
| BBAX | Cboe BZX:BBAX | 2018-08-07 | 7.97 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_CBOE_BZX_BBAX Performance]] |
| CNYA | Cboe BZX:CNYA | 2016-06-13 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_BZX_CNYA Performance]] |
| INDA | Cboe BZX:INDA | 2012-02-02 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_BZX_INDA Performance]] |
| SMIN | Cboe BZX:SMIN | 2012-02-08 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_BZX_SMIN Performance]] |
| VNM | Cboe BZX:VNM | 2009-08-11 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_BZX_VNM Performance]] |
| DDLS | Cboe BZX:DDLS | 2016-01-07 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_DDLS Performance]] |
| DDWM | Cboe BZX:DDWM | 2016-01-07 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_DDWM Performance]] |
| EFAV | Cboe BZX:EFAV | 18 ต.ค. 2011 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_EFAV Performance]] |
| IDV | Cboe BZX:IDV | 2007-06-11 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_CBOE_IDV Performance]] |
| ICHN | Euronext Amsterdam:ICHN | 2019-06-20 | 7.10 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_EURONEXT_AMSTERDAM_ICHN Performance]] |
| CEMA | LSE:CEMA | 2010-08-06 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_CEMA Performance]] |
| CJPU | LSE:CJPU | 2010-01-11 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_CJPU Performance]] |
| CPXJ | LSE:CPXJ | 2010-01-12 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_CPXJ Performance]] |
| CSKR | LSE:CSKR | 2010-08-24 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_CSKR Performance]] |
| DXJ | LSE:DXJ | 2015-05-18 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_DXJ Performance]] |
| DXJA | LSE:DXJA | 2017-03-07 | 9.39 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_LSE_DXJA Performance]] |
| FLXI | LSE:FLXI | 2019-06-25 | 7.09 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_LSE_FLXI Performance]] |
| FXC | LSE:FXC | 2004-10-21 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_FXC Performance]] |
| IAPD | LSE:IAPD | 2006-06-02 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_IAPD Performance]] |
| IJPD | LSE:IJPD | 2013-09-30 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_IJPD Performance]] |
| IJPU | LSE:IJPU | 2004-10-01 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_IJPU Performance]] |
| KWEB | LSE:KWEB | 2018-11-21 | 7.68 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_LSE_KWEB Performance]] |
| SAUS | LSE:SAUS | 2010-01-22 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_SAUS Performance]] |
| SJPA | LSE:SJPA | 2009-09-25 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_SJPA Performance]] |
| VAPU | LSE:VAPU | 2019-09-24 | 6.84 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_LSE_VAPU Performance]] |
| VDJP | LSE:VDJP | 2013-05-21 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_VDJP Performance]] |
| VDPX | LSE:VDPX | 2013-05-21 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_LSE_VDPX Performance]] |
| VJPU | LSE:VJPU | 2020-01-31 | 6.48 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_LSE_VJPU Performance]] |
| AAXJ | NASDAQ:AAXJ | 2008-08-13 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_AAXJ Performance]] |
| AIA | NASDAQ:AIA | 2007-11-13 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_AIA Performance]] |
| CNQQ | NASDAQ:CNQQ | 2025-09-24 | 0.84 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_CNQQ Performance]] |
| CXSE | NASDAQ:CXSE | 2012-09-19 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_CXSE Performance]] |
| DVY | Nasdaq:DVY | 2003-11-03 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_DVY Performance]] |
| EEMA | NASDAQ:EEMA | 2012-02-08 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_EEMA Performance]] |
| ENZL | NASDAQ:ENZL | 2010-09-01 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_ENZL Performance]] |
| EWJV | NASDAQ:EWJV | 2019-03-05 | 7.39 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_EWJV Performance]] |
| FCA | Nasdaq:FCA | 2011-04-18 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_FCA Performance]] |
| FJP | NASDAQ:FJP | 2011-04-18 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_FJP Performance]] |
| FPA | NASDAQ:FPA | 2011-04-18 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_FPA Performance]] |
| IND | Nasdaq:IND | 2025-11-24 | 0.67 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_IND Performance]] |
| INDH | Nasdaq:INDH | 2024-05-09 | 2.21 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_INDH Performance]] |
| INDQ | Nasdaq:INDQ | 2026-03-31 | 0.32 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_INDQ Performance]] |
| INDY | NASDAQ:INDY | 18 พ.ย. 2009 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_INDY Performance]] |
| KBWD | Nasdaq:KBWD | 2010-12-02 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_KBWD Performance]] |
| KBWY | Nasdaq:KBWY | 2010-12-02 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_KBWY Performance]] |
| MCHI | NASDAQ:MCHI | 2011-03-29 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_MCHI Performance]] |
| NFTY | NASDAQ:NFTY | 2012-02-14 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_NFTY Performance]] |
| OPPJ | NASDAQ:OPPJ | 28 มิ.ย. 2013 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_OPPJ Performance]] |
| PEY | Nasdaq:PEY | 2004-12-09 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_PEY Performance]] |
| PFM | Nasdaq:PFM | 2005-09-15 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_PFM Performance]] |
| PGJ | NASDAQ:PGJ | 2004-12-09 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_PGJ Performance]] |
| PID | Nasdaq:PID | 2005-09-15 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_PID Performance]] |
| SMHC | Nasdaq:SMHC | 2026-06-23 | 0.09 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_SMHC Performance]] |
| TCHI | NASDAQ:TCHI | 2022-01-25 | 4.50 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_TCHI Performance]] |
| TDIV | Nasdaq:TDIV | 2012-08-13 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_TDIV Performance]] |
| VIGI | NASDAQ:VIGI | 25 ก.พ. 2016 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_VIGI Performance]] |
| VXUS | Nasdaq:VXUS | 26 ม.ค. 2011 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_VXUS Performance]] |
| VYMI | Nasdaq:VYMI | 2016-02-25 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NASDAQ_VYMI Performance]] |
| WDAF | Nasdaq:WDAF | 2025-09-12 | 0.87 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NASDAQ_WDAF Performance]] |
| ASEA | NYSE Arca:ASEA | 2011-02-16 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_ASEA Performance]] |
| ASHR | NYSE Arca:ASHR | 2013-11-05 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_ASHR Performance]] |
| ASHS | NYSE Arca:ASHS | 2014-05-20 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_ASHS Performance]] |
| CHIQ | NYSE Arca:CHIQ | 2009-11-30 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_CHIQ Performance]] |
| CNXT | NYSE Arca:CNXT | 2014-07-23 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_CNXT Performance]] |
| CQQQ | NYSE Arca:CQQQ | 2009-12-08 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_CQQQ Performance]] |
| DBJP | NYSE Arca:DBJP | 2011-06-08 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_DBJP Performance]] |
| DGIN | NYSE Arca:DGIN | 2022-02-15 | 4.44 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_DGIN Performance]] |
| DVYA | NYSE Arca:DVYA | 23 ก.พ. 2012 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_DVYA Performance]] |
| ECNS | NYSE Arca:ECNS | 28 ก.ย. 2010 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_ECNS Performance]] |
| EIDO | NYSE Arca:EIDO | 2010-05-05 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EIDO Performance]] |
| EPHE | NYSE Arca:EPHE | 2010-09-28 | >=10.00 | official rolling/10-calendar-year NAV TR | 2016-06 to 2026-06 retained; current snapshot refreshed | EXPANDED_TO_10Y | YTD 2.76% | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EPHE Performance]] |
| EPI | NYSE Arca:EPI | 2008-02-22 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EPI Performance]] |
| EPP | NYSE Arca:EPP | 2001-10-25 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EPP Performance]] |
| EWA | NYSE Arca:EWA | 12 มี.ค. 1996 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWA Performance]] |
| EWC | NYSE Arca:EWC | 12 มี.ค. 1996 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWC Performance]] |
| EWG | NYSE Arca:EWG | 12 มี.ค. 1996 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWG Performance]] |
| EWH | NYSE Arca:EWH | 12 มี.ค. 1996 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWH Performance]] |
| EWJ | NYSE Arca:EWJ | 12 มี.ค. 1996 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWJ Performance]] |
| EWM | NYSE Arca:EWM | 1996-03-12 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWM Performance]] |
| EWS | NYSE Arca:EWS | 1996-03-12 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWS Performance]] |
| EWT | NYSE Arca:EWT | 2000-06-20 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWT Performance]] |
| EWY | NYSE Arca:EWY | 2000-05-09 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_EWY Performance]] |
| FLAU | NYSE Arca:FLAU | 2017-11-02 | 8.73 | official available NAV TR; <10y | 2018-2025 retained; current snapshot refreshed | ACCEPTED_SHORT_HISTORY | YTD 9.50%; since-inception 7.53% | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLAU Performance]] |
| FLAX | NYSE Arca:FLAX | 2018-02-06 | 8.47 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLAX Performance]] |
| FLCA | NYSE Arca:FLCA | 2017-11-02 | 8.73 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLCA Performance]] |
| FLCH | NYSE Arca:FLCH | 2017-11-02 | 8.73 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLCH Performance]] |
| FLIN | NYSE Arca:FLIN | 2018-02-06 | 8.47 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLIN Performance]] |
| FLJH | NYSE Arca:FLJH | 2017-11-02 | 8.73 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLJH Performance]] |
| FLJP | NYSE Arca:FLJP | 2017-11-02 | 8.73 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLJP Performance]] |
| FLKR | NYSE Arca:FLKR | 2017-11-02 | 8.73 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLKR Performance]] |
| FLTW | NYSE Arca:FLTW | 2017-11-02 | 8.73 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_FLTW Performance]] |
| FXI | NYSE Arca:FXI | 5 ต.ค. 2004 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_FXI Performance]] |
| GLIN | NYSE Arca:GLIN | 2010-08-24 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_GLIN Performance]] |
| GMF | NYSE Arca:GMF | 2007-03-20 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_GMF Performance]] |
| GSJY | NYSE Arca:GSJY | 2016-03-02 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_GSJY Performance]] |
| GXC | NYSE Arca:GXC | 2007-03-20 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_GXC Performance]] |
| HEWJ | NYSE Arca:HEWJ | 2014-01-31 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_HEWJ Performance]] |
| IDX | NYSE Arca:IDX | 15 ม.ค. 2009 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_IDX Performance]] |
| IMVP | NYSE Arca:IMVP | 2008-03-05 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_IMVP Performance]] |
| INCO | NYSE Arca:INCO | 2011-08-10 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_INCO Performance]] |
| INQQ | NYSE Arca:INQQ | 2022-04-05 | 4.31 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_INQQ Performance]] |
| IPAC | NYSE Arca:IPAC | 2014-06-10 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_IPAC Performance]] |
| JPXN | NYSE Arca:JPXN | 2001-10-23 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_JPXN Performance]] |
| KBA | NYSE Arca:KBA | 2014-03-04 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_KBA Performance]] |
| KCAI | NYSE Arca:KCAI | 2024-08-27 | 1.91 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_KCAI Performance]] |
| KDEF | NYSE Arca:KDEF | 2025-02-05 | 1.47 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_KDEF Performance]] |
| KGRN | NYSE Arca:KGRN | 2017-10-12 | 8.79 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_KGRN Performance]] |
| KMCA | NYSE Arca:KMCA | 2026-05-06 | 0.22 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_KMCA Performance]] |
| KSTR | NYSE Arca:KSTR | 2021-01-26 | 5.49 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_KSTR Performance]] |
| KTEC | NYSE Arca:KTEC | 2021-06-08 | 5.13 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_KTEC Performance]] |
| KURE | NYSE Arca:KURE | 2018-01-31 | 8.48 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_KURE Performance]] |
| KWEB | NYSE Arca:KWEB | 31 ก.ค. 2013 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_KWEB Performance]] |
| SCJ | NYSE Arca:SCJ | 2007-12-20 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_SCJ Performance]] |
| THD | NYSE Arca:THD | 2008-03-26 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_THD Performance]] |
| VNAM | NYSE Arca:VNAM | 2021-12-07 | 4.63 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_ARCA_VNAM Performance]] |
| VOO | NYSE Arca:VOO | 7 ก.ย. 2010 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_VOO Performance]] |
| VPL | NYSE Arca:VPL | 2005-03-04 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_VPL Performance]] |
| VSS | NYSE Arca:VSS | 2 เม.ย. 2009 | >=10.00 | official rolling/10-calendar-year NAV TR | unchanged; audited | EXPANDED_TO_10Y | none | Official NAV TR evidence qualifies; raw endpoints or annual-row gaps remain labeled where applicable | [[ETF_NYSE_ARCA_VSS Performance]] |
| KPHO | NYSE:KPHO | 2025-12-02 | 0.65 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_NYSE_KPHO Performance]] |
| VJPA | XETRA:VJPA | 2019-09-24 | 6.84 | official available NAV TR; <10y | unchanged; audited | ACCEPTED_SHORT_HISTORY | none | Inception under 10 years as of 2026-07-26; no 10-year proxy; official available history retained | [[ETF_XETRA_VJPA Performance]] |

## Source and calculation checks

- Every durable number remains owned by its performance page or dated source batch; the master index and region pages are navigation/snapshot consumers.
- Updated FLAU figures: official NAV TR YTD `9.50%` as of `2026-07-17`; since-inception NAV annualized `7.53%` as of `2026-06-30`; 10-year field remains `—` because inception is `2017-11-02`.
- Updated EPHE figure: official NAV TR YTD `2.76%` as of `2026-07-23`; official rolling 10-year NAV TR remains cumulative `-28.05%` / CAGR `-3.24%` from `2016-06-30` to `2026-06-30`; 2016-2020 annual rows remain not disclosed.
- Verified AAXJ: official rolling 10-year NAV TR cumulative `164.36%` / CAGR `10.21%` for `2016-06-30` to `2026-06-30`; current NAV TR YTD `21.30%` as of `2026-07-22`.
- Verified FLCA: official inception `2017-11-02`, current YTD `8.17%` as of `2026-07-06`, and 10-year field `—`; no 10-year proxy.
- S&P 500 comparisons retain the cached 2016-2025 USD total-return convention where eligible; date-to-date/current-YTD references are kept separate.

## Graph and link verification

- Canonical performance page filenames resolve.
- Every performance page appears exactly once in the audit table. The unique canonical target sets in the master index and primary region navigation each cover all 143 pages; repeated index references and non-primary snapshot rows are not counted as ownership.
- Every affected page retains the breadcrumb `[[ETF Region Index]] → [[<Region> ETF]] → [[ETF Performance Index]]`, canonical geography tag, and performance-page ownership of numeric data.
- FLAU remains in `Australia ETF`; EPHE remains in `Philippines ETF`; no region page was duplicated or moved.

## Follow-up

ไม่มี action-blocking gap. Retain current-source as-of dates and recheck short-history pages when they reach their 10-year anniversary.

## Review record

 - Independent pre-save review: PASS after correcting stale YTD occurrences, source-batch pointers, visible as-of dates, qualified KWEB identifiers, repeated-link wording, and complete evidence-packet coverage.
