# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    text1_elements = set(text1.lower())
    text2_elements = set(text2.lower())
    vowels = 'aeiou'
    consonants = []
    for item in text1_elements & text2_elements:
        if item.isalpha():
            if item not in vowels and item not in consonants:
                consonants.append(item)

    cconst = ''.join(sorted(consonants))

    return cconst


if __name__ == '__main__':
    run('Flat is bEtter than nested', 'Readability counts')