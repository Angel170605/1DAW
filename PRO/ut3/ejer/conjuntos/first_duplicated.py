# *************************
# PRIMER ELEMENTO DUPLICADO
# *************************


def run(numbers: list) -> int:
    fdup = -1
    unique_n = []

    for number in numbers:
        if number not in unique_n:
            unique_n.append(number)
        else:
            fdup = number
            break

    return fdup


if __name__ == '__main__':
    run([2, 3, 5, 3, 2])
