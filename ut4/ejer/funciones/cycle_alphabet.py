# *****************
# ALFABETO CIRCULAR
# *****************

letters = 'abcdefghijklmnopqrstuvwxyz'


def alpha_letters(letters):
    for letter in letters:
        yield letter


def run(max_letters: int) -> str:
    alpha_chars = []
    for a in range(max_letters):
        for char in alpha_letters(letters):
            alpha_chars.append(char)

    text = ''.join(alpha_chars)
    return text


if __name__ == '__main__':
    run(0)
