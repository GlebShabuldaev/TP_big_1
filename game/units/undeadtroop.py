from game.units.Troop import Troop
import random


class UndeadTroop(Troop):
    def __init__(self):
        super(UndeadTroop, self).__init__()
        self.x = random.randrange(100, 300, 15)
        self.y = random.randrange(250, 650, 20)
        
    def __repr__(self) -> str:
        return 'An undead troop unit with hp: %s, dmg: %s' % (self.hp, self.dmg)
