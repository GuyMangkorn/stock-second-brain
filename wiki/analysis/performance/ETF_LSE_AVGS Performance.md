---
type: etf-performance
instrument_type: ETF
entity_key: LSE:AVGS
ticker: AVGS
input_ticker: AGSCF
exchange: London Stock Exchange
fund: Avantis Global Small Cap Value UCITS ETF
tracked_index: no specific index; actively managed
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: systematic-active
management_benchmark: MSCI World Small Cap Value Index
track_record: developing-short-live-history
management_evidence: positive-return-evidence
risk_evidence: not-verified
updated: 2026-08-17
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/AVGS
  - ticker/AGSCF
  - geography/International
---

# AVGS Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

AGSCF เป็น input alias ของ official USD listing `LSE:AVGS` ของ Avantis Global
Small Cap Value UCITS ETF. กองทุนเป็น active long-only international small-cap
value ETF ที่ใช้ systematic-active process และไม่ได้มุ่ง replicate ดัชนีใด
โดยเฉพาะ. Official factsheet ณ 2026-07-31 รายงาน NAV Total Return YTD
21.43% เทียบกับ management benchmark MSCI World Small Cap Value Index ที่
13.80% และ rolling 1-year 36.36% เทียบกับ 27.16%. ประวัติยังสั้นและ issuer
ไม่เปิดเผย annual calendar rows ใน source ที่ตรวจสอบได้ จึงไม่คำนวณ CAGR หรือ
hit rate จากช่วงที่ไม่ครบ.

## Performance check

- entity_key: LSE:AVGS; input_ticker: AGSCF; USD listing on London Stock Exchange
- Fund inception: 2024-09-25; LSE AVGS listing date: 2024-12-04; ISIN IE0003R87OG3
- Ongoing charges figure: 0.39% p.a.; product structure physical; use of income accumulating; domicile Ireland; legal structure UCITS ETF
- Metric: official NAV Total Return; factsheet states that returns assume reinvestment of dividends and capital gains; currency USD
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark only)
- management_mode: active-equity-long-only
- active_process: systematic-active; Avantis combines broad diversification and low turnover with active valuation/profitability tilts and daily active oversight
- management_benchmark: MSCI World Small Cap Value Index, the official strategy-aligned small-cap developed-market value comparator
- track_record: developing-short-live-history; inception is 2024-09-25 and the reviewed factsheet has less than two years of annualized-history context
- management_evidence: positive return-only; official YTD excess is +7.63 pp and rolling 1-year excess is +9.20 pp
- risk_evidence: not-verified; compatible daily NAV history for maximum drawdown and recovery was not captured
- 10-year and 2021-2025 windows: not applicable; history is under 10 years and the fund started after 2021
- Coverage/source note: official factsheet as of 2026-07-31 reports YTD and 1-year rows but no complete calendar-year table or ITD annualized figure; no unsupported annual rows were backfilled

| Window | AVGS NAV TR | Management benchmark | Excess return |
|---|---:|---:|---:|
| 2026 YTD | 21.43% | 13.80% | +7.63 pp |
| Rolling 1-year | 36.36% | 27.16% | +9.20 pp |

S&P 500 TR เป็น common reference benchmark ที่ไม่ได้ใช้เป็น management
benchmark ของ AVGS; same-date S&P current-YTD pairing was not captured.

## Up years / Down years

- Up years / Down years: ไม่พบข้อมูลที่ยืนยันได้ เพราะ official factsheet ไม่แสดง complete calendar-year rows
- Best / worst calendar year: ไม่พบข้อมูลที่ยืนยันได้
- 2026 YTD: NAV TR 21.43% as of 2026-07-31; management benchmark 13.80%
- Rolling 1-year: NAV TR 36.36% as of 2026-07-31; management benchmark 27.16%
- Cumulative, CAGR and hit rate: ไม่พบข้อมูลที่ยืนยันได้จาก complete annual rows; ไม่คำนวณจาก partial/rolling windows

## Risk read-through

AVGS มี developed-market small-cap value exposure โดย official factsheet ระบุ
weighted average market cap ของกองทุน $3.6B เทียบ benchmark $8.9B, 1,701
holdings เทียบ benchmark 2,374 และ top ten holdings รวม 6.67% ณ 2026-07-31.
Top-country exposure ที่เปิดเผยคือ United States 69.24%, Japan 10.22%, United
Kingdom 3.61%, Canada 3.27% และ Australia 2.71%. Official risk text ระบุ
small-company, international/currency, market, liquidity และ derivative risks.
Official daily NAV history sufficient for reproducible maximum drawdown and
recovery was not verified, so no numeric drawdown claim is saved.

## Active management read-through

- management_mode: active-equity-long-only
- active_process: systematic-active
- management_benchmark: MSCI World Small Cap Value Index
- track_record: developing-short-live-history
- management_evidence: positive return-only
- risk_evidence: not-verified
- Official 2026 YTD active difference is +7.63 pp and rolling 1-year active difference is +9.20 pp. These are benchmark-relative return observations, not alpha.
- The selected benchmark is the official small-cap value comparator. The fund explicitly does not seek to replicate a specified index; its approach overweights lower-valuation and higher-profitability securities while retaining broad diversification and low-turnover implementation.
- The official factsheet identifies a portfolio management team including Eduardo Repetto, Ted Randall, Daniel Ong, Mitchell Firestein and Matthew Dubin. The live record remains too short for an established track-record label.

## Sources

- Official Avantis product page: https://www.avantisinvestors.com/ucitsetf/avantis-global-small-cap-value-ucits-etf/
- Official Avantis factsheet: https://res.avantisinvestors.com/docs/avantis-global-small-cap-value-ucits-etf-fact-sheet.pdf
- Official London Stock Exchange company page: https://www.londonstockexchange.com/stock/AVGS/american-century-icav/company-page
- Central Bank of Ireland fund register: https://registers.centralbank.ie/%28S%28atb1s1eysq1bdt45cyzep0nm%29%29/FundRegisterDataPage.aspx?fundReferenceNumber=C544701&register=28
