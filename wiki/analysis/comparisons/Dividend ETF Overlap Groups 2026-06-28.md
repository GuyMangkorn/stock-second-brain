---
type: etf_overlap_grouping
created: 2026-06-28
source_memo: wiki/analysis/comparisons/Dividend ETF Full Universe Triage 2026-06-28.md
universe_count: 100
grouped_count: 100
unknown_group_count: 0
custom-width: 90
---

# Dividend ETF Overlap Groups 2026-06-28
## Selected ETF Entities

[[ETF_AMEX_DGRO]] · [[ETF_AMEX_VIG]] · [[ETF_NASDAQ_VIGI]]

## Purpose

Memo นี้จัด ETF จาก `Dividend ETF Full Universe Triage 2026-06-28` เป็นกลุ่ม exposure/holdings ที่ใกล้เคียงกัน เพื่อช่วยหลีกเลี่ยงการซื้อ ETF หลายตัวที่ลงทุนซ้ำในสินทรัพย์หรือ factor เดียวกัน. การจัดกลุ่มใช้ข้อมูลใน memo เดิมเป็นหลัก ได้แก่ `Theme`, `Region`, fund name, และ `Top-10 theme read`; ไม่ได้เติม holdings fact ใหม่ที่ยังไม่ได้ verify.

คะแนน `Score` และ `Action Read` ถูกยกมาจาก memo เดิมเพื่อใช้ประกอบการ triage แต่ตารางนี้ไม่ได้ sort ตามคะแนนแล้ว. ภายในแต่ละกลุ่มเรียงตาม original `Sort` จาก universe memo เพื่อรักษา traceability.

Updated holdings workflow: `Dividend ETF Top 10 Holdings Tracker 2026-07-01` เป็น tracker ใหม่สำหรับเปลี่ยน grouping จาก description/theme inference ไปเป็น Top 10 holdings จริง. Memo นี้ยังใช้เป็น fallback description group สำหรับ ETF ที่ยังหา holdings ไม่เจอหรือยังไม่ได้ตรวจ official source.

## Grouping Rule

- Group by portfolio role first: dividend growth/core, broad dividend income, high-yield/value income, sector-only income, country/regional sleeves, and asset-class sleeves.
- Treat cross-listing / local wrappers as potential substitutes when the underlying exposure is likely similar, even if exchange/currency differs.
- If a fund cannot be assigned from current local evidence, put it in `G99 Unknown / needs issuer holdings refresh`; current verification found no unassigned ETF.
- Before order execution, refresh issuer holdings CSV/factsheet for the final shortlist because current `Top-10 theme read` is partly inferred for non-source-deepened ETFs.

## Group Coverage Summary

