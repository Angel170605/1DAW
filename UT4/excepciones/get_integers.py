n = int(input('Give me a integer number: '))


def getint(n: int) -> int:
    try:
        if isinstance(n, int):
            return n
    except ValueError:
        print(f'''Not a valid integer. Try it again!''')
        n = input('Give me a integer number: ')
        return getint(n)


forza_barça = getint(n)
