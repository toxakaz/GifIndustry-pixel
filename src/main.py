from PIL import Image, ImageDraw
import numpy as np
from triangulate import *
from sklearn.preprocessing import MinMaxScaler
from utils import RGB_to_OKLAB, RGB_img_to_OKLAB
from time import time
from figure import Triangle
from drawing import *

import random

img = Image.open("../data/imgs/parrots.webp")

frame = img.copy().convert('RGB')

img_array = np.array(frame, dtype=np.float32)

print(img_array.shape)
print(img_array)

t1 = time()
print(f"start convert")
img_array_OKLAB = RGB_img_to_OKLAB(img_array)
print(f"Stop convert, elapsed: {time()-t1}")

print("pixelating")

pixels = np.array([
    np.concatenate((i, img_array_OKLAB[i]))
    for i in np.ndindex(img_array_OKLAB.shape[:2])
])

print(pixels)

print("clustering")

points = sobel_points(img_array_OKLAB, 512)
triangles = build_triangles_delaunay(np.array(points[0]))
t1 = time()
print(f"start raster")
rasterized_triangles = raster_triangles(triangles)
print(f"Stop raster, elapsed: {time()-t1}")

triangles_colors = [
    (triangle, get_colors(img_array, points))
    for triangle, points in rasterized_triangles
]

triangles_mean_colors = [
    (triangle, np.array(np.mean(colors, axis=0), int))
    for triangle, colors in triangles_colors
]

triangles = [
    Triangle(triangle.flatten().tolist(), tuple(color))
    for triangle, color in triangles_mean_colors
]

draw_figures(frame, triangles)

frame.show()
