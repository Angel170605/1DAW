# ********************
# REORGANIZANDO FECHAS
# ********************


def run(input_date: str, base_year: int) -> str:
    date_lst = input_date.split('/')
    year = base_year + int(date_lst[2])
    month = int(date_lst[0])
    day = int(date_lst[1])

    output_date = f'{day:02d}-{month:02d}-{year}'

    return output_date


if __name__ == '__main__':
    run('12/31/23', 2000)
