# Data Contract (Daily Bars)

## Universe (Sprint 1)
Example tickers: AAPL, MSFT, AMZN, GOOGL, KO, PEP, JPM, XOM, NVDA
Start date: 2018-01-01
Frequency: 1d (daily)

## Required Columns & Types
- ts: timestamp, UTC, ISO8601 (e.g., 2020-03-15T00:00:00Z)
- symbol: string (ticker)
- open: float
- high: float
- low: float
- close: float
- volume: float or int

## Primary Key
- (ts, symbol) must be unique

## File Format & Layout
- Parquet file: `data/bars_1d.parquet`
- One file for Sprint 1 (partitioning optional later)

## Time Zone
- All timestamps stored as UTC

## Missing Data Rules
- If a symbol is missing on a date, we keep the others
- No row with all OHLCV null is allowed

## Quality Checks (run after ingest)
1) Row count > 0
2) Unique (ts, symbol) — no duplicates
3) For each symbol: `ts` strictly increasing (no time travel)
4) `close` has no impossible values (e.g., negative)
5) Date range covers at least [start_date, latest_date_expected]

## Pass/Fail Examples
- **Pass:** 9 symbols × ~252 days/year × N years, no duplicate keys, UTC timestamps.
- **Fail:** duplicated (ts, symbol), mixed time zones, all-null OHLCV rows.
s