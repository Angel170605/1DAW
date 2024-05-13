# *********************
# ENCONTRANDO ISOGRAMAS
# *********************


def run(text: str) -> bool:
    isogram = list()
    for char in text:
        if char.isalpha():
            if char not in isogram:
                isogram.append(char)
        else:
            isogram.append(char)
    if len(isogram) == len(text):
        is_isogram = True
    if len(isogram) < len(text):
        is_isogram = False

    return is_isogram


if __name__ == '__main__':
    run('lumberjacks')
