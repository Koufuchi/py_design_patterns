from __future__ import annotations
from abc import ABC, abstractmethod


class WeaponAbstractFactory(ABC):

    @abstractmethod
    def create_sword(self) -> SwordAbstract:
        pass

    @abstractmethod
    def create_bow(self) -> BowAbstract:
        pass


class Lv10WeaponFactory(WeaponAbstractFactory):

    def create_sword(self) -> SwordAbstract:
        return ConcreteLongsword()

    def create_bow(self) -> BowAbstract:
        return ConcreateHornBow()


class Lv20WeaponFactory(WeaponAbstractFactory):

    def create_sword(self) -> SwordAbstract:
        return ConcreteShortsword()

    def create_bow(self) -> BowAbstract:
        return ConcreateGreatbow()


class SwordAbstract(ABC):
    name: str
    attack_damage: int

    @abstractmethod
    def normal_attack(self) -> str:
        pass


class ConcreteLongsword(SwordAbstract):
    def __init__(self) -> None:
        self.name = "Longsword"
        self.attack_damage = 25

    def normal_attack(self) -> str:
        return f"{self.name} normal attack! dealing {self.attack_damage} damage!"


class ConcreteShortsword(SwordAbstract):
    def __init__(self) -> None:
        self.name = "Shortsword"
        self.attack_damage = 10

    def normal_attack(self) -> str:
        return f"{self.name} normal attack! dealing {self.attack_damage} damage!"


class BowAbstract(ABC):
    name: str
    attack_damage: int

    @abstractmethod
    def normal_attack(self) -> None:
        pass

    @abstractmethod
    def coordinate_attack(self, coordinate: SwordAbstract) -> None:
        pass



class ConcreateHornBow(BowAbstract):
    def __init__(self) -> None:
        self.name = "HornBow"
        self.attack_damage = 75

    def normal_attack(self) -> str:
        return f"{self.name} normal attack! dealing {self.attack_damage} damage!"

    def coordinate_attack(self, coordinate: SwordAbstract) -> str:
        return f"Perform a coordinated attack with a {self.name} and a {coordinate.name}, dealing {self.attack_damage + coordinate.attack_damage} damage."


class ConcreateGreatbow(BowAbstract):
    def __init__(self) -> None:
        self.name = "Greatbow"
        self.attack_damage = 100

    def normal_attack(self) -> str:
        return f"{self.name} normal attack! dealing {self.attack_damage} damage!"

    def coordinate_attack(self, coordinate: SwordAbstract):
        return f"Perform a coordinated attack with a {self.name} and a {coordinate.name}, dealing {self.attack_damage + coordinate.attack_damage} damage."


def run_client_test(factory: WeaponAbstractFactory) -> None:

    product_sword = factory.create_sword()
    product_bow = factory.create_bow()

    print(f"- The sword object created by this factory has the following attributes : \n {vars(product_sword)} \n")
    print(f"- Starting a normal attack with {product_sword.name} : \n {product_sword.normal_attack()} \n")

    print(f"- The bow object created by this factory has the following attributes : \n {vars(product_bow)} \n")
    print(f"- Starting a normal attack with {product_bow.name} : \n {product_bow.normal_attack()} \n")
    print(f"- Starting a coordinate attack : \n {product_bow.coordinate_attack(product_sword)}", end="")


if __name__ == "__main__":

    print("Client: Testing client code with the Lv10WeaponFactory:")
    run_client_test(Lv10WeaponFactory())

    print("\n-----------------------")

    print("Client: Testing the same client code with the Lv20WeaponFactory:")
    run_client_test(Lv20WeaponFactory())