# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    locations = cinfo.split(';')

    cities = {}

    for location in locations:
        target_location = tuple(str(locations).split(':'))
        city_name, city_info = target_location

        cities[city_name] = city_info


    return cities


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')