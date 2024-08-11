# noqa: B01
# noqa: INP

# %%
import numpy as np

a = np.arange(1_000_000)
print(a)
# %%
# change shape (still references the same data) to a 2dim 1000x1000 array
b = a.reshape((1000, 1000))
b  # noqa: B018
# %%
# first row of the matrix
b[0]

# %%
# first column of the matrix
b[:, 0]
# %%
# row 10 up to 12, the even columns between 20 and 30
b[10:12, 20:30:2]
# %%
# Row 10, columns 5 up to 10
b[10, 5:10]
# %%
# alternate syntax for the last slice
b[10][5:10]
# %%
# slicing is powerful bc they are all references/views instead of copies.
# Meaning if you modify the data in a slice, the original array will be modified as well.
b[0] *= 10
b[:, 0] *= 20
# %%
a
# %%
b[0:2]
# %%
# Notice after modifying the first row and first column for each row, we see that a, b, and consequently
# all slices of a and b have been modified; and all of that in a single operation
# instead of having to loop.
a = list(range(1_000_000))
b = np.array(a)

# %%
def dot(xs, ys):
    total = 0
    for x, y in zip(xs, ys, strict=False):
        total += x * y
    return total

%timeit dot(a, a)

# %%
%timeit np.dot(b, b)
# aka np.dot is ~150x faster than than python implementation.
# %%
## Numba
import numba as na
numbers = np.arange(500, dtype=np.int64)

# %%
@na.vectorize([na.int64(na.int64)])
def add_one(x):
    return x + 1


# %%
numbers
# %%
add_one(numbers)
# %%
"""
The function @vectorize above only accepts a 64bit int and returns a 64bit int.
if you want to create a function that takes two 32- or 64bit floats and returns a 64bit int it would be the following:
"""
# @na.vectorize([
#     na.int64(na.float32, na.float32),
#     na.int64(na.float64, na.float64),
# ])
from scipy import sparse as sp
x = np.identity(10_000)
y = sp.identity(10_000)
x.data.nbytes

# %%
"""
Summing the memory usage of scipy.sparse objects requires the summing of all internal
arrays. We can test for these arrays using the nbytes attribute
"""
arrays = [a for a in vars(y).values() if hasattr(a, 'nbytes')]

# sum the bytes from all arrays

print(f"{sum(a.nbytes for a in arrays)}\nAs you can see here the non-sparse identity matrix ($x$) took 10,000 times more memory.")
# %%
import pandas as pd
import re, io

data = """
Version\tLatest micro version\tRelease date\tEnd of full support\tEnd ...
0.9\t0.9.9[2]\t1991-02-20[2]\t1993-07-29[a][2]
...
3.9\t3.9.5[60]\t2020-10-05[60]\t2022-05[61]\t2025-10[60][61]
3.10\t\t2021-10-04[62]\t2023-05[62]\t2026-10[62]
""".strip()

# %%
# slightly clean up data by removing references
data = re.sub(r'\[.+?\]', '', data)
# %%
df = pd.read_table(io.StringIO(data))
# %%
df.columns
# %%
# list versions
df['Version']

# %%
dff = pd.read_table(io.StringIO(data), dtype=dict(Version = str))
dff
# %%
print(df)
# %%
df['Release date'] = pd.to_datetime(df['Release date'])

# %%
df['Release date']
# %%
# see which month is most popular for python releases.
# run groupby() on the relese month
# then run count() on the version:
df.groupby([df['Release date'].dt.month])['Version'].count()
# %%
# pivoting and grouping
_df = pd.DataFrame(dict(
    building = ['x', 'x', 'y', 'x', 'x', 'y', 'z', 'z', 'z'],
    rooms = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c' ],
    hours = [10, 11, 12, 10, 11, 12, 10, 11, 12],
    temps = np.arange(0.0, 9.0),
))
_df
# %%
pd.pivot_table(
    _df, values = 'temps', index = ['rooms'],
    columns = ['hours'], aggfunc= np.mean
)

# %%
pd.pivot_table(
    _df, values = 'temps', index = ['building', 'rooms'],
    columns = ['hours'], aggfunc=np.mean
)


# %%
_df.groupby(pd.Grouper(key='hours')).mean()
# %%
pd_series = pd.Series(np.arange(100))

# %%
window = pd_series.rolling(10)

# %%
window.mean().dropna()
# %%
import statsmodels.api as sm
Y = np.arange(8)
X = np.ones(8)
# %%
model = sm.WLS(Y, X)

# %%
fit = model.fit()
# %%
print(f"fit params: {fit.params}\nfit tvalues: {fit.tvalues}")
# %%
import xarray as xr
ds = xr.Dataset.from_dataframe(dff)
# %%
ds.groupby('Release date.month').count()['Version']
# %%
dff.groupby([dff['Release date'].dt.month]).count()['Version']
# %%
points = np.arange(27).reshape((3, 3, 3))
triangles = np.arange(27).reshape((3, 3, 3))
ds = xr.Dataset(dict(
    triangles = (['p0', 'p1', 'p2'], triangles),
), coords=dict(
    points=(['x', 'y', 'z'], points),
))
ds
# %%
import stumpy as st
temps = np.array([22., 21., 22., 21., 22., 23.])
window_size = 3

# %%
stump = st.stump(temps, window_size)
stump

# %%
temps[0:window_size]

# %%
temps[2:2 + window_size]
# %%
