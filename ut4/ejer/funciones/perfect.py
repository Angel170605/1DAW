# *****************
# NÚMEROS PERFECTOS
# *****************


def calc_divisors(n: int) -> list[int]:
    return [num for num in range(1, n - 1) if n % num == 0]


def is_perfect(n: int) -> bool:
    if sum(calc_divisors(n)) == n:
        return True
    else:
        return False
