import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use("notebook")
K = 1_000
fig = plt.figure()
ax1 = fig.add_subplot(121)
shrink = 0.5
gammas = [2.0, 1.0, 0.5, 0.01]
labels = [f"$N/K = {1 / gamma}$" for gamma in gammas]
slab = labels[0] + " shrunk"
e_values = [None for gamma in gammas]
for idx, gamma in enumerate(gammas):
    N = int(K / gamma)
    X = np.random.normal(size=(N, K))
    C = X.T @ X / N  # (K, K)
    e_values[idx], _ = np.linalg.eigh(C)
    ax1.plot(range(K), np.flip(e_values[idx]), label=labels[idx])
    if idx == 0 and shrink:
        shrunk, _ = np.linalg.eigh(shrink * C + (1 - shrink) * np.identity(K))
        ax1.plot(range(K), np.flip(shrunk), "-.", color="m", label=slab)

ax1.plot(range(K), np.ones(K), "--", color="grey")
ax2 = fig.add_subplot(122)
plt.yscale("log")
for idx, gamma in enumerate(gammas):
    # Marchenko-Pastur theory:
    a, b = (1 - np.sqrt(gamma)) ** 2, (1 + np.sqrt(gamma)) ** 2
    xx = np.linspace(a, b, 100)
    mp = np.sqrt((b - xx) * (xx - a)) / (2 * np.pi * gamma * xx) * max(gamma, 1)
    ax2.plot(xx, mp, label=labels[idx] + " (MP)")

for idx, gamma in enumerate(gammas):
    # histograms of eigenvalues:
    evals = e_values[idx]
    evals = evals[evals > 1e-3].reshape((-1, 1))
    ax2.hist(
        evals,
        bins=50,
        histtype="step",
        density=True,
        fill=True,
        alpha=0.1 + idx * 0.05,
    )
    if idx == 0 and shrink:
        # discard repeated lowest eigenvalues:
        shrunk = shrunk[shrunk > 1 - shrink + 1e-3]
        ax2.hist(
            shrunk,
            bins=40,
            histtype="step",
            density=True,
            color="m",
            label=slab,
        )

ax1.set_xlabel(r"$k$")
ax1.set_ylabel(r"$\lambda$")
ax1.legend()
ax2.set_xlabel(r"$\lambda$")
ax2.legend()
plt.subplots_adjust(wspace=0)
# plt.show()
plt.plot()
