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
In file main.py we run our code
"""

from products import Products
from buyer import Buyer
from order import Order

pr_1 = Products('Banana', 45, 'very sweet')
pr_2 = Products('Orange', 35, 'sweet')
pr_3 = Products('Avocado', 109, 'very ripe')
pr_4 = Products('Cherry', 77, 'sweeter than your girlfriend')

b_1 = Buyer('Pupkin', 'Aleksey', '0343203964')

print('*' * 45)
order = Order('Customer => ', 'Purchases:')
order.cart.append(pr_1)
order.cart.append(pr_3)
order.info_buyer_res.append(b_1)
print(order)
print('*' * 45)

