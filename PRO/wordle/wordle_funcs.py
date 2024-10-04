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


def CheckGuess(try_word, secret_word, splitted_secret_word):
    """This function is the Wordle game"""
    coincidences = ''
    emojis = ''
    for secret_letter, trial_letter in zip(list(secret_word), list(try_word)):
        if trial_letter == secret_letter and splitted_secret_word[secret_letter] > 0:
            coincidences += f'{trial_letter} '
            emojis += '🟩'
            splitted_secret_word[trial_letter] -= 1

        elif (
            trial_letter != secret_letter
            and trial_letter in splitted_secret_word.keys()
            and splitted_secret_word[trial_letter] > 0
        ):
            splitted_secret_word[trial_letter] -= 1
            coincidences += f'{trial_letter} '
            emojis += '🟧'

        elif (
            trial_letter != secret_letter
            and trial_letter not in splitted_secret_word.keys()
            or splitted_secret_word[trial_letter] == 0
        ):
            coincidences += f'{trial_letter} '
            emojis += '⬛'

    return coincidences, emojis
