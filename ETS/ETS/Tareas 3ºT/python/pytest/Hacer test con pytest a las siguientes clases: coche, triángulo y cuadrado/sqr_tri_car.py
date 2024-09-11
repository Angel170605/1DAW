class Triangle:

    def __init__(self, bass, height):
        self.bass = bass
        self.height = height

    def calc_triangle_area(self, bass, height):
        return self.bass * self.height / 2

class Square:

    def __init__(self, bass, height):
        self.bass = bass
        self.height = height

    def calc_square_area(self, bass, height):
        return self.bass * self.height 

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.deposit = 0

    def charge_fuel(self, deposit):
        while self.deposit < 100:
            self.deposit + 20
            return f'Se ha recargado un 20% de su depósito'
        if self.deposit => 100:
            return 'No puedes llenar más el depósito'
