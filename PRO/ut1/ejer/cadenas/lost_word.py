# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    posit = text.find(target_word)
    word = int(posit)
    first_part = text[:posit]
    second_part = text[posit:]

    mtext = first_part + replace_word + second_part

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')
