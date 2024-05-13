# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: tuple, target: int) -> int:
    """
    Count how many times appears the target number in a tuple.

    :param items: tuple that contains the numbers to count
    :type items: tuple.
    :param target: the number whose apppareances in the tuple will be counted.
    :type target: int

    :return :count: Number of appears of 'target' in 'items'.
    :rtype: int

    """

    count = 0
    for item in items:
        if item == target:
            count += 1

    return count
    # TU CÓDIGO AQUÍ
