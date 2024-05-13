# *********************
# DAME UN SLUG SENCILLO
# *********************


def run(text: str) -> str:
    lower_text = text.lower()
    space_to_dash = lower_text.replace(' ', '-')
    delete_acents = space_to_dash.replace('á' 'é' 'í' 'ó' 'ú', 'a' 'e' 'i' 'o' 'u')
    slug = delete_acents

    return slug


if __name__ == '__main__':
    run('hola probando')
