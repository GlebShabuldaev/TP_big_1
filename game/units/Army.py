from game.units.unitsinterface import Units


class Army(Units):
    def __init__(self):
        self.hp = 5000
        self.dmg = 250
