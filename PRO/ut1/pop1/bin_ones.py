# ***************************
# LOS UNOS CUENTAN EN BINARIO
# ***************************


def run(number: int) -> int:
    bin_number = bin(number)
    count_ones = bin_number.count('1')

    return count_ones


if __name__ == '__main__':
    run(99)
