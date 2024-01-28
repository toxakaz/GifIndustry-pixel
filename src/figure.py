from abc import ABC, abstractmethod
from color import Color


class Figure(ABC):
    # dots of figure
    @abstractmethod
    def dots(self) -> list[(int, int)]:
        pass

    # RGB
    @abstractmethod
    def color(self) -> Color:
        pass

    @abstractmethod
    def command(self) -> str:
        pass

    # move the Figure
    @abstractmethod
    def shift(self, x_shift: int, y_shift: int) -> "Figure":
        pass


class Triangle(Figure):
    def __init__(self, dots: ((int, int), (int, int), (int, int)), color: Color) -> None:
        self.dots = tuple(dots)
        self.color = color

    def dots(self) -> list[(int, int)]:
        return list(self.dots)

    def color(self) -> Color:
        return self.color

    def command(self) -> str:
        result = "draw triangle"
        for dot in self.dots:
            result += f" {dot[0]} {dot[1]}"
        return result

    def shift(self, x_shift: int, y_shift: int) -> Figure:
        new_dots = [(dot[0] + x_shift, dot[1] + y_shift) for dot in self.dots]
        return Triangle(new_dots, self.color)
