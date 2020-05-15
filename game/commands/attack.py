from __future__ import annotations
from game.commands.command import Command
from game.commands.HP_remover import deal_damage
from game.utils.img_maker import Renderer
from game.utils.params import params
from game.commands.invoker import Invoker


class SimpleCommand(Command):
    def __init__(self, receiver: Receiver, forces_num: int) -> None:
        self._receiver = receiver
        self._num = forces_num

    def execute(self) -> None:
        self._receiver.do_attack(self._num)


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, forces_num: int) -> None:
        self._receiver = receiver
        self._num = forces_num

    def execute(self) -> None:
        self._receiver.do_dmg(self._num)
        self._receiver.remove_unit(self._num)


class Receiver:
    def __init__(self):
        self.rend = Renderer()

    def do_attack(self, forces_num) -> None:
        self.rend.draw_forces(forces_num)

    @staticmethod
    def do_dmg(forces_num) -> None:
        deal_damage(forces_num)

    def remove_unit(self, forces_num):
        self.rend.remove_forces(forces_num)


def attack(forces_num):
    par = params[forces_num]
    if par["num"] > 0:
        invoker = Invoker()
        receiver = Receiver()
        invoker.set_on_start(SimpleCommand(receiver, forces_num))
        invoker.set_on_finish(ComplexCommand(
            receiver, forces_num))
        invoker.do_command()
