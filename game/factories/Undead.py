from game.factories.factionfactory import Faction
from game.composite.squad_composite import Squad
from game.composite.troop_composite import Troop
from game.composite.army_composite import Army
from game.composite.general_composite import General
from game.utils.img_maker import Renderer
from game.config import squad_members, army_squads, army_generals
from game.utils.troops_lists import troops_list, generals_list, squad_list, army_list


class UndeadFaction(Faction):
    def __init__(self):
        self.r = Renderer()

    def create_troop(self) -> Troop:
        troop = Troop()
        troops_list.add(troop)
        self.r.add_unit(0)
        return troop

    def create_general(self) -> General:
        general = General()
        generals_list.add(general)
        self.r.add_unit(1)
        return general

    def create_squad(self) -> Squad:
        if troops_list.total_number() >= squad_members:
            squad = Squad()
            for i in reversed(range(squad_members)):
                squad.add(troops_list.list[i])
                troops_list.remove(Troop())
            squad_list.add(squad)
            self.r.add_unit(2)
            self.r.add_unit(0)
            return squad

    def create_army(self) -> Army:
        if len(squad_list.list) >= army_squads and generals_list.total_number() >= army_generals:
            army = Army()
            for i in reversed(range(army_squads)):
                army.add(squad_list.list[i])
                squad_list.remove(Squad())
            for i in reversed(range(army_generals)):
                army.add(generals_list.list[i])
                generals_list.remove(General())
            army_list.add(army)
            self.r.add_unit(3)
            self.r.add_unit(2)
            self.r.add_unit(1)
            return army
