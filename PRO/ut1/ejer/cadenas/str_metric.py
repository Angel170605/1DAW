# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    n_letters = len(text)
    n_vocals = (
        text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    )

    metric = n_letters * n_vocals
    return metric


if __name__ == '__main__':
    run('ordenador')
