from units.unitsinterface import Units
from abc import abstractmethod

class Squad(Units):
    def __init__(self):
        self.hp = 1000
        self.lvl = 10
        self.dmg = 50
        self.members = 5
        self.price = 50

    def unit_lvl_up(self):
        self.lvl += 1
        self.dmg += 10
        self.hp += 100
        self.members += 1
