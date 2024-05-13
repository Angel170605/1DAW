# *********************
# VOLUMEN DE UNA ESFERA
# *********************


def run(radius: float) -> float:
    frac = 4 / 3
    pi = 3.14
    pi_frac = frac * pi
    rad_cube = radius**3

    volume = pi_frac * rad_cube

    return volume


if __name__ == '__main__':
    run(5)
