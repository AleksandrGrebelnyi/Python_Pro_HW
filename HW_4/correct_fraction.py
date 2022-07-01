# Создайте класс «Правильная дробь» и реализуйте методы сравнения,
# сложения, вычитания и произведения для экземпляров этого класса.

class CorrectFraction:

    def __init__(self, numerator: int, denominator: int):
        if isinstance(numerator, float) or isinstance(denominator, float):
            raise TypeError
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(self, float) and isinstance(other, float):
            return NotImplemented
        else:
            return CorrectFraction(self.numerator * other.denominator + other.numerator * self.denominator,
                                self.denominator * other.denominator)

    def __sub__(self, other):
        return CorrectFraction(self.numerator * other.denominator - other.numerator * self.denominator,
                               self.denominator * other.denominator)

    def __mul__(self, other):
        return CorrectFraction(self.numerator * other.numerator, other.denominator * self.denominator)

    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __ne__(self, other):
        return self.numerator / self.denominator != other.numerator / other.denominator

    def __gt__(self, other):
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __lt__(self, other):
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __ge__(self, other):
        return self.numerator / self.denominator >= other.numerator / other.denominator

    def __le__(self, other):
        return self.numerator / self.denominator <= other.numerator / other.denominator

    def __str__(self):
        if self.numerator < self.denominator:
            return f'Correct fraction {self.numerator} / {self.denominator}\n'
        else:
            return f'Incorrect fraction {self.numerator} / {self.denominator}'

fr_1 = CorrectFraction(1, 3)
fr_2 = CorrectFraction(2, 6)
print('Plus = ', fr_1 + fr_2)
print('Minus = ', fr_1 - fr_2)
print('Multipy = ', fr_1 * fr_2)
print('Equal? ', fr_1 == fr_2)
print(fr_1, fr_2)
print('Not equal? ', fr_1 != fr_2)