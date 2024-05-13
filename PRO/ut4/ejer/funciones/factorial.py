# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n: int):
    if n < 0:
        return None
    if n == 0:
        return 1
    if n > 0:
        result = n
        for num in range(1, n):
            result *= num
        return result
