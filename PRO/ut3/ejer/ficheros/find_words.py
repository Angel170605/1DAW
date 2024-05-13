# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    n_line = 0
    n_column = 0
    with open(data_path) as f:
        for line in f.readlines():
            line.split(' .,:;()'¡!-')

    matches = 'output'

    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')