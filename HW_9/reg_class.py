# Создайте декоратор, который зарегистрирует декорируемый класс в
# списке классов.

list_of_class = []


def registration_class(cls):
    list_of_class.append(cls)
    def inclose_func(*args, **kwargs):
        return cls(*args, **kwargs)
    return inclose_func


@registration_class
class Cat:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}"

@registration_class
class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box: x = {self.x}, y = {self.y}, z = {self.z}"


cat_1 = Cat('Vaska', 14)
box_1 = Box(1, 2, 3)
print(cat_1)
print(box_1)
print(list_of_class)



