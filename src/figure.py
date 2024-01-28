from abc import ABC, abstractmethod
from utils import *
from color import Color


class Figure(ABC):
    # dots of figure
    @abstractmethod
    def dots(self) -> list[Dot]:
        raise NotImplementedError

    # RGB
    @abstractmethod
    def color(self) -> Color:
        raise NotImplementedError

    @abstractmethod
    def command(self) -> str:
        raise NotImplementedError

    # move the Figure
    @abstractmethod
    def shift(self, x_shift: int, y_shift: int) -> "Figure":
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, dots: tuple[Dot, Dot, Dot], color: Color) -> None:
        self.dots = tuple(dots)
        self.color = color

    def dots(self) -> list[Dot]:
        return list(self.dots)

    def color(self) -> Color:
        return self.color

    def command(self) -> str:
        result = "draw triangle"
        for dot in self.dots:
            result += f" {dot[0]} {dot[1]}"
        return result

    def shift(self, x_shift: int, y_shift: int) -> "Triangle":
        new_dots = [(dot[0] + x_shift, dot[1] + y_shift) for dot in self.dots]
        return Triangle(new_dots, self.color)
