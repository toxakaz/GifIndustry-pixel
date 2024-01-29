from abc import ABC, abstractmethod
from utils import *
from PIL import Image, ImageDraw


class Figure(ABC):
    @property
    @abstractmethod
    def dots(self) -> tuple[Dot]:
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

    def draw(self, img: Image.Image):
        img_draw = ImageDraw.Draw(img)
        img_draw.polygon(self.dots, fill=self.color, width=0)


class Triangle(Figure):
    def __init__(self, dots: tuple[Dot, Dot, Dot], color: Color) -> None:
        self._dots = dots
        self._color = color

    @property
    def dots(self) -> tuple[Dot]:
        return self._dots

    @property
    def color(self) -> Color:
        return self._color

    @property
    def command(self) -> str:
        result = "draw triangle"
        for dot in self._dots:
            result += f" {dot[0]} {dot[1]}"
        return result

    def shift(self, x_shift: int, y_shift: int) -> "Triangle":
        new_dots = [(dot[0] + x_shift, dot[1] + y_shift) for dot in self.dots]
        return Triangle(new_dots, self.color)
