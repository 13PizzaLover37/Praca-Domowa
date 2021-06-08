from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """

    Abstrakcja tworzy interfejs dla części „kontrolnej” dwóch hierarchii
    klasów. Ona zawiera odniesienie(link) do obiektu z hierarchii implementacji i oddaje
    mu całą  pracę.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    Możemy rozszerzyć Abstrakcje bez zmiany klasów Realizacji
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    """
    Realizacja tworzy interfejs dla wszystkich klasów realizacji
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass





class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    

    # ... może coś być dodane

    print(abstraction.operation(), end="")

    # ... może coś być dodane


if __name__ == "__main__":
    
    # testowanie czy wszystko działa poprawnie z implementacją A
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    # testowanie czy wszystko działa poprawnie z implementacją B

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
    # żeby terminal nie zamykał się po skończeniu pracy programu
    input()