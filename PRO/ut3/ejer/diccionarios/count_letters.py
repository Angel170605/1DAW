# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = {}
    for letter in sentence:
        if letter not in counter:
            counter[letter] = 0
        if letter in counter:
            counter[letter] +=1
    

    return counter


if __name__ == '__main__':
    run('boom')