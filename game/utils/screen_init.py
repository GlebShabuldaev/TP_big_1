from game import screen
import pygame

def load(path):
    map_ = pygame.image.load(path)
    screen.blit(map_, (0, 0))

def init():
    load('game/images/map.png')
    load('game/images/tab.png')
    load('game/images/troop.png')
    load('game/images/gen.png')
    load('game/images/squad.png')
    load('game/images/army.png')
    load('game/images/hp.png')
    font = pygame.font.Font("font.ttf", 24)
    text = font.render('Gold: 1000', True, (255, 255, 0, 255))
    screen.blit(text, (10, 10))
    text = font.render('HP: 1000', True, (0, 0, 0, 255))
    screen.blit(text, (1145, 53))
    text = font.render('Count: 0', True, (255, 150, 0, 255))
    screen.blit(text, (30, 235))
    screen.blit(text, (30, 365))
    screen.blit(text, (30, 490))
    screen.blit(text, (30, 630))
    font = pygame.font.Font("font.ttf", 34)
    text = font.render('Click on unit\'s image to attack the castle!', True, (0, 0, 50, 255))
    screen.blit(text, (300, 660))
    pygame.display.set_caption("A Strategy Game")
