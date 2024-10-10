import time as ti
from functools import wraps


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice

# The do_twice() decorator calls the decorated function twice.

def time_fn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = ti.time()
        result = fn(*args, **kwargs)
        t2 = ti.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time