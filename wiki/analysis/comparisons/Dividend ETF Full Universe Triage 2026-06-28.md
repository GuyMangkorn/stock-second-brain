---
type: etf_full_universe_triage
created: 2026-06-28
source_file: raw/assets/ETF ที่เน้นการจ่ายเงินปันผล.md
universe_count: 100
sort_rule: verified dividend yield desc, then score desc
custom-width: 80
---

# Dividend ETF Full Universe Triage 2026-06-28
## Selected ETF Entities

[[ETF_AMEX_DGRO]] · [[ETF_AMEX_VIG]] · [[ETF_NASDAQ_VIGI]]

## Scope

ต่อจาก `Dividend ETF Triage 2026-06-28` รอบแรกที่ทำเฉพาะ 10 ตัวแรกตาม AUM. Memo นี้ parse ETF ทั้ง `100` rows จากไฟล์ local `raw/assets/ETF ที่เน้นการจ่ายเงินปันผล.md` และใช้ `Exchange:Ticker` เป็น key เพราะมี ticker ซ้ำข้ามตลาด เช่น `TDIV` และ `WDIV`.

Grouped companion note: `Dividend ETF Overlap Groups 2026-06-28` จัดครบทั้ง `100` ETF เป็นกลุ่ม exposure/holdings ที่ใกล้เคียงกันเพื่อช่วยลดการซื้อ ETF ซ้ำซ้อนในสินทรัพย์หรือ factor เดียวกัน. คะแนน `Score` ยังถูกยกติดไปด้วย แต่ไม่ได้ใช้เป็น sort หลักใน grouped view.

Original ranking below ยังเก็บ logic เดิมไว้เพื่อ traceability: กองที่หา dividend yield ได้จะเรียงจาก yield สูงไปต่ำก่อน; กองที่ยังหา dividend yield ไม่ได้จะเรียงด้วย `Score /10` ต่อ. `DVY` ถูก manual-adjust เป็น 5.8 เพราะ prior source-deepening พบ high-yield / utilities sensitivity สูงกว่า heuristic raw score. Dividend ที่ไม่ได้ verify จะเขียน `ไม่พบข้อมูลที่ยืนยันได้` แทน ไม่เดา.

Macro backdrop ณ 2026-06-28: Fed เพิ่งประชุม 2026-06-16 ถึง 2026-06-17 และ market commentary ล่าสุดตีความ tone เป็น hawkish / higher-for-longer. Scoring จึงให้ premium กับ low-cost, diversified, dividend growth / quality และ penalize high-yield trap, REIT/property, MLP/energy, financial-only, single-country concentration, high fee, และกองที่เล็ก/complex มากเกินไป.

## Scoring Method

- Base inputs from local TradingView clipping: AUM, 3Y NAV total return, expense ratio, asset class, focus.
- Quality adjustment: dividend growth / quality > broad dividend equity > high-yield-only.
- Macro adjustment: Fed hawkish penalizes REIT/property, MLP/energy, bank-only/financial-only, high-yield concentration, high expenses, and country/FX concentration.
- `Score` เป็น triage score ไม่ใช่ target allocation; ก่อนซื้อจริงต้อง refresh issuer holdings/factsheet ในวัน order.

## Grouped Overlap View

- Grouped memo: `wiki/analysis/comparisons/Dividend ETF Overlap Groups 2026-06-28.md`
- Coverage verification: source universe `100`, assigned `100`, unknown group `0`, duplicate assignment `0`.
- Use grouped view เป็นหน้าหลักสำหรับหลีกเลี่ยง ETF overlap; ใช้ original ranking below เป็น audit trail ของ yield/score เดิม.

## Source-Deepened Top Read

