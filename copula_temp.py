from functools import partial
from itertools import combinations, product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import yfinance as yf
from numpy.linalg import norm as np_norm
from scipy.optimize import minimize as sp_minimize
from sklearn.linear_model import LinearRegression as lr

prices = pd.read_parquet("prices_yf.parquet")
THRES = 0.8
N_DAYS = 500
_nulls = prices.isnull().mean(axis=0)
stocks_w_nans = _nulls[_nulls > THRES].sort_values()

cols = prices.columns
stocks = cols[~cols.isin(stocks_w_nans.index)]
prices = prices.loc[:, stocks].ffill().dropna().iloc[:N_DAYS, :]

returns = prices.pct_change().iloc[1:, :]
# returns
# prices.head()

# tickers available to be used (in the parque) are => ['gme', 'aapl', 'tsla', 'msft', 'dis', 'ge', 'goog', 'amzn', 'amd', 'nvda']
cpl = ('amd', 'goog')
dic_cpl = {'x': cpl[0], 'y': cpl[1]}
returns_cpl = returns.loc[:, cpl]
returns.plot.scatter(**dic_cpl, grid = True)
