# 1) Создайте класс «Прямоугольник», у которого присутствуют два поля
# (ширина и высота). Реализуйте метод сравнения прямоугольников по
# площади. Также реализуйте методы сложения прямоугольников (площадь
# суммарного прямоугольника должна быть равна сумме площадей
# прямоугольников, которые вы складываете). Реализуйте методы
# умножения прямоугольника на число n (это должно увеличить площадь
# базового прямоугольника в n раз).

class Rectangle:

    def __init__(self, high: int | float, width: int | float):
        if not isinstance(high, (int, float)) and not isinstance(width, (int, float)):
            raise TypeError
        self.high = high
        self.width = width

    def rec_area(self):
        return self.high * self.width

    def __add__(self, other):
        new_high = self.high
        new_width = other.rec_area() / new_high
        total_high = self.high
        total_width = self.width + new_width
        return Rectangle(total_high, total_width)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.high * other, self.width * other
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.rec_area() == other.rec_area()

    def __str__(self):
        res = f'[high = {self.high}, width = {self.width}]\n'
        res += f'Area = {self.rec_area()}'
        return res

rec_1 = Rectangle(4, 5)
rec_2 = Rectangle(3, 7)

print(rec_1, rec_2, sep='\n')
print(f'Equal?  {rec_1 == rec_2}')
print(f'Square = {rec_1.rec_area()}')
print(f'Summa = {rec_1 + rec_2}')
print(f'Multipy = {rec_1 * 2}')


