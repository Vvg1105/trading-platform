"""
Base class for data sources

---------------------------

This script is responsible for:
- Defining the base class for data sources
- Defining the interface for data sources
"""

from abc import ABC, abstractmethod
from concurrent.futures import ProcessPoolExecutor
import pandas as pd

## Custom Exceptions ##

# Rate Limit Error for api calls that exceed the rate limit
class RateLimitError(Exception):
    pass

# Invalid Symbol Error for api calls that receive an invalid symbol
class InvalidSymbolError(Exception):
    pass

# Data Source Error for api calls that receive an error from the data source
class DataSourceError(Exception):
    pass


class DataSource(ABC):

    # Initialize the data source
    def __init__(self, api_key: str = None, **kwargs):
        self.api_key = api_key
        self.kwargs = kwargs
        self.request_count = 0
        self.last_request = None

    ## Properties ##

    @property
    def name(self) -> str:
        return self.__class__.__name__.lower().replace("source", "")
    
    @property
    def requires_api_key(self) -> bool:
        return self.api_key is not None
    
    @property
    def supported_intervals(self) -> list[str]:
        return ["1m", "5m", "15m", "30m", "1h", "4h", "1d"]
    
    ## Methods ##

    def validate_symbol(self, symbol: str) -> bool:
        """Validate if symbol is in the correct format"""
        if not symbol or not isinstance(symbol, str):
            return False
        # Basic validation - alphanumeric and dots only
        return symbol.replace('.', '').replace('-', '').isalpha()
    
    def check_rate_limit(self) -> bool:
        """Check if the data source is rate limited"""
        # This will be implemented in the child class
        raise NotImplementedError("check_rate_limit method not implemented")
    
    def _standardize_data(self, raw_data) -> pd.DataFrame:
        """Convert raw data to a standardized format of a DataFrame"""
        # This will be implemented in the child class
        raise NotImplementedError("_standardize_data method not implemented")
    
    def get_rate_limit_info(self) -> dict:
        """Get current rate limit informaiton"""
        return {
            "last_request": self.last_request,
            "request_count": self.request_count
        }

    ## Abstract Methods ##

    @abstractmethod
    def fetch_data(self, symbol: str, period = "1y", interval = "1d") -> pd.DataFrame:
        """Fetch data for a given symbol and date range"""
        pass
    
    @abstractmethod
    def fetch_raw_data(self, symbol: str, period = str, interval = str) -> pd.DataFrame:
        """Fetch raw data for a given symbol and date range"""
        pass
    
