# 2) Модифицируете класс Заказ (задание Лекции 1) добавив реализацию
# протокола последовательностей и итерационного протокола.
"""
In file main.py we run our code. And for example I added some products and client
"""

from products import Products
from buyer import Buyer
from order import Order

product_1 = Products('apple', 20, 'sweet')
product_2 = Products('banana', 30, 'very good')

client_1 = Buyer('Pupkin', 'Ivan', '93459734597')

order_1 = Order(client_1)
order_1.add_product(product_1, 2)
order_1.add_product(product_2, 1)
order_1.add_product(product_2, 2)
print(order_1)