| ETF | Verified dividend / yield | Source | Top-10 theme read | Example holdings / names | Score | Action Read |
| --- | ---: | --- | --- | --- | ---: | --- |
| `AMEX:SPYD` | 4.40% | Kiplinger high-yield ETF screen, May 2026 | high-yield equities, financials, utilities, energy, staples | S&P 500 high-yield names across staples, financials, REITs, utilities, energy | 6.5 | Satellite / tactical |
| `CBOE:IDV` | 4.36% | iShares official, 12m trailing yield as of 2026-05-31 | high-yield equities, financials, utilities, energy, staples | international financials, energy, utilities, telecom; exact names need current iShares CSV | 5.9 | Satellite / tactical |
| `NASDAQ:VYMI` | 4.20% | Barron's / Morningstar screen, 2025 | high-yield equities, financials, utilities, energy, staples | Nestle/Roche/Novartis-type Swiss defensives, Toyota-type Japan cyclicals, European/Canadian banks | 6.4 | Satellite / tactical |
| `AMEX:DEM` | 4.10% | Kiplinger diversified dividend ETF screen, May 2026 | high-yield equities, financials, utilities, energy, staples | China Construction Bank plus Taiwan/Brazil/EM high dividend names | 4.8 | Avoid unless mandate |
| `AMEX:DHS` | 3.59% | Kiplinger monthly dividend ETF screen, May 2026 | high-yield equities, financials, utilities, energy, staples | U.S. high-dividend financials, staples, health care; lower technology weight | 5.9 | Satellite / tactical |
| `AMEX:FDVV` | 3.20% | Barron's / Morningstar screen, 2025 | high-yield equities, financials, utilities, energy, staples | Nvidia, JPMorgan Chase, Coca-Cola, Broadcom, Visa / Exxon Mobil-type names | 7.1 | Income sleeve / watch |
| `AMEX:DES` | 3.00% | Barron's / Morningstar screen, 2025 | small-cap value, industrials, financials, consumer cyclicals | U.S. small-cap dividend payers; exact names need WisdomTree CSV | 6.2 | Satellite / tactical |
| `AMEX:SDY` | 2.50% | Kiplinger dividend growth ETF screen, May 2026 | broad dividend payers across financials, tech, health care, staples, industrials | Dividend Aristocrats across industrials, staples, utilities, financials, health care | 6.4 | Satellite / tactical |
| `AMEX:VYM` | 2.40% | Kiplinger high-yield ETF screen, May 2026 | high-yield equities, financials, utilities, energy, staples | Broadcom, JPMorgan Chase, Exxon Mobil, Procter & Gamble, Johnson & Johnson | 7.3 | Income sleeve / watch |
| `AMEX:DON` | 2.40% | Barron's / Morningstar screen, 2025 | mid-cap value, industrials, financials, consumer/health care | U.S. mid-cap dividend payers; exact names need WisdomTree CSV | 6.2 | Satellite / tactical |
| `NASDAQ:VIGI` | 2.20% | Kiplinger diversified dividend ETF screen, May 2026 | dividend growers, quality large caps, staples/industrials/health care | Nestle, SAP, Novartis, Royal Bank of Canada, Novo Nordisk | 7.7 | Core candidate |
| `CBOE:NOBL` | 2.12% | ProShares official, 12-month yield as of 2026-05-31 | dividend growers, quality large caps, staples/industrials/health care | West Pharmaceutical Services, Hormel Foods, Caterpillar, AbbVie, J.M. Smucker | 6.9 | Income sleeve / watch |
| `AMEX:DTD` | 1.98% | Kiplinger monthly dividend ETF screen, May 2026 | broad dividend payers across financials, tech, health care, staples, industrials | Nvidia, JPMorgan Chase, Microsoft, Apple, Alphabet, Broadcom | 7.0 | Income sleeve / watch |
| `AMEX:DGRO` | 1.96% | iShares official, 12m trailing yield as of 2026-05-31 | broad dividend payers across financials, tech, health care, staples, industrials | Microsoft, Apple, JPMorgan Chase, Exxon Mobil, Johnson & Johnson / Procter & Gamble-type names | 8.1 | Core candidate |
| `AMEX:DLN` | 1.90% | Kiplinger monthly dividend ETF screen, May 2026 | large-cap dividend payers, financials, tech, health care, staples | Nvidia, JPMorgan Chase, Microsoft, Apple, Alphabet / Broadcom-type large dividend payers | 7.0 | Income sleeve / watch |
| `AMEX:VIG` | 1.70% | Kiplinger dividend growth ETF screen, May 2026 | dividend growers, quality large caps, staples/industrials/health care | Broadcom, Microsoft, Apple, Eli Lilly, JPMorgan Chase | 8.2 | Core candidate |

