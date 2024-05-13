# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
    remainder = int(nif) % 23
    nif_letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
    letter_position = nif_letters[remainder]
    wnif = nif + letter_position

    return wnif


if __name__ == '__main__':
    run('78654355')
