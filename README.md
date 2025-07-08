# xquantesis - The XNO-powered Quant Trading Toolkit built on Practical Wisdom.
**`xquantesis` = XNO + Quant + Phronesis**  

---

**`xquantesis`** is a Python SDK designed for quant traders and researchers to **build, test, and deploy** trading strategies using data and infrastructure from the **XNO platform**. It bridges raw market data, alpha generation models, technical indicators, backtesting engines, and execution logic — all grounded in *phronesis* (Greek: φρόνησις), meaning **practical wisdom** — the art of applying knowledge effectively in real-world decisions.

---

## 🔧 Features

### A. 📊 Data Integration (via XNO)
| Data Type                              | Description                             |
|----------------------------------------|-----------------------------------------|
| Historical OHLCV data                  | Candlestick data with multiple timeframes |
| Bid/Ask order book snapshots           | Timestamped order book data capturing full bid-ask depth |
| Tick-level & matching engine data      | Raw trades, quote changes, market events |
| Foreign trading activity               | Buy/sell activity from foreign investors |
| Historical access (Pro)                | Time-series access across all data types |
| Volume profile analytics (Pro)         | Price-volume concentration by levels     |
| Financial statements & reporting (Pro) | Balance sheet, income, cash flow         |
| Macroeconomic data (Pro)               | Interest rates, inflation, GDP, etc.     |

### B. ⏱️ Time Series Utilities
- Technical indicators (e.g. RSI, MACD, VWMA, Ichimoku, OBV)
- Rolling windows (mean, std, z-score, min/max)
- Rolling rank, correlation, volatility
- Time alignment, forward/backward shifting
- Smart Money Concepts (CHoCH, BOS, FVG, Order Blocks)

### C. 🧪 Backtesting Engine
- **Strategy Backtesting**: Simulate strategies on historical data
- **Performance Metrics**: Sharpe ratio, drawdown, alpha/beta, Sortino, Calmar, etc.
- **Execution Simulation**: Slippage, spread, latency, commissions, position tracking
- **Portfolio-level backtests**: Multiple symbols with capital allocation

### D. 📈 Alpha Generation
- **Signal Generation**: Create buy/sell signals using indicators, patterns, or ML models
- **Model Training**: Train ML models on historical data
- **Feature Engineering**: Build custom features from raw or derived inputs (e.g. momentum, mean reversion)

### E. 🚀 Execution Engine
- **Paper & Live Trading**: Use the same logic for backtest, simulation, and live
- **Pluggable Broker API**: Connect to brokers like DNSE, VPS, VNDirect, or custom gateways

### F. 📦 Modular Architecture
- `xquantesis.data`: Data connectors and pipelines
- `xquantesis.report`: Reporting tools and metrics
- `xquantesis.timeseries`: Time series utilities and indicators
- `xquantesis.xno`: Direct integration with XNO platform


## 🧪 Quick Start

```bash
pip install xquantesis
```
```python

from xquantesis import OHLCHandler
from xquantesis import settings
import time

# settings.api_key = 'your_api_key_here'  # Or load from environment variable XNO_API_KEY

data_handler = OHLCHandler([
    'VN30F1M', 'VN30F2M'
], resolution='m')
data_handler.load_data(from_time='2025-07-01', to_time='2025-12-31').stream()
print(data_handler.get_datas())
#
while True:
    print("Current DataFrame:")
    print(data_handler.get_datas())
    print("Data for VN30F1M:")
    print(data_handler.get_data('VN30F1M'))
    time.sleep(20)
```

## 📌 Roadmap

- ✅ **Data Integration** – Load and manage historical & live market data
- ✅ **Technical Indicators** – Built-in and custom time-series features
- ⏳ **Backtesting Engine** – Fast, realistic strategy simulation
- ⏳ **Alpha Generation** – Signal modeling with SMC, ML, or custom logic
- ⏳ **Execution Engine** – Live & paper trading with broker integration
- ⏳ **Reporting Tools** – Performance metrics and visual analytics
- ⏳ **Documentation & Examples** – Notebooks, tutorials, and API reference

> Status Legend: ✅ Completed ⏳ In Progress 🛠️ Planned

---

## 🧠 Philosophy

> In volatile markets, **phronesis** — not just data or theory — determines survival and edge.  
> `xquantesis` is built for those who understand that *practical wisdom* is the ultimate alpha.
