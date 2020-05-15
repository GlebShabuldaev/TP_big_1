import random
from typing import List

from game.composite.squad_composite import Squad
from game.composite.component import Component


class Army(Component):
    def __init__(self) -> None:
        self.list: List[Squad] = []

    def add(self, squad: Squad) -> None:
        self.list.append(squad)

    def remove(self, squad: Squad) -> None:
        self.list.pop()

    def total_hp(self) -> int:
        res = 0
        for squad in self.list:
            res += squad.total_hp()
        return res

    def total_dmg(self):
        res = 15
        for squad in self.list:
            res += squad.total_dmg()
        return res

    def total_number(self):
        res = 0
        for squad in self.list:
            res += squad.total_number()
        return res

