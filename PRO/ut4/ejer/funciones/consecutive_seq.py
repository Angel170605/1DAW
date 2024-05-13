# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(items: int, target_count):
    nums_appears = {}
    for item in items:
        if item not in nums_appears.items():
            nums_appears[item] = 0
        else:
            nums_appears[item] += 1
