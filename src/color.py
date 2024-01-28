from abc import ABC, abstractmethod
from enum import Enum


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
    def from_RGB(cls, coordinates: tuple[int, int, int]) -> "ColorRGB":
        r, g, b = coordinates
        return cls(r, g, b)

    @property
    def color_space(self) -> ColorSpace:
        return ColorSpace.RGB


class ColorOKLAB(Color):
    def __init__(self, L: float, a: float, b: float) -> None:
        self.coordinates = (L, a, b)

    @classmethod
    def from_Lab(cls, coordinates: tuple[float, float, float]) -> "ColorOKLAB":
        L, a, b = coordinates
        return cls(L, a, b)

    @classmethod
    def from_ColorRGB(cls, source: ColorRGB) -> "ColorOKLAB":
        return cls.from_RGB(source.coordinates)

    @classmethod
    def from_RGB(cls, source: tuple[int, int, int]):
        r, g, b = source
        l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
        m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
        s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b

        l_ = l**(1/3)
        m_ = m**(1/3)
        s_ = s**(1/3)

        return cls.from_Lab(
            0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*s_,
            1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*s_,
            0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*s_,
        )

    @property
    def color_space(self) -> ColorSpace:
        return ColorSpace.OKLAB

    def to_RGB(self) -> ColorRGB:
        raise NotImplementedError
