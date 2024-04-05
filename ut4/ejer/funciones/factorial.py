# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n: int):
    if n < 0:
        return None
    result = 1
    if n == 0:
        return 1
    for num in range(1, n + 1):
        result *= num
        return result
