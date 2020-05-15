from abc import ABC


class Faction(ABC):
    def create_troop(self):
        pass

    def create_general(self):
        pass

    def create_squad(self):
        pass

    def create_army(self):
        pass

    def faction_members(self):
        pass
