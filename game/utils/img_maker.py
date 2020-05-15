import pygame
from game import screen
from game.config import castle_position, display_settings
from game.utils.params import params


class Renderer:
    @staticmethod
    def draw_forces(forces_num):
        par = params[forces_num]
        num = par['num']
        if num != 0:
            pos = par['unit_position']
            path = par['path']
            x = pos[0]
            y = pos[1]
            zoom = par['zoom_config']
            img = pygame.image.load(path)
            img = pygame.transform.scale(img, zoom)
            map_ = pygame.image.load('game/images/map.png')
            map_ = pygame.transform.scale(map_, display_settings)
            while x < castle_position:
                x += 3
                screen.blit(map_, (0, 0))
                screen.blit(img, (x, y))
                pygame.display.flip()
            screen.blit(map_, (0, 0))

    @staticmethod
    def add_unit(forces_num):
        par = params[forces_num]
        units = par['forces']
        par['num'] = len(units.list)
        num = par['num']
        position = par['position']
        img = par['image_side']
        font = pygame.font.Font("font.ttf", 24)
        count = "%s" % ('Count: ' + str(num))
        map_ = pygame.image.load(img)
        screen.blit(map_, (0, 0))
        text = font.render(count, True, (255, 150, 0, 255))
        screen.blit(text, position)

    def remove_forces(self, forces_num):
        par = params[forces_num]
        units = par['forces']
        units.remove(par['f_type'])
        self.add_unit(forces_num)
