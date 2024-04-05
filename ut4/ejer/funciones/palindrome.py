# **********
# PALÍNDROMO
# **********


def is_palindrome(text):
    text_chars = [char for char in text.lower() if char != ' ']
    reversed_text = list(reversed(text_chars))
    if text_chars == reversed_text:
        return True
    else:
        return False
