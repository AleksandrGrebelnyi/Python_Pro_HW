# Создайте декоратор с параметрами для проведения хронометража работы
# той или иной функции. Параметрами должны выступать то, сколько раз нужно
# запустить декорируемую функцию и в какой файл сохранить результаты
# хронометража. Цель - провести хронометраж декорируемой функции.

import time


def to_file(reps: int, file_name: str):
    def our_func_decor(f):
        def new_func(*args, **kwargs):
            index = 0
            while index < reps:
                index += 1
                start = time.time()
                result = f(*args, **kwargs)
                end = time.time()
                with open(file_name, 'w') as info:
                    info.writelines(f"Index times: {index}\nResult: {result}\nTime: {end - start}\n")
            return result  # этот return работает в этой позиции и с рекурсивными функциями
        return new_func
    return our_func_decor


@to_file(2, 's1')
def factorial(n):
    if not n:
        return 1
    else:
        return n * factorial(n - 1)


@to_file(2, 's2')
def calc_degree(n):
    return [i ** 3 for i in n]


@to_file(2, 's3')
def calc_plus(a, b):
    return a + b


print(calc_degree([13]))
print(factorial(5))
print(calc_plus(1, 6))
