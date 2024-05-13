# *****************
# INTERÉS COMPUESTO
# *****************


def run(amount: float, rate: float, years: int) -> float:
    int_type = 1 + rate / 100
    interest = int_type**years

    future_amount = amount * interest

    return future_amount


if __name__ == '__main__':
    run(10000, 3.5, 7)
