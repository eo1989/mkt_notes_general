# ruff: noqa: I001
# import jax
from jax import grad
import jax.numpy as np
from jax.scipy.stats import norm


class EuropeanCall:
    """"""

    def call_price(self, asset_price, asset_vol, strike_price, time_expiration, rfr):
        b = np.exp(-rfr * time_expiration).astype("float")
        x1 = np.log(asset_price / (b * strike_price))
        x1 += 0.5 * ((asset_vol**2) * (time_expiration))
        # x1 = x1/ (asset_vol*(time_expiration**.5))
        x1 /= asset_vol * (time_expiration**0.5)
        z1 = norm.cdf(x1)
        # z1 = z1*asset_price
        # z1 *= norm.cdf(x1) * asset_price
        z1 *= asset_price
        x2 = (
            np.log(asset_price / (b * strike_price))
            - 0.5 * (asset_vol**2) * time_expiration
        )
        x2 = x2 / (asset_vol * (time_expiration**0.5))
        z2 = norm.cdf(x2)
        # z2 = b * strike_price * z2
        z2 *= b * strike_price
        return z1 - z2

    def __init__(self, inputs):
        self.asset_price = inputs[0]  # ruff: ignore
        self.asset_vol = inputs[1]  # ruff: ignore
        self.strike_price = inputs[2]  # ruff: ignore
        self.time_expiration = inputs[3]  # ruff: ignore
        self.rfr = inputs[4]  # ruff: ignore

        self.price = self.call_price(
            self.asset_price,
            self.asset_vol,
            self.strike_price,
            self.time_expiration,
            self.rfr,
        )

        self.gradient_func = grad(self.call_price, (0, 1, 3, 4))
        self.delta, self.vega, self.theta, self.rho = self.gradient_func(
            inputs[0], inputs[1], inputs[2], inputs[3], inputs[4]
        )
        self.theta /= -365
        self.vega /= 100
        self.rho /= 100


class EuropeanPut:
    """ """

    def call_price(self, asset_price, asset_vol, strike_price, time_expiration, rfr):
        b = np.exp(-rfr * time_expiration).astype("float")
        x1 = (
            np.log((b * strike_price) / asset_price)
            + 0.5 * (asset_vol**2) * time_expiration
        )
        x1 = x1 / (asset_vol * (time_expiration**0.5))
        # x1 /= (asset_vol*(time_expiration)**.5)
        z1 = norm.cdf(x1)
        # z1 = z1*asset_price
        z1 *= b * strike_price
        x2 = (
            np.log((b * strike_price) / asset_price)
            - 0.5 * (asset_vol**2) * time_expiration
        )
        # x2 = x2 / (asset_vol * (time_expiration**0.5))
        x2 /= asset_vol * (time_expiration**0.5)
        z2 = norm.cdf(x2)
        # z2 = b * strike_price * z2
        z2 *= asset_price
        return z1 - z2

    def __init__(self, inputs):
        self.asset_price = inputs[0]  # ruff: ignore
        self.asset_vol = inputs[1]  # ruff: ignore
        self.strike_price = inputs[2]  # ruff: ignore
        self.time_expiration = inputs[3]  # ruff: ignore
        self.rfr = inputs[4]  # ruff: ignore

        self.price = self.call_price(
            self.asset_price,
            self.asset_vol,
            self.strike_price,
            self.time_expiration,
            self.rfr,
        )

        self.gradient_func = grad(self.call_price, (0, 1, 3, 4))
        self.delta, self.vega, self.theta, self.rho = self.gradient_func(
            inputs[0], inputs[1], inputs[2], inputs[3], inputs[4]
        )
        self.theta /= -365
        self.vega /= 100
        self.rho /= 100


if __name__ == "__main__":
    print(
        f"Price of a $100 stock w/ a $110 strike w/ 30 days to expiry & 16% volatility & 0.04% rfr is: {EuropeanCall.call_price(100, .16, 110, 30, 0.04):.2f}"
    )
