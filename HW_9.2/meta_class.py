# Реализуйте метакласс, который обладает следующим функционалом: при
# его использовании в файл с заранее определенным названием нужно
# сохранить имя класса и список его полей.

# 1
class MetaToFile(type):
    def __new__(cls, class_name, super_classes, class_attr):
        field_list = []
        for attr in class_attr:
            field_list.append(attr)
        with open("MetaToFile.txt", "a") as f:
            f.write(f"{class_name}: {field_list}\n")
        return type.__new__(cls, class_name, super_classes, class_attr)


class Cat(metaclass=MetaToFile):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat [name = {self.name}, age = {self.age}]"


# 2
class ToFile(type):

    def __new__(cls, class_name, sper_class, class_attr):
        info = f"Class name: {class_name}\nClass attributes: {class_attr}\n"
        counter = 1
        for attr in class_attr.keys():
            attribute = f"{counter}) {attr} = {class_attr[attr]}\n"
            info += attribute
            counter += 1
        with open('ToFile.txt', 'a') as f:
            f.write(info)


class Cat(metaclass=ToFile):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat [name: {self.name}, age: {self.age}]"
