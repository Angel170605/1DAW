# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    to_sum = []
    for value in values:
        if value != sorted(values)[0] and value != sorted(values)[-1]:
            to_sum.append(value)
    tsum = sum(to_sum)

    return tsum


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])
