# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    text = (text.strip(' ')).lower()
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False
