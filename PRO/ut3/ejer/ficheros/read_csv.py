# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:

    f = open(datafile, 'r')
    clean_data = [(line.strip()).split(',') for line in f.readlines()]
    data = []
    data_keys = [item for item in clean_data[0]]
    poke_data = [item for item in clean_data[1:]]
    for poke in poke_data:
        pokemon = {}
        for stat, stat_key in zip(poke, data_keys):
            if stat == '':
                stat = None
            elif stat == 'True':
                stat = True
            elif stat == 'False':
                stat = False
            elif stat.isnumeric():
                stat = int(stat)
            pokemon[stat_key] = stat
        data.append(pokemon)

    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')
