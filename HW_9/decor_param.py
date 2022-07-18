# Создайте декоратор класса с параметром. Параметром должна быть
# строка, которая должна дописываться (слева) к результату работы метода
# __str__.

def add_string(string: str):
    def class_decor(cls):
        def add_str(*args, **kwargs):
            return string + str(cls(*args, **kwargs))
        return add_str
    return class_decor

@add_string('Here is string from the left side ;) ')
class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box: x = {self.x}, y = {self.y}, z = {self.z}"

@add_string('Class Cat: ')
class Cat:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}"


box_1 = Box(1, 2, 3)
cat_1 = Cat('Vaska', 14)
print(box_1)
print(cat_1)