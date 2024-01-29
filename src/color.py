from abc import ABC, abstractmethod
from enum import Enum
from utils import *


class ColorSpace(Enum):
    RGB = "RGB"
    OKLAB = "OKLAB"


class Color(ABC):
    @property
    @abstractmethod
    def color_space(self) -> ColorSpace:
        pass


class ColorRGB(Color):
    def __init__(self, r: int, g: int, b: int) -> None:
        self.coordinates = (r, g, b)

    @classmethod
    def from_RGB(cls, coordinates: RGB) -> "ColorRGB":
        r, g, b = coordinates
        return cls(r, g, b)

    @property
    def color_space(self) -> ColorSpace:
        return ColorSpace.RGB


class ColorOKLAB(Color):
    def __init__(self, L: float, a: float, b: float) -> None:
        self.coordinates = (L, a, b)

    @classmethod
    def from_Lab(cls, coordinates: OKLAB) -> "ColorOKLAB":
        L, a, b = coordinates
        return cls(L, a, b)

    @classmethod
    def from_ColorRGB(cls, source: ColorRGB) -> "ColorOKLAB":
        return cls.from_RGB(source.coordinates)

    @classmethod
    def from_RGB(cls, source: RGB):
        return cls(RGB_to_OKLAB(source))

    @property
    def color_space(self) -> ColorSpace:
        return ColorSpace.OKLAB

    def to_RGB(self) -> ColorRGB:
        raise NotImplementedError
