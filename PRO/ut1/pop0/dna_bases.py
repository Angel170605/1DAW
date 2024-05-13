# ********************
# EN LAS BASES DEL ADN
# ********************


def run(dna: str) -> tuple:
    n_adenines = dna.count('A')
    n_guanines = dna.count('G')
    n_thymines = dna.count('T')
    n_cytosines = dna.count('C')
    dna_length = len(dna)
    adenines_rate = 100 * n_adenines / dna_length
    guanines_rate = 100 * n_guanines / dna_length
    thymines_rate = 100 * n_thymines / dna_length
    cytosines_rate = 100 * n_cytosines / dna_length
    'output'

    return adenines_rate, guanines_rate, thymines_rate, cytosines_rate


if __name__ == '__main__':
    run('GGTTACCAACCCAGTCGAAAATTTGGTCAGGG')
