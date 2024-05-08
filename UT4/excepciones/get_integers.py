def getint(value):
    try:
        result = int(value)
    except ValueError:
        print('Not a valid integer. Try it again!')
        return getint((input('Give me an integer number: ')))
    else:
        return f'{result}'


value = input('Give me an integer: ')
get_integer = getint(value)
