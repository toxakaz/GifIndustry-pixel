from PIL import Image
from figure import Figure, Triangle
from utils import *
import numpy as np
from sklearn.cluster import KMeans
from skimage.filters import sobel
from scipy.spatial import Delaunay
from sklearn.preprocessing import MinMaxScaler, normalize
from shapely import contains_xy, prepare
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


def sobel_points(img: np.ndarray, n_points: int) -> tuple[tuple[int, int], dict]:
    mag = np.sum(np.power(sobel(img[:, :, i]), 2) for i in range(img.shape[2]))
    mag_norm = mag / mag.sum()
    points = random.choices(
        [i[::-1] for i in np.ndindex(img.shape[:2])],
        k=n_points,
        weights=mag_norm.flat
    )
    return (points, dict())


def build_triangles_delaunay(points: np.ndarray):
    return points[Delaunay(points).simplices]


def raster_triangles(triangles: np.ndarray):
    return [raster_triangle(triangle) for triangle in triangles]


def raster_triangle(triangle: np.ndarray):
    min_xy = np.min(triangle, axis=0)
    max_xy = np.max(triangle, axis=0)

    poly = to_polygon(triangle-min_xy)
    prepare(poly)

    # points = np.array([(x, y) for x in range(min_x, max_x)
    # for y in range(min_y, max_y)])
    points = list(np.ndindex(tuple(max_xy-min_xy)))

    points = np.array(points)[
        np.array([
            contains_xy(poly, p[0], p[1])
            for p in points
        ])
    ]

    if 0 not in points.shape:
        points = np.concatenate((triangle, points + min_xy))
    else:
        points = triangle

    return (triangle, points)
