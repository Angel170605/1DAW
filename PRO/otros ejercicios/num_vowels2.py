word = input('Introduzca una palabra')
num_vowels = 0

for letter in word:
    print(letter)
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num_vowels += 1
print('El número de vocales en ' f'{word}' 'es ' f'{num_vowels}')
