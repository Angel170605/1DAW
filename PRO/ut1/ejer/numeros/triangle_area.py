# ********************
# ÁREA DE UN TRIÁNGULO
# ********************


def run(base: float, height: float) -> float:
    base_height = base * height

    area = base_height / 2

    return area


if __name__ == '__main__':
    run(3, 3)
