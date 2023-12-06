from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_healthy(self) -> None:
        pass

    @abstractmethod
    def set_magic(self) -> None:
        pass

    @abstractmethod
    def set_hunger(self) -> None:
        pass


class ConcreteBuilderGameObject(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = gameObject()

    @property
    def product(self) -> gameObject:
        product = self._product
        self.reset()
        return product

    def set_healthy(self) -> None:
        self._product.add("set_healthy()")

    def set_magic(self) -> None:
        self._product.add("set_magic()")

    def set_hunger(self) -> None:
        self._product.add("set_hunger()")


class gameObject():
    """
    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Process parts: {', '.join(self.parts)}", end="")


class ConcreteBuilderGameHint(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = gameHint()

    @property
    def product(self) -> gameHint:
        product = self._product
        self.reset()
        return product

    def set_healthy(self) -> None:
        self._product.add_str("- The term 'healthy' represents life points.")

    def set_magic(self) -> None:
        self._product.add_str("- The term 'magic' represents Mana.")

    def set_hunger(self) -> None:
        self._product.add_str("- The term 'hunger' represents the hunger level")


class gameHint():
    def __init__(self) -> None:
        self.parts = ''

    def add_str(self, part: Any) -> None:
        self.parts = self.parts + "\n" + part

    def list_parts_str(self) -> None:
        print(f"Process parts: {self.parts}", end="")


class Director:
    """
    The Director is optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_wall(self) -> None:
        self.builder.set_healthy()

    def build_magic_sentinel_device(self) -> None:
        self.builder.set_healthy()
        self.builder.set_magic()

    def build_wizard(self) -> None:
        self.builder.set_healthy()
        self.builder.set_magic()
        self.builder.set_hunger()


if __name__ == "__main__":

    director = Director()
    builder = ConcreteBuilderGameObject()
    director.builder = builder

    print("Build wall : ")
    director.build_wall()
    builder.product.list_parts()

    print("\n")

    print("List parts again without build_wall(): ")
    builder.product.list_parts()

    print("\n")

    print("Build magic sentinel device: ")
    director.build_magic_sentinel_device()
    builder.product.list_parts()

    print("\n")

    print("Build wizard: ")
    director.build_wizard()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Build customize farmer without Director: ")
    builder.set_healthy()
    builder.set_hunger()
    builder.product.list_parts()

    print("\n")

    builder_hint = ConcreteBuilderGameHint()

    print("Build customize game hint with ConcreteBuilderGameHint(): ")
    builder_hint.set_healthy()
    builder_hint.set_hunger()
    builder_hint.product.list_parts_str()