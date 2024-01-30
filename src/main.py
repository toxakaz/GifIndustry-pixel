from PIL import Image, ImageDraw
import numpy as np
from triangulate import clustering, build_triangles_delaunay
from sklearn.preprocessing import MinMaxScaler

img = Image.open("../data/imgs/parrots.webp")
img.convert("RGB")

img_array = np.array(img)
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

clusters = clustering(pixels, 256)

print(clusters)

triangles = build_triangles_delaunay(clusters[:, :2])

print(triangles)

img_draw = ImageDraw.Draw(img)

for triangle in triangles:
    img_draw.polygon(triangle.flatten().tolist(), outline=(0, 255, 0), width=1)

img.show()
