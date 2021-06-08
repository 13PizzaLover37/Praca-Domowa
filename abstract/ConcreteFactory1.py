from abstractfactory import AbstractFactory


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        super(ConcreteFactory1, self).create_product_a()
        print("ConcreteFactory1, A!")

    def create_product_b(self):
        super(ConcreteFactory1, self).create_product_b()
        print("ConcreteFactory1, B!")