# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    name_location = fullname.find(' ')
    name = fullname[:name_location]
    surname = fullname[name_location + 1 :]
    swapname = surname + ' ' + name

    return swapname


if __name__ == '__main__':
    run('John McClane')
