from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class DiscountSubject(ABC):
    @abstractmethod
    def attach(self, observer: DiscountObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: DiscountObserver) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @abstractmethod
    def get_discount(self) -> int:
        pass

class ConcreteDiscountSubject(DiscountSubject):
    _discount: int = 0
    _observers: List[DiscountObserver] = []

    def attach(self, observer: DiscountObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: DiscountObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def set_discount(self, discount: int) -> None:
        self._discount = discount
        self.notify()

    def get_discount(self) -> int:
        return self._discount

class DiscountObserver(ABC):
    @abstractmethod
    def update(self, subject: DiscountSubject) -> None:
        pass

class Customer(DiscountObserver):
    def update(self, subject: DiscountSubject) -> None:
        discount = subject.get_discount()
        print(f"Customer: Received a {discount}% discount. Time to shop!")

if __name__ == "__main__":
    store = ConcreteDiscountSubject()

    customer1 = Customer()
    customer2 = Customer()

    store.attach(customer1)
    store.attach(customer2)

    store.set_discount(10)
    store.set_discount(20)
    store.set_discount(30)
    store.detach(customer1)  
    store.set_discount(10)
