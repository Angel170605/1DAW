# ****************
# CONTEO REGRESIVO
# ****************


def run(n: int) -> list:
    rev_nums = []
    while n >= 1:
        rev_nums.append(n)
        n -= 1

    return rev_nums


if __name__ == '__main__':
    run(5)
