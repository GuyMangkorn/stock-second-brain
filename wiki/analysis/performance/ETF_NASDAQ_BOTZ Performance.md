---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:BOTZ
ticker: BOTZ
exchange: Nasdaq
fund: Global X Robotics & Artificial Intelligence ETF
tracked_index: Indxx Global Robotics & Artificial Intelligence Thematic Index
benchmark: Indxx Global Robotics & Artificial Intelligence Thematic Index
updated: 2026-09-01
performance_as_of: 2026-07-31
annual_rows_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/BOTZ
  - geography/International
---

# BOTZ Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

BOTZ เป็น passive thematic global equity ETF ที่ลงทุนใน robotics, automation, autonomous vehicles และ AI. Official factsheet ล่าสุด ณ 2026-07-31 รายงาน NAV TR YTD `-1.53%`, 1-year `6.64%`, 3-year annualised `7.22%`, 5-year annualised `1.26%` และ since inception annualised `9.72%`; NAV ณ 2026-08-31 คือ USD `36.07` และ market price คือ USD `35.89`. Annual complete row ที่ยืนยันได้จาก current SEC prospectus คือ 2025 NAV TR `13.71%`, ต่ำกว่า S&P 500 TR `17.88%` และ index `13.98%`. จึงไม่ backfill annual history 2016-2024 จาก price-only series หรือ secondary data.

## Performance check

- entity_key: NASDAQ:BOTZ
- Fund: Global X Robotics & Artificial Intelligence ETF
- Classification: passive index-tracking thematic equity ETF; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified
- Inception: 2016-09-12; total expense ratio: 0.68%; primary exchange: Nasdaq; holdings: 61 as of 2026-08-31
- Tracked index: Indxx Global Robotics & Artificial Intelligence Thematic Index (`IBOTZNT`)
- Return basis: total return with gross income reinvested where applicable; NAV and market-price returns are kept separate
- Current official snapshot as of 2026-08-31: NAV USD 36.07, market price USD 35.89, net assets USD 3.44 billion, and 30-day SEC yield -0.06%
- Official factsheet performance as of 2026-07-31: NAV YTD -1.53%, 1-year 6.64%, 3-year annualised 7.22%, 5-year annualised 1.26%, since inception annualised 9.72%; index values are -1.28%, 7.09%, 7.65%, 1.69%, and 10.13% respectively
- 2025: NAV TR 13.71%; index 13.98%; implementation gap -0.27 percentage points; S&P 500 TR reference 17.88%
- Common benchmark: S&P 500 Total Return in USD with dividends reinvested; cached reference as of 2025-12-31 and used only as a broad reference

### Annual NAV TR

| Calendar year | BOTZ NAV TR | Indxx index | S&P 500 TR |
|---|---:|---:|---:|
| 2025 | 13.71% | 13.98% | 17.88% |

The current official SEC prospectus identifies the row as a calendar-year NAV return. Complete official 2016-2024 rows were not established in the retrieved current packet and remain `not disclosed`; no partial year is ranked.

## Up years / Down years

- Up years: 1; down years: 0 among verified complete annual rows
- Best year: 2025, +13.71% (only verified complete annual row)
- Historical worst-year ranking: not disclosed because the verified annual history is incomplete
- 2026 YTD is partial and excluded from annual ranking

## Risk read-through

BOTZ มี thematic concentration สูง: official exposure ณ 2026-07-31 อยู่ที่ Industrials `45.2%`, Information Technology `37.1%`, Health Care `8.1%`, และ country exposureหลักคือ United States `32.13%`, Japan `31.43%`, China `18.52%`, Switzerland `10.05%`. Official risk stats ณ 2026-07-31 รายงาน standard deviation `22.40%`, beta เทียบ S&P 500 `1.68`, Nasdaq-100 `1.12` และ MSCI EAFE `1.28`; factsheet ระบุ fund เป็น non-diversified. ความเสี่ยงหลักคือ valuation/technology cycle, rapid obsolescence, competition, international currency/geopolitical exposure, country concentration และ index/tracking risk. Daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น `not disclosed`.

## Sources

- [Official Global X BOTZ product page](https://www.globalxetfs.com/funds/botz)
- [Official BOTZ factsheet](https://assets.globalxetfs.com/funds/documents/botz/Fact-Sheet_BOTZ.pdf)
- [Official current SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1432353/000143235326000461/a497kroboticsartificialint.htm)
- Source batch: [[ETF_performance_sources_2026-09-01_run-5]]
