# ********************
# DESPLAZANDO LA VOCAL
# ********************


def run(target_vowel: str, target_offset: int, input_text: str) -> str:
    vowels = 'aeiou'

    new_vowel_position = vowels.find(target_vowel) + target_offset
    new_vowel = str(vowels[new_vowel_position])
    output_text = input_text.replace(target_vowel, new_vowel)

    return output_text


if __name__ == '__main__':
    run('e', 2, 'diferencia')
