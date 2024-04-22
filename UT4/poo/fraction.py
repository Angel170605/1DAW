from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    def __add__(self, other: Fraction):
        den = self.den * other.den
        num = (self.num * (den / self.den)) + (other.num * (den / other.den))
        return Fraction(num, den)

    def __sub__(self, other: Fraction):
        den = self.den * other.den
        num = (self.num * (den / self.den)) + (other.num * (den / other.den))
        return Fraction(num, den)

    def __mul__(self, other: Fraction):
        den = self.den * other.den
        num = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other: Fraction):
        den = self.den * other.num
        num = self.num * other.den
        return Fraction(num, den)

    def __str__(self):
        return f''

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a
