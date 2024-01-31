from PIL import Image, ImageDraw
import numpy as np
from triangulate import kmeans_points, build_triangles_delaunay, sobel_points
from sklearn.preprocessing import MinMaxScaler
from utils import RGB_to_OKLAB, RGB_img_to_OKLAB

import random

img = Image.open("../data/gifs/earth.gif")

frame = img.copy().convert('RGB')

img_array = np.array(frame, dtype=np.float32)

print(img_array.shape)
print(img_array)

print("converting")

img_array = RGB_img_to_OKLAB(img_array)

print("pixelating")

pixels = np.array([
    np.concatenate((i, img_array[i]))
    for i in np.ndindex(img_array.shape[:2])
])

print(pixels)

print("clustering")

points = sobel_points(img_array, 512)
triangles = build_triangles_delaunay(np.array(points[0]))
img_draw = ImageDraw.Draw(frame)

for triangle in triangles:
    img_draw.polygon(
        triangle.flatten().tolist(),
        outline=(0, 255, 0),
        width=1
    )

frame.show()
