# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
    numer = (4 * x) * (180 - x)
    denom = 40500 - (x * (180 - x))

    sin = numer / denom

    return sin


if __name__ == '__main__':
    run(90)
