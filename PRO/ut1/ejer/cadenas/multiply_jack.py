# *************************
# LA MULTIPLICACIÓN DE JACK
# *************************


def run(n: int) -> int:
    n_positive = str(n).strip('-')
    exponent = len(str(n_positive))
    result = n * (5**exponent)

    return result


if __name__ == '__main__':
    run(3)
