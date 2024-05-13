# ****************
# SE PONE EN VERDE
# ****************


def run(color: str) -> str:
    match color:
        case '🟢':
            new_color = '🟠'
        case '🟠':
            new_color = '🔴'
        case '🔴':
            new_color = '🟢'

    return new_color


if __name__ == '__main__':
    run('🟢')
