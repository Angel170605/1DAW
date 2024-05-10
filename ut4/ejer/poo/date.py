from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        self.year = year
        if self.year < 1900 or self.year > 2050:
            self.year = 1900

        self.month = month
        if self.month < 1 or self.month > 12:
            self.month = 1

        self.day = day
        if self.day < 1 or self.day > Date.days_in_month(self.month, self.year):
            self.day = 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        match month:
            case 2:
                if Date.is_leap_year(year):
                    return 29
                else:
                    return 28
            case 4, 6, 9, 11:
                return 30
            case _:
                return 31

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        ...
        delta_days = self.day

        for _ in range(1, self.month):
            delta_days += Date.days_in_month(_, self.year)

        for y in range(1900, self.year):
            if Date.is_leap_year(y) and y != 1900:
                delta_days += 366
            else:
                delta_days += 365

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

        self.str_day = ''
        self.str_month = ''
        self.str_year = ''

        if 0 < self.day or self.day > 10:
            self.str_day = '1' + str(self.day)
        else:
            self.str_day = str(self.day)

        if 0 < self.month or self.month > 10:
            self.str_month = '1' + str(self.month)
        else:
            self.str_month = str(self.month)

        self.str_year = str(self.year)

        return f'{self.str_day}/{self.str_month}/{self.str_year}'

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        self.WEEK_DAYS = {
            'DOMINGO': 0,
            'LUNES': 1,
            'MARTES': 3,
            'MIÉRCOLES': 4,
            'JUEVES': 5,
            'VIERNES': 6,
            'SÁBADO': 7,
        }
        self.YEAR_MONTHS = {
            'ENERO': 1,
            'FEBRERO': 2,
            'MARZO': 3,
            'ABRIL': 4,
            'MAYO': 5,
            'JUNIO': 6,
            'JULIO': 7,
            'AGOSTO': 8,
            'SEPTIEMBRE': 9,
            'OCTUBRE': 10,
            'NOVIEMBRE': 11,
            'DICIEMBRE': 12,
        }

        self.day_name = ''
        self.month_name = ''

        for wk_day, n_weekday in self.WEEK_DAYS.items():
            if n_weekday == Date.weekday(self.day):
                self.day_name = wk_day

        for yr_month, n_year in self.YEAR_MONTHS:
            if n_year == int(self.month % 13):
                self.month_name = yr_month

        return f'{self.day_name} {self.day} DE {self.month_name} {self.year}'

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        self.total_days = days + Date.get_delta_days(self)

        self.days_to_yrs = self.total_days // 365
        self.days_to_months = (((self.total_days + self.days_to_yrs) // 4) % 365) // 31
        self.left_days = int((self.total_days % 365) % 31)

        return Date(self.left_days, self.days_to_months, self.days_to_yrs)
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días

            Para hacer esto, convierte las dos fechas en dias (ej: 16/20/2024 -> 365425168 dias), las restas, y las vuelves a pasar a fecha.

        2) Restar un número de días la fecha -> Nueva fecha

            Para hacer esto, convierte las dos fechas en dias (ej: 16/20/2024 -> 365425168 dias), las restas, y las vuelves a pasar a fecha.

        '''
        if isinstance(other, Date):
            return Date.get_delta_days(self) - Date.get_delta_days(other)

        else:
            self.total_days = Date.get_delta_days(self) - Date.get_delta_days(other)

            self.days_to_yrs = self.total_days // 365
            self.days_to_months = (((self.total_days + self.days_to_yrs) // 4) % 365) // 31
            self.left_days = int((self.total_days % 365) % 31)

            return Date(self.left_days, self.days_to_months, self.days_to_yrs)

    def __lt__(self, other) -> bool:
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False

    def __gt__(self, other) -> bool:
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                return self.day > other.day
        return False

    def __eq__(self, other) -> bool:
        return self.year == other.year and self.month == other.month and self.day == other.day
