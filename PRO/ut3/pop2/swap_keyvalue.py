# ****************************************
# INTERCAMBIAR CLAVE-VALOR EN DICCIONARIOS
# ****************************************


def run(data: dict) -> dict:

    swapped_data = {v: k for k, v in data.items()}

    return swapped_data


if __name__ == '__main__':
    run({'a': 1, 'b': 2, 'c': 3})
