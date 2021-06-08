from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_product_a(self):
        print('Hello')

    @abstractmethod
    def create_product_b(self):
        pass
