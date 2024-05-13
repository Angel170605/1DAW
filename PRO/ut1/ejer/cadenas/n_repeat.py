# *************
# SUMA REPETIDA
# *************


def run(n: int) -> int:
    n_mult = n * 10
    basic_calc = n_mult + n
    result = n + basic_calc + (n * 100 + basic_calc)
    return result


if __name__ == '__main__':
    run(3)
