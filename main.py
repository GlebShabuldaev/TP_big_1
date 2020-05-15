#! ./venv/bin/python3
import pygame
from game.utils.mouse_handler import MouseHandler
from game.utils.keyboard_handler import KeyboardHandler
import argparse
from game.utils.screen_init import init

parser = argparse.ArgumentParser(description='Enter your faction')
parser.add_argument('--faction', type=str, help='Player\'s faction (humans or undead)')
args = parser.parse_args()


def main():
    init()
    keyboard_handler = KeyboardHandler()
    mouse_handler = MouseHandler()
    for event in pygame.event.get():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keyboard_handler.handle(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    mouse_handler.handle(position)
            pygame.display.flip()


if __name__ == "__main__":
    main()
