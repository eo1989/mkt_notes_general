import time as ti

# fake profile decorator
if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        return func

@profile
def calc_z_serial_purepy(max_iter, zs, cs):
    with profile.timestamp("create_output_list"):
        output = [0] * len(zs)
    ti.sleep(0)
    with profile.timestamp("calculate_output"):
        for i in range(len(zs)):
            n = 0; z = zs[i]; c = cs[i]
            while n < max_iter and abs(z) < 2:
                z = z*z + c
                n += 1
            output[i] = n
    return output


def fn_expressive(upper = 1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total


def fn_terse(upper = 1_000_000):
    return sum(range(upper))


assert fn_expressive() == fn_terse(), f"expect identical results from both functions"  # debug me


def test_some_func():
    assert some_fn(2) == 4
    assert some_fn(1) == 1
    assert some_fn(-1) == 1


@profile
def some_fn(x):
    ti.sleep(1)
    return x**2


if __name__ == "__main__":
    print(f"some_fn(2) == {some_fn(2)}")