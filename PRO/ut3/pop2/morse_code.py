# ************
# CÓDIGO MORSE
# ************
from pathlib import Path


def run(morse_signals: Path, sentence: str) -> str:
    translation = []
    translator = {}
    with open(morse_signals) as f:
        for lines in f:
            line = lines.strip('\n')
            translator[line[0]] = line[2:]

    for char in sentence.upper():
        for alpha_l, morse_l in translator.items():
            if char.isalpha() and char == alpha_l:
                translation.append(morse_l + ' ')

    morse_sentence = (''.join(translation)).rstrip(' ')

    return morse_sentence


if __name__ == '__main__':
    run('data/morse_code/signals.morse', 'hello, world!')
