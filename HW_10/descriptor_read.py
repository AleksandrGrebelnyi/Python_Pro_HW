# Создайте дескриптор, который будет делать поля класса управляемые им
# доступными только для чтения.

class CatDescriptor:

    """
    description class (settings for reading only)
    name: instance of class Cat
    age: instance of class Cat
    """

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        return instance.name, instance.age

    def __set__(self, instance, value):
        raise AttributeError('Only for reading')

    def __delete__(self, instance):
        raise AttributeError('You can not delete, only reading ')


class Cat:

    """
    Simple class Cat
    check how is working description only for reading
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat: [name: {self.name}, age: {self.age}]"

    value = CatDescriptor()


cat_1 = Cat('Vaska', 14)
print(cat_1)
print(cat_1.value)
# cat_1.value = 11
print(cat_1)