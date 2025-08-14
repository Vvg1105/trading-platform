# Data Ingestion Runbook (Sprint 1)

## Universe
Tickers: AAPL, MSFT, AMZN, GOOGL, KO, PEP, JPM, XOM, NVDA, TSLA
Start date: 2018-01-01
Frequency: 1-day bars
Timezone: UTC

## Steps
1. Fetch data for each ticker from chosen API (yfinance for Sprint 1)
2. Merge all tickers into one dataframe
3. Save as data/bars_1d.parquet
4. Run validation script to ensure:
   - No duplicate (ts, symbol)
   - Dates increase for each symbol
   - No all-null OHLCV rows
   - Covers start_date → most recent market day
5. Log ingestion date and universe in data/catalog.json

## Pass/Fail
- **Pass:** File exists, matches data contract, passes validation checks
- **Fail:** Any duplicates, missing columns, wrong frequency, or bad timestamps
