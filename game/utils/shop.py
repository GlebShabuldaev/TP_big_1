from game import screen
import pygame
from game.utils.troops_lists import forces_members
total_gold = 1000


class Shop:
    @staticmethod
    def buy_unit(price):
        """Allows buying units"""
        global total_gold
        font = pygame.font.Font("font.ttf", 24)
        if total_gold - price < 0:
            total_gold = 0
        else:
            total_gold -= price
        gold = "%s"%('Gold: ' + str(total_gold))
        map_ = pygame.image.load('game/images/tab.png')
        screen.blit(map_, (0, 0))
        text = font.render(gold, True, (255, 255, 0, 255))
        screen.blit(text, (10, 10))
        return total_gold

    @staticmethod
    def out_of_gold():
        if total_gold == 0 and forces_members() == 0:
            font = pygame.font.Font("font.ttf", 154)
            text = font.render('WASTED', True, (255, 0, 0, 255))
            screen.blit(text, (400, 300))
