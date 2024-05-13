# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    chars_mix = ''.join(texts)
    chars = list(chars_mix)

    return chars


if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])
