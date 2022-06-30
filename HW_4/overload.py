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

    def rec_square(self):
        return self.high * self.width

    def __str__(self):
        res = f'[high = {self.high}, width = {self.width}]\n'
        # res += f'Square of rectangle is: {self.rec_square()}\n'
        return res

    def __add__(self, other):
        return self.high + other.high, self.width + other.width

    def __mul__(self, other):
        if isinstance(other, int):
            return self.high * other, self.width * other
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.rec_square() == other.rec_square()

rec_1 = Rectangle(4, 5)
rec_2 = Rectangle(4, 7)
rec_3 = Rectangle(8, 12)
print(rec_1, rec_2, rec_3, sep='\n')
print(f'Equal?  {rec_1 == rec_2}')
print(f'Square: {rec_1.rec_square()}')
print(f'Summa {rec_1 + rec_2}')

print(rec_1 * 2)

