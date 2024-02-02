import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely import contains_xy, prepare


Dot = tuple[int, int] | tuple[float, float]
Color = tuple[int] | tuple[float]
RGB = tuple[int, int, int] | tuple[float, float, float]
OKLAB = tuple[float, float, float]


def RGB_img_to_OKLAB(img: np.ndarray) -> np.ndarray:
    return np.apply_along_axis(RGB_to_OKLAB, 2, img)


def RGB_to_OKLAB(source: RGB | np.ndarray) -> np.ndarray:
    r, g, b = np.array(source, float)[:3] / 255

    l = np.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b)
    m = np.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b)
    s = np.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b)

    l_ = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    m_ = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    s_ = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s

    return np.array((l_, m_, s_))


def to_point(point: np.ndarray) -> Point:
    return Point(point)


def to_polygon(poly: np.ndarray) -> Polygon:
    poly = Polygon(poly)
    prepare(poly)
    return poly


def polygon_contains_point(poly: Polygon, point: Point) -> bool:
    return poly.contains(point)


def polygon_contains_xy(poly: Polygon, point: tuple) -> bool:
    return contains_xy(poly, point[0], point[1])
