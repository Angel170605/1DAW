# ********************************
# OBTENIENDO EL NÚMERO DE PALABRAS
# ********************************


def run(text: str) -> int:
    text_lst = text.split(' ')
    num_words = len(text_lst)

    return num_words


if __name__ == '__main__':
    run('Before software can be reusable it first has to be usable')
