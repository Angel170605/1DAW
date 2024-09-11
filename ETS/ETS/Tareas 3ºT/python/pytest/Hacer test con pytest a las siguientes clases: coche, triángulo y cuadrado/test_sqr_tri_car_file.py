import pytest

from sqr_tri_car import Triangle, Square, Car

@pytest.fixure():
def triangle:
    return Triangle(16, 2)
def square:
    return Square(3, 3)
def honda_civic:
    return Car('Honda', 'Civic')

def calc_tr_area_right(triangle: Triangle):
    assert triangle.calc_triangle_area() == 16

def calc_sq_area_right(square: Square):
    assert square.calc_square_area() == 9

def charge_fuel_works(honda_civic: Car):
    assert honda_civic.charge_fuel == 20