| Group | ETF Count | Avg Score | Overlap Rationale |
| --- | ---: | ---: | --- |
| G01 U.S. dividend growth / quality core | 7 | 7.0 | U.S. large-cap dividend growers / aristocrats and wrappers with similar U.S. dividend appreciation exposure. Overlap risk is high between these; pick one core vehicle unless there is a tax/listing reason. |
| G02 U.S. broad dividend large-cap income | 9 | 6.4 | Broad U.S. dividend payers with large-cap/value tilt. These can overlap heavily with VYM/DGRO-style portfolios, but usually have less strict growth screening than G01. |
| G03 U.S. high-dividend yield / value income | 6 | 6.2 | U.S. high-yield equity screens, often financials/utilities/energy/staples heavy. Do not stack several of these unless intentionally increasing high-yield/value and rate-sensitive exposure. |
| G04 U.S. dividend technology tilt | 2 | 6.1 | Mature technology dividend payers. This is a sector tilt, not a diversified dividend sleeve; overlap with Nasdaq/tech-heavy core equity should be checked separately. |
| G05 U.S. small/mid-cap dividend | 4 | 6.0 | U.S. small/mid dividend payers. Overlap with U.S. large-cap dividend groups is lower, but cyclicality/liquidity risk is higher. |
| G06 International dividend growth / quality | 4 | 6.3 | Non-U.S. or ex-U.S. dividend growers/aristocrats/quality screens. Use as a separate international quality sleeve; avoid doubling with broad global dividend funds if the holdings CSV later shows the same countries/sectors. |
| G07 International/global broad dividend income | 8 | 6.0 | Broad international/global dividend equity exposure. These are likely substitutes for one another when the goal is global dividend income rather than a country-specific sleeve. |
| G08 International/global high-dividend yield | 9 | 5.3 | High-yield international/global dividend screens. Similar risk bucket to G03 but with extra country/FX concentration; avoid stacking multiple high-yield global funds. |
| G09 Europe/UK dividend equity | 14 | 6.1 | Europe/UK regional dividend ETFs and UCITS wrappers. The common risk is Europe financials, energy, utilities, telecom, and FX exposure. |
| G10 Canada dividend equity | 6 | 6.1 | Canada dividend/high-dividend ETFs, usually banks, pipelines, utilities, telecom, and energy heavy. Treat as one Canada income sleeve. |
| G11 Australia dividend equity | 4 | 5.8 | Australia dividend ETFs, often banks/resources/defensive income. This is a country sleeve with AUD exposure. |
| G12 Japan dividend equity | 5 | 5.1 | Japan dividend/high-yield equity ETFs. This is a Japan country sleeve; `AMEX:DFJ` is grouped here because the fund name indicates Japan small-cap dividend exposure. |
| G13 Emerging Asia / EM high-dividend equity | 12 | 4.8 | Emerging-market, Taiwan, Korea, China/HK, and EM small-cap dividend funds. These may not hold identical names, but the portfolio role and macro risks overlap strongly. |
| G14 Energy / MLP infrastructure income | 3 | 4.8 | Pipelines, midstream, and MLP infrastructure income. This is commodity/rate/tax-structure sensitive and should not be treated as a normal dividend equity sleeve. |
| G15 Financials / bank-only income | 4 | 4.1 | Bank/financial-only dividend products. This is concentrated sector income exposure; avoid combining with Canada dividend funds without checking aggregate bank weight. |
| G16 REIT / property income | 3 | 3.8 | REIT/property-income ETFs. Rate-sensitive real estate sleeve; separate from broad dividend equities. |
| G99 Unknown / needs issuer holdings refresh | 0 | not applicable | Reserved bucket for ETFs that cannot be assigned from current local evidence. Verification currently shows zero ETFs in this group. |

## ETF Groups

### G01 U.S. dividend growth / quality core

Overlap rationale: U.S. large-cap dividend growers / aristocrats and wrappers with similar U.S. dividend appreciation exposure. Overlap risk is high between these; pick one core vehicle unless there is a tax/listing reason.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 8 | `AMEX:SDY` | State Street SPDR S&P Dividend ETF | U.S. | Broad dividend equity | 2.50% | 6.4 | Satellite / tactical only |
| 12 | `CBOE:NOBL` | ProShares S&P 500 Dividend Aristocrats ETF | U.S. | Dividend growth / quality | 2.12% | 6.9 | Income sleeve / watch |
| 16 | `AMEX:VIG` | Vanguard Dividend Appreciation ETF | U.S. | Dividend growth / quality | 1.70% | 8.2 | Core candidate |
| 20 | `TSX:VGG` | Vanguard US Dividend Appreciation Index ETF | Canada-listed / Canada or U.S.-tilt | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 7.5 | Income sleeve / watch |
| 23 | `NASDAQ:PEY` | Invesco High Yield Equity Dividend Achievers ETF | U.S. | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 7.2 | Income sleeve / watch |
| 31 | `NASDAQ:PFM` | Invesco Dividend Achievers ETF | U.S. | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 6.5 | Satellite / tactical only |
| 33 | `TSX:VGH` | Vanguard US Dividend Appreciation Index ETF (CAD-hedged) | Canada-listed / Canada or U.S.-tilt | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 6.4 | Satellite / tactical only |

### G02 U.S. broad dividend large-cap income

Overlap rationale: Broad U.S. dividend payers with large-cap/value tilt. These can overlap heavily with VYM/DGRO-style portfolios, but usually have less strict growth screening than G01.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 13 | `AMEX:DTD` | WisdomTree U.S. Total Dividend Fund | U.S. | Broad dividend equity | 1.98% | 7.0 | Income sleeve / watch |
| 14 | `AMEX:DGRO` | iShares Core Dividend Growth ETF | U.S. | Broad dividend equity | 1.96% | 8.1 | Core candidate |
| 15 | `AMEX:DLN` | WisdomTree U.S. LargeCap Dividend Fund | U.S. | Large-cap dividend | 1.90% | 7.0 | Income sleeve / watch |
| 19 | `AMEX:DJD` | Invesco Dow Jones Industrial Average Dividend ETF | U.S. | Large-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 7.5 | Income sleeve / watch |
| 22 | `AMEX:SDOG` | ALPS Sector Dividend Dogs ETF | U.S. | Large-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 7.2 | Income sleeve / watch |
| 34 | `AMEX:FVD` | First Trust Value Line Dividend Index Fund | U.S. | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 48 | `AMEX:QDPL` | Pacer Metaurus US Large Cap Dividend Multiplier 400 ETF | U.S. | Large-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 77 | `KRX:402970` | KIM ACE S&P US Dividend 100 ETF | Korea-listed / Korea or U.S.-tilt | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.0 | Avoid / mandate-only |
| 92 | `KRX:489250` | SAMSUNG KODEX US Dividend Dow Jones ETF | Korea-listed / Korea or U.S.-tilt | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |

