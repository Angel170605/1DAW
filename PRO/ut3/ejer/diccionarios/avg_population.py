# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:

    avg_data = {}

    total_population = [int(population) for population in pdata.values()]
    world_population = sum(total_population)
    
    for value in pdata.values():
        for element in pdata.keys():
            avg_data[element] = round(((value * 100) / world_population), 3)

    return avg_data


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})