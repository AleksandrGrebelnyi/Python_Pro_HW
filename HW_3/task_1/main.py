# 1) Напишите программу, которая реализует функциональность считывания
# с клавиатуры стоимости товара. При этом стоит учесть, что пользователь
# может ввести не цифры, а смесь цифр и букв или отрицательное число. При
# необходимости создайте пользовательское исключение и обработайте его
# (например, для отрицательных чисел).
from exception import NegativeNumber
from product import Products
from buyer import Buyer
from order import Order

if __name__ == '__main__':

    try:
        product_1 = Products('apple', 23, 'sweet')
        product_2 = Products('banana', 34, 'sweet')
    except NegativeNumber as ng:
        print('Your number should not be negative')


    client_1 = Buyer('Pupkin', 'Ivan', '93459734597')

    order_1 = Order(client_1)
    order_1.add_product(product_1, 2)
    order_1.add_product(product_2, 1)
    order_1.add_product(product_2, 2)
    print(order_1)

    print(__name__)