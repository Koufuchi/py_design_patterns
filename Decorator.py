class Attack():
    def calc_dmg(self) -> int:
        pass


class ConcreteAttack(Attack):
    _dmg = 10
    def calc_dmg(self) -> int:
        return self._dmg


class Decorator(Attack):
    _dmg: int = 0
    _Attack: Attack = None

    def __init__(self, Attack: Attack) -> None:
        self._Attack = Attack

    @property
    def Attack(self) -> Attack:
        return self._Attack

    def calc_dmg(self) -> int:
        return self._Attack.calc_dmg()


class ConcreteDecoratorHero(Decorator):
    _dmg = 50
    def calc_dmg(self) -> int:
        return self._dmg + self.Attack.calc_dmg()


class ConcreteDecoratorPet(Decorator):
    _dmg = 15
    def calc_dmg(self) -> int:
        return self._dmg + self.Attack.calc_dmg()


def client_code(Attack: Attack) -> int:
    return Attack.calc_dmg()



if __name__ == "__main__":

    normal = ConcreteAttack()
    dmg = client_code(normal)
    print(f"Client: normal attack! dealing {dmg} damage!")
    
    print("\n",
          "Client: Nowadays,",
          "I have become a hero and raised a pet,",
          "so I have an additional attack bonus.")

    with_hero_bonus = ConcreteDecoratorHero(normal)
    with_pet_bonus = ConcreteDecoratorPet(with_hero_bonus)
    dmg = client_code(with_pet_bonus)
    print(f"Client: normal attack with hero and pet bonus! dealing {dmg} damage!")

    print("\n",
          "Client: For even more additional attack bonus,",
          "I've raised another pet.")
    
    with_pet_bonus = ConcreteDecoratorPet(with_pet_bonus)
    dmg = client_code(with_pet_bonus)
    print(f"Client: normal attack with hero and double pet bonus! dealing {dmg} damage!")
