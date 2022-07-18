# Реализуйте функционал, который будет запрещать установку полей класса
# любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
# попытаться присвоить, например, строку, то должно быть возбужденно
# исключение

class Cat:

    """
    Simple class Cat:
    check how is working functional for all fields of cls
    which allow set only int for all fields of cls.
    """

    def __init__(self, birthday: int, age: int, test: int):
        self.birthday = birthday
        self.age = age
        self.test = test

    def __str__(self):
        return f"Cat: [Year of birth: {self.birthday}, age: {self.age}, test: {self.test}]"

    def __setattr__(self, key, value):
        if not isinstance(value, int):  # key - it's the name of field, value - it's a value of our field
            raise AttributeError('Only integers')
        print(key, value)  # just for me, I checked how it works
        self.__dict__[key] = value

cat_1 = Cat(2017, 5, 4)
print(cat_1)
