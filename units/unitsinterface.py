from abc import ABC, abstractmethod
import pygame

class Units(ABC):
    @abstractmethod
    def unit_lvl_up(self):
        pass