### G03 U.S. high-dividend yield / value income

Overlap rationale: U.S. high-yield equity screens, often financials/utilities/energy/staples heavy. Do not stack several of these unless intentionally increasing high-yield/value and rate-sensitive exposure.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 1 | `AMEX:SPYD` | State Street SPDR Portfolio S&P 500 High Dividend ETF | U.S. | High dividend yield | 4.40% | 6.5 | Satellite / tactical only |
| 5 | `AMEX:DHS` | WisdomTree U.S. High Dividend Fund | U.S. | High dividend yield | 3.59% | 5.9 | Satellite / tactical only |
| 6 | `AMEX:FDVV` | Fidelity High Dividend ETF | U.S. | High dividend yield | 3.20% | 7.1 | Income sleeve / watch |
| 9 | `AMEX:VYM` | Vanguard High Dividend Yield Index ETF | U.S. | High dividend yield | 2.40% | 7.3 | Income sleeve / watch |
| 49 | `NASDAQ:DVY` | iShares Select Dividend ETF | U.S. | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 80 | `XETR:EXX5` | iShares Dow Jones U.S. Select Dividend UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 4.9 | Avoid / mandate-only |

### G04 U.S. dividend technology tilt

Overlap rationale: Mature technology dividend payers. This is a sector tilt, not a diversified dividend sleeve; overlap with Nasdaq/tech-heavy core equity should be checked separately.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 30 | `NASDAQ:TDIV` | First Trust NASDAQ Technology Dividend Index Fund | U.S. | Technology dividend | ไม่พบข้อมูลที่ยืนยันได้ | 6.6 | Satellite / tactical only |
| 55 | `CBOE:TDV` | ProShares S&P Technology Dividend Aristocrats ETF | U.S. | Technology dividend | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |

### G05 U.S. small/mid-cap dividend

Overlap rationale: U.S. small/mid dividend payers. Overlap with U.S. large-cap dividend groups is lower, but cyclicality/liquidity risk is higher.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 7 | `AMEX:DES` | WisdomTree U.S. SmallCap Dividend Fund | U.S. | Small-cap dividend | 3.00% | 6.2 | Satellite / tactical only |
| 10 | `AMEX:DON` | WisdomTree U.S. MidCap Dividend Fund | U.S. | Mid-cap dividend | 2.40% | 6.2 | Satellite / tactical only |
| 39 | `CBOE:REGL` | ProShares S&P MidCap 400 Dividend Aristocrats ETF | U.S. | Mid-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 59 | `CBOE:SMDV` | ProShares Russell 2000 Dividend Growers ETF | U.S. | Small-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 5.5 | Avoid / mandate-only |

### G06 International dividend growth / quality

Overlap rationale: Non-U.S. or ex-U.S. dividend growers/aristocrats/quality screens. Use as a separate international quality sleeve; avoid doubling with broad global dividend funds if the holdings CSV later shows the same countries/sectors.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 11 | `NASDAQ:VIGI` | Vanguard International Dividend Appreciation ETF | International / global | Dividend growth / quality | 2.20% | 7.7 | Core candidate |
| 32 | `XETR:ZPRG` | SSGA SPDR ETFs Europe I PLC - State Street SPDR S&P Global Dividend Aristocrats UCITS ETF Ptg USD | Europe-listed UCITS / global or regional | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 6.5 | Satellite / tactical only |
| 46 | `NASDAQ:PID` | Invesco International Dividend Achievers ETF | International / global | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 5.9 | Satellite / tactical only |
| 74 | `XETR:ZPRA` | SSGA SPDR ETFs Europe I PLC - State Street SPDR S&P Pan Asia Dividend Aristocrats UCITS ETF Ptg USD | Europe-listed UCITS / global or regional | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |

### G07 International/global broad dividend income

