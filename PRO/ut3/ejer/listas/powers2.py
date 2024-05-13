# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    powers2 = []
    for exponent in range(num_powers + 1):
        powers2.append(2 ** int(exponent))

    return powers2


if __name__ == '__main__':
    run(0)
