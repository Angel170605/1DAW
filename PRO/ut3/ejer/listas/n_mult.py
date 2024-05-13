# ********************
# CALCULANDO MÚLTIPLOS
# ********************


def run(x: int, n: int) -> list:
    # TU CÓDIGO AQUÍ
    nums = []
    for multiple in range(n + 1):
        if multiple >= 1:
            nums.insert(-1, x * multiple)

    multiples = sorted(nums)

    return multiples


if __name__ == '__main__':
    run(1, 10)
