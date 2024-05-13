# ***************
# PALABRA DIVERSA
# ***************


def run(words: list) -> str:

    dword = ''

    for word in words:
        if len(set(word)) > len(set(dword)):
            dword = word
        

    return dword


if __name__ == '__main__':
    run(['dictionary', 'turtle', 'flexibility', 'humanity'])