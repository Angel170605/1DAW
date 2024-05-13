# *******************
# NÚMERO EN INTERVALO
# *******************


def in_range(value: int, lower_limit: int, upper_limit: int) -> bool:
    interval_numbers = [lower_limit, upper_limit]
    while lower_limit < upper_limit:
        lower_limit += 1
        interval_numbers.append(lower_limit)
        if value in interval_numbers:
            return True
        if lower_limit == upper_limit:
            return False
    return True
