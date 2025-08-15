# Trading Platform

A comprehensive trading platform with data ingestion, backtesting, risk management, and analysis capabilities.

## Architecture

The platform consists of several microservices:

- **Data Ingestion Service**: Fetches price data from multiple sources (Yahoo Finance, Alpha Vantage, Polygon)
- **PostgreSQL Database**: Stores historical price data and metadata
- **Redis**: Caching and job queue management
- **Main Application**: Core trading platform logic
- **pgAdmin**: Database management interface (optional)

## Quick Start with Docker

### Prerequisites

- Docker and Docker Compose installed
- API keys for data sources (optional, Yahoo Finance works without keys)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd trading-platform
```

### 2. Configure Environment

Copy the example environment file and add your API keys:

```bash
cp env.example .env
```

Edit `.env` and add your API keys:
```bash
# Get free API keys from:
# Alpha Vantage: https://www.alphavantage.co/support/#api-key
# Polygon: https://polygon.io/
ALPHA_VANTAGE_API_KEY=your_key_here
POLYGON_API_KEY=your_key_here
```

### 3. Start the Platform

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f trading-app

# Stop services
docker-compose down
```

### 4. Access Services

- **Main App**: http://localhost:8000
- **pgAdmin**: http://localhost:5050 (admin@trading.com / admin123)
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

## Data Ingestion

The platform automatically ingests price data for configured symbols:

### Default Symbols
- AAPL, GOOGL, MSFT, TSLA (stocks)
- SPY, QQQ (ETFs)

### Data Sources
1. **Yahoo Finance** (free, no API key required)
2. **Alpha Vantage** (free tier available)
3. **Polygon** (free tier available)

### Manual Data Ingestion

```bash
# Run data ingestion manually
docker-compose exec trading-app python -m app.data.ingestor

# Check ingestion logs
docker-compose exec postgres psql -U trading_user -d trading_platform -c "SELECT * FROM ingestion_logs ORDER BY started_at DESC LIMIT 5;"
```

## 🗄️ Database Schema

### Price Data Table
```sql
price_data (
    id UUID PRIMARY KEY,
    symbol VARCHAR(20),
    timestamp TIMESTAMP WITH TIME ZONE,
    open, high, low, close DECIMAL(15,6),
    volume BIGINT,
    source VARCHAR(50),
    created_at, updated_at TIMESTAMP
)
```

### Symbols Table
```sql
symbols (
    id UUID PRIMARY KEY,
    symbol VARCHAR(20) UNIQUE,
    name VARCHAR(255),
    exchange VARCHAR(50),
    asset_type VARCHAR(50),
    is_active BOOLEAN
)
```

## 🔧 Development

### Adding New Symbols

```sql
INSERT INTO symbols (symbol, name, exchange, asset_type) 
VALUES ('NVDA', 'NVIDIA Corporation', 'NASDAQ', 'stock');
```

### Custom Data Sources

Extend the ingestor by adding new data source classes in `app/data/ingestor.py`.

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | - |
| `REDIS_URL` | Redis connection string | - |
| `ALPHA_VANTAGE_API_KEY` | Alpha Vantage API key | - |
| `POLYGON_API_KEY` | Polygon API key | - |
| `YAHOO_FINANCE_ENABLED` | Enable Yahoo Finance | true |
| `DEFAULT_SYMBOLS` | Comma-separated symbols | AAPL,GOOGL,MSFT,TSLA,SPY,QQQ |

## 📁 Project Structure

```
trading-platform/
├── app/
│   ├── data/           # Data ingestion modules
│   ├── core/           # Core trading logic
│   ├── backtest/       # Backtesting engine
│   ├── risk/           # Risk management
│   ├── metrics/        # Performance metrics
│   ├── alpha/          # Alpha generation
│   └── requirements.txt
├── docs/               # Documentation
├── tests/              # Test files
├── ui/                 # User interface
├── docker-compose.yml  # Docker services
├── init.sql           # Database initialization
└── env.example        # Environment template
```

## Troubleshooting

### Common Issues

1. **Database connection failed**
   ```bash
   docker-compose logs postgres
   ```

2. **API rate limits**
   - Check your API key limits
   - Increase `REQUEST_TIMEOUT_SECONDS` in `.env`

3. **Data not ingesting**
   ```bash
   docker-compose logs data-ingestor
   ```

### Reset Everything

```bash
# Stop and remove all containers and volumes
docker-compose down -v

# Rebuild and start
docker-compose up --build -d
```

## Next Steps

- [ ] Implement backtesting engine
- [ ] Add risk management modules
- [ ] Create web dashboard
- [ ] Add real-time data streaming
- [ ] Implement trading strategies

## License

MIT License - see LICENSE file for details.
