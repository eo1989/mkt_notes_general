import time

x1: float = 1.8
x2: float = -1.8
y1: float = 1.8
y2: float = -1.8
c_real: float = -0.62667
c_imag: float = -0.32193


def calc_z_serial_purepy(maxiter: int, zs: list, cs: list) -> list:
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z*z + c
            n += 1
        output[i] = n
    return output


def calc_pure_py(desired_width, max_iteration):
    x_step: float = (x2 - x1) / desired_width
    y_step: float = (y1 - y2) / desired_width

    x: list = []
    y: list = []
    ycoord: float = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord: float = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step


    zs: list = []
    cs: list = []

    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print(f"len of x: {len(x)}")
    print(f"total: {len(zs)}")

    start_time = time.time()
    output = calc_z_serial_purepy(zs, cs, max_iteration)
    end_time = time.time()
    secs = end_time - start_time
    print(f"took {calc_z_serial_purepy().__name__}", f"{secs} seconds")

    assert sum(output) == 332100980


if __name__ == "__main__":
    calc_pure_py(1_000, 300)