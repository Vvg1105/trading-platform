"""
Yahoo Finance Data Source

This script is responsible for:
- Fetching data from Yahoo Finance
- Standardizing the Yahoo Finance data to a common format
- Handling Yahoo Finance specific errors (such as rate limits etc.)'
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
from .base_class import DataSource, RateLimitError, InvalidSymbolError, DataSourceError

class YahooSource(DataSource):

    def __init__(self, api_key: str = None, **kwargs):
        super().__init__(api_key, **kwargs)
        # Yahoo finance doesn't require an api key
        self.api_key = None
    

    ## Properties ##

    @property
    def name(self) -> str:
        return "yahoo"
    
    @property
    def requires_api_key(self) -> bool:
        return False
    
    @property
    def supported_intervals(self) -> list[str]:
        return ["1m", "5m", "15m", "30m", "1h", "4h", "1d", "5d", "1wk", "1mo"]
    
    ## Methods ##

    def check_rate_limit(self) -> bool:
        """Check if the data source is rate limited"""
        # Yahoo finance doesn't have a rate limit
        return True
    
    def _standardize_data(self, raw_data) -> pd.DataFrame:
        """Standardize the raw data to a common format"""
        if raw_data.empty:
            return pd.DataFrame()
        
        # Rename the columns to a standard format
        data = raw_data.copy()
        data.columns = [col.lower() for col in data.columns]

        # Ensure required columns are present
        required_columns = ['open', 'high', 'low', 'close', 'volume']
        for col in required_columns:
            if col not in data.columns:
                data[col] = 0

        # Convert to datetime if not already
        data = data.reset_index()
        if 'date' in data.columns:
            data = data.rename(columns={"date": "timestamp"})
        elif 'index' in data.columns:
            data = data.rename(columns={"index": "timestamp"})

        return data[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    

    def fetch_data(self, symbol: str, period = "1y", interval = "1d") -> pd.DataFrame:
        """Fetch data for a given symbol and date range"""
        try:

            # Validate the symbol and check if data source has a rate limit
            self.validate_symbol(symbol)
            self.check_rate_limit()

            # Fetch raw data
            raw_data = self.fetch_raw_data(symbol, period, interval)

            # Standardize the data
            standardized_data = self._standardize_data(raw_data)

            # Update request tracking
            self.request_count += 1
            self.last_request = datetime.now()

            return standardized_data
        
        except Exception as e:
            raise DataSourceError(f"Error fetching data from Yahoo Finance: {str(e)}")
    
    
    def fetch_raw_data(self, symbol: str, period = str, interval = str) -> pd.DataFrame:
        """Fetch raw data for a given symbol and date range"""
        try:
            # Download data from Yahoo Finance
            historic  = yf.Ticker(symbol)
            data = historic.history(period=period, interval=interval)
            return data

        except Exception as e:
            raise DataSourceError(f"Error fetching raw data from Yahoo Finance: {str(e)}")