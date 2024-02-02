from PIL import Image, ImageDraw
import numpy as np
from triangulate import *
from sklearn.preprocessing import MinMaxScaler
from utils import RGB_to_OKLAB, RGB_img_to_OKLAB
from time import time

import random

img = Image.open("../data/imgs/parrots.webp")

frame = img.copy().convert('RGB')

img_array = np.array(frame, dtype=np.float32)

print(img_array.shape)
print(img_array)

t1 = time()
print(f"start convert")
img_array = RGB_img_to_OKLAB(img_array)
print(f"Stop convert, elapsed: {time()-t1}")

print("pixelating")

pixels = np.array([
    np.concatenate((i, img_array[i]))
    for i in np.ndindex(img_array.shape[:2])
])

print(pixels)

print("clustering")

points = sobel_points(img_array, 512)
triangles = build_triangles_delaunay(np.array(points[0]))
t1 = time()
print(f"start raster")
a = raster_triangles(triangles)
print(f"Stop raster, elapsed: {time()-t1}")
img_draw = ImageDraw.Draw(frame)

for triangle in triangles:
    img_draw.polygon(
        triangle.flatten().tolist(),
        outline=(0, 255, 0),
        width=1
    )

frame.show()
