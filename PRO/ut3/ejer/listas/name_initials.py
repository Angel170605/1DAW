# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    letters = []
    name = str((fullname[: fullname.index(',')]).capitalize)
    surname = str((fullname[fullname.index(',') :]).capitalize)

    for char in name:
        if char.isupper is True:
            letters.insert(0, char)

    for char in surname:
        if char.isupper is True:
            letters.append(char)

    initials = letters

    return initials


if __name__ == '__main__':
    run('Delgado Quintero, sergio')
