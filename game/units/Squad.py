from game.units.unitsinterface import Units


class Squad(Units):
    def __init__(self):
        self.hp = 1000
        self.dmg = 50
