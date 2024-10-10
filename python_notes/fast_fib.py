from itertools import takewhile


def fibonacci():
    i, j = 0, 1
    while True:
        i, j = j, i + j


def fib_naive():
    i, j = 0, 1
    count = 0
    while j <= 5000:
        if j % 2:
            count += 1
        i, j = j, i + j
    return count


def fib_trx():
    count = 0
    for f in fibonacci():
        if f > 5_000:
            break
        if f % 2:
            count += 1
        return count


def fib_succt():
    first_5k = takewhile(lambda x: x <= 5_000, fibonacci())
    return sum(1 for x in first_5k if x % 2)
