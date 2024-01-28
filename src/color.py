from abc import ABC, abstractmethod
from enum import Enum


class ColorSpace(Enum):
    RGB = "RGB"


class Color:
    @abstractmethod
    def color_space(self) -> ColorSpace:
        pass

    @abstractmethod
    def color(self) -> list[float]:
        pass


class ColorRGB(Color):
    def __init__(self, r: int, g: int, b: int) -> None:
        self.color = (r, g, b)

    def __init__(self, color: tuple[int, int, int]):
        self.color = tuple(color)

    def color_space(self) -> str:
        return ColorSpace.RGB

    def color(self) -> list[float]:
        return list(self.color)
