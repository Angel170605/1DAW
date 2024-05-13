# ******************
# DISTANCIA EUCLÍDEA
# ******************


def run(x1: float, y1: float, x2: float, y2: float) -> float:
    x_square = (x1 - x2) ** 2
    y_square = (y1 - y1) ** 2

    distance = (x_square + y_square) ** 0.5

    return distance


if __name__ == '__main__':
    run(3, 5, -7, -4)
