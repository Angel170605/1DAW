# *******************
# SEPARANDO EL TIEMPO
# *******************


def run(seconds: int) -> tuple:
    hours = int(seconds / 3600)
    total_time_hours = seconds / 3600
    hours_rest = total_time_hours - hours

    total_time_minutes = hours_rest * 60
    minutes = int(hours_rest * 60)
    minutes_rest = total_time_minutes - minutes

    seconds = round(minutes_rest * 60)

    return hours, minutes, seconds


if __name__ == '__main__':
    run(31256)
