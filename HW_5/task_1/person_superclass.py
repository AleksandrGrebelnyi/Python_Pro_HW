class Person:

    """
    Superclass
    """

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname.strip().title()
        self.lastname = lastname.strip().title()

    def __str__(self):
        return f'{self.lastname}  {self.firstname}'
