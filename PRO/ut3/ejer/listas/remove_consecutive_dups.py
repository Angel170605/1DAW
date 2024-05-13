# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    result = []
    for item in items:
        if result == []:
            result.append(item)
        if item != result[-1]:
            result.append(item)

    return result


if __name__ == '__main__':
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
