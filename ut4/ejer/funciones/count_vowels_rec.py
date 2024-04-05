# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text):
    return len([letter for letter in text if letter in 'aeiou'])
