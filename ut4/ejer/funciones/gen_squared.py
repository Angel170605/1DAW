# *******************
# GENERANDO CUADRADOS
# *******************


def gen_sq(n):
    """
    Gen the square of the numbers from 0 to 'n'.

    :param n: Limit number of the square generator.
    :type n: int
    :param gen_nums: The squared number generator. I takes each number between 0 and 'n' and calculates its square.
    :type gen_nums: Generator

    :return :sqared: List of each squared number from gen_nums(n).
    :rtype: list[int].
    """
    gen_nums = (value**2 for value in range(0, n))
    squared = [n for n in gen_nums]
    return squared
