"""
Validate module
----------------
Responsbile for:
- Validating the ingested data
- Checking for duplicate keys: (ts, symbol) must be unique
- Checking for monotonic timestamps
- Checking column presence: open, high, low, close, volume
- Checking for missing or negative values
- Checking that the first timestamp is the start date and the last timestamp is the most recent market day
"""