Overlap rationale: Broad international/global dividend equity exposure. These are likely substitutes for one another when the goal is global dividend income rather than a country-specific sleeve.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 17 | `AMEX:DIVI` | Franklin International Core Dividend Tilt Index Fund | International / global | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 7.9 | Core candidate |
| 26 | `CBOE:DDWM` | WisdomTree Dynamic International Equity Fund | International / global | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 6.9 | Income sleeve / watch |
| 38 | `AMEX:WDIV` | State Street SPDR S&P Global Dividend ETF | International / global | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 52 | `ASX:WDIV` | State Street SPDR S&P Global Dividend ETF | Australia-listed / Australia or global | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.7 | Avoid / mandate-only |
| 54 | `AMEX:DWM` | WisdomTree International Equity Fund | International / global | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 65 | `AMEX:IDOG` | ALPS International Sector Dividend Dogs ETF | International / global | Large-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 71 | `AMEX:DWX` | State Street SPDR S&P International Dividend ETF | International / global | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |
| 72 | `NASDAQ:MDIV` | Multi-Asset Diversified Income Index Fund | U.S. | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |

### G08 International/global high-dividend yield

Overlap rationale: High-yield international/global dividend screens. Similar risk bucket to G03 but with extra country/FX concentration; avoid stacking multiple high-yield global funds.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 2 | `CBOE:IDV` | iShares International Select Dividend ETF | International / global | High dividend yield | 4.36% | 5.9 | Satellite / tactical only |
| 3 | `NASDAQ:VYMI` | Vanguard International High Dividend Yield ETF | International / global | High dividend yield | 4.20% | 6.4 | Satellite / tactical only |
| 45 | `LSE:VHYA` | Vanguard Funds PLC - Vanguard FTSE All-World High Dividend Yield UCITS ETF AccumUSD | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.0 | Satellite / tactical only |
| 47 | `XETR:ISPA` | iShares STOXX Global Select Dividend 100 UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.9 | Satellite / tactical only |
| 64 | `XETR:XGSD` | Xtrackers STOXX GLOBAL SELECT DIVIDEND 100 SWAP UCITS ETF Distribution 1D | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 76 | `AMEX:FDD` | First Trust Stoxx European Select Dividend Index Fund | International / global | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.0 | Avoid / mandate-only |
| 83 | `AMEX:DTH` | WisdomTree International High Dividend Fund | International / global | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |
| 88 | `AMEX:SDIV` | Global X Superdividend ETF | International / global | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 4.2 | Avoid / mandate-only |
| 91 | `TSX:FCID` | Fidelity International High Dividend ETF Trust Units Series L | Canada-listed / Canada or U.S.-tilt | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 4.0 | Avoid / mandate-only |

### G09 Europe/UK dividend equity

Overlap rationale: Europe/UK regional dividend ETFs and UCITS wrappers. The common risk is Europe financials, energy, utilities, telecom, and FX exposure.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 18 | `SIX:CHDVD` | iShares Swiss Dividend ETF (CH) | Europe-listed UCITS / global or regional | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 7.6 | Income sleeve / watch |
| 24 | `XETR:SPYW` | State Street SPDR S&P Euro Dividend Aristocrats UCITS ETF EUR | Europe-listed UCITS / global or regional | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 7.2 | Income sleeve / watch |
| 25 | `EURONEXT:TDIV` | VanEck Vectors ETFs NV - Morningstar Dev. Mrkts. Div. Ldrs. | Europe-listed UCITS / global or regional | Large-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 7.1 | Income sleeve / watch |
| 27 | `LSE:IUKD` | iShares UK Dividend UCITS ETF GBP | Europe-listed UCITS / global or regional | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 6.9 | Income sleeve / watch |
| 37 | `XETR:EXSH` | iShares STOXX Europe Select Dividend 30 UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 41 | `XETR:DXSA` | Xtrackers Euro Stoxx Quality Dividend UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 42 | `XETR:QDVD` | iShares MSCI USA Quality Dividend ESG UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 51 | `XETR:ELFC` | Deka EURO iSTOXX ex Fin Dividend+ UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 53 | `XETR:EXSB` | iShares DivDAX UCITS ETF (DE) | Europe-listed UCITS / global or regional | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.7 | Avoid / mandate-only |
| 56 | `EURONEXT:SEL` | Amundi STOXX Europe Select Dividend 30 - UCITS ETF Dist | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 67 | `XETR:EL4G` | Deka EURO STOXX Select Dividend 30 UCITS ETF | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 68 | `XETR:EXSG` | iShares Euro Stoxx Select Dividend 30 UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 69 | `XETR:EXXW` | iShares Dow Jones Asia Pacific Select Dividend 30 UCITS ETF | Europe-listed UCITS / global or regional | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 87 | `XETR:EL4X` | Deka DAXplus Maximum Dividend UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 4.3 | Avoid / mandate-only |

