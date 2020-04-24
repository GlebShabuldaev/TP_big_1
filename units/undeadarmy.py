import random
import pygame
from units.Army import Army


class UndeadArmy(Army):
    def __init__(self):
        super(UndeadArmy, self).__init__()
        self.x = random.randrange(100, 300, 50)
        self.y = random.randrange(250, 650, 50)
        
    def __repr__(self) -> str:
        return 'An undead army unit with hp: %s, lvl: %s, dmg: %s, members: %s'% (self.hp, self.lvl,
                                                                                 self.dmg, self.members)
