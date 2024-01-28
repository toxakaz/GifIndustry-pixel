from abc import ABC, abstractmethod, staticmethod
from enum import Enum


class ColorSpace(Enum):
    RGB = "RGB"
    OKLAB = "OKLAB"


class Color(ABC):
    @abstractmethod
    def color_space(self) -> ColorSpace:
        pass


class ColorRGB(Color):
    def __init__(self, r: int, g: int, b: int) -> None:
        self.coordinates = (r, g, b)

    def __init__(self, coordinates: tuple[int, int, int]) -> None:
        self.coordinates = tuple(coordinates)

    def color_space(self) -> ColorSpace:
        return ColorSpace.RGB


class ColorOKLAB(Color):
    def __init__(self, L: float, a: float, b: float) -> None:
        self.coordinates = (L, a, b)

    def __init__(self, coordinates: tuple[float, float, float]) -> None:
        self.coordinates = coordinates

    def color_space(self) -> ColorSpace:
        return ColorSpace.OKLAB

    @staticmethod
    def from_RGB(source: ColorRGB) -> "ColorOKLAB":

        l = 0.4122214708 * source.coordinates[0] + 0.5363325363 * \
            source.coordinates[1] + 0.0514459929 * source.coordinates[2]
        m = 0.2119034982 * source.coordinates[0] + 0.6806995451 * \
            source.coordinates[1] + 0.1073969566 * source.coordinates[2]
        s = 0.0883024619 * source.coordinates[0] + 0.2817188376 * \
            source.coordinates[1] + 0.6299787005 * source.coordinates[2]

        l_ = l**(1/3)
        m_ = m**(1/3)
        s_ = s**(1/3)

        return ColorOKLAB(
            0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*s_,
            1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*s_,
            0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*s_,
        )

    def to_RGB(self) -> ColorRGB:
        raise NotImplementedError
