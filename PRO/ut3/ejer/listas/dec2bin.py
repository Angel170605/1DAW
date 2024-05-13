# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    bins = []
    for value in range(num):
        if value <= 1:
            bins.append(1)
        else:
            if value % 2 == 0:
                value /= 2
                bins.append(0)
            if value % 2 != 0:
                int(value)
                value /= 2
                bins.append(1)
            if value <= 1:
                break

    to_bin = bins

    return to_bin


if __name__ == '__main__':
    run(1)
