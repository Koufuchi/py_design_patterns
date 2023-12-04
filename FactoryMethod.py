from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def choose_protagonist(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.choose()}"

        return result
    
    def display_introduction(self) -> str:
        product = self.factory_method()
        return f"Creator: The protagonist said '{product.character_introduction()}'"


class ConcreteCreatorHero(Creator):
    def factory_method(self) -> Protagonist:
        return ConcreteHero()


class ConcreteCreatorAssassin(Creator):
    def factory_method(self) -> Protagonist:
        return ConcreteAssassin()



class Protagonist(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    # 當用了 @abstractmethod 宣告，代表他是抽象方法，所有子類別都要實作這個方法。
    @abstractmethod
    def choose(self) -> str:
        pass

    @abstractmethod
    def character_introduction(self) -> str:
        pass


class ConcreteHero(Protagonist):
    def choose(self) -> str:
        return "{Thp player choose to be a hero}"
    
    def character_introduction(self) -> str:
        return "{I am a Heeeeeeeeerooooooooo !!!!!}"


class ConcreteAssassin(Protagonist):
    def choose(self) -> str:
        return "{Thp player choose to be a assassin}"
    
    def character_introduction(self) -> str:
        return "{@$#@$## *$&$&*#  @*(*@(#(*))) !!!!!}"



def client_code(creator: Creator) -> None:
    print("Perform some_operation :")
    print(f"- {creator.choose_protagonist()} \n")
    
    print("Perform character_introduction :")
    print(f"- {creator.display_introduction()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorHero.")
    client_code(ConcreteCreatorHero())
 
    print("\n-----------------------")

    print("App: Launched with the ConcreteCreatorAssassin.")
    client_code(ConcreteCreatorAssassin())