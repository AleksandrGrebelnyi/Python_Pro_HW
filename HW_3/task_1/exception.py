class NegativeNumber(Exception):

    def __init__(self, price):
        super().__init__()
        self.price = price

    def __str__(self):
        return f'Invalid {self.price}'

