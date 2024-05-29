import re

"""
    ('3.14', True),
    ('-5.', True),
    ('3e2', True),
    ('3.54_000_321', True),
    ('.5', True),
    ('-0.5', True),
    ('-.5', False),
    ('3', False),
    ('-5', False),
    ('3e2.5', False),

    ([^[-]?\d]?\.{1}[\d])

"""


def is_valid_float(number: str) -> bool:
    regexp = r'^[-]?\d]?\.{1}[\d]?|^\.\d|^\d[e]\d$'
    return re.fullmatch(regexp, number) is not None
