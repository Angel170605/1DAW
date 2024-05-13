# *************************
# ECUACIÓN DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:
    denom = 2 * a
    root = ((b**2) - (4 * a * c)) ** 0.5

    x1 = (-b + root) / denom
    x2 = (-b - root) / denom

    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)
