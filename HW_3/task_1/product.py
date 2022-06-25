from exception import NegativeNumber

class Products:
    """
    Created class Product
    """
    def __init__(self, name, price, descriptions, *args, **kwargs):
        if price < 0:
            raise NegativeNumber(price)
        self.name = name
        self.descriptions = descriptions
        self.price = price


    def __str__(self):
        return f'{self.name} - {self.descriptions}, {self.price} UAH'