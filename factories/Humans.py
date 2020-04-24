from factories.factionfactory import Faction
from units.humanarmy import HumanArmy
from units.humansquad import HumanSquad
from units.humantroop import HumanTroop
from units.humangeneral import HumanGeneral
from units.Army import Army
from units.Troop import Troop
from units.Squad import Squad
from units.General import General
import sys


class HumanFaction(Faction):
    troops_count = 0
    general_count = 0
    army_count = 0
    squad_count = 0

    def create_troop(self) -> Troop:
        self.__class__.troops_count += 1
        return HumanTroop()

    def create_general(self) -> General:
        self.__class__.general_count += 1
        return HumanGeneral()

    def create_squad(self) -> Squad:
        if self.__class__.troops_count >= 5:
            self.__class__.squad_count += 1
            self.__class__.troops_count -= 5
            return HumanSquad()
        else:
            print('Not enough forces to create a squad')
            sys.exit(0)

    def create_army(self) -> Army:
        if self.__class__.squad_count >= 9 and self.__class__.general_count >= 1:
            self.__class__.army_count += 1
            self.__class__.squad_count -= 9
            self.__class__.general_count -= 1
            return HumanArmy()
        else:
            print('Not enough forces to create an army')
            sys.exit(0)

    def faction_members(self) -> str:
        return 'Your current forces are \n troops: %s\n' \
               'generals: %s\n squads: %s\n armies: %s\n' % (self.__class__.troops_count,
                                                             self.__class__.general_count, self.__class__.squad_count,
                                                             self.__class__.army_count)

