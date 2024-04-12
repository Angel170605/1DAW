# ************************
# CONVERSOR DE TEMPERATURA
# ************************


def temp_converter(source: str):
    def convertion(temp: int):
        if source == 'c2f':
            result = round((temp * 1.8 + 32), 2)
            return result
        elif source == 'f2c':
            return round(((temp - 32) / 1.8), 2)
        else:
            return None

    return convertion


def run(source: str, temp: int):
    converter = temp_converter(source)
    result = converter(temp)
    return result
