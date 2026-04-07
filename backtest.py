import pandas as pd

class Backtester:
    def __init__(self, df, fee=0.001):
        self.df = df.copy()
        self.fee = fee

    def run(self):
        df = self.df.copy()
        position = 0
        entry_price = 0
        equity = [1.0]
        trades = []
        for i in range(1, len(df)):
            if position == 0:
                if df['signal'].iloc[i] == 1:
                    position = 1
                    entry_price = df['Close'].iloc[i]
                    trades.append({'type': 'buy', 'price': entry_price, 'index': i})
                    equity.append(equity[-1] * (1 - self.fee))
                elif df['signal'].iloc[i] == -1:
                    position = -1
                    entry_price = df['Close'].iloc[i]
                    trades.append({'type': 'sell', 'price': entry_price, 'index': i})
                    equity.append(equity[-1] * (1 - self.fee))
                else:
                    equity.append(equity[-1])
            elif position == 1:
                if df['exit'].iloc[i]:
                    pnl = (df['Close'].iloc[i] - entry_price) / entry_price
                    equity.append(equity[-1] * (1 + pnl - self.fee))
                    trades.append({'type': 'exit', 'price': df['Close'].iloc[i], 'index': i})
                    position = 0
                else:
                    equity.append(equity[-1])
            elif position == -1:
                if df['exit'].iloc[i]:
                    pnl = (entry_price - df['Close'].iloc[i]) / entry_price
                    equity.append(equity[-1] * (1 + pnl - self.fee))
                    trades.append({'type': 'exit', 'price': df['Close'].iloc[i], 'index': i})
                    position = 0
                else:
                    equity.append(equity[-1])
        df = df.iloc[1:].copy()
        df['equity'] = equity[1:]
        return {'df': df, 'trades': trades}
