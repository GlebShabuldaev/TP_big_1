import random
from typing import List
from game.composite.component import Component
from game.composite.troop_composite import Troop


class Squad(Component):
    def __init__(self) -> None:
        self.list: List[Troop] = []

    def add(self, troop: Troop) -> None:
        self.list.append(troop)

    def remove(self, troop: Troop) -> None:
        self.list.pop()

    def total_hp(self) -> int:
        res = 0
        for troop in self.list:
            res += troop.total_hp()
        return res

    def total_dmg(self):
        res = 5
        for troop in self.list:
            res += troop.total_dmg()
        return res

    def total_number(self):
        res = 0
        for troop in self.list:
            res += troop.total_number()
        return res
