num = int(input('Introduzca un número'))

while (num % ((num / 2) - 1)) != 0:
    num -= 1
    print(f'{num}' 'no es un número primo')
    if num % ((num / 2) - 1):
        print(f'{num}' 'es es un número primo')
