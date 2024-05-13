# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    results = []
    with open(data_path) as f:
        for line in f:
            nums = line.strip().split()
            results.append(sum(int(num) for num in nums))
    rsum = tuple(results)

    return rsum


if __name__ == '__main__':
    run('data/sum_rows/data1.txt')
