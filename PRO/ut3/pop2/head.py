# *************************
# SIMULANDO EL COMANDO HEAD
# *************************
from pathlib import Path


def run(file: Path, n: int) -> str:
    players = []
    target_n_lines = n - 1
    with open(file) as f:
        path_lines = f.readlines()
        for item in range(len(path_lines)):
            if item <= (target_n_lines):
                players.append(path_lines[item])
            else:
                break

    lines = ''.join(players).rstrip()
    return lines


if __name__ == '__main__':
    run('data/head/nba_season22.txt', 3)
