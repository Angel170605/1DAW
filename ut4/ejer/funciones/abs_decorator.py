# *******************************
# DECORANDO CON VALORES ABSOLUTOS
# *******************************


def f_abs(fprod):
    def wrapped(a, b):
        result = fprod(a, b)
        return abs(result)

    return wrapped


@f_abs
def fprod(a, b):
    return a * b
