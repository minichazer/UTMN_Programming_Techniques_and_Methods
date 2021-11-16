class Facade():

    def __init__(self, subclass1, subclass2):
        self._subclass1 = subclass1
        self._subclass2 = subclass2
        self._func_collection1 = [func for func in dir(self._subclass1) if callable(getattr(self._subclass1, func)) and not func.startswith("__")]
        self._func_collection2 = [func for func in dir(self._subclass2) if callable(getattr(self._subclass2, func)) and not func.startswith("__")]
    
    def show_functionality(self):
        print(f"Доступные для вызова из фасада методы других классов: {self._func_collection1 + self._func_collection2}")

    def invoke_funcs(self):
        for i in self._func_collection1:
            eval(f"self._subclass1.{i}()")
        for i in self._func_collection2:
            eval(f"self._subclass2.{i}()")

    def invoke_func(self, func):
        if func in self._func_collection1:
            eval(f"self._subclass1.{func}()")
        elif func in self._func_collection2:
            eval(f"self._subclass2.{func}()")
        else:
            print(f"Функции {func} нет в фасаде.")
        

class Cat():

    def meow(self):
        print("Meow")

    def purr(self):
        print("Purr")


class Dog():

    def bark(self):
        print("Bark")

    def wag(self):
        print("*wagging its tail*")


if __name__ == "__main__":
    cat = Cat()
    dog = Dog()
    facade = Facade(cat, dog)

    facade.show_functionality()
    facade.invoke_funcs()
    facade.invoke_func('meow')
    facade.invoke_func('meowbark')
