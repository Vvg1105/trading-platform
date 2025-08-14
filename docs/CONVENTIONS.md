# Conventions

## Runtime & Tools
- Python: 3.12
- Formatting: black
- Linting: ruff
- Types: mypy (gradual typing)
- Tests: pytest

## Project Layout (top-level)
- `app/` — source code
  - `alpha/` strategies (rules to buy/sell)
  - `backtest/` engine, orders, portfolio
  - `data/` ingest & validation
  - `core/` config, logging
  - `risk/` risk checks & limits
  - `metrics/` performance stats & reports
- `ui/` dashboard & API (later)
- `tests/` unit tests
- `docs/` documentation

## Naming
- Classes: `CamelCase` (e.g., `PortfolioManager`)
- Functions & variables: `snake_case` (e.g., `calc_sharpe`)
- Constants: `ALL_CAPS` (e.g., `TRADING_COST_BPS`)

## Style
- Type hints on public functions.
- No notebooks for core logic (scripts/tests ok).

## Commits
- Format: `[module] short change`
  - Example: `[backtest] add order and fill models`

## Branching
- `main` is stable.
- Feature branches: `feat/<module>-<short-name>`
