# Создайте декоратор, который зарегистрирует декорируемую функцию в
# списке функций, для обработки последовательности

func_list = []  # список для декорируемых функций


def add_func(f):
    func_list.append(f)

    def func_close(*args):  # замыкающая функция
        return f(*args)
    return func_close

@add_func
def seq_two(seq):
    return [i ** 2 for i in seq]

@add_func
def seq_min_one(seq):
    return [i - 1 for i in seq]

seq = [2, 4, 7]
print(seq_two(seq))
print(seq_min_one(seq))
print(func_list)