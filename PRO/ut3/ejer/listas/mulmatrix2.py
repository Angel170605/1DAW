# *****************************
# MULTIPLICANDO MATRICES DE 2X2
# *****************************


def run(A: list, B: list) -> list:
    first_element = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    second_element = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    third_element = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    fourth_element = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    line1 = [first_element, second_element]
    line2 = [third_element, fourth_element]
    P = [line1, line2]

    return P


if __name__ == '__main__':
    run([[6, 4], [8, 9]], [[3, 2], [1, 7]])
