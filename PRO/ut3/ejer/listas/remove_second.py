# *************************
# NO ME INTERESAN LOS PARES
# *************************


def run(items: list) -> list:
    filter = []
    index = 0
    for item in items:
        if index % 2 == 0:
            filter.append(item)
        index += 1

    return filter


if __name__ == '__main__':
    run([1, 2, 1, 2, 1, 2])
