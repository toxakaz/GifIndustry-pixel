import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


Dot = tuple[int, int] | tuple[float, float]
Color = tuple[int] | tuple[float]
RGB = tuple[int, int, int] | tuple[float, float, float]
OKLAB = tuple[float, float, float]


def RGB_img_to_OKLAB(img: np.ndarray) -> np.ndarray:
    return np.apply_along_axis(RGB_to_OKLAB, 2, img)


def RGB_to_OKLAB(source: RGB | np.ndarray) -> np.ndarray:
    source = np.array(source, dtype=np.float32)

    lms = np.sum(source[:3] / 255 * [
        [0.4122214708, 0.5363325363, 0.0514459929],
        [0.2119034982, 0.6806995451, 0.1073969566],
        [0.0883024619, 0.2817188376, 0.6299787005]
    ], axis=1)

    source[:3] = np.sum(np.cbrt(lms) * [
        [0.2104542553, 0.7936177850, -0.0040720468],
        [1.9779984951, -2.4285922050, 0.4505937099],
        [0.0259040371, 0.7827717662, -0.8086757660]
    ], axis=1)

    return source


def to_point(point: np.ndarray) -> Point:
    return Point(point)


def to_polygon(poly: np.ndarray) -> Polygon:
    return Polygon(poly)


def polygon_contains_point(poly: Polygon, point: Point) -> bool:
    return poly.contains(point)
