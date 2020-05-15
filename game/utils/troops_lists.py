from game.composite.squad_composite import Squad
from game.composite.army_composite import Army
from game.config import squad_members, army_generals, army_squads

troops_list = Squad()
generals_list = Squad()
squad_list = Army()
army_list = Army()


def forces_members():
    members = len(squad_list.list) + len(army_list.list) + troops_list.total_number() + generals_list.total_number()
    return members


def check_squads():
    return troops_list.total_number() >= squad_members


def check_army():
    return len(squad_list.list) >= army_squads and generals_list.total_number() >= army_generals
