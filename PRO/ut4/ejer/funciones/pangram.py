# ********
# PANGRAMA
# ********


def is_pangram(text):
    letters = []
    for letter in text.lower():
        if letter.isalpha() and letter not in letters:
            letters.append(letter)

    if len(letters) == 26:
        return True
    else:
        return False
