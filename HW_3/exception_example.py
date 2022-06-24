# 1) Напишите программу, которая реализует функциональность считывания
# с клавиатуры стоимости товара. При этом стоит учесть, что пользователь
# может ввести не цифры, а смесь цифр и букв или отрицательное число. При
# необходимости создайте пользовательское исключение и обработайте его
# (например, для отрицательных чисел).


class NegativeValueError(Exception):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def __str__(self):
        return 'Input positive number'


while True:
    try:
        number = float(input("Input number: "))
        if number < 0:
            raise NegativeValueError(number)
        break
    except ValueError:
        print('Try again')
    except NegativeValueError as ng:
        print(ng, 'Because you entered: ', ng.number)