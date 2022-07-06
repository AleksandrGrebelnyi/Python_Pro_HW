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
product_3 = Products('paper', 47, 'very good')
product_4 = Products('avocado', 70, 'good')

client_1 = Buyer('Pupkin', 'Ivan', '93459734597')

order_1 = Order(client_1)
order_1.add_product(product_1, 2)
order_1.add_product(product_2, 1)
order_1.add_product(product_2, 2)
order_1.add_product(product_3, 1)
order_1.add_product(product_4, 2)
print(order_1)

# итерация работает
for prod in order_1:
    print(prod.name)
print('*' * 45)

# по идексу работает
print(order_1[1])
print('*' * 45)

# по срезу работает
prod_slice = order_1[0:]
for prod in prod_slice:
    print(prod)