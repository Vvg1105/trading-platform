import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path
from .sources.base_class import DataSource
from .sources.yahoo_source import YahooSource
import logging

class DataCatalog:
    """
    DataCatalog class
    ----------------
    Responsible for:
    - Listing all available tickers
    - Listing all available timeframes
    - Listing all available data sources
    """
    def __init__(self, data_dir: str = "data"):
        self.data_sources: Dict[str, DataSource] = {}
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        # Automatically register YahooSource as a default
        yahoo_source = YahooSource()
        self.add_data_source(yahoo_source)
        logging.info("YahooSource registered as default data source")

    def add_data_source(self, source: DataSource):
        """Add a data source to the catalog"""
        if not isinstance(source, DataSource) or source.name not in self.get_data_sources():
            raise ValueError(f"Invalid data source: {source}")
        self.data_sources[source.name] = source

    def get_data_sources(self) -> List[str]:
        """Get all data sources in the catalog"""
        return list(self.data_sources.keys())
    
    def get_data_source(self, name: str) -> DataSource:
        """Get a data source by name"""
        if name not in self.get_data_sources():
            raise ValueError(f"Data source {name} not found")
        return self.data_sources[name]
    
    def list_symbols(self) -> List[str]:
        """List all available symbols in the catalog"""
        symbols = set()
        for source in self.data_sources.values():
            try:
                symbols.update(source.list_symbols())
            except Exception as e:
                logging.warning(f"Error listing symbols from {source.name}: {str(e)}")
        return list(symbols)    
    
    def list_intervals(self) -> List[str]:
        """List all available intervals in the catalog"""
        intervals = set()
        for source in self.data_sources.values():
            try:
                intervals.update(source.list_intervals())
            except Exception as e:
                logging.warning(f"Error listing intervals from {source.name}: {str(e)}")
        return list(intervals)
    
    def get_data(self, symbol: str, start_date: str, end_date: str, interval: str = "1d", source_name: Optional[str] = None) -> pd.DataFrame:
        """
        Get data for a given symbol and date range
        """

        # 1. Validate the inputs
        # 2. Check if we have any data sources
        # 3. Try to fetch data from available sources
        # 4. Return the data or raise an error

        if not self.data_sources:
            raise ValueError("No data sources available")
        
        if source_name:
            # Try specific source first
            logging.info(f"Fetching data for {symbol} from {source_name}")
            if source_name not in self.get_data_sources():
                raise ValueError(f"Data source {source_name} not found")
            
            source = self.get_data_source(source_name)
            logging.info(f"Using data source: {source_name}")

            try:
                data = source.fetch_data(symbol, period = "1y", interval = interval)
                logging.info(f"Data fetched successfully for {symbol} from {source_name}")
                return data
            except Exception as e:
                raise ValueError(f"Error fetching data from {source_name}: {str(e)}")
        
        else:
            # Try all sources in the catalog
            for source_name, source in self.data_sources.items():
                try:
                    # Convert date range to period format that YahooSource expects (i.e "1d", "1wk", "1mo", etc.)

                    data = source.fetch_data(symbol, period = "1y", interval = interval)
                    logging.info(f"Data fetched successfully for {symbol} from {source_name}")
                    return data
                
                except Exception as e:
                    # If this source fails, try the next one
                    logging.warning(f"Error fetching data from {source_name}: {str(e)} so moving on to the next source")
                    continue
        
            # If no data is found, then all sources have failed and raise an error
            logging.error(f"No data found for {symbol} in any available source")
            raise ValueError(f"No data found for {symbol} in any available source")

