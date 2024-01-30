from PIL import Image
from figure import Figure, Triangle
from utils import *
import numpy as np
from sklearn.cluster import KMeans
from skimage.filters import sobel
from scipy.spatial import Delaunay
from sklearn.preprocessing import MinMaxScaler


# img - array of {"pixel_num": ("x", "y", "color1, color2, ...")}
def clustering(img: np.ndarray, n_triangles: int) -> np.ndarray:
    scaler = MinMaxScaler()
    scaler.fit(img)
    img_t = scaler.transform(img)
    clusters = KMeans(n_clusters=n_triangles + 2).fit(img_t).cluster_centers_
    return scaler.inverse_transform(clusters)


def build_triangles_delaunay(points: np.ndarray):
    return points[Delaunay(points).simplices]
