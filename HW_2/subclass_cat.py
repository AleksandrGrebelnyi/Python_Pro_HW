from superclass_animal import Animal


class Cat(Animal):

    def __init__(self, age, ration, color, name, character):
        super().__init__(age, ration, color)
        self.name = name
        self.character = character

    def get_voice(self):
        print('Myyaaauuu')

    def __str__(self):
        return f'Cat: {super().__str__()} + {self.name} - {self.character}'

cat_1 = Cat(7, 'birds', 'black', 'Vaska', 'very calm')
print(cat_1)
cat_1.get_voice()
print(Cat.__doc__)