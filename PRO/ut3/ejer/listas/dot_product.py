# ****************
# PRODUCTO ESCALAR
# ****************


def run(vector1: list, vector2: list) -> float:
    dprod = 0
    for value1, value2 in zip(vector1, vector2):
        if len(vector1) != len(vector2):
            dprod = None
        if len(vector1) == len(vector2):
            dprod += int(value1) * int(value2)

    return dprod


if __name__ == '__main__':
    run([4, 3, 8, 1], [9, 2, 7, 3])
