import re


def is_valid_float(number: str) -> bool:
    regexp = r'-(\w)+\.{1}|-(\d)+\.{1}\w|(\d)+\.{1}\w'
    matracazo = re.search(regexp, number)
    return matracazo is not None
