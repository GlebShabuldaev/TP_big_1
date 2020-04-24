from units.unitsinterface import Units
from abc import abstractmethod


class Army(Units):
    def __init__(self):
        self.hp = 5000
        self.lvl = 20
        self.dmg = 250
        self.members = 50
        self.price = 500

    def unit_lvl_up(self):
        self.lvl += 1
        self.dmg += 25
        self.hp += 250
        self.members += 5

