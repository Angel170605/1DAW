# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    values = [-num for num in numbers]
    add_inv = sum(values)
    return add_inv


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])
