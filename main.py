from strategy import MeanReversionStrategy
from backtest import Backtester
from utils import plot_results, print_metrics

if __name__ == "__main__":
    # Config
    symbol = "AAPL"  # or "BTC-USD"
    start_date = "2020-01-01"
    end_date = "2024-01-01"
    window = 20
    fee = 0.001  # 0.1% per trade

    # 1. Run strategy
    strategy = MeanReversionStrategy(symbol, start_date, end_date, window)
    df = strategy.run()

    # 2. Backtest
    backtester = Backtester(df, fee)
    results = backtester.run()

    # 3. Plot
    plot_results(df, results)

    # 4. Metrics
    print_metrics(results)
