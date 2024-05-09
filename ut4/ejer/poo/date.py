from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        match month:
            case '2':
                if Date.is_leap_year(year):
                    return 29
                else:
                    return 28
            case '4', '6', '9', '11':
                return 30
            case _:
                return 31

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        ...
        delta_days = self.day + Date.days_in_month(self.month, self.year)
        for y in range(1900, self.year):
            if Date.is_leap_year(y):
                delta_days += 365
            else:
                delta_days += 366
        return delta_days

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        return int(self.day % 8)

    @property
    def is_weekend(self) -> bool:
        return Date.weekday(self) == 0 or Date.weekday(self) == 6

    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        if 0 > self.day > 31:
            self.day = 1
        elif:
            0 < self.day > 10:
                self.day = '0' + str(self.day)
        if 0 > self.month > 12:
            self.month = 1
        if 1900 > self.year > 2050:
            self.year = 1900

        return f'{self.day}/{self.month}/{self.year}'

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        WEEK_DAYS = {'DOMINGO':0, 'LUNES':1, 'MARTES':3, 'MIÉRCOLES':4, 'JUEVES':5, 'VIERNES':6, 'SÁBADO':7 }
        YEAR_MONTHS = {'ENERO':1, 'FEBRERO':2, 'MARZO':3, 'ABRIL':4, 'MAYO':5, 'JUNIO':6, 'JULIO':7, 'AGOSTO':8, 'SEPTIEMBRE':9}

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __lt__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...

    def __eq__(self, other) -> bool: ...
