# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    dif_items = []
    for item in items:
        if item not in dif_items:
            dif_items.append(item)
    if len(dif_items) == 1:
        all_same = True
    else:
        all_same = False

    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])
