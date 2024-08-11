# %%
# noqa: INP001
from typing import Tuple, Optional, Union, List, Text
from enum import Enum

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D

from dataclasses import dataclass

class OptionType(Enum):
    Call = "Call"
    Put = "Put"

@dataclass
class BS:
    """
    Calculate the option price according to the BSM.

    Attributes
    ==========
    :Option: - OptionType
        True if option is a call, False if option is a put
    :S0: - float
        Price of underlying
    :K: - float
        Strike price
    :Maturity: - float
        Time to maturity in years
    :IR: - float
        Risk-free rate in years
    :sigma: - float
        Volatility of underlying
    :div: - float
        Dividend yield

    Methods
    =======
    :price: - Returns the price of the option according to BSM

    """

    Option: OptionType
    S0: float | np.ndarray
    K: float | np.ndarray
    T: float | np.ndarray
    IR: float | np.ndarray
    sigma: float | np.ndarray
    div: float
    # d1: float = (sigma * np.sqrt(Maturity)) ** (-1) * (
    #     np.log(S0 / K) + (IR - div + sigma**2 / 2) * Maturity
    # )
    # d2: float = d1 - sigma * np.sqrt(Maturity)

    # def prices(self):
    #     if self.Option == "Call":
    #         return np.exp(-self.div * self.Maturity) * norm.cdf(
    #             self.d1
    #         ) * self.S0 - norm.cdf(self.d2) * self.K * np.exp(-self.IR * self.Maturity)
    #     elif self.Option == "Put":
    #         return (
    #             norm.cdf(-self.d2) * self.K * np.exp(-self.IR * self.Maturity)
    #             - np.exp(-self.div * self.Maturity)
    #             - norm.cdf(-self.d1) * self.S0 * np.exp(-self.div * self.Maturity)
    #         )
    d1 = (np.log(S0 / K) + (IR + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K) + (IR - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

    if Option["Call"] == "Call":
        result = S0 * norm.cdf(d1, 0.0, 1.0) - K * np.exp(-IR * T) * norm.cdf(
            d2, 0.0, 1.0
        )
    elif Option["Put"] == "Put":
        result = K * np.exp(-IR * T) * norm.cdf(-d2, 0.0, 1.0) - S0 * norm.cdf(
            -d1, 0.0, 1.0
        )


# Create arrays with the different input values for each variable
_S0 = np.linspace(1, 50, 50)
# K = np.linspace(50, 100, 50)
_T = np.linspace(0.01, 3, 50)
_s = np.linspace(0.001, 8, 50)

# %%

# Calculate prices for different stock prices and time to maturity
ct = np.array([])
for i in range(len(_T)):
    ct = np.append(
        ct,
        BS("Call", S0=_S0, K=25, T=_T[i], IR=0.05, sigma=_s[i], div=0.02),
        axis=0,
    )

# %%