# Домашнее задание
# 1) Создайте пользовательский класс для описания товара (предположим,
# это задел для интернет-магазина). В качестве полей товара можете
# использовать значение цены, описание, габариты товара. Создайте пару
# экземпляров вашего класса и протестируйте их работу.
# 2) Создайте класс «Покупатель». В качестве полей можете использовать
# фамилию, имя, отчество, мобильный телефон и т. д.
# 3) Создайте класс «Заказ». Заказ может содержать несколько товаров.
# Заказ должен содержать данные о пользователе, который его осуществил.
# Реализуйте метод вычисления суммарной стоимости заказа. Определите
# метод __str__() для корректного вывода информации об этом заказе.
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
