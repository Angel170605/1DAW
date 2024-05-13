# ********************************
# OBTENIENDO EL NÚMERO DE PALABRAS
# ********************************


def run(text: str) -> int:
    split_sentence = text.split()

    num_words = len(split_sentence)

    return num_words


if __name__ == '__main__':
    run('Before software can be reusable it first has to be usable')
