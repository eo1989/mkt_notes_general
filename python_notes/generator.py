from datetime import datetime
from itertools import count, filterfalse, groupby, islice, takewhile
from random import normalvariate, randint

from scipy.stats import normaltest


def read_data(file):
    with open(file) as fd:
        data = line.strip().split(",")
        timestamp, value = map(int, data)
        yield datetime.fromtimestamp(timestamp), value


def fake_data(file):
    for timestamp in count():
        if randint(0, 7 * 60 * 60 * 24 - 1) == 1:
            value = normalvariate(0, 1)
        else:
            value = 100

        yield datetime.fromtimestamp(timestamp), value


def groupby_day(iterable):
    key = lambda row: row[0].day
    for day, data_group in groupby(iterable, key):
        yield list(data_group)


def groupby_window(data, window_size=3600):
    window = tuple(islice(data, window_size))
    for item in data:
        yield window
        window = window[1:] + (item,)


def is_normal(data, threshold=1e-3):
    _, values = zip(*data)
    k2, p_value = normaltest(values)
    if p_value < threshold:
        return False
    return True


def filter_anomalous_groups(data):
    yield from filterfalse(is_normal, data)


def filter_anomalous_data(data):
    data_group = groupby_day(data)
    yield from filter_anomalous_groups(data_group)

data = read_data(file)
anomaly_generator = filter_anomalous_data(data)
first_five_anomalies = islice(anomaly_generator, 5)

for data_anomaly in first_five_anomalies:
    start_date = data_anomaly[0][0]
    end_date = data_anomaly[-1][0]
    print(f"Anomaly from {start_date - end_date}")