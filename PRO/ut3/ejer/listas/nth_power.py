# *************
# N ELEVADO A N
# *************


def run(values: list, power: int) -> int:
    result = 0
    for value in values:
        if power == len(values):
            result = -1
        if power < len(values):
            if power == values.index(value):
                result = value**power
                break

    return result


if __name__ == '__main__':
    run([1, 2, 3, 4], 2)
