from data import word_list
from match_messages import *
from wordle_funcs import *

print(start_message)

start = str(input('¿Qué quieres hacer?: '))

if start == '1':
    print(instructions)
if start == '2':
    exit()

secret_word = SetSecretWord(word_list)  # random.choice de un str de una lista
guesses_left = 6

for _ in range(guesses_left):
    try_word = input('Intenta adivinar la palabra secreta: ').lower()
    splitted_secret_word = InspectWord(secret_word)
    coincidences = ''
    emojis = ''
    lifes = '❤️ ' * guesses_left

    if try_word == 'exit':
        print(f"""Adiós
              
              
              
              PD: La palabra era {secret_word}""")
        break

    elif try_word == secret_word:
        print(win_message)
        break

    else:
        coincidences, emojis = CheckGuess(try_word, secret_word, splitted_secret_word)
        guesses_left -= 1

    if guesses_left > 0:
        print(f"""
######################################################################
#########################   W O R D L E ##############################
###################################################################### 
  
                    --  INFO DE LA PARTIDA -- 
                
                          {coincidences}
                          {emojis}

                        VIDAS RESTANTES:
                            
                          {lifes}
                        
                    -- INFO DE LA PARTIDA --

######################################################################
#########################   W O R D L E ##############################
###################################################################### 
 """)

    else:
        print(lose_message)
        print(f'PD: La palabra era: {secret_word}')
