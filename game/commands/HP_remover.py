from game import screen
import pygame
from game.utils.params import params
HP = 1000


def deal_damage(num):
    """Deal damage to the castle"""
    par = params[num]
    units = par['forces']
    damage = units.list[0].total_dmg()
    global HP
    if HP - damage <= 0:
        HP = 0
        font = pygame.font.Font("font.ttf", 154)
        text = font.render('VICTORY!', True, (255, 255, 0, 255))
        screen.blit(text, (400, 300))
    else:
        HP -= damage
    health = "%s" % ('HP: ' + str(HP))
    map_ = pygame.image.load('game/images/hp.png')
    screen.blit(map_, (0, 0))
    font = pygame.font.Font("font.ttf", 34)
    text = font.render(health, True, (0, 0, 0, 255))
    screen.blit(text, (1145, 53))
    return health
