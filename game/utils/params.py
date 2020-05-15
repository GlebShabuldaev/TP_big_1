import random
from game.utils.troops_lists import army_list, squad_list, troops_list, generals_list
from game.composite.squad_composite import Squad
from game.composite.troop_composite import Troop
from game.composite.army_composite import Army
from game.composite.general_composite import General

params = [
    {
        'path': "game/images/undead_troop.png",
        'zoom_config': (30, 40),
        'unit_position': [random.randrange(200, 300, 15), random.randrange(250, 650, 20)],
        'position': (30, 235),
        'image_side': "game/images/troop.png",
        "num": 0,
        'forces': troops_list,
        'f_type': Troop()
    },
    {
        'path': "game/images/undead_general.png",
        'zoom_config': (40, 50),
        'unit_position': [random.randrange(200, 300, 35), random.randrange(250, 650, 15)],
        'position': (30, 365),
        'image_side': "game/images/gen.png",
        "num": 0,
        'forces': generals_list,
        'f_type': General()
    },
    {
        'path': "game/images/undead_squad.png",
        'zoom_config': (100, 80),
        'unit_position': [random.randrange(200, 300, 35), random.randrange(250, 650, 30)],
        'position': (30, 490),
        'image_side': "game/images/squad.png",
        "num": 0,
        'forces': squad_list,
        'f_type': Squad()
    },
    {
        'path': "game/images/undead_army.png",
        'zoom_config': (200, 150),
        'unit_position': [random.randrange(200, 300, 50), random.randrange(250, 650, 50)],
        'position': (30, 630),
        'image_side': "game/images/army.png",
        "num": 0,
        'forces': army_list,
        'f_type': Army()
    }
]
