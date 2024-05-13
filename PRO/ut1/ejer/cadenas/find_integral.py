# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
    position = symbol.find(',')
    first_num = symbol[:position]
    second_num = symbol[position:]
    exponent = int(second_num[1:])
    coeficient = exponent / int(first_num) + int(1)
    integral = str(f'{coeficient}'x^{exponent})
    return integral


if __name__ == '__main__':
    run('3,2')
