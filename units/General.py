from units.unitsinterface import Units
from abc import abstractmethod


class General(Units):
    def __init__(self):
        self.hp = 150
        self.lvl = 5
        self.dmg = 10
        self.price = 50

    def unit_lvl_up(self):
        self.lvl += 1
        self.dmg += 3
        self.hp += 15

