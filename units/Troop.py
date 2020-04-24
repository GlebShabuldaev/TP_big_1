from units.unitsinterface import Units
from abc import ABC, abstractmethod


class Troop(Units):
    def __init__(self):
        self.hp = 100
        self.lvl = 5
        self.dmg = 5
        self.price = 5

    def unit_lvl_up(self):
        self.lvl += 1
        self.dmg += 1
        self.hp += 10
