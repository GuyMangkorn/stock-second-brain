---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:PIZ
input_ticker: PIZ
input_alias: PIZ
ticker: PIZ
exchange: Nasdaq
fund: Invesco Dorsey Wright Developed Markets Momentum ETF
tracked_index: Dorsey Wright Developed Markets Tech Leaders Index
benchmark: S&P 500 Total Return
issuer_benchmark: Dorsey Wright Developed Markets Tech Leaders Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: long-running-fund
management_evidence: not applicable
risk_evidence: prospectus-fields
updated: 2026-09-02
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: not disclosed
price_nav_as_of: not disclosed
fund_facts_as_of: 2026-02-27
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-4.md
return_basis: USD NAV total return; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/PIZ
  - geography/International
  - geography/developed-markets
---

# PIZ Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

PIZ เป็น passive developed-market ex-U.S. momentum equity ETF ที่ติดตาม Dorsey
Wright Developed Markets Tech Leaders Index และใช้ full replication. Official NAV
Total Return ล่าสุดที่อ่านได้ครบถ้วนจาก Invesco คือ `9.04%` annualized สำหรับ 10 ปี
ณ `2025-12-31`; current 2026 NAV TR YTD และ current NAV/market price ยัง
`ไม่พบข้อมูลที่ยืนยันได้` จาก official performance module ที่ตรวจครั้งนี้. ช่วง
complete 2016-2025 ให้ CAGR `9.04%` จาก cumulative `137.57%` เทียบ S&P 500 TR
`14.82%`; ช่วง 2021-2025 ให้ CAGR `9.44%` จาก cumulative `56.98%` เทียบ
`14.43%`.

## Performance check

- `entity_key`: `Nasdaq:PIZ`; input ticker: `PIZ`; listing: Nasdaq Stock Market LLC
- CUSIP: `46138E875`; fund inception `2007-12-28`
- Management fee / total annual fund operating expenses: `0.80% / 0.80%` ตาม Summary Prospectus วันที่ `2026-02-27`
- Fund generally invests at least `90%` of total assets in the underlying index and uses full replication; the index selects approximately 100 large-cap companies from developed markets excluding the United States based on relative strength
- Latest official fund facts as of `2025-12-31`: 100 underlying securities; portfolio turnover `122%` in the latest fiscal year; Invesco's official table reports 30-day SEC yield `0.79%`
- Metric: official `ETF - NAV` total return; market-price return and underlying-index return are kept separate. The annual NAV series includes the fund's applicable expenses and distribution effects as reported by Invesco.
- Issuer benchmark: `Dorsey Wright Developed Markets Tech Leaders Index`; the index return is net of applicable withholding taxes but excludes fund fees and expenses
- Official average annual NAV total return as of `2025-12-31`: 1-year `36.34%`, 5-year `9.44%`, 10-year `9.04%`, since inception `5.47%`
- Current 2026 official NAV TR YTD, current NAV and current market price: `not disclosed` in the reviewed official product-page performance capture; no secondary price series is substituted for NAV total return.
- Calendar rows are from Invesco's official Q4 2025 table dated `2025-12-31`; S&P 500 TR uses the cached USD dividend-reinvested convention for 2016-2025.

| Year | PIZ NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | -7.99% | 11.96% |
| 2017 | 30.70% | 21.83% |
| 2018 | -16.18% | -4.38% |
| 2019 | 27.33% | 31.49% |
| 2020 | 17.91% | 18.40% |
| 2021 | 20.78% | 28.71% |
| 2022 | -30.47% | -18.11% |
| 2023 | 17.88% | 26.29% |
| 2024 | 16.31% | 25.02% |
| 2025 | 36.34% | 17.88% |

## Up years / Down years

- Complete 2016-2025 window: `7 / 3` up/down years
- Best complete year: 2025, `+36.34%`
- Least positive: 2024, `+16.31%`
- Worst complete year: 2022, `-30.47%`
- Least-bad down year: 2016, `-7.99%`
- Complete 2016-2025 cumulative return / rounded-input CAGR: `137.57% / 9.04%`
- Complete 2021-2025 window: `4 / 1` up/down years; cumulative return / rounded-input CAGR: `56.98% / 9.44%`
- Current official NAV TR YTD: `ไม่พบข้อมูลที่ยืนยันได้`; no current S&P 500 comparison is asserted.

## Risk read-through

PIZ ใช้ momentum selection และมี turnover สูง: Invesco prospectus ระบุว่า index
คัดหุ้นจาก developed markets นอกสหรัฐฯ ด้วย relative-strength score, มีประมาณ
100 securities และ fund turnover ล่าสุด `122%`. Prospectus ณ `2025-10-31` ระบุว่า
กองทุนมี significant exposure ต่อกลุ่ม Industrials และ Financials; น้ำหนัก
country/sector ปัจจุบันแบบละเอียด รวมถึง official standard deviation, beta และ
daily NAV history สำหรับคำนวณ maximum drawdown/recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`
จากชุด official sources ที่ตรวจ. ความเสี่ยงหลักจึงรวม momentum reversal, industry และ
geographic concentration, foreign-currency/ADR-GDR, mid-cap และ market-price/NAV
divergence; อย่าใช้ผลตอบแทนปี 2025 ที่สูงเป็นหลักฐานว่ากลยุทธ์จะทำได้ซ้ำ.

## Sources

- [Invesco official PIZ product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-dorsey-wright-developed-markets-momentum-etf.html) — official product identity and current performance module checked on `2026-09-02`; the reviewed capture did not expose current performance fields
- [SEC Summary Prospectus dated February 27, 2026](https://www.sec.gov/Archives/edgar/data/1378872/000119312526079042/d12489d497k.htm) — objective, index construction, fees, replication, turnover, risks and management continuity
- [Invesco official Q4 2025 fund performance table](https://www.invesco.com/us-rest/contentdetail?contentId=bbd2fd05f0e21410VgnVCM100000c2f1bf0aRCRD) — NAV/market-price/index/benchmark returns and calendar rows as of `2025-12-31`
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references and calculation convention: [[ETF_performance_sources_2026-09-02_run-4]]
