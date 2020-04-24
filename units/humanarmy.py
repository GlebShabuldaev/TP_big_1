from units.Army import Army
import pygame
import random


class HumanArmy(Army):
    def __init__(self):
        super(HumanArmy, self).__init__()
        self.x = random.randrange(1000, 1200, 50)
        self.y = random.randrange(250, 650, 40)

    def __repr__(self) -> str:
        return 'A humans army unit with hp: %s, lvl: %s, dmg: %s, members: %s'% (self.hp, self.lvl,
                                                                                 self.dmg, self.members)
