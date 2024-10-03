from data import word_list
from match_messages import *
from wordle_funcs import *

print(start_message)

secret_word = SetSecretWord(word_list)  # random.choice de un str de una lista
guesses_left = 6


for _ in range(guesses_left):
    try_word = input('Dime una palabra: ')
    splitted_secret_word = InspectWord(secret_word)
    coincidences = []
    emojis = []

    if try_word == 'exit':
        print(f"""Adiós
              
              
              
              PD: La palabra era {secret_word}""")
        break

    elif try_word == secret_word:
        print(win_message)
        break

    else:
        for secret_letter, trial_letter in zip(list(secret_word), list(try_word)):
            if trial_letter == secret_letter and splitted_secret_word[secret_letter] > 0:
                coincidences.append(trial_letter)
                emojis.append('🟩')
                splitted_secret_word[trial_letter] -= 1

            elif (
                trial_letter != secret_letter
                and trial_letter in splitted_secret_word.keys()
                and splitted_secret_word[trial_letter] > 0
            ):
                splitted_secret_word[trial_letter] -= 1
                coincidences.append(trial_letter)
                emojis.append('🟧')

            elif (
                trial_letter != secret_letter
                and trial_letter not in splitted_secret_word.keys()
                or splitted_secret_word[trial_letter] == 0
            ):
                coincidences.append(trial_letter)
                emojis.append('⬛')

            if guesses_left == 1:
                print(f"""Bien jugado rey 🫡
              
              
              
              
              PD: La palabra era {secret_word}""")
                break

        print(f"""
 ######################################################################
 ######################### INFO DE LA PARTIDA #########################
 ######################################################################
  
                Coincidencias: 
                
                    {coincidences}
                    {emojis}

                Te quedan {(guesses_left -1)} intentos

 ######################################################################
 ######################################################################
 ######################################################################
 """)

        guesses_left -= 1
