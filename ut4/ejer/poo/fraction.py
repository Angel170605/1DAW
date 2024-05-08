from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    def __add__(self, other: Fraction):
        den = self.den * other.den
        num = (self.num * (den // self.den)) + (other.num * (den // other.den))
        simply = Fraction.gcd(num, den)
        return Fraction((num // simply), (den // simply))

    def __sub__(self, other: Fraction):
        den = self.den * other.den
        num = (self.num * (den // self.den)) - (other.num * (den // other.den))
        simply = Fraction.gcd(num, den)
        return Fraction((num // simply), (den // simply))

    def __mul__(self, other: Fraction):
        den = self.den * other.den
        num = self.den * other.den
        simply = Fraction.gcd(num, den)
        return Fraction((num // simply), (den // simply))

    def __truediv__(self, other: Fraction):
        den = self.den * other.num
        num = self.num * other.den
        simply = Fraction.gcd(num, den)
        return Fraction((num // simply), (den // simply))

    def __str__(self) -> str:
        return f'La solucion es {self.num}/{self.den}'

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a
