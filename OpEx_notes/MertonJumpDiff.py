import numpy as np  # noqa
import math

rng = np.random.default_rng()
# normal = rng.normal()
# poisson = rng.poisson()


def _cdf(x):
    # noqa
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    # noqa

    sign = 1
    if x < 0:
        sign = -1
    x = abs(x) / np.sqrt(2.0)

    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 + a4) * t) + a3) * t + a2) * t + a1) * t * np.exp(-x * x)

    return 0.5 * (1.0 + sign * y)


def BS_call(S0, sig, tau, r, K):
    d1 = np.log(S0 / K) + (r + 0.5 * sig**2) * tau
    d1 /= sig * np.sqrt(tau)
    d2 = d1 - sig * np.sqrt(tau)

    price = S0 * _cdf(d1) - K * np.exp(-r * tau) * _cdf(d2)
    return price


def merton_call(S0, sig, tau, r, K, lam, muy, sigy, N):
    price = 0.0
    k = np.exp(muy + 0.5 * (sigy**2)) - 1
    for n in range(N):
        sig_n = np.sqrt(sig * sig + n * sigy**2 / tau)
        S0_n = S0 * np.exp(-lam * k * tau + n * muy + 0.5 * n * sigy * sigy)
        prob_n = (lam * tau) ** n / math.factorial(n) * np.exp(-lam * tau)
        price += BS_call(S0_n, sig_n, tau, r, K) * prob_n
    return price


def merton_call_alt(S0, sig, tau, r, K, lam, muy, sigy, N):
    price = 0.0
    k = np.exp(muy + 0.5 * sigy**2) - 1
    lam_b = lam * (1.0 + k)
    for n in range(N):
        sig_n = np.sqrt(sig * sig + n * sigy**2 / tau)
        r_n = r - lam * k + n * (muy + 0.5 * sigy**2) / tau
        prob_n = (lam_b * tau) ** n / math.factorial(n) * np.exp(-lam_b * tau)
        price += BS_call(S0, sig_n, tau, r_n, K) * prob_n
    return price


def merton_call_simulation(S0, sig, tau, r, K, lam, muy, sigy):
    nsim = 100_000
    k = np.exp(muy + 0.5 * sigy**2) - 1
    price = 0.0
    for i in range(nsim):
        # jump_N = np.random.poisson(lam * tau)
        jump_N = rng.poisson(lam*tau)
        # jump_norm = np.random.normal(muy, sigy, jump_N)
        jump_norm = rng.normal(muy, sigy, jump_N)
        jump_sum = np.sum(jump_norm)
        # S_tau = S0 * np.exp((r - lam*k - 0.5*sig**2)*tau + sig * normal(0, np.sqrt(tau)) + jump_sum)
        S_tau = S0 * np.exp(
            (r - lam * k - 0.5 * sig**2) * tau
            + sig * rng.normal(0, np.sqrt(tau))
            + jump_sum
        )
        price += max(S_tau - K, 0)
    price *= np.exp(-r * tau)
    price /= nsim
    return price


print(f"BS_Call = {BS_call(100, 0.4, 1, 0.05, 100)}")
print(f"merton_call = {merton_call(100, 0.4, 1, 0.05, 100, 0.5, 0.1, 0.1, 20)}")
print(f"merton_call_alt = {merton_call_alt(100, 0.4, 1, 0.05, 100, 0.5, 0.1, 0.1, 20)}")
print(
    f"merton_call_simulation = {merton_call_simulation(100, 0.4, 1, 0.05, 100, 0.5, 0.1, 0.1)}"
)