## Full Universe Ranking

| Sort | ETF | Fund | Region | Theme | Top-10 theme read | Dividend / yield | Score | Action Read |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | --- |
| 1 | `AMEX:SPYD` | State Street SPDR Portfolio S&P 500 High Dividend ETF | U.S. | High dividend yield | high-yield equities, financials, utilities, energy, staples | 4.40% | 6.5 | Satellite / tactical only |
| 2 | `CBOE:IDV` | iShares International Select Dividend ETF | International / global | High dividend yield | high-yield equities, financials, utilities, energy, staples | 4.36% | 5.9 | Satellite / tactical only |
| 3 | `NASDAQ:VYMI` | Vanguard International High Dividend Yield ETF | International / global | High dividend yield | high-yield equities, financials, utilities, energy, staples | 4.20% | 6.4 | Satellite / tactical only |
| 4 | `AMEX:DEM` | WisdomTree Emerging Markets High Dividend Fund | International / global | High dividend yield | high-yield equities, financials, utilities, energy, staples | 4.10% | 4.8 | Avoid / mandate-only |
| 5 | `AMEX:DHS` | WisdomTree U.S. High Dividend Fund | U.S. | High dividend yield | high-yield equities, financials, utilities, energy, staples | 3.59% | 5.9 | Satellite / tactical only |
| 6 | `AMEX:FDVV` | Fidelity High Dividend ETF | U.S. | High dividend yield | high-yield equities, financials, utilities, energy, staples | 3.20% | 7.1 | Income sleeve / watch |
| 7 | `AMEX:DES` | WisdomTree U.S. SmallCap Dividend Fund | U.S. | Small-cap dividend | small-cap value, industrials, financials, consumer cyclicals | 3.00% | 6.2 | Satellite / tactical only |
| 8 | `AMEX:SDY` | State Street SPDR S&P Dividend ETF | U.S. | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | 2.50% | 6.4 | Satellite / tactical only |
| 9 | `AMEX:VYM` | Vanguard High Dividend Yield Index ETF | U.S. | High dividend yield | high-yield equities, financials, utilities, energy, staples | 2.40% | 7.3 | Income sleeve / watch |
| 10 | `AMEX:DON` | WisdomTree U.S. MidCap Dividend Fund | U.S. | Mid-cap dividend | mid-cap value, industrials, financials, consumer/health care | 2.40% | 6.2 | Satellite / tactical only |
| 11 | `NASDAQ:VIGI` | Vanguard International Dividend Appreciation ETF | International / global | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | 2.20% | 7.7 | Core candidate |
| 12 | `CBOE:NOBL` | ProShares S&P 500 Dividend Aristocrats ETF | U.S. | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | 2.12% | 6.9 | Income sleeve / watch |
| 13 | `AMEX:DTD` | WisdomTree U.S. Total Dividend Fund | U.S. | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | 1.98% | 7.0 | Income sleeve / watch |
| 14 | `AMEX:DGRO` | iShares Core Dividend Growth ETF | U.S. | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | 1.96% | 8.1 | Core candidate |
| 15 | `AMEX:DLN` | WisdomTree U.S. LargeCap Dividend Fund | U.S. | Large-cap dividend | large-cap dividend payers, financials, tech, health care, staples | 1.90% | 7.0 | Income sleeve / watch |
| 16 | `AMEX:VIG` | Vanguard Dividend Appreciation ETF | U.S. | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | 1.70% | 8.2 | Core candidate |
| 17 | `AMEX:DIVI` | Franklin International Core Dividend Tilt Index Fund | International / global | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 7.9 | Core candidate |
| 18 | `SIX:CHDVD` | iShares Swiss Dividend ETF (CH) | Europe-listed UCITS / global or regional | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 7.6 | Income sleeve / watch |
| 19 | `AMEX:DJD` | Invesco Dow Jones Industrial Average Dividend ETF | U.S. | Large-cap dividend | large-cap dividend payers, financials, tech, health care, staples | ไม่พบข้อมูลที่ยืนยันได้ | 7.5 | Income sleeve / watch |
| 20 | `TSX:VGG` | Vanguard US Dividend Appreciation Index ETF | Canada-listed / Canada or U.S.-tilt | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 7.5 | Income sleeve / watch |
| 21 | `TSX:VDY` | Vanguard FTSE Canadian High Dividend Yield Index ETF | Canada-listed / Canada or U.S.-tilt | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 7.3 | Income sleeve / watch |
| 22 | `AMEX:SDOG` | ALPS Sector Dividend Dogs ETF | U.S. | Large-cap dividend | large-cap dividend payers, financials, tech, health care, staples | ไม่พบข้อมูลที่ยืนยันได้ | 7.2 | Income sleeve / watch |
| 23 | `NASDAQ:PEY` | Invesco High Yield Equity Dividend Achievers ETF | U.S. | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 7.2 | Income sleeve / watch |
| 24 | `XETR:SPYW` | State Street SPDR S&P Euro Dividend Aristocrats UCITS ETF EUR | Europe-listed UCITS / global or regional | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 7.2 | Income sleeve / watch |
| 25 | `EURONEXT:TDIV` | VanEck Vectors ETFs NV - Morningstar Dev. Mrkts. Div. Ldrs. | Europe-listed UCITS / global or regional | Large-cap dividend | large-cap dividend payers, financials, tech, health care, staples | ไม่พบข้อมูลที่ยืนยันได้ | 7.1 | Income sleeve / watch |
| 26 | `CBOE:DDWM` | WisdomTree Dynamic International Equity Fund | International / global | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 6.9 | Income sleeve / watch |
| 27 | `LSE:IUKD` | iShares UK Dividend UCITS ETF GBP | Europe-listed UCITS / global or regional | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 6.9 | Income sleeve / watch |
| 28 | `TSX:XEI` | iShares S&P/TSX Composite High Dividend Index ETF | Canada-listed / Canada or U.S.-tilt | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.8 | Income sleeve / watch |
| 29 | `ASX:VHY` | Vanguard Australian Shares High Yield ETF | Australia-listed / Australia or global | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.6 | Satellite / tactical only |
| 30 | `NASDAQ:TDIV` | First Trust NASDAQ Technology Dividend Index Fund | U.S. | Technology dividend | mature tech, semis, hardware/software cash return names | ไม่พบข้อมูลที่ยืนยันได้ | 6.6 | Satellite / tactical only |
| 31 | `NASDAQ:PFM` | Invesco Dividend Achievers ETF | U.S. | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 6.5 | Satellite / tactical only |
| 32 | `XETR:ZPRG` | SSGA SPDR ETFs Europe I PLC - State Street SPDR S&P Global Dividend Aristocrats UCITS ETF Ptg USD | Europe-listed UCITS / global or regional | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 6.5 | Satellite / tactical only |
| 33 | `TSX:VGH` | Vanguard US Dividend Appreciation Index ETF (CAD-hedged) | Canada-listed / Canada or U.S.-tilt | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 6.4 | Satellite / tactical only |
| 34 | `AMEX:FVD` | First Trust Value Line Dividend Index Fund | U.S. | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 35 | `ASX:IHD` | iShares S&P/ASX Dividend Opportunities ETF | Australia-listed / Australia or global | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 36 | `KRX:161510` | Hanwha PLUS High Dividend ETF | Korea-listed / Korea or U.S.-tilt | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 37 | `XETR:EXSH` | iShares STOXX Europe Select Dividend 30 UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.3 | Satellite / tactical only |
| 38 | `AMEX:WDIV` | State Street SPDR S&P Global Dividend ETF | International / global | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 39 | `CBOE:REGL` | ProShares S&P MidCap 400 Dividend Aristocrats ETF | U.S. | Mid-cap dividend | mid-cap value, industrials, financials, consumer/health care | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 40 | `TSX:VIDY` | Vanguard FTSE Developed ex North America High Dividend Yield | Canada-listed / Canada or U.S.-tilt | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 41 | `XETR:DXSA` | Xtrackers Euro Stoxx Quality Dividend UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 42 | `XETR:QDVD` | iShares MSCI USA Quality Dividend ESG UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 6.2 | Satellite / tactical only |
| 43 | `TSE:1489` | Next Funds Nikkei 225 High Dividend Yield Stock 50 Index ETF | Japan | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.1 | Satellite / tactical only |
| 44 | `TSE:1577` | NEXT FUNDS Nomura Japan Equity High Dividend 70 Exchange Traded Fund | Japan | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.1 | Satellite / tactical only |
| 45 | `LSE:VHYA` | Vanguard Funds PLC - Vanguard FTSE All-World High Dividend Yield UCITS ETF AccumUSD | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 6.0 | Satellite / tactical only |
| 46 | `NASDAQ:PID` | Invesco International Dividend Achievers ETF | International / global | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 5.9 | Satellite / tactical only |
| 47 | `XETR:ISPA` | iShares STOXX Global Select Dividend 100 UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.9 | Satellite / tactical only |
| 48 | `AMEX:QDPL` | Pacer Metaurus US Large Cap Dividend Multiplier 400 ETF | U.S. | Large-cap dividend | large-cap dividend payers, financials, tech, health care, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 49 | `NASDAQ:DVY` | iShares Select Dividend ETF | U.S. | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 50 | `TSX:PDC` | Invesco Canadian Dividend Index ETF | Canada-listed / Canada or U.S.-tilt | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 51 | `XETR:ELFC` | Deka EURO iSTOXX ex Fin Dividend+ UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.8 | Satellite / tactical only |
| 52 | `ASX:WDIV` | State Street SPDR S&P Global Dividend ETF | Australia-listed / Australia or global | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.7 | Avoid / mandate-only |
| 53 | `XETR:EXSB` | iShares DivDAX UCITS ETF (DE) | Europe-listed UCITS / global or regional | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.7 | Avoid / mandate-only |
| 54 | `AMEX:DWM` | WisdomTree International Equity Fund | International / global | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 55 | `CBOE:TDV` | ProShares S&P Technology Dividend Aristocrats ETF | U.S. | Technology dividend | mature tech, semis, hardware/software cash return names | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 56 | `EURONEXT:SEL` | Amundi STOXX Europe Select Dividend 30 - UCITS ETF Dist | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 57 | `KRX:315960` | KB RISE Large Cap High Dividend10TR ETF | Korea-listed / Korea or U.S.-tilt | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 58 | `TSX:CDZ` | iShares S&P/TSX Canadian Dividend Aristocrats Index ETF | Canada-listed / Canada or U.S.-tilt | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 5.6 | Avoid / mandate-only |
| 59 | `CBOE:SMDV` | ProShares Russell 2000 Dividend Growers ETF | U.S. | Small-cap dividend | small-cap value, industrials, financials, consumer cyclicals | ไม่พบข้อมูลที่ยืนยันได้ | 5.5 | Avoid / mandate-only |
| 60 | `AMEX:DLS` | WisdomTree International SmallCap Dividend Fund | International / global | Small-cap dividend | small-cap value, industrials, financials, consumer cyclicals | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 61 | `AMEX:ENFR` | Alerian Energy Infrastructure ETF | U.S. | Energy / MLP infrastructure | pipelines, midstream, energy infrastructure | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 62 | `ASX:SYI` | State Street SPDR MSCI Australia Select High Dividend Yield ETF | Australia-listed / Australia or global | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 63 | `TWSE:00918` | United Taiwan High Dividend Recovery 30 ETF | Taiwan | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 64 | `XETR:XGSD` | Xtrackers STOXX GLOBAL SELECT DIVIDEND 100 SWAP UCITS ETF Distribution 1D | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.4 | Avoid / mandate-only |
| 65 | `AMEX:IDOG` | ALPS International Sector Dividend Dogs ETF | International / global | Large-cap dividend | large-cap dividend payers, financials, tech, health care, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 66 | `TWSE:00919` | Capital TIP Customized Taiwan Select High Dividend ETF | Taiwan | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 67 | `XETR:EL4G` | Deka EURO STOXX Select Dividend 30 UCITS ETF | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 68 | `XETR:EXSG` | iShares Euro Stoxx Select Dividend 30 UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 69 | `XETR:EXXW` | iShares Dow Jones Asia Pacific Select Dividend 30 UCITS ETF | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.3 | Avoid / mandate-only |
| 70 | `AMEX:AMLP` | Alerian MLP ETF | U.S. | Energy / MLP infrastructure | pipelines, midstream, energy infrastructure | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |
| 71 | `AMEX:DWX` | State Street SPDR S&P International Dividend ETF | International / global | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |
| 72 | `NASDAQ:MDIV` | Multi-Asset Diversified Income Index Fund | U.S. | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |
| 73 | `TSX:FCCD` | Fidelity Canadian High Dividend ETF Trust Units Series L | Canada-listed / Canada or U.S.-tilt | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |
| 74 | `XETR:ZPRA` | SSGA SPDR ETFs Europe I PLC - State Street SPDR S&P Pan Asia Dividend Aristocrats UCITS ETF Ptg USD | Europe-listed UCITS / global or regional | Dividend growth / quality | dividend growers, quality large caps, staples/industrials/health care | ไม่พบข้อมูลที่ยืนยันได้ | 5.2 | Avoid / mandate-only |
| 75 | `AMEX:DGS` | WisdomTree Emerging Markets SmallCap Dividend Fund | International / global | Small-cap dividend | small-cap value, industrials, financials, consumer cyclicals | ไม่พบข้อมูลที่ยืนยันได้ | 5.0 | Avoid / mandate-only |
| 76 | `AMEX:FDD` | First Trust Stoxx European Select Dividend Index Fund | International / global | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 5.0 | Avoid / mandate-only |
| 77 | `KRX:402970` | KIM ACE S&P US Dividend 100 ETF | Korea-listed / Korea or U.S.-tilt | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 5.0 | Avoid / mandate-only |
| 78 | `TSX:RBNK` | RBC Canadian Bank Yield Index ETF | Canada-listed / Canada or U.S.-tilt | Financials / bank dividend | banks, insurers, lenders, financial income stocks | ไม่พบข้อมูลที่ยืนยันได้ | 4.9 | Avoid / mandate-only |
| 79 | `TSX:TBNK` | TD Canadian Bank Dividend Index ETF | Canada-listed / Canada or U.S.-tilt | Financials / bank dividend | banks, insurers, lenders, financial income stocks | ไม่พบข้อมูลที่ยืนยันได้ | 4.9 | Avoid / mandate-only |
| 80 | `XETR:EXX5` | iShares Dow Jones U.S. Select Dividend UCITS ETF (DE) | Europe-listed UCITS / global or regional | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 4.9 | Avoid / mandate-only |
| 81 | `TSE:1698` | Listed Index Fund Japan High Dividend (TSE Dividend Focus 100) | Japan | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 4.8 | Avoid / mandate-only |
| 82 | `AMEX:DFJ` | WisdomTree Japan SmallCap Dividend Fund | International / global | Small-cap dividend | small-cap value, industrials, financials, consumer cyclicals | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |
| 83 | `AMEX:DTH` | WisdomTree International High Dividend Fund | International / global | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |
| 84 | `ASX:RDV` | Russell Investments High Dividend Australian Shares ETF | Australia-listed / Australia or global | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |
| 85 | `CBOE:DDLS` | WisdomTree Dynamic International SmallCap Equity Fund | International / global | Small-cap dividend | small-cap value, industrials, financials, consumer cyclicals | ไม่พบข้อมูลที่ยืนยันได้ | 4.7 | Avoid / mandate-only |
| 86 | `KRX:466940` | MIRAE ASSET TIGER Bank High Dividend Plus TOP 10 Fn ETF Units | Korea-listed / Korea or U.S.-tilt | Financials / bank dividend | banks, insurers, lenders, financial income stocks | ไม่พบข้อมูลที่ยืนยันได้ | 4.4 | Avoid / mandate-only |
| 87 | `XETR:EL4X` | Deka DAXplus Maximum Dividend UCITS ETF | Europe-listed UCITS / global or regional | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 4.3 | Avoid / mandate-only |
| 88 | `AMEX:SDIV` | Global X Superdividend ETF | International / global | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 4.2 | Avoid / mandate-only |
| 89 | `SZSE:159691` | ICBCCS CSI Hong Kong Connect High Dividend Yield Select ETF Units | SZSE | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 4.2 | Avoid / mandate-only |
| 90 | `NASDAQ:KBWY` | Invesco KBW Premium Yield Equity REIT ETF | U.S. | REIT / property income | REIT/property income; rate-sensitive | ไม่พบข้อมูลที่ยืนยันได้ | 4.0 | Avoid / mandate-only |
| 91 | `TSX:FCID` | Fidelity International High Dividend ETF Trust Units Series L | Canada-listed / Canada or U.S.-tilt | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 4.0 | Avoid / mandate-only |
| 92 | `KRX:489250` | SAMSUNG KODEX US Dividend Dow Jones ETF | Korea-listed / Korea or U.S.-tilt | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |
| 93 | `LSE:MLPD` | Invesco Morningstar US Energy Infrastructure MLP UCITS ETF | Europe-listed UCITS / global or regional | Energy / MLP infrastructure | pipelines, midstream, energy infrastructure | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |
| 94 | `SSE:513910` | SOEs Dividend Index Exchange Traded Fund Units | China / Hong Kong | Broad dividend equity | broad dividend payers across financials, tech, health care, staples, industrials | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |
| 95 | `TSE:1660` | MAXIS High Yield J-REIT ETF | Japan | REIT / property income | REIT/property income; rate-sensitive | ไม่พบข้อมูลที่ยืนยันได้ | 3.9 | Avoid / mandate-only |
| 96 | `SSE:513690` | Bosera Hang Seng High Dividend Yield ETF | China / Hong Kong | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 3.7 | Avoid / mandate-only |
| 97 | `TSE:2564` | Global X MSCI SuperDividend Japan ETF | Japan | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 3.7 | Avoid / mandate-only |
| 98 | `HKEX:3110` | Global X Hang Seng High Dividend Yield ETF | China / Hong Kong | High dividend yield | high-yield equities, financials, utilities, energy, staples | ไม่พบข้อมูลที่ยืนยันได้ | 3.5 | Avoid / mandate-only |
| 99 | `LSE:DPYA` | iShares Developed Markets Property Yield UCITS ETF | Europe-listed UCITS / global or regional | REIT / property income | REIT/property income; rate-sensitive | ไม่พบข้อมูลที่ยืนยันได้ | 3.5 | Avoid / mandate-only |
| 100 | `NASDAQ:KBWD` | Invesco KBW High Dividend Yield Financial ETF | U.S. | Financials / bank dividend | banks, insurers, lenders, financial income stocks | ไม่พบข้อมูลที่ยืนยันได้ | 2.0 | Avoid / mandate-only |

