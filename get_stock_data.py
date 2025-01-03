from datetime import date
import yfinance as yf  # noqa: I001, BLE001
import numpy as np
import pandas as pd


def get_stock_data(tickers: list[str], start: str, end: str):
    data = {}
    for ticker in tickers:
        try:
            df = pd.read_csv(f"../_data/{ticker}.csv", index_col=0, parse_dates=True)
            data[ticker] = df
        except Exception as e:  # noqa: BLE001
            print(f"Downloading data for {ticker} due to error: {e}")
            df = yf.download(
                ticker, start=start, end=end, group_by="ticker", auto_adjust=True
            )
            # df = yf.download(ticker, start = start, end = end)
            data[ticker] = df
            df.to_csv(f"../_data/{ticker}.csv")
    return data


if __name__ == "__main__":
    get_stock_data(
        tickers=[
            "AAPL",
            "AVGO",
            "RIVN",
            "LLY",
            "LULU",
            "LCID",
            "VST",
            "PLTR",
            "NVDA",
            "MDB",
            "MBLY",
            "RDDT",
            "UBER",
            "VKTX",
            "VRNA",
            "QURE",
        ],
        start = "2023-01-01",
        end = date.today()
    )
