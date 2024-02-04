from PIL import Image
from figure import Figure, Triangle
from utils import *
import numpy as np
from sklearn.cluster import KMeans
from skimage.filters import sobel
from scipy.spatial import Delaunay
from sklearn.preprocessing import MinMaxScaler
import random


# img - array of {"pixel_num": ("x", "y", "color1, color2, ...")}
def kmeans_points(img: np.ndarray, n_triangles: int) -> np.ndarray:
    scaler = MinMaxScaler()
    scaler.fit(img)
    color_scale = 250
    param_scales = np.array([1, 1]+[color_scale]*3)
    img_t = scaler.transform(img)*param_scales
    clusters = KMeans(n_clusters=n_triangles + 2).fit(img_t).cluster_centers_
    return scaler.inverse_transform(clusters/param_scales)


# actually implement sobel here
def sobel_kmeans_points(img: np.ndarray, n_triangles: int) -> np.ndarray:
    scaler = MinMaxScaler()
    scaler.fit(img)
    color_scale = 250
    param_scales = np.array([1, 1]+[color_scale]*3)
    img_t = scaler.transform(img)*param_scales
    clusters = KMeans(n_clusters=n_triangles + 2).fit(img_t).cluster_centers_
    return scaler.inverse_transform(clusters/param_scales)


def sobel_points(img: np.ndarray, n_points: int) -> tuple[list[tuple[int, int]], dict]:
    mag = np.sum(np.power(sobel(img[:, :, i]), 2) for i in range(img.shape[2]))
    mag_norm = mag / mag.sum()
    points = random.choices(
        [i[::-1] for i in np.ndindex(img.shape[:2])],
        k=n_points,
        weights=mag_norm.flat
    )
    return (points, dict())


def square_grid(img: np.ndarray, n_points: int) -> tuple[list[tuple[int, int]], dict]:
    x, y = img.shape[:2]
    freq = np.sqrt(n_points/(x*y))
    x_p, y_p = int(x*freq), int(y*freq)
    return (np.array([(j/(y_p-1)*y, i/(x_p-1)*x) for i in range(x_p) for j in range(y_p)]).astype(int), dict())


def build_triangles_delaunay(points: np.ndarray):
    return points[Delaunay(points).simplices]


def raster_triangles(triangles: np.ndarray, memoization=False):
    return [raster_triangle(triangle, memoization) for triangle in triangles]


def raster_triangle(triangle: np.ndarray, memoization=False):
    min_xy = np.min(triangle, axis=0)

    points = raster_triangle_norm(triangle - min_xy, memoization=memoization)

    return (triangle, points + min_xy)


@memoize(False)
def raster_triangle_norm(triangle: np.ndarray):
    max_xy = np.max(triangle, axis=0)

    poly = to_polygon(triangle)
    points = list(np.ndindex(tuple(max_xy)))

    points = np.array(points)[[
        polygon_contains_xy(poly, p)
        for p in points
    ]]

    if 0 not in points.shape:
        points = np.concatenate((triangle, points))
    else:
        points = triangle

    return points
