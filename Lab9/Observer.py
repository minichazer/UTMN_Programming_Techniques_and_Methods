from abc import ABC, abstractmethod
from random import randrange


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class SomethingInterestingToObserve(Subject):

    _state = 0
    _observers = []

    def attach(self, observer):
        print(f"SomethingInteresting: {observer} теперь подписан на меня.")
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        print("SomethingInteresting: оповещаю обсерверов об изменении ...")
        for observer in self._observers:
            observer.update(self)

    def main_code(self):
        print("\nSomethingInteresting: меняю состояние ...")
        self._state = randrange(0, 10)

        print(f"SomethingInteresting: теперь state равен {self._state}")
        self.notify()


class ObserverA(Observer):
    def update(self, subject):
        if subject._state <= 4:
            print("ObserverA: состояние изменилось, оно меньше 4")


class ObserverB(Observer):
    def update(self, subject):
        if subject._state >= 5:
            print("ObserverB: состояние изменилось, оно больше 5")


if __name__ == "__main__":

    subject = SomethingInterestingToObserve()
    observerA = ObserverA()
    observerB = ObserverB()

    subject.attach(observerA)
    subject.attach(observerB)

    subject.main_code()
    subject.main_code()

    subject.detach(observerB)

    subject.main_code()
