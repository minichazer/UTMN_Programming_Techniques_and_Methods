from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    # помимо просто создания объекта, мы всегда можем переопределить фабричный метод,
    # и возвращать совсем другой результат (зависит от цели)
    def do_something(self):

        product = self.factory_method()
        result = f"Creator_: класс создателя через фабричный метод получил новый объект {product.operation()}"

        return result


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


# каждый из создателей сам переопределяет фабричный метод, чтобы изменить тип результата 
# сигнатуры разные ---> независимость от конкретных классов Product_
class CreatorA(Creator):
    def factory_method(self):
        print("*имитация какой-то работы CreatorA*")
        return ProductA()


class CreatorB(Creator):
    def factory_method(self):
        print("*имитация какой-то работы CreatorB*")
        return ProductB()


class ProductA(Product):
    def operation(self):
        return "*тут ProductA*"


class ProductB(Product):
    def operation(self):
        return "*тут ProductB*"


# основной код хоть и работает через интерфейс Creator с конкретными Creator_, 
# но благодаря этому мы можем передавать основному коду в качестве
# аргумента любой подкласс создателя (CreatorA, CreatorB)
def main(creator):
    print(f"Основной код: не в курсе про класс создателя, но всё равно могу с ним работать\n"
          f"{creator.do_something()}", end="")


if __name__ == "__main__":

    print("Работаем с CreatorA ...")
    main(CreatorA())
    print("\n")

    print("Работаем с CreatorB ...")
    main(CreatorB())