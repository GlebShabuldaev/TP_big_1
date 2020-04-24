#! ./venv/bin/python3
import pygame
import sys
from factories.Humans import HumanFaction
from factories.Undead import UndeadFaction
import argparse
import string


parser = argparse.ArgumentParser(description='Enter your faction')
parser.add_argument('faction', type=str, help='Player\'s faction (humans or undead)')
args = parser.parse_args()


def buy_unit(total_gold, price):
    """Allows buying units"""
    font = pygame.font.Font("font.ttf", 24)
    total_gold -= price
    if total_gold < 0:
        print('You lost\nNo money left')
        sys.exit(0)
    gold = "%s"%('Gold: ' + str(total_gold))
    map = pygame.image.load('images/map1.png')
    screen.blit(map, (0, 0))
    text = font.render(gold, True, (255, 255, 0, 255))
    screen.blit(text, (10, 10))
    return total_gold

def choose_faction(faction):
    '''Returns player's faction'''
    faction = faction.lower()
    if faction == 'humans':
        return HumanFaction()
    elif faction == 'undead':
        return UndeadFaction()
    else:
        print('Unknown faction')
        sys.exit(0)

def get_unit(total_gold, player, image):
    '''Function to place a unit'''
    screen.blit(image, (player.x, player.y))
    return buy_unit(total_gold, player.price)    

def main():
    total_gold = 1000
    faction = choose_faction(args.faction)
    pygame.init()
    global screen
    screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    map = pygame.image.load('images/map.png')
    map = pygame.transform.scale(map, (1366, 768))
    screen.blit(map, (0, 0))
    map = pygame.image.load('images/map1.png')
    screen.blit(map, (0, 0))
    pygame.display.set_caption("A Strategy Game")
    game_over = False
    buy_unit(total_gold, 0)
    args.faction = args.faction.lower()
    for event in pygame.event.get():
        while game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True        
                    if event.key == pygame.K_1:
                        player = faction.create_troop()
                        img_troop = pygame.image.load("images/%s_troop.png"%(args.faction))
                        img_troop = pygame.transform.scale(img_troop, (30, 40))
                        total_gold = get_unit(total_gold, player, img_troop)
                    if event.key == pygame.K_2:
                        player = faction.create_general()
                        img_general = pygame.image.load("images/%s_general.png"%(args.faction))
                        img_general = pygame.transform.scale(img_general, (40, 50))
                        total_gold = get_unit(total_gold, player, img_general)
                    if event.key == pygame.K_3:
                        player = faction.create_squad()
                        img_squad = pygame.image.load("images/%s_squad.png"%(args.faction))
                        img_squad = pygame.transform.scale(img_squad, (70, 60))
                        total_gold = get_unit(total_gold, player, img_squad)
                    if event.key == pygame.K_4:
                        player = faction.create_army()
                        img_army = pygame.image.load("images/%s_army.png"%(args.faction))
                        img_army = pygame.transform.scale(img_army, (100, 80))
                        total_gold = get_unit(total_gold, player, img_army)
            pygame.display.flip()


if __name__ == "__main__":
    main()
