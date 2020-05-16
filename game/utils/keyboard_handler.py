import pygame
import sys
from game.factories.Undead import UndeadFaction
from game.utils.shop import Shop
from game.config import *
from game.utils.troops_lists import check_army, check_squads


class KeyboardHandler:
    faction = UndeadFaction()

    def __init__(self):
        self.shop = Shop()

    def k_1_pressed(self):
        self.shop.out_of_gold()
        if self.shop.buy_unit(troop_price) != 0:
            self.faction.create_troop()

    def k_2_pressed(self):
        self.shop.out_of_gold()
        if self.shop.buy_unit(general_price) != 0:
            self.faction.create_general()

    def k_3_pressed(self):
        self.shop.out_of_gold()
        if check_squads():
            if self.shop.buy_unit(squad_price) != 0:
                self.faction.create_squad()

    def k_4_pressed(self):
        self.shop.out_of_gold()
        if check_army():
            if self.shop.buy_unit(army_price) != 0:
                self.faction.create_army()

    def handle(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)
        if event.key == pygame.K_1:
            self.k_1_pressed()
        if event.key == pygame.K_2:
            self.k_2_pressed()
        if event.key == pygame.K_3:
            self.k_3_pressed()
        if event.key == pygame.K_4:
            self.k_4_pressed()
