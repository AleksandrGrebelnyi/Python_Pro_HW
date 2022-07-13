# Напишите функцию, которая применит к списку чисел произвольную
# пользовательскую функцию и вернет суммы элементов полученного списка

def sum_func(n: list, funk):
    if not isinstance(n, list):
        raise ValueError('Only list')
    return sum(funk(n)), funk(n)

def plus_one(n):
    list_plus_one = []
    for i in n:
        list_plus_one.append(i + 1)
    return list_plus_one

def degree_func(n):
    list_degree = []
    for i in n:
        list_degree.append(i ** 2)
    return list_degree


list_number = [3, 5, 44, 90, -2, 73]
res = sum_func(list_number, degree_func)
print(res)