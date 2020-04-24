from units.Troop import Troop
import pygame
import random


class HumanTroop(Troop):
    def __init__(self):
        super(HumanTroop, self).__init__()
        self.x = random.randrange(1000, 1300, 20)
        self.y = random.randrange(250, 650, 20)

    def __repr__(self) -> str:
        return 'A humans troop unit with hp: %s, lvl: %s, dmg: %s' % (self.hp, self.lvl, self.dmg)
