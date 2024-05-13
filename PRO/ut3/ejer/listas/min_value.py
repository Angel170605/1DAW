# ************
# VALOR MÍNIMO
# ************


def run(values: list) -> int:
    min = [0]
    for value in values:
        if value < min[0]:
            min[0] = value
    min_value = int(min[0])

    return min_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])
