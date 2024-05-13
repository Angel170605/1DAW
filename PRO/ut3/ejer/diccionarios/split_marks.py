# *********************
# CADA NOTA EN SU SITIO
# *********************


def run(marks: dict) -> tuple:
    passed = {}
    failed = {}

    for key, value in marks.items():
        if value >= 5:
            passed[str(key).upper()] = value
        elif value < 5:
            failed[str(key).lower()] = value

    return passed, failed


if __name__ == '__main__':
    run({'Ana': 4, 'Domingo': 7, 'Eva': 5, 'Álvaro': 3, 'Juan': 8, 'Belén': 1})