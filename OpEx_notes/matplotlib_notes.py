# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
def f(x):
    return x * (x - 2) * np.exp(3 - x)


def g(x):
    return x**2


def h(x):
    return 1 - x

# %%
x = np.linspace(-0.5, 3.0)  # 50 (default) values between -0.5 and 3
y1 = f(x)
y2 = g(x)
y3 = h(x)

# %%
fig, ax = plt.subplots()
ax.plot(x, y1, "k")  # black solid line style
ax.plot(x, y2, "k--")  # black dashed line style
ax.plot(x, y3, "k.-")  # black dot-dashed line style

ax.set_title("Plot of the functions f, g, & h")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(["f", "g", "h"])
ax.text(0.4, 2.0, "intersection")
plt.show()

# %%
plt.plot(x, y1, "k", x, y2, "k--", x, y3, "k.-")
plt.title("Plot of funcs f, g, & h")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["f", "g", "h"])
plt.text(0.4, 2.0, "Intersection")
plt.show()

# %%
y1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y2 = np.array([1.2, 1.6, 3.1, 4.2, 4.8])
y3 = np.array([3.2, 1.1, 2.0, 4.9, 2.5])
fig, ax = plt.subplots()
ax.plot(y1, "o", y2, "x", y3, "*", color="k")
ax.axis([-0.5, 5.5, 0, 5.5])  # set axes
ax.set_xticks([0.5 * i for i in range(9)])  # set xticks
ax.set_yticks([0.5 * i for i in range(11)])  # set yticks
ax.grid()

# %%
# Netwton Iterators
def gen_newton_iters(x0, num):
    iterates = [x0]
    errors = [abs(x0 - 1.0)]
    for _ in range(num):
        x0 = x0 - (x0 * x0 - 1.0) / (2 * x0)
        iterates.append(x0)
        errors.append(abs(x0 - 1.0))
    return iterates, errors

# %%
iterates, errors = gen_newton_iters(2.0, 5)

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)
ax1.plot(iterates, "kx")
ax1.set_title("Iterates")
ax1.set_xlabel("$i$")
ax1.set_ylabel("$x_i$")

ax2.semilogy(errors, "kx")  # plot y on logarithmic scale
ax2.set_title("Error")
ax2.set_xlabel("$i$")
ax2.set_ylabel("Error")

# %%
# Plotting with error bars
measurement_id = np.arange(1, 11)
measurements = np.array([2.3, 1.9, 4.4, 1.5, 3.0, 3.3, 2.9, 2.6, 4.1, 3.6])  # cm
err = np.array([0.1] * 10)  # 1mm

# %%
fig, ax = plt.subplots()

# ax.errorbar(measurement_id, measurements, yerr=err, fmt="kx", capsize=2.0)
ax.bar(measurement_id, measurements, yerr=err, capsize=2.0, alpha=0.4)
ax.set_title("Plot of measurements and their estimated error")
ax.set_xlabel("Measurement ID")
ax.set_ylabel("Measurement(cm)")
ax.set_xticks(measurement_id)

# %% [markdown]
# Surface plotting to the corresponding function:
#
# $$
# f(x, y) = \exp(-((x - 2)^2 + (y - 3)^2)/4) - \exp(-((x + 3)^2 + (y + 2)^2)/3)
# $$
#

# %%
X = np.linspace(-5, 5)
Y = np.linspace(-5, 5)

grid_x, grid_y = np.meshgrid(X, Y)

z = np.exp(-((grid_x - 2.0) ** 2 + (grid_y - 3.0) ** 2) / 4) - np.exp(
    -((grid_x + 3.0) ** 2 + (grid_y + 2.0) ** 2) / 3
)

from mpl_toolkits import mplot3d # noqa

fig = plt.figure()

ax = fig.add_subplot(projection="3d")

ax.plot_surface(grid_x, grid_y, z, cmap="viridis")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Graph of the function f(x, y)")

# %%
fig = plt.figure()
plt.contour(grid_x, grid_y, z, cmap="viridis")
plt.title("Contours of f(x, y)")
plt.xlabel("x")
plt.ylabel("y")

# %%
# plotting trisurf
x = np.array(
    [
        0.19,
        -0.82,
        0.8,
        0.95,
        0.46,
        0.71,
        -0.86,
        -0.55,
        0.75,
        -0.98,
        0.55,
        -0.17,
        -0.89,
        -0.4,
        0.48,
        -0.09,
        1.0,
        -0.03,
        -0.87,
        -0.43,
    ]
)
y = np.array(
    [
        -0.25,
        -0.71,
        -0.88,
        0.55,
        -0.88,
        0.23,
        0.18,
        -0.06,
        0.95,
        0.04,
        -0.59,
        -0.21,
        0.14,
        0.94,
        0.51,
        0.47,
        0.79,
        0.33,
        -0.85,
        0.19,
    ]
)
z = np.array(
    [
        -0.04,
        0.44,
        -0.53,
        0.4,
        -0.31,
        0.13,
        -0.12,
        0.03,
        0.53,
        -0.03,
        -0.25,
        0.03,
        -0.1,
        -0.29,
        0.19,
        -0.03,
        0.58,
        -0.01,
        0.55,
        -0.06,
    ]
)

fig = plt.figure(tight_layout=True)
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
ax1.plot_trisurf(x, y, z)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
ax1.set_title("Approximate sufrace")

ax2 = fig.add_subplot(1, 2, 2)
ax2.tricontour(x, y, z)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("Approximate contours")

# %%
# Customizing 3d plots
t = np.linspace(-5, 5)
x, y = np.meshgrid(t, t)
z = np.exp(-((x-2.)**2 + (y-3.)**2)/4) - np.exp(-((x+3.)**2 + (y+2.)**2)/3)
fig = plt.figure()
ax = fig.add_subplot(projection = "3d", azim = -80, elev = 22)
ax.plot_surface(x, y, z, cmap = "viridis", vmin = -1.2, vmax = 1.2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Customized 3D surface plot")


# %%
"""
Normalization step in applying a colormap is performed by an object derived from the Normalize class.
Mpl provides a number of standard normalization routines, including LogNorm and PowerNorm.
An alternative Normalize subclass can be added using the `norm` keyword of `plot_surface` or other plotting functions.
"""
from matplotlib.colors import LightSource  # noqa
light_source = LightSource(0, 45)  # angles of lightsource
cmap = plt.get_cmap("binary_r")
vals = light_source.shade(z, cmap)
surf = ax.plot_surface(x, y, z, facecolors = vals)
# plt.show()
# %%
def f(x, y):
    v = x**2 + y**2
    return np.exp(-2*v)* (x + y), np.exp(-2*v) * (x - y)

t = np.linspace(-1., 1.)
x, y = np.meshgrid(t, t)
dx, dy = f(x, y)
fig, ax = plt.subplots()
ax.quiver(x, y, dx, dy)
# %%
def f(x, y):
    v = x**2 + y**2
    return np.exp(-2*v)* (x + y), np.exp(-2*v) * (x - y)

t = np.linspace(-1., 1.)
x, y = np.meshgrid(t, t)
dx, dy = f(x, y)
fig, ax = plt.subplots()
ax.streamplot(x,y, dx, dy)
# %%
