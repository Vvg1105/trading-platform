# Trading Platform: Backtesting & Paper Trading Bot

## 1. Purpose

The goal of this project is to design and implement a modular trading platform that can:
- Download past market price data for multiple assets
- Test trading strategies on historical data
- Simulate live trades using current market prices without risking money
- Track and display performance and safety rules in real time

This project serves two purposes:
- Learn the tools and techniques used by engineers in the finance industry (data pipelines, APIs, strategy engines, dashboards)
- Produce a portfolio-ready system that demonstrates technical skills

## 2. Scope
In-Scope (will be built):

- Data ingestion module: Download daily historical prices for 10–20 assets and store them in a consistent format
- Backtester engine: Play through historical data one day at a time, apply trading rules, simulate performance.

Two trading strategies:
- Momentum strategy — buy assets that have been going up recently.
- Pairs mean reversion strategy — trade when two related assets’ prices move unusually far apart.

- Risk management module: Enforce limits like “no more than 2% of money in one asset” or “stop for the day if losses exceed 5%.”
- Paper trading module: Run the strategies using live prices but with virtual money.
- Monitoring dashboard: Show performance, trades, and risk alerts in real time.
- Performance metrics/reporting: Summarize results with graphs and key metrics.

Out-of-Scope (will not be built):
- Trading with real money
- High-frequency or millisecond-level trading
- Using proprietary or paid data sources

## 3. Success Criteria
The project will be considered complete if:
- The backtester produces consistent results with the same input data
- Both strategies run successfully in backtesting and paper trading modes

The monitoring dashboard displays:
- Equity curve (total account value over time)
- Current holdings
- Active safety rules or alerts

- Risk management rules are enforced automatically in both modes.
- The project runs end-to-end using Docker without manual intervention.

## 4. Risks & Constraints
- Data source limitations: Free APIs may have limits or outages.
- Strategy realism: Without proper safeguards, the system could produce unrealistic performance (look-ahead bias, ignoring trading costs).
- Complexity creep: Adding too many features too early could delay completion.

## 5. Deliverables

GitHub repository with:
- Modular codebase (app/ folder for source, tests/ for unit tests)
- Two strategy modules
- Risk management module
- Monitoring dashboard code

Documentation (/docs/) including:
- Project charter (this file)
- Data contract (column names, types, format)
- Backtester specification
- Risk policy

Sample results:
- Backtest performance report (metrics + equity curve)
- Screenshot/video of dashboard running in paper trading mode

Deployment setup:
- Docker Compose file for running the system locally
- README with step-by-step setup instructions