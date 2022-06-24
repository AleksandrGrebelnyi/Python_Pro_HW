class NegativeNumber(Exception):

    def __init__(self, price, desc):
        self.price = price
        self.desc = desc

    def __str__(self):
        return f'Invalid {self.price} - {self.desc}'

