word = input('Introduzca una palabra ')
num_vowels = 0

for letter in word:
    print(letter)
    if (
        letter == 'a'
        or letter == 'á'
        or letter == 'e'
        or letter == 'é'
        or letter == 'i'
        or letter == 'í'
        or letter == 'o'
        or letter == 'ó'
        or letter == 'u'
        or letter == 'ú'
    ):
        num_vowels += 1
print('El número de vocales en ' f'{word} ' + ' ' + ' es ' f'{num_vowels}')
