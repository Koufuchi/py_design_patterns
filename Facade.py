from __future__ import annotations


class SetCharacterFacade:
    def __init__(self, GenAllySubsystem: GenAllySubsystem, GenEnemySubsystem: GenEnemySubsystem) -> None:
        self._GenAllySubsystem = GenAllySubsystem or GenAllySubsystem()
        self._GenEnemySubsystem = GenEnemySubsystem or GenEnemySubsystem()


    def set_default(self) -> str:
        results = []
        results.append("SetCharacterFacade initializes subsystems:")
        results.append(self._GenAllySubsystem.set_hero(1))
        results.append(self._GenEnemySubsystem.set_dark_lord(1))
        results.append(self._GenAllySubsystem.set_fighter(5))
        results.append(self._GenEnemySubsystem.set_demon(5))
        return "\n".join(results)


class GenAllySubsystem:
    def set_hero(self, number: int=1) -> str:
        return f"GenAllySubsystem: set {number} hero!"


    def set_fighter(self, number: int=1) -> str:
        return f"GenAllySubsystem: set {number} fighter!"


class GenEnemySubsystem:
    def set_dark_lord(self, number: int=1) -> str:
        return f"GenEnemySubsystem: set {number} dark lord!"


    def set_demon(self, number: int=1) -> str:
        return f"GenEnemySubsystem: set {number} demon!"


def client_code(SetCharacterFacade: SetCharacterFacade) -> None:
    print(SetCharacterFacade.set_default(), end="")


if __name__ == "__main__":
    print("At the start of every game,",
          "there will always be a fixed number of basic character configurations.",
          "Therefore, I can use the set_default() method of the SetCharacterFacade to generate them directly.\n")
    genAllySubsystem = GenAllySubsystem()
    genEnemySubsystem = GenEnemySubsystem()
    setCharacterFacade = SetCharacterFacade(genAllySubsystem, genEnemySubsystem)
    client_code(setCharacterFacade)
    
    print("\n")

    print("Besides, I can also directly operate any method of the subsystem to generate characters.\n")
    print(genEnemySubsystem.set_demon(50), end="")