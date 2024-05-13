num = int(input('Introduzca un número'))

for line in range(num):
    for column in range(num):
        if column < line:
            character = 'U'
        elif line > column:
            character = 'D'
        else:
            character = 'X'
        print(character, end=' ')
    print()