### G10 Canada dividend equity

Overlap rationale: Canada dividend/high-dividend ETFs, usually banks, pipelines, utilities, telecom, and energy heavy. Treat as one Canada income sleeve.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 21 | `TSX:VDY` | Vanguard FTSE Canadian High Dividend Yield Index ETF | Canada-listed / Canada or U.S.-tilt | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 7.3 | Income sleeve / watch |
| 28 | `TSX:XEI` | iShares S&P/TSX Composite High Dividend Index ETF | Canada-listed / Canada or U.S.-tilt | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.8 | Income sleeve / watch |
| 40 | `TSX:VIDY` | Vanguard FTSE Developed ex North America High Dividend Yield | Canada-listed / Canada or U.S.-tilt | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 50 | `TSX:PDC` | Invesco Canadian Dividend Index ETF | Canada-listed / Canada or U.S.-tilt | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 58 | `TSX:CDZ` | iShares S&P/TSX Canadian Dividend Aristocrats Index ETF | Canada-listed / Canada or U.S.-tilt | Dividend growth / quality | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 73 | `TSX:FCCD` | Fidelity Canadian High Dividend ETF Trust Units Series L | Canada-listed / Canada or U.S.-tilt | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |

### G11 Australia dividend equity

Overlap rationale: Australia dividend ETFs, often banks/resources/defensive income. This is a country sleeve with AUD exposure.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 29 | `ASX:VHY` | Vanguard Australian Shares High Yield ETF | Australia-listed / Australia or global | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.6 | Satellite / tactical only |
| 35 | `ASX:IHD` | iShares S&P/ASX Dividend Opportunities ETF | Australia-listed / Australia or global | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 62 | `ASX:SYI` | State Street SPDR MSCI Australia Select High Dividend Yield ETF | Australia-listed / Australia or global | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 84 | `ASX:RDV` | Russell Investments High Dividend Australian Shares ETF | Australia-listed / Australia or global | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |

### G12 Japan dividend equity

Overlap rationale: Japan dividend/high-yield equity ETFs. This is a Japan country sleeve; `AMEX:DFJ` is grouped here because the fund name indicates Japan small-cap dividend exposure.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 43 | `TSE:1489` | Next Funds Nikkei 225 High Dividend Yield Stock 50 Index ETF | Japan | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.1 | Satellite / tactical only |
| 44 | `TSE:1577` | NEXT FUNDS Nomura Japan Equity High Dividend 70 Exchange Traded Fund | Japan | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.1 | Satellite / tactical only |
| 81 | `TSE:1698` | Listed Index Fund Japan High Dividend (TSE Dividend Focus 100) | Japan | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 4.8 | Avoid / mandate-only |
| 82 | `AMEX:DFJ` | WisdomTree Japan SmallCap Dividend Fund | International / global | Small-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |
| 97 | `TSE:2564` | Global X MSCI SuperDividend Japan ETF | Japan | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 3.7 | Avoid / mandate-only |

### G13 Emerging Asia / EM high-dividend equity

Overlap rationale: Emerging-market, Taiwan, Korea, China/HK, and EM small-cap dividend funds. These may not hold identical names, but the portfolio role and macro risks overlap strongly.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 4 | `AMEX:DEM` | WisdomTree Emerging Markets High Dividend Fund | International / global | High dividend yield | 4.10% | 4.8 | Avoid / mandate-only |
| 36 | `KRX:161510` | Hanwha PLUS High Dividend ETF | Korea-listed / Korea or U.S.-tilt | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 57 | `KRX:315960` | KB RISE Large Cap High Dividend10TR ETF | Korea-listed / Korea or U.S.-tilt | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 60 | `AMEX:DLS` | WisdomTree International SmallCap Dividend Fund | International / global | Small-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 63 | `TWSE:00918` | United Taiwan High Dividend Recovery 30 ETF | Taiwan | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 66 | `TWSE:00919` | Capital TIP Customized Taiwan Select High Dividend ETF | Taiwan | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 75 | `AMEX:DGS` | WisdomTree Emerging Markets SmallCap Dividend Fund | International / global | Small-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 5.0 | Avoid / mandate-only |
| 85 | `CBOE:DDLS` | WisdomTree Dynamic International SmallCap Equity Fund | International / global | Small-cap dividend | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |
| 89 | `SZSE:159691` | ICBCCS CSI Hong Kong Connect High Dividend Yield Select ETF Units | SZSE | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 4.2 | Avoid / mandate-only |
| 94 | `SSE:513910` | SOEs Dividend Index Exchange Traded Fund Units | China / Hong Kong | Broad dividend equity | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |
| 96 | `SSE:513690` | Bosera Hang Seng High Dividend Yield ETF | China / Hong Kong | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 3.7 | Avoid / mandate-only |
| 98 | `HKEX:3110` | Global X Hang Seng High Dividend Yield ETF | China / Hong Kong | High dividend yield | ไม่พบข้อมูลที่ยืนยันได้ | 3.5 | Avoid / mandate-only |

