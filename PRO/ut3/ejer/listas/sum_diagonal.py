# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    nums_to_sum = []
    for index in range(len(matrix)):
        nums_to_sum.append(matrix[index][index])

    sum_diagonal = sum(nums_to_sum)

    return sum_diagonal


if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])
