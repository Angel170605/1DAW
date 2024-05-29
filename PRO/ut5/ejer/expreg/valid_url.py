import re


def is_valid_url(url: str) -> bool:
    regexp = r'^http[s]?://'
    is_valid_url = re.search(regexp, url)
    return is_valid_url is not None
