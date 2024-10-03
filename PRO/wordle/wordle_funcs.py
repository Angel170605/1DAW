import random

from data import word_list

word_list = word_list


def SetSecretWord(word_list):
    """Returns the word that the player have to guess"""
    secret_word = random.choice(word_list)
    return secret_word


def InspectWord(word):
    """Return a dict where the keys are the former letters of the word
    and the keys are the number of appareances of this letter on the
    entire word.
    At this way, it's easier to compare the secret word with the player's
    tryal word.
    Example:
        word_1 = 'jamon' --> {'j': 1, 'a': 1, 'm': 1, 'o': 1, 'n': 1}
        word_2 = 'oreos' --> {'o': 2, 'r': 1, 'e': 1, 's': 1}
        word_3 = 'hanna' --> {'h': 1, 'a': 2, 'n': 2}
    """
    # word = ''.join(sorted(l for l in (sorted(random.choice(words)))))
    splitted_word = {letter: word.count(letter) for letter in word}
    return splitted_word


def MatchMessage(num_guesses):
    if num_guesses == 6:
        intro_info = """Siento ser yo quien te lo diga, 
            pero esto es lo que sale cuando no acertaste."""
        num_guesses_message = f"""Pero chill, que te quedan
        {num_guesses} intentazos"""

    elif 2 > num_guesses < 6:
        intro_info = """Buen intento, pero no"""
        num_guesses_message = f"""Todavía te quedan 
        {num_guesses} intentos."""

    else:
        intro_info = """Mejora esas habilidades, rey"""
        num_guesses_message = f"""No es por presionar, 
        pero te quedan {num_guesses} intentos."""

        return intro_info, num_guesses_message
