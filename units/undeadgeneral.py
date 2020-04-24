import random
import pygame
from units.General import General


class UndeadGeneral(General):
    def __init__(self):
        super(UndeadGeneral, self).__init__()
        self.x = random.randrange(100, 300, 35)
        self.y = random.randrange(250, 650, 15)

    def __repr__(self) -> str:
        return 'An undead scout unit with hp: %s, lvl: %s, dmg: %s' % (self.hp, self.lvl, self.dmg)
