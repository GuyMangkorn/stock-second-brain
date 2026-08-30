---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:PBPH
ticker: PBPH
exchange: Nasdaq
fund: Portfolio Building Block World Pharma and Biotech Index ETF
tracked_index: BITA Global Pharma and Biotech Select Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-30
performance_as_of: 2026-07-31
calendar_years_as_of: not applicable (no complete calendar year)
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; distributions included; net of fund expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/PBPH
  - geography/International
---

# PBPH Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

PBPH เป็น passive/index-tracking thematic equity ETF ของ Portfolio Building
Block ที่ให้ exposure ต่อ global pharmaceutical และ biotechnology companies
ผ่าน `BITA Global Pharma and Biotech Select Index`. กองทุนเริ่ม 24 พ.ย. 2025
จึงยังไม่มี complete calendar year, 10-year CAGR หรือ 2021-2025 comparison ที่
คำนวณได้อย่างถูกต้อง.

Official NAV Total Return ณ 31 ก.ค. 2026 คือ `+7.69%` YTD และ since inception
สะสม `+8.74%`; market-price return คือ `+7.71%` YTD และ `+8.86%` since
inception. Latest reviewed official pricing snapshot ณ 27 ส.ค. 2026 แสดง NAV
`US$29.00` และ closing price `US$29.05`; same-page capture ที่เก่ากว่า ณ 26
ส.ค. แสดง `US$29.31`/`US$29.33`, จึงเก็บเป็น source conflict และไม่ใช้ราคาใน
NAV performance synthesis.

## Performance check

- `entity_key: NASDAQ:PBPH`; official ticker: `PBPH`; primary exchange: `Nasdaq`
- Fund: `Portfolio Building Block World Pharma and Biotech Index ETF`; issuer/adviser: Tidal Trust IV / Tidal Investments LLC
- Classification: supported passive/index-tracking equity ETF; the SEC summary prospectus states a passive indexing approach and direct equity exposure, not bond, commodity, leveraged, inverse, option-income or derivative-heavy exposure
- Inception: `2025-11-24`; no complete calendar year and no applicable 10-year or 2021-2025 CAGR
- Metric: `NAV Total Return` บนฐาน USD; official page reports NAV and market-price returns separately, with distributions included in the return series; fund expenses are reflected in NAV performance
- Tracked index: `BITA Global Pharma and Biotech Select Index`; rules-based developed-market pharma/biotech index with thematic exposure criteria
- Gross expense ratio: `0.13%`; official page's Fund Details row incorrectly displays ticker `PBEU`, but page title, URL, performance rows, holdings account, and SEC summary prospectus identify this fund as `PBPH`; the conflict is preserved rather than silently normalized
- Official current performance as of `2026-07-31`: NAV `1 month 0.11%`, `3 month 8.55%`, `6 month 4.02%`, `YTD 7.69%`, and since inception cumulative `8.74%`; market-price equivalents are `0.05%`, `8.55%`, `4.02%`, `7.71%`, and `8.86%`
- Current official fund snapshot: the latest reviewed official page capture as of `2026-08-27` reports net assets about `US$1.04B`, NAV `US$29.00`, closing price `US$29.05`, shares outstanding `35.8M`, premium/discount `0.16%`, and median 30-day spread `0.11%`; this dynamic quote conflicts with an older same-page `2026-08-26` capture and is not used in return calculations

| Period | PBPH NAV TR | PBPH market-price return |
|---|---:|---:|
| 1 month | 0.11% | 0.05% |
| 3 months | 8.55% | 8.55% |
| 6 months | 4.02% | 4.02% |
| 2026 YTD | 7.69% | 7.71% |
| Since inception cumulative | 8.74% | 8.86% |

No annual calendar table is presented because the fund had not completed a full
calendar year in the reviewed official prospectus and the latest official
performance page reports only available-period returns.

## Risk read-through

PBPH เป็นกองทุน thematic ที่กระจุกตัวใน healthcare/pharma/biotech มากกว่า
กองทุน global broad-market. Top holdings ณ 27 ส.ค. 2026 ได้แก่ Eli Lilly
`14.65%`, Johnson & Johnson `9.49%`, AbbVie `6.78%`, Merck `5.49%`, Amgen
`4.91%`, Roche `4.62%`, Novartis `4.18%`, Gilead `3.98%`, AstraZeneca `3.53%`
และ Pfizer `3.49%`; holdings ทั้งหมด `ไม่พบข้อมูลที่ยืนยันได้` ใน reviewed
official page เพราะเปิดเผยเฉพาะ top 10.

ความเสี่ยงหลักคือ pharma/biotech industry concentration, clinical/regulatory
outcomes, patent and pricing pressure, foreign securities, currency, index
methodology/data, tracking error, new-fund history, liquidity และ premium/
discount. Official daily NAV Total Return history ยังไม่ยาวพอและไม่ถูกเปิดเผย
เป็นชุดที่ใช้คำนวณ maximum drawdown, recovery duration, downside capture หรือ
risk-adjusted persistence ได้; ค่าเหล่านี้จึงเป็น `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Portfolio Building Block PBPH official product page](https://portfoliobuildingblocketfs.com/pbph/) — identity, BITA index objective, available-period NAV/market returns, inception, current fund data, top holdings and disclosed source-field conflict
- [PBPH summary prospectus](https://portfoliobuildingblocketfs.com/PBPH/summary-prospectus) — PBPH/Nasdaq identity, passive indexing, BITA methodology, 0.13% expenses and pharma/biotech, concentration, foreign-market, tracking and new-fund risks
- [SEC PBPH summary prospectus filing](https://www.sec.gov/Archives/edgar/data/2043390/000199937125018297/pbph_497k-112125.htm) — statutory identity, listing, objective, fee structure and passive strategy confirmation
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition; not used for a calendar CAGR because PBPH has no complete calendar year
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
