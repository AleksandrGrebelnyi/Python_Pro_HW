class Products:
    """
    Created class Product
    """
    def __init__(self, name, price, descriptions, *args, **kwargs):
        self.name = name
        self.price = price
        self.descriptions = descriptions

    def __str__(self):
        return f'{self.name} - {self.descriptions} - {self.price} UAH'

