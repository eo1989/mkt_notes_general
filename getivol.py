# %%
# ---
# title: "iv term structure"
# format: html
# jupyter: Win Pyenv3.11.1
# ---

# %%
import yfinance as yf
import time  # noqa: F401
import pandas as pd
from datetime import date
from yahoo_fin import options
import numpy as np
import math

import matplotlib.pyplot as plt

from warnings import filterwarnings

filterwarnings("ignore")


# %%

symbol = "AMD"
RFR = math.e ** (0.0525) - 1
TODAY = date(2024, 2, 23)

ticker_yahoo = yf.Ticker(symbol)
data = ticker_yahoo.history()
_price = data["Close"].iloc[-1]
print(type(_price))

__price = (data["Close"].iloc[-1]).round(2)
print(type(__price))


# %%
def _get_iv(chain):
    """get_iv(Object)
    @param Object: chain, an objcet from options.get_options_chain()
    Returns implied volatility as float
    """
    iv = None
    # iv = str(iv) or None
    for i in range(len(chain) - 1):
        c = chain["Strike"]
        if c[i + 1] >= _price and c[i] <= _price:
            iv = chain["Implied Volatility"][i]
            # if None or 0 or 0.0 or [] or {} or () or '':
            #     print("iv not str")
            # print(f"iv = {iv}")

            break
        # iv = float(iv) # strip("%")
    if iv is None:
        # return [float(iv.strip("%")) / 100 if iv is not None else None]
        return iv
    elif iv is str:
        return iv.strip("%") / 100


def get_iv(type_options):
    """get_iv(str)
    @param str: type_options, a string to specify either "calls" or "puts"
    Returns tuple of (A) list of expiry dates, and (B) a list of volatilites (iv)
    """
    list_iv = []
    list_expdates = []
    # date_expir_str: str
    for date_expire_str in options.get_expiration_dates(symbol):
        tmp = options.get_options_chain(symbol, date_expire_str)[type_options]
        iv = _get_iv(tmp)
        list_expdates.append(date_expire_str)
        list_iv.append(iv)
        print(f"{date_expire_str}; ATM Call; IV: {iv}")
    return (list_expdates, list_iv)


list1, list2 = get_iv("calls")

# %%
pd.DataFrame({"Expiry": list1, "Implied Volatility": list2}).plot(
    x="Expiry",
    y="Implied Volatility",
    kind="line",
    xlabel="Expiration Date",
    ylabel="Implied Volatility",
)

# %%
np.average(np.array(list2))

# %%
list1, list2 = get_iv("puts")

pd.DataFrame({"Expiry": list1, "Implied Volatility": list2}).plot(
    x="Expiry",
    y="Implied Volatility",
    kind="line",
    xlabel="Expiration Date",
    ylabel="Implied Volatility",
)

# %%
np.average(np.array(list2))

# %%
from datetime import date, datetime

date_today = data.index[len(data) - 1].date()
date_today

# %%
date(2024, 2, 22)


def get_data(con_type):
    chains, list_ttm, list_moneyness, list_iv = {}, [], [], []

    for date_expire_str in options.get_expiration_dates(symbol):
        chain = options.get_options_chain(symbol, date_expire_str)[con_type]
        _exp_date = datetime.strptime(date_expire_str, "%B %d, %Y").date()
        ttm = (date(_exp_date.year, _exp_date.month, _exp_date.day) - date_today).days

        chains[ttm] = chain

        for i in range(len(chain) - 1):
            iv = float(chain["Implied Volatility"][i].strip("%"))
            if iv < 100:
                k = chain["Strike"][i]
                list_ttm.append(ttm)
                list_moneyness.append(_price / k)
                list_iv.append(iv)
    return (chains, list_ttm, list_moneyness, list_iv)


# %%
def do_plots(chains, list_ttm, list_moneyness, list_iv):
    list_x_atm, list_y_atm = [], []

    for ttm in chains.keys():
        df = chains[ttm]
        df_filtered = df[(df["Strike"] > _price)]
        list_x_atm.append(ttm)
        list_y_atm.append(
            float(df_filtered["Implied Volatility"][df_filtered.index[0]].strip("%"))
        )

    plt.plot(list_x_atm, list_y_atm, label="ATM Strike: " + con_type)
    plt.legend()
    plt.xlabel("Time to Maturity (days)")
    plt.ylabel("Implied Volatility (%)")
    plt.show()

    fig, ax = plt.figure(figsize=(10, 5)), fig.add_subplot(projection="3d")
    for i in range(len(list_ttm) - 1):
        ax.scatter(list_ttm[i], list_moneyness[i], list_iv[i], c="b", marker="o")

    ax.set_xlabel("Time to Maturity (Days)")
    ax.set_ylabel("Moneyness")
    ax.set_zlabel("Implied Volatility (%)")
    plt.show()

    fig, ax = plt.figure
