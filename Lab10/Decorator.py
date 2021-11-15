from random import randint
from datetime import datetime


def decorator_example(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        exec_time = (datetime.now() - start).total_seconds()
        print(f"\nВремя выполнения функции {func.__name__} составило: {exec_time} секунд")
        return result
    return wrapper


def my_func(x):
    return sum([randint(50, 100) for i in range(x)])


# прямое декорирование функции
@decorator_example
def my_func2(x):
    return sum([randint(-100, 50) for i in range(x)])


# возвращаем значение функции после обёртки её в декоратор
my_func = decorator_example(my_func)


if __name__ == '__main__':

    print(my_func(10000))
    print(my_func2(10000))
 