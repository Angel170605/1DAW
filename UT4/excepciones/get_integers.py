def getint():
    value = int(input('Give me an integer number: '))
    try:
        value
    except ValueError:
        print('Not a valid integer. Try it again!')
        return getint((input('Give me an integer number')))
    else:
        return f'{value}'


get_integer = getint()
