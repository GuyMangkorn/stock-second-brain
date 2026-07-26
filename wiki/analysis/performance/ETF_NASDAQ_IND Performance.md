---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:IND
ticker: IND
exchange: Nasdaq
fund: Xtrackers Nifty 500 India ETF
tracked_index: Nifty 500 Index (N500USNT)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-03-31
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IND
  - geography/India
---

# IND Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

IND เป็น passive/index-tracking India equity ETF ที่เพิ่งเริ่มดำเนินงานในเดือนพฤศจิกายน 2025 จึงไม่มี 10-year NAV Total Return. Official DWS factsheet ที่ยืนยันได้ล่าสุด (Q1 2026) เปิดเผยเพียง 3-month NAV TR `-18.41%` ถึง `2026-03-31`; ไม่เปิดเผย inception-to-date NAV TR endpoints หรือ current NAV YTD ถึง `2026-07-26`. ตัวเลข 3-month นี้ไม่ถูก annualize และไม่ถูกเรียกว่า 2026 YTD.

## Performance check

- entity_key: `Nasdaq:IND`
- Fund: Xtrackers Nifty 500 India ETF
- Inception: `2025-11-24` ตาม official Q1 factsheet; DWS launch/Nasdaq listing and the first holdings report identify commencement/listing on `2025-11-25`
- Primary listing: Nasdaq
- Expense ratio: `0.19%` net/gross according to the reviewed prospectus/factsheet
- Tracked index: Nifty 500 Index (`N500USNT`), maintained by NSE Indices
- Metric: NAV Total Return including reinvested distributions and fund expenses
- 10-year NAV TR: unavailable; fund history is under 10 years
- Available official observation: 3-month NAV TR `-18.41%` for the official period ending `2026-03-31`; raw start/end TR values are not disclosed
- Available observation actual elapsed time: `2025-12-31` to `2026-03-31`, `90 days / 0.246412 years`
- Available-observation CAGR: not calculated; the issuer supplies a rounded short-period snapshot rather than inception-to-date endpoints, and annualizing it would overstate precision
- Current NAV TR YTD: not disclosed in the reviewed official capture through `2026-03-31`; the 3-month value is not relabelled as YTD

| Period | IND NAV TR | S&P 500 TR |
|---|---:|---:|
| Before 2025-11-24 | not applicable; fund had not launched | cached reference rows available separately |
| 2025 | not disclosed; incomplete inception year | 17.88% |
| 2026 Q1 / 3-month observation | -18.41% as of 2026-03-31 | not comparable to a current 2026 YTD figure |
| 2026 YTD | not disclosed | not comparable; current year is outside the cached complete-year window |

The S&P 500 rows used elsewhere in this vault are the cached USD Total Return convention for complete calendar years `2016-2025`; no S&P row is used to fill IND's missing inception-to-date or current-YTD data.

## Up years / Down years

- Up years / Down years: not disclosed; no complete IND calendar-year NAV TR table
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed

## Risk read-through

IND provides broad India exposure across large-, mid- and small-cap companies, with India country, INR/USD FX, emerging-market, liquidity, policy and sector-concentration risks. DWS reports 499 holdings and India exposure of 97.14% in the Q1 factsheet, but these are holdings data rather than performance inputs. The fund is new and its official performance history remains incomplete.

## Sources

- [DWS Xtrackers IND Q1 2026 factsheet](https://etf.dws.com/download/asset/048952ad-b7d4-462d-95c8-e726ff2484bd)
- [DWS launch release for IND](https://www.dws.com/en-us/about-us/media/media-releases/xtrackers-by-dws-launches-nifty-500-india-etf-nasdaq-ind/)
- [SEC/DBX ETF Trust prospectus and SAI](https://www.sec.gov/Archives/edgar/data/1503123/000008805325000603/dbxetf-20250531.htm)
- [Nasdaq IND listing alert](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETP2025-204)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
