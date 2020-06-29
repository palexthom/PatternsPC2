from __future__ import annotations
from abc import ABC, abstractmethod

# Creation du projet dans PyCharm, creation du repository git (local) depuis PC, creation du repository distant et push depuis PC.

class Pizza(ABC):

    name: str = None

    def prepare(self) -> str:
        print("Classe Pizza : je prépare toutes les pizzas de la même façon!")
        print (f"Classe Pizza : je ne connais le type de pizza qu'au runtime (ici : '{self.name}').")
        print("Classe Pizza : Tossing dough...")
        print("Classe Pizza : Adding sauce...")
        print("Classe Pizza : Adding toppings...")

    def bake(self) -> str:
        print("Classe Pizza : Cuisson de la pizza")

    def cut(self) -> str:
        print("Classe Pizza : Découpe de la pizza")

    def box(self) -> str:
        print("Classe Pizza : Emballage de la pizza")

    def getName(self) -> str:
        return self.name


class CheesePizza(Pizza):
    name = "Cheese"


class ClamPizza(Pizza):
    name = "Clam"


class PepperoniPizza(Pizza):
    name = "Pepperoni"


class VeggiePizza(Pizza):
    name = "Pepperoni"


class SimplePizzaFactory(ABC):
    pizza: Pizza = None

    def createPizza(self, typePizza: str) -> Pizza:
        print(f"Factory : c'est moi qui crée la pizza.")
        print(f"Factory : on m'a passé en param le type de pizza (ici : '{typePizza}'), c'est celle là que je vais créer et renvoyer à PizzaStore")
        if typePizza == "cheese":
            pizza = CheesePizza()
        elif typePizza == 'pepperoni':
            pizza = PepperoniPizza()
        elif typePizza == 'clam':
            pizza = ClamPizza()
        elif typePizza == 'veggie':
            pizza = VeggiePizza()

        return pizza


class PizzaStore(ABC):
    simpleFactory: SimplePizzaFactory = None

    def __init__(self, factory: SimplePizzaFactory) -> None:
        self.simpleFactory = factory

    def orderPizza(self, typePizza: str):
        print(f"PizzaStore : on m'a commandé une pizza {typePizza}.")
        print(f"PizzaStore : je ne sais pas créer de pizza, je délègue!")
        pizza = self.simpleFactory.createPizza(typePizza)
        print(f"PizzaStore : quelque soit la pizza, je sais la manipuler en faisant appel à ses méthodes.")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


if __name__ == "__main__":
    magasin = PizzaStore(SimplePizzaFactory())
    magasin.orderPizza('cheese')
    magasin.orderPizza('clam')
    magasin.orderPizza('pepperoni')
