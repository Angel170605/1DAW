import pytest

from maths import Calculator

@pytest.fixure():
def calculator:
    return Calculator(16, 2)

def add_works(calculator: Calculator):
    assert calculator.add() == 18

def sub_works(calculator: Calculator):
    assert calculator.sub() == 14

def mul_works(calculator: Calculator):
    assert calculator.mul() == 32

def div_works(calculator: Calculator):
    assert calculator.div() == 8

@pytest.fixure():
def calculator2:
    return Calculator(14, 7)

def add_works(calculator2: Calculator):
    assert calculator.add() == 21

def sub_works(calculator2: Calculator):
    assert calculator.sub() == 7

def mul_works(calculator2: Calculator):
    assert calculator.mul() == 98

def div_works(calculator2: Calculator):
    assert calculator.div() == 2