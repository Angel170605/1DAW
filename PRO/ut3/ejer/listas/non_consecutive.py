# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    refree = values[0]
    target = 0
    for value in values:
        if len(values) > 1:
            if value > 0:
                refree += 1
                if value != refree:
                    target = value
                else:
                    target = None
            if value < 0:
                refree -= 1
                if value != refree:
                    target = value
                else:
                    target = None
        else:
            target = None

    return target


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])
