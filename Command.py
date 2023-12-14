from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class StartHintCommand(Command):
    def __init__(self, stage_no: int) -> None:
        self._stage_no = stage_no

    def execute(self) -> None:
        print(f"StartHintCommand: The stage ({self._stage_no}) is start!")


class SetupBattleFieldCommand(Command):
    def __init__(self, receiver: Receiver, enemy_dict: dict, background: str) -> None:
        self._receiver = receiver
        self._enemy_dict = enemy_dict
        self._background = background

    def execute(self) -> None:
        self._receiver.gen_enemy(self._enemy_dict)
        self._receiver.gne_background(self._background)


class Receiver:
    def gen_enemy(self, enemy_dict: dict) -> None:
        for enemy_name, number in enemy_dict.items(): 
            print(f"\nReceiver: Generating ({number}) ({enemy_name})!", end="")

    def gne_background(self, background: str) -> None:
        print(f"\nReceiver: Set the background to ({background})!")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def start_stage(self, extra_msg: str=None) -> None:
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if (extra_msg):
            print(f"\n{extra_msg}")

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":

    invoker = Invoker()
    invoker.set_on_start(StartHintCommand(1))

    receiver = Receiver()
    invoker.set_on_finish(SetupBattleFieldCommand(
        receiver=receiver, 
        enemy_dict={
            "shark": 1,
            "shrimp": 10,
            "octopus": 3,
        }, 
        background="Ocean"
    ))

    invoker.start_stage("Invoker: Just a notice. The enemy is coming!")