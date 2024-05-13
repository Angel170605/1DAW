# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    # TU CÓDIGO AQUÍ

    f = open(input_path, 'r')
    lines = f.readlines()
    num_lines = len(lines)
    num_words = 0
    num_bytes = 0
    for line in lines:
        num_bytes += len(line.encode('utf-8'))
        if line != '\n':
            num_words += len(line.split(' '))

    return num_lines, num_words, num_bytes


if __name__ == '__main__':
    run('data/wc/lorem.txt')
