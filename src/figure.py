from abc import ABC, abstractmethod
from utils import *
from PIL import Image, ImageDraw


class Figure(ABC):
    @property
    @abstractmethod
    def dots(self) -> list[Dot]:
        raise NotImplementedError

    @property
    @abstractmethod
    def color(self) -> RGB:
        raise NotImplementedError

    @property
    @abstractmethod
    def command(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def shift(self, x_shift: int, y_shift: int) -> "Figure":
        raise NotImplementedError

    def draw(self, img: Image.Image):
        img_draw = ImageDraw.Draw(img)
        img_draw.polygon(self.dots, fill=self.color, width=0)


class Triangle(Figure):
    def __init__(self, dots: tuple[Dot, Dot, Dot], color: RGB) -> None:
        self.dots = tuple(dots)
        self.color = color

    @property
    def dots(self) -> list[Dot]:
        return list(self._dots)

    @dots.setter
    def dots(self, value: list[Dot]):
        self._dots = value

    @property
    def color(self) -> RGB:
        return self._color

    @color.setter
    def color(self, color: RGB):
        self._color = color

    @property
    def command(self) -> str:
        result = "draw triangle"
        for dot in self.dots:
            result += f" {dot[0]} {dot[1]}"
        return result

    def shift(self, x_shift: int, y_shift: int) -> "Triangle":
        new_dots = [(dot[0] + x_shift, dot[1] + y_shift) for dot in self.dots]
        return Triangle(new_dots, self.color)
