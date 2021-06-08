from abstractfactory import AbstractFactory


class ConcreteFactory(AbstractFactory):
    def create_product_a(self):
        super(AbstractFactory, self).create_product_a()
        print('Concrete_factory_2, prod A!')

    def create_product_b(self):
        super(AbstractFactory, self).create_product_b()
        print("Concrete_factory_2, prod B!")