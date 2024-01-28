from abc import ABC, abstractmethod
from color import Color
from utils import *


class Figure(ABC):
    @property
    @abstractmethod
    def dots(self) -> list[Dot]:
        raise NotImplementedError

    @property
    @abstractmethod
    def color(self) -> Color:
        raise NotImplementedError

    @property
    @abstractmethod
    def command(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def shift(self, x_shift: int, y_shift: int) -> "Figure":
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, dots: tuple[Dot, Dot, Dot], color: Color) -> None:
        self.dots = tuple(dots)
        self.color = color

    @property
    def dots(self) -> list[Dot]:
        return list(self.dots)

    @property
    def color(self) -> Color:
        return self.color

    @property
    def command(self) -> str:
        result = "draw triangle"
        for dot in self.dots:
            result += f" {dot[0]} {dot[1]}"
        return result

    def shift(self, x_shift: int, y_shift: int) -> "Triangle":
        new_dots = [(dot[0] + x_shift, dot[1] + y_shift) for dot in self.dots]
        return Triangle(new_dots, self.color)
