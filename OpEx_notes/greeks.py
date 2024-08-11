# options trading numerical greek calculations  # noqa

from turtle import backward
from matplotlib import pyplot as plt
import numpy as np


def f(x):
    return np.exp(x)


def forward_diff(f, x, dx):
    return (f(x + dx) - f(x)) / dx


# Backward Diff
def backward_diff(f, x, dx):
    return (f(x) - f(x - dx)) / dx


# Central Diff
def central_diff(f, x, dx):
    return (f(x + dx) - f(x - dx)) / (2 * dx)


plt.figure(figsize=(8, 6))
_delta_xs = [1.5, 1.0, 0.5, 0.2, 0.1]
nums = np.arange(1, 5, 0.01)
# nums = np.linspace(1.0, 5.0, 0.01)
true = f(nums)

plt.plot(nums, true, label="True", linewidth=3)

# for delt in _delta_xs:
#     plt.plot(
#         nums,
#         forward_diff(f, nums, delt),
#         label=f"$\\Delta x$ = {delt}",
#         linewidth=2,
#         linestyle="--",
#     )

plt.legend()
# plt.xlim(right=6)
plt.xlabel("Derivative")
# plt.ylim(top=350)
plt.ylabel("$x$")
plt.title("Finite Difference")


for delt in _delta_xs:
    plt.plot(
        nums,
        [
            forward_diff(f, nums, delt),
            backward_diff(f, nums, delt),
            central_diff(f, nums, delt),
        ],
        label=f"$\\Delta x$ = {delt}",
        linewidth=2,
        linestyle="--",
    )