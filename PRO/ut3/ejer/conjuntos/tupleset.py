# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:
    firsts = set()
    seconds = set()

    for element in input:
        firsts.add(element[0])
        seconds.add(element[1])

    output = (firsts, seconds)

    return output

if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))

    