# ***************
# EDADES CRUZADAS
# ***************


def run(mother_age: int, daughter_age: int) -> tuple:
    target_mother_age = 0
    target_daughter_age = 0
    while mother_age == (2 * daughter_age):
        target_mother_age += 1
        target_daughter_age += 1
        if mother_age == (2 * daughter_age):
            target_mother_age = mother_age
            target_daughter_age = daughter_age
            break
        else:
            target_mother_age -= 1
            target_daughter_age -= 1
            if mother_age == (2 * daughter_age):
                target_mother_age = mother_age
                target_daughter_age = daughter_age
                break

    return target_mother_age, target_daughter_age


if __name__ == '__main__':
    run(67, 23)
