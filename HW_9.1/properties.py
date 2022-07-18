# Реализуйте свойство класса, которое обладает следующим
# функционалом: при установке значения этого свойства в файл с заранее
# определенным названием должно сохранятся время (когда устанавливали
# значение свойства) и установленное значение.

from datetime import datetime

class Car:

    def __init__(self, model: str, __price: int):
        self.model = model
        self.__price = __price

    def __str__(self):
        return f"Car: model = {self.model}, price = {self.__price}"

    price = property()

    @price.getter
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value
        with open('Price.txt', 'a') as f:
            f.write(f'Price: {value}, data: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}\n')


car_1 = Car('Reno', 45_000)
print(car_1)
car_1.model = 'BMW'
print(car_1)
car_1.__price = 47_000
print(car_1)


"""
The same with help od DESCRIPTOR
"""
class CarDescriptor:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def __get__(self, instance, owner):
        raise AttributeError('Only set')

    def __set__(self, instance, value):
        self.value = value
        with open(self.file_name, 'a') as f:
            f.write(f'Price: {value}, data: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}\n')

    def __delete__(self, instance):
        raise AttributeError('Only set')


class Car:

    def __init__(self, model: str, price: int):
        self.model = model
        self.price = price

    def __str__(self):
        return f"Car: model = {self.model}, price = {self.price}"

    value_price = CarDescriptor('price_descr.txt')

car_1 = Car('Reno', 27_000)
print(car_1)
car_1.value_price = 28_000
print(car_1)