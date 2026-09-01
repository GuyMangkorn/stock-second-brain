---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IDWP
ticker: IDWP
input_ticker: ISPFF
exchange: London Stock Exchange
fund: iShares Developed Markets Property Yield UCITS ETF USD (Dist)
tracked_index: FTSE EPRA Nareit Developed Dividend+ Net Index in USD
benchmark: FTSE EPRA Nareit Developed Dividend+ Net Index in USD
updated: 2026-09-01
performance_as_of: 2026-08-27
annual_rows_as_of: 2026-03-31
current_ytd_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IDWP
  - geography/International
---

# IDWP Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

`ISPFF` เป็น OTC alias ของกอง iShares เดียวกับ USD-distributing share class ที่มี official listing บน London Stock Exchange เป็น `IDWP` (ISIN `IE00B1FZS350`); จึงใช้ `entity_key: LSE:IDWP` เป็น canonical identity. NAV Total Return ล่าสุดที่ยืนยันได้คือ YTD `10.11%` ณ 2026-08-27 และ NAV ล่าสุดคือ USD `25.65` ณ 2026-08-28. Calendar-year NAV TR 2016-2025 ให้ผลสะสม `36.77%` หรือ rounded-input CAGR `3.18%`; ในช่วง 2021-2025 ให้ผลสะสม `12.79%` หรือ CAGR `2.44%`, ต่ำกว่า S&P 500 Total Return ที่ `14.43%` ต่อปีในช่วงเดียวกัน. ผลลัพธ์มีความไวต่อ interest rates, property cycle และ sector concentration.

## Performance check

- entity_key: LSE:IDWP; input alias: OTC:ISPFF; canonical listing: London Stock Exchange `IDWP` in USD, confirmed by the official listing table and ISIN `IE00B1FZS350`
- Fund: iShares Developed Markets Property Yield UCITS ETF USD (Dist)
- Classification: passive index-tracking equity ETF focused on listed real estate companies and REITs
- Inception: 2006-10-20; total expense ratio: 0.59%; quarterly distributing; physical and optimised replication
- Issuer benchmark: FTSE EPRA Nareit Developed Dividend+ Net Index in USD
- NAV Total Return: USD NAV basis with gross income reinvested where applicable; fund expenses are reflected in NAV. Market-price returns may differ
- Current official snapshot: NAV USD 25.65 as of 2026-08-28; NAV Total Return YTD 10.11% as of 2026-08-27; net assets USD 1,180,449,055 and 312 holdings as of 2026-08-28/2026-08-27 respectively
- Issuer-reported annualised NAV TR as of 2026-06-30: 1-year 16.30%, 3-year 8.75%, 5-year 1.03%, 10-year 2.81%, since inception 3.62%. These are kept as issuer-reported rolling figures and are not recomputed from undisclosed endpoints
- 2016-2025: cumulative 36.77%; rounded-input CAGR 3.18%
- 2021-2025: cumulative 12.79%; rounded-input CAGR 2.44%
- Official 3-year standard deviation is 16.05% and 3-year beta is 0.998, both as of 2026-07-31
- Common benchmark: S&P 500 Total Return in USD with dividends reinvested; cached reference as of 2025-12-31, used only as a broad reference rather than the strategy benchmark

### Annual NAV TR

| Calendar year | IDWP NAV TR | FTSE benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 5.50% | 5.52% | 11.96% |
| 2017 | 10.59% | 10.53% | 21.83% |
| 2018 | -5.80% | -5.75% | -4.38% |
| 2019 | 21.95% | 21.97% | 31.49% |
| 2020 | -9.47% | -9.56% | 18.40% |
| 2021 | 25.18% | 25.28% | 28.71% |
| 2022 | -24.33% | -24.17% | -18.11% |
| 2023 | 8.92% | 8.87% | 26.29% |
| 2024 | 1.00% | 1.06% | 25.02% |
| 2025 | 8.24% | 8.28% | 17.88% |

จาก rounded annual inputs, 2016-2025 IDWP CAGR `3.18%` เทียบ S&P 500 TR `14.82%` เป็น spread `-11.64` percentage points. ช่วง 2021-2025 IDWP CAGR `2.44%` เทียบ S&P `14.43%` เป็น spread `-11.99` percentage points. ความแตกต่างระหว่าง fund กับ FTSE benchmark ในแต่ละปีอยู่ใกล้เคียงกันและสอดคล้องกับ implementation drag ขนาดเล็ก ไม่ใช่หลักฐานของ manager alpha.

## Up years / Down years

- Up years: 7; down years: 3
- Best year: 2021, +25.18%
- Least-positive year: 2024, +1.00%
- Worst year: 2022, -24.33%
- Least-bad down year: 2018, -5.80%

## Risk read-through

ช่วง 2016-2025 population standard deviation จาก rounded calendar rows อยู่ที่ประมาณ `13.95%`; official 3-year standard deviation ล่าสุดสูงกว่าเล็กน้อยที่ `16.05%`. กองมี exposure กระจุกใน listed real estate/REITs จำนวน 312 holdings จึงมี sector concentration และ sensitivity ต่อ interest rates, financing cost, property valuation, local property markets, currency และ counterparty risk. การมี total-return NAV ที่รวม distributions ไม่ได้แปลว่าราคาตลาดของ listing `IDWP` จะเท่ากับ NAV เสมอ. Official daily NAV history สำหรับคำนวณ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น `not disclosed` และไม่ใช้ secondary proxy.

## Sources

- [Official iShares product page](https://www.ishares.com/uk/individual/en/products/251801/?siteEntryPassthrough=true)
- [Official iShares factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/iwdp-ishares-developed-markets-property-yield-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y)
- [Official KIID](https://www.ishares.com/uk/professional/en/literature/kiid/ucits_kiid-ishares-developed-markets-property-yield-ucits-etf-usd-dist-gb-ie00b1fzs350-en.pdf?siteEntryPassthrough=true)
- Source batch: [[ETF_performance_sources_2026-09-01_run-5]]
