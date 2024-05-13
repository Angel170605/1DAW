# ****************
# SUMA HETEROGÉNEA
# ****************


def run(items: list) -> int:
    to_sum = []
    for item in items:
        if item == int:
            to_sum.append(item)
        else:
            to_sum.append(int(item))

    sum_items = sum(to_sum)

    return sum_items


if __name__ == '__main__':
    run([1, '2', 3, '4', 5])
