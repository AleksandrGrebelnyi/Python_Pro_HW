from products import Products
from buyer import Buyer


class Order:

    """
    Created class Order and here we construct our methods
    """

    def __init__(self, client, goods, *args, **kwargs):
        self.cart = []
        self.info_buyer_res = []
        self.client = client
        self.goods = goods

    def add_product(self):
        return self.cart.append(Products)

    def info_buyer(self):
        return f"{self.info_buyer_res.append(Buyer)}"

    def calculate_summa_price(self):  # достаем стоимость товара и сразу суммируем
        return sum([getattr(i, 'price') for i in self.cart])

    def __str__(self, *args, **kwargs):
        res = self.client + ' ' + ''.join(map(str, self.info_buyer_res)) + '\n'
        res += self.goods + ' ' + '\n'.join(map(str, self.cart)) + '\n'
        res += 'Total price => ' + str(self.calculate_summa_price()) + ' UAH'
        return res

    def test_commit(self):
        pass


