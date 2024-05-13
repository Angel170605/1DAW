# *************************************
# CALCULANDO EL MÁXIMO CON RECURSIVIDAD
# *************************************


def rmax(items: list[int]):
    if items:
        target_max = items[0]
        for item in items:
            if item > target_max:
                target_max = item
                return rmax(items[1:])
        return target_max
