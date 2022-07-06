from buyer import Buyer
from products import Products
from cart_iter import CartIter


class Order:

    """
    Created class Order and here we construct our methods
    """

    def __init__(self, buyer: Buyer):
        self.cart = []
        self.quantity = []
        self.buyer = buyer

    def add_product(self, products: Products, quantity: int | float):
        self.cart.append(products)
        self.quantity.append(quantity)

    def total_price(self):
        total = 0
        for i, item in enumerate(self.cart):
            total += item.price * self.quantity[i]
        return total

    def __str__(self):
        res = f'{self.buyer}\n'
        for i, item in enumerate(self.cart):
            tmp = f'\t{item} UAH * {self.quantity[i]} = {self.quantity[i] * item.price} UAH \n'
            res += tmp
        res += f'Total price: {self.total_price()} UAH'
        return res

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index <= len(self.cart):
                return self.cart[index]
            else:
                raise IndexError

        if isinstance(index, slice):
            slice_cart = []
            start = 0 if index.start is None else index.start
            stop = len(self.cart) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if 0 > index.start and index.stop > len(self.cart):
                raise IndexError
            for i in range(start, stop, step):
                slice_cart.append(self.cart[i])
            return slice_cart
        else:
            raise TypeError

    def __len__(self):
        return self.cart  # может потом попробовать len

    def __iter__(self):
        return CartIter(self.cart)



    # def __init__(self, buyer: Buyer):
    #     self.cart = {}
    #     self.buyer = buyer
    #
    # def add_product(self, products: Products, quantity: int | float):
    #     if self.cart.get(products):
    #         self.cart[products] += quantity
    #     else:
    #         self.cart[products] = quantity
    #
    # def total_price(self):
    #     total = 0
    #     for key, value in self.cart.items():
    #         total += key.price * value
    #     return total
    #
    # def __str__(self):
    #     res = f'{self.buyer}\n'
    #     for key, value in self.cart.items():
    #         tmp = f'\t{key} UAH * {value} = {key.price * value} UAH \n'
    #         res += tmp
    #     res += f'Total price: {self.total_price()} UAH'
    #     return res