import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('dark_background')

def plot_results(df, results):
    trades = results['trades']
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    # Price + MA
    axs[0].plot(df.index, df['Close'], label='Price', color='cyan')
    axs[0].plot(df.index, df['rolling_mean'], label='MA', color='orange')
    buy_idx = [t['index'] for t in trades if t['type'] == 'buy']
    sell_idx = [t['index'] for t in trades if t['type'] == 'sell']
    exit_idx = [t['index'] for t in trades if t['type'] == 'exit']
    axs[0].scatter(df.iloc[buy_idx].index, df.iloc[buy_idx]['Close'], marker='^', color='lime', label='Buy', s=80)
    axs[0].scatter(df.iloc[sell_idx].index, df.iloc[sell_idx]['Close'], marker='v', color='red', label='Sell', s=80)
    axs[0].scatter(df.iloc[exit_idx].index, df.iloc[exit_idx]['Close'], marker='o', color='yellow', label='Exit', s=60)
    axs[0].legend()
    axs[0].set_ylabel('Price')
    axs[0].set_title('Mean Reversion Trading System')
    # Equity curve
    # Use the index from results['df'] to match equity length
    axs[1].plot(results['df'].index, results['df']['equity'], color='magenta', label='Equity Curve')
    axs[1].set_ylabel('Equity')
    axs[1].legend()
    plt.tight_layout()
    plt.show()

def print_metrics(results):
    df = results['df']
    returns = df['equity'].pct_change().dropna()
    total_return = df['equity'].iloc[-1] - 1
    sharpe = np.sqrt(252) * returns.mean() / returns.std() if returns.std() > 0 else 0
    roll_max = df['equity'].cummax()
    drawdown = (df['equity'] - roll_max) / roll_max
    max_dd = drawdown.min()
    print(f"Total Return: {total_return*100:.2f}%")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Max Drawdown: {max_dd*100:.2f}%")
