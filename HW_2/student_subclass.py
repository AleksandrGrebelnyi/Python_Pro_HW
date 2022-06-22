from person_superclass import Person


class Student(Person):
    total_students = 0

    def __init__(self, firstname, lastname, age: int):
        super().__init__(firstname, lastname)
        self.age = age
        self.quantity = []
        Student.total_students = 0

    def __str__(self):
        return f'{super().__str__()} - {self.age} years\n\t'







