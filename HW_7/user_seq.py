# Реализуйте генераторную функцию, которая будет возвращать по одному
# члену числовой последовательности, закон которой задается с помощью
# пользовательской функции. Кроме этого параметром генераторной функции
# должны быть значение первого члена прогрессии и количество выдаваемых
# членов последовательности (n). Генератор должен остановить свою работу
# или по достижению n — го члена, или при передаче команды на завершение.

def gen_func(start, iterations, rule):
    if not isinstance(start, int) or not isinstance(iterations, int):
        raise TypeError('Only integers')
    for i in rule(start, iterations):
        yield i


def rule_of_plus_one(begin, end):
    res = []  # создали пустой список его можно итерировать
    while len(res) < end:
        res.append(begin)
        begin += 1
    return res


def rule_of_sqrt(begin, end):
    res = []
    while len(res) < end:
        res.append(begin ** 2)
        begin += 1
    return res


res = gen_func(1, 10, rule_of_plus_one)
for i in res:
    print(i, end=' ')