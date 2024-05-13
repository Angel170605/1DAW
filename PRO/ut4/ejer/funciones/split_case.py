# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words):
    return [word for word in words if word.islower()], [word for word in words if word.isupper()]
