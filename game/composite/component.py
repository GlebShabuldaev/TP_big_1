from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def total_hp(self):
        pass

    @abstractmethod
    def total_number(self):
        pass

    @abstractmethod
    def total_dmg(self):
        pass

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass
