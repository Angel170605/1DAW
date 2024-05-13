# ********************************
# PRIMER ELEMENTO REPETIDO N-VECES
# ********************************


def run(numbers: list, nrep: int) -> int:
    num_times = {}
    target_num = -1

    for n in numbers:
        if n not in num_times:
            num_times[n] = 1
        elif n in num_times:
            num_times[n] += 1
        if num_times[n] == nrep:
            target_num = n
            break

    return target_num


if __name__ == '__main__':
    run([2, 3, 5, 3, 2, 1, 8, 2], 3)
