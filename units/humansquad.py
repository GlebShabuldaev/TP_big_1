from units.Squad import Squad
import random
import pygame


class HumanSquad(Squad):
    def __init__(self):
        super(HumanSquad, self).__init__()
        self.x = random.randrange(1000, 1200, 35)
        self.y = random.randrange(250, 650, 30)

    def __repr__(self) -> str:
        return 'A humans squad unit with hp: %s, lvl: %s, dmg: %s, members: %s' % (self.hp, self.lvl,
                                                                                   self.dmg, self.members)
