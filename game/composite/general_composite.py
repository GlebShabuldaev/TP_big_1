from game.config import *
from game.composite.component import Component
from game.units.undeadgeneral import UndeadGeneral


class General(Component):
    def __init__(self):
        self.unit = UndeadGeneral()

    def total_hp(self) -> int:
        return self.unit.hp

    def total_dmg(self):
        return self.unit.dmg

    def total_number(self):
        return 1