## Top 10 By Score If Dividend Is Ignored

| Rank | ETF | Score | Why |
| ---: | --- | ---: | --- |
| 1 | `AMEX:VIG` | 8.2 | Dividend growth / quality; U.S.; source row from full universe |
| 2 | `AMEX:DGRO` | 8.1 | Broad dividend equity; U.S.; source row from full universe |
| 3 | `AMEX:DIVI` | 7.9 | Broad dividend equity; International / global; source row from full universe |
| 4 | `NASDAQ:VIGI` | 7.7 | Dividend growth / quality; International / global; source row from full universe |
| 5 | `SIX:CHDVD` | 7.6 | Broad dividend equity; Europe-listed UCITS / global or regional; source row from full universe |
| 6 | `AMEX:DJD` | 7.5 | Large-cap dividend; U.S.; source row from full universe |
| 7 | `TSX:VGG` | 7.5 | Dividend growth / quality; Canada-listed / Canada or U.S.-tilt; source row from full universe |
| 8 | `TSX:VDY` | 7.3 | High dividend yield; Canada-listed / Canada or U.S.-tilt; source row from full universe |
| 9 | `AMEX:VYM` | 7.3 | High dividend yield; U.S.; source row from full universe |
| 10 | `AMEX:SDOG` | 7.2 | Large-cap dividend; U.S.; source row from full universe |

