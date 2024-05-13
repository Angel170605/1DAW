# *************************
# QUITANDO PRIMERO Y ÚLTIMO
# *************************


def run(text: str) -> str:
    first_character = text[0]
    last_character = text[-1]
    at_second = text.strip(first_character)
    stext = at_second.strip(last_character)

    return stext


if __name__ == '__main__':
    run('What can I do')
