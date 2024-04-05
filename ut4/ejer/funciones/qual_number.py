# ********************
# CUALIFICANDO NÚMEROS
# ********************


def run(number: int) -> str:
    """
    Put the related commas in a number, to make it easier to read.

    :param number: The imput number.
    :type number: int
    :param split_number: A list where the numbers and commas will be introduced.
    :type split_number: list
    :param count: The counter to calculate where the commas wear.
    :type count: int
    :param rev_number: The imput number converted into a reversed list to make the commas introducing easier to do.
    :type rev_number: list[str]

    :return :qnumber: The imput number with their correspondent commas.
    :rtype: str
    """

    qnumber = ''
    split_number = []
    count = 0
    rev_number = reversed(list(str(number)))

    for char in rev_number:
        split_number.insert(0, char)
        count += 1
        if count % 3 == 0:
            split_number.insert(0, ',')

    qnumber = (''.join(split_number)).lstrip(',')
    return qnumber


if __name__ == '__main__':
    run(1)
