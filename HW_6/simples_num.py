#  Напишите функцию-генератор, которая будет возвращать простые числа.
# Верхняя граница этого диапазона должна быть задана параметром этой
# функции

def prime_numbers(stop):
    for i in range(2, stop - 1):
        if i == 1:
            continue
        for j in range(2, i):
            if not i % j:  # если делиться без остатка, тогда брейк и берем следующее число
                break
        else:
            yield i
    return

print(*prime_numbers(100))