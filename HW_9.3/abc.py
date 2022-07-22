# 1) Создайте ABC класс с абстрактным методом проверки целого числа на
# простоту. Т.е., если параметром этого метода является целое число и оно
# простое, то метод должен вернуть True, а в противном случае False.
# 2) Создайте класс его наследующий.
# 3) Создайте класс, который не наследует пользовательский ABC класс, но
# обладает нужным методом. Зарегистрируйте его в качестве виртуального
# подкласса.
# 4) Проверьте работоспособность проекта.

import abc


class NumberValidatorPrime(abc.ABC):

    @abc.abstractmethod  # 1) класс с абстрактным методом
    def check(self, number):
        pass


class SomeClass(NumberValidatorPrime):  # 2) класс наследующий его
    def __init__(self, number):
        self.number = number

    def check(self, number):
        if not isinstance(number, int):
            raise TypeError('Only integers')
        for i in range(1, number):
            if i == 1:
                continue
            for j in range(2, number):
                if not number % j:
                    return False
                else:
                    return True
        # реализовали обязательный метод check в дочернем классе
        # return super().check(number)  # теперь можно создать объект этого класса, потому что мы реализовали
    # здесь метод check из абстрактного класса


class AnotherClass:  # 3) виртуальный класс

    def check(self, number):  # реализовали обязательный метод check
        if not isinstance(number, int):
            raise TypeError('Only integers')
        for i in range(1, number):
            if i == 1:
                continue
            for j in range(2, number):
                if not number % j:
                    return False
                else:
                    return True

NumberValidatorPrime.register(AnotherClass)  # 3) регистрация класса как виртульного подкласса ABC класса

number_one = AnotherClass()
print(isinstance(number_one, NumberValidatorPrime))

number_two = SomeClass(1)
print(number_two.check(8))

if __name__=='__main__':
    pass
# test from vs code