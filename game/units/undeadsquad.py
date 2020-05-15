import random
from game.units.Squad import Squad


class UndeadSquad(Squad):
    def __init__(self):
        super(UndeadSquad, self).__init__()
        self.x = random.randrange(100, 300, 35)
        self.y = random.randrange(250, 650, 30)

    def __repr__(self) -> str:
        return 'An undead squad unit with hp: %s, lvl: %s, dmg: %s, members: %s' % (self.hp, self.lvl,
                                                                                   self.dmg, self.members)