### G14 Energy / MLP infrastructure income

Overlap rationale: Pipelines, midstream, and MLP infrastructure income. This is commodity/rate/tax-structure sensitive and should not be treated as a normal dividend equity sleeve.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 61 | `AMEX:ENFR` | Alerian Energy Infrastructure ETF | U.S. | Energy / MLP infrastructure | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 70 | `AMEX:AMLP` | Alerian MLP ETF | U.S. | Energy / MLP infrastructure | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |
| 93 | `LSE:MLPD` | Invesco Morningstar US Energy Infrastructure MLP UCITS ETF | Europe-listed UCITS / global or regional | Energy / MLP infrastructure | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |

### G15 Financials / bank-only income

Overlap rationale: Bank/financial-only dividend products. This is concentrated sector income exposure; avoid combining with Canada dividend funds without checking aggregate bank weight.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 78 | `TSX:RBNK` | RBC Canadian Bank Yield Index ETF | Canada-listed / Canada or U.S.-tilt | Financials / bank dividend | ไม่พบข้อมูลที่ยืนยันได้ | 4.9 | Avoid / mandate-only |
| 79 | `TSX:TBNK` | TD Canadian Bank Dividend Index ETF | Canada-listed / Canada or U.S.-tilt | Financials / bank dividend | ไม่พบข้อมูลที่ยืนยันได้ | 4.9 | Avoid / mandate-only |
| 86 | `KRX:466940` | MIRAE ASSET TIGER Bank High Dividend Plus TOP 10 Fn ETF Units | Korea-listed / Korea or U.S.-tilt | Financials / bank dividend | ไม่พบข้อมูลที่ยืนยันได้ | 4.4 | Avoid / mandate-only |
| 100 | `NASDAQ:KBWD` | Invesco KBW High Dividend Yield Financial ETF | U.S. | Financials / bank dividend | ไม่พบข้อมูลที่ยืนยันได้ | 2.0 | Avoid / mandate-only |

### G16 REIT / property income

Overlap rationale: REIT/property-income ETFs. Rate-sensitive real estate sleeve; separate from broad dividend equities.

| Original Sort | ETF | Fund | Region | Theme | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 90 | `NASDAQ:KBWY` | Invesco KBW Premium Yield Equity REIT ETF | U.S. | REIT / property income | ไม่พบข้อมูลที่ยืนยันได้ | 4.0 | Avoid / mandate-only |
| 95 | `TSE:1660` | MAXIS High Yield J-REIT ETF | Japan | REIT / property income | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |
| 99 | `LSE:DPYA` | iShares Developed Markets Property Yield UCITS ETF | Europe-listed UCITS / global or regional | REIT / property income | ไม่พบข้อมูลที่ยืนยันได้ | 3.5 | Avoid / mandate-only |

### G99 Unknown / needs issuer holdings refresh

Overlap rationale: Reserved bucket for ETFs that cannot be assigned from current local evidence. Verification currently shows zero ETFs in this group.

ไม่พบ ETF ที่ต้องใส่ใน unknown group หลัง verification รอบนี้.

## Verification

- Source universe rows: `100`
- Assigned ETF rows: `100`
- Unknown group rows: `0`
- Duplicate assignment check: no ETF assigned to more than one group.
- Unassigned check: no ETF left without a group.

## Source Map

- Source memo: `wiki/analysis/comparisons/Dividend ETF Full Universe Triage 2026-06-28.md`
- Local source universe: `raw/assets/ETF ที่เน้นการจ่ายเงินปันผล.md`
