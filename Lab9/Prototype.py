from abc import ABC, abstractmethod
from datetime import datetime
from random import randint
import copy
import time


# ABC - абстрактные классы в питоне
class Prototype(ABC):

    def __init__(self):

        self.name = None
        self.age = None
        self.height = None
        self.weight = None

    # пустой абстрактный метод для будущего переопределения
    @abstractmethod
    def clone(self):
        pass


class Pupil(Prototype):

    def __init__(self, name, age, height, weight):
        time.sleep(randint(1, 2))
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.privilegues = 10

    # перезаписаем абстрактный метод прототипного класса
    def clone(self):
        return copy.deepcopy(self) 


if __name__ == '__main__':

    total_time = 0
    print("Имитация создания объектов класса Pupil:")
    for i in range(5):
        start = datetime.now()
        pupil = Pupil("Вася", 16, 175, 70)
        nd = (datetime.now() - start).total_seconds()
        print(f"Объект {pupil} был создан за {nd} секунд")
        total_time += nd
    print(f"Завершено создание 5 объектов pupil за {total_time} секунд")

    total_time = 0
    print("Имитация копирования объектов класса Pupil:")
    pupil_c = Pupil("Вася", 16, 175, 70)
    for i in range(50):
        start = datetime.now()
        pupil_clone = pupil_c.clone()
        nd = (datetime.now() - start).total_seconds()
        print(f"Объект {pupil_clone} был создан за {nd} секунд")
        total_time += nd
    print(f"Завершено копирование 50 объектов pupil_clone за {total_time} секунд")
