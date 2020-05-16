from game.units.unitsinterface import Units


class Troop(Units):
    def __init__(self):
        self.hp = 100
        self.dmg = 5
