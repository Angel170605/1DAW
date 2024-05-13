# *********************
# VALOR MÁXIMO Y MÍNIMO
# *********************


def run(values: list) -> tuple:
    max = [0]
    min = [0]
    for value in values:
        if value < min[0]:
            min[0] = value
        if value > max[0]:
            max[0] = value
        if len(values) == 1:
            max[0] = value
            min[0] = value
    max_value = max[0]
    min_value = min[0]

    return max_value, min_value


if __name__ == '__main__':
    run([4, 6, 2, 1, 9, 63, -134, 566])
