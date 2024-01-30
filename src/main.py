from PIL import Image, ImageDraw
import numpy as np
from triangulate import kmeans_points, build_triangles_delaunay, sobel_points
from sklearn.preprocessing import MinMaxScaler
from utils import RGB_to_OKLAB

import random

img = Image.open("../data/imgs/parrots.webp")
img.convert("RGB")

img_array = np.array(img, dtype=np.float32)

for i in range(img_array.shape[0]):
    for j in range(img_array.shape[1]):
        img_array[i, j] = np.array(RGB_to_OKLAB(img_array[i, j]))


pixels = []

for i in range(img_array.shape[0]):
    for j in range(img_array.shape[1]):
        pixels.append(
            np.array((
                j,
                i,
                img_array[i, j, 0],
                img_array[i, j, 1],
                img_array[i, j, 2]
            ))
        )
pixels = np.array(pixels)
print(pixels)
print("start clustering")

points = sobel_points(img_array, 1024)
triangles = build_triangles_delaunay(np.array(points[0]))
img_draw = ImageDraw.Draw(img)

for triangle in triangles:
    img_draw.polygon(triangle.flatten().tolist(), outline=(
        0, 255, 0), width=1)

img.show()
