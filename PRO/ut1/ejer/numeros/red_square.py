# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    pi = 3.14
    perim = 4 * arc_A
    ratio = perim / (2 * pi)

    area = ratio**2

    return area


if __name__ == '__main__':
    run(1)
