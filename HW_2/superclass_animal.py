class Animal:
    def __init__(self, age, ration, color):
        self.age = age
        self.ration = ration
        self.color = color

    def get_voice(self):
        pass

    def __str__(self):
        return f'{self.age} years old - {self.ration} - {self.color}'
