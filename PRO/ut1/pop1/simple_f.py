# ********************
# UNA SENCILLA FUNCIÓN
# ********************


def run(a: int, b: int) -> float:
    function = (a**2 + b**2) - ((a * b) ** 0.5)
    F = float(f'{function:.7f}')

    return F


if __name__ == '__main__':
    run(5, 7)
