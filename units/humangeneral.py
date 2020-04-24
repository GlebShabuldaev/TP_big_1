from units.General import General
import random
import pygame


class HumanGeneral(General):
    def __init__(self):
        super(HumanGeneral, self).__init__()
        self.x = random.randrange(900, 1200, 25)
        self.y = random.randrange(250, 650, 30)

    def __repr__(self) -> str:
        return 'A humans scout unit with hp: %s, lvl: %s, dmg: %s'% (self.hp, self.lvl, self.dmg)
