# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
   
    hex_items = [chr(int(code, 16)) for code in hex_codes]
    text = ''.join(hex_items)

    return text


if __name__ == '__main__':
    run(['1f49a', '2728', '1f389', '1f3c6'])