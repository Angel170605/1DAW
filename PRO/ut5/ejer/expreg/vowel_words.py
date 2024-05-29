import re


def extract_vowel_words(text: str) -> list[str]:
    # Escriba un programa en Python que encuentre todas las palabras que comiencen por vocal en un texto dado
    regexp = r'\b[aeiou]\w*'
    return re.findall(regexp, text, re.I)
