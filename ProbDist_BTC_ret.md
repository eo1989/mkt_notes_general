Ernest Orlowski

# Check out [BlackScholesGreeks](clinthoward.github.io/portfolio/2017/04/16/BlackScholesGreeks/)

<details class="code-fold">
<summary>Code</summary>

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import yfinance as yf
from IPython.display import display
```

</details>

Calculating the stock return probability distribution is popular in
statistics, quantitative analysis, and algorithmic trading to forecast
future stock prices and assess risks. The probability distribution of
stock returns represents the likelihood of different returns that may
generate over a certain period. The SciPy library will be used for its
normal distribution functions (like the survival function). The survival
function (also known as the complementary cumulative distribution
function, or CCDF) is the context of normal distributions describes the
probability) that a random variable `x` takes on a value greater than a
certain threshold. We will use it on the bitcoin spot price.

<details class="code-fold">
<summary>Code</summary>

``` python
from datetime import datetime
TICKER = 'BTC-USD'
df = yf.download(TICKER, start='2024-01-01', interval='1d', auto_adjust=True)
_df = (
    df.rename(columns={col: col[0] for col in df.columns})
    )

# print(_df)
display(_df.head())
```

</details>

    [*********************100%***********************]  1 of 1 completed

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead tr th {
        text-align: left;
    }
&#10;    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>

| Price      | Close        | High         | Low          | Open         | Volume      |
|------------|--------------|--------------|--------------|--------------|-------------|
| Ticker     | BTC-USD      | BTC-USD      | BTC-USD      | BTC-USD      | BTC-USD     |
| Date       |              |              |              |              |             |
| 2024-01-01 | 44167.332031 | 44175.437500 | 42214.976562 | 42280.234375 | 18426978443 |
| 2024-01-02 | 44957.968750 | 45899.707031 | 44176.949219 | 44187.140625 | 39335274536 |
| 2024-01-03 | 42848.175781 | 45503.242188 | 40813.535156 | 44961.601562 | 46342323118 |
| 2024-01-04 | 44179.921875 | 44770.023438 | 42675.175781 | 42855.816406 | 30448091210 |
| 2024-01-05 | 44162.691406 | 44353.285156 | 42784.718750 | 44192.980469 | 32336029347 |

</div>

<details class="code-fold">
<summary>Code</summary>

``` python
# weekly_data = df.resample('W').agg({'Close': ['first', 'last']})
# weekly_data.columns = ['start_of_week_price', 'end_of_week_price']

# weekly_data['start_of_week'] = weekly_data.index - pd.offsets.Week(weekday = 0) + pd.offsets.BDay(0)
# weekly_data['end_of_week'] = weekly_data.index - pd.offsets.Week(weekday = 4) + pd.offsets.BDay(0)

# weekly_data['PriceChange'] = weekly_data['end_of_week_price'] - weekly_data['start_of_week_price']
# weekly_data['PercentChange'] = (weekly_data['PriceChange'] / weekly_data['start_of_week_price'])*100

# price_changes = weekly_data['PercentChange'].dropna()
```

</details>
