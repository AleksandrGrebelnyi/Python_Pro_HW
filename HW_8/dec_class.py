# Предположим, в классе определен метод __str__, который возвращает
# строку на основании класса. Создайте такой декоратор для этого метода,
# чтобы полученная строка сохранялась в текстовый файл, имя которого
# совпадает с именем класса, метод которого вы декорировали.


def decor(f):
    def save_to_file(args):
        with open(args.__class__.__name__ + '.txt', 'a') as info:  # a добавляет значения в файл
            info.writelines(f(args))  # writelines позволяет в новую строку записывать
        return f(args)
    return save_to_file


class Cat:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @decor
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}\n'

cat_1 = Cat('Vaska', 9)
cat_2 = Cat('Stepka', 14)
print(cat_1, cat_2, sep='\n')