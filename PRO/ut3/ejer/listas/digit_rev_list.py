# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    # TU CÓDIGO AQUÍ
    digits = []
    for num in str(number):
        digits.insert(0, int(num))

    rev_digits = digits
    return rev_digits


if __name__ == '__main__':
    run(35231)
