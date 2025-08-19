"""
Test the Yahoo Finance data source

This script is responsible for:
- Testing the Yahoo Finance data source
- Checking if the data source is working as expected
"""

import unittest
import yfinance as yf
import pandas as pd
from unittest.mock import Mock, patch
from app.data.sources.yahoo_source import YahooSource
from app.data.sources.base_class import DataSource, DataSourceError, InvalidSymbolError

class TestYahooSource(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.yahoo_source = YahooSource()
    
    def test_init(self):
        """Test the initialization of the YahooSource class"""
        source = YahooSource()
        self.assertIsInstance(source, YahooSource)
        self.assertIsInstance(source , DataSource)
        self.assertIsNone(source.api_key)

    def test_properties(self):
        """Test YahooSource properties"""
        self.assertEqual(self.yahoo_source.name, "yahoo")
        self.assertFalse(self.yahoo_source.requires_api_key)
        self.assertIsInstance(self.yahoo_source.supported_intervals, list)
        self.assertIn("1d", self.yahoo_source.supported_intervals)
    
    def test_validate_symbol_valid(self):
        """Test validate_symbol with a valid symbol"""
        valid_symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
        for symbol in valid_symbols:
            self.assertTrue(self.yahoo_source.validate_symbol(symbol))
    
    def test_validate_symbol_invalid(self):
        """Test validate_symbol with an invalid symbol"""
        invalid_symbols = [123, None, "", "123AAPL", "AAPL@"]
        for symbol in invalid_symbols:
            with self.assertRaises(InvalidSymbolError):
                self.yahoo_source.validate_symbol(symbol)
        
    def test_check_rate_limit(self):
        """Test the check_rate_limit method"""
        # Yahoo Finance doesn't have a rate limit so it always returns True
        self.assertTrue(self.yahoo_source.check_rate_limit())
    
    def test_standardize_data_empty(self):
        """Test _standardize_data with empty data"""
        data = pd.DataFrame()
        result = self.yahoo_source._standardize_data(data)
        self.assertTrue(result.empty)
    
    def test_standardize_data_valid(self):
        """Test data standardization with valid data"""
        # create sample raw data
        raw_data = pd.DataFrame({
            'Open': [100, 101, 102],
            'High': [105, 106, 107],
            'Low': [95, 96, 97],
            'Close': [102, 103, 104],
            'Volume': [1000, 1500, 2000]
        }, index = pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']))

        result = self.yahoo_source._standardize_data(raw_data)

        expected_columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
        self.assertEqual(list(result.columns), expected_columns)
        
        # Check data types
        self.assertIsInstance(result['timestamp'].iloc[0], pd.Timestamp)
    
    @patch('yfinance.Ticker')
    def test_fetch_raw_data_success(self, mock_ticker):
        """Test successful raw data fetching"""
        # Mock the yfinance response
        mock_data = pd.DataFrame({
            'Open': [100], 'High': [105], 'Low': [99], 
            'Close': [103], 'Volume': [1000]
        })
        mock_ticker_instance = Mock()
        mock_ticker_instance.history.return_value = mock_data
        mock_ticker.return_value = mock_ticker_instance

        result = self.yahoo_source.fetch_data("AAPL", "1d", "1d")
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ticker.assert_called_once_with("AAPL")
        self.assertEqual(self.yahoo_source.request_count, 1)

    @patch('yfinance.Ticker')
    def test_fetch_raw_data_error(self, mock_ticker):
        """Test raw data fetching with an error"""
        # Mock yfinance to raise an exception
        mock_ticker.side_effect = Exception("Newtork error")
        with self.assertRaises(DataSourceError):
            self.yahoo_source._fetch_raw_data("INVALID", "1y", "1d")
    
    @patch('yfinance.Ticker')
    def test_fetch_data_invalid_symbol(self, mock_ticker):
        """Test fetching data with an invalid symbol"""
        with self.assertRaises(DataSourceError):
            self.yahoo_source.fetch_data("", "1y", "1d")
        
        mock_ticker.assert_not_called()
        self.assertEqual(self.yahoo_source.request_count, 0)

    @patch('yfinance.Ticker')
    def test_fetch_data_rate_limit(self, mock_ticker):
        """Test that rate limiting is checked before API call"""

        # Mock the yfinance response
        mock_data = pd.DataFrame({
            'Open': [100], 'High': [105], 'Low': [99], 
            'Close': [103], 'Volume': [1000]
        })
        mock_ticker_instance = Mock()
        mock_ticker_instance.history.return_value = mock_data
        mock_ticker.return_value = mock_ticker_instance
        
        result = self.yahoo_source.fetch_data("AAPL", "1y", "1d")

        # Verify the method completed successfully
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(self.yahoo_source.request_count, 1)
    
if __name__ == '__main__':
    unittest.main()
