---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:CEUU
input_ticker: ISVYF
ticker: CEUU
exchange: Euronext Amsterdam
fund: iShares Core MSCI EMU UCITS ETF USD Hedged (Accumulating)
tracked_index: MSCI EMU Net Index (EUR)
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: not-applicable
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; income reinvested per issuer
return_currency: USD hedged share class; tracked benchmark is EUR
tags:
  - analysis/etf-performance
  - ticker/CEUU
  - ticker/ISVYF
  - geography/Europe
---

# CEUU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`ISVYF` เป็น OTC input alias ของ official USD Euronext Amsterdam line
`Euronext Amsterdam:CEUU` สำหรับ iShares Core MSCI EMU UCITS ETF USD Hedged
(Accumulating), ISIN `IE00BKBF6616`. กองทุนเป็น passive, physically replicated,
currency-hedged และ accumulating UCITS equity ETF ที่ติดตาม `MSCI EMU Net
Index (EUR)`. Share class เปิดตัว 5 มิ.ย. 2019 จึงยังไม่มี 10-year NAV TR
history; 2020-2025 NAV TR ที่ตรวจสอบได้ให้ cumulative `95.47%` / rounded-input
CAGR `11.82%`, ส่วน common 2021-2025 ให้ cumulative `95.00%` / CAGR `14.29%`.
เทียบ S&P 500 TR ใน common USD window ที่ `96.17%` / `14.43%` โดยไม่ใช้
MSCI EMU benchmark EUR เพื่อคำนวณ tracking gap กับ USD share class. ล่าสุด
official NAV TR YTD คือ `17.09%` ณ 13 ส.ค. 2026 และ NAV `US$12.99` ณ 14 ส.ค.
2026.

## Performance check

- `entity_key: Euronext Amsterdam:CEUU`; `input_ticker: ISVYF`. Official
  iShares listings map the USD line to `CEUU` on Euronext Amsterdam; the OTC
  symbol is retained only as an input alias. The target share-class ISIN is
  `IE00BKBF6616`.
- Classification: supported passive/index-tracking equity UCITS ETF; official
  materials describe physical replication, accumulating use of income, and a
  USD-hedged share class. Domicile Ireland; share-class launch 2019-06-05;
  ongoing charges `0.15%`.
- Tracked index: `MSCI EMU Net Index (EUR)`. The share class is USD hedged, but
  the issuer's displayed benchmark calendar rows remain EUR-based; those rows
  are kept separate from the USD NAV series.
- Return basis: issuer NAV total return with income reinvested and net of fund
  charges where shown. No 2016-2019 complete annual rows are available for this
  share class, and a 10-year CAGR is not applicable while the share class is
  under ten years old.
- Official current snapshot: NAV `US$12.99`, NAV TR YTD `17.09%`, share-class
  net assets `US$975.37M`, and 220 holdings; current fields are as of
  2026-08-14 or 2026-08-13 as labeled by the issuer.
- Official risk snapshot as of 2026-07-31: 3-year standard deviation `11.89%`
  and beta `1.005`. Sector weights as of 2026-08-14 were Financials `26.78%`,
  Industrials `20.26%`, Information Technology `15.93%`, Consumer
  Discretionary `7.78%`, Utilities `6.37%`, and Healthcare `5.54%`.
- Cash distribution: not applicable as a cash-income series for this
  accumulating share class; the official `Use of Income` field is
  `Accumulating`. No cash-distribution yield is inferred.

| Year | CEUU NAV TR (USD) | MSCI EMU Net (EUR) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2020 | 0.24% | -1.02% | 18.40% |
| 2021 | 23.88% | 22.16% | 28.71% |
| 2022 | -9.31% | -12.47% | -18.11% |
| 2023 | 22.15% | 18.78% | 26.29% |
| 2024 | 12.00% | 9.49% | 25.02% |
| 2025 | 26.87% | 23.70% | 17.88% |

The CEUU NAV rows are the USD share-class series. The MSCI EMU rows are the
issuer's EUR benchmark series and are shown for context only; no arithmetic
excess return or tracking gap is calculated across these different currency
bases.

## Up years / Down years

- Complete 2020-2025 NAV TR up/down: `5 / 1`
- Best NAV TR year: 2025, `+26.87%`
- Worst NAV TR year: 2022, `-9.31%`
- Common 2021-2025 NAV TR cumulative/CAGR: `95.00%` / `14.29%`
- Common 2021-2025 S&P 500 TR cumulative/CAGR: `96.17%` / `14.43%`
- Latest official NAV TR YTD: `+17.09%` ณ 13 ส.ค. 2026
- Issuer rolling 10-year NAV TR: not applicable because the share class launched
  2019-06-05.

## Risk read-through

CEUU gives diversified Eurozone equity exposure but remains concentrated in
Financials, Industrials and Information Technology. The currency-hedged USD
share class reduces direct EUR/USD exposure relative to an unhedged share class,
but hedge instruments introduce hedge-cost, counterparty and basis risks. The
tracked-index evidence is EUR while the share-class NAV return is USD, so
cross-currency benchmark comparisons need care. The official reviewed capture
does not disclose a daily NAV maximum drawdown or recovery date, and no
price-only proxy is substituted for that missing evidence.

## Sources

- [iShares Core MSCI EMU UCITS ETF product page](https://www.ishares.com/uk/professionals/en/products/309033/ishares-core-msci-emu-ucits-etf) — official CEUU listing, ISIN, NAV/YTD, share-class assets, holdings, fees, index and risk snapshot
- [iShares CEUU factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/ceuu-ishares-core-msci-emu-ucits-etf-fund-fact-sheet-en-gb.pdf) — official share-class structure, 2020-2025 calendar rows, benchmark rows and rolling return fields
- [iShares CEUU KIID](https://www.ishares.com/uk/individual/en/literature/kiid/kiid-ishares-core-msci-emu-ucits-etf-usd-hedged-acc-ie00bkbf6616-en.pdf) — official passive/index objective and share-class risk/structure context
- [Stock Analysis ISVYF quote](https://stockanalysis.com/quote/otc/ISVYF/) — OTC alias identity cross-check only; not used as primary NAV performance evidence
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
