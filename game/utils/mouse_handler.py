from game.config import *
from game.commands.attack import attack


class MouseHandler:
    def mouse1_pressed(self):
        attack(0)

    def mouse2_pressed(self):
        attack(1)

    def mouse3_pressed(self):
        attack(2)

    def mouse4_pressed(self):
        attack(3)

    def handle(self, position):
        if img_1_borders[0][0] < position[0] < img_1_borders[1][0] and img_1_borders[0][1] < position[1] < img_1_borders[1][1]:
            self.mouse1_pressed()
        elif img_2_borders[0][0] < position[0] < img_2_borders[1][0] and img_2_borders[0][1] < position[1] < img_2_borders[1][1]:
            self.mouse2_pressed()
        elif img_3_borders[0][0] < position[0] < img_3_borders[1][0] and img_3_borders[0][1] < position[1] < img_3_borders[1][1]:
            self.mouse3_pressed()
        elif img_4_borders[0][0] < position[0] < img_4_borders[1][0] and img_4_borders[0][1] < position[1] < img_4_borders[1][1]:
            self.mouse4_pressed()
