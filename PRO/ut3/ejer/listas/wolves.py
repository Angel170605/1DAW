# **************
# EL LOBO ACECHA
# **************


def run(farm: list) -> str:
    for position in farm:
        if (
            farm[position] == 'lobo'
            and (farm[position + 1] == 'oveja' or farm[position - 1] == 'oveja')
            and farm[-1] != 'lobo'
        ):
            msg = 'Cuidado oveja' + ' ' + f'{position}' + 'el lobo te va a comer'
        if farm[-1] == 'lobo':
            msg = 'No te quiero ver más por aquí, lobo'

    return msg


if __name__ == '__main__':
    run(['oveja', 'oveja', 'lobo', 'oveja'])
