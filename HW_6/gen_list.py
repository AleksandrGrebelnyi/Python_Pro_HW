# Напишите выражение-генератор для заполнения списка. Список должен
# быть заполнен кубами чисел от 2 и до указанной вами величины.

n = int(input('Input number: '))
cube_list = (x ** 3 for x in range(2, n))

for cube in cube_list:
    print(cube, end=' ')