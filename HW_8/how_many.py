# Создайте декоратор, который будет подсчитывать, сколько раз была
# вызвана декорируемая функция.

class Calculate:
    count = 0

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        Calculate.count += 1  # возвращаем количество вызовов
        return self.f(*args)  # возвращаем результат суммы

@Calculate
def summa(a, b):
    return a + b

s = summa(2, 3)
s2 = summa(3, 7)
s3 = summa(3, 7)
print(s, s2)
print(Calculate.count)
