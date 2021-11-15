class SingletonMeta(type):

    # все сущности, которые имеют ссылку на данный объект
    _instances = {}

    # __call__ вызывается при создании объекта класса, наследующего этот мета-класс 
    # (объект Singleton класса ---> вызов __call__ из мета-класса SingletonMeta)
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # метод super() нужен для получения доступа к методам родительского класса
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def print_self(self):
        print(f"Я - {self}")


if __name__ == "__main__":
    something1 = Singleton()
    something2 = Singleton('meow')

    something1.print_self()
    something2.print_self()