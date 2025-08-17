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
from base_class import DataSource, RateLimitError, InvalidSymbolError, DataSourceError

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
