import yfinance as yf
import pandas as pd

class MeanReversionStrategy:
    def __init__(self, symbol, start, end, window=20):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.window = window

    def run(self):
        df = yf.download(self.symbol, start=self.start, end=self.end)
        # Flatten MultiIndex columns if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = ['_'.join(col).strip() for col in df.columns.values]
            close_col = f'Close_{self.symbol}'
        else:
            close_col = 'Close'
        df = df[[close_col]].copy()
        df.rename(columns={close_col: 'Close'}, inplace=True)
        df['rolling_mean'] = df['Close'].rolling(self.window).mean()
        df['rolling_std'] = df['Close'].rolling(self.window).std()
        # Drop rows with NaN values from rolling calculations
        df = df.dropna().copy()
        zscore = (df['Close'] - df['rolling_mean']) / df['rolling_std']
        df['zscore'] = zscore.values
        df['signal'] = 0
        df.loc[df['zscore'] < -2, 'signal'] = 1  # Buy
        df.loc[df['zscore'] > 2, 'signal'] = -1  # Sell
        df['signal'] = df['signal'].ffill().fillna(0)
        df['exit'] = (df['zscore'] * df['signal'] < 0).astype(int)
        return df
