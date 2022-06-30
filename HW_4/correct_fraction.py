# Создайте класс «Правильная дробь» и реализуйте методы сравнения,
# сложения, вычитания и произведения для экземпляров этого класса.

from fractions import Fraction


class CorrectFraction:

    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return f'Summa: {Fraction(self.numerator, self.denominator) + Fraction(other.numerator, other.denominator)}'

    def __sub__(self, other):
        return f'Subtraction: {Fraction(self.numerator, self.denominator) - Fraction(other.numerator, other.denominator)}'

    def __mul__(self, other):
        return f'Multipy: {Fraction(self.numerator, self.denominator) * Fraction(other.numerator, other.denominator)}'

    def __eq__(self, other):
        return f'Equal?: {Fraction(self.numerator, self.denominator) == Fraction(other.numerator, other.denominator)}'

    def __ne__(self, other):
        return f'Equal?: {Fraction(self.numerator, self.denominator) != Fraction(other.numerator, other.denominator)}'

    def __gt__(self, other):
        return f'Equal?: {Fraction(self.numerator, self.denominator) > Fraction(other.numerator, other.denominator)}'

    def __lt__(self, other):
        return f'Equal?: {Fraction(self.numerator, self.denominator) < Fraction(other.numerator, other.denominator)}'

    def __ge__(self, other):
        return f'Equal?: {Fraction(self.numerator, self.denominator) >= Fraction(other.numerator, other.denominator)}'

    def __le__(self, other):
        return f'Equal?: {Fraction(self.numerator, self.denominator) <= Fraction(other.numerator, other.denominator)}'

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

fr_1 = CorrectFraction(1, 7)
fr_2 = CorrectFraction(2, 5)
print(fr_1 + fr_2)
print(fr_1 - fr_2)
print(fr_1 * fr_2)
print(fr_1 == fr_2)
print(fr_1, fr_2)
print(fr_1 != fr_2)