## Practical Shortlist

- `AMEX:VIG`, `AMEX:DGRO`, `NASDAQ:VIGI`: กลุ่มที่เหมาะสุดสำหรับ long-term core/quality dividend ใน Fed hawkish เพราะไม่ไล่ yield สูงสุดและ fee ต่ำ.
- `AMEX:VYM`, `AMEX:FDVV`, `AMEX:DLN`, `AMEX:DTD`: ใช้เป็น income sleeve ได้ แต่ต้องรับ value/financial/sector tilt มากกว่า dividend growth core.
- `AMEX:SPYD`, `CBOE:IDV`, `AMEX:DHS`, `NASDAQ:VYMI`, `AMEX:DEM`: yield สูงกว่า แต่เป็น satellite/tactical มากกว่า core เพราะมี sector, FX, country, หรือ high-yield concentration risk.
- REIT/property, MLP/energy, bank-only, และกอง expense สูงมาก เช่น `NASDAQ:KBWD` ควรเป็น mandate-only ในสภาพแวดล้อม Fed hawkish.

## Source Map

- Local source universe: `raw/assets/ETF ที่เน้นการจ่ายเงินปันผล.md`, captured from TradingView dividend ETF screen: `https://th.tradingview.com/markets/etfs/funds-dividend/`
- Prior memo: `wiki/analysis/comparisons/Dividend ETF Triage 2026-06-28.md`
- Federal Reserve FOMC calendar / June 2026 meeting materials: `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm`
- Kiplinger interest-rate outlook, 2026-06-25: `https://www.kiplinger.com/economic-forecasts/interest-rates`
- Kiplinger dividend growth ETF screen, May 2026: `https://www.kiplinger.com/investing/etfs/dividend-growth-etfs`
- Kiplinger high-yield ETF screen, May 2026: `https://www.kiplinger.com/investing/etfs/602375/high-yield-etfs-for-income-investors`
- Kiplinger monthly dividend ETF screen, May 2026: `https://www.kiplinger.com/investing/etfs/best-monthly-dividend-etfs`
- Kiplinger diversified dividend ETF screen, May 2026: `https://www.kiplinger.com/investing/etfs/603435/best-dividend-etfs-to-buy-for-a-diversified-portfolio`
- Barron's / Morningstar dividend ETF yield screen, 2025: `https://www.barrons.com/articles/stock-dividend-etfs-yields-77435efd`
- iShares DGRO official page: `https://www.ishares.com/us/products/264623/ishares-core-dividend-growth-etf`
- iShares IDV official page: `https://www.ishares.com/us/products/239499/ishares-international-select-dividend-etf`
- ProShares NOBL official page: `https://www.proshares.com/our-etfs/strategic/nobl`
- Vanguard VIG official profile: `https://investor.vanguard.com/investment-products/etfs/profile/vig`
- Vanguard VYM official profile: `https://investor.vanguard.com/investment-products/etfs/profile/vym`
- Vanguard VIGI official profile: `https://investor.vanguard.com/investment-products/etfs/profile/vigi`
- Vanguard VYMI official profile: `https://investor.vanguard.com/investment-products/etfs/profile/vymi`

## Caveats / Follow-Up

- `Dividend / yield` ในตารางไม่ใช่ค่าเดียวกันทุกแหล่ง: บางตัวเป็น 30-day SEC yield, บางตัวเป็น trailing 12-month yield. ใช้เพื่อ triage เท่านั้น ไม่ควรเทียบแบบ precise allocation โดยไม่ refresh factsheet.
- `Top-10 theme read` ของกองที่ไม่ได้ source-deepen เป็น inference จาก fund name/focus/region ไม่ใช่ verified holdings list; จึงใส่ example holdings เป็น `ไม่พบข้อมูลที่ยืนยันได้`.
- ก่อนซื้อจริงควรโหลด current holdings CSV/factsheet จาก issuer สำหรับ shortlist 5-10 ตัวสุดท้าย แล้วเช็ค distribution history, withholding tax, liquidity, bid-ask spread, และ broker availability.
