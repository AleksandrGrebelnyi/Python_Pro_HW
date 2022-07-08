# Реализуйте свой аналог генераторной функции range(). Да, вы теперь
# знаете, что это - генератор.

def analog_range(start, stop, step):
    while start <= stop:
        yield start
        start += step
    return

for i in analog_range(0, 100, 5):
    print(i, end=' ')
# два варианта вывода инфы
print('\n', *analog_range(0, 100, 5))