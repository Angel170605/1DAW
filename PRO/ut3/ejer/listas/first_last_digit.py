# ****************************************
# ENCONTRANDO EL PRIMER Y EL ÚLTIMO DÍGITO
# ****************************************


def run(text: str) -> tuple:
    nums = '01234567890'
    for char in text:
        if char in nums:
            first_digit = int(char)
            break
        continue
    for char in text[::-1]:
        if char in nums:
            last_digit = int(char)
            break

    return first_digit, last_digit


if __name__ == '__main__':
    run('1abc2')
