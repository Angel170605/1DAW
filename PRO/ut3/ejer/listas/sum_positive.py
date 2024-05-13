# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    to_sum = []
    sum_positive = 0
    for num in numbers:
        if num > 0:
            to_sum.append(num)
            sum_positive = sum(to_sum)

    return sum_positive


if __name__ == '__main__':
    run([1, -4, 7, 12])
