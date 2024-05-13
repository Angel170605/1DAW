# *************************
# CONTANDO LETRAS Y DÍGITOS
# *************************


def run(text: str) -> tuple:
    new_text = (
        (text.lower())
        .replace('a', 'á')
        .replace('e', 'é')
        .replace('i', 'í')
        .replace('o', 'ó')
        .replace('u', 'ú')
    )
    num_letters = 0
    num_digits = 0
    for characters in text:
        if (
            'a'
            or 'b'
            or 'c'
            or 'd'
            or 'e'
            or 'f'
            or 'g'
            or 'h'
            or 'i'
            or 'j'
            or 'k'
            or 'l'
            or 'm'
            or 'n'
            or 'ñ'
            or 'o'
            or 'p'
            or 'q'
            or 'r'
            or 's'
            or 't'
            or 'u'
            or 'v'
            or 'w'
            or 'x'
            or 'y'
            or 'z' in text
        ):
            num_letters += 1
            num_digits += 0
        if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in text:
            num_digits += 1
            num_letters += 0
        else:
            num_letters += 0
            num_digits += 0

    return num_letters, num_digits


if __name__ == '__main__':
    run('pycheck 1.2.35')
