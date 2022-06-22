class Person:

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'{self.lastname}  {self.firstname}'