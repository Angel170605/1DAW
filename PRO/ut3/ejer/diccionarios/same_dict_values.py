# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    same = []
    all_same = True
    for item in items.values():
        if item not in same:
            same.append(item)
            if len(same) <= 1:
                all_same = True
            if len(same) > 1:
                all_same = False

    return all_same


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})