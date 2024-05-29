import re


def is_valid_email(email: str) -> bool:
    regexp = r'\w[-]?*[@]\d\.*'
    email_validate = re.search(regexp, email)
    return email_validate is not None
