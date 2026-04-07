## dev/creator = tubakhxn

# Mean Reversion Trading System

This project is a Python-based backtesting system for a mean reversion trading strategy. It fetches historical price data (e.g., stocks or crypto), applies a mean reversion logic using z-score, simulates trades with transaction costs, and visualizes results with key performance metrics.

## Features
- Fetches historical data using yfinance
- Implements a mean reversion strategy with rolling mean/z-score
- Simulates realistic trading with position tracking and transaction costs
- Plots price, moving average, buy/sell/exit signals, and equity curve
- Calculates total return, Sharpe ratio, and max drawdown

## How to Fork & Run
1. **Fork this repository** on GitHub (or download the code).
2. Clone your fork or download the ZIP and extract it.
3. Install requirements:
   ```bash
   pip install yfinance pandas matplotlib numpy
   ```
4. Run the main script:
   ```bash
   python main.py
   ```
5. Edit `main.py` to change the symbol, date range, or parameters as needed.

## Relevant Links & Resources
- [yfinance documentation](https://github.com/ranaroussi/yfinance)
- [pandas documentation](https://pandas.pydata.org/docs/)
- [matplotlib documentation](https://matplotlib.org/stable/contents.html)
- [Mean Reversion Trading (Investopedia)](https://www.investopedia.com/terms/m/meanreversion.asp)
- [Sharpe Ratio (Investopedia)](https://www.investopedia.com/terms/s/sharperatio.asp)
- [Max Drawdown (Investopedia)](https://www.investopedia.com/terms/m/maximum-drawdown-mdd.asp)

## Project Structure
- `main.py` — Entry point, runs strategy and backtest
- `strategy.py` — Mean reversion logic
- `backtest.py` — Backtesting engine
- `utils.py` — Plotting and metrics

---
Feel free to fork, modify, and experiment with your own strategies!