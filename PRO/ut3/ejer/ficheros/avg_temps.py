# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    # TU CÓDIGO AQUÍ
    media_temps = []

    f = open(input_path, 'r')
    for line in f:
        month = line.split(',')
        for temp in month:
            media_temps.append(str(round((sum((int(temp) for temp in month))) / len(month), 2)))

    n = open(output_path, 'a')
    for media_temp in media_temps:
        n.write(media_temp + '\n')

    f.close()
    n.close()

    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')
