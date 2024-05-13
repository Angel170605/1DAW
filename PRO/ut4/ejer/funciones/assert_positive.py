# *******************************
# ASEGURANDO ARGUMENTOS POSITIVOS
# *******************************


def check_possitive(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n > 0 and n.isnumeric():
            return n
        return 0

    return wrapper


@check_possitive
def factorial(n: int):
    # idfk
    return n
