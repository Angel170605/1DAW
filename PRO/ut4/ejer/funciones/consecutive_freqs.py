# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items: list, as_string: bool):
    freq = 0
    freqs = {}
    if len(items) > 0:
        target_item = items[0]
        for item in items:
            if item != target_item:
                freqs[item] = freq
                freq = 1
                target_item = item
            else:
                freq += 1
        if as_string == False:
            return [tuple((k, v)) for k, v in freqs.items()]
        else:
            output = [f'{k}:{v},' for k, v in freqs.items()]
            return ''.join(output)
    else:
        if as_string == False:
            freqs = []
        else:
            freqs = ''
        return freqs
