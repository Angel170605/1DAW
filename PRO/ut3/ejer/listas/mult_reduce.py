# ************************
# MULTIPLICACIÓN EN CADENA
# ************************


def run(numbers: list) -> int:
    for num in numbers:
        num *= numbers[(num + 1)]
    rmult = num

    return rmult


if __name__ == '__main__':
    run([1, 2, 3, 4])
