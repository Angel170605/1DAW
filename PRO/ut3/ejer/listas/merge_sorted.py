# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    for num_1, num_2 in zip(values1, values2):
        if num_1 == num_2:
            merged.append(num_1)
    merged = 'output'

    return merged


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])