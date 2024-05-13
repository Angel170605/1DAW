# **************
# AÑOS BISIESTOS
# **************


def run(year: int) -> bool:
    is_leap_year = True if (year / 400) == int else False
    return is_leap_year


if __name__ == '__main__':
    run(1900)
