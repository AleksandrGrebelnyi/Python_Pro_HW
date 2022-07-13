# Используя функцию замыкания реализуйте такой прием программирования
# как Мемоизация - https://en.wikipedia.org/wiki/Memoization
# Используйте полученный механизм для ускорения функции рекурсивного
# вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
# просто рекурсивным подходом.
# from datetime import datetime - вариант с датой
import functools  # просто пушечное ускорение из стандартной библиотеки
import time

def fibonachi_memo_close(func):
    mem = {}
    def mem_func(n):
        # 'n': func  итого ключ это n и значение это func
        if n in mem:  # или if mem.get(n):
            return mem[n]
        else:
            mem[n] = func(n)  # здесь мы создаем ключ = значение если его нет в словаре
            return mem[n]
    return mem_func

# @functools.lru_cache()  # просто супер
def fibonachi_recurs(n):
    if n in (1, 2):
        return 1
    return fibonachi_recurs(n - 1) + fibonachi_recurs(n - 2)


start2 = time.time()
res = fibonachi_recurs(35)
print(res, 'Time rec = ', time.time() - start2)

start = time.time()
res2 = fibonachi_memo_close(fibonachi_recurs)
print(res2(35), 'Time memo = ', time.time() - start